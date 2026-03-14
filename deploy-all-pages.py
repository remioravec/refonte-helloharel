#!/usr/bin/env python3
"""
Deploy all 16 mega-menu pages with UNIQUE content per page.
Structure = homepage design system, but bento/hero/FAQ customized per page.
"""

import json, re, sys, requests, time
from requests.auth import HTTPBasicAuth

WP_URL = "https://www.helloharel.com/prometheus/wp-json/wp/v2"
AUTH = HTTPBasicAuth("administration@remi-oravec.fr", "T8Yu 6UBr 1BOh H3i2 PNSw khHk")

# ── Load CSS from deploy-homepage.py ──
with open('/workspaces/refonte-helloharel/deploy-homepage.py', 'r') as f:
    deploy_script = f.read()
css_match = re.search(r'CSS = r"""(.*?)"""', deploy_script, re.DOTALL)
CSS = css_match.group(1)

# ── SVG ICONS (reusable) ──
I = {
    "users": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg>',
    "doc": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>',
    "dollar": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>',
    "box": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>',
    "gear": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>',
    "cart": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/></svg>',
    "arrows": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"/></svg>',
    "globe": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>',
    "shield": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>',
    "chart": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>',
    "clock": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>',
    "check": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>',
    "bell": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/></svg>',
    "truck": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16V6a1 1 0 00-1-1H4a1 1 0 00-1 1v10a1 1 0 001 1h1m8-1a1 1 0 01-1 1H9m4-1V8a1 1 0 011-1h2.586a1 1 0 01.707.293l3.414 3.414a1 1 0 01.293.707V16a1 1 0 01-1 1h-1m-6-1a1 1 0 001 1h1M5 17a2 2 0 104 0m-4 0a2 2 0 114 0m6 0a2 2 0 104 0m-4 0a2 2 0 114 0"/></svg>',
    "clipboard": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"/></svg>',
    "database": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4"/></svg>',
    "tag": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"/></svg>',
    "fire": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.879 16.121A3 3 0 1012.015 11L11 14H9c0 .768.293 1.536.879 2.121z"/></svg>',
    "leaf": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 2c-1 3-4 5-4 9a4 4 0 008 0c0-4-3-6-4-9zM8 15l-2 6h12l-2-6"/></svg>',
    "bread": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 18c0 1 1.5 3 7 3s7-2 7-3c0-2-3-3-7-3s-7 1-7 3zM5 18c-1-2 0-5 2-7 1.5-1.5 3-2 5-2s3.5.5 5 2c2 2 3 5 2 7"/></svg>',
    "knife": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 3l-1.5 1.5M9 9l-6 6c-1 1-1 2.5 0 3.5l2 2c1 1 2.5 1 3.5 0l6-6M18 6c1.5-1.5 1.5-4 0-5.5s-4 0-5.5 0L9 4l3 3 3 3 3.5-3.5z"/></svg>',
    "bottle": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 2h8l1 4H7L8 2zM7 6v2c0 1-1 2-1 3v7a2 2 0 002 2h8a2 2 0 002-2v-7c0-1-1-2-1-3V6"/></svg>',
    "plate": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 13h18M5 13c0-4 3-7 7-7s7 3 7 7M4 13v1a1 1 0 001 1h14a1 1 0 001-1v-1"/></svg>',
    "thermo": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9V3m0 6a3 3 0 100 6 3 3 0 000-6zm0 6v6"/></svg>',
    "scale": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"/></svg>',
    "calendar": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>',
    "search": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>',
    "link": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"/></svg>',
    "warehouse": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>',
    "list": '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/></svg>',
}

# ── SHARED HTML SECTIONS (from index.html) ──

