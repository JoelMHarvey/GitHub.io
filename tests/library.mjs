/* The joelmharvey.com view of the shared library.
 *
 * The API it talks to lives on shinyashimada.com, so every call is stubbed
 * here: what is under test is this page's handling of the passcode gate, the
 * cross-origin round trip and the editing loop — not the backend, which has
 * its own tests in the other repository.
 *
 * Run:  node tests/library.mjs        (with a static server on :8901)
 */
import { chromium } from 'playwright';

const BASE = process.env.BASE || 'http://127.0.0.1:8901';
const browser = await chromium.launch();
const ctx = await browser.newContext();
const page = await ctx.newPage();

const errs = [];
page.on('pageerror', e => errs.push(e.message));
page.on('console', m => {
  if (m.type() === 'error' && !/status of (401|503)/.test(m.text())) errs.push(m.text());
});

// The site password gate would block the page; unlock it up front.
await page.addInitScript(() => {
  localStorage.setItem('jmh_gate', 'ed05301a98dd6a6b78a2fb3b599ced7a33312336c2cf24fdc6195df1cffdb04c');
});

/* --- the stubbed backend ------------------------------------------------- */

const GOOD = 'let-me-in';
let server = [
  { id: 'b1', title: 'Bagombo Snuff Box', authors: ['Kurt Vonnegut'], owner: 'joel',
    status: 'read', rating: 4, publisher: 'Putnam', publishedYear: 1999, pages: 295,
    description: 'Twenty-three short stories written for the magazines of the 1950s.',
    location: 'Bookcase 1 – Shelf 1', createdAt: '2026-08-01T00:00:00.000Z',
    updatedAt: '2026-08-01T00:00:00.000Z' },
  { id: 'b2', title: 'Hedro', owner: 'joel', confidence: 'low',
    location: 'Bookcase 1 – Shelf 5', createdAt: '2026-08-02T00:00:00.000Z',
    updatedAt: '2026-08-02T00:00:00.000Z' }
];
let posted = [];
let sawPasscodeHeader = null;

await page.route('https://shinyashimada.com/api/**', async route => {
  const req = route.request();
  const url = new URL(req.url());
  const given = req.headers()['x-store-passcode'];

  if (req.method() === 'OPTIONS') return route.fulfill({ status: 204 });

  if (url.pathname === '/api/store' && url.searchParams.has('health')) {
    return route.fulfill({ status: 200, contentType: 'application/json',
      body: JSON.stringify({ ok: true, database: true, authRequired: true }) });
  }

  if (given !== GOOD) {
    return route.fulfill({ status: 401, contentType: 'application/json',
      body: JSON.stringify({ error: 'Passcode required.', code: 'unauthorized' }) });
  }
  sawPasscodeHeader = given;

  if (url.pathname === '/api/store' && req.method() === 'GET') {
    return route.fulfill({ status: 200, contentType: 'application/json',
      body: JSON.stringify({ records: server }) });
  }
  if (url.pathname === '/api/store' && req.method() === 'POST') {
    const body = JSON.parse(req.postData() || '{}');
    posted.push(body);
    (body.records || []).forEach(r => {
      const i = server.findIndex(s => s.id === r.id);
      if (i === -1) server.push(r); else server[i] = r;
    });
    return route.fulfill({ status: 200, contentType: 'application/json',
      body: JSON.stringify({ ok: true, written: (body.records || []).length }) });
  }
  if (url.pathname === '/api/books') {
    const q = (url.searchParams.get('q') || '').toLowerCase();
    const hit = /bagombo|vonnegut/.test(q)
      ? { title: 'Bagombo Snuff Box', authors: ['Kurt Vonnegut'], publisher: 'Putnam',
          publishedYear: 1999, description: 'Twenty-three short stories.', isbn13: '9780399144509' }
      : { title: 'Something Else Entirely', authors: ['Not The Author'], publisher: 'Wrong Press',
          publishedYear: 1234, description: 'Must never be written to a record.' };
    return route.fulfill({ status: 200, contentType: 'application/json',
      body: JSON.stringify({ results: [hit] }) });
  }
  return route.fulfill({ status: 404, body: '{}' });
});

/* ------------------------------------------------------------------------- */

const fails = [];
const t = async (name, fn) => {
  try { const r = await fn(); if (r !== true) fails.push(`${name}: ${r}`); }
  catch (e) { fails.push(`${name}: threw ${e.message}`); }
};

await page.goto(`${BASE}/library/`, { waitUntil: 'networkidle' });
await page.waitForTimeout(500);

/* --- the gate ------------------------------------------------------------ */

await t('asks for the passcode first', async () =>
  await page.isVisible('#gate') && !(await page.isVisible('#app')) ? true : 'app shown unlocked');

