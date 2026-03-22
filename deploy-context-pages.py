#!/usr/bin/env python3
"""Deploy context pages (tarifs, contact, qui-sommes-nous, etc.) with new design.

NEW APPROACH: For each page, build the FULL page HTML from scratch using
shared sections from the homepage design system, plus page-specific content.
No more replacing header/footer in old HTML — we construct everything fresh.
"""

import json, sys, subprocess, tempfile, os, time

WP_URL = "https://www.helloharel.com/prometheus/wp-json/wp/v2"
WP_USER = "administration@remi-oravec.fr"
WP_PASS = "T8Yu 6UBr 1BOh H3i2 PNSw khHk"

# Read CSS from style.css (for CSS file upload)
with open('/workspaces/refonte-helloharel/style.css', 'r') as f:
    CSS = f.read()

# External CSS URL (loaded at runtime instead of inline)
CSS_URL = "https://www.helloharel.com/prometheus/wp-content/uploads/2026/03/hh-style.txt"

CONTEXT_PAGES = {
    "tarifs": 608,
    "contact": 661,
    "qui-sommes-nous": 4911,
    "ecosysteme": 552,
    "blog": 141,
    "erp-ia": 6156,
    "integrateurs": 6054,
}

# ══════════════════════════════════════════════════════════════════════
# SHARED HTML SECTIONS (copied from deploy-all-pages.py)
# ══════════════════════════════════════════════════════════════════════

HEADER = '''<!-- HEADER -->
<header class="site-header">
    <div class="container header-inner">
        <a href="/prometheus/" class="logo">
            <img loading="eager" src="https://www.helloharel.com/wp-content/uploads/2019/05/hello-harel-logo-white.svg" alt="Hello Harel - ERP Agroalimentaire" class="logo-white">
            <img loading="eager" src="https://www.helloharel.com/wp-content/uploads/2019/05/hello-harel-logo-white.svg" alt="Hello Harel - ERP Agroalimentaire" class="logo-dark">
        </a>
        <nav class="desktop-nav">
            <a href="/prometheus/">Accueil</a>
            <div class="nav-dropdown">
                <button class="nav-dropdown-trigger">Fonctionnalités <svg class="chevron-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></button>
                <div class="dropdown-panel" style="width:420px;max-width:95vw">
                    <div class="dropdown-card">
                        <a href="/prometheus/fonctionnalites/crm/" class="dropdown-link"><div class="dropdown-link-icon tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg></div><span class="dropdown-link-text">Gestion de la relation client</span></a>
                        <a href="/prometheus/fonctionnalites/facturation/" class="dropdown-link"><div class="dropdown-link-icon tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg></div><span class="dropdown-link-text">Gestion de la facturation</span></a>
                        <a href="/prometheus/fonctionnalites/vente/" class="dropdown-link"><div class="dropdown-link-icon tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div><span class="dropdown-link-text">Gestion commerciale</span></a>
                        <a href="/prometheus/fonctionnalites/gestion-de-stock/" class="dropdown-link"><div class="dropdown-link-icon tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg></div><span class="dropdown-link-text">Gestion des stocks</span></a>
                        <a href="/prometheus/fonctionnalites/fabrication/" class="dropdown-link"><div class="dropdown-link-icon tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg></div><span class="dropdown-link-text">Gestion de la fabrication</span></a>
                        <a href="/prometheus/fonctionnalites/achat/" class="dropdown-link"><div class="dropdown-link-icon tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/></svg></div><span class="dropdown-link-text">Gestion des achats</span></a>
                        <a href="/prometheus/fonctionnalites/logistique/" class="dropdown-link"><div class="dropdown-link-icon tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"/></svg></div><span class="dropdown-link-text">Gestion de la logistique</span></a>
                        <a href="/prometheus/fonctionnalites/import-export/" class="dropdown-link"><div class="dropdown-link-icon tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div><span class="dropdown-link-text">Gestion des imports exports</span></a>
<div style="border-top:1px solid #e2e8f0;margin-top:0.5rem;padding-top:0.5rem">
<a href="/prometheus/negoce/" class="dropdown-link"><div class="dropdown-link-icon tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg></div><span class="dropdown-link-text">ERP Négoce</span></a>
</div>
                    </div>
                </div>
            </div>
            <div class="nav-dropdown">
                <button class="nav-dropdown-trigger">Industries <svg class="chevron-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></button>
                <div class="dropdown-panel mega-industries-card">
                    <div class="dropdown-card" style="padding:0;overflow:hidden">
                        <div class="mega-industries-inner">
<div class="mega-col">
<h5><svg fill="none" stroke="currentColor" viewBox="0 0 24 24" style="width:1rem;height:1rem"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"/></svg> Agroalimentaire</h5>
<a href="/prometheus/agroalimentaire/" class="industry-link"><div class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></div><span>Agroalimentaire</span></a>
<a href="/prometheus/agroalimentaire/traiteur/" class="industry-link"><div class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z"/></svg></div><span>Traiteur</span></a>
<a href="/prometheus/agroalimentaire/maraicher/" class="industry-link"><div class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 2c-1 3-4 5-4 9a4 4 0 008 0c0-4-3-6-4-9zM8 15l-2 6h12l-2-6"/></svg></div><span>Fruits et légumes</span></a>
<a href="/prometheus/agroalimentaire/boulanger/" class="industry-link"><div class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 18c0 1 1.5 3 7 3s7-2 7-3c0-2-3-3-7-3s-7 1-7 3zM5 18c-1-2 0-5 2-7 1.5-1.5 3-2 5-2s3.5.5 5 2c2 2 3 5 2 7"/></svg></div><span>Boulangerie</span></a>
<a href="/prometheus/agroalimentaire/charcutier/" class="industry-link"><div class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 3l-1.5 1.5M9 9l-6 6c-1 1-1 2.5 0 3.5l2 2c1 1 2.5 1 3.5 0l6-6M18 6c1.5-1.5 1.5-4 0-5.5s-4 0-5.5 0L9 4l3 3 3 3 3.5-3.5z"/></svg></div><span>Charcutier</span></a>
<a href="/prometheus/agroalimentaire/industrie-laitiere/" class="industry-link"><div class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 2h8l1 4H7L8 2zM7 6v2c0 1-1 2-1 3v7a2 2 0 002 2h8a2 2 0 002-2v-7c0-1-1-2-1-3V6"/></svg></div><span>Laitier</span></a>
<a href="/prometheus/agroalimentaire/plats-cuisines-industriels/" class="industry-link"><div class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 13h18M5 13c0-4 3-7 7-7s7 3 7 7M4 13v1a1 1 0 001 1h14a1 1 0 001-1v-1"/></svg></div><span>Plats cuisinés</span></a>
</div>
<div class="mega-col">
<h5><svg fill="none" stroke="currentColor" viewBox="0 0 24 24" style="width:1rem;height:1rem"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg> Médical</h5>
<a href="/prometheus/medical/" class="industry-link"><div class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></div><span>Dispositifs Médicaux</span></a>
<a href="/prometheus/medical/laboratoires/" class="industry-link"><div class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg></div><span>Laboratoires</span></a>
<a href="/prometheus/medical/materiel-dentaire/" class="industry-link"><div class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg></div><span>Mat. Dentaire</span></a>
<a href="/prometheus/medical/maintien-a-domicile/" class="industry-link"><div class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg></div><span>Maintien Domicile</span></a>
<a href="/prometheus/medical/hygiene-professionnelle/" class="industry-link"><div class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></div><span>Hygiène Pro.</span></a>
</div>
</div>
                    </div>
                </div>
            </div>
            <a href="/prometheus/tarifs/">Tarifs</a>
            <a href="/prometheus/ecosysteme/">Écosystème</a>
            <a href="/prometheus/erp-ia/" style="color:#16DB7F !important;font-weight:700 !important">IA</a>
            <a href="/prometheus/implantations/">Implantations</a>
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
            <div><button class="mobile-accordion-btn" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')">Fonctionnalités <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></button><div class="mobile-submenu"><a href="/prometheus/fonctionnalites/crm/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg></span>CRM</a><a href="/prometheus/fonctionnalites/facturation/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg></span>Facturation</a><a href="/prometheus/fonctionnalites/vente/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></span>Commercial</a><a href="/prometheus/fonctionnalites/gestion-de-stock/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg></span>Stocks</a><a href="/prometheus/fonctionnalites/fabrication/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg></span>Fabrication</a><a href="/prometheus/fonctionnalites/achat/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/></svg></span>Achats</a><a href="/prometheus/fonctionnalites/logistique/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"/></svg></span>Logistique</a><a href="/prometheus/fonctionnalites/import-export/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></span>Import-Export</a><a href="/prometheus/negoce/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg></span>ERP Négoce</a></div></div>
            <div><button class="mobile-accordion-btn" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')">Industries <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg></button><div class="mobile-submenu">
<span class="mobile-sector-title">Agroalimentaire</span>
<a href="/prometheus/agroalimentaire/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></span>Agroalimentaire</a>
<a href="/prometheus/agroalimentaire/traiteur/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z"/></svg></span>Traiteur</a>
<a href="/prometheus/agroalimentaire/maraicher/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 2c-1 3-4 5-4 9a4 4 0 008 0c0-4-3-6-4-9zM8 15l-2 6h12l-2-6"/></svg></span>Fruits & Légumes</a>
<a href="/prometheus/agroalimentaire/boulanger/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 18c0 1 1.5 3 7 3s7-2 7-3c0-2-3-3-7-3s-7 1-7 3zM5 18c-1-2 0-5 2-7 1.5-1.5 3-2 5-2s3.5.5 5 2c2 2 3 5 2 7"/></svg></span>Boulangerie</a>
<a href="/prometheus/agroalimentaire/charcutier/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 3l-1.5 1.5M9 9l-6 6c-1 1-1 2.5 0 3.5l2 2c1 1 2.5 1 3.5 0l6-6M18 6c1.5-1.5 1.5-4 0-5.5s-4 0-5.5 0L9 4l3 3 3 3 3.5-3.5z"/></svg></span>Charcutier</a>
<a href="/prometheus/agroalimentaire/industrie-laitiere/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 2h8l1 4H7L8 2zM7 6v2c0 1-1 2-1 3v7a2 2 0 002 2h8a2 2 0 002-2v-7c0-1-1-2-1-3V6"/></svg></span>Laitier</a>
<a href="/prometheus/agroalimentaire/plats-cuisines-industriels/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 13h18M5 13c0-4 3-7 7-7s7 3 7 7M4 13v1a1 1 0 001 1h14a1 1 0 001-1v-1"/></svg></span>Plats cuisinés</a>
<span class="mobile-sector-title">Médical</span>
<a href="/prometheus/medical/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg></span>Dispositifs Médicaux</a>
<a href="/prometheus/medical/laboratoires/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/></svg></span>Laboratoires</a>
<a href="/prometheus/medical/materiel-dentaire/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg></span>Mat. Dentaire</a>
<a href="/prometheus/medical/maintien-a-domicile/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg></span>Maintien Domicile</a>
<a href="/prometheus/medical/hygiene-professionnelle/"><span class="tilted-icon-mini"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></span>Hygiène Pro.</a>
</div></div>
            <a href="/prometheus/tarifs/">Tarifs</a>
            <a href="/prometheus/ecosysteme/">Écosystème</a>
            <a href="/prometheus/erp-ia/" style="color:#16DB7F !important;font-weight:700 !important">IA</a>
            <a href="/prometheus/implantations/">Implantations</a>
            <div class="mobile-ctas"><a href="/prometheus/contact/" class="mobile-cta-primary" style="background:#22C55E !important;border-color:#22C55E !important;">Demander une démo</a><a href="/prometheus/contact/" class="mobile-cta-secondary">Contactez-nous</a></div>
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
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.14.24-300x64.png" alt="Corseprim">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.12.46.png" alt="Les Primeurs">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.10.42-300x226.png" alt="HPS">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.08.48-300x86.png" alt="Kore">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.07.48-300x165.png" alt="Poujauran">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.06.38-300x131.png" alt="Eatmotion">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.03.06-300x170.png" alt="Ciao Gusto">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Logo_Pro-inter_Magasins_Orientaux.png" alt="Pro-Inter">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/1.png" alt="Leclerc">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.14.24-300x64.png" alt="Corseprim">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.12.46.png" alt="Les Primeurs">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.10.42-300x226.png" alt="HPS">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.08.48-300x86.png" alt="Kore">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.07.48-300x165.png" alt="Poujauran">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.06.38-300x131.png" alt="Eatmotion">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.03.06-300x170.png" alt="Ciao Gusto">
            </div>
            <div class="logo-carousel logo-carousel-reverse" style="margin-top:1rem">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.04.34-300x103.png" alt="Chef Cheffe">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.01.39-300x163.png" alt="Savary">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.00.01-300x218.png" alt="Karine & Jeff">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-14.57.18-300x122.png" alt="Chrono Primeurs">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-14.56.24-300x154.png" alt="Maison Aléna">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/5-300x240.png" alt="Client">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/4-300x240.png" alt="Client">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/3-300x240.png" alt="Client">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/2-300x240.png" alt="Client">
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

ABOUT_VIDEO = '''<!-- QUI SOMMES-NOUS — 2 columns, video sticky -->
<section class="about-card-section">
    <div class="container">
        <div class="about-two-col scroll-reveal">
            <div class="about-card">
                <div class="about-card-inner">
                    <p class="section-tag">Qui sommes-nous ?</p>
                    <h2>Hello Harel, l\'ERP pensé pour l\'agroalimentaire</h2>
                    <p>Fondée il y a une dizaine d\'années, l\'entreprise française Hello Harel s\'est donné pour mission de révolutionner la gestion des PME agroalimentaires. Un outil unique qui évolue avec les sociétés, les accompagne dans leur croissance et leur ouverture sur de nouveaux marchés.</p>
                    <div class="about-stats">
                        <div class="about-stat-card"><span class="stat-number">2007</span><span class="stat-label">Depuis</span></div>
                        <div class="about-stat-card"><span class="stat-number">+600</span><span class="stat-label">Clients</span></div>
                        <div class="about-stat-card"><span class="stat-number">100%</span><span class="stat-label">Cloud SaaS</span></div>
                    </div>
                    <blockquote class="founder-quote"><p>Transformez votre gestion, nourrissez votre succès !</p><cite>— Timothy Jollivet, Fondateur</cite></blockquote>
                    <a href="/prometheus/qui-sommes-nous/" class="card-link">En savoir plus <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></a>
                </div>
            </div>
            <div class="about-video-card">
                <div class="video-wrapper"><iframe src="https://www.youtube.com/embed/pANFAv6-sJk" title="Présentation Hello Harel" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe></div>
                <div class="video-card-text">
                    <p>Découvrez Hello Harel et son interface en 3 min.</p>
                    <a href="https://www.youtube.com/watch?v=pANFAv6-sJk" class="card-link" target="_blank" rel="noopener"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24" style="width:16px;height:16px"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> Regarder la vidéo</a>
                </div>
            </div>
        </div>
    </div>