HEADER = '''<!-- ANNOUNCEMENT BAR -->
<div class="announcement-bar">
    <span class="ann-badge">Nouveau</span>
    <span class="ann-text">L'intelligence artificielle arrive dans votre ERP</span>
    <a href="/prometheus/erp-ia/" class="ann-cta">Découvrir l'ERP IA →</a>
</div>

<!-- HEADER -->
<header class="site-header">
    <div class="container header-inner">
        <a href="/prometheus/" class="logo"><img loading="eager" src="https://www.helloharel.com/wp-content/uploads/2019/05/hello-harel-logo-white.svg" alt="Hello Harel - ERP Agroalimentaire"></a>
        <nav class="desktop-nav">
            <a href="/prometheus/">Accueil</a>
            <div class="nav-dropdown">
                <button class="nav-dropdown-trigger">Fonctionnalités <svg class="chevron-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></button>
                <div class="dropdown-panel" style="width:380px;max-width:95vw">
                    <div class="dropdown-card">
                        <a href="/prometheus/fonctionnalites/crm/" class="dropdown-link"><div class="dropdown-link-icon blue">''' + I["users"] + '''</div><span class="dropdown-link-text">Gestion de la relation client</span></a>
                        <a href="/prometheus/fonctionnalites/facturation/" class="dropdown-link"><div class="dropdown-link-icon indigo">''' + I["doc"] + '''</div><span class="dropdown-link-text">Gestion de la facturation</span></a>
                        <a href="/prometheus/fonctionnalites/vente/" class="dropdown-link"><div class="dropdown-link-icon emerald">''' + I["dollar"] + '''</div><span class="dropdown-link-text">Gestion commerciale</span></a>
                        <a href="/prometheus/fonctionnalites/gestion-de-stock/" class="dropdown-link"><div class="dropdown-link-icon amber">''' + I["box"] + '''</div><span class="dropdown-link-text">Gestion des stocks</span></a>
                        <a href="/prometheus/fonctionnalites/fabrication/" class="dropdown-link"><div class="dropdown-link-icon red">''' + I["gear"] + '''</div><span class="dropdown-link-text">Gestion de la fabrication</span></a>
                        <a href="/prometheus/fonctionnalites/achat/" class="dropdown-link"><div class="dropdown-link-icon teal">''' + I["cart"] + '''</div><span class="dropdown-link-text">Gestion des achats</span></a>
                        <a href="/prometheus/fonctionnalites/logistique/" class="dropdown-link"><div class="dropdown-link-icon cyan">''' + I["arrows"] + '''</div><span class="dropdown-link-text">Gestion de la logistique</span></a>
                        <a href="/prometheus/fonctionnalites/import-export/" class="dropdown-link"><div class="dropdown-link-icon orange">''' + I["globe"] + '''</div><span class="dropdown-link-text">Gestion des imports exports</span></a>
                    </div>
                </div>
            </div>
            <div class="nav-dropdown">
                <button class="nav-dropdown-trigger">Industries <svg class="chevron-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></button>
                <div class="dropdown-panel mega-industries-card">
                    <div class="dropdown-card" style="padding:0;overflow:hidden">
                        <div class="mega-industries-inner">
                            <h5>''' + I["scale"] + ''' Agroalimentaire</h5>
                            <a href="/prometheus/agroalimentaire/" class="industry-link"><div class="industry-link-icon">''' + I["shield"] + '''</div><span>ERP Agroalimentaire</span></a>
                            <a href="/prometheus/agroalimentaire/traiteur/" class="industry-link"><div class="industry-link-icon">''' + I["fire"] + '''</div><span>ERP Traiteur</span></a>
                            <a href="/prometheus/agroalimentaire/maraicher/" class="industry-link"><div class="industry-link-icon">''' + I["leaf"] + '''</div><span>ERP Fruits et légumes</span></a>
                            <a href="/prometheus/agroalimentaire/boulanger/" class="industry-link"><div class="industry-link-icon">''' + I["bread"] + '''</div><span>ERP Boulangerie Pâtisserie</span></a>
                            <a href="/prometheus/agroalimentaire/charcutier/" class="industry-link"><div class="industry-link-icon">''' + I["knife"] + '''</div><span>ERP Charcutier</span></a>
                            <a href="/prometheus/agroalimentaire/industrie-laitiere/" class="industry-link"><div class="industry-link-icon">''' + I["bottle"] + '''</div><span>ERP Laitier</span></a>
                            <a href="/prometheus/agroalimentaire/plats-cuisines-industriels/" class="industry-link"><div class="industry-link-icon">''' + I["plate"] + '''</div><span>ERP Plats cuisinés</span></a>
<div style="border-top:1px solid #e2e8f0;margin-top:0.75rem;padding-top:0.75rem">
<h5><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg> Médical</h5>
<a href="/prometheus/medical/" class="industry-link"><div class="industry-link-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></div><span>ERP Dispositifs Médicaux</span></a>
<a href="/prometheus/medical/laboratoires/" class="industry-link"><div class="industry-link-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg></div><span>ERP Laboratoires</span></a>
<a href="/prometheus/medical/materiel-dentaire/" class="industry-link"><div class="industry-link-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg></div><span>ERP Matériel Dentaire</span></a>
<a href="/prometheus/medical/maintien-a-domicile/" class="industry-link"><div class="industry-link-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg></div><span>ERP Maintien à Domicile</span></a>
<a href="/prometheus/medical/hygiene-professionnelle/" class="industry-link"><div class="industry-link-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></div><span>ERP Hygiène Professionnelle</span></a>
</div>
                        </div>
                    </div>
                </div>
            </div>
            <a href="/prometheus/tarifs/">Tarifs</a>
            <a href="/prometheus/ecosysteme/">Écosystème</a>
        </nav>
        <div class="header-actions">
            <a href="/prometheus/contact/" class="btn-contact-header">Contactez-nous</a>
            <a href="/prometheus/contact/" class="btn-demo-header">Demandez une démo</a>
        </div>
        <button class="hamburger-btn" id="hamburgerBtn" aria-label="Menu"><svg id="iconMenu" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg><svg id="iconClose" style="display:none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg></button>
    </div>
    <div class="mobile-menu" id="mobileMenu">
        <div class="mobile-menu-inner">
            <a href="/prometheus/">Accueil</a>
            <div><button class="mobile-accordion-btn" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')">Fonctionnalités <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></button><div class="mobile-submenu"><a href="/prometheus/fonctionnalites/crm/">Gestion relation client</a><a href="/prometheus/fonctionnalites/facturation/">Gestion facturation</a><a href="/prometheus/fonctionnalites/vente/">Gestion commerciale</a><a href="/prometheus/fonctionnalites/gestion-de-stock/">Gestion des stocks</a><a href="/prometheus/fonctionnalites/fabrication/">Gestion fabrication</a><a href="/prometheus/fonctionnalites/achat/">Gestion des achats</a><a href="/prometheus/fonctionnalites/logistique/">Gestion logistique</a><a href="/prometheus/fonctionnalites/import-export/">Gestion imports exports</a></div></div>
            <div><button class="mobile-accordion-btn" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')">Industries <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></button><div class="mobile-submenu"><a href="/prometheus/agroalimentaire/">ERP Agroalimentaire</a><a href="/prometheus/agroalimentaire/traiteur/">ERP Traiteur</a><a href="/prometheus/agroalimentaire/maraicher/">ERP Fruits et légumes</a><a href="/prometheus/agroalimentaire/boulanger/">ERP Boulangerie</a><a href="/prometheus/agroalimentaire/charcutier/">ERP Charcutier</a><a href="/prometheus/agroalimentaire/industrie-laitiere/">ERP Laitier</a><a href="/prometheus/agroalimentaire/plats-cuisines-industriels/">ERP Plats cuisinés</a><a href="/prometheus/medical/">ERP Médical</a><a href="/prometheus/medical/dispositifs-medicaux/">ERP Dispositifs Médicaux</a><a href="/prometheus/medical/laboratoires/">ERP Laboratoires</a><a href="/prometheus/medical/materiel-dentaire/">ERP Matériel Dentaire</a><a href="/prometheus/medical/maintien-a-domicile/">ERP Maintien à Domicile</a><a href="/prometheus/medical/hygiene-professionnelle/">ERP Hygiène Professionnelle</a></div></div>
            <a href="/prometheus/tarifs/">Tarifs</a>
            <a href="/prometheus/ecosysteme/">Écosystème</a>
            <div class="mobile-ctas"><a href="/prometheus/contact/" class="mobile-cta-primary">Demandez une démo</a><a href="/prometheus/contact/" class="mobile-cta-secondary">Contactez-nous</a></div>
        </div>
    </div>
</header>'''

