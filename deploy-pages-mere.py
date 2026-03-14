#!/usr/bin/env python3
"""
Deploy Hello Harel "Pages Mère" (Fonctionnalités + Agroalimentaire)
EXACT same mechanism as deploy-homepage.py:
  - Read HTML file body
  - Wrap in #hh-page
  - Inject same CSS from deploy-homepage.py
  - Push via REST API with elementor_canvas template
"""

import json, re, sys, requests
from requests.auth import HTTPBasicAuth

WP_URL = "https://www.helloharel.com/prometheus/wp-json/wp/v2"
AUTH = HTTPBasicAuth("administration@remi-oravec.fr", "T8Yu 6UBr 1BOh H3i2 PNSw khHk")

PAGES = {
    "fonctionnalites": {
        "id": 4728,
        "html_file": "/workspaces/refonte-helloharel/fonctionnalites.html",
        "name": "Fonctionnalités"
    },
    "agroalimentaire": {
        "id": 1726,
        "html_file": "/workspaces/refonte-helloharel/agroalimentaire.html",
        "name": "ERP Agroalimentaire"
    }
}

# ── Load CSS from deploy-homepage.py (EXACT same CSS) ──
with open('/workspaces/refonte-helloharel/deploy-homepage.py', 'r') as f:
    deploy_script = f.read()
css_match = re.search(r'CSS = r"""(.*?)"""', deploy_script, re.DOTALL)
CSS = css_match.group(1)


def deploy_page(slug):
    page = PAGES[slug]
    page_id = page["id"]
    name = page["name"]

    print(f"\n{'=' * 60}")
    print(f"DEPLOYING: {name} (ID: {page_id})")
    print(f"{'=' * 60}")

    # Read HTML file body (EXACT same method as deploy-homepage.py)
    with open(page["html_file"], 'r') as f:
        html_full = f.read()
    body_match = re.search(r'<body>(.*?)</body>', html_full, re.DOTALL)
    body_content = body_match.group(1).strip()

    # Wrap in #hh-page div (EXACT same as deploy-homepage.py)
    wrapped_html = f'<div id="hh-page">\n{body_content}\n</div>'

    # Build full content (EXACT same as deploy-homepage.py)
    full_content = f"""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
{CSS}
</style>
{wrapped_html}"""

    # Wrap in wp:html block (EXACT same as deploy-homepage.py)
    wp_content = f'<!-- wp:html -->\n{full_content}\n<!-- /wp:html -->'

    # Deploy (EXACT same as deploy-homepage.py)
    response = requests.post(
        f"{WP_URL}/pages/{page_id}",
        auth=AUTH,
        json={
            "content": wp_content,
            "template": "elementor_canvas",
            "meta": {
                "_elementor_edit_mode": "",
                "_elementor_data": "[]"
            }
        },
        headers={"Content-Type": "application/json"},
        timeout=60
    )

    if response.status_code == 200:
        data = response.json()
        rendered = data.get('content', {}).get('rendered', '')
        print(f"\nSUCCESS!")
        print(f"  URL: {data['link']}")
        print(f"  Template: {data['template']}")
        print(f"  Modified: {data['modified']}")
        print(f"  Rendered length: {len(rendered)}")
        print(f"\nVerification:")

        checks = {
            '#hh-page wrapper': 'id="hh-page"' in rendered,
            'CSS vars (--hh-blue-900)': '--hh-blue-900' in rendered,
            'z-index 99999': 'z-index: 99999' in rendered or 'z-index:99999' in rendered,
            'Nuclear reset': 'elementor-location-header' in rendered,
            'Header (site-header)': 'site-header' in rendered,
            'Hero centered': 'hero-content-centered' in rendered,
            'Bento grid': 'bento-grid' in rendered,
            'About section': 'about-section' in rendered,
            'Process section': 'process-section' in rendered,
            'Industries section': 'industries-section' in rendered,
            'Team section': 'team-section' in rendered,
            'Reviews section': 'reviews-section' in rendered,
            'FAQ drawer': 'faq-drawer' in rendered,
            'Footer': 'footer-grid' in rendered,
            'Sticky CTA': 'sticky-cta' in rendered,
            'JS (hamburgerBtn)': 'hamburgerBtn' in rendered,
        }
        for check_name, ok in checks.items():
            print(f"  {'✓' if ok else '✗'} {check_name}")

        all_ok = all(checks.values())
        print(f"\n{'ALL CHECKS PASSED' if all_ok else 'SOME CHECKS FAILED'}")
        return all_ok
    else:
        print(f"ERROR {response.status_code}")
        print(response.text[:1000])
        return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        slug = sys.argv[1]
        if slug not in PAGES:
            print(f"Unknown page: {slug}. Available: {', '.join(PAGES.keys())}")
            sys.exit(1)
        deploy_page(slug)
    else:
        results = {}
        for slug in PAGES:
            results[slug] = deploy_page(slug)
        print(f"\n{'=' * 60}")
        print("SUMMARY")
        print(f"{'=' * 60}")
        for slug, ok in results.items():
            print(f"  {'✓' if ok else '✗'} {PAGES[slug]['name']}")
