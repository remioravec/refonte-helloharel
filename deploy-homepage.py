#!/usr/bin/env python3
"""
Deploy Hello Harel homepage — v4 COMPLETE
All CSS scoped under #hh-page with !important everywhere.
Includes: hero-centered, about, reviews, FAQ drawer, all responsive.
"""

import json, re, requests
from requests.auth import HTTPBasicAuth

WP_URL = "https://www.helloharel.com/prometheus/wp-json/wp/v2"
AUTH = HTTPBasicAuth("administration@remi-oravec.fr", "T8Yu 6UBr 1BOh H3i2 PNSw khHk")
PAGE_ID = 2

# ── Read index.html body ──
with open('/workspaces/refonte-helloharel/index.html', 'r') as f:
    html_full = f.read()
body_match = re.search(r'<body>(.*?)</body>', html_full, re.DOTALL)
body_content = body_match.group(1).strip()

# ── HARDENED CSS ──
# Every rule scoped under #hh-page for max specificity
# !important on ALL visual properties to override WP/Elementor globals
CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ====== NUCLEAR RESET: hide ALL WP/Elementor/theme headers & footers ====== */
/* Target by Elementor location hooks */
body .elementor-location-header,
body .elementor-location-footer,
/* Target by Elementor template IDs */
body .elementor-1868,
body .elementor-1746,
body [data-elementor-type="header"],
body [data-elementor-type="footer"],
/* Target by common theme selectors */
body > header,
body #masthead,
body #site-header,
body #colophon,
body .site-branding,
body .main-navigation,
body .primary-navigation,
body .site-navigation,
body .ast-above-header-wrap,
body .ast-below-header-wrap,
body .ast-main-header-wrap,
body .ast-footer-overlay,
body .wp-site-blocks > header,
body .wp-site-blocks > footer,
/* Structural: any header/nav NOT inside #hh-page */
header:not(#hh-page header),
nav:not(#hh-page nav):not(#hh-page .desktop-nav):not(.mobile-menu-inner nav),
/* Target by Elementor widget containers that are headers/footers injected outside page content */
body > .elementor[data-elementor-type="header"],
body > .elementor[data-elementor-type="footer"],
body > div > .elementor[data-elementor-type="header"],
body > div > .elementor[data-elementor-type="footer"],
.elementor-element[data-elementor-type="header"],
.elementor-element[data-elementor-type="footer"],
/* JetKit / Hello theme / GeneratePress / OceanWP / Kadence etc. */
body #site-navigation,
body .genesis-nav-menu,
body .kadence-header,
body .site-header-wrap,
body #header,
body .top-bar,
body .header-wrap,
body .header-main,
body .header-widget-area,
body .footer-widget-area,
body .site-footer:not(#hh-page .site-footer) {
  display: none !important;
  visibility: hidden !important;
  height: 0 !important;
  max-height: 0 !important;
  min-height: 0 !important;
  overflow: hidden !important;
  position: absolute !important;
  pointer-events: none !important;
  opacity: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  border: none !important;
  clip: rect(0,0,0,0) !important;
  width: 0 !important;
}

/* Extra safety: force body to have no top padding/margin from theme header spacing */
body {
  padding-top: 0 !important;
  margin-top: 0 !important;
}
body.admin-bar #hh-page .site-header {
  top: 72px !important;
}
body.admin-bar #hh-page .hero-section {
  padding-top: 244px !important;
}
body.admin-bar #hh-page .mobile-menu {
  top: 144px !important;
}

/* ====== PAGE WRAPPER RESET ====== */
#hh-page {
  all: initial !important;
  display: block !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  -webkit-font-smoothing: antialiased !important;
  -moz-osx-font-smoothing: grayscale !important;
  color: #0f172a !important;
  line-height: 1.6 !important;
  font-size: 16px !important;
  position: relative !important;
  width: 100% !important;
  overflow-x: hidden !important;
}

#hh-page *, #hh-page *::before, #hh-page *::after {
  box-sizing: border-box !important;
  -webkit-font-smoothing: antialiased !important;
}

#hh-page img { max-width: 100% !important; height: auto !important; border: none !important; }
#hh-page a { text-decoration: none !important; color: inherit !important; }
#hh-page ul, #hh-page ol { list-style: none !important; margin: 0 !important; padding: 0 !important; }
#hh-page h1, #hh-page h2, #hh-page h3, #hh-page h4, #hh-page h5, #hh-page h6,
#hh-page p, #hh-page blockquote, #hh-page figure {
  margin: 0 !important; padding: 0 !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}
#hh-page button { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important; }
#hh-page svg { vertical-align: middle !important; }

:root {
  --hh-blue-50: #eff6ff; --hh-blue-100: #dbeafe; --hh-blue-200: #bfdbfe;
  --hh-blue-500: #3b82f6; --hh-blue-600: #2563eb; --hh-blue-700: #1d4ed8;
  --hh-blue-800: #1e40af; --hh-blue-900: #1e3a8a;
  --hh-slate-50: #f8fafc; --hh-slate-100: #f1f5f9; --hh-slate-200: #e2e8f0;
  --hh-slate-300: #cbd5e1; --hh-slate-400: #94a3b8; --hh-slate-500: #64748b;
  --hh-slate-600: #475569; --hh-slate-700: #334155; --hh-slate-800: #1e293b;
  --hh-slate-900: #0f172a;
  --hh-emerald-50: #ecfdf5; --hh-emerald-600: #059669;
  --hh-indigo-50: #eef2ff; --hh-indigo-600: #4f46e5;
  --hh-amber-50: #fffbeb; --hh-amber-600: #d97706;
  --hh-red-50: #fef2f2; --hh-red-600: #dc2626;
  --hh-teal-50: #f0fdfa; --hh-teal-600: #0d9488;
  --hh-cyan-50: #ecfeff; --hh-cyan-600: #0891b2;
  --hh-orange-50: #fff7ed; --hh-orange-600: #ea580c;
  --hh-purple-50: #faf5ff; --hh-purple-600: #9333ea;
}

#hh-page .container {
  max-width: 1280px !important; margin: 0 auto !important; padding: 0 1.5rem !important;
  width: 100% !important; display: block !important;
}

/* ====== HEADER — z-index 99999, position fixed, triple specificity ====== */
html body #hh-page .site-header,
#hh-page header.site-header,
#hh-page .site-header {
  position: fixed !important; top: 40px !important; left: 0 !important; right: 0 !important;
  z-index: 99999 !important;
  background: #1e3a8a !important;
  background-color: #1e3a8a !important;
  border-bottom: 1px solid rgba(255,255,255,0.1) !important;
  display: block !important; visibility: visible !important;
  height: auto !important; min-height: 72px !important;
  overflow: visible !important;
  pointer-events: auto !important; opacity: 1 !important;
  width: 100% !important; max-width: 100% !important;
  padding: 0 !important; margin: 0 !important;
  transform: none !important;
  clip: auto !important;
  max-height: none !important;
}
#hh-page .header-inner {
  display: flex !important; align-items: center !important; justify-content: space-between !important;
  height: 72px !important; max-width: 1280px !important; margin: 0 auto !important;
  padding: 0 1.5rem !important;
}
#hh-page .logo img { height: 32px !important; width: auto !important; }
#hh-page .desktop-nav {
  display: flex !important; align-items: center !important; gap: 0.25rem !important;
}
#hh-page .desktop-nav > a {
  color: rgba(255,255,255,0.9) !important; font-weight: 500 !important; font-size: 0.9375rem !important;
  padding: 0.5rem 0.75rem !important; border-radius: 0.5rem !important;
  transition: all 0.3s ease !important; display: inline-block !important;
  background: transparent !important; border: none !important;
}
#hh-page .desktop-nav > a:hover { color: #fff !important; background: rgba(255,255,255,0.08) !important; }

