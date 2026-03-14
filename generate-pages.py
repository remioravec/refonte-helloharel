#!/usr/bin/env python3
"""
Generate all 16 static HTML files from mega menu page data.
Outputs files to pages/{slug}.html
"""

import importlib, importlib.util, os, sys

# ── Import deploy-all-pages module (has dashes in name) ──
spec = importlib.util.spec_from_file_location(
    "deploy_all_pages",
    "/workspaces/refonte-helloharel/deploy-all-pages.py"
)
dap = importlib.util.module_from_spec(spec)

# Prevent the module from importing requests at module level (not needed here)
# We need to mock requests since deploy-all-pages.py imports it at top level
# and also reads deploy-homepage.py for CSS. Let's handle that.

# First, ensure deploy-homepage.py exists or handle the CSS load gracefully
spec.loader.exec_module(dap)

from page_data import PAGES

# ── Canonical URL mapping ──
# Fonctionnalites pages live under /fonctionnalites/{slug}/
# Industry pages live under /agroalimentaire/{slug}/ (except agroalimentaire itself)
FONC_SLUGS = {
    "fonctionnalites", "crm", "facturation", "vente",
    "gestion-de-stock", "fabrication", "achat", "logistique", "import-export"
}
INDUSTRY_SLUGS = {
    "traiteur", "maraicher", "boulanger", "charcutier",
    "industrie-laitiere", "plats-cuisines-industriels"
}

def get_canonical_path(page):
    slug = page["slug"]
    if slug == "fonctionnalites":
        return "/fonctionnalites/"
    elif slug in FONC_SLUGS:
        return f"/fonctionnalites/{slug}/"
    elif slug == "agroalimentaire":
        return "/agroalimentaire/"
    elif slug in INDUSTRY_SLUGS:
        return f"/agroalimentaire/{slug}/"
    else:
        return f"/{slug}/"

BASE_URL = "https://www.helloharel.com"

def generate_page(page):
    """Generate a full standalone HTML page."""
    canonical_path = get_canonical_path(page)
    canonical_url = BASE_URL + canonical_path
    title = page["name"]
    description = page["hero"]["desc"]

    body_html = "\n\n".join([
        dap.HEADER,
        dap.make_hero(page),
        dap.LOGO_CAROUSEL,
        dap.make_bento(page),
        dap.ABOUT_VIDEO,
        dap.PROCESS,
        dap.INDUSTRIES,
        dap.TEAM,
        dap.TESTIMONIAL,
        dap.make_faq(page),
        dap.REVIEWS,
        dap.CTA_BANNER,
        dap.FOOTER,
        dap.STICKY_CTA,
        dap.JS,
    ])

    html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Hello Harel ERP Agroalimentaire</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical_url}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="https://cdnjs.cloudflare.com">
    <meta property="og:title" content="{title} - Hello Harel ERP Agroalimentaire">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:type" content="website">
    <link rel="stylesheet" href="../style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
</head>
<body>

{body_html}

</body>
</html>'''
    return html


def main():
    outdir = "/workspaces/refonte-helloharel/pages"
    os.makedirs(outdir, exist_ok=True)

    print(f"Generating {len(PAGES)} static HTML pages into {outdir}/\n")

    for page in PAGES:
        slug = page["slug"]
        html = generate_page(page)
        filepath = os.path.join(outdir, f"{slug}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        size_kb = len(html.encode("utf-8")) / 1024
        print(f"  OK | {page['name']:40s} | {slug}.html | {size_kb:.1f} KB")

    print(f"\nDone. {len(PAGES)} files written to {outdir}/")


if __name__ == "__main__":
    main()