</section>'''

PROCESS = '''<!-- PROCESS — 3 steps timeline -->
<section class="process-section">
    <div class="container">
        <div class="section-header">
            <p class="overline">Notre accompagnement</p>
            <h2>Succès guidé par des experts</h2>
            <p>Un ERP déployé en quelques minutes, et un accompagnement pas à pas pour garantir votre réussite.</p>
        </div>
        <div class="timeline-wrapper">
            <div class="timeline-line"></div>
            <div class="timeline-grid">
                <div class="timeline-step scroll-reveal"><div class="timeline-circle">1</div><div class="timeline-card"><div class="tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg></div><h3>Ateliers de conception</h3><p>Nous guidons vos équipes à travers des ateliers de conception rapides et efficaces pour découvrir la configuration parfaite pour votre nouveau système ERP.</p></div></div>
                <div class="timeline-step scroll-reveal"><div class="timeline-circle">2</div><div class="timeline-card"><div class="tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg></div><h3>Déploiement clé en main</h3><p>Clé en main, notre logiciel de gestion commerciale se déploie en quelques minutes sans intégrateur.</p></div></div>
                <div class="timeline-step scroll-reveal"><div class="timeline-circle">3</div><div class="timeline-card"><div class="tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18.364 5.636l-3.536 3.536m0 5.656l3.536 3.536M9.172 9.172L5.636 5.636m3.536 9.192l-3.536 3.536M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-5 0a4 4 0 11-8 0 4 4 0 018 0z"/></svg></div><h3>Accompagnement continu</h3><p>Nous vous assistons étape par étape dans le déploiement de l\'outil, de la migration de vos données métier jusqu\'au paramétrage de votre environnement de travail.</p></div></div>
            </div>
        </div>
    </div>
</section>'''

METIERS_CAROUSEL = '''<!-- MÉTIERS — Carousel -->
<section class="metiers-section">
    <div class="container">
        <div class="section-header">
            <p class="overline">Solutions par métier</p>
            <h2>Nos secteurs d\'expertise</h2>
            <p>Un ERP spécialisé pour chaque industrie.</p>
        </div>
        <div class="metiers-carousel-wrapper">
            <div class="metiers-carousel">
                <a href="/prometheus/blog/logiciel-maree-mareyeur/" class="metier-slide scroll-reveal">
                    <div class="tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z"/></svg></div>
                    <h3>Mareyeur</h3><p>Gestion criée, filetage, poids variable et traçabilité FAO.</p>
                    <span class="discover-link">Découvrir <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></span>
                </a>
                <a href="/prometheus/agroalimentaire/boulanger/" class="metier-slide scroll-reveal">
                    <div class="tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 18c0 1 1.5 3 7 3s7-2 7-3c0-2-3-3-7-3s-7 1-7 3zM5 18c-1-2 0-5 2-7 1.5-1.5 3-2 5-2s3.5.5 5 2c2 2 3 5 2 7"/></svg></div>
                    <h3>Boulangerie</h3><p>Coût de revient, planification fournées, multi-points de vente.</p>
                    <span class="discover-link">Découvrir <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></span>
                </a>
                <a href="/prometheus/agroalimentaire/" class="metier-slide scroll-reveal">
                    <div class="tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg></div>
                    <h3>Grossiste</h3><p>Volumes importants, marges serrées, télévente ultra-rapide.</p>
                    <span class="discover-link">Découvrir <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></span>
                </a>
                <a href="/prometheus/agroalimentaire/plats-cuisines-industriels/" class="metier-slide scroll-reveal">
                    <div class="tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 13h18M5 13c0-4 3-7 7-7s7 3 7 7M4 13v1a1 1 0 001 1h14a1 1 0 001-1v-1"/></svg></div>
                    <h3>Traiteur</h3><p>Recettes multi-niveaux, PRI, commandes GMS, INCO.</p>
                    <span class="discover-link">Découvrir <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></span>
                </a>
                <a href="/prometheus/agroalimentaire/maraicher/" class="metier-slide scroll-reveal">
                    <div class="tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 2c-1 3-4 5-4 9a4 4 0 008 0c0-4-3-6-4-9zM8 15l-2 6h12l-2-6"/></svg></div>
                    <h3>Fruits & Légumes</h3><p>Saisonnier, cadencier de vente, gestion des lots.</p>
                    <span class="discover-link">Découvrir <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></span>
                </a>
            </div>
        </div>
    </div>
</section>'''

TEAM = '''<!-- NOTRE ÉQUIPE -->
<section class="team-section">
    <div class="container">
        <div class="section-header">
            <p class="overline">Notre équipe</p>
            <h2>Une équipe humaine</h2>
            <p>Disponible et à l\'écoute !</p>
        </div>
        <div class="team-grid">
            <div class="team-card scroll-reveal">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2024/10/Timothy-Jolliver-President-de-Hello-Harel-150x150.jpeg" alt="Timothy Jollivet">
                <div class="team-info"><h4>Timothy</h4><p>Gérant</p></div>
                <a href="https://fr.linkedin.com/in/timothy-jollivet-80516070" class="linkedin-btn" target="_blank" rel="noopener"><i class="fab fa-linkedin-in"></i></a>
            </div>
            <div class="team-card scroll-reveal">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Nicolas-150x150.jpeg" alt="Nicolas">
                <div class="team-info"><h4>Nicolas</h4><p>Resp. Partenariat</p></div>
                <a href="https://fr.linkedin.com/in/nicolas-de-cerner-mercimax" class="linkedin-btn" target="_blank" rel="noopener"><i class="fab fa-linkedin-in"></i></a>
            </div>
            <div class="team-card scroll-reveal">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Maxence-150x150.jpeg" alt="Maxence">
                <div class="team-info"><h4>Maxence</h4><p>Resp. Commercial</p></div>
                <a href="https://fr.linkedin.com/in/maxence-flavigny-5a5549120" class="linkedin-btn" target="_blank" rel="noopener"><i class="fab fa-linkedin-in"></i></a>
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
                <p class="review-text">"Un ERP parfaitement adapté à notre métier de traiteur. La gestion des fiches techniques et des DLC est un vrai gain de temps au quotidien."</p>
                <div class="review-source"><i class="fab fa-google"></i> Google</div>
            </div>
            <div class="review-card">
                <div class="review-header"><div class="review-avatar">MC</div><div><div class="review-name">Marie C.</div><div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div></div></div>
                <p class="review-text">"Hello Harel comprend nos contraintes de grossiste en fruits et légumes : calibres, agréages, prix du jour..."</p>
                <div class="review-source"><i class="fab fa-google"></i> Google</div>
            </div>
            <div class="review-card">
                <div class="review-header"><div class="review-avatar">PD</div><div><div class="review-name">Philippe D.</div><div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div></div></div>
                <p class="review-text">"En 3 jours nous étions opérationnels. Le suivi des marges nous a permis d\'identifier des pertes qu\'on ne voyait pas."</p>
                <div class="review-source"><i class="fab fa-google"></i> Google</div>
            </div>
            <div class="review-card">
                <div class="review-header"><div class="review-avatar">SL</div><div><div class="review-name">Sophie L.</div><div class="review-stars"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div></div></div>
                <p class="review-text">"La gestion multi-entrepôts est excellente. On gère 3 sites avec des stocks consolidés en temps réel."</p>
                <div class="review-source"><i class="fab fa-google"></i> Google</div>
            </div>
        </div>
    </div>
