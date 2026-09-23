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

## Visual price-action playbook

`/playbook/` contains 60 educational theses with synthetic candlestick diagrams, search, family and direction filters, detail pages, source notes, and a pre-trade checklist. Edit the supplied narratives in `content/thesis-library.md` and editorial decision maps / diagram coordinates in `tools/thesis_notes.py`, then run `python3 tools/build_playbook.py`. The generator also updates the sitemap. Styles and search behavior live in `playbook/assets/`.

Run `python3 tests/validate_site.py`, `python3 tests/validate_playbook.py`, and `node tests/search.test.js` before deployment. See `reports/playbook-20260923.md` and `.json` for scope, verification limits, and governance. Classification: operator_display / knowledge_graph; promotion_allowed=false.