/* Dropdowns */
#hh-page .nav-dropdown { position: relative !important; display: inline-block !important; }
#hh-page .nav-dropdown-trigger {
  display: inline-flex !important; align-items: center !important; gap: 0.375rem !important;
  color: rgba(255,255,255,0.9) !important; font-weight: 500 !important; font-size: 0.9375rem !important;
  padding: 0.5rem 0.75rem !important; border-radius: 0.5rem !important;
  background: none !important; border: none !important; cursor: pointer !important;
  font-family: inherit !important; transition: all 0.3s ease !important;
  line-height: 1.5 !important;
}
#hh-page .nav-dropdown-trigger:hover { color: #fff !important; background: rgba(255,255,255,0.08) !important; }
#hh-page .chevron-icon { width: 16px !important; height: 16px !important; transition: transform 0.3s ease !important; }
#hh-page .nav-dropdown:hover .chevron-icon { transform: rotate(180deg) !important; }
#hh-page .dropdown-panel {
  position: absolute !important; top: 100% !important; left: 50% !important; transform: translateX(-50%) !important;
  padding-top: 0.75rem !important;
  opacity: 0 !important; visibility: hidden !important; pointer-events: none !important;
  transition: all 0.25s ease !important; z-index: 10000 !important;
}
#hh-page .nav-dropdown:hover .dropdown-panel {
  opacity: 1 !important; visibility: visible !important; pointer-events: auto !important;
}
#hh-page .dropdown-card {
  background: #fff !important; border: 1px solid var(--hh-slate-200) !important;
  border-radius: 1rem !important; padding: 1rem !important;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25) !important;
}
#hh-page .dropdown-link {
  display: flex !important; align-items: center !important; gap: 0.75rem !important;
  padding: 0.625rem 0.75rem !important; border-radius: 0.625rem !important;
  transition: background 0.2s ease !important;
}
#hh-page .dropdown-link:hover { background: var(--hh-slate-50) !important; }
#hh-page .dropdown-link-icon {
  width: 2.5rem !important; height: 2.5rem !important; border-radius: 0.5rem !important;
  display: flex !important; align-items: center !important; justify-content: center !important;
  flex-shrink: 0 !important; transition: all 0.3s ease !important;
}
#hh-page .dropdown-link-icon svg { width: 1.25rem !important; height: 1.25rem !important; }
#hh-page .dropdown-link-icon.blue { background: var(--hh-blue-50) !important; color: var(--hh-blue-600) !important; }
#hh-page .dropdown-link:hover .dropdown-link-icon.blue { background: var(--hh-blue-600) !important; color: #fff !important; }
#hh-page .dropdown-link-icon.indigo { background: var(--hh-indigo-50) !important; color: var(--hh-indigo-600) !important; }
#hh-page .dropdown-link:hover .dropdown-link-icon.indigo { background: var(--hh-indigo-600) !important; color: #fff !important; }
#hh-page .dropdown-link-icon.emerald { background: var(--hh-emerald-50) !important; color: var(--hh-emerald-600) !important; }
#hh-page .dropdown-link:hover .dropdown-link-icon.emerald { background: var(--hh-emerald-600) !important; color: #fff !important; }
#hh-page .dropdown-link-icon.amber { background: var(--hh-amber-50) !important; color: var(--hh-amber-600) !important; }
#hh-page .dropdown-link:hover .dropdown-link-icon.amber { background: var(--hh-amber-600) !important; color: #fff !important; }
#hh-page .dropdown-link-icon.red { background: var(--hh-red-50) !important; color: var(--hh-red-600) !important; }
#hh-page .dropdown-link:hover .dropdown-link-icon.red { background: var(--hh-red-600) !important; color: #fff !important; }
#hh-page .dropdown-link-icon.teal { background: var(--hh-teal-50) !important; color: var(--hh-teal-600) !important; }
#hh-page .dropdown-link:hover .dropdown-link-icon.teal { background: var(--hh-teal-600) !important; color: #fff !important; }
#hh-page .dropdown-link-icon.cyan { background: var(--hh-cyan-50) !important; color: var(--hh-cyan-600) !important; }
#hh-page .dropdown-link:hover .dropdown-link-icon.cyan { background: var(--hh-cyan-600) !important; color: #fff !important; }
#hh-page .dropdown-link-icon.orange { background: var(--hh-orange-50) !important; color: var(--hh-orange-600) !important; }
#hh-page .dropdown-link:hover .dropdown-link-icon.orange { background: var(--hh-orange-600) !important; color: #fff !important; }
#hh-page .dropdown-link-text { font-size: 0.875rem !important; font-weight: 600 !important; color: var(--hh-slate-700) !important; }

/* Mega Industries */
#hh-page .mega-industries-card { width: 420px !important; max-width: 95vw !important; }
#hh-page .mega-industries-inner { padding: 1.25rem !important; }
#hh-page .mega-industries-inner h5 {
  display: flex !important; align-items: center !important; gap: 0.5rem !important;
  font-size: 0.6875rem !important; font-weight: 700 !important; text-transform: uppercase !important;
  letter-spacing: 0.08em !important; color: var(--hh-slate-400) !important;
  margin-bottom: 1rem !important; padding-bottom: 0.75rem !important;
  border-bottom: 1px solid var(--hh-slate-100) !important; line-height: 1.4 !important;
}
#hh-page .mega-industries-inner h5 svg { width: 1rem !important; height: 1rem !important; }
#hh-page .industry-link {
  display: flex !important; align-items: center !important; gap: 0.75rem !important;
  padding: 0.5rem 0.625rem !important; border-radius: 0.5rem !important;
  font-size: 0.875rem !important; font-weight: 500 !important; color: var(--hh-slate-700) !important;
  transition: all 0.2s ease !important;
}
#hh-page .industry-link:hover { background: var(--hh-blue-50) !important; color: var(--hh-blue-700) !important; }
#hh-page .industry-link-icon {
  width: 2rem !important; height: 2rem !important; border-radius: 0.375rem !important;
  background: var(--hh-slate-50) !important; display: flex !important; align-items: center !important; justify-content: center !important;
  transition: all 0.3s ease !important;
}
#hh-page .industry-link:hover .industry-link-icon { background: var(--hh-blue-100) !important; color: var(--hh-blue-700) !important; }
#hh-page .industry-link-icon svg { width: 1rem !important; height: 1rem !important; }

/* Header actions */
#hh-page .header-actions { display: flex !important; align-items: center !important; gap: 0.75rem !important; }
#hh-page .btn-contact-header {
  color: #fff !important; font-weight: 600 !important; font-size: 0.875rem !important;
  padding: 0.5rem 1rem !important; border-radius: 0.5rem !important;
  border: 1px solid rgba(255,255,255,0.25) !important; transition: all 0.3s ease !important;
  background: transparent !important; display: inline-block !important;
}
#hh-page .btn-contact-header:hover { background: rgba(255,255,255,0.1) !important; border-color: #fff !important; }
#hh-page .btn-demo-header {
  background: #fff !important; color: var(--hh-blue-900) !important; font-weight: 700 !important; font-size: 0.875rem !important;
  padding: 0.5rem 1.25rem !important; border-radius: 0.5rem !important;
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1) !important; transition: all 0.3s ease !important;
  display: inline-block !important; border: none !important;
}
#hh-page .btn-demo-header:hover { background: var(--hh-blue-50) !important; transform: translateY(-1px) !important; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1) !important; }

