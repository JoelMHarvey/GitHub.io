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

## Site layout

- `/` — homepage (links to Research Hub, GitHub, contact)
- `/lostphone/` — the lost-phone contact card that used to be the homepage.
  **Note:** if your phone's lock screen prints `www.joelmharvey.com`, a
  finder now lands on the homepage — the "Found my phone?" link at the
  bottom takes them to the card, and the contact email is on the homepage
  anyway. If you'd rather keep the card at the root, don't merge this.
- `/faresay/` — existing Faresay documents (unchanged; note this repo is
  public, so these are publicly reachable).