LOGO_CAROUSEL = '''<!-- LOGO CAROUSEL -->
<section class="logos-section">
    <div class="container">
        <p class="section-label">Ils nous font confiance</p>
        <div class="logo-carousel-container">
            <div class="logo-carousel">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Logo_Pro-inter_Magasins_Orientaux.png" alt="Pro-Inter">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/1.png" alt="Leclerc">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Jacob-150x150.jpeg" alt="Jacob">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.14.24-300x64.png" alt="Corseprim">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.12.46.png" alt="Les Primeurs">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.10.42-300x226.png" alt="HPS">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.08.48-300x86.png" alt="Kore">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.07.48-300x165.png" alt="Poujauran">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.06.38-300x131.png" alt="Eatmotion">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.03.06-300x170.png" alt="Ciao Gusto">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.04.34-300x103.png" alt="Chef Cheffe">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.01.39-300x163.png" alt="Savary">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.00.01-300x218.png" alt="Karine & Jeff">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-14.57.18-300x122.png" alt="Chrono Primeurs">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-14.56.24-300x154.png" alt="Maison Aléna">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/5-300x240.png" alt="Client">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/4-300x240.png" alt="Client">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/3-300x240.png" alt="Client">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/2-300x240.png" alt="Client">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Logo_Pro-inter_Magasins_Orientaux.png" alt="Pro-Inter">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/1.png" alt="Leclerc">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Jacob-150x150.jpeg" alt="Jacob">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.14.24-300x64.png" alt="Corseprim">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.12.46.png" alt="Les Primeurs">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.10.42-300x226.png" alt="HPS">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.08.48-300x86.png" alt="Kore">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.07.48-300x165.png" alt="Poujauran">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.06.38-300x131.png" alt="Eatmotion">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.03.06-300x170.png" alt="Ciao Gusto">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.04.34-300x103.png" alt="Chef Cheffe">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.01.39-300x163.png" alt="Savary">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.00.01-300x218.png" alt="Karine & Jeff">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-14.57.18-300x122.png" alt="Chrono Primeurs">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-14.56.24-300x154.png" alt="Maison Aléna">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/5-300x240.png" alt="Client">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/4-300x240.png" alt="Client">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/3-300x240.png" alt="Client">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/2-300x240.png" alt="Client">
            </div>
        </div>
    </div>
</section>'''