/* Hamburger */
#hh-page .hamburger-btn {
  display: none !important; background: none !important; border: none !important; cursor: pointer !important;
  color: #fff !important; padding: 0.5rem !important;
}
#hh-page .hamburger-btn svg { width: 1.5rem !important; height: 1.5rem !important; }

/* Mobile menu */
#hh-page .mobile-menu {
  display: none !important; position: fixed !important; top: 112px !important; left: 0 !important; right: 0 !important; bottom: 0 !important;
  background: var(--hh-blue-900) !important; z-index: 9998 !important;
  overflow-y: auto !important; transform: translateX(100%) !important;
  transition: transform 0.3s ease !important;
}
#hh-page .mobile-menu.open { transform: translateX(0) !important; }
#hh-page .mobile-menu-inner { padding: 1.5rem !important; }
#hh-page .mobile-menu-inner > a {
  display: block !important; color: rgba(255,255,255,0.9) !important; font-weight: 500 !important;
  font-size: 1rem !important; padding: 0.875rem 0 !important;
  border-bottom: 1px solid rgba(255,255,255,0.08) !important;
  background: transparent !important;
}
#hh-page .mobile-accordion-btn {
  display: flex !important; align-items: center !important; justify-content: space-between !important; width: 100% !important;
  color: rgba(255,255,255,0.9) !important; font-weight: 500 !important; font-size: 1rem !important;
  padding: 0.875rem 0 !important; border: none !important; background: none !important; cursor: pointer !important;
  font-family: inherit !important; border-bottom: 1px solid rgba(255,255,255,0.08) !important;
  text-align: left !important;
}
#hh-page .mobile-accordion-btn svg { width: 1.25rem !important; height: 1.25rem !important; transition: transform 0.3s !important; color: rgba(255,255,255,0.9) !important; }
#hh-page .mobile-accordion-btn.open svg { transform: rotate(180deg) !important; }
#hh-page .mobile-submenu { max-height: 0 !important; overflow: hidden !important; transition: max-height 0.3s ease !important; }
#hh-page .mobile-submenu.open { max-height: 500px !important; }
#hh-page .mobile-submenu a {
  display: block !important; color: rgba(255,255,255,0.7) !important; font-size: 0.875rem !important;
  padding: 0.625rem 1rem !important; font-weight: 500 !important; background: transparent !important;
}
#hh-page .mobile-submenu a:hover { color: #fff !important; }
#hh-page .mobile-ctas { padding: 1.5rem 0 !important; display: flex !important; flex-direction: column !important; gap: 0.75rem !important; }
#hh-page .mobile-cta-primary {
  display: block !important; text-align: center !important; background: #fff !important; color: var(--hh-blue-900) !important;
  font-weight: 700 !important; padding: 0.875rem !important; border-radius: 0.5rem !important;
}
#hh-page .mobile-cta-secondary {
  display: block !important; text-align: center !important; color: #fff !important;
  font-weight: 600 !important; padding: 0.875rem !important; border-radius: 0.5rem !important;
  border: 1px solid rgba(255,255,255,0.25) !important; background: transparent !important;
}

/* ====== HERO ====== */
#hh-page .hero-section {
  padding: 100px 0 120px !important; padding-top: 212px !important; margin-top: 0 !important;
  display: block !important; position: relative !important; width: 100% !important;
}
#hh-page .hero-grid {
  display: grid !important; grid-template-columns: 1fr 1fr !important; gap: 3rem !important; align-items: center !important;
}
#hh-page .hero-badge {
  display: inline-flex !important; align-items: center !important; gap: 0.5rem !important;
  background: rgba(255,255,255,0.15) !important; backdrop-filter: blur(8px) !important;
  border: 1px solid rgba(255,255,255,0.2) !important;
  border-radius: 9999px !important; padding: 0.375rem 1rem !important;
  font-size: 0.75rem !important; font-weight: 600 !important; color: rgba(255,255,255,0.95) !important;
  margin-bottom: 1.5rem !important;
}
#hh-page .dot {
  width: 8px !important; height: 8px !important; border-radius: 50% !important; background: #34d399 !important;
  animation: hh-pulse-dot 2s infinite !important; display: inline-block !important;
}
@keyframes hh-pulse-dot { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
#hh-page .hero-title {
  font-size: clamp(2.25rem, 5vw, 3.75rem) !important; font-weight: 900 !important;
  line-height: 1.1 !important; letter-spacing: -0.03em !important; margin-bottom: 1.5rem !important;
}
#hh-page .hero-title .accent { color: #60a5fa !important; }
#hh-page .hero-description {
  font-size: 1.125rem !important; line-height: 1.75 !important; margin-bottom: 2rem !important; max-width: 540px !important;
}
#hh-page .hero-cta {
  display: inline-flex !important; align-items: center !important;
  padding: 1rem 2rem !important; border-radius: 0.75rem !important;
  font-weight: 800 !important; font-size: 1rem !important;
  transition: all 0.3s ease !important;
}
#hh-page .hero-cta:hover { transform: translateY(-2px) !important; }
#hh-page .hero-cta-sub { font-size: 0.8125rem !important; margin-top: 0.75rem !important; }
#hh-page .hero-content-centered {
  max-width: 800px !important; margin: 0 auto !important; text-align: center !important;
}
#hh-page .hero-content-centered .hero-badge { justify-content: center !important; }
#hh-page .hero-content-centered .hero-description { margin-left: auto !important; margin-right: auto !important; }
#hh-page .hero-image-wrapper {
  border-radius: 1rem !important; overflow: hidden !important;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.35) !important;
  border: 4px solid rgba(255,255,255,0.15) !important;
}
#hh-page .hero-image-wrapper img { display: block !important; width: 100% !important; }

/* ====== LOGOS ====== */
#hh-page .logos-section {
  padding: 3rem 0 !important; background: var(--hh-slate-50) !important;
  border-top: 1px solid var(--hh-slate-100) !important;
  border-bottom: 1px solid var(--hh-slate-100) !important;
  display: block !important; width: 100% !important;
}
#hh-page .section-label {
  text-align: center !important; font-size: 0.75rem !important; font-weight: 600 !important;
  text-transform: uppercase !important; letter-spacing: 0.1em !important;
  color: var(--hh-slate-400) !important; margin-bottom: 1.5rem !important;
}
#hh-page .logo-carousel-container {
  overflow: hidden !important;
  mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent) !important;
  -webkit-mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent) !important;
}
#hh-page .logo-carousel {
  display: flex !important; gap: 3rem !important; align-items: center !important;
  animation: hh-scroll-logos 40s linear infinite !important;
  width: max-content !important;
}
#hh-page .logo-carousel img {
  height: 2rem !important; width: auto !important; filter: grayscale(100%) !important; opacity: 0.5 !important;
  transition: all 0.3s ease !important; flex-shrink: 0 !important; border-radius: 0 !important;
}
#hh-page .logo-carousel img:hover { filter: grayscale(0) !important; opacity: 1 !important; }
@keyframes hh-scroll-logos { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }

