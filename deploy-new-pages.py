#!/usr/bin/env python3
"""
Deploy all NEW pages (Négoce, IA, Implantations) to WordPress.
Each page is a standalone HTML file in pages/.
This script reads the HTML, wraps it for WP, and pushes via REST API.

Usage:
  python3 deploy-new-pages.py              # Deploy all new pages
  python3 deploy-new-pages.py negoce       # Deploy only the negoce page
  python3 deploy-new-pages.py ia           # Deploy only IA pages
  python3 deploy-new-pages.py geo          # Deploy only geo pages
"""

import json, re, sys, subprocess, tempfile, os, time

WP_URL = "https://www.helloharel.com/prometheus/wp-json/wp/v2"
WP_USER = "administration@remi-oravec.fr"
WP_PASS = "T8Yu 6UBr 1BOh H3i2 PNSw khHk"

# Read CSS from style.css (for CSS file upload)
with open('/workspaces/refonte-helloharel/style.css', 'r') as f:
    CSS = f.read()

# External CSS URL (loaded at runtime instead of inline)
CSS_URL = "https://www.helloharel.com/prometheus/wp-content/uploads/2026/03/hh-style.txt"

# ══════════════════════════════════════════════════════════════
# PAGE REGISTRY — slug → (html_file, wp_page_id, parent_id)
# Set wp_page_id to 0 for pages that need to be created first
# ══════════════════════════════════════════════════════════════

NEGOCE_PAGES = {
    "negoce": ("pages/negoce.html", 6248, 0),
}

IA_PAGES = {
    "intelligence-artificielle": ("pages/intelligence-artificielle.html", 7039, 0),
    "ia-analyse-predictive": ("pages/ia-analyse-predictive.html", 7041, 0),
    "ia-automatisation-comptable": ("pages/ia-automatisation-comptable.html", 7043, 0),
    "ia-assistant-commercial": ("pages/ia-assistant-commercial.html", 7045, 0),
    "ia-optimisation-stocks": ("pages/ia-optimisation-stocks.html", 7047, 0),
}

GEO_PAGES = {
    "implantations": ("pages/implantations.html", 7049, 0),
    "implantation-reunion": ("pages/implantation-reunion.html", 7051, 0),
    "implantation-maurice": ("pages/implantation-maurice.html", 7053, 0),
    "implantation-belgique": ("pages/implantation-belgique.html", 7055, 0),
    "implantation-ile-de-france": ("pages/implantation-ile-de-france.html", 7057, 0),
    "implantation-hauts-de-france": ("pages/implantation-hauts-de-france.html", 7059, 0),
    "implantation-auvergne-rhone-alpes": ("pages/implantation-auvergne-rhone-alpes.html", 7061, 0),
    "implantation-occitanie": ("pages/implantation-occitanie.html", 7026, 0),
    "implantation-nouvelle-aquitaine": ("pages/implantation-nouvelle-aquitaine.html", 7064, 0),
    "implantation-bretagne": ("pages/implantation-bretagne.html", 7066, 0),
}

ALL_PAGES = {**NEGOCE_PAGES, **IA_PAGES, **GEO_PAGES}


def extract_body(html_path):
    """Read an HTML file and extract the <body> content."""
    full_path = os.path.join('/workspaces/refonte-helloharel', html_path)
    with open(full_path, 'r') as f:
        html = f.read()
    match = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    if match:
        return match.group(1).strip()
    # Fallback: return everything after <body> tag
    idx = html.find('<body>')
    if idx >= 0:
        end = html.find('</body>')
        return html[idx+6:end].strip() if end >= 0 else html[idx+6:].strip()
    return html


def extract_title(html_path):
    """Extract <title> from the HTML file."""
    full_path = os.path.join('/workspaces/refonte-helloharel', html_path)
    with open(full_path, 'r') as f:
        html = f.read()
    match = re.search(r'<title>(.*?)</title>', html)
    return match.group(1) if match else ""


