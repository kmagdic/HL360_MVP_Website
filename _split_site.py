#!/usr/bin/env python3
"""
Splits FlexQ-Website-v3_8.html into a proper multi-page site:
  css/site.css, js/site.js,
  index.html, therapists.html, enterprise.html, privacy.html, team.html
"""
import os, re

with open('FlexQ-Website-v3_8.html', 'r', encoding='utf-8') as f:
    src = f.read()

lines = src.split('\n')

# ─────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────
def slice_lines(start, end):
    """1-based inclusive line range → joined string."""
    return '\n'.join(lines[start-1:end])

os.makedirs('css', exist_ok=True)
os.makedirs('js',  exist_ok=True)

# ─────────────────────────────────────────────────────────
# 1. CSS  →  css/site.css
# ─────────────────────────────────────────────────────────
css_raw = re.search(r'<style>(.*?)</style>', src, re.DOTALL).group(1)

with open('css/site.css', 'w', encoding='utf-8') as f:
    f.write(css_raw.strip() + '\n')
print('✓ css/site.css')

# ─────────────────────────────────────────────────────────
# 2. JS  →  js/site.js
# ─────────────────────────────────────────────────────────
js_raw = re.search(r'<script>(.*?)</script>', src, re.DOTALL).group(1)

# Replace showPage() with real navigation + keep as wrapper
nav_wrapper = """
// ── Navigation ──
function showPage(name) {
  var map = {
    landing:'index.html', therapists:'therapists.html',
    enterprise:'enterprise.html', privacy:'privacy.html', team:'team.html'
  };
  location.href = map[name] || 'index.html';
}

// Mark active nav link based on current URL
function initNav() {
  var file = location.pathname.split('/').pop() || 'index.html';
  var map = {
    'index.html':'landing', '':'landing',
    'therapists.html':'therapists',
    'enterprise.html':'enterprise',
    'privacy.html':'privacy',
    'team.html':'team'
  };
  var page = map[file] || 'landing';
  var el = document.getElementById('nav-' + page);
  if (el) el.classList.add('active');
}
"""

# Remove the old showPage from the extracted JS
js_raw = re.sub(
    r'function showPage\(name\)\{.*?\}',
    '',
    js_raw,
    flags=re.DOTALL
)

# Inject nav wrapper before translations block
js_raw = nav_wrapper + js_raw

# Replace the auto-init at the bottom: call initNav() too
js_raw = js_raw.replace(
    'setLang(currentLang);',
    'initNav();\nsetLang(currentLang);'
)

# Fix ham menu toggle (references showPage in mobile)
js_raw = js_raw.replace(
    "if(ham){ham.classList.remove('open');nl.classList.remove('open')}",
    "if(ham){ham.classList.remove('open');nl.classList.remove('open')}"
)

with open('js/site.js', 'w', encoding='utf-8') as f:
    f.write(js_raw.strip() + '\n')
print('✓ js/site.js')

# ─────────────────────────────────────────────────────────
# 3. Shared fragments
# ─────────────────────────────────────────────────────────
FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300;1,6..72,400&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet">'''

# Extract the current nav HTML and update onclick → href
nav_raw = re.search(r'<nav>(.*?)</nav>', src, re.DOTALL).group(0)

# Convert nav links to href (remove onclick, add href)
nav_raw = nav_raw.replace(
    'class="active" onclick="showPage(\'landing\')" data-i18n="nav.home">Home</a>',
    'href="index.html" data-i18n="nav.home">Home</a>'
)
nav_raw = nav_raw.replace(
    'id="nav-therapists" onclick="showPage(\'therapists\')" data-i18n="nav.therapists">For therapists</a>',
    'id="nav-therapists" href="therapists.html" data-i18n="nav.therapists">For therapists</a>'
)
nav_raw = nav_raw.replace(
    'id="nav-enterprise" onclick="showPage(\'enterprise\')" data-i18n="nav.enterprise">For enterprises</a>',
    'id="nav-enterprise" href="enterprise.html" data-i18n="nav.enterprise">For enterprises</a>'
)
# Logo → link to index
nav_raw = nav_raw.replace(
    '<div class="logo" onclick="showPage(\'landing\')">',
    '<div class="logo" onclick="location.href=\'index.html\'" style="cursor:pointer">'
)
# Remove the stray id="nav-landing" class="active" on the first link (class set by JS now)
nav_raw = nav_raw.replace(
    '<a id="nav-landing"',
    '<a id="nav-landing" class=""'
)