/* ====== DISCOVER ====== */
#hh-page .discover-section { padding: clamp(4rem, 8vw, 7rem) 0 !important; display: block !important; background: #fff !important; }
#hh-page .discover-grid { display: grid !important; grid-template-columns: 1fr 1fr !important; gap: 4rem !important; align-items: center !important; }
#hh-page .discover-media { position: relative !important; }
#hh-page .discover-media > img {
  border-radius: 1.5rem !important; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.15) !important;
  border: 6px solid var(--hh-slate-50) !important; display: block !important; width: 100% !important;
}
#hh-page .discover-badges {
  position: absolute !important; bottom: -1.5rem !important; left: 50% !important; transform: translateX(-50%) !important;
  display: flex !important; align-items: center !important; gap: 1.5rem !important;
  background: #fff !important; padding: 1rem 2rem !important;
  border-radius: 1rem !important; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1) !important;
  white-space: nowrap !important;
}
#hh-page .badge-stat { text-align: center !important; }
#hh-page .badge-stat .num { font-size: 1.5rem !important; font-weight: 900 !important; color: var(--hh-blue-700) !important; line-height: 1.2 !important; }
#hh-page .badge-stat .label { font-size: 0.6875rem !important; font-weight: 600 !important; color: var(--hh-slate-500) !important; text-transform: uppercase !important; letter-spacing: 0.05em !important; }
#hh-page .discover-badges .divider { width: 1px !important; height: 2.5rem !important; background: var(--hh-slate-200) !important; }
#hh-page .section-tag {
  display: inline-flex !important; background: var(--hh-blue-50) !important; color: var(--hh-blue-700) !important;
  font-size: 0.6875rem !important; font-weight: 700 !important; text-transform: uppercase !important;
  letter-spacing: 0.08em !important; padding: 0.375rem 1rem !important; border-radius: 9999px !important;
  margin-bottom: 1rem !important;
}
#hh-page .discover-text h2 {
  font-size: clamp(1.75rem, 3vw, 2.5rem) !important; font-weight: 900 !important;
  line-height: 1.15 !important; letter-spacing: -0.02em !important; color: var(--hh-slate-900) !important; margin-bottom: 1rem !important;
}
#hh-page .discover-text > p { color: var(--hh-slate-600) !important; font-size: 1rem !important; line-height: 1.75 !important; margin-bottom: 1.5rem !important; }
#hh-page .discover-features { display: flex !important; flex-direction: column !important; gap: 1.25rem !important; margin-bottom: 1.5rem !important; }
#hh-page .discover-feature-item { display: flex !important; gap: 1rem !important; align-items: flex-start !important; }
#hh-page .discover-feature-icon {
  width: 2.5rem !important; height: 2.5rem !important; border-radius: 0.625rem !important;
  background: var(--hh-blue-50) !important; color: var(--hh-blue-600) !important;
  display: flex !important; align-items: center !important; justify-content: center !important; flex-shrink: 0 !important;
}
#hh-page .discover-feature-icon svg { width: 1.25rem !important; height: 1.25rem !important; }
#hh-page .discover-feature-item h4 { font-size: 0.9375rem !important; font-weight: 700 !important; color: var(--hh-slate-900) !important; margin-bottom: 0.25rem !important; }
#hh-page .discover-feature-item p { font-size: 0.8125rem !important; color: var(--hh-slate-500) !important; line-height: 1.5 !important; }
#hh-page .discover-link {
  display: inline-flex !important; align-items: center !important; gap: 0.5rem !important;
  color: var(--hh-blue-700) !important; font-weight: 700 !important; font-size: 0.9375rem !important;
  transition: gap 0.3s ease !important;
}
#hh-page .discover-link:hover { gap: 0.75rem !important; }
#hh-page .discover-link svg { width: 1.25rem !important; height: 1.25rem !important; }

/* ====== ABOUT SECTION ====== */
#hh-page .about-section { padding: clamp(4rem, 8vw, 7rem) 0 !important; background: #fff !important; display: block !important; }
#hh-page .about-grid { display: grid !important; grid-template-columns: 1fr 1fr !important; gap: 4rem !important; align-items: center !important; }
#hh-page .about-text h2 {
  font-size: clamp(1.75rem, 3vw, 2.5rem) !important; font-weight: 900 !important;
  line-height: 1.15 !important; letter-spacing: -0.02em !important; color: var(--hh-slate-900) !important; margin-bottom: 1rem !important;
}
#hh-page .about-text > p { color: var(--hh-slate-600) !important; font-size: 1rem !important; line-height: 1.75 !important; margin-bottom: 1rem !important; }
#hh-page .about-video { position: relative !important; }
#hh-page .video-wrapper {
  position: relative !important; padding-bottom: 56.25% !important; height: 0 !important; overflow: hidden !important;
  border-radius: 1rem !important; box-shadow: 0 25px 50px -12px rgba(0,0,0,0.15) !important;
}
#hh-page .video-wrapper iframe {
  position: absolute !important; top: 0 !important; left: 0 !important;
  width: 100% !important; height: 100% !important; border: none !important; border-radius: 1rem !important;
}

/* ====== BENTO FEATURES ====== */
#hh-page .features-section { padding: clamp(4rem, 8vw, 7rem) 0 !important; background: var(--hh-slate-50) !important; display: block !important; }
#hh-page .section-header { text-align: center !important; margin-bottom: 3rem !important; }
#hh-page .section-header .overline {
  font-size: 0.6875rem !important; font-weight: 700 !important; text-transform: uppercase !important;
  letter-spacing: 0.1em !important; color: var(--hh-blue-700) !important; margin-bottom: 0.5rem !important;
}
#hh-page .section-header h2 {
  font-size: clamp(1.75rem, 4vw, 2.75rem) !important; font-weight: 900 !important;
  line-height: 1.15 !important; letter-spacing: -0.02em !important; color: var(--hh-slate-900) !important;
}
#hh-page .section-header > p { color: var(--hh-slate-500) !important; font-size: 1rem !important; margin-top: 0.5rem !important; }
#hh-page .bento-grid { display: grid !important; grid-template-columns: repeat(3, 1fr) !important; gap: 1.25rem !important; }
#hh-page .bento-card {
  background: #fff !important; border: 1px solid var(--hh-slate-200) !important;
  border-radius: 1.25rem !important; padding: 1.75rem !important;
  transition: all 0.35s ease !important; position: relative !important; overflow: hidden !important;
  display: block !important;
}
#hh-page .bento-card:hover { transform: translateY(-6px) !important; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.08) !important; }
#hh-page .bento-card.large { grid-row: span 2 !important; padding: 2.25rem !important; }
#hh-page .bento-card.wide { grid-column: span 3 !important; }
#hh-page .bg-pattern { position: absolute !important; top: -2rem !important; right: -2rem !important; opacity: 0.04 !important; width: 12rem !important; height: 12rem !important; }
#hh-page .bg-pattern svg { width: 100% !important; height: 100% !important; }
#hh-page .bento-icon {
  width: 2.75rem !important; height: 2.75rem !important; border-radius: 0.75rem !important;
  display: flex !important; align-items: center !important; justify-content: center !important;
  margin-bottom: 1rem !important; transition: all 0.3s ease !important;
}
#hh-page .bento-icon svg { width: 1.375rem !important; height: 1.375rem !important; }
#hh-page .bento-icon.blue { background: var(--hh-blue-50) !important; color: var(--hh-blue-600) !important; }
#hh-page .bento-card:hover .bento-icon.blue { background: var(--hh-blue-600) !important; color: #fff !important; }
#hh-page .bento-icon.indigo { background: var(--hh-indigo-50) !important; color: var(--hh-indigo-600) !important; }
#hh-page .bento-card:hover .bento-icon.indigo { background: var(--hh-indigo-600) !important; color: #fff !important; }
#hh-page .bento-icon.emerald { background: var(--hh-emerald-50) !important; color: var(--hh-emerald-600) !important; }
#hh-page .bento-card:hover .bento-icon.emerald { background: var(--hh-emerald-600) !important; color: #fff !important; }
#hh-page .bento-icon.amber { background: var(--hh-amber-50) !important; color: var(--hh-amber-600) !important; }
#hh-page .bento-card:hover .bento-icon.amber { background: var(--hh-amber-600) !important; color: #fff !important; }
#hh-page .bento-icon.purple { background: var(--hh-purple-50) !important; color: var(--hh-purple-600) !important; }
#hh-page .bento-card:hover .bento-icon.purple { background: var(--hh-purple-600) !important; color: #fff !important; }
#hh-page .bento-card h3 { font-size: 1.125rem !important; font-weight: 800 !important; color: var(--hh-slate-900) !important; margin-bottom: 0.5rem !important; letter-spacing: -0.01em !important; line-height: 1.3 !important; }
#hh-page .bento-card p { font-size: 0.875rem !important; color: var(--hh-slate-500) !important; line-height: 1.7 !important; }
#hh-page .check-list { margin-top: 1rem !important; }
#hh-page .check-list li {
  display: flex !important; align-items: center !important; gap: 0.5rem !important;
  font-size: 0.8125rem !important; font-weight: 500 !important; color: var(--hh-slate-700) !important;
  padding: 0.375rem 0 !important;
}
#hh-page .check-list li svg { width: 1rem !important; height: 1rem !important; color: var(--hh-emerald-600) !important; flex-shrink: 0 !important; }
#hh-page .card-link {
  display: inline-flex !important; align-items: center !important; gap: 0.375rem !important;
  color: var(--hh-blue-700) !important; font-weight: 700 !important; font-size: 0.8125rem !important;
  margin-top: 0.75rem !important; transition: gap 0.3s ease !important;
}
#hh-page .card-link:hover { gap: 0.625rem !important; }
#hh-page .card-link svg { width: 1rem !important; height: 1rem !important; }

