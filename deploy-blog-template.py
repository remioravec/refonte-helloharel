#!/usr/bin/env python3
"""Deploy HH design system to all blog posts."""
import json, re, sys, requests, time
from requests.auth import HTTPBasicAuth

WP_URL = "https://www.helloharel.com/prometheus/wp-json/wp/v2"
AUTH = HTTPBasicAuth("administration@remi-oravec.fr", "T8Yu 6UBr 1BOh H3i2 PNSw khHk")

# Load CSS from deploy-homepage.py
with open('/workspaces/refonte-helloharel/deploy-homepage.py', 'r') as f:
    deploy_script = f.read()
css_match = re.search(r'CSS = r"""(.*?)"""', deploy_script, re.DOTALL)
CSS = css_match.group(1)

# Load shared sections from deploy-all-pages
import importlib.util
spec = importlib.util.spec_from_file_location("deploy_all", "/workspaces/refonte-helloharel/deploy-all-pages.py")
deploy = importlib.util.module_from_spec(spec)
old_argv = sys.argv
sys.argv = ['deploy-all-pages.py', '--skip']
try:
    spec.loader.exec_module(deploy)
except SystemExit:
    pass
sys.argv = old_argv

# Article CSS
ARTICLE_CSS = """
.article-section { padding: 172px 0 4rem; background: #fff; }
.article-container { max-width: 800px; margin: 0 auto; padding: 0 1.5rem; }
.article-breadcrumb { font-size: 0.8125rem; color: #64748b; margin-bottom: 2rem; }
.article-breadcrumb a { color: #1d4ed8; font-weight: 600; }
.article-meta { margin-bottom: 2rem; }
.article-meta time { font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: #94a3b8; }
.article-title { font-size: clamp(1.75rem, 4vw, 2.75rem); font-weight: 900; line-height: 1.15; letter-spacing: -0.02em; color: #0f172a; margin-bottom: 1.5rem; }
.article-content { font-size: 1.0625rem; line-height: 1.85; color: #334155; }
.article-content h2 { font-size: 1.5rem; font-weight: 800; color: #0f172a; margin-top: 2.5rem; margin-bottom: 1rem; letter-spacing: -0.01em; }
.article-content h3 { font-size: 1.25rem; font-weight: 700; color: #0f172a; margin-top: 2rem; margin-bottom: 0.75rem; }
.article-content p { margin-bottom: 1.25rem; }
.article-content ul, .article-content ol { margin: 1rem 0 1.25rem 1.5rem; padding: 0; }
.article-content ul { list-style: disc; }
.article-content ol { list-style: decimal; }
.article-content li { margin-bottom: 0.5rem; font-size: 1rem; color: #475569; line-height: 1.7; }
.article-content a { color: #1d4ed8; font-weight: 600; text-decoration: underline; }
.article-content a:hover { color: #1e3a8a; }
.article-content strong { color: #0f172a; font-weight: 700; }
.article-content blockquote { border-left: 4px solid #1d4ed8; padding: 1rem 1.5rem; margin: 1.5rem 0; background: #f8fafc; border-radius: 0 0.5rem 0.5rem 0; font-style: italic; color: #475569; }
.article-content img { max-width: 100%; height: auto; border-radius: 1rem; margin: 1.5rem 0; }
.article-content table { width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.9375rem; border: 1px solid #e2e8f0; border-radius: 0.75rem; overflow: hidden; }
.article-content thead { background: #1e3a8a; }
.article-content thead th { color: #fff; font-weight: 700; padding: 0.75rem 1rem; text-align: left; }
.article-content tbody tr { border-bottom: 1px solid #e2e8f0; }
.article-content tbody tr:nth-child(even) { background: #f8fafc; }
.article-content tbody td { padding: 0.625rem 1rem; color: #475569; }
.article-cta { background: linear-gradient(135deg, #1e3a8a, #1d4ed8); border-radius: 1.25rem; padding: 2.5rem; text-align: center; margin-top: 3rem; color: #fff; }
.article-cta h3 { font-size: 1.5rem; font-weight: 900; margin-bottom: 0.75rem; color: #fff; }
.article-cta p { color: rgba(255,255,255,0.8); margin-bottom: 1.5rem; font-size: 1rem; }
.article-cta a { display: inline-flex; padding: 0.875rem 2rem; background: #fff; color: #1e3a8a; border-radius: 0.75rem; font-weight: 800; font-size: 0.9375rem; transition: all 0.3s; text-decoration: none; }
.article-cta a:hover { transform: translateY(-2px); box-shadow: 0 10px 25px rgba(0,0,0,0.2); }
"""


def deploy_post(post_id, title, content, date_str):
    """Wrap post content in HH template and deploy."""
    article_html = f'''
{deploy.HEADER}
<section class="article-section">
    <div class="article-container">
        <div class="article-breadcrumb">
            <a href="/prometheus/">Accueil</a> / <a href="/prometheus/blog/">Blog</a> / {title}
        </div>
        <div class="article-meta"><time>{date_str}</time></div>
        <h1 class="article-title">{title}</h1>
        <div class="article-content">
            {content}
        </div>
        <div class="article-cta">
            <h3>Prêt à optimiser votre gestion ?</h3>
            <p>Découvrez comment Hello Harel peut transformer votre activité.</p>
            <a href="/prometheus/contact/">Demander une démo gratuite</a>
        </div>
    </div>
</section>
{deploy.CTA_BANNER}
{deploy.FOOTER}
{deploy.STICKY_CTA}
{deploy.JS}
'''
    wrapped = f'<div id="hh-page">\n{article_html}\n</div>'
    full = f'''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
{CSS}
{ARTICLE_CSS}
</style>
{wrapped}'''
    wp_content = f'<!-- wp:html -->\n{full}\n<!-- /wp:html -->'

    resp = requests.post(
        f"{WP_URL}/posts/{post_id}",
        auth=AUTH,
        json={"content": wp_content, "template": "elementor_canvas"},
        headers={"Content-Type": "application/json"},
        timeout=120
    )
    return resp.status_code == 200


if __name__ == "__main__":
    # Get all posts
    page = 1
    all_posts = []
    while True:
        r = requests.get(f"{WP_URL}/posts?per_page=50&page={page}", auth=AUTH, timeout=30)
        if r.status_code != 200:
            break
        posts = r.json()
        if not posts:
            break
        all_posts.extend(posts)
        total_pages = int(r.headers.get('X-WP-TotalPages', 1))
        if page >= total_pages:
            break
        page += 1

    print(f"Found {len(all_posts)} posts to template")
    print("=" * 80)

    ok_count = 0
    for post in all_posts:
        pid = post['id']
        title = post['title']['rendered']
        content = post['content']['rendered']
        date_obj = post['date'][:10]

        # Skip if already templated (has #hh-page)
        if 'id="hh-page"' in content:
            # Extract just the article-content
            match = re.search(r'<div class="article-content">\s*(.*?)\s*</div>\s*<div class="article-cta">', content, re.DOTALL)
            if match:
                content = match.group(1)
            else:
                print(f"  SKIP | {title[:50]} (already templated, cannot extract)")
                continue

        success = deploy_post(pid, title, content, date_obj)
        status = "OK" if success else "FAIL"
        if success:
            ok_count += 1
        print(f"  {status} | {title[:60]}")
        time.sleep(0.5)  # Rate limiting

    print(f"\n{ok_count}/{len(all_posts)} posts templated successfully.")