# Extract lightbox HTML
lb_raw = re.search(
    r'<!-- ════ LIGHTBOX ════ -->(.*?)(?=\n<script>)',
    src, re.DOTALL
).group(0).strip()

# Extract cookie banner HTML + fix Privacy policy link
cookie_raw = re.search(
    r'<!-- ════ COOKIE CONSENT BANNER ════ -->(.*?)(?=\n<!-- ════ LIGHTBOX)',
    src, re.DOTALL
).group(0).strip()
# Update privacy link in cookie banner to href
cookie_raw = re.sub(
    r"onclick=\"showPage\('privacy'\)\"",
    'href="privacy.html"',
    cookie_raw
)

# ─────────────────────────────────────────────────────────
# 4. Page content extraction (inner HTML of each page div)
# ─────────────────────────────────────────────────────────
def extract_page(page_id, start_line, end_line):
    """Extract content between <div id='page-X'> and its closing </div>."""
    chunk = slice_lines(start_line, end_line)
    # Remove the outer wrapper div
    chunk = re.sub(
        rf'<div id="page-{page_id}" class="page[^"]*">\s*',
        '',
        chunk,
        count=1
    )
    # Remove trailing </div> (the wrapper's closing tag)
    chunk = chunk.rstrip()
    if chunk.endswith('</div>'):
        chunk = chunk[:-6].rstrip()
    return chunk

landing_content    = extract_page('landing',    346, 476)
therapists_content = extract_page('therapists', 479, 569)
enterprise_content = extract_page('enterprise', 572, 616)
privacy_content    = extract_page('privacy',    619, 800)
team_content       = extract_page('team',       803, 944)

# Fix remaining showPage() calls in footer links → use href
def fix_footer_links(html):
    html = re.sub(
        r'onclick="showPage\(\'privacy\'\)" style="cursor:pointer"',
        'href="privacy.html"',
        html
    )
    html = re.sub(
        r'onclick="showPage\(\'team\'\)" style="cursor:pointer"',
        'href="team.html"',
        html
    )
    html = re.sub(
        r'onclick="showPage\(\'landing\'\)" style="cursor:pointer"',
        'href="index.html"',
        html
    )
    return html

landing_content    = fix_footer_links(landing_content)
therapists_content = fix_footer_links(therapists_content)
enterprise_content = fix_footer_links(enterprise_content)
privacy_content    = fix_footer_links(privacy_content)
team_content       = fix_footer_links(team_content)

# ─────────────────────────────────────────────────────────
# 5. HTML template builder
# ─────────────────────────────────────────────────────────
def make_html(title, description, content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
{FONTS}
<link rel="stylesheet" href="css/site.css">
</head>
<body>

{nav_raw}

{content.strip()}

{cookie_raw}

{lb_raw}

<script src="js/site.js"></script>
</body>
</html>
"""

# ─────────────────────────────────────────────────────────
# 6. Write HTML files
# ─────────────────────────────────────────────────────────
pages = [
    ('index.html',       'FlexQ — Intervention before escalation',
     'FlexQ is the continuous layer between therapy sessions — turning daily signals into early warning so therapists act before a crisis.',
     landing_content),
    ('therapists.html',  'FlexQ — For therapists',
     'Walk into every session already oriented. FlexQ shows what changed, why it matters, and the rule that flagged it — in 90 seconds.',
     therapists_content),
    ('enterprise.html',  'FlexQ — For enterprises',
     'A leading indicator of workforce mental strain — not a wellness app. Aggregate signal, anonymised by design.',
     enterprise_content),
    ('privacy.html',     'FlexQ — Privacy policy',
     'FlexQ Health privacy policy. GDPR and AZOP compliant.',
     privacy_content),
    ('team.html',        'FlexQ — The team',
     'Meet the team behind FlexQ. Built with clinicians, not just for them.',
     team_content),
]

for filename, title, desc, content in pages:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(make_html(title, desc, content))
    print(f'✓ {filename}')

print('\nDone. Files created:')
print('  css/site.css, js/site.js')
print('  index.html, therapists.html, enterprise.html, privacy.html, team.html')