/* ====== PROCESS ====== */
#hh-page .process-section { padding: clamp(4rem, 8vw, 7rem) 0 !important; display: block !important; background: #fff !important; }
#hh-page .steps-wrapper { position: relative !important; margin-top: 3rem !important; }
#hh-page .steps-line {
  position: absolute !important; top: 1.75rem !important; left: 10% !important; right: 10% !important;
  height: 2px !important; background: linear-gradient(to right, var(--hh-blue-200), var(--hh-blue-500), var(--hh-emerald-600)) !important;
  display: block !important;
}
#hh-page .steps-grid { display: grid !important; grid-template-columns: repeat(4, 1fr) !important; gap: 2rem !important; position: relative !important; }
#hh-page .step-item { text-align: center !important; }
#hh-page .step-circle {
  width: 3.5rem !important; height: 3.5rem !important; border-radius: 50% !important;
  background: var(--hh-blue-700) !important; color: #fff !important;
  display: flex !important; align-items: center !important; justify-content: center !important;
  font-size: 1.125rem !important; font-weight: 800 !important;
  margin: 0 auto 1.25rem !important; box-shadow: 0 4px 14px rgba(29,78,216,0.3) !important;
  position: relative !important; z-index: 1 !important;
}
#hh-page .step-circle svg { width: 1.25rem !important; height: 1.25rem !important; }
#hh-page .step-item:last-child .step-circle { background: var(--hh-emerald-600) !important; box-shadow: 0 4px 14px rgba(5,150,105,0.3) !important; }
#hh-page .step-item h3 { font-size: 1rem !important; font-weight: 800 !important; color: var(--hh-slate-900) !important; margin-bottom: 0.5rem !important; }
#hh-page .step-item p { font-size: 0.8125rem !important; color: var(--hh-slate-500) !important; line-height: 1.6 !important; }

/* ====== INDUSTRIES ====== */
#hh-page .industries-section {
  padding: clamp(4rem, 8vw, 7rem) 0 !important;
  background: var(--hh-slate-900) !important; color: #fff !important; position: relative !important; overflow: hidden !important;
  display: block !important;
}
#hh-page .bg-grid { position: absolute !important; inset: 0 !important; opacity: 0.04 !important; color: #fff !important; }
#hh-page .industries-section .section-header .overline { color: var(--hh-blue-200) !important; }
#hh-page .industries-section .section-header h2 { color: #fff !important; }
#hh-page .industries-section .section-header h2 a { color: #fff !important; }
#hh-page .industries-section .section-header > p { color: var(--hh-slate-400) !important; }
#hh-page .industries-grid { display: grid !important; grid-template-columns: repeat(3, 1fr) !important; gap: 1.25rem !important; position: relative !important; z-index: 1 !important; }
#hh-page .industry-card {
  display: block !important; background: rgba(255,255,255,0.04) !important;
  border: 1px solid rgba(255,255,255,0.08) !important;
  border-radius: 1rem !important; padding: 1.75rem !important;
  transition: all 0.35s ease !important;
}
#hh-page .industry-card:hover {
  background: rgba(255,255,255,0.08) !important;
  border-color: rgba(255,255,255,0.15) !important;
  transform: translateY(-4px) !important;
}
#hh-page .card-icon {
  width: 3rem !important; height: 3rem !important; border-radius: 0.75rem !important;
  background: rgba(96,165,250,0.1) !important; color: #60a5fa !important;
  display: flex !important; align-items: center !important; justify-content: center !important;
  margin-bottom: 1rem !important;
}
#hh-page .industry-card:hover .card-icon { background: var(--hh-blue-600) !important; color: #fff !important; }
#hh-page .industry-card h3 { font-size: 1.0625rem !important; font-weight: 700 !important; margin-bottom: 0.5rem !important; color: #fff !important; }
#hh-page .industry-card p { font-size: 0.8125rem !important; color: var(--hh-slate-400) !important; line-height: 1.6 !important; }

/* ====== TEAM ====== */
#hh-page .team-section { padding: clamp(4rem, 8vw, 7rem) 0 !important; text-align: center !important; display: block !important; background: #fff !important; }
#hh-page .team-section h2 { font-size: clamp(1.75rem, 3.5vw, 2.5rem) !important; font-weight: 900 !important; letter-spacing: -0.02em !important; color: var(--hh-slate-900) !important; }
#hh-page .team-section .subtitle { color: var(--hh-slate-500) !important; margin-top: 0.5rem !important; margin-bottom: 3rem !important; font-size: 1rem !important; }
#hh-page .team-grid { display: flex !important; justify-content: center !important; gap: 2rem !important; flex-wrap: wrap !important; }
#hh-page .team-card {
  background: #fff !important; border: 1px solid var(--hh-slate-200) !important;
  border-radius: 1.25rem !important; padding: 1.75rem !important; text-align: center !important;
  width: 220px !important; transition: all 0.35s ease !important; position: relative !important;
}
#hh-page .team-card:hover { transform: translateY(-6px) !important; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.08) !important; }
#hh-page .team-card img { width: 80px !important; height: 80px !important; border-radius: 50% !important; object-fit: cover !important; margin-bottom: 1rem !important; display: block !important; margin-left: auto !important; margin-right: auto !important; }
#hh-page .team-info h4 { font-size: 1rem !important; font-weight: 700 !important; color: var(--hh-slate-900) !important; }
#hh-page .team-info p { font-size: 0.8125rem !important; color: var(--hh-slate-500) !important; }
#hh-page .linkedin-icon {
  display: inline-flex !important; align-items: center !important; justify-content: center !important;
  width: 2rem !important; height: 2rem !important; border-radius: 0.5rem !important;
  background: var(--hh-blue-50) !important; color: var(--hh-blue-600) !important;
  margin-top: 0.75rem !important; transition: all 0.3s ease !important; font-size: 0.875rem !important;
}
#hh-page .linkedin-icon:hover { background: var(--hh-blue-600) !important; color: #fff !important; }