def find_or_create_page(slug, title, parent_id=0):
    """Find existing WP page by slug, or create a new one. Returns page ID."""
    # First, try to find by slug
    result = subprocess.run([
        'curl', '-s', '--tlsv1.2', '--max-time', '30',
        '-u', f'{WP_USER}:{WP_PASS}',
        f'{WP_URL}/pages?slug={slug}&status=any'
    ], capture_output=True, text=True, timeout=60)

    if result.returncode == 0:
        try:
            pages = json.loads(result.stdout)
            if isinstance(pages, list) and len(pages) > 0:
                pid = pages[0]['id']
                print(f"  FOUND | {slug:40s} | id={pid}")
                return pid
        except json.JSONDecodeError:
            pass

    # Create new page
    create_payload = json.dumps({
        "title": title,
        "slug": slug,
        "status": "publish",
        "parent": parent_id,
        "template": "elementor_canvas",
        "content": "<!-- placeholder -->",
    })

    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tf:
        tf.write(create_payload)
        payload_path = tf.name

    try:
        result = subprocess.run([
            'curl', '-s', '--tlsv1.2', '--max-time', '60',
            '-u', f'{WP_USER}:{WP_PASS}',
            '-X', 'POST',
            '-H', 'Content-Type: application/json',
            '-d', f'@{payload_path}',
            f'{WP_URL}/pages'
        ], capture_output=True, text=True, timeout=120)
    finally:
        os.unlink(payload_path)

    if result.returncode == 0:
        try:
            data = json.loads(result.stdout)
            if 'id' in data:
                pid = data['id']
                print(f"  CREATE | {slug:40s} | id={pid}")
                return pid
        except json.JSONDecodeError:
            pass

    print(f"  FAIL | Could not find or create page: {slug}")
    print(f"        {result.stdout[:200] if result.stdout else result.stderr[:200]}")
    return None


def deploy_page(slug, html_path, page_id):
    """Deploy page content to WordPress."""
    body_html = extract_body(html_path)
    wrapped = f'<div id="hh-page">\n{body_html}\n</div>'
    full = f'''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style id="hh-preload">#hh-page{{opacity:0;transition:opacity .3s}}</style>
<script>
fetch('{CSS_URL}').then(function(r){{return r.text()}}).then(function(css){{
  var s=document.createElement('style');s.textContent=css;document.head.appendChild(s);
  var p=document.getElementById('hh-preload');if(p)p.remove();
  var e=document.getElementById('hh-page');if(e)e.style.opacity='1';
}});
</script>
{wrapped}'''
    wp_content = f'<!-- wp:html -->\n{full}\n<!-- /wp:html -->'

    payload = json.dumps({
        "content": wp_content,
        "template": "elementor_canvas",
        "meta": {
            "_elementor_edit_mode": "",
            "_elementor_data": "[]"
        }
    })

    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tf:
        tf.write(payload)
        payload_path = tf.name

    try:
        result = subprocess.run([
            'curl', '-s', '--tlsv1.2', '--max-time', '120',
            '-u', f'{WP_USER}:{WP_PASS}',
            '-X', 'POST',
            '-H', 'Content-Type: application/json',
            '-d', f'@{payload_path}',
            f'{WP_URL}/pages/{page_id}'
        ], capture_output=True, text=True, timeout=180)
    finally:
        os.unlink(payload_path)

    if result.returncode != 0:
        print(f"  FAIL | {slug:40s} | curl exit {result.returncode}")
        return False

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        print(f"  FAIL | {slug:40s} | Invalid JSON")
        return False

    if 'id' in data:
        rendered = data.get('content', {}).get('rendered', '')
        has_hh = 'id="hh-page"' in rendered
        print(f"  OK   | {slug:40s} | id={page_id} | hh-page={has_hh}")
        return True
    else:
        print(f"  FAIL | {slug:40s} | {data.get('message', 'Unknown error')}")
        return False


def deploy_group(pages_dict):
    """Deploy a group of pages."""
    ok = 0
    fail = 0
    for slug, (html_path, page_id, parent_id) in pages_dict.items():
        full_path = os.path.join('/workspaces/refonte-helloharel', html_path)
        if not os.path.exists(full_path):
            print(f"  SKIP | {slug:40s} | File not found: {html_path}")
            fail += 1
            continue

        title = extract_title(html_path)

        # Find or create the page
        pid = page_id if page_id > 0 else find_or_create_page(slug, title, parent_id)
        if pid is None:
            fail += 1
            continue

        if deploy_page(slug, html_path, pid):
            ok += 1
        else:
            fail += 1

        time.sleep(1)  # Rate limiting

    return ok, fail


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'all'

    print(f"\n{'='*60}")
    print(f"  DEPLOYING NEW PAGES — target: {target}")
    print(f"{'='*60}\n")

    if target == 'all':
        pages = ALL_PAGES
    elif target == 'negoce':
        pages = NEGOCE_PAGES
    elif target == 'ia':
        pages = IA_PAGES
    elif target == 'geo':
        pages = GEO_PAGES
    else:
        # Try single slug
        if target in ALL_PAGES:
            pages = {target: ALL_PAGES[target]}
        else:
            print(f"Unknown target: {target}")
            print("Usage: deploy-new-pages.py [all|negoce|ia|geo|<slug>]")
            sys.exit(1)

    ok, fail = deploy_group(pages)

    print(f"\n{'='*60}")
    print(f"  DONE — {ok} deployed, {fail} failed")
    print(f"{'='*60}\n")

    sys.exit(0 if fail == 0 else 1)
