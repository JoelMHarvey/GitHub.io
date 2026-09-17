# joelmharvey.com — how the domain reaches this site

**Done, not a to-do.** The apex `joelmharvey.com` is the live name: it is what
the `CNAME` file holds and what GitHub Pages serves. These are the records
behind it, for reference if the domain ever has to be rebuilt:

```
A     @    185.199.108.153
A     @    185.199.109.153
A     @    185.199.110.153
A     @    185.199.111.153
AAAA  @    2606:50c0:8000::153
AAAA  @    2606:50c0:8001::153
AAAA  @    2606:50c0:8002::153
AAAA  @    2606:50c0:8003::153
CNAME www  joelmharvey.github.io
```

The `www` record stays: GitHub answers `www.joelmharvey.com` with a 301 to the
apex, so both names work and only one is canonical. HTTPS is enforced in
**Settings → Pages**.

## If the site starts 404ing

A 404 from `server: GitHub.com` on a domain whose settings all look correct
means Pages has the domain but no published deployment. The usual cause:

> **Making this repo private takes the site down, and making it public again
> does not bring it back.** Pages on a free plan is a public-repo feature, so
> going private unpublishes the site; going public again restores the settings
> — source branch, custom domain, DNS check, the `CNAME` file, even the
> www → apex redirect — but *not* the deployment. Everything reads green and
> the apex still serves GitHub's stock "There isn't a GitHub Pages site here."
> (That is what the "Visibility / GitHub Enterprise" panel on the Pages
> settings page is advertising: private-repo Pages is the paid tier.)

The fix is to make Pages build again, which a visibility change does not do on
its own. Re-run the most recent **pages build and deployment** run in
[Actions](../../actions), or in **Settings → Pages** switch the branch to
anything else, Save, switch back to `master` / `(root)`, Save. One green run
and the site is back. Two things to know while doing it: only one Pages
deployment can be in flight at a time (a second is refused with *"due to in
progress deployment"* — just re-run it after the first finishes), and whichever
branch is selected when a build fires is the branch that goes live, so put the
selector back on `master` before you walk away.

To tell this apart from a DNS problem without leaving the terminal:

```bash
curl -sSI https://joelmharvey.com/ | head -3
```

`server: GitHub.com` with a 404 is the case above. Anything else answering, or
no answer at all, is DNS or the registrar, not Pages.

The Research Hub goes on `research.joelmharvey.com` separately — see
`mens-health-research/DEPLOY.md` in the projects repo (one CNAME record to
Fly.io; doesn't interact with any of the above).

## Mission Control on `ops.joelmharvey.com`

The **Ops** section on the homepage links to `ops.joelmharvey.com`. That name
is the Mission Control Vercel project (`ops`, generated URL
`ops-theta-black.vercel.app`) with the domain added under **Settings →
Domains** and one record at the DNS provider:

```
CNAME  ops   cname.vercel-dns.com
```

Same shape as every other subdomain here. If the name ever stops resolving, the
generated URL still answers; the Claude Code task-board hook in the projects
repo (`ops/hooks/mc-sync.py`) falls back to it on its own. Nothing else on
this site depends on it.

### Every subdomain this site links to

All of them are Vercel projects in the `projects` repo (except `research`,
which is Fly.io), each one `CNAME <name> → cname.vercel-dns.com` at the DNS
provider *and* the domain added under the Vercel project's **Settings →
Domains**. Both halves are needed; one without the other is a dead link.

| Name | Project | Linked from |
|---|---|---|
| `research` | mens-health-research (Fly.io) | Research & writing |
| `quire` | quire | Research & writing |
| `nihongo` | nihongo | Daily |
| `eigo` | eigo | Daily |
| `tradeflow` | tradeflow | Ventures |
| `ops` | ops | Ops |
| `listen` | listening | Ops |
| `outreach` | outreach | Ops |

Before adding a link to this site, check the name actually resolves:

```bash
getent hosts eigo.joelmharvey.com || echo "no DNS — do not link it yet"
```

The link is `rel="nofollow"`, which asks crawlers not to follow it — it does
not stop them, and it does nothing about anyone reading the page source. This
repo is public, so treat that URL as public knowledge. What actually protects
the dashboard is `OPS_PASSWORD` on the Vercel project; the app refuses to
start without it (`ops/test_auth.py` in the projects repo pins that), so a
misconfigured deployment returns 500 rather than serving the cost model.

## Site layout

- `/` — homepage (links to Research Hub, GitHub, contact)
- `/lostphone/` — the lost-phone contact card that used to be the homepage.
  **Note:** if your phone's lock screen prints `www.joelmharvey.com`, a
  finder now lands on the homepage — the "Found my phone?" link at the
  bottom takes them to the card, and the contact email is on the homepage
  anyway. If you'd rather keep the card at the root, don't merge this.
- `/writing/` — the writing catalogue.
- `/italian/` — Forza Italiano!, the A1 grammar drill app. Self-contained
  static page; progress is kept in the visitor's own localStorage, so there is
  no account, no server and nothing to sign in to.
- **Daily** section — the two language-game sites are not hosted here:
  **日本語ゲーム** (`nihongo.joelmharvey.com`, Japanese for English speakers)
  and **英語ゲーム** (`eigo.joelmharvey.com`, its mirror image — English for
  Japanese speakers, interface in Japanese). Both want an account, so both
  links are `rel="nofollow"` like the Ops ones.
- **Ops** section — the private tools, hosted on Vercel, not part of this
  site, each behind its own login: **Mission Control** (see above),
  **Listening Post** (`listen.joelmharvey.com`) and **Outreach**
  (`outreach.joelmharvey.com`). All three live in the `projects` repo.