</section>'''

CTA_BANNER = '''<!-- CTA FINAL -->
<section class="cta-banner">
    <div class="container"><div class="cta-banner-inner"><h2>Prêt à transformer votre gestion ?</h2><p>Obtenez votre démo gratuite en 3 minutes. Déploiement clé en main, sans intégrateur.</p><div class="cta-buttons"><a href="/prometheus/contact/" class="cta-btn-primary" style="background:#22C55E !important;border-color:#22C55E !important;">Demander ma démo gratuite</a><a href="https://www.youtube.com/watch?v=pANFAv6-sJk" class="cta-btn-secondary" target="_blank" rel="noopener"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24" style="width:18px;height:18px"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> Voir la vidéo</a></div></div></div>
</section>'''

FOOTER = '''<!-- FOOTER -->
<footer>
    <div class="container">
        <div class="footer-grid">
            <div class="footer-brand"><img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2019/05/hello-harel-logo-white.svg" alt="Hello Harel" style="height:36px;margin-bottom:15px"><div class="social-icons"><a href="https://www.linkedin.com/company/26042947/" target="_blank" rel="noopener"><i class="fab fa-linkedin-in"></i></a><a href="https://www.youtube.com/@HelloHarel" target="_blank" rel="noopener"><i class="fab fa-youtube"></i></a></div><p>Hello Harel est un ERP SAAS pour l\'industrie de l\'agroalimentaire.</p></div>
            <div class="footer-col"><h4>Fonctionnalités</h4><ul><li><a href="/prometheus/fonctionnalites/crm/">Logiciel CRM</a></li><li><a href="/prometheus/fonctionnalites/facturation/">Logiciel de Facturation</a></li><li><a href="/prometheus/fonctionnalites/fabrication/">Logiciel de Fabrication</a></li><li><a href="/prometheus/fonctionnalites/gestion-de-stock/">Logiciel de Gestion de stock</a></li><li><a href="/prometheus/fonctionnalites/vente/">Logiciel de gestion des Ventes</a></li><li><a href="/prometheus/fonctionnalites/achat/">Logiciel d\'Achat</a></li><li><a href="/prometheus/fonctionnalites/logistique/">Logiciel de Logistique</a></li><li><a href="/prometheus/fonctionnalites/import-export/">Logiciel Import Export</a></li><li><a href="/prometheus/negoce/">ERP Négoce</a></li></ul></div>
            <div class="footer-col"><h4>Industries</h4><ul><li><a href="/prometheus/agroalimentaire/">ERP Agroalimentaire</a></li><li><a href="/prometheus/agroalimentaire/boulanger/">ERP Boulangerie</a></li><li><a href="/prometheus/agroalimentaire/traiteur/">ERP Traiteur</a></li><li><a href="/prometheus/agroalimentaire/maraicher/">ERP Fruits et légumes</a></li><li><a href="/prometheus/agroalimentaire/charcutier/">ERP Charcutier</a></li><li><a href="/prometheus/agroalimentaire/industrie-laitiere/">ERP Laitier</a></li><li><a href="/prometheus/agroalimentaire/plats-cuisines-industriels/">ERP Plats cuisinés</a></li><li><a href="/prometheus/medical/">ERP Médical</a></li><li><a href="/prometheus/medical/dispositifs-medicaux/">ERP Dispositifs Médicaux</a></li><li><a href="/prometheus/medical/laboratoires/">ERP Laboratoires</a></li></ul></div>
            <div class="footer-col"><h4>Informations</h4><ul><li><a href="/prometheus/blog/">Blog</a></li><li><a href="/prometheus/qui-sommes-nous/">Qui sommes nous ?</a></li><li><a href="/prometheus/ecosysteme/">Ecosystème</a></li><li><a href="https://doc.harelsystems.io/doc/basic" target="_blank" rel="noopener">Tutoriels</a></li><li><a href="/prometheus/erp-ia/" style="color:#16DB7F !important;font-weight:700 !important">Nouveau : ERP IA</a></li><li><a href="/prometheus/intelligence-artificielle/">Intelligence Artificielle</a></li><li><a href="/prometheus/implantations/">Implantations</a></li><li style="margin-top:0.75rem;padding-top:0.75rem;border-top:1px solid rgba(255,255,255,0.06)"><a href="/prometheus/integrateurs/" style="color:#16DB7F !important;font-weight:700 !important">Devenir intégrateur</a></li></ul></div>
        </div>
        <div class="footer-bottom"><a href="/prometheus/mentions-legales/">Mentions légales</a><a href="/prometheus/politique-de-confidentialite/">Politique de confidentialité</a><a href="/prometheus/cgu/">Conditions générales d\'utilisation</a></div>
    </div>
</footer>'''

STICKY_CTA = '<div class="sticky-cta"><a href="/prometheus/contact/" style="background:#22C55E !important;border-color:#22C55E !important;box-shadow:0 25px 50px -12px rgba(0,0,0,0.25), 0 8px 24px rgba(34,197,94,0.4) !important;">Demander une démo</a></div>'

JS = '''<script>
document.getElementById('hamburgerBtn').addEventListener('click',function(){var m=document.getElementById('mobileMenu');var open=m.classList.toggle('open');document.getElementById('iconMenu').style.display=open?'none':'block';document.getElementById('iconClose').style.display=open?'block':'none';document.body.classList.toggle('menu-open',open);});
window.addEventListener('resize',function(){if(window.innerWidth>=1024){document.getElementById('mobileMenu').classList.remove('open');document.getElementById('iconMenu').style.display='block';document.getElementById('iconClose').style.display='none';document.body.classList.remove('menu-open');}});
(function(){var h=document.querySelector('.site-header'),hr=document.querySelector('.hero-section');if(!h||!hr)return;new IntersectionObserver(function(e){h.classList.toggle('scrolled',!e[0].isIntersecting);},{threshold:0.1}).observe(hr);})();
(function(){var r=document.querySelectorAll('.scroll-reveal');if(!r.length)return;var o=new IntersectionObserver(function(e){e.forEach(function(en){if(en.isIntersecting){var s=en.target.parentElement.querySelectorAll('.scroll-reveal');en.target.style.transitionDelay=(Array.prototype.indexOf.call(s,en.target)*100)+'ms';en.target.classList.add('revealed');o.unobserve(en.target);}});},{threshold:0.1,rootMargin:'0px 0px -50px 0px'});r.forEach(function(el){o.observe(el);});})();
</script>'''


# ══════════════════════════════════════════════════════════════════════
# PAGE-SPECIFIC CONTENT SECTIONS
# ══════════════════════════════════════════════════════════════════════

# ── TARIFS ──────────────────────────────────────────────────────────

TARIFS_HERO = '''<!-- HERO -->
<section class="hero-section" style="border-bottom:none;">
    <div class="container">
        <div class="hero-grid">
            <div class="hero-text">
                <div class="hero-badge"><span class="dot"></span>Tarifs</div>
                <h1 class="hero-title">Une tarification progressive, <span class="accent">pour accompagner votre croissance</span></h1>
                <p class="hero-description">Choisissez le plan adapté à vos besoins. Tous nos plans incluent le déploiement, la formation et le support. Sans engagement.</p>
                <div class="hero-ctas">
                    <a href="/prometheus/contact/" class="hero-cta-primary">Demander ma démo gratuite</a>
                    <a href="/prometheus/contact/" class="hero-cta-secondary">Essayez</a>
                </div>
                <p class="hero-cta-sub">Sans engagement. Déploiement rapide.</p>
            </div>
            <div class="hero-image-spacer"></div>
        </div>
    </div>