/* ====== TESTIMONIAL ====== */
#hh-page .testimonial-section { padding: clamp(4rem, 8vw, 7rem) 0 !important; background: var(--hh-slate-50) !important; display: block !important; }
#hh-page .testimonial-card {
  display: flex !important; gap: 2.5rem !important; align-items: center !important;
  background: #fff !important; border: 1px solid var(--hh-slate-200) !important;
  border-radius: 1.5rem !important; padding: 2.5rem !important;
  box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05) !important;
  max-width: 900px !important; margin: 0 auto !important;
}
#hh-page .testimonial-photo {
  width: 180px !important; height: 180px !important; border-radius: 1rem !important;
  object-fit: cover !important; flex-shrink: 0 !important; display: block !important;
}
#hh-page .quote-icon { color: var(--hh-blue-200) !important; font-size: 2rem !important; margin-bottom: 0.75rem !important; }
#hh-page .testimonial-text blockquote {
  font-size: 1.0625rem !important; line-height: 1.75 !important; color: var(--hh-slate-700) !important;
  font-style: italic !important; margin: 0 0 1rem 0 !important;
  border: none !important; background: none !important; padding: 0 !important;
}
#hh-page .testimonial-author { font-size: 0.875rem !important; color: var(--hh-slate-500) !important; }
#hh-page .testimonial-author strong { color: var(--hh-slate-900) !important; font-weight: 700 !important; }

/* ====== FAQ CARDS + DRAWER ====== */
#hh-page .faq-section { padding: clamp(4rem, 8vw, 7rem) 0 !important; display: block !important; background: #fff !important; }
#hh-page .faq-cards-grid { display: grid !important; grid-template-columns: repeat(2, 1fr) !important; gap: 1.25rem !important; max-width: 960px !important; margin: 0 auto !important; }
#hh-page .faq-card {
  display: flex !important; align-items: center !important; justify-content: space-between !important;
  background: #fff !important; border: 1px solid var(--hh-slate-200) !important;
  border-radius: 1.25rem !important; padding: 1.75rem !important;
  cursor: pointer !important; transition: all 0.35s ease !important;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
}
#hh-page .faq-card:hover {
  transform: translateY(-6px) !important;
  box-shadow: 0 20px 40px -10px rgba(30,58,138,0.15) !important;
  border-color: var(--hh-blue-300, #93c5fd) !important;
}
#hh-page .faq-card-inner { flex: 1 !important; }
#hh-page .faq-card-emoji {
  width: 2.75rem !important; height: 2.75rem !important; border-radius: 0.75rem !important;
  background: var(--hh-blue-50) !important; color: var(--hh-blue-600) !important;
  display: flex !important; align-items: center !important; justify-content: center !important;
  margin-bottom: 1rem !important; transition: all 0.3s ease !important;
}
#hh-page .faq-card-emoji svg { width: 1.375rem !important; height: 1.375rem !important; }
#hh-page .faq-card:hover .faq-card-emoji { background: var(--hh-blue-600) !important; color: #fff !important; }
#hh-page .faq-card-question { display: block !important; font-weight: 800 !important; font-size: 1rem !important; color: var(--hh-slate-900) !important; line-height: 1.4 !important; margin-bottom: 0.5rem !important; letter-spacing: -0.01em !important; }
#hh-page .faq-card-meta { display: block !important; font-size: 0.8125rem !important; color: var(--hh-slate-400) !important; font-weight: 500 !important; }
#hh-page .faq-card-arrow {
  width: 2.5rem !important; height: 2.5rem !important; flex-shrink: 0 !important;
  border-radius: 50% !important; background: var(--hh-slate-100) !important;
  display: flex !important; align-items: center !important; justify-content: center !important;
  margin-left: 1rem !important; transition: all 0.3s ease !important;
}
#hh-page .faq-card-arrow svg { width: 1.125rem !important; height: 1.125rem !important; color: var(--hh-slate-400) !important; transition: all 0.3s ease !important; }
#hh-page .faq-card:hover .faq-card-arrow { background: var(--hh-blue-600) !important; }
#hh-page .faq-card:hover .faq-card-arrow svg { color: #fff !important; transform: translateX(2px) !important; }

/* FAQ Drawer overlay */
#hh-page .faq-drawer-overlay,
.faq-drawer-overlay {
  position: fixed !important; inset: 0 !important; background: rgba(0,0,0,0.5) !important;
  z-index: 100000 !important; opacity: 0 !important; visibility: hidden !important;
  transition: all 0.3s ease !important;
}
#hh-page .faq-drawer-overlay.open,
.faq-drawer-overlay.open { opacity: 1 !important; visibility: visible !important; }

/* FAQ Drawer panel */
#hh-page .faq-drawer,
.faq-drawer {
  position: fixed !important; top: 0 !important; right: 0 !important; bottom: 0 !important;
  width: 540px !important; max-width: 90vw !important;
  background: #fff !important; z-index: 100001 !important;
  transform: translateX(100%) !important; transition: transform 0.35s cubic-bezier(0.4,0,0.2,1) !important;
  overflow-y: auto !important; box-shadow: -10px 0 40px rgba(0,0,0,0.15) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  color: #0f172a !important; line-height: 1.6 !important; font-size: 16px !important;
}
#hh-page .faq-drawer.open,
.faq-drawer.open { transform: translateX(0) !important; }
#hh-page .faq-drawer-close,
.faq-drawer-close {
  position: absolute !important; top: 1.25rem !important; right: 1.25rem !important;
  width: 2.5rem !important; height: 2.5rem !important; border-radius: 50% !important;
  background: var(--hh-slate-100) !important; border: none !important; cursor: pointer !important;
  display: flex !important; align-items: center !important; justify-content: center !important;
  transition: all 0.3s ease !important; z-index: 2 !important;
}
.faq-drawer-close svg { width: 1.25rem !important; height: 1.25rem !important; color: var(--hh-slate-600) !important; }
.faq-drawer-close:hover { background: var(--hh-slate-200) !important; }
#hh-page .faq-drawer-content,
.faq-drawer-content { padding: 3rem 2.5rem 2rem !important; }
.faq-drawer-content h2 {
  font-size: 1.5rem !important; font-weight: 900 !important; color: #1e3a8a !important;
  line-height: 1.25 !important; margin-bottom: 1.5rem !important; padding-right: 2rem !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}
.faq-drawer-content h3 {
  font-size: 1.25rem !important; font-weight: 800 !important; color: #0f172a !important;
  margin-bottom: 1rem !important; line-height: 1.3 !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}
.faq-drawer-content h4 {
  font-size: 1.0625rem !important; font-weight: 700 !important; color: #1e3a8a !important;
  margin-top: 1.5rem !important; margin-bottom: 0.75rem !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}