ABOUT_VIDEO = '''<!-- A PROPOS + VIDEO -->
<section class="about-section">
    <div class="container">
        <div class="about-grid">
            <div class="about-text">
                <p class="section-tag">Qui sommes-nous</p>
                <h2>Hello Harel, l\'ERP pensé pour l\'agroalimentaire</h2>
                <p>Depuis plus de 15 ans, Hello Harel accompagne les professionnels de l\'agroalimentaire dans la gestion intégrale de leur activité. Notre mission : offrir un <strong>ERP SaaS complet</strong>, conçu spécifiquement pour répondre aux contraintes de traçabilité, de gestion des DLC/DDM, de calcul des marges et de logistique propre au secteur alimentaire.</p>
                <p>Que vous soyez grossiste, traiteur, boulanger industriel ou maraîcher, notre solution s\'adapte à votre réalité terrain. Plus de 500 entreprises nous font confiance pour piloter leurs achats, leurs ventes, leur production et leur logistique au quotidien.</p>
                <p>Basée en France, notre équipe combine expertise métier et innovation technologique pour vous offrir un outil performant, évolutif et simple à prendre en main — sans intégrateur, déployé en quelques jours.</p>
                <a href="/prometheus/qui-sommes-nous/" class="discover-link">En savoir plus <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></a>
            </div>
            <div class="about-video">
                <div class="video-wrapper">
                    <iframe src="https://www.youtube.com/embed/pANFAv6-sJk" title="Présentation Hello Harel" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
            </div>
        </div>
    </div>
</section>'''

PROCESS = '''<!-- PROCESS -->
<section class="process-section">
    <div class="container">
        <div class="section-header"><h2>Nos process — Succès guidé par des experts</h2></div>
        <div class="steps-wrapper"><div class="steps-line"></div>
            <div class="steps-grid">
                <div class="step-item"><div class="step-circle">1</div><h3>Planification</h3><p>Nous guidons vos équipes à travers des ateliers de conception rapides et efficaces pour découvrir la configuration parfaite pour votre nouveau système ERP.</p></div>
                <div class="step-item"><div class="step-circle">2</div><h3>Mise en oeuvre</h3><p>Clé en main, notre logiciel de gestion commerciale se déploie en quelques minutes sans intégrateur.</p></div>
                <div class="step-item"><div class="step-circle">3</div><h3>Validation</h3><p>Nous guidons vos équipes à travers des ateliers de conception rapides et efficaces pour découvrir la configuration parfaite pour votre nouveau système ERP.</p></div>
                <div class="step-item"><div class="step-circle">''' + I["check"] + '''</div><h3>Mise en production</h3><p>Nous vous assistons étape par étape dans le déploiement de l\'outil, de la migration de vos données métier jusqu\'au paramétrage de votre environnement de travail.</p></div>
            </div>
        </div>
    </div>
</section>'''

INDUSTRIES = '''<!-- INDUSTRIES -->
<section class="industries-section">
    <div class="bg-grid"><svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%"><defs><pattern id="gp" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M0 40V0h40" fill="none" stroke="currentColor" stroke-width="1"/></pattern></defs><rect width="100%" height="100%" fill="url(#gp)"/></svg></div>
    <div class="container">
        <div class="section-header"><p class="overline">Solutions par métier</p><h2><a href="/prometheus/agroalimentaire/" style="color:inherit">Les métiers de notre ERP agroalimentaire</a></h2><p>Chaque niche agroalimentaire a ses propres contraintes. Harel s\'adapte à votre réalité terrain.</p></div>
        <div class="industries-grid">
            <a href="/prometheus/agroalimentaire/traiteur/" class="industry-card"><div class="card-icon"><svg width="40" height="40" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 2C8 2 4 4 4 8c0 2.5 2 4 4 5v1h8v-1c2-1 4-2.5 4-5 0-4-4-6-8-6zM8 16h8m-6 3h4m-2 3v-3"/></svg></div><h3>Traiteur</h3><p>Création de fiches techniques, devis complexes et logistique pour les réceptions.</p></a>
            <a href="/prometheus/agroalimentaire/charcutier/" class="industry-card"><div class="card-icon"><svg width="40" height="40" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 3l-1.5 1.5M9 9l-6 6c-1 1-1 2.5 0 3.5l2 2c1 1 2.5 1 3.5 0l6-6M18 6c1.5-1.5 1.5-4 0-5.5s-4 0-5.5 0L9 4l3 3 3 3 3.5-3.5z"/></svg></div><h3>Charcutier</h3><p>Gérez la découpe, les rendements matière et les pertes de poids (freintes).</p></a>
            <a href="/prometheus/agroalimentaire/boulanger/" class="industry-card"><div class="card-icon"><svg width="40" height="40" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 18c0 1 1.5 3 7 3s7-2 7-3c0-2-3-3-7-3s-7 1-7 3zM5 18c-1-2 0-5 2-7 1.5-1.5 3-2 5-2s3.5.5 5 2c2 2 3 5 2 7M9 9c0-2 1.5-4 3-5 1.5 1 3 3 3 5"/></svg></div><h3>Boulanger</h3><p>Planification de production centralisée et dispatch vers vos différents magasins.</p></a>
            <a href="/prometheus/agroalimentaire/maraicher/" class="industry-card"><div class="card-icon"><svg width="40" height="40" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 2c-1 3-4 5-4 9a4 4 0 008 0c0-4-3-6-4-9zM8 15l-2 6h12l-2-6M12 11v4m-2-2h4"/></svg></div><h3>Maraîcher</h3><p>Gérez les calibres, les origines, les agréages et les variations de prix quotidiennes.</p></a>
            <a href="/prometheus/agroalimentaire/industrie-laitiere/" class="industry-card"><div class="card-icon"><svg width="40" height="40" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 2h8l1 4H7L8 2zM7 6v2c0 1-1 2-1 3v7a2 2 0 002 2h8a2 2 0 002-2v-7c0-1-1-2-1-3V6M10 12h4M10 15h4"/></svg></div><h3>Laitier</h3><p>Collecte du lait, maturation, DDM courtes et respect strict de la chaîne du froid.</p></a>
            <a href="/prometheus/agroalimentaire/plats-cuisines-industriels/" class="industry-card"><div class="card-icon"><svg width="40" height="40" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 13h18M5 13c0-4 3-7 7-7s7 3 7 7M4 13v1a1 1 0 001 1h14a1 1 0 001-1v-1M8 17v2m8-2v2M6 21h12"/></svg></div><h3>Plats cuisinés</h3><p>Nomenclatures multi-niveaux, calcul des coûts de revient et étiquetage INCO.</p></a>
        </div>
    </div>
</section>'''