</section>'''

TARIFS_CSS = '''
.pricing-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; max-width: 1100px; margin: 0 auto; }
.pricing-card { background: #fff; border: 1px solid #e2e8f0; border-radius: 1.25rem; padding: 2.5rem 2rem; text-align: center; transition: all 0.35s ease; position: relative; }
.pricing-card:hover { transform: translateY(-6px); box-shadow: 0 20px 25px -5px rgba(0,0,0,0.08); }
.pricing-card.featured { border: 2px solid #00B4FC; box-shadow: 0 10px 25px -5px rgba(29,78,216,0.15); }
.pricing-card .plan-name { font-size: 1.5rem; font-weight: 900; color: #101828; margin-bottom: 0.5rem; }
.pricing-card .plan-price { font-size: 3rem; font-weight: 900; color: #00B4FC; line-height: 1; }
.pricing-card .plan-price span { font-size: 1rem; font-weight: 600; color: #64748b; }
.pricing-card .plan-period { font-size: 0.8125rem; color: #94a3b8; margin-top: 0.25rem; margin-bottom: 1.5rem; }
.pricing-card .plan-cta { display: block; padding: 0.875rem; border-radius: 0.75rem; font-weight: 700; font-size: 0.9375rem; transition: all 0.3s ease; text-align: center; margin-bottom: 1.5rem; }
.pricing-card .plan-cta-primary { background: #00B4FC; color: #fff; }
.pricing-card .plan-cta-primary:hover { background: #005F88; transform: translateY(-1px); }
.pricing-card .plan-cta-secondary { background: #eff6ff; color: #00B4FC; }
.pricing-card .plan-cta-secondary:hover { background: #dbeafe; }
.pricing-card .features-list { text-align: left; }
.pricing-card .features-list .category { font-size: 0.6875rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #00B4FC; margin-top: 1rem; margin-bottom: 0.5rem; padding-bottom: 0.375rem; border-bottom: 1px solid #f1f5f9; }
.pricing-card .features-list li { display: flex; align-items: center; gap: 0.5rem; font-size: 0.8125rem; padding: 0.3rem 0; color: #334155; }
.pricing-card .features-list li svg { width: 1rem; height: 1rem; flex-shrink: 0; }
.pricing-card .features-list li.included svg { color: #059669; }
.pricing-card .features-list li.excluded { color: #cbd5e1; }
.pricing-card .features-list li.excluded svg { color: #cbd5e1; }
.pricing-badge { position: absolute; top: -0.75rem; left: 50%%; transform: translateX(-50%%); background: #00B4FC; color: #fff; font-size: 0.6875rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; padding: 0.25rem 1rem; border-radius: 9999px; }
@media (max-width: 1024px) { .pricing-grid { grid-template-columns: 1fr 1fr; } }
@media (max-width: 640px) { .pricing-grid { grid-template-columns: 1fr; } }
'''

# The pricing cards content is read from the HTML file at build time
# (extracted between <!-- PRICING SECTION --> and the next shared section)


# ── CONTACT ─────────────────────────────────────────────────────────

CONTACT_HERO = '''<!-- HERO -->
<section class="hero-section" style="background:linear-gradient(rgba(0,50,80,0.75),rgba(0,95,136,0.8)),url('https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=1920&h=800&fit=crop&q=80') center/cover no-repeat;border-bottom:none;">
    <div class="container">
        <div class="hero-grid">
            <div class="hero-text">
                <div class="hero-badge"><span class="dot"></span>Contact</div>
                <h1 class="hero-title" style="color:#fff">Obtenez votre démo <span class="accent" style="color:#00B4FC">gratuitement</span></h1>
                <p class="hero-description" style="color:rgba(255,255,255,0.85)">Découvrez tous les aspects de notre ERP en quelques minutes. Notre équipe vous accompagne dans la prise en main.</p>
            </div>
            <div class="hero-image-spacer"></div>
        </div>
    </div>
</section>'''

CONTACT_CSS = '''
.contact-section { padding: clamp(4rem,8vw,7rem) 0; background: #fff; }
.contact-grid { display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 3rem; align-items: start; }
.contact-form { background: #fff; border: 1px solid #e2e8f0; border-radius: 1.5rem; padding: 2.5rem; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); }
.contact-form h3 { font-size: 1.5rem; font-weight: 900; color: #101828; margin-bottom: 0.5rem; }
.contact-form > p { font-size: 0.875rem; color: #64748b; margin-bottom: 1.5rem; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
.form-group { margin-bottom: 1rem; }
.form-group label { display: block; font-size: 0.8125rem; font-weight: 600; color: #334155; margin-bottom: 0.375rem; }
.form-group input, .form-group select, .form-group textarea { width: 100%%; padding: 0.75rem 1rem; border: 1px solid #e2e8f0; border-radius: 0.75rem; font-size: 0.9375rem; font-family: inherit; color: #101828; transition: border-color 0.3s; }
.form-group input:focus, .form-group select:focus, .form-group textarea:focus { outline: none; border-color: #3b82f6; box-shadow: 0 0 0 3px rgba(59,130,246,0.1); }
.form-group textarea { resize: vertical; min-height: 100px; }
.form-submit { width: 100%%; padding: 1rem; background: #00B4FC; color: #fff; border: none; border-radius: 0.75rem; font-weight: 800; font-size: 1rem; cursor: pointer; font-family: inherit; transition: all 0.3s ease; }
.form-submit:hover { background: #005F88; transform: translateY(-1px); box-shadow: 0 10px 25px rgba(29,78,216,0.3); }
.form-note { font-size: 0.75rem; color: #94a3b8; margin-top: 0.75rem; text-align: center; }
.contact-info { }
.contact-info-card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 1.25rem; padding: 2rem; margin-bottom: 1.25rem; }
.contact-info-card h4 { font-size: 1rem; font-weight: 800; color: #101828; margin-bottom: 1rem; }
.contact-detail { display: flex; align-items: center; gap: 0.75rem; padding: 0.625rem 0; }
.contact-detail-icon { width: 2.5rem; height: 2.5rem; border-radius: 0.625rem; background: #eff6ff; color: #00B4FC; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.contact-detail-icon svg { width: 1.25rem; height: 1.25rem; }
.contact-detail-text { font-size: 0.875rem; color: #334155; }
.contact-detail-text strong { display: block; font-weight: 700; color: #101828; font-size: 0.9375rem; }
.contact-person { display: flex; align-items: center; gap: 1rem; background: #005F88; border-radius: 1.25rem; padding: 1.5rem; color: #fff; }
.contact-person img { width: 64px; height: 64px; border-radius: 50%%; object-fit: cover; border: 3px solid rgba(255,255,255,0.2); }
.contact-person-info h4 { font-size: 1rem; font-weight: 700; color: #fff; }
.contact-person-info p { font-size: 0.8125rem; color: rgba(255,255,255,0.7); }
.contact-person-info a { color: #16DB7F; font-weight: 700; font-size: 0.9375rem; }
@media (max-width: 1024px) { .contact-grid { grid-template-columns: 1fr; } .form-row { grid-template-columns: 1fr; } }
'''

CONTACT_CONTENT = '''<!-- CONTACT SECTION -->
<section class="contact-section">
    <div class="container">
        <div class="contact-grid">
            <div class="contact-form">
                <h3>Demandez votre démonstration</h3>
                <p>Remplissez le formulaire ci-dessous et notre équipe vous recontactera sous 24h.</p>
                <form onsubmit="event.preventDefault();alert('Merci ! Notre équipe vous recontactera sous 24h.');this.reset()">
                    <div class="form-row">
                        <div class="form-group"><label>Prénom *</label><input type="text" required placeholder="Jean"></div>
                        <div class="form-group"><label>Nom *</label><input type="text" required placeholder="Dupont"></div>
                    </div>
                    <div class="form-group"><label>Email professionnel *</label><input type="email" required placeholder="jean.dupont@entreprise.fr"></div>
                    <div class="form-row">
                        <div class="form-group"><label>Entreprise *</label><input type="text" required placeholder="Nom de votre société"></div>
                        <div class="form-group"><label>Téléphone</label><input type="tel" placeholder="06 00 00 00 00"></div>
                    </div>
                    <div class="form-group"><label>Secteur d'activité</label><select><option value="">Sélectionnez...</option><option>Grossiste agroalimentaire</option><option>Traiteur</option><option>Boulangerie / Pâtisserie</option><option>Fruits et légumes</option><option>Charcuterie</option><option>Industrie laitière</option><option>Plats cuisinés</option><option>Dispositifs médicaux</option><option>Laboratoire</option><option>Matériel dentaire</option><option>Maintien à domicile</option><option>Hygiène professionnelle</option><option>Autre</option></select></div>
                    <div class="form-group"><label>Votre besoin</label><textarea placeholder="Décrivez brièvement votre projet ou vos besoins..."></textarea></div>
                    <button type="submit" class="form-submit">Demander ma démo gratuite</button>
                    <p class="form-note">Sans engagement. Réponse sous 24h ouvrées.</p>
                </form>
            </div>
            <div class="contact-info">
                <div class="contact-person" style="margin-bottom:1.25rem">
                    <img src="https://www.helloharel.com/wp-content/uploads/2026/01/Maxence-150x150.jpeg" alt="Maxence">
                    <div class="contact-person-info">
                        <h4>Maxence</h4>
                        <p>Responsable Commercial</p>
                        <a href="tel:+33618060018">06 18 06 00 18</a>
                    </div>
                </div>
                <div class="contact-info-card">
                    <h4>Nos coordonnées</h4>
                    <div class="contact-detail">
                        <div class="contact-detail-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg></div>
                        <div class="contact-detail-text"><strong>06 18 06 00 18</strong>Du lundi au vendredi, 9h-18h</div>
                    </div>
                    <div class="contact-detail">
                        <div class="contact-detail-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg></div>
                        <div class="contact-detail-text"><strong>contact@helloharel.com</strong>Réponse sous 24h</div>
                    </div>
                    <div class="contact-detail">
                        <div class="contact-detail-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg></div>
                        <div class="contact-detail-text"><strong>HAREL SYSTEMS</strong>6 Avenue de Rueil, 92420 Vaucresson</div>
                    </div>
                </div>
                <div class="contact-info-card">
                    <h4>Pourquoi Hello Harel ?</h4>
                    <div class="contact-detail"><div class="contact-detail-icon" style="background:#ecfdf5;color:#059669"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg></div><div class="contact-detail-text">Déploiement en quelques jours</div></div>
                    <div class="contact-detail"><div class="contact-detail-icon" style="background:#ecfdf5;color:#059669"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg></div><div class="contact-detail-text">Sans engagement, sans intégrateur</div></div>
                    <div class="contact-detail"><div class="contact-detail-icon" style="background:#ecfdf5;color:#059669"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg></div><div class="contact-detail-text">+500 entreprises nous font confiance</div></div>
                    <div class="contact-detail"><div class="contact-detail-icon" style="background:#ecfdf5;color:#059669"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg></div><div class="contact-detail-text">Support humain et réactif</div></div>
                </div>
            </div>
        </div>
    </div>
</section>'''


# ── QUI-SOMMES-NOUS ─────────────────────────────────────────────────

QSN_HERO = '''<!-- HERO -->
<section class="hero-section" style="background:linear-gradient(rgba(0,50,80,0.75),rgba(0,95,136,0.8)),url('https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1920&h=800&fit=crop&q=80') center/cover no-repeat;border-bottom:none;">
    <div class="container">
        <div class="hero-grid">
            <div class="hero-text">
                <div class="hero-badge"><span class="dot"></span>Notre Histoire</div>
                <h1 class="hero-title" style="color:#fff">Digitaliser l'agroalimentaire, <span class="accent" style="color:#00B4FC">sécuriser vos marges</span></h1>
                <p class="hero-description" style="color:rgba(255,255,255,0.85)">Depuis plus de 15 ans, Hello Harel accompagne les professionnels de l'agroalimentaire dans la gestion intégrale de leur activité. Notre mission : offrir un <strong>ERP SaaS complet</strong>, conçu spécifiquement pour répondre aux contraintes de traçabilité, de gestion des DLC/DDM, de calcul des marges et de logistique propre au secteur alimentaire.</p>
                <a href="/prometheus/contact/" class="hero-cta" style="background:#fff;color:#005F88;box-shadow:0 10px 25px rgba(0,0,0,0.3)">Contactez-nous pour une démonstration</a>
                <p class="hero-cta-sub" style="color:rgba(255,255,255,0.7)">Sans engagement. Déploiement rapide.</p>
            </div>
            <div class="hero-image-spacer"></div>
        </div>
    </div>
</section>'''

QSN_CSS = '''
.team-card-enhanced { width: 300px !important; }
.team-card-enhanced .team-bio { font-size: 0.8125rem; color: #64748b; line-height: 1.6; margin-top: 0.75rem; text-align: left; }
'''

QSN_CONTENT = '''<!-- TEAM (Enhanced with bios) -->
<section class="team-section">
    <div class="container">
        <div class="section-header">
            <p class="overline">Notre équipe</p>
            <h2>Une équipe humaine</h2>
            <p>Disponible et à l'écoute !</p>
        </div>
        <div class="team-grid">
            <div class="team-card team-card-enhanced scroll-reveal">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2024/10/Timothy-Jolliver-President-de-Hello-Harel-150x150.jpeg" alt="Timothy - Gérant">
                <div class="team-info"><h4>Timothy</h4><p>Gérant</p></div>
                <a href="https://fr.linkedin.com/in/timothy-jollivet-80516070" class="linkedin-btn" target="_blank" rel="noopener"><i class="fab fa-linkedin-in"></i></a>
                <p class="team-bio">Visionnaire et architecte de la solution, Timothy pilote Hello Harel depuis plus de 15 ans. Il s'assure que l'ERP réponde toujours aux exigences techniques et réglementaires les plus strictes du marché agroalimentaire.</p>
            </div>
            <div class="team-card team-card-enhanced scroll-reveal">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Nicolas-150x150.jpeg" alt="Nicolas - Resp. Partenariat">
                <div class="team-info"><h4>Nicolas</h4><p>Resp. Partenariat</p></div>
                <a href="https://fr.linkedin.com/in/nicolas-de-cerner-mercimax" class="linkedin-btn" target="_blank" rel="noopener"><i class="fab fa-linkedin-in"></i></a>
                <p class="team-bio">En charge du développement de l'écosystème Harel. Nicolas noue des alliances stratégiques pour connecter l'ERP à vos outils préférés (comptabilité, e-commerce, marketplaces).</p>
            </div>
            <div class="team-card team-card-enhanced scroll-reveal">
                <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Maxence-150x150.jpeg" alt="Maxence - Resp. Commercial">
                <div class="team-info"><h4>Maxence</h4><p>Resp. Commercial</p></div>
                <a href="https://fr.linkedin.com/in/maxence-flavigny-5a5549120" class="linkedin-btn" target="_blank" rel="noopener"><i class="fab fa-linkedin-in"></i></a>
                <p class="team-bio">Votre premier point de contact. Maxence analyse vos processus actuels pour vous proposer la configuration Hello Harel la plus adaptée à vos besoins.</p>
            </div>
        </div>
    </div>
</section>

<!-- CLIENT LOGO WALL -->
<section class="logos-section" style="padding:4rem 0;background:#fff;border-top:1px solid #f1f5f9;border-bottom:1px solid #f1f5f9">
    <div class="container">
        <div class="section-header" style="margin-bottom:2.5rem">
            <p class="overline">Ils nous font confiance</p>
            <h2>+500 entreprises nous utilisent au quotidien</h2>
        </div>
        <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:2rem;align-items:center;justify-items:center;max-width:900px;margin:0 auto">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Logo_Pro-inter_Magasins_Orientaux.png" alt="Pro-Inter" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/1.png" alt="Leclerc" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Jacob-150x150.jpeg" alt="Jacob" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.14.24-300x64.png" alt="Corseprim" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.12.46.png" alt="Les Primeurs" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.10.42-300x226.png" alt="HPS" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.08.48-300x86.png" alt="Kore" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.07.48-300x165.png" alt="Poujauran" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.06.38-300x131.png" alt="Eatmotion" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.03.06-300x170.png" alt="Ciao Gusto" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.04.34-300x103.png" alt="Chef Cheffe" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.01.39-300x163.png" alt="Savary" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-15.00.01-300x218.png" alt="Karine & Jeff" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-14.57.18-300x122.png" alt="Chrono Primeurs" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
            <img loading="lazy" src="https://www.helloharel.com/wp-content/uploads/2026/01/Capture-decran-2026-01-13-a-14.56.24-300x154.png" alt="Maison Aléna" style="height:2.5rem;width:auto;filter:grayscale(100%);opacity:0.5;transition:all 0.3s">
        </div>
    </div>
</section>

<!-- VALUES -->
<section class="features-section">
    <div class="container">
        <div class="section-header">
            <p class="overline">Nos valeurs</p>
            <h2>Ce qui nous anime au quotidien</h2>
        </div>
        <div class="bento-grid">
            <div class="bento-card">
                <h3>Exigence Qualité</h3>
                <p>Parce que vos produits nourrissent des millions de personnes, notre code est développé pour ne tolérer aucune faille de traçabilité.</p>
            </div>
            <div class="bento-card">
                <h3>Agilité SaaS</h3>
                <p>Fini les installations lourdes et les serveurs locaux. Hello Harel est accessible partout, tout le temps, et toujours à jour.</p>
            </div>
            <div class="bento-card">
                <h3>Proximité Client</h3>
                <p>Une équipe à taille humaine, basée en France, qui connaît vos enjeux métiers et vous répond sans délai.</p>
            </div>
        </div>
    </div>
</section>'''


# ── ECOSYSTEME ──────────────────────────────────────────────────────

ECO_HERO = '''<!-- HERO -->
<section class="hero-section" style="border-bottom:none;">
    <div class="container">
        <div class="hero-grid">
            <div class="hero-text">
                <div class="hero-badge"><span class="dot"></span>Écosystème</div>
                <h1 class="hero-title">Un ERP ouvert, <span class="accent">connecté à vos outils</span></h1>
                <p class="hero-description">Hello Harel est un logiciel de facturation ouvert. Connectez-vous aux services dont vous avez besoin parmi nos partenaires et nos applications métier.</p>
                <div class="hero-ctas">
                    <a href="/prometheus/contact/" class="hero-cta-primary">Demander ma démo gratuite</a>
                    <a href="/prometheus/contact/" class="hero-cta-secondary">Essayez</a>
                </div>
                <p class="hero-cta-sub">Sans engagement. Déploiement rapide.</p>
            </div>
            <div class="hero-image-spacer"></div>
        </div>
    </div>
</section>'''

ECO_CSS = '''
.eco-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.25rem; }
@media (max-width: 1024px) { .eco-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 640px) { .eco-grid { grid-template-columns: 1fr; } }
'''

ECO_MODULES = [
    ("Thème de couleurs","Mettez de la couleur dans votre ERP !"),("Marketplace","Utilisez votre boutique en ligne comme une marketplace. Des marchands tiers pourront vendre leurs produits avec commission automatique."),("Vente en caisse","Effectuez des ventes dans votre boutique physique simplement et efficacement."),("Pôles de préparation","Organisez vos pôles de préparation de commandes pour gagner en productivité."),("Limite d'encours","Définissez une limite d'encours pour vos clients ou bloquez les commandes lors d'un retard de paiement."),("Production","Planifiez et suivez votre production en temps réel."),("Import WooCommerce","Importez vos données de WooCommerce en quelques clics."),("Rungismarket.com","Tout Rungis en un clic. Connectez-vous au marché de Rungis."),("Kimayo","La solution de gestion des ventes dédiée au B2B agroalimentaire, simple, ergonomique et mobile."),("Chorus Pro","Envoyez vos factures à la plateforme Chorus Pro."),("Mercuriales","Créez et envoyez vos mercuriales à vos clients et prospects. Réalisez facilement des sélections de produits personnalisées."),("Colis consignés","Gérez vos colis consignés et suivez les retours de vos emballages."),("Optimisation des tournées","Optimisez vos tournées de livraison pour réduire vos coûts."),("Coffre-fort","Offrez à vos clients un accès sécurisé à leurs données et documents."),("Gestion Électronique des Documents","Accédez à tous vos documents et scannez-en de nouveaux depuis un smartphone ou une tablette."),("Urssaf HomePlus","Vos factures de services à la personne transmises directement à l'Urssaf !"),("Compagnon contacts","Accédez à tous vos contacts et appelez directement depuis votre smartphone."),("Abonnements","Créez des abonnements récurrents et gagnez du temps !"),("Authentification avancée","Gérez les clés et les restrictions d'authentification."),("Codinf","Des réseaux de confiance pour une information fiable."),("Gestion des tournées","Planifiez et gérez vos tournées de livraison."),("Achats","Gérez votre approvisionnement grâce à ce compagnon simple d'utilisation."),("Mandats de prélèvement","Enregistrez vos mandats de prélèvement et exportez vos ordres de prélèvement."),("Mailjet","Tous les outils d'emailing pour atteindre les boîtes de réception."),("Brevo","La solution emailing et CRM pour booster vos ventes."),("Fullsoon","La solution pour gérer les restaurants et stopper le gaspillage alimentaire."),("Tableau de bord","Tous vos indicateurs à portée de main."),("Dimpl","Dimpl, c'est l'assurance d'être payé à temps !"),("Boutique en ligne","Simplifiez votre prise de commande avec votre application de vente en ligne."),("PrestaShop","Gérez plus efficacement les commandes générées par votre site marchand PrestaShop."),("Communication interne","Partagez les informations essentielles en temps réel avec vos collègues."),("Star One","Un thème épuré et très configurable pour votre boutique en ligne."),("Hello EDI","Communiquez avec vos clients grâce au standard international EDI GS1."),("FoodoMarket","Le marché en ligne des restaurateurs et professionnels de l'alimentaire."),("Suggestions de commande","Recevez des suggestions de commande basées sur vos habitudes d'achat."),("Yokitup","La solution de gestion idéale pour la restauration."),("Qualipad","Pratique, tactile et interactive, adoptez la solution QUALIPAD."),("Inventaire","Faites l'inventaire de votre stock sur un smartphone ou une tablette."),("Vente","Faites une vente sur tablette ou smartphone."),("Mailgun","Une plateforme d'envoi d'emails souple, évolutive et axée sur les résultats."),("Smartsupp","Stimulez vos ventes en ligne grâce aux conversations en ligne."),("Prestachef","Prestachef, application de prise de commande pour la restauration."),("Choco","Simplifiez la gestion de vos commandes fournisseurs."),("Signature de bon de livraison","Visualisez les commandes à livrer et obtenez la signature du client sur tablette."),("Carte des clients","Géolocalisez simplement vos clients, fournisseurs et prospects sur une carte."),("Permissions avancées","Limitez l'accès des utilisateurs aux comptes CRM."),("SystemPay","Utilisez SystemPay pour enregistrer les paiements en ligne par carte bancaire."),("FoodFlow","Connectez votre flux alimentaire en temps réel."),("Gestion de flotte","Gérez et suivez votre flotte de véhicules."),("Préparation","Préparez vos commandes sur tablette."),("GCollect","Facilitez le recouvrement de vos factures impayées."),("Orderlion","L'appli des fournisseurs de l'alimentaire et de la boisson."),("StoqueMarket","La meilleure plateforme de courses en ligne pour les restaurateurs."),("Export journal comptable","Exportez votre journal comptable dans plusieurs formats de logiciels comptables."),
]


# ── BLOG ────────────────────────────────────────────────────────────

BLOG_HERO = '''<!-- HERO — compact centered for blog -->
<section class="hero-section blog-hero" style="border-bottom:none;">
    <div class="container">
        <div class="hero-grid">
            <div class="hero-text">
                <div class="hero-badge"><span class="dot"></span>Blog</div>
                <h1 class="hero-title">Ressources et <span class="accent">actualités ERP</span></h1>
                <p class="hero-description">Guides, comparatifs et conseils pour optimiser la gestion de votre entreprise agroalimentaire ou médicale.</p>
                <div class="blog-search">
                    <svg class="blog-search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                    <input type="text" id="blogSearchInput" placeholder="Rechercher un article..." autocomplete="off">
                </div>
            </div>
            <div class="hero-image-spacer"></div>
        </div>
    </div>
</section>'''

BLOG_CSS = '''
.blog-hero { min-height: auto !important; padding-top: 140px !important; padding-bottom: 3rem !important; }
.blog-hero .hero-grid { display: block !important; max-width: 680px; margin: 0 auto; text-align: center; }
.blog-hero .hero-text { text-align: center !important; }
.blog-hero .hero-title { font-size: clamp(2rem, 4.5vw, 3rem) !important; margin-bottom: 0.75rem !important; }
.blog-hero .hero-description { margin: 0 auto 2rem !important; }
.blog-hero .hero-ctas { justify-content: center; }
.blog-hero .hero-image-spacer { display: none; }
.blog-search { max-width: 520px; margin: 0 auto; position: relative; }
.blog-search input { width: 100%%; padding: 0.875rem 1.25rem 0.875rem 3rem; background: rgba(255,255,255,0.12); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.18); border-radius: 9999px; color: #fff; font-size: 0.9375rem; font-family: inherit; font-weight: 500; outline: none; transition: all 0.3s; }
.blog-search input::placeholder { color: rgba(255,255,255,0.5); }
.blog-search input:focus { background: rgba(255,255,255,0.18); border-color: rgba(255,255,255,0.35); }
.blog-search-icon { position: absolute; left: 1.125rem; top: 50%%; transform: translateY(-50%%); width: 18px; height: 18px; color: rgba(255,255,255,0.5); pointer-events: none; }
.blog-section { padding: clamp(3rem,6vw,5rem) 0; background: #f8fafc; }
.blog-layout { display: grid; grid-template-columns: 1fr 280px; gap: 2.5rem; align-items: start; }
.blog-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.75rem; }
.blog-card:first-child { grid-column: 1 / -1; flex-direction: row; }
.blog-card:first-child .blog-card-img { width: 45%%; min-width: 300px; height: auto; min-height: 280px; }
.blog-card:first-child .blog-card-body { padding: 2rem 2.25rem; justify-content: center; }
.blog-card:first-child .blog-card-title { font-size: 1.375rem; line-height: 1.3; margin-bottom: 1rem; }
.blog-card:first-child .blog-card-excerpt { font-size: 0.9rem; line-height: 1.7; -webkit-line-clamp: 4; }
.blog-card:first-child .blog-card-cat { font-size: 0.75rem; padding: 0.3rem 0.875rem; }
.blog-card { background: #fff; border: 1px solid #e5e7eb; border-radius: 1.25rem; overflow: hidden; transition: all 0.4s cubic-bezier(.4,0,.2,1); display: flex; flex-direction: column; text-decoration: none; box-shadow: 0 1px 2px rgba(0,0,0,0.04), 0 4px 16px rgba(0,0,0,0.02); opacity: 0; transform: translateY(24px); animation: blogCardIn 0.5s ease forwards; }
.blog-card:hover { transform: translateY(-6px); box-shadow: 0 16px 48px -8px rgba(0,95,136,0.13), 0 4px 16px rgba(0,0,0,0.05); border-color: #dbeafe; }
@keyframes blogCardIn { to { opacity: 1; transform: translateY(0); } }
.blog-card:nth-child(1) { animation-delay: 0s; } .blog-card:nth-child(2) { animation-delay: 0.08s; } .blog-card:nth-child(3) { animation-delay: 0.16s; } .blog-card:nth-child(4) { animation-delay: 0.24s; } .blog-card:nth-child(5) { animation-delay: 0.32s; } .blog-card:nth-child(6) { animation-delay: 0.4s; } .blog-card:nth-child(n+7) { animation-delay: 0.45s; }
.blog-card-img { width: 100%%; height: 210px; position: relative; background: linear-gradient(135deg, #005F88 0%%, #0891b2 50%%, #3b82f6 100%%); background-size: cover; background-position: center; display: flex; align-items: center; justify-content: center; overflow: hidden; }
.blog-card-img::after { content: ''; position: absolute; inset: 0; background: linear-gradient(0deg, rgba(0,0,0,0.1) 0%%, transparent 50%%); pointer-events: none; transition: opacity 0.4s; }
.blog-card:hover .blog-card-img::after { opacity: 0.6; }
.blog-card-img svg { width: 3rem; height: 3rem; color: rgba(255,255,255,0.25); position: relative; z-index: 1; }
.blog-card-body { padding: 1.375rem 1.5rem 1.5rem; flex: 1; display: flex; flex-direction: column; gap: 0; }
.blog-card-cat { display: inline-flex; align-items: center; gap: 0.325rem; font-size: 0.6875rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; color: #0284c7; background: #eff8ff; padding: 0.25rem 0.625rem; border-radius: 5px; margin-bottom: 0.625rem; width: fit-content; border: 1px solid #dbeafe; }
.blog-card-date { font-size: 0.75rem; font-weight: 500; color: #94a3b8; margin-bottom: 0.5rem; }
.blog-card-title { font-size: 1.0625rem; font-weight: 800; color: #0f172a; line-height: 1.4; margin-bottom: 0.625rem; letter-spacing: -0.01em; transition: color 0.25s; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.blog-card:hover .blog-card-title { color: #0369a1; }
.blog-card-excerpt { font-size: 0.8125rem; color: #64748b; line-height: 1.65; flex: 1; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
.blog-card-readmore { display: inline-flex; align-items: center; gap: 0.375rem; color: #0284c7; font-weight: 700; font-size: 0.8125rem; margin-top: 0.875rem; transition: gap 0.3s; }
.blog-card:hover .blog-card-readmore { gap: 0.625rem; }
.blog-card-readmore svg { width: 14px; height: 14px; transition: transform 0.3s; }
.blog-card:hover .blog-card-readmore svg { transform: translateX(2px); }
.blog-load-more { text-align: center; margin-top: 2.5rem; }
.blog-load-more button { padding: 0.875rem 2.5rem; background: #fff; color: #0284c7; border: 2px solid #0284c7; border-radius: 0.75rem; font-weight: 700; font-size: 0.9375rem; cursor: pointer; font-family: inherit; transition: all 0.3s; }
.blog-load-more button:hover { background: #0284c7; color: #fff; }
.blog-loading-grid { display: contents; }
.blog-skeleton { border-radius: 1.25rem; overflow: hidden; background: #fff; border: 1px solid #e5e7eb; }
.blog-skeleton-img { height: 210px; background: linear-gradient(90deg, #f1f5f9 25%%, #e2e8f0 50%%, #f1f5f9 75%%); background-size: 200%% 100%%; animation: shimmer 1.5s infinite; }
.blog-skeleton-body { padding: 1.375rem 1.5rem; }
.blog-skeleton-line { height: 12px; border-radius: 6px; background: linear-gradient(90deg, #f1f5f9 25%%, #e2e8f0 50%%, #f1f5f9 75%%); background-size: 200%% 100%%; animation: shimmer 1.5s infinite; margin-bottom: 0.75rem; }
.blog-skeleton-line.w60 { width: 60%%; } .blog-skeleton-line.w80 { width: 80%%; } .blog-skeleton-line.w100 { width: 100%%; } .blog-skeleton-line.title { height: 18px; margin-bottom: 1rem; }
@keyframes shimmer { 0%% { background-position: 200%% 0; } 100%% { background-position: -200%% 0; } }
.blog-empty { grid-column: 1 / -1; text-align: center; padding: 4rem 2rem; color: #94a3b8; }
.blog-empty svg { width: 48px; height: 48px; margin: 0 auto 1rem; color: #cbd5e1; }
.blog-empty p { font-size: 1rem; font-weight: 600; color: #64748b; margin-bottom: 0.25rem; }
.blog-empty small { font-size: 0.8125rem; }
.blog-card-author { display: flex; align-items: center; gap: 0.625rem; margin-top: auto; padding-top: 0.875rem; border-top: 1px solid #f1f5f9; }
.blog-card-avatar { width: 30px; height: 30px; border-radius: 50%%; background: linear-gradient(135deg, #0284c7, #06b6d4); color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 0.625rem; flex-shrink: 0; object-fit: cover; }
img.blog-card-avatar { background: none; }
.blog-card-author-info { display: flex; align-items: center; gap: 0.5rem; }
.blog-card-author-name { font-size: 0.75rem; font-weight: 700; color: #334155; }
.blog-card-author-sep { width: 3px; height: 3px; border-radius: 50%%; background: #cbd5e1; }
.blog-card-read-time { font-size: 0.6875rem; color: #94a3b8; }
.blog-sidebar { position: sticky; top: 100px; display: flex; flex-direction: column; gap: 1.25rem; }
.blog-toc { background: #fff; border: 1px solid #e2e8f0; border-radius: 1rem; padding: 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,0.03); }
.blog-toc h3 { font-size: 0.6875rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; color: #94a3b8; margin-bottom: 0.875rem; display: flex; align-items: center; gap: 0.5rem; padding-bottom: 0.75rem; border-bottom: 1px solid #f1f5f9; }
.blog-toc h3 svg { width: 14px; height: 14px; color: #0284c7; }
.blog-toc-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 2px; }
.blog-toc-list li a { display: flex; align-items: center; gap: 0.5rem; padding: 0.5rem 0.625rem; border-radius: 0.5rem; font-size: 0.8125rem; font-weight: 600; color: #475569; text-decoration: none; transition: all 0.2s; border: 1px solid transparent; }
.blog-toc-list li a:hover { background: #f8fafc; color: #0369a1; }
.blog-toc-list li a.active { background: #eff8ff; color: #0284c7; border-color: #dbeafe; }
.blog-toc-list li a .toc-count { margin-left: auto; font-size: 0.625rem; font-weight: 700; background: #f1f5f9; color: #94a3b8; padding: 0.125rem 0.4375rem; border-radius: 9999px; min-width: 22px; text-align: center; }
.blog-toc-list li a.active .toc-count { background: #dbeafe; color: #0284c7; }
.blog-toc-list li a svg { width: 14px; height: 14px; flex-shrink: 0; opacity: 0.5; }
.blog-toc-list li a.active svg { opacity: 1; }
.blog-sidebar-cta { background: linear-gradient(135deg, #005F88 0%%, #0284c7 100%%); border-radius: 1rem; padding: 1.5rem 1.25rem; text-align: center; color: #fff; position: relative; overflow: hidden; }
.blog-sidebar-cta::before { content: ''; position: absolute; top: -25px; right: -25px; width: 80px; height: 80px; border-radius: 50%%; background: rgba(255,255,255,0.06); }
.blog-sidebar-cta h4 { font-size: 1rem; font-weight: 800; margin-bottom: 0.5rem; position: relative; }
.blog-sidebar-cta p { font-size: 0.8125rem; color: rgba(255,255,255,0.75); margin-bottom: 1rem; line-height: 1.55; position: relative; }
.blog-sidebar-cta a { display: block; padding: 0.75rem; background: #fff; color: #005F88; border-radius: 0.75rem; font-weight: 800; font-size: 0.875rem; transition: all 0.3s; text-decoration: none; position: relative; }
.blog-sidebar-cta a:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(0,0,0,0.2); }
@media (max-width: 1200px) { .blog-layout { grid-template-columns: 1fr 250px; gap: 2rem; } }
@media (max-width: 1024px) { .blog-layout { grid-template-columns: 1fr; } .blog-sidebar { position: static; flex-direction: row; flex-wrap: wrap; } .blog-sidebar > * { flex: 1; min-width: 240px; } .blog-toc-list { flex-direction: row; flex-wrap: wrap; gap: 0.375rem; } .blog-toc-list li a { white-space: nowrap; padding: 0.375rem 0.75rem; font-size: 0.75rem; } .blog-card:first-child { flex-direction: row; } .blog-card:first-child .blog-card-img { min-width: 240px; } }
@media (max-width: 768px) { .blog-hero .hero-title { font-size: clamp(1.75rem, 5vw, 2.25rem) !important; } .blog-card:first-child { flex-direction: column; } .blog-card:first-child .blog-card-img { width: 100%%; min-width: unset; min-height: 180px; height: 210px; } .blog-card:first-child .blog-card-body { padding: 1.375rem 1.5rem; } .blog-card:first-child .blog-card-title { font-size: 1.0625rem; } .blog-grid { grid-template-columns: repeat(2, 1fr); gap: 1.25rem; } }
@media (max-width: 640px) { .blog-grid { grid-template-columns: 1fr; gap: 1.25rem; } .blog-card-body { padding: 1.125rem 1.25rem 1.25rem; } .blog-search input { font-size: 0.875rem; padding: 0.75rem 1rem 0.75rem 2.75rem; } }
'''

BLOG_CONTENT = '''<!-- BLOG GRID -->
<section class="blog-section">
    <div class="container">
        <div class="blog-layout">
            <div>
                <div class="blog-grid" id="blogGrid">
                    <div class="blog-loading-grid" id="blogSkeleton">
                        <div class="blog-skeleton" style="grid-column:1/-1"><div class="blog-skeleton-img" style="height:260px"></div><div class="blog-skeleton-body"><div class="blog-skeleton-line w60"></div><div class="blog-skeleton-line title w100"></div><div class="blog-skeleton-line w80"></div><div class="blog-skeleton-line w60"></div></div></div>
                        <div class="blog-skeleton"><div class="blog-skeleton-img"></div><div class="blog-skeleton-body"><div class="blog-skeleton-line w60"></div><div class="blog-skeleton-line title w100"></div><div class="blog-skeleton-line w80"></div></div></div>
                        <div class="blog-skeleton"><div class="blog-skeleton-img"></div><div class="blog-skeleton-body"><div class="blog-skeleton-line w60"></div><div class="blog-skeleton-line title w100"></div><div class="blog-skeleton-line w80"></div></div></div>
                        <div class="blog-skeleton"><div class="blog-skeleton-img"></div><div class="blog-skeleton-body"><div class="blog-skeleton-line w60"></div><div class="blog-skeleton-line title w100"></div><div class="blog-skeleton-line w80"></div></div></div>
                        <div class="blog-skeleton"><div class="blog-skeleton-img"></div><div class="blog-skeleton-body"><div class="blog-skeleton-line w60"></div><div class="blog-skeleton-line title w100"></div><div class="blog-skeleton-line w80"></div></div></div>
                    </div>
                </div>
                <div class="blog-load-more" id="blogLoadMore" style="display:none">
                    <button onclick="loadMorePosts()">Charger plus d\\'articles</button>
                </div>
            </div>
            <aside class="blog-sidebar">
                <div class="blog-toc">
                    <h3><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"/></svg> Catégories</h3>
                    <ul class="blog-toc-list" id="blogToc">
                        <li><a href="#" data-cat="all" class="active"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg> Tous <span class="toc-count" id="tocCountAll">-</span></a></li>
                    </ul>
                </div>
                <div class="blog-sidebar-cta">
                    <h4>Optimisez votre gestion</h4>
                    <p>Découvrez comment Hello Harel transforme votre quotidien.</p>
                    <a href="/prometheus/contact/">Demander une démo</a>
                </div>
            </aside>
        </div>
    </div>
</section>'''

BLOG_JS = '''<script>
var blogPage=1,blogPerPage=12,blogTotal=0,currentCat='all',searchQuery='',categoryMap={},searchTimer=null;
function renderPost(p){var d=new Date(p.date),ds=d.toLocaleDateString('fr-FR',{day:'numeric',month:'long',year:'numeric'}),ex=p.excerpt.rendered.replace(/<[^>]*>/g,'').trim();ex=ex.length>160?ex.substring(0,160)+'...':ex;var t=p.title.rendered,l='/prometheus/'+p.slug+'/',fi=p._embedded&&p._embedded['wp:featuredmedia']&&p._embedded['wp:featuredmedia'][0]?p._embedded['wp:featuredmedia'][0].source_url:'',ih=fi?'<div class="blog-card-img" style="background-image:url('+fi+');background-size:cover;background-position:center"></div>':'<div class="blog-card-img"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/></svg></div>',ch='';if(p.categories&&p.categories.length>0){var cn=categoryMap[p.categories[0]];if(cn)ch='<span class="blog-card-cat">'+cn+'</span>';}var an='Hello Harel',av='';if(p._embedded&&p._embedded.author&&p._embedded.author[0]){an=p._embedded.author[0].name||'Hello Harel';var avs=p._embedded.author[0].avatar_urls||{};av=avs['48']||avs['96']||'';}var ini=an.split(' ').map(function(w){return w[0]}).join('').substring(0,2).toUpperCase(),ah=av?'<img class="blog-card-avatar" src="'+av+'" alt="'+an+'">':'<div class="blog-card-avatar">'+ini+'</div>';return '<a href="'+l+'" class="blog-card">'+ih+'<div class="blog-card-body">'+ch+'<p class="blog-card-date">'+ds+'</p><h3 class="blog-card-title">'+t+'</h3><p class="blog-card-excerpt">'+ex+'</p><div class="blog-card-author">'+ah+'<div class="blog-card-author-info"><span class="blog-card-author-name">'+an+'</span><span class="blog-card-author-sep"></span><span class="blog-card-read-time">5 min</span></div></div><span class="blog-card-readmore">Lire l\\'article <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></span></div></a>';}
function showEmptyState(m){document.getElementById('blogGrid').innerHTML='<div class="blog-empty"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg><p>'+(m||'Aucun article trouvé')+'</p><small>Essayez une autre catégorie ou un autre terme de recherche.</small></div>';}
function loadPosts(){var u='/prometheus/wp-json/wp/v2/posts?per_page='+blogPerPage+'&page='+blogPage+'&_embed=author,wp:featuredmedia&_fields=id,slug,title,excerpt,date,categories,_links,_embedded';if(currentCat!=='all')u+='&categories='+currentCat;if(searchQuery)u+='&search='+encodeURIComponent(searchQuery);fetch(u).then(function(r){blogTotal=parseInt(r.headers.get('X-WP-TotalPages'))||0;return r.json();}).then(function(posts){var g=document.getElementById('blogGrid');if(blogPage===1)g.innerHTML='';if(!posts.length&&blogPage===1){showEmptyState();document.getElementById('blogLoadMore').style.display='none';return;}posts.forEach(function(p){g.innerHTML+=renderPost(p);});document.getElementById('blogLoadMore').style.display=blogPage<blogTotal?'':'none';}).catch(function(){document.getElementById('blogGrid').innerHTML='<div class="blog-empty"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg><p>Impossible de charger les articles</p><small>Vérifiez votre connexion et réessayez.</small></div>';});}
function loadMorePosts(){blogPage++;loadPosts();}
document.getElementById('blogSearchInput').addEventListener('input',function(e){clearTimeout(searchTimer);var v=e.target.value.trim();searchTimer=setTimeout(function(){searchQuery=v;blogPage=1;loadPosts();},350);});
fetch('/prometheus/wp-json/wp/v2/categories?per_page=50&_fields=id,name,count').then(function(r){return r.json();}).then(function(cats){var toc=document.getElementById('blogToc');var total=0;cats.forEach(function(cat){if(cat.count===0||cat.name==='Non classé')return;categoryMap[cat.id]=cat.name;total+=cat.count;var li=document.createElement('li');li.innerHTML='<a href="#" data-cat="'+cat.id+'"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A2 2 0 013 12V7a4 4 0 014-4z"/></svg> '+cat.name+' <span class="toc-count">'+cat.count+'</span></a>';toc.appendChild(li);});document.getElementById('tocCountAll').textContent=total||'-';toc.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();toc.querySelectorAll('a').forEach(function(x){x.classList.remove('active');});a.classList.add('active');currentCat=a.getAttribute('data-cat');blogPage=1;loadPosts();});});}).catch(function(){}).then(function(){loadPosts();});
</script>'''


# ── ERP IA ──────────────────────────────────────────────────────────

ERPIA_HERO = '''<!-- HERO -->
<section class="hero-section" style="background:linear-gradient(rgba(0,50,80,0.75),rgba(0,95,136,0.8)),url('https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1920&h=800&fit=crop&q=80') center/cover no-repeat;border-bottom:none;">
    <div class="container">
        <div class="hero-grid">
            <div class="hero-text">
                <div class="hero-badge"><span class="dot"></span>Nouveau — Intelligence Artificielle</div>
                <h1 class="hero-title" style="color:#fff">L'IA au service de <span class="accent" style="color:#00B4FC">votre ERP agroalimentaire</span></h1>
                <p class="hero-description" style="color:rgba(255,255,255,0.85)">Hello Harel intègre l'intelligence artificielle pour automatiser vos tâches répétitives, prédire vos besoins en stock et optimiser vos marges. Découvrez comment l'IA transforme la gestion de votre entreprise.</p>
                <a href="/prometheus/contact/" class="hero-cta" style="background:#fff;color:#005F88;box-shadow:0 10px 25px rgba(0,0,0,0.3)">Demander une démo IA</a>
                <p class="hero-cta-sub" style="color:rgba(255,255,255,0.7)">Sans engagement. Déploiement rapide.</p>
            </div>
            <div class="hero-image-spacer"></div>
        </div>
    </div>
</section>'''

ERPIA_CSS = '''
.usecases-section { padding: clamp(4rem,8vw,7rem) 0; background: #fff; }
.usecases-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; max-width: 960px; margin: 0 auto; }
.usecase-card { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 1.25rem; padding: 2rem; transition: all 0.35s ease; }
.usecase-card:hover { transform: translateY(-4px); box-shadow: 0 20px 25px -5px rgba(0,0,0,0.08); }
.usecase-number { width: 2.5rem; height: 2.5rem; border-radius: 0.625rem; background: #00B4FC; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1rem; margin-bottom: 1rem; }
.usecase-card h3 { font-size: 1.0625rem; font-weight: 800; color: #101828; margin-bottom: 0.5rem; }
.usecase-card p { font-size: 0.875rem; color: #64748b; line-height: 1.7; }
.usecase-result { display: inline-flex; align-items: center; gap: 0.375rem; margin-top: 0.75rem; font-size: 0.8125rem; font-weight: 700; color: #059669; }
@media (max-width: 640px) { .usecases-grid { grid-template-columns: 1fr; } }
'''

ERPIA_CONTENT = '''<!-- AI FEATURES BENTO -->
<section class="features-section" id="fonctionnalites-ia">
    <div class="container">
        <div class="section-header">
            <p class="overline">ERP & Intelligence Artificielle</p>
            <h2>L'IA au service de votre performance</h2>
            <p>Des algorithmes entraînés sur les données agroalimentaires pour des résultats concrets.</p>
        </div>
        <div class="bento-grid">
            <div class="bento-card span-2 scroll-reveal">
                <div style="position:relative;z-index:1">
                <div class="tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg></div>
                <h3>Intelligence Artificielle Prédictive</h3>
                <p>Anticipez la demande, optimisez vos stocks et maximisez vos marges grâce à des algorithmes d'IA entraînés sur les données du secteur agroalimentaire.</p>
                <ul class="check-list"><li><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>Prévision de la demande à 30/60/90 jours</li><li><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>Réduction des ruptures de stock de 40%</li><li><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>Optimisation automatique des réapprovisionnements</li></ul>
                <a href="/prometheus/contact/" class="card-link">Demander une démo IA <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></a></div>
            </div>
            <div class="bento-card scroll-reveal"><div class="tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/></svg></div><h3>Détection d'anomalies</h3><p>L'IA surveille vos flux en continu et vous alerte en temps réel sur les écarts de marge, les dérives de prix fournisseurs et les comportements inhabituels.</p></div>
            <div class="bento-card scroll-reveal"><div class="tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div><h3>Optimisation des marges</h3><p>Recalcul automatique des prix de vente optimaux en fonction des coûts réels, de la concurrence et de l'élasticité prix de chaque client.</p></div>
            <div class="bento-card scroll-reveal"><div class="tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"/></svg></div><h3>Saisie intelligente</h3><p>Reconnaissance automatique des bons de commande, factures fournisseurs et documents de transport. Moins de saisie, zéro erreur.</p></div>
            <div class="bento-card span-3 scroll-reveal"><div class="bento-crm-inner"><div class="bento-crm-content"><div class="tilted-icon"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg></div><h3>Assistant Commercial IA</h3><p>Un copilote IA pour vos commerciaux : suggestions de cross-sell, alertes clients inactifs, et recommandations de tarifs personnalisés.</p><ul class="check-list-horizontal"><li><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>Cross-sell intelligent</li><li><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>Scoring client prédictif</li><li><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>Relances automatisées</li><li><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>Analyse des tendances</li></ul></div></div></div>
        </div>
    </div>
</section>'''


# ── INTEGRATEURS ────────────────────────────────────────────────────

INTEGRATEURS_HERO = '''<!-- HERO -->
<section class="hero-section" style="background:linear-gradient(rgba(0,50,80,0.75),rgba(0,95,136,0.8)),url('https://images.unsplash.com/photo-1552664730-d307ca884978?w=1920&h=800&fit=crop&q=80') center/cover no-repeat;border-bottom:none;">
    <div class="container">
        <div class="hero-grid">
            <div class="hero-text">
                <div class="hero-badge"><span class="dot"></span>Accompagnement inclus</div>
                <h1 class="hero-title" style="color:#fff">Accompagnement intégrateur <span class="accent" style="color:#00B4FC">inclus dans votre abonnement</span></h1>
                <p class="hero-description" style="color:rgba(255,255,255,0.85)">Hello Harel vous accompagne pour trouver un intégrateur local adapté à votre métier. Formation, paramétrage et accompagnement au changement : tout est prévu pour garantir la réussite de votre projet ERP.</p>
                <div class="hero-ctas">
                    <a href="/prometheus/contact/" class="hero-cta-primary">Demander un accompagnement</a>
                </div>
            </div>
            <div class="hero-image-spacer"></div>
        </div>
    </div>
</section>'''

INTEGRATEURS_CONTENT = '''<!-- SERVICE DESCRIPTION -->
<section style="padding:4rem 0;background:#fff;">
    <div class="container">
        <div class="section-header">
            <p class="overline">Notre service d'intégration</p>
            <h2>Hello Harel vous trouve un intégrateur local adapté à votre métier</h2>
            <p>Contrairement aux ERP traditionnels où vous devez chercher et financer un intégrateur externe, Hello Harel inclut un service d'accompagnement complet. Nous sélectionnons pour vous le partenaire le plus qualifié selon votre secteur d'activité et votre localisation géographique.</p>
        </div>
    </div>
</section>

<!-- BENEFITS CARDS -->
<section style="padding:4rem 0;background:#f8fafc;">
    <div class="container">
        <div class="section-header">
            <p class="overline">Les avantages</p>
            <h2>Un accompagnement terrain à chaque étape</h2>
        </div>
        <div class="bento-grid" style="margin-top:2rem;">
            <div class="bento-card">
                <h3>Formation terrain</h3>
                <p>Votre intégrateur forme vos équipes directement sur site ou en visio. Des sessions adaptées à chaque profil utilisateur pour une prise en main rapide et efficace de l'ERP.</p>
            </div>
            <div class="bento-card">
                <h3>Paramétrage sur-mesure</h3>
                <p>Configuration complète de votre environnement : entrepôts, utilisateurs, droits d'accès, grilles tarifaires, fiches produits et workflows adaptés à votre activité.</p>
            </div>
            <div class="bento-card">
                <h3>Accompagnement au changement</h3>
                <p>La transition vers un nouvel ERP est un projet humain avant tout. Votre intégrateur accompagne vos équipes pour garantir l'adoption et minimiser les résistances au changement.</p>
            </div>
            <div class="bento-card">
                <h3>Support local</h3>
                <p>Un interlocuteur proche de votre entreprise, qui connaît votre région et vos contraintes locales. Support téléphonique et interventions sur site quand nécessaire.</p>
            </div>
        </div>
    </div>
</section>

<!-- CTA BECOME INTEGRATOR -->
<section class="cta-banner">
    <div class="container">
        <div class="cta-banner-inner">
            <h2>Devenir intégrateur partenaire</h2>
            <p>Vous êtes une ESN, un consultant indépendant ou un cabinet de conseil ? Rejoignez notre réseau de partenaires certifiés et développez votre activité d'intégration ERP.</p>
            <a href="/prometheus/contact/" class="hero-cta" style="background:#005F88;color:#fff;box-shadow:0 10px 25px rgba(0,95,136,0.3);border:none;cursor:pointer;font-family:inherit;text-decoration:none;display:inline-block">Devenir intégrateur partenaire</a>
        </div>
    </div>
</section>'''


# ══════════════════════════════════════════════════════════════════════
# PAGE BUILDER — construct full HTML for each page from scratch
# ══════════════════════════════════════════════════════════════════════

def build_tarifs():
    """Build tarifs page: read pricing cards from HTML file."""
    import re
    with open('/workspaces/refonte-helloharel/tarifs.html', 'r') as f:
        html = f.read()
    # Extract pricing section (between <!-- PRICING SECTION --> and <!-- À PROPOS)
    m = re.search(r'(<!-- PRICING SECTION -->.*?</section>)', html, re.DOTALL)
    if not m:
        # Fallback: extract the features-section with id="tarifs"
        m = re.search(r'(<section class="features-section" id="tarifs">.*?</section>)', html, re.DOTALL)
    pricing_html = m.group(1) if m else '<!-- pricing section not found -->'

    return '\n\n'.join([
        HEADER,
        TARIFS_HERO,
        LOGO_CAROUSEL,
        pricing_html,
        ABOUT_VIDEO,
        METIERS_CAROUSEL,
        PROCESS,
        TEAM,
        REVIEWS,
        CTA_BANNER,
        FOOTER,
        STICKY_CTA,
        JS,
    ])


def build_contact():
    return '\n\n'.join([
        HEADER,
        CONTACT_HERO,
        CONTACT_CONTENT,
        LOGO_CAROUSEL,
        ABOUT_VIDEO,
        METIERS_CAROUSEL,
        PROCESS,
        TEAM,
        REVIEWS,
        CTA_BANNER,
        FOOTER,
        STICKY_CTA,
        JS,
    ])


def build_qui_sommes_nous():
    return '\n\n'.join([
        HEADER,
        QSN_HERO,
        QSN_CONTENT,
        ABOUT_VIDEO,
        METIERS_CAROUSEL,
        PROCESS,
        REVIEWS,
        CTA_BANNER,
        FOOTER,
        STICKY_CTA,
        JS,
    ])


def build_ecosysteme():
    # Build the eco grid HTML
    cards = '\n'.join(f'            <div class="bento-card"><h3>{name}</h3><p>{desc}</p></div>' for name, desc in ECO_MODULES)
    eco_section = f'''<!-- ECOSYSTEM GRID -->
<section class="features-section" id="modules">
    <div class="container">
        <div class="section-header">
            <p class="overline">Modules & Intégrations</p>
            <h2>54 modules pour étendre votre ERP</h2>
            <p>Connectez Hello Harel à vos outils préférés</p>
        </div>
        <div class="eco-grid">
{cards}
        </div>
    </div>
</section>'''

    return '\n\n'.join([
        HEADER,
        ECO_HERO,
        LOGO_CAROUSEL,
        eco_section,
        ABOUT_VIDEO,
        METIERS_CAROUSEL,
        PROCESS,
        TEAM,
        REVIEWS,
        CTA_BANNER,
        FOOTER,
        STICKY_CTA,
        JS,
    ])


def build_blog():
    return '\n\n'.join([
        HEADER,
        BLOG_HERO,
        BLOG_CONTENT,
        LOGO_CAROUSEL,
        ABOUT_VIDEO,
        METIERS_CAROUSEL,
        PROCESS,
        TEAM,
        REVIEWS,
        CTA_BANNER,
        FOOTER,
        STICKY_CTA,
        BLOG_JS,
        JS,
    ])


def build_erp_ia():
    return '\n\n'.join([
        HEADER,
        ERPIA_HERO,
        LOGO_CAROUSEL,
        ERPIA_CONTENT,
        ABOUT_VIDEO,
        METIERS_CAROUSEL,
        PROCESS,
        TEAM,
        REVIEWS,
        CTA_BANNER,
        FOOTER,
        STICKY_CTA,
        JS,
    ])


def build_integrateurs():
    return '\n\n'.join([
        HEADER,
        INTEGRATEURS_HERO,
        INTEGRATEURS_CONTENT,
        LOGO_CAROUSEL,
        ABOUT_VIDEO,
        PROCESS,
        TEAM,
        REVIEWS,
        CTA_BANNER,
        FOOTER,
        STICKY_CTA,
        JS,
    ])


# Map slug -> (builder_function, extra_css)
PAGE_BUILDERS = {
    "tarifs":           (build_tarifs, TARIFS_CSS),
    "contact":          (build_contact, CONTACT_CSS),
    "qui-sommes-nous":  (build_qui_sommes_nous, QSN_CSS),
    "ecosysteme":       (build_ecosysteme, ECO_CSS),
    "blog":             (build_blog, BLOG_CSS),
    "erp-ia":           (build_erp_ia, ERPIA_CSS),
    "integrateurs":     (build_integrateurs, ''),
}


# ══════════════════════════════════════════════════════════════════════
# DEPLOY FUNCTION
# ══════════════════════════════════════════════════════════════════════

def deploy_page(slug, page_id):
    """Deploy one context page to WordPress using curl (TLS 1.2)."""
    print(f"\n  Deploying {slug} (id={page_id})...")

    builder, extra_css = PAGE_BUILDERS[slug]
    body_html = builder()
    wrapped = f'<div id="hh-page">\n{body_html}\n</div>'

    extra_style = ''
    if extra_css:
        extra_style = f'\n<style>\n{extra_css}\n</style>'

    full = f'''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style id="hh-preload">#hh-page{{opacity:0;transition:opacity .3s}}</style>
<script>
fetch('{CSS_URL}').then(function(r){{return r.text()}}).then(function(css){{
  var s=document.createElement('style');s.textContent=css;document.head.appendChild(s);
  var p=document.getElementById('hh-preload');if(p)p.remove();
  var e=document.getElementById('hh-page');if(e)e.style.opacity='1';
}});
</script>{extra_style}
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
        print(f"  FAIL | {slug:30s} | id={page_id} | curl exit {result.returncode}")
        print(f"        {result.stderr[:200]}")
        return False

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        print(f"  FAIL | {slug:30s} | id={page_id} | Invalid JSON response")
        print(f"        {result.stdout[:200]}")
        return False

    if 'id' in data:
        rendered = data.get('content', {}).get('rendered', '')
        has_hh = 'id="hh-page"' in rendered
        has_header = 'site-header' in rendered
        has_footer = 'footer-grid' in rendered
        ok = has_hh and has_header and has_footer
        status = "OK" if ok else "WARN"
        print(f"  {status} | {slug:30s} | id={page_id} | {len(rendered):,} chars | hh={has_hh} header={has_header} footer={has_footer}")
        return ok
    else:
        print(f"  FAIL | {slug:30s} | id={page_id} | No 'id' in response")
        print(f"        {result.stdout[:200]}")
        return False


# ══════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    if len(sys.argv) > 1:
        slugs = sys.argv[1:]
        for slug in slugs:
            if slug not in CONTEXT_PAGES:
                print(f"  Unknown page: {slug}")
                print(f"  Available: {', '.join(CONTEXT_PAGES.keys())}")
                sys.exit(1)
    else:
        slugs = list(CONTEXT_PAGES.keys())

    print(f"Deploying {len(slugs)} context page(s)...")
    print("=" * 80)

    ok_count = 0
    fail_count = 0

    for slug in slugs:
        page_id = CONTEXT_PAGES[slug]
        success = deploy_page(slug, page_id)
        if success:
            ok_count += 1
        else:
            fail_count += 1
        time.sleep(2)

    print("\n" + "=" * 80)
    print(f"Done. {ok_count} OK, {fail_count} FAIL out of {len(slugs)} pages.")

    if fail_count > 0:
        sys.exit(1)
