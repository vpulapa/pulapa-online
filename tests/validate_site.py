#!/usr/bin/env python3
"""Focused validation for the Pulapa static site."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "index.html",
    "styles.css",
    "script.js",
    "404.html",
    "CNAME",
    ".nojekyll",
    "robots.txt",
    "sitemap.xml",
    "DEPLOYMENT.md",
    "README.md",
]


class SiteParser(HTMLParser):
    def __init__(self):
      super().__init__()
      self.ids = set()
      self.refs = []

    def handle_starttag(self, tag, attrs):
      attrs = dict(attrs)
      if "id" in attrs:
        self.ids.add(attrs["id"])
      for attr in ("href", "src"):
        value = attrs.get(attr)
        if value:
          self.refs.append((tag, attr, value))


def is_external(value):
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https", "mailto"}


def validate_html_file(path):
    parser = SiteParser()
    parser.feed(path.read_text(encoding="utf-8"))
    errors = []

    for tag, attr, value in parser.refs:
      if value.startswith("#"):
        target = value[1:]
        if target and target not in parser.ids:
          errors.append(f"{path.name}: missing fragment target #{target}")
        continue

      if is_external(value) or value.startswith("/"):
        continue

      target = (path.parent / value.split("#", 1)[0]).resolve()
      if value.split("#", 1)[0] and not target.exists():
        errors.append(f"{path.name}: missing local {attr} target {value}")

      if "#" in value:
        file_part, fragment = value.split("#", 1)
        target_file = (path.parent / file_part).resolve() if file_part else path
        if target_file.exists() and fragment:
          nested = SiteParser()
          nested.feed(target_file.read_text(encoding="utf-8"))
          if fragment not in nested.ids:
            errors.append(f"{path.name}: missing fragment target {value}")

    return errors


def main():
    errors = []

    for rel_path in REQUIRED_FILES:
      if not (ROOT / rel_path).exists():
        errors.append(f"missing required file: {rel_path}")

    cname = ROOT / "CNAME"
    if cname.exists() and cname.read_text(encoding="utf-8").strip() != "pulapa.online":
      errors.append("CNAME must contain exactly pulapa.online")

    for html_name in ("index.html", "404.html"):
      html_path = ROOT / html_name
      if html_path.exists():
        errors.extend(validate_html_file(html_path))

    index = ROOT / "index.html"
    if index.exists():
      text = index.read_text(encoding="utf-8")
      for required_id in ("home", "about", "ai", "research", "projects", "contact"):
        if f'id="{required_id}"' not in text:
          errors.append(f"index.html missing section id: {required_id}")
      if "http://" in text:
        errors.append("index.html contains insecure http:// reference")

    if errors:
      print("Pulapa site validation failed:")
      for error in errors:
        print(f"- {error}")
      raise SystemExit(1)

    print("Pulapa site validation passed.")
    print(f"Checked {len(REQUIRED_FILES)} required files, local links, fragments, CNAME, and HTTPS-safe references.")


if __name__ == "__main__":
    main()
