"""Check a Jekyll build for broken local URLs and missing stylesheets.

Usage: python scripts/check_site.py /path/to/jekyll/output
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.stylesheets = []
        self.canonicals = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.stylesheets.append(attrs.get('href', ''))
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonicals.append(attrs.get('href', ''))


def check(build):
    failures = []
    pages = [build / name for name in ('index.html', 'about.html', 'portfolio.html', 'contact.html', '404.html')]
    for path in pages:
        if not path.is_file():
            failures.append(f'Missing page: {path.name}')
            continue
        page = Page()
        page.feed(path.read_text(encoding='utf-8'))
        if not page.stylesheets:
            failures.append(f'{path.name}: no stylesheet')
        for href in page.links:
            url = urlsplit(href)
            if '/https:' in url.path or '/http:' in url.path:
                failures.append(f'{path.name}: domain embedded in path: {href}')
            if url.scheme or url.netloc or not url.path:
                continue
            target = build / unquote(url.path.lstrip('/')) if url.path.startswith('/') else path.parent / unquote(url.path)
            if not any(candidate.is_file() for candidate in (target, target.with_suffix('.html'), target / 'index.html')):
                failures.append(f'{path.name}: missing local target: {href}')
        for href in page.stylesheets:
            target = build / unquote(urlsplit(href).path.lstrip('/'))
            if not target.is_file() or '--blue:' not in target.read_text(encoding='utf-8'):
                failures.append(f'{path.name}: expected portfolio stylesheet not found')
        for canonical in page.canonicals:
            if not canonical.startswith('https://kushbhag.at/'):
                failures.append(f'{path.name}: incorrect canonical: {canonical}')
    if failures:
        raise SystemExit('\n'.join(failures))
    print(f'PASS: {len(pages)} pages, internal links, stylesheet paths, and canonical URLs.')


if __name__ == '__main__':
    check(Path(sys.argv[1]).resolve())