await page.fill('#gate-input', 'wrong-one');
await page.click('#gate-form button');
await page.waitForTimeout(600);
await t('a wrong passcode is refused', async () =>
  await page.isVisible('#gate') ? true : 'let in with the wrong passcode');
await t('and says so', async () =>
  (await page.textContent('#gate-msg')).includes('not accepted') ? true : await page.textContent('#gate-msg'));

await page.fill('#gate-input', GOOD);
await page.click('#gate-form button');
await page.waitForTimeout(800);

await t('the right passcode opens the library', async () =>
  await page.isVisible('#app') ? true : 'still locked');
await t('the passcode travelled as a header', async () =>
  sawPasscodeHeader === GOOD ? true : `header was ${sawPasscodeHeader}`);

/* --- what came back ------------------------------------------------------ */

await t("the other site's records are shown", async () => {
  const n = await page.locator('.book').count();
  return n === 2 ? true : `${n} cards`;
});
await t('a title from the shared shelf is there', async () =>
  (await page.textContent('#grid')).includes('Bagombo Snuff Box') ? true : 'missing');
await t('the low-confidence row is flagged', async () =>
  (await page.locator('.chip.check').count()) === 1 ? true : 'no check chip');
await t('stats are computed', async () =>
  (await page.textContent('#stats')).includes('2') ? true : 'stats blank');
await t('the shelf filter picked up both shelves', async () => {
  const n = await page.locator('#f-shelf option').count();
  return n === 3 ? true : `${n} options`;
});

/* --- the description gap ------------------------------------------------- */
// One of the two has a blurb; the other is the gap.

await t('the no-description filter appears with a count', async () => {
  if (await page.isHidden('#f-nodesc')) return 'filter hidden while a book has no description';
  const label = (await page.textContent('#f-nodesc')).replace(/\s+/g, ' ').trim();
  return label.includes('(1)') ? true : `label read "${label}"`;
});

await t('the described book shows a snippet on its card', async () => {
  const n = await page.locator('.book .desc').count();
  if (n !== 1) return `${n} snippets for 1 described book`;
  return (await page.textContent('.book .desc')).includes('Twenty-three short stories')
    ? true : await page.textContent('.book .desc');
});

await page.click('#f-nodesc');
await page.waitForTimeout(400);
await t('filtering to it leaves only the undescribed one', async () => {
  const n = await page.locator('.book').count();
  if (n !== 1) return `${n} shown`;
  return (await page.textContent('.book')).includes('Hedro') ? true : await page.textContent('.book');
});
await page.click('#f-nodesc');
await page.waitForTimeout(400);

await t('turning the filter off brings the shelf back', async () =>
  (await page.locator('.book').count()) === 2 ? true : 'shelf did not come back');

/* --- editing writes back ------------------------------------------------- */

posted = [];
await page.locator('.book', { hasText: 'Bagombo' }).click();
await page.waitForTimeout(400);
await t('detail opens', async () => await page.isVisible('#detail') ? true : 'not open');
await t('detail shows the publisher', async () =>
  (await page.textContent('#d-body')).includes('Putnam') ? true : 'publisher missing');

await page.click('#d-edit');
await page.waitForTimeout(400);
await page.fill('#e-notes', 'Read on the Chuo line.');
await page.click('#ed-form button[type=submit]');
await page.waitForTimeout(700);

await t('the edit was pushed to the shared store', async () =>
  posted.length === 1 && posted[0].collection === 'books' ? true : JSON.stringify(posted));
await t('and carried the note', async () =>
  (posted[0].records[0].notes || '').includes('Chuo') ? true : 'note missing from the payload');
await t('the server copy now has it', async () =>
  (server.find(b => b.id === 'b1').notes || '').includes('Chuo') ? true : 'server not updated');

/* --- adding a book through the lookup ------------------------------------ */

posted = [];
await page.click('#add-book');
await page.waitForTimeout(300);
await page.fill('#look-input', 'bagombo vonnegut');
await page.click('#look-go');
await page.waitForTimeout(600);
await t('the lookup returns a hit', async () =>
  (await page.locator('.hit').count()) === 1 ? true : 'no hits');
await page.locator('.hit [data-use]').click();
await page.waitForTimeout(300);
await t('the hit fills the title', async () =>
  (await page.inputValue('#e-title')) === 'Bagombo Snuff Box' ? true : await page.inputValue('#e-title'));
await t('and the ISBN', async () =>
  (await page.inputValue('#e-isbn')) === '9780399144509' ? true : 'isbn missing');
await page.selectOption('#e-owner', 'shin');
await page.click('#ed-form button[type=submit]');
await page.waitForTimeout(700);
await t('the new book was saved', async () => {
  const n = await page.locator('.book').count();
  return n === 3 ? true : `${n} cards`;
});