TEAM = '''<!-- TEAM -->
<section class="team-section">
    <div class="container">
        <h2>Une equipe humaine</h2>
        <p class="subtitle">Disponible et à l\'écoute !</p>
        <div class="team-grid">
            <div class="team-card"><img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2024/10/Timothy-Jolliver-President-de-Hello-Harel-150x150.jpeg" alt="Timothy - Gérant"><div class="team-info"><h4>Timothy</h4><p>Gérant</p></div><a href="https://fr.linkedin.com/in/timothy-jollivet-80516070" class="linkedin-icon" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i></a></div>
            <div class="team-card"><img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Nicolas-150x150.jpeg" alt="Nicolas - Resp. Partenariat"><div class="team-info"><h4>Nicolas</h4><p>Resp. Partenariat</p></div><a href="https://fr.linkedin.com/in/nicolas-de-cerner-mercimax" class="linkedin-icon" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i></a></div>
            <div class="team-card"><img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Maxence-150x150.jpeg" alt="Maxence - Resp. Commercial"><div class="team-info"><h4>Maxence</h4><p>Resp. Commercial</p></div><a href="https://fr.linkedin.com/in/maxence-flavigny-5a5549120" class="linkedin-icon" target="_blank" rel="noopener"><i class="fab fa-linkedin"></i></a></div>
        </div>
        <a href="/prometheus/qui-sommes-nous/" class="discover-link" style="display:inline-flex;align-items:center;gap:0.5rem;color:#1d4ed8;font-weight:700;font-size:0.9375rem;margin-top:2rem">Découvrir notre équipe <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></a>
    </div>
</section>'''

TESTIMONIAL = '''<!-- TESTIMONIAL -->
<section class="testimonial-section">
    <div class="container">
        <div class="testimonial-card">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2024/11/handsome-baker-in-uniform-at-the-manufacturing-sma-2022-04-11-21-08-04-utc-768x768.jpg" alt="Julien Benguigui - Misencil" class="testimonial-photo">
            <div class="testimonial-text">
                <div class="quote-icon"><i class="fas fa-quote-left"></i></div>
                <blockquote>Nous avons une véritable traçabilité de l\'historique de nos clients, ce qui nous permet de mieux les connaître et leur offrir une relation client plus humaine et authentique.</blockquote>
                <div class="testimonial-author"><strong>Julien Benguigui</strong>Co-fondateur filiale France — @Misencil</div>
            </div>
        </div>
    </div>
</section>'''

REVIEWS = '''<!-- GOOGLE REVIEWS -->
<section class="reviews-section">
    <div class="container">
        <div class="section-header">
            <p class="overline">Avis clients</p>
            <h2>Ils nous font confiance</h2>
            <div class="reviews-rating">
                <div class="stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
                <span class="rating-text">5.0/5 — 31 avis Google</span>
            </div>
        </div>
        <div class="reviews-grid">
            <div class="review-card">
                <div class="review-header"><div class="review-avatar">JB</div><div><div class="review-name">Julien B.</div><div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div></div></div>
                <p class="review-text">"Un ERP parfaitement adapté à notre métier de traiteur. La gestion des fiches techniques et des DLC est un vrai gain de temps au quotidien. L\'équipe est réactive et à l\'écoute."</p>
                <div class="review-source"><i class="fab fa-google"></i> Google</div>
            </div>
            <div class="review-card">
                <div class="review-header"><div class="review-avatar">MC</div><div><div class="review-name">Marie C.</div><div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div></div></div>
                <p class="review-text">"Nous avons migré depuis un ERP généraliste et la différence est flagrante. Hello Harel comprend nos contraintes de grossiste en fruits et légumes : calibres, agréages, prix du jour..."</p>
                <div class="review-source"><i class="fab fa-google"></i> Google</div>
            </div>
            <div class="review-card">
                <div class="review-header"><div class="review-avatar">PD</div><div><div class="review-name">Philippe D.</div><div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div></div></div>
                <p class="review-text">"Déploiement rapide, sans intégrateur. En 3 jours nous étions opérationnels. Le suivi des marges produit par produit nous a permis d\'identifier des pertes qu\'on ne voyait pas avant."</p>
                <div class="review-source"><i class="fab fa-google"></i> Google</div>
            </div>
            <div class="review-card">
                <div class="review-header"><div class="review-avatar">SL</div><div><div class="review-name">Sophie L.</div><div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div></div></div>
                <p class="review-text">"La gestion multi-entrepôts est excellente. On gère 3 sites avec des stocks consolidés en temps réel. Le support est toujours disponible et comprend nos problématiques métier."</p>
                <div class="review-source"><i class="fab fa-google"></i> Google</div>
            </div>
        </div>
    </div>
</section>'''

