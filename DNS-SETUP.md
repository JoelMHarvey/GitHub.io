# Pointing joelmharvey.com (apex) at this site

The site is already served by GitHub Pages at **www.joelmharvey.com** (the
`CNAME` file). To make the bare apex `joelmharvey.com` work too, add these
records at your DNS provider:

```
A     @    185.199.108.153
A     @    185.199.109.153
A     @    185.199.110.153
A     @    185.199.111.153
AAAA  @    2606:50c0:8000::153
AAAA  @    2606:50c0:8001::153
AAAA  @    2606:50c0:8002::153
AAAA  @    2606:50c0:8003::153
```

(Keep the existing `www` CNAME record pointing at `joelmharvey.github.io`.)

GitHub then automatically redirects `joelmharvey.com` → `www.joelmharvey.com`
and issues the certificate. Check status in the repo's **Settings → Pages**;
tick "Enforce HTTPS" once the cert is issued.

The Research Hub goes on `research.joelmharvey.com` separately — see
`mens-health-research/DEPLOY.md` in the projects repo (one CNAME record to
Fly.io; doesn't interact with any of the above).

## Mission Control on `ops.joelmharvey.com`

The footer links to the Vercel-generated URL because that is what currently
resolves. To move it to a subdomain: add `ops.joelmharvey.com` under the
Vercel project's **Settings → Domains**, add the CNAME record Vercel gives you
(`cname.vercel-dns.com`), then change the one `href` in `index.html`. Nothing
else on this site depends on it.

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
- `/faresay/` — existing Faresay documents (unchanged; note this repo is
  public, so these are publicly reachable).
- `/writing/` — the writing catalogue.
- Footer → **Mission Control** — the private ops dashboard, hosted on Vercel,
  not part of this site. Password-protected; see above.