/* --- lent-to only when lent ---------------------------------------------- */

await page.locator('.book').first().click();
await page.waitForTimeout(350);
await page.click('#d-edit');
await page.waitForTimeout(350);
await t('lent-to is hidden while not lent', async () =>
  !(await page.isVisible('#lentto-wrap')) ? true : 'shown too early');
await page.selectOption('#e-status', 'lent');
await page.waitForTimeout(200);
await t('lent-to appears when lent', async () =>
  await page.isVisible('#lentto-wrap') ? true : 'still hidden');
await page.click('#editor [data-close]');
await page.waitForTimeout(250);

/* --- bulk fill respects the title guard ---------------------------------- */

posted = [];
await page.click('#bulk-go');
await page.waitForTimeout(2600);
if (await page.isVisible('#bulk')) { await page.click('#bulk-go'); await page.waitForTimeout(700); }

await t('the misread row did not take a wrong book', async () => {
  const bad = await page.evaluate(() =>
    JSON.parse(localStorage.getItem('jmh.library.cache') || '[]')
      .filter(b => b.publisher === 'Wrong Press').length);
  return bad === 0 ? true : `${bad} records took it`;
});
await t('nothing was invented', async () => {
  const bad = await page.evaluate(() =>
    JSON.parse(localStorage.getItem('jmh.library.cache') || '[]')
      .filter(b => b.publishedYear === 1234).length);
  return bad === 0 ? true : `${bad} records`;
});

/* --- the cache survives a reload ----------------------------------------- */

await page.reload({ waitUntil: 'networkidle' });
await page.waitForTimeout(800);
await t('a remembered passcode skips the gate', async () =>
  await page.isVisible('#app') ? true : 'asked again');
await t('the shelf is still there after a reload', async () =>
  (await page.locator('.book').count()) >= 3 ? true : 'books lost');


/* --- an empty shelf must say WHY it is empty ----------------------------- */

async function emptyCase(label, routeFn, expect) {
  const c = await browser.newContext();
  const pg = await c.newPage();
  await pg.addInitScript(() => {
    localStorage.setItem('jmh_gate', 'ed05301a98dd6a6b78a2fb3b599ced7a33312336c2cf24fdc6195df1cffdb04c');
    localStorage.setItem('jmh.library.passcode', JSON.stringify('let-me-in'));
    localStorage.removeItem('jmh.library.cache');
  });
  await routeFn(pg);
  await pg.goto(`${BASE}/library/`, { waitUntil: 'networkidle' });
  await pg.waitForTimeout(900);
  const txt = (await pg.textContent('#empty').catch(() => '')) || '';
  const appShown = !(await pg.locator('#app').getAttribute('hidden').catch(()=>'x')) ;
  await t(label, async () => txt.includes(expect) ? true : `saw ${JSON.stringify(txt.replace(/\s+/g,' ').trim().slice(0,110))}`);
  await c.close();
}

// The server answers but holds nothing — say so, and point at the likely cause.
await emptyCase('an empty server says the shared shelf is empty', async pg => {
  await pg.route('https://shinyashimada.com/api/**', r => {
    const u = new URL(r.request().url());
    if (u.searchParams.has('health')) return r.fulfill({ status:200, contentType:'application/json',
      body: JSON.stringify({ ok:true, database:true, authRequired:true }) });
    return r.fulfill({ status:200, contentType:'application/json', body: JSON.stringify({ records: [] }) });
  });
}, 'shared shelf is empty');

// The read failed — never render that as "no books".
await emptyCase('a failed read says the read failed', async pg => {
  await pg.route('https://shinyashimada.com/api/**', r => {
    const u = new URL(r.request().url());
    if (u.searchParams.has('health')) return r.fulfill({ status:200, contentType:'application/json',
      body: JSON.stringify({ ok:true, database:true, authRequired:true }) });
    return r.abort('failed');
  });
}, 'Could not read the shelf');

// No passcode required, but the read still fails — the branch that used to
// swallow the error entirely and show a bare empty shelf.
await emptyCase('an open server with a failing read still explains itself', async pg => {
  await pg.route('https://shinyashimada.com/api/**', r => {
    const u = new URL(r.request().url());
    if (u.searchParams.has('health')) return r.fulfill({ status:200, contentType:'application/json',
      body: JSON.stringify({ ok:true, database:true, authRequired:false }) });
    return r.abort('failed');
  });
}, 'Could not read the shelf');

/* ------------------------------------------------------------------------- */

if (errs.length) fails.push('console/page errors: ' + errs.join(' | '));
console.log(`\njmh-library: ${fails.length ? 'FAILED' : 'passed'}`);
if (fails.length) fails.forEach(f => console.error('  ✗ ' + f));
await browser.close();
process.exit(fails.length ? 1 : 0);