CTA_BANNER = '''<!-- CTA BANNER -->
<section class="cta-banner">
    <div class="container">
        <div class="cta-banner-inner">
            <h2>Prêt à optimiser votre gestion ?</h2>
            <p>Découvrez comment Hello Harel peut s\'adapter à vos contraintes spécifiques.</p>
            <div class="cta-infos">
                <div class="info-item">''' + '<svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>' + ''' 06 18 06 00 18</div>
                <div class="info-item"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg> contact@helloharel.com</div>
                <div class="info-item"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg> Paris, France</div>
            </div>
        </div>
    </div>
</section>'''

FOOTER = '''<!-- FOOTER -->
<footer>
    <div class="container">
        <div class="footer-grid">
            <div class="footer-brand">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2019/05/hello-harel-logo-white.svg" alt="Hello Harel" style="height:36px;margin-bottom:15px">
                <div class="social-icons"><a href="https://www.linkedin.com/company/26042947/" target="_blank" rel="noopener"><i class="fab fa-linkedin-in"></i></a><a href="https://www.youtube.com/@HelloHarel" target="_blank" rel="noopener"><i class="fab fa-youtube"></i></a></div>
                <p>Hello Harel est un ERP SAAS pour l\'industrie de l\'agroalimentaire. Ce logiciel vous permet de gérer l\'ensemble de votre entreprise. De la gestion des stocks à la gestion des achats en passant par la gestion relation client.</p>
            </div>
            <div class="footer-col"><h4>Fonctionnalités</h4><ul><li><a href="/prometheus/fonctionnalites/crm/">Logiciel CRM</a></li><li><a href="/prometheus/fonctionnalites/facturation/">Logiciel de Facturation</a></li><li><a href="/prometheus/fonctionnalites/fabrication/">Logiciel de Fabrication</a></li><li><a href="/prometheus/fonctionnalites/gestion-de-stock/">Logiciel de Gestion de stock</a></li><li><a href="/prometheus/fonctionnalites/vente/">Logiciel de gestion des Ventes</a></li><li><a href="/prometheus/fonctionnalites/achat/">Logiciel d\'Achat</a></li><li><a href="/prometheus/fonctionnalites/logistique/">Logiciel de Logistique</a></li><li><a href="/prometheus/fonctionnalites/import-export/">Logiciel Import Export</a></li></ul></div>
            <div class="footer-col"><h4>Industries</h4><ul><li><a href="/prometheus/agroalimentaire/">ERP Agroalimentaire</a></li><li><a href="/prometheus/agroalimentaire/boulanger/">ERP Pâtisserie – Boulangerie</a></li><li><a href="/prometheus/agroalimentaire/traiteur/">ERP Traiteur</a></li><li><a href="/prometheus/agroalimentaire/maraicher/">ERP Fruits et légumes</a></li><li><a href="/prometheus/agroalimentaire/charcutier/">ERP Charcutier</a></li><li><a href="/prometheus/agroalimentaire/industrie-laitiere/">ERP Laitier</a></li><li><a href="/prometheus/agroalimentaire/plats-cuisines-industriels/">ERP Plats cuisinés</a></li><li><a href="/prometheus/medical/">ERP Médical</a></li><li><a href="/prometheus/medical/dispositifs-medicaux/">ERP Dispositifs Médicaux</a></li><li><a href="/prometheus/medical/laboratoires/">ERP Laboratoires</a></li></ul></div>
            <div class="footer-col"><h4>Informations</h4><ul><li><a href="/prometheus/blog/">Blog</a></li><li><a href="/prometheus/qui-sommes-nous/">Qui sommes nous ?</a></li><li><a href="/prometheus/ecosysteme/">Ecosystème</a></li><li><a href="https://doc.harelsystems.io/doc/basic" target="_blank" rel="noopener">Tutoriels</a></li><li><a href="/prometheus/page-sitemap.xml">Plan de site – Pages</a></li><li><a href="/prometheus/post-sitemap.xml">Plan de site – Articles</a></li><li style="margin-top:0.75rem;padding-top:0.75rem;border-top:1px solid rgba(255,255,255,0.06)"><a href="/prometheus/integrateurs/" style="color:#60a5fa !important;font-weight:700 !important">Devenir intégrateur →</a></li></ul></div>
        </div>
        <div class="footer-bottom"><a href="/prometheus/mentions-legales/">Mentions légales</a><a href="/prometheus/politique-de-confidentialite/">Politique de confidentialité</a><a href="/prometheus/cgu/">Conditions générales d\'utilisation</a></div>
    </div>
</footer>'''

