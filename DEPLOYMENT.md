# Deploying `pulapa.online`

This site is built for a simple GitHub Pages + Cloudflare DNS setup.

## What You Own

You own the domain name `pulapa.online`. The files in this folder are the website. GitHub Pages hosts those files. Cloudflare manages the DNS records that tell browsers where to find the site.

## GitHub Pages

1. Create a GitHub repository for this site.
2. Push this folder's contents to the repository.
3. Go to **Settings > Pages**.
4. Set **Source** to **Deploy from a branch**.
5. Select your default branch and `/(root)`.
6. Set **Custom domain** to `pulapa.online`.
7. Wait for the DNS check to pass.
8. Turn on **Enforce HTTPS** when GitHub makes it available.

## Cloudflare DNS

Add `pulapa.online` to Cloudflare, then update your registrar nameservers to the two Cloudflare nameservers shown in the Cloudflare dashboard.

Recommended initial DNS records:

| Type | Name | Content | Proxy status | Notes |
| --- | --- | --- | --- | --- |
| A | `@` | `185.199.108.153` | DNS only | GitHub Pages IPv4 |
| A | `@` | `185.199.109.153` | DNS only | GitHub Pages IPv4 |
| A | `@` | `185.199.110.153` | DNS only | GitHub Pages IPv4 |
| A | `@` | `185.199.111.153` | DNS only | GitHub Pages IPv4 |
| AAAA | `@` | `2606:50c0:8000::153` | DNS only | GitHub Pages IPv6 |
| AAAA | `@` | `2606:50c0:8001::153` | DNS only | GitHub Pages IPv6 |
| AAAA | `@` | `2606:50c0:8002::153` | DNS only | GitHub Pages IPv6 |
| AAAA | `@` | `2606:50c0:8003::153` | DNS only | GitHub Pages IPv6 |
| CNAME | `www` | `<YOUR_GITHUB_USERNAME>.github.io` | DNS only | Replace with your GitHub username or organization |

Start with DNS-only so GitHub can verify the records clearly. After GitHub Pages shows the custom domain and HTTPS as healthy, you can either leave DNS-only for the simplest setup or switch the web records to proxied if you want Cloudflare caching, analytics, and protection.

Do not add wildcard DNS records like `*.pulapa.online` for this GitHub Pages site.

## Verification Commands

```bash
dig pulapa.online +noall +answer -t A
dig pulapa.online +noall +answer -t AAAA
dig www.pulapa.online +nostats +nocomments +nocmd
```

Expected result: the apex returns GitHub Pages A and AAAA records, and `www` points to your GitHub Pages default domain.

## Optional Cloudflare Email

If you want `hello@pulapa.online` to receive email, enable Cloudflare Email Routing and forward it to your real inbox.

## Official References

- GitHub Pages custom domains: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- GitHub Pages publishing source: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- Cloudflare domain onboarding: https://developers.cloudflare.com/fundamentals/manage-domains/add-site/
- Cloudflare proxy status: https://developers.cloudflare.com/dns/proxy-status/
