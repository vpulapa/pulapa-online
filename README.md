# Pulapa

Static personal site for `pulapa.online`, designed to publish directly with GitHub Pages and use Cloudflare for DNS.

## Local Preview

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000` from this directory.

## Publish With GitHub Pages

1. Create a new GitHub repository for the site.
2. Push the contents of this folder to the repository default branch.
3. In GitHub, open **Settings > Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Choose the default branch and `/(root)` as the source.
6. Under **Custom domain**, enter `pulapa.online`.
7. Enable **Enforce HTTPS** once GitHub says it is available.

GitHub Pages expects an `index.html` at the publishing source root. This site includes that entry file, plus `CNAME` and `.nojekyll`.

## Governance

- Task classification: `operator_display`
- Allowed-state mapping: `raw_source -> interpreted_doctrine -> admitted_component` does not apply because this is a public website, not a trading runtime component.
- Runtime trading impact: none
- Promotion allowed: `false`
- Governance status: website-only artifact; no strategy, ML trade creation, runtime rule, or source-blocked rule is introduced.

## Reports

- Human-readable report: `reports/pulapa_website_setup_report.md`
- Machine-readable artifact: `reports/pulapa_website_setup.json`
- Focused validation: `python3 tests/validate_site.py`