STICKY_CTA = '<div class="sticky-cta"><a href="/prometheus/contact/">Demander une démo</a></div>'

JS = '''<script>
document.getElementById('hamburgerBtn').addEventListener('click',function(){
    var m=document.getElementById('mobileMenu');
    var open=m.classList.toggle('open');
    document.getElementById('iconMenu').style.display=open?'none':'block';
    document.getElementById('iconClose').style.display=open?'block':'none';
    document.body.classList.toggle('menu-open',open);
});
window.addEventListener('resize',function(){if(window.innerWidth>=1024){document.getElementById('mobileMenu').classList.remove('open');document.getElementById('iconMenu').style.display='block';document.getElementById('iconClose').style.display='none';document.body.classList.remove('menu-open');}});
</script>'''


# ── HTML GENERATORS ──

def make_hero(page):
    h = page["hero"]
    return f'''<section class="hero-section" style="background:linear-gradient(rgba(30,58,138,0.82),rgba(30,58,138,0.82)),url('{h["bg"]}') center/cover no-repeat;border-bottom:none;">
    <div class="container">
        <div class="hero-content-centered">
            <div class="hero-badge"><span class="dot"></span>{h["badge"]}</div>
            <h1 class="hero-title" style="color:#fff">{h["title_w"]} <span class="accent" style="color:#60a5fa">{h["title_a"]}</span></h1>
            <p class="hero-description" style="color:rgba(255,255,255,0.85)">{h["desc"]}</p>
            <a href="/prometheus/contact/" class="hero-cta" style="background:#fff;color:#1e3a8a;box-shadow:0 10px 25px rgba(0,0,0,0.3)">Contactez-nous pour une démonstration</a>
            <p class="hero-cta-sub" style="color:rgba(255,255,255,0.7)">Sans engagement. Déploiement rapide.</p>
        </div>
    </div>
</section>'''


def make_bento(page):
    b = page["bento"]
    cards = b["cards"]
    # Card 0 = large card
    c0 = cards[0]
    checklist_html = ""
    if "checks" in c0:
        items = "".join(f'<li>{I["check"]}{c}</li>' for c in c0["checks"])
        checklist_html = f'<ul class="check-list">{items}</ul>'
    link0 = f'<a href="{c0.get("link","#")}" class="card-link">{c0.get("link_text","En savoir plus")} <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></a>' if c0.get("link") else ""

    large_card = f'''<div class="bento-card large">
                <div class="bg-pattern">{I.get(c0.get("bg_icon","shield"), I["shield"])}</div>
                <div style="position:relative;z-index:1"><div class="bento-icon {c0["color"]}">{I[c0["icon"]]}</div>
                <h3>{c0["title"]}</h3>
                <p>{c0["desc"]}</p>
                {checklist_html}
                {link0}</div>
            </div>'''

    # Cards 1-3 = regular cards
    regular = ""
    for c in cards[1:4]:
        link_h = f'<a href="{c.get("link","#")}" class="card-link">En savoir plus →</a>' if c.get("link") else ""
        regular += f'''<div class="bento-card"><div class="bento-icon {c["color"]}">{I[c["icon"]]}</div><h3>{c["title"]}</h3><p>{c["desc"]}</p>{link_h}</div>\n            '''

    # Card 4 = wide card (if exists)
    wide_card = ""
    if len(cards) > 4:
        c4 = cards[4]
        extra_links = ""
        if "sub_links" in c4:
            links = "".join(f'<a href="{sl["href"]}" class="card-link">{sl["text"]}</a>' for sl in c4["sub_links"])
            extra_links = f'<div style="display:flex;gap:16px;flex-wrap:wrap;margin-top:12px">{links}</div>'
        wide_card = f'''<div class="bento-card wide"><div style="display:flex;gap:24px;align-items:center"><div style="flex:1"><div class="bento-icon {c4["color"]}">{I[c4["icon"]]}</div><h3>{c4["title"]}</h3><p>{c4["desc"]}</p>{extra_links}</div></div></div>'''

    return f'''<section class="features-section" id="fonctionnalites">
    <div class="container">
        <div class="section-header">
            <p class="overline">{b["overline"]}</p>
            <h2>{b["heading"]}</h2>
            <p>{b["sub"]}</p>
        </div>
        <div class="bento-grid">
            {large_card}
            {regular}
            {wide_card}
        </div>
    </div>
</section>'''


