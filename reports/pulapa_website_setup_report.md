# Pulapa Website Setup Report

Date: 2026-07-21

## Summary

Built a first static website for `pulapa.online` that can be published directly from a GitHub Pages repository root and managed through Cloudflare DNS.

## Task Classification

`operator_display`

This is a public-facing personal and project website. It is not a Genesis runtime rule, not a trading strategy, not an ML trading system, and not a promotion pathway.

## Produced Artifacts

- Website files: `index.html`, `styles.css`, `script.js`, `404.html`
- GitHub Pages domain files: `CNAME`, `.nojekyll`
- Search/discovery files: `robots.txt`, `sitemap.xml`
- Human-readable deployment guide: `DEPLOYMENT.md`
- Focused validation script: `tests/validate_site.py`
- Machine-readable governance artifact: `reports/pulapa_website_setup.json`

## Focused Tests

Run:

```bash
python3 tests/validate_site.py
```

The test checks required files, the `CNAME` value, local links, fragment targets, required sections, and insecure local references.

Result: passed on 2026-07-21.

## Governance Status

- Governance status: website-only artifact
- Trading runtime impact: none
- ML trade creation: none
- Blocked or quarantined strategy family impact: none
- Promotion allowed: `false`

## Deployment Status

Local files are ready for GitHub Pages.

Publish attempt on 2026-07-21:

- GitHub CLI was not installed in this environment.
- Chrome was later signed in to GitHub by the owner.
- Repository created: `https://github.com/vpulapa/pulapa-online`
- Initial commit pushed: `54a31031e57d8f576270060a67cd89980fac7c3c`
- GitHub Pages enabled from `main` / `/(root)`.
- GitHub Pages workflow completed successfully.
- GitHub reports the site live at `http://pulapa.online/`.

Cloudflare and registrar update on 2026-07-21:

- Cloudflare zone created for `pulapa.online` on the Free plan.
- Cloudflare DNS records configured for GitHub Pages:
  - `A pulapa.online -> 185.199.108.153`
  - `A pulapa.online -> 185.199.109.153`
  - `A pulapa.online -> 185.199.110.153`
  - `A pulapa.online -> 185.199.111.153`
  - `AAAA pulapa.online -> 2606:50c0:8000::153`
  - `AAAA pulapa.online -> 2606:50c0:8001::153`
  - `AAAA pulapa.online -> 2606:50c0:8002::153`
  - `AAAA pulapa.online -> 2606:50c0:8003::153`
  - `CNAME www -> vpulapa.github.io`
- Web records were left as DNS only during GitHub Pages verification.
- Existing Namecheap email-forwarding MX records and SPF TXT record were preserved in Cloudflare.
- Namecheap nameservers were changed from `dns1.registrar-servers.com` and `dns2.registrar-servers.com` to:
  - `joel.ns.cloudflare.com`
  - `virginia.ns.cloudflare.com`
- Cloudflare activation status: waiting for registrar propagation.
- Direct DNS queries to Cloudflare's assigned nameservers confirmed the GitHub Pages A, AAAA, and `www` CNAME records.
- DNSSEC check returned no DS record, so DNSSEC is not expected to block activation.

HTTPS enablement on 2026-07-21:

- Public DNS now delegates to `joel.ns.cloudflare.com` and `virginia.ns.cloudflare.com`.
- GitHub Pages DNS check is successful.
- GitHub issued a Let's Encrypt certificate for `pulapa.online` and `www.pulapa.online`.
- GitHub Pages Enforce HTTPS is enabled.
- `http://pulapa.online/` redirects to `https://pulapa.online/`.
- `https://pulapa.online/` returns `200 OK`.
- `http://www.pulapa.online/` redirects through the apex and resolves to `https://pulapa.online/`.

Remaining account-specific setup:

- None for HTTPS. Cloudflare proxy remains DNS-only while GitHub Pages owns certificate enforcement.
