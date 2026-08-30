/* Tokyo Today's headlines.
 *
 * The feeds live behind shinyashimada.com/api/news, so the API is stubbed
 * here: what is under test is this page's half of the deal — that it asks for
 * each language separately, that it reads the shape the endpoint actually
 * returns, and that the English column is English.
 *
 * That last one is the bug this test exists for. The page used to read a
 * single mixed bundle from the research hub and split it by key; when the
 * split went wrong, Japanese headlines appeared under "News — English".
 *
 * Run:  node tests/tokyo.mjs        (with a static server on :8901)
 */
import { chromium } from 'playwright';

const BASE = process.env.BASE || 'http://127.0.0.1:8901';
const browser = await chromium.launch();

const JA = [
  { title: '東京で今年最高の暑さ', link: 'https://www3.nhk.or.jp/news/a',
    source: 'NHK ニュース', publishedAt: '2026-08-30T04:15:00+09:00' },
  { title: '台風１０号、週末に上陸か', link: 'https://www.asahi.com/b',
    source: '朝日新聞', publishedAt: '2026-08-30T02:00:00+09:00' }
];
const EN = [
  { title: 'Tokyo posts its hottest day of the year', link: 'https://www3.nhk.or.jp/nhkworld/en/news/a',
    source: 'NHK World-Japan', publishedAt: '2026-08-30T04:20:00+09:00' },
  { title: 'Typhoon No. 10 may make landfall at the weekend', link: 'https://www.japantimes.co.jp/b?a=1&b=2',
    source: 'The Japan Times', publishedAt: '2026-08-30T02:10:00+09:00' }
];

const fails = [];
const t = async (name, fn) => {
  try { const r = await fn(); if (r !== true) fails.push(`${name}: ${r}`); }
  catch (e) { fails.push(`${name}: threw ${e.message}`); }
};

/**
 * Opens the page with /api/news answered by `answer(lang)`, which returns
 * either a body to serve as 200 or a status number to fail with.
 */
async function open(answer) {
  const ctx = await browser.newContext();
  const page = await ctx.newPage();
  const errs = [];
  const asked = [];
  page.on('pageerror', (e) => errs.push(e.message));
  page.on('console', (m) => { if (m.type() === 'error') errs.push(m.text()); });

  await page.addInitScript(() => {
    localStorage.setItem('jmh_gate', 'ed05301a98dd6a6b78a2fb3b599ced7a33312336c2cf24fdc6195df1cffdb04c');
  });

  // The weather half has its own upstream; keep it out of the way.
  await page.route('**/api.open-meteo.com/**', (r) => r.fulfill({
    status: 200, contentType: 'application/json', body: JSON.stringify({
      current: { temperature_2m: 31, relative_humidity_2m: 70, apparent_temperature: 35,
        weather_code: 3, wind_speed_10m: 9 },
      daily: { time: ['2026-08-30'], weather_code: [3], temperature_2m_max: [33],
        temperature_2m_min: [26], precipitation_probability_max: [20],
        sunrise: ['2026-08-30T05:10'], sunset: ['2026-08-30T18:12'] }
    })
  }));

  await page.route('**/shinyashimada.com/api/news*', (r) => {
    const lang = new URL(r.request().url()).searchParams.get('lang');
    asked.push(lang);
    const res = answer(lang);
    if (typeof res === 'number') return r.fulfill({ status: res, contentType: 'application/json',
      body: JSON.stringify({ ok: false, error: 'nope' }) });
    r.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify(res) });
  });

  await page.goto(`${BASE}/tokyo/`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(500);
  return { page, ctx, errs, asked };
}

/* --- the ordinary day ----------------------------------------------------- */

const ok = (lang) => ({ ok: true, lang, fallbackFrom: null,
  fetchedAt: '2026-08-30T04:30:00+09:00',
  sources: lang === 'ja' ? ['NHK ニュース', '朝日新聞'] : ['NHK World-Japan', 'The Japan Times'],
  items: lang === 'ja' ? JA : EN });

let { page, ctx, errs, asked } = await open(ok);

await t('it asks for each language separately', async () =>
  asked.slice().sort().join(',') === 'en,ja' ? true : `asked for [${asked.join(', ')}]`);

await t('the Japanese column carries the Japanese headlines', async () => {
  const txt = await page.textContent('#news-jp');
  return txt.includes('東京で今年最高の暑さ') && txt.includes('台風１０号、週末に上陸か')
    ? true : `got "${txt.trim().slice(0, 80)}"`;
});

await t('the English column carries the English headlines', async () => {
  const txt = await page.textContent('#news-en');
  return txt.includes('Tokyo posts its hottest day of the year')
    ? true : `got "${txt.trim().slice(0, 80)}"`;
});

// The bug, stated directly.
await t('no Japanese headline appears under News — English', async () => {
  const txt = await page.textContent('#news-en');
  const cjk = txt.match(/[぀-ヿ一-鿿]/g) || [];
  return cjk.length === 0 ? true : `English column contains ${cjk.length} Japanese characters`;
});

await t('each headline links to its own story', async () => {
  const href = await page.getAttribute('#news-en li:first-child a', 'href');
  return href === EN[0].link ? true : href;
});

await t('a link with query parameters survives escaping', async () => {
  const href = await page.getAttribute('#news-en li:nth-child(2) a', 'href');
  return href === EN[1].link ? true : href;
});

// publishedAt, not published: reading the wrong field is silent, it just
// leaves every timestamp blank.
await t('the published time is rendered in JST', async () => {
  const time = await page.textContent('#news-en li:first-child time');
  return /^NHK World-Japan · 30 Aug, 04:20$/.test(time.trim())
    ? true : `time read "${time}"`;
});

await t('no fallback note on an ordinary day', async () =>
  !(await page.isVisible('#note-jp')) ? true : 'note shown when nothing fell back');

await t('the page raised no errors', async () =>
  errs.length === 0 ? true : errs.join(' | '));

await ctx.close();

/* --- the Japanese feeds are down ------------------------------------------ */

({ page, ctx, errs, asked } = await open((lang) =>
  lang === 'ja'
    ? { ok: true, lang: 'ja', fallbackFrom: 'en', fetchedAt: '2026-08-30T04:30:00+09:00',
        sources: ['NHK World-Japan'], items: EN }
    : ok('en')));

await t('a fallback to the English wire is admitted, not hidden', async () => {
  if (!(await page.isVisible('#note-jp'))) return 'no note shown';
  const txt = await page.textContent('#note-jp');
  return /Japanese feeds unavailable/.test(txt) ? true : `note read "${txt}"`;
});

await ctx.close();

/* --- one language fails outright ------------------------------------------ */

({ page, ctx, errs, asked } = await open((lang) => (lang === 'ja' ? 502 : ok('en'))));

await t('a failed language says so rather than sitting on "Loading…"', async () => {
  const txt = (await page.textContent('#news-jp')).trim();
  return /No headlines right now|Headlines unavailable/.test(txt) ? true : `read "${txt}"`;
});

await t('the other language is unaffected by it', async () => {
  const txt = await page.textContent('#news-en');
  return txt.includes('Tokyo posts its hottest day of the year') ? true : `read "${txt.trim().slice(0, 60)}"`;
});

await ctx.close();
await browser.close();

console.log(`\ntokyo: ${fails.length ? 'FAILED' : 'passed'}`);
if (fails.length) fails.forEach((f) => console.error('  ✗ ' + f));
process.exit(fails.length ? 1 : 0);