def make_faq(page):
    f = page["faq"]
    cards_html = ""
    data_js = ""
    for idx, item in enumerate(f["items"]):
        cards_html += f'''<div class="faq-card" onclick="openFaqDrawer({idx})">
                <div class="faq-card-inner">
                    <div class="faq-card-emoji">{I.get(item.get("icon","shield"), I["shield"])}</div>
                    <span class="faq-card-question">{item["q"]}</span>
                    <span class="faq-card-meta">{item["meta"]}</span>
                </div>
                <div class="faq-card-arrow"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></div>
            </div>\n            '''
        # Escape single quotes for JS
        safe_html = item["html"].replace("'", "\\'").replace("\n", "\\n")
        safe_title = item["q"].replace("'", "\\'")
        data_js += f"    {{title: '{safe_title}', html: '{safe_html}'}},\n"

    return f'''<section class="faq-section">
    <div class="container">
        <div class="section-header">
            <p class="overline">{f["overline"]}</p>
            <h2>{f["heading"]}</h2>
            <p>{f["sub"]}</p>
        </div>
        <div class="faq-cards-grid">
            {cards_html}
        </div>
    </div>
</section>
<div class="faq-drawer-overlay" id="faqOverlay" onclick="closeFaqDrawer()"></div>
<div class="faq-drawer" id="faqDrawer">
    <button class="faq-drawer-close" onclick="closeFaqDrawer()" aria-label="Fermer"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg></button>
    <div class="faq-drawer-content" id="faqDrawerContent"></div>
</div>
<script>
var faqData = [
{data_js}];
function openFaqDrawer(index) {{
    var d = faqData[index];
    document.getElementById('faqDrawerContent').innerHTML = '<h2>' + d.title + '</h2>' + d.html;
    document.getElementById('faqOverlay').classList.add('open');
    document.getElementById('faqDrawer').classList.add('open');
    document.body.style.overflow = 'hidden';
}}
function closeFaqDrawer() {{
    document.getElementById('faqOverlay').classList.remove('open');
    document.getElementById('faqDrawer').classList.remove('open');
    document.body.style.overflow = '';
}}
document.addEventListener('keydown', function(e) {{ if (e.key === 'Escape') closeFaqDrawer(); }});
</script>'''


def build_page_html(page):
    """Build full page body HTML."""
    body = "\n\n".join([
        HEADER,
        make_hero(page),
        LOGO_CAROUSEL,
        make_bento(page),
        ABOUT_VIDEO,
        PROCESS,
        INDUSTRIES,
        TEAM,
        TESTIMONIAL,
        make_faq(page),
        REVIEWS,
        CTA_BANNER,
        FOOTER,
        STICKY_CTA,
        JS,
    ])
    return body


def deploy_page(page):
    """Deploy one page to WordPress."""
    body_html = build_page_html(page)
    wrapped = f'<div id="hh-page">\n{body_html}\n</div>'
    full = f'''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
{CSS}
</style>
{wrapped}'''
    wp_content = f'<!-- wp:html -->\n{full}\n<!-- /wp:html -->'

    resp = requests.post(
        f"{WP_URL}/pages/{page['id']}",
        auth=AUTH,
        json={
            "content": wp_content,
            "template": "elementor_canvas",
            "meta": {"_elementor_edit_mode": "", "_elementor_data": "[]"}
        },
        headers={"Content-Type": "application/json"},
        timeout=120
    )

    name = page["name"]
    pid = page["id"]
    if resp.status_code == 200:
        data = resp.json()
        rendered = data.get('content', {}).get('rendered', '')
        # Quick checks
        has_hh = 'id="hh-page"' in rendered
        has_bento = 'bento-grid' in rendered
        has_hero = 'hero-content-centered' in rendered
        has_faq = 'faq-drawer' in rendered
        ok = has_hh and has_bento and has_hero and has_faq
        status = "OK" if ok else "WARN"
        print(f"  {status} | {name:40s} | id={pid} | {len(rendered):,} chars | hh={has_hh} bento={has_bento} hero={has_hero} faq={has_faq}")
        return ok
    else:
        print(f"  FAIL | {name:40s} | id={pid} | HTTP {resp.status_code}")
        print(f"        {resp.text[:200]}")
        return False


# ═══════════════════════════════════════════
# PAGE DATA — imported from page_data.py
# ═══════════════════════════════════════════
from page_data import PAGES

if __name__ == "__main__":
    if len(sys.argv) > 1:
        slug = sys.argv[1]
        matches = [p for p in PAGES if p["slug"] == slug]
        if not matches:
            print(f"Unknown slug: {slug}")
            print(f"Available: {', '.join(p['slug'] for p in PAGES)}")
            sys.exit(1)
        deploy_page(matches[0])
    else:
        print("=" * 100)
        print("DEPLOYING ALL 16 PAGES WITH UNIQUE CONTENT")
        print("=" * 100)

        # Purge LiteSpeed cache first
        try:
            requests.get(
                "https://www.helloharel.com/prometheus/",
                auth=AUTH,
                headers={"X-LiteSpeed-Purge": "*"},
                timeout=30
            )
            print("LiteSpeed cache purged.\n")
        except:
            pass

        results = []
        for page in PAGES:
            ok = deploy_page(page)
            results.append((page["name"], page["id"], ok))
            time.sleep(1)  # Be gentle with the server

        print("\n" + "=" * 100)
        print("SUMMARY")
        print("=" * 100)
        ok_count = sum(1 for _, _, ok in results if ok)
        for name, pid, ok in results:
            print(f"  {'✓' if ok else '✗'} {name} (id={pid})")
        print(f"\n{ok_count}/{len(results)} pages deployed successfully.")