.faq-drawer-content p {
  font-size: 0.9375rem !important; color: #475569 !important; line-height: 1.75 !important;
  margin-bottom: 0.75rem !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}
.faq-drawer-content ul { margin: 0.5rem 0 1rem !important; padding: 0 !important; list-style: none !important; }
.faq-drawer-content ul li {
  font-size: 0.9375rem !important; color: #475569 !important; padding: 0.375rem 0 !important;
  padding-left: 1.5rem !important; position: relative !important; line-height: 1.7 !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}
.faq-drawer-content ul li::before {
  content: '' !important; position: absolute !important; left: 0 !important; top: 0.75rem !important;
  width: 6px !important; height: 6px !important; border-radius: 50% !important; background: #3b82f6 !important;
}
.faq-drawer-content strong { color: #0f172a !important; font-weight: 700 !important; }
.faq-drawer-content a { color: #1d4ed8 !important; text-decoration: underline !important; font-weight: 600 !important; }
.faq-drawer-content a:hover { color: #1e3a8a !important; }
.faq-drawer-content table {
  width: 100% !important; border-collapse: collapse !important; margin: 1rem 0 1.5rem !important;
  font-size: 0.875rem !important; border-radius: 0.75rem !important; overflow: hidden !important;
  border: 1px solid #e2e8f0 !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}
.faq-drawer-content thead { background: #1e3a8a !important; }
.faq-drawer-content thead th {
  color: #fff !important; font-weight: 700 !important; padding: 0.75rem 1rem !important;
  text-align: left !important; font-size: 0.8125rem !important; text-transform: uppercase !important;
  letter-spacing: 0.03em !important;
}
.faq-drawer-content tbody tr { border-bottom: 1px solid #e2e8f0 !important; }
.faq-drawer-content tbody tr:nth-child(even) { background: #f8fafc !important; }
.faq-drawer-content tbody td {
  padding: 0.625rem 1rem !important; color: #475569 !important; line-height: 1.5 !important;
}

/* ====== REVIEWS ====== */
#hh-page .reviews-section { padding: clamp(4rem, 8vw, 7rem) 0 !important; background: var(--hh-slate-50) !important; display: block !important; }
#hh-page .reviews-rating { display: flex !important; align-items: center !important; justify-content: center !important; gap: 0.75rem !important; margin-top: 1rem !important; }
#hh-page .reviews-rating .stars { color: #facc15 !important; font-size: 1.25rem !important; display: flex !important; gap: 0.125rem !important; }
#hh-page .reviews-rating .rating-text { font-size: 1rem !important; font-weight: 600 !important; color: var(--hh-slate-600) !important; }
#hh-page .reviews-grid { display: grid !important; grid-template-columns: repeat(4, 1fr) !important; gap: 1.25rem !important; margin-top: 3rem !important; }
#hh-page .review-card {
  background: #fff !important; border: 1px solid var(--hh-slate-200) !important;
  border-radius: 1rem !important; padding: 1.5rem !important;
  transition: all 0.35s ease !important; display: flex !important; flex-direction: column !important;
}
#hh-page .review-card:hover { transform: translateY(-4px) !important; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.08) !important; }
#hh-page .review-header { display: flex !important; align-items: center !important; gap: 0.75rem !important; margin-bottom: 1rem !important; }
#hh-page .review-avatar {
  width: 2.75rem !important; height: 2.75rem !important; border-radius: 50% !important;
  background: var(--hh-blue-700) !important; color: #fff !important;
  display: flex !important; align-items: center !important; justify-content: center !important;
  font-weight: 700 !important; font-size: 0.875rem !important; flex-shrink: 0 !important;
}
#hh-page .review-name { font-weight: 700 !important; font-size: 0.9375rem !important; color: var(--hh-slate-900) !important; }
#hh-page .review-stars { color: #facc15 !important; font-size: 0.75rem !important; display: flex !important; gap: 0.0625rem !important; }
#hh-page .review-text { font-size: 0.875rem !important; color: var(--hh-slate-600) !important; line-height: 1.7 !important; flex: 1 !important; }
#hh-page .review-source { margin-top: 1rem !important; font-size: 0.75rem !important; color: var(--hh-slate-400) !important; font-weight: 500 !important; display: flex !important; align-items: center !important; gap: 0.375rem !important; }

/* ====== CTA BANNER ====== */
#hh-page .cta-banner {
  padding: clamp(4rem, 8vw, 6rem) 0 !important;
  background: linear-gradient(135deg, var(--hh-blue-900), var(--hh-blue-700)) !important;
  display: block !important;
}
#hh-page .cta-banner-inner { text-align: center !important; color: #fff !important; }
#hh-page .cta-banner-inner h2 {
  font-size: clamp(1.75rem, 3.5vw, 2.5rem) !important; font-weight: 900 !important;
  margin-bottom: 0.75rem !important; letter-spacing: -0.02em !important; color: #fff !important;
}
#hh-page .cta-banner-inner > p { color: var(--hh-blue-200) !important; font-size: 1.0625rem !important; margin-bottom: 2rem !important; }
#hh-page .cta-infos { display: flex !important; justify-content: center !important; gap: 2rem !important; flex-wrap: wrap !important; }
#hh-page .info-item {
  display: flex !important; align-items: center !important; gap: 0.5rem !important;
  color: rgba(255,255,255,0.85) !important; font-size: 0.875rem !important; font-weight: 500 !important;
}
#hh-page .info-item svg { width: 1.25rem !important; height: 1.25rem !important; color: var(--hh-blue-200) !important; }

/* ====== FOOTER ====== */
#hh-page footer {
  background: var(--hh-slate-900) !important; padding: 4rem 0 2rem !important; color: var(--hh-slate-400) !important;
  display: block !important; visibility: visible !important; height: auto !important;
  position: relative !important; overflow: visible !important; pointer-events: auto !important;
  opacity: 1 !important;
}
#hh-page .footer-grid { display: grid !important; grid-template-columns: 1.5fr 1fr 1fr 1fr !important; gap: 3rem !important; margin-bottom: 3rem !important; }
#hh-page .footer-brand img { height: 36px !important; margin-bottom: 1rem !important; display: block !important; }
#hh-page .footer-brand p { font-size: 0.8125rem !important; line-height: 1.7 !important; color: var(--hh-slate-400) !important; }
#hh-page .social-icons { display: flex !important; gap: 0.5rem !important; margin-bottom: 1rem !important; }
#hh-page .social-icons a {
  width: 2.25rem !important; height: 2.25rem !important; border-radius: 0.5rem !important;
  background: rgba(255,255,255,0.06) !important;
  display: flex !important; align-items: center !important; justify-content: center !important;
  color: #fff !important; transition: all 0.3s ease !important; font-size: 0.875rem !important;
}
#hh-page .social-icons a:hover { background: var(--hh-blue-700) !important; transform: translateY(-2px) !important; }
#hh-page .footer-col h4 {
  font-size: 0.6875rem !important; font-weight: 700 !important; text-transform: uppercase !important;
  letter-spacing: 0.1em !important; color: #fff !important; margin-bottom: 1rem !important; line-height: 1.4 !important;
}
#hh-page .footer-col ul li { margin-bottom: 0.5rem !important; }
#hh-page .footer-col ul li a { color: var(--hh-slate-400) !important; font-size: 0.8125rem !important; font-weight: 500 !important; transition: color 0.3s !important; }
#hh-page .footer-col ul li a:hover { color: #fff !important; }
#hh-page .footer-bottom {
  border-top: 1px solid rgba(255,255,255,0.06) !important;
  padding-top: 1.5rem !important; display: flex !important; gap: 2rem !important; flex-wrap: wrap !important;
}
#hh-page .footer-bottom a { color: var(--hh-slate-500) !important; font-size: 0.75rem !important; font-weight: 500 !important; transition: color 0.3s !important; }
#hh-page .footer-bottom a:hover { color: var(--hh-slate-300) !important; }

/* ====== STICKY CTA ====== */
#hh-page .sticky-cta {
  position: fixed !important; bottom: 1.25rem !important; left: 50% !important; transform: translateX(-50%) !important;
  z-index: 9998 !important;
}
#hh-page .sticky-cta a {
  display: inline-flex !important; align-items: center !important;
  background: var(--hh-blue-700) !important; color: #fff !important;
  padding: 0.875rem 2rem !important; border-radius: 1rem !important;
  font-weight: 800 !important; font-size: 0.9375rem !important;
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25), 0 8px 24px rgba(29,78,216,0.4) !important;
  border: 1px solid var(--hh-blue-600) !important;
  transition: all 0.3s ease !important;
}
#hh-page .sticky-cta a:hover { background: var(--hh-blue-800) !important; transform: translateY(-2px) !important; }

/* ====== RESPONSIVE ====== */
@media (max-width: 1024px) {
  #hh-page .desktop-nav, #hh-page .header-actions { display: none !important; }
  #hh-page .hamburger-btn { display: block !important; }
  #hh-page .mobile-menu { display: block !important; }
  #hh-page .hero-grid { grid-template-columns: 1fr !important; text-align: center !important; }
  #hh-page .hero-description { margin-left: auto !important; margin-right: auto !important; }
  #hh-page .hero-badge { justify-content: center !important; }
  #hh-page .about-grid { grid-template-columns: 1fr !important; }
  #hh-page .about-video { margin-top: 2rem !important; }
  #hh-page .discover-grid { grid-template-columns: 1fr !important; }
  #hh-page .discover-media { margin-bottom: 2rem !important; }
  #hh-page .bento-grid { grid-template-columns: 1fr 1fr !important; }
  #hh-page .bento-card.large { grid-row: span 1 !important; }
  #hh-page .bento-card.wide { grid-column: span 2 !important; }
  #hh-page .steps-grid { grid-template-columns: repeat(2, 1fr) !important; }
  #hh-page .steps-line { display: none !important; }
  #hh-page .industries-grid { grid-template-columns: repeat(2, 1fr) !important; }
  #hh-page .reviews-grid { grid-template-columns: repeat(2, 1fr) !important; }
  #hh-page .footer-grid { grid-template-columns: 1fr 1fr !important; }
}

@media (max-width: 640px) {
  #hh-page .container { padding: 0 1rem !important; }
  #hh-page .hero-section { padding-top: 172px !important; padding-bottom: 60px !important; }
  #hh-page .hero-title { font-size: 2rem !important; }
  #hh-page .about-grid { grid-template-columns: 1fr !important; }
  #hh-page .bento-grid { grid-template-columns: 1fr !important; }
  #hh-page .bento-card.wide { grid-column: span 1 !important; }
  #hh-page .steps-grid { grid-template-columns: 1fr 1fr !important; }
  #hh-page .industries-grid { grid-template-columns: 1fr !important; }
  #hh-page .reviews-grid { grid-template-columns: 1fr !important; }
  #hh-page .faq-cards-grid { grid-template-columns: 1fr !important; }
  #hh-page .testimonial-card { flex-direction: column !important; text-align: center !important; padding: 1.5rem !important; }
  #hh-page .testimonial-photo { width: 120px !important; height: 120px !important; }
  #hh-page .footer-grid { grid-template-columns: 1fr !important; gap: 2rem !important; }
  #hh-page .cta-infos { flex-direction: column !important; align-items: center !important; }
  #hh-page .discover-badges { padding: 0.75rem 1.25rem !important; gap: 1rem !important; }
  #hh-page .team-card { width: 100% !important; }
  .faq-drawer-content { padding: 2.5rem 1.5rem 1.5rem !important; }
}

/* ====== ANNOUNCEMENT BANNER ====== */
#hh-page .announcement-bar {
  position: fixed !important; top: 0 !important; left: 0 !important; right: 0 !important;
  z-index: 100000 !important;
  background: linear-gradient(90deg, #7c3aed, #1d4ed8, #0891b2) !important;
  padding: 0 1rem !important; text-align: center !important;
  display: flex !important; align-items: center !important; justify-content: center !important; gap: 0.75rem !important;
  height: 40px !important;
}
#hh-page .announcement-bar .ann-badge {
  background: rgba(255,255,255,0.2) !important; color: #fff !important;
  font-size: 0.625rem !important; font-weight: 800 !important; text-transform: uppercase !important;
  letter-spacing: 0.08em !important; padding: 0.1875rem 0.625rem !important;
  border-radius: 9999px !important; white-space: nowrap !important;
}
#hh-page .announcement-bar .ann-text {
  color: rgba(255,255,255,0.9) !important; font-size: 0.8125rem !important; font-weight: 500 !important;
}
#hh-page .announcement-bar .ann-cta {
  background: #fff !important; color: #1d4ed8 !important;
  font-size: 0.75rem !important; font-weight: 700 !important;
  padding: 0.3125rem 0.875rem !important; border-radius: 9999px !important;
  white-space: nowrap !important; transition: all 0.3s ease !important;
}
#hh-page .announcement-bar .ann-cta:hover {
  background: rgba(255,255,255,0.9) !important; transform: scale(1.05) !important;
}
"""

# ── Wrap body content in #hh-page div ──
wrapped_html = f'<div id="hh-page">\n{body_content}\n</div>'

# ── Build full content ──
full_content = f"""<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
{CSS}
</style>
{wrapped_html}"""

# ── Wrap in wp:html block ──
wp_content = f'<!-- wp:html -->\n{full_content}\n<!-- /wp:html -->'

# ── Deploy ──
print("=" * 60)
print("DEPLOYING HOMEPAGE v4 — COMPLETE WITH REVIEWS + FAQ DRAWER")
print("=" * 60)

response = requests.post(
    f"{WP_URL}/pages/{PAGE_ID}",
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
        'Our CSS vars': '--hh-blue-900' in rendered,
        'z-index 99999': 'z-index: 99999' in rendered or 'z-index:99999' in rendered,
        'Nuclear reset': 'elementor-location-header' in rendered,
        'Header': 'site-header' in rendered,
        'Hero centered': 'hero-content-centered' in rendered,
        'About section': 'about-section' in rendered,
        'Bento': 'bento-grid' in rendered,
        'Industries': 'industries-section' in rendered,
        'Team': 'team-section' in rendered,
        'Reviews': 'reviews-section' in rendered,
        'FAQ drawer': 'faq-drawer' in rendered,
        'Footer': 'footer-grid' in rendered,
        'Sticky CTA': 'sticky-cta' in rendered,
        'JS script': 'hamburgerBtn' in rendered,
        'No Elementor render': 'elementor-element-4021e48' not in rendered,
    }
    for name, ok in checks.items():
        print(f"  {'✓' if ok else '✗'} {name}")

    all_ok = all(checks.values())
    print(f"\n{'ALL CHECKS PASSED' if all_ok else 'SOME CHECKS FAILED'}")
else:
    print(f"ERROR {response.status_code}")
    print(response.text[:1000])
