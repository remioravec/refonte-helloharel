#!/usr/bin/env python3
"""
Unique content data for all 16 mega-menu pages.
Each page has: hero, bento (5 cards), faq (4 items with drawer HTML).
All content extracted from original Elementor data + adapted.
"""

# ── FONCTIONNALITÉS (parent page) ──
P_FONCTIONNALITES = {
    "id": 4728, "slug": "fonctionnalites", "name": "Fonctionnalités",
    "hero": {
        "badge": "ERP Modulaire",
        "title_w": "L'ERP qui s'adapte à votre PME,",
        "title_a": "et pas l'inverse !",
        "desc": "100% personnalisable, déploiement express, pilotage centralisé. Un ERP qui s'aligne sur vos processus pour une gestion fluide de toute votre activité agroalimentaire.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2023/08/bg-line-v7.png"
    },
    "bento": {
        "overline": "Modules ERP",
        "heading": "Toutes les fonctionnalités dont vous avez besoin",
        "sub": "Un ERP complet qui couvre l'intégralité de votre chaîne de valeur",
        "cards": [
            {"icon": "users", "color": "blue", "bg_icon": "users", "title": "Gestion de la relation client (CRM)", "desc": "Centralisez vos contacts clients, l'historique des commandes et les relances commerciales. Fidélisez vos clients et développez vos ventes récurrentes.", "checks": ["Historique complet des interactions", "Relances commerciales automatisées", "Tarifs personnalisés par client"], "link": "/prometheus/fonctionnalites/crm/", "link_text": "Découvrir notre CRM"},
            {"icon": "doc", "color": "indigo", "title": "Gestion de la facturation", "desc": "Générez devis, bons de livraison, factures et suivez vos règlements en temps réel. Conformité légale garantie.", "link": "/prometheus/fonctionnalites/facturation/"},
            {"icon": "dollar", "color": "emerald", "title": "Gestion commerciale", "desc": "Organisez vos catalogues produits, promotions et tarifs spécifiques par client ou groupe.", "link": "/prometheus/fonctionnalites/vente/"},
            {"icon": "box", "color": "amber", "title": "Gestion des stocks", "desc": "Suivez vos stocks en temps réel sur plusieurs entrepôts. Évitez les ruptures et optimisez votre trésorerie.", "link": "/prometheus/fonctionnalites/gestion-de-stock/"},
            {"icon": "gear", "color": "purple", "title": "Fabrication, Achats, Logistique & Import-Export", "desc": "Gérez gammes et recettes, anticipez vos approvisionnements, optimisez vos tournées et prenez en charge vos documents douaniers.", "sub_links": [{"text": "Fabrication", "href": "/prometheus/fonctionnalites/fabrication/"}, {"text": "Achats", "href": "/prometheus/fonctionnalites/achat/"}, {"text": "Logistique", "href": "/prometheus/fonctionnalites/logistique/"}, {"text": "Import-Export", "href": "/prometheus/fonctionnalites/import-export/"}]},
        ]
    },
    "faq": {
        "overline": "FAQ Fonctionnalités",
        "heading": "Questions fréquentes sur nos modules",
        "sub": "Tout ce que vous devez savoir avant de choisir votre ERP.",
        "items": [
            {"icon": "shield", "q": "Quels modules sont inclus dans l'ERP Hello Harel ?", "meta": "CRM, facturation, stocks, achats, fabrication...", "html": "<h3>Un ERP complet et modulaire</h3><p>Hello Harel intègre nativement 8 modules : <strong>CRM</strong>, <strong>Facturation</strong>, <strong>Gestion commerciale</strong>, <strong>Stocks</strong>, <strong>Fabrication</strong>, <strong>Achats</strong>, <strong>Logistique</strong> et <strong>Import-Export</strong>. Chaque module est activable indépendamment selon vos besoins.</p><p>Contrairement aux ERP traditionnels qui facturent chaque module séparément, Hello Harel propose un accès complet à tous les modules dans chaque formule.</p>"},
            {"icon": "chart", "q": "L'ERP est-il personnalisable selon mon métier ?", "meta": "Agroalimentaire, traiteur, boulanger, grossiste...", "html": "<h3>100% adaptable à votre réalité terrain</h3><p>Chaque module est paramétrable : champs personnalisés, workflows adaptés, règles de gestion spécifiques. Que vous soyez <strong>traiteur</strong>, <strong>boulanger industriel</strong>, <strong>grossiste en fruits et légumes</strong> ou <strong>charcutier</strong>, l'ERP s'adapte à vos processus.</p><p>Les nomenclatures, les unités de mesure, les modes de calcul de prix et les documents sont tous configurables sans développement.</p>"},
            {"icon": "clock", "q": "Combien de temps pour déployer l'ERP ?", "meta": "Déploiement rapide, sans intégrateur", "html": "<h3>Opérationnel en 3 à 5 jours</h3><p>Hello Harel est un ERP SaaS : pas d'installation serveur, pas d'intégrateur externe. Notre équipe vous accompagne :</p><ul><li><strong>Jour 1</strong> — Import de vos données (clients, produits, tarifs)</li><li><strong>Jour 2</strong> — Paramétrage de vos entrepôts et conditions commerciales</li><li><strong>Jour 3</strong> — Formation de votre équipe (2h en visio) et premières commandes réelles</li></ul>"},
            {"icon": "link", "q": "L'ERP s'intègre-t-il avec mes outils existants ?", "meta": "Comptabilité, e-commerce, EDI...", "html": "<h3>Intégrations natives et API ouverte</h3><p>Hello Harel s'intègre avec les principaux logiciels comptables (export écritures), les plateformes e-commerce et les flux EDI pour la grande distribution.</p><p>Notre API REST permet de connecter n'importe quel outil tiers. Vos données circulent en temps réel entre tous vos systèmes.</p>"},
        ]
    }
}

# ── CRM ──
P_CRM = {
    "id": 4736, "slug": "crm", "name": "CRM - Relation Client",
    "hero": {
        "badge": "Module CRM",
        "title_w": "Logiciel de gestion",
        "title_a": "de la relation client",
        "desc": "Gérer vos clients avec précision n'est plus un luxe, c'est une nécessité. Un ERP CRM centralise toutes les interactions clients, automatise les relances et optimise votre stratégie commerciale.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2025/07/Logiciel-de-gestion-de-la-relation-client-crm.svg"
    },
    "bento": {
        "overline": "CRM Agroalimentaire",
        "heading": "Gérez votre relation client avec un ERP conçu pour votre PME",
        "sub": "qui s'adapte à 100% de vos besoins",
        "cards": [
            {"icon": "database", "color": "blue", "bg_icon": "users", "title": "Centralisation des données clients", "desc": "Regroupez tous vos contacts, devis, historiques d'achats et échanges commerciaux en un seul endroit. Vous gagnez en fiabilité et en rapidité d'accès à l'information.", "checks": ["Fiche client complète et unifiée", "Historique des commandes et échanges", "Conditions tarifaires personnalisées"], "link": "/prometheus/fonctionnalites/crm/", "link_text": "Découvrir le module CRM"},
            {"icon": "chart", "color": "emerald", "title": "Pipeline commercial en temps réel", "desc": "Visualisez votre pipeline commercial, suivez vos opportunités et anticipez vos prévisions de chiffre d'affaires grâce à des tableaux de bord clairs.", "link": "/prometheus/fonctionnalites/crm/"},
            {"icon": "bell", "color": "amber", "title": "Automatisation des relances", "desc": "Programmez vos relances, e-mails et rappels téléphoniques. Votre ERP CRM travaille pour vous, même lorsque vous êtes sur d'autres tâches.", "link": "/prometheus/fonctionnalites/crm/"},
            {"icon": "clipboard", "color": "indigo", "title": "Analyse et reporting", "desc": "Pilotez votre activité avec des rapports détaillés : performances commerciales, clients les plus rentables, périodes creuses.", "link": "/prometheus/fonctionnalites/crm/"},
            {"icon": "users", "color": "purple", "title": "Gestion multi-contacts et segmentation", "desc": "Segmentez votre base clients par secteur, volume, localisation. Ciblez vos actions commerciales et personnalisez vos offres pour chaque segment."},
        ]
    },
    "faq": {
        "overline": "FAQ CRM",
        "heading": "Questions sur la gestion de la relation client",
        "sub": "Tout savoir sur le module CRM de Hello Harel.",
        "items": [
            {"icon": "users", "q": "Qu'est-ce qu'un ERP CRM et en quoi diffère-t-il d'un CRM classique ?", "meta": "ERP vs CRM standalone, données unifiées", "html": "<h3>ERP CRM : le meilleur des deux mondes</h3><p>Un <strong>CRM standalone</strong> (Salesforce, HubSpot) gère vos contacts et opportunités, mais reste déconnecté de votre facturation, de vos stocks et de votre production.</p><p>Un <strong>ERP CRM</strong> comme Hello Harel intègre la relation client directement dans votre chaîne opérationnelle : quand un commercial crée un devis, les stocks sont vérifiés en temps réel, les prix sont calculés sur le coût d'achat réel, et la facture est générée automatiquement à la livraison.</p><h4>Avantages concrets</h4><ul><li><strong>Zéro double saisie</strong> — Les données circulent du devis à la facture sans ressaisie</li><li><strong>Marges en temps réel</strong> — Chaque devis affiche la marge réelle, pas un prix théorique</li><li><strong>Vision 360°</strong> — Commercial, logistique et comptabilité partagent les mêmes données</li></ul>"},
            {"icon": "chart", "q": "Quels sont les avantages mesurables d'un ERP CRM ?", "meta": "ROI, gain de temps, satisfaction client", "html": "<h3>Des résultats concrets dès les premiers mois</h3><p>Nos clients constatent en moyenne :</p><ul><li><strong>+25% de taux de conversion</strong> grâce au suivi structuré des opportunités</li><li><strong>-40% de temps de saisie</strong> sur les commandes récurrentes</li><li><strong>+15% de rétention client</strong> avec les relances automatisées</li></ul><p>Le ROI est mesurable dès le premier trimestre d'utilisation.</p>"},
            {"icon": "gear", "q": "Un ERP CRM est-il adapté à une PME agroalimentaire ?", "meta": "PME, TPE, grossistes, traiteurs", "html": "<h3>Conçu pour les PME du secteur alimentaire</h3><p>Hello Harel a été développé spécifiquement pour les PME agroalimentaires. Pas de fonctionnalités superflues, pas de complexité inutile.</p><p>Le module CRM gère nativement les spécificités du secteur : <strong>multi-tarifs par client</strong>, <strong>conditions commerciales complexes</strong> (remises volume, fidélité, promotionnelles), <strong>historique des commandes par lot</strong>.</p>"},
            {"icon": "dollar", "q": "Comment choisir entre un CRM gratuit et un ERP CRM intégré ?", "meta": "Gratuit vs intégré, TCO, évolutivité", "html": "<h3>Le vrai coût d'un CRM gratuit</h3><p>Les CRM gratuits (HubSpot Free, Zoho Free) semblent attractifs mais présentent des limites critiques pour un grossiste :</p><ul><li><strong>Pas de lien avec vos stocks</strong> — Vous vendez des produits que vous n'avez plus</li><li><strong>Pas de calcul de marge</strong> — Vous ne savez pas si votre devis est rentable</li><li><strong>Export manuel</strong> — Doubles saisies entre CRM et facturation</li></ul><p>Un ERP CRM intégré élimine ces frictions et vous fait gagner bien plus que le coût de l'abonnement.</p>"},
        ]
    }
}

# ── FACTURATION ──
P_FACTURATION = {
    "id": 4750, "slug": "facturation", "name": "Facturation",
    "hero": {
        "badge": "Module Facturation",
        "title_w": "Gagnez du temps et",
        "title_a": "sécurisez votre gestion comptable",
        "desc": "Émettre des factures, suivre les paiements, éviter les erreurs : un logiciel de facturation moderne ne se contente pas de générer des PDF. Il automatise votre cycle de vente complet.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2024/11/shop-assistant-placing-order-from-notepad-into-pos-point-of-sale-terminal-at-register-in-restaurant-2.jpg"
    },
    "bento": {
        "overline": "Facturation ERP",
        "heading": "Gérez votre facturation simplement",
        "sub": "Du devis à l'encaissement, tout est automatisé",
        "cards": [
            {"icon": "clock", "color": "blue", "bg_icon": "doc", "title": "Gain de temps considérable", "desc": "Créez vos devis, transformez-les en factures, enregistrez les paiements : tout se fait en quelques clics. Vous éliminez les doubles saisies et libérez du temps.", "checks": ["Transformation devis → facture en 1 clic", "Numérotation automatique conforme", "Export comptable automatisé"], "link": "/prometheus/fonctionnalites/facturation/", "link_text": "Découvrir la facturation"},
            {"icon": "shield", "color": "emerald", "title": "Moins d'erreurs, plus de sécurité", "desc": "TVA appliquée automatiquement, mentions légales conformes, cohérence des données contrôlée. Vous évitez les erreurs coûteuses et les pénalités fiscales.", "link": "/prometheus/fonctionnalites/facturation/"},
            {"icon": "bell", "color": "amber", "title": "Suivi des paiements clients", "desc": "Identifiez instantanément qui vous doit quoi. Relances automatisées, échéanciers, alertes sur impayés : sécurisez votre trésorerie.", "link": "/prometheus/fonctionnalites/facturation/"},
            {"icon": "chart", "color": "indigo", "title": "Vision claire du chiffre d'affaires", "desc": "Tableaux de bord intégrés pour piloter vos revenus mois par mois, suivre vos meilleures ventes et anticiper votre trésorerie.", "link": "/prometheus/fonctionnalites/facturation/"},
            {"icon": "doc", "color": "purple", "title": "Documents commerciaux complets", "desc": "Devis, bons de commande, bons de livraison, factures, avoirs : tous vos documents sont liés et traçables dans un flux unique."},
        ]
    },
    "faq": {
        "overline": "FAQ Facturation",
        "heading": "Questions sur la facturation",
        "sub": "Simplifiez votre gestion comptable au quotidien.",
        "items": [
            {"icon": "doc", "q": "Qu'est-ce qu'un logiciel de facturation intégré à un ERP ?", "meta": "Devis, factures, avoirs, conformité", "html": "<h3>Plus qu'un simple outil de facturation</h3><p>Un logiciel de facturation intégré à un ERP relie vos factures directement à vos commandes, livraisons et stocks. Quand vous facturez, les stocks sont mis à jour, les marges calculées et la comptabilité alimentée automatiquement.</p><ul><li><strong>Devis → Commande → BL → Facture</strong> en flux continu</li><li><strong>TVA et mentions légales</strong> appliquées automatiquement</li><li><strong>Export comptable</strong> vers votre logiciel comptable</li></ul>"},
            {"icon": "chart", "q": "Pourquoi passer d'Excel à un logiciel de facturation ?", "meta": "Erreurs, conformité, temps perdu", "html": "<h3>Excel n'est pas un outil de facturation</h3><p>Avec Excel, vous risquez :</p><ul><li><strong>Des erreurs de TVA</strong> — calculs manuels, taux obsolètes</li><li><strong>Des doublons de numérotation</strong> — non conforme à la réglementation</li><li><strong>Aucune traçabilité</strong> — impossible de relier facture et livraison</li></ul><p>Un logiciel dédié élimine ces risques et vous fait gagner en moyenne <strong>2 heures par jour</strong> de saisie.</p>"},
            {"icon": "shield", "q": "Le logiciel est-il conforme aux obligations légales ?", "meta": "Anti-fraude TVA, archivage, mentions obligatoires", "html": "<h3>Conformité totale garantie</h3><p>Hello Harel respecte toutes les obligations légales françaises :</p><ul><li><strong>Loi anti-fraude TVA</strong> — Logiciel certifié NF525</li><li><strong>Mentions obligatoires</strong> — Automatiquement ajoutées à chaque facture</li><li><strong>Archivage sécurisé</strong> — Conservation des documents pendant 10 ans</li><li><strong>Piste d'audit fiable</strong> — Traçabilité complète de chaque modification</li></ul>"},
            {"icon": "link", "q": "Puis-je relier mon logiciel de facturation à mon comptable ?", "meta": "Export FEC, intégration comptable", "html": "<h3>Export comptable en 1 clic</h3><p>Hello Harel génère des fichiers d'export compatibles avec tous les grands logiciels comptables (Sage, Cegid, ACD, Quadratus). Votre comptable reçoit des écritures propres, sans ressaisie.</p><p>Le <strong>Fichier des Écritures Comptables (FEC)</strong> est également générable à la demande pour les contrôles fiscaux.</p>"},
        ]
    }
}

# ── VENTE ──
P_VENTE = {
    "id": 4767, "slug": "vente", "name": "Gestion Commerciale",
    "hero": {
        "badge": "Module Vente",
        "title_w": "Boostez vos ventes et",
        "title_a": "pilotez votre business en temps réel",
        "desc": "Dans un marché ultra-concurrentiel, chaque opportunité compte. Un ERP dédié à la gestion des ventes devient le centre névralgique de votre stratégie commerciale.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2024/11/portrait-of-smiling-asian-girl-barista-standing-near-coffee-brewing-kit-making-filter-in-cafe-1.jpg"
    },
    "bento": {
        "overline": "Gestion Commerciale",
        "heading": "Pilotez vos ventes avec précision",
        "sub": "Du catalogue produit à l'analyse des marges",
        "cards": [
            {"icon": "chart", "color": "emerald", "bg_icon": "dollar", "title": "Vision globale et instantanée", "desc": "Gérer ses ventes avec des fichiers Excel, c'est courir après l'information. Un ERP spécialisé change la donne avec des tableaux de bord en temps réel.", "checks": ["Dashboard CA en temps réel", "Marges par produit et par client", "Prévisions de ventes automatiques"], "link": "/prometheus/fonctionnalites/vente/", "link_text": "Découvrir la gestion commerciale"},
            {"icon": "arrows", "color": "blue", "title": "Processus commerciaux fluides", "desc": "Devis, commandes, livraisons, factures : tout est relié. Vous évitez les erreurs et donnez une image professionnelle à vos clients.", "link": "/prometheus/fonctionnalites/vente/"},
            {"icon": "users", "color": "amber", "title": "Collaboration inter-équipes", "desc": "Les informations commerciales sont accessibles à tous : service commercial, production, logistique, comptabilité. Moins d'erreurs, plus de réactivité.", "link": "/prometheus/fonctionnalites/vente/"},
            {"icon": "tag", "color": "indigo", "title": "Multi-tarifs et promotions", "desc": "Gérez des grilles tarifaires illimitées par client, groupe ou volume. Appliquez automatiquement remises et promotions selon vos règles.", "link": "/prometheus/fonctionnalites/vente/"},
            {"icon": "dollar", "color": "purple", "title": "Suivi de marge en temps réel", "desc": "Chaque vente affiche sa marge réelle calculée sur le coût d'achat effectif, pas un prix théorique. Identifiez les produits à perte en un clic."},
        ]
    },
    "faq": {
        "overline": "FAQ Vente",
        "heading": "Questions sur la gestion commerciale",
        "sub": "Optimisez votre stratégie de vente.",
        "items": [
            {"icon": "dollar", "q": "Qu'est-ce qu'un ERP Vente et pourquoi en ai-je besoin ?", "meta": "Centralisation, automatisation, marges", "html": "<h3>Au-delà d'un simple logiciel de vente</h3><p>Un ERP Vente connecte votre activité commerciale à vos stocks, achats et production. Quand un commercial passe une commande, les stocks sont réservés, la marge est calculée en temps réel et la préparation est lancée automatiquement.</p><ul><li><strong>Devis en 30 secondes</strong> — Catalogue produits avec prix et stocks à jour</li><li><strong>Marge instantanée</strong> — Sur chaque ligne du devis, marge nette affichée</li><li><strong>Zéro rupture</strong> — Vérification des stocks à la commande</li></ul>"},
            {"icon": "chart", "q": "Comment l'ERP m'aide-t-il à suivre mes marges ?", "meta": "Prix d'achat réel, freintes, marges nettes", "html": "<h3>Le moteur de marge Hello Harel</h3><p>Notre module calcule la marge sur le <strong>coût d'achat réel</strong> (prix du lot effectivement reçu), pas un CMUP approximatif. Pour chaque vente :</p><ul><li>Prix d'achat effectif du lot</li><li>Frais de transport et manutention imputés</li><li>Pertes matière (freintes) déduites</li><li>Remises et conditions déduites</li></ul><p>Résultat : une marge nette fiable, produit par produit, client par client.</p>"},
            {"icon": "users", "q": "Puis-je gérer des conditions commerciales complexes ?", "meta": "Multi-tarifs, remises, accords cadre", "html": "<h3>Flexibilité tarifaire totale</h3><p>Hello Harel gère nativement :</p><ul><li><strong>Tarifs par client</strong> — Chaque client a sa grille de prix</li><li><strong>Remises conditionnelles</strong> — Volume, fidélité, périodique</li><li><strong>Accords cadre</strong> — Prix négociés sur une période avec plafond</li><li><strong>Promotions flash</strong> — Sur produits proches DLC ou en surstock</li></ul>"},
            {"icon": "link", "q": "L'ERP Vente est-il adapté aux petites entreprises ?", "meta": "TPE, PME, interface simple", "html": "<h3>Simple à utiliser, puissant dans les résultats</h3><p>Hello Harel a été conçu pour des équipes de 2 à 50 personnes. L'interface est intuitive : vos commerciaux sont opérationnels en moins d'une journée de formation.</p><p>Pas besoin d'un DSI ou d'un intégrateur. Vous activez les fonctionnalités dont vous avez besoin, quand vous en avez besoin.</p>"},
        ]
    }
}

# ── GESTION DE STOCK ──
P_STOCK = {
    "id": 4772, "slug": "gestion-de-stock", "name": "Gestion des Stocks",
    "hero": {
        "badge": "Module Stocks",
        "title_w": "Optimisez votre logistique et",
        "title_a": "réduisez vos coûts",
        "desc": "Évitez les ruptures, réduisez vos stocks dormants et gagnez en réactivité. Un ERP dédié à la gestion des stocks sécurise votre trésorerie et satisfait vos clients.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2025/07/Logiciel-de-gestion-des-achats-1.png"
    },
    "bento": {
        "overline": "Stocks & Entrepôts",
        "heading": "Maîtrisez vos stocks en temps réel",
        "sub": "Multi-entrepôts, traçabilité lots, alertes automatiques",
        "cards": [
            {"icon": "warehouse", "color": "amber", "bg_icon": "box", "title": "Multi-entrepôts", "desc": "Pilotez vos stocks sur plusieurs sites depuis une seule interface. Vision globale ou détaillée par entrepôt, avec transferts inter-sites tracés.", "checks": ["Stocks par entrepôt en temps réel", "Transferts inter-sites avec traçabilité", "Consolidation multi-sites en 1 clic"], "link": "/prometheus/fonctionnalites/gestion-de-stock/", "link_text": "Découvrir la gestion de stock"},
            {"icon": "search", "color": "blue", "title": "Traçabilité lots et séries", "desc": "Traçabilité totale des lots et numéros de séries. Indispensable pour les secteurs soumis à des normes strictes comme l'agroalimentaire.", "link": "/prometheus/fonctionnalites/gestion-de-stock/"},
            {"icon": "bell", "color": "red", "title": "Alertes seuils mini/maxi", "desc": "Alertes automatiques dès que vos stocks passent en dessous ou au-dessus des seuils définis. Anticipez vos achats et évitez ruptures ou surstock.", "link": "/prometheus/fonctionnalites/gestion-de-stock/"},
            {"icon": "clipboard", "color": "emerald", "title": "Inventaires simplifiés", "desc": "Interface intuitive pour le comptage physique, cohérence des écarts, inventaires tournants ou complets.", "link": "/prometheus/fonctionnalites/gestion-de-stock/"},
            {"icon": "link", "color": "purple", "title": "Connexion ventes/achats", "desc": "Toutes vos opérations de ventes et d'achats sont synchronisées en temps réel avec les stocks. Intégration totale qui élimine les doubles saisies et réduit les erreurs."},
        ]
    },
    "faq": {
        "overline": "FAQ Stocks",
        "heading": "Questions sur la gestion des stocks",
        "sub": "Optimisez vos entrepôts et votre trésorerie.",
        "items": [
            {"icon": "box", "q": "Quelles méthodes de valorisation des stocks sont disponibles ?", "meta": "CMUP, FIFO, prix standard, par site", "html": "<h3>4 méthodes de valorisation</h3><table><thead><tr><th>Méthode</th><th>Principe</th><th>Adapté pour</th></tr></thead><tbody><tr><td>CMUP</td><td>Coût moyen unitaire pondéré</td><td>Produits secs, conserves</td></tr><tr><td>FIFO</td><td>Premier entré, premier sorti</td><td>Produits frais, DLC courtes</td></tr><tr><td>Prix standard</td><td>Prix fixé manuellement</td><td>Produits importés, cours fixe</td></tr><tr><td>Par site</td><td>Valorisation indépendante par entrepôt</td><td>Multi-régions</td></tr></tbody></table>"},
            {"icon": "warehouse", "q": "Comment gérer plusieurs entrepôts ?", "meta": "Multi-sites, transferts, consolidation", "html": "<h3>Gestion multi-sites native</h3><p>Hello Harel gère un nombre illimité d'entrepôts : dépôts régionaux, chambres froides, quais, zones de picking, véhicules frigorifiques.</p><ul><li><strong>Vision consolidée</strong> — Stocks totaux en un clic</li><li><strong>Transferts tracés</strong> — Ordres de transfert avec lots, dates, transporteur</li><li><strong>Règles par site</strong> — Seuils, méthodes de valorisation et alertes indépendantes</li></ul>"},
            {"icon": "shield", "q": "Comment la traçabilité fonctionne-t-elle ?", "meta": "Lots, numéros de série, DLC, rappels", "html": "<h3>Traçabilité ascendante et descendante</h3><p>Chaque mouvement de stock est tracé avec : <strong>numéro de lot</strong>, <strong>date de réception</strong>, <strong>fournisseur</strong>, <strong>DLC/DLUO</strong>. En cas de rappel produit, vous identifiez en quelques secondes tous les clients concernés.</p>"},
            {"icon": "chart", "q": "Quel impact sur ma trésorerie ?", "meta": "Surstock, ruptures, BFR", "html": "<h3>Réduction du BFR mesurable</h3><p>Nos clients constatent en moyenne :</p><ul><li><strong>-35% de ruptures de stock</strong></li><li><strong>-20% de surstock dormant</strong></li><li><strong>-15 000€/an</strong> de coûts logistiques évités (grossiste 3 sites)</li></ul><p>Le module optimise vos niveaux de stock pour libérer de la trésorerie sans compromettre votre taux de service.</p>"},
        ]
    }
}

# ── FABRICATION ──
P_FABRICATION = {
    "id": 4778, "slug": "fabrication", "name": "Fabrication",
    "hero": {
        "badge": "Module Fabrication",
        "title_w": "Gagnez en productivité et",
        "title_a": "en rentabilité",
        "desc": "Sans outil adapté, gérer la production est un casse-tête. Ordres de fabrication dispersés, retards, surcharges machines, coûts mal maîtrisés. Notre module GPAO change la donne.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2025/07/Logiciel-de-gestion-des-achats.png"
    },
    "bento": {
        "overline": "GPAO & Production",
        "heading": "Pilotez votre production de A à Z",
        "sub": "Nomenclatures, ordres de fabrication, coûts de revient",
        "cards": [
            {"icon": "calendar", "color": "red", "bg_icon": "gear", "title": "Ordonnancement de la production", "desc": "Ajustez vos plannings en fonction des commandes, ressources disponibles et délais. Garantissez une fluidité maximale sur vos lignes de production.", "checks": ["Planning dynamique par atelier", "Gestion des capacités machines", "Ajustement temps réel aux commandes"], "link": "/prometheus/fonctionnalites/fabrication/", "link_text": "Découvrir le module fabrication"},
            {"icon": "list", "color": "blue", "title": "Suivi des ordres de fabrication", "desc": "Chaque OF est tracé en temps réel, du lancement au produit fini. Visibilité sur l'avancement, consommations matières et temps de fabrication.", "link": "/prometheus/fonctionnalites/fabrication/"},
            {"icon": "gear", "color": "amber", "title": "Nomenclatures et gammes", "desc": "Gérez des nomenclatures complexes multi-niveaux et des gammes opératoires détaillées pour calculer précisément vos besoins et temps.", "link": "/prometheus/fonctionnalites/fabrication/"},
            {"icon": "dollar", "color": "emerald", "title": "Calcul des coûts de production", "desc": "Calcul automatique des coûts : matières premières, main-d'œuvre, charges. Analysez vos marges et repérez les postes d'économie.", "link": "/prometheus/fonctionnalites/fabrication/"},
            {"icon": "box", "color": "purple", "title": "Gestion intégrée des stocks matières", "desc": "Stocks de matières premières intégrés au module production. Évitez les ruptures, anticipez vos approvisionnements et limitez le capital immobilisé."},
        ]
    },
    "faq": {
        "overline": "FAQ Fabrication",
        "heading": "Questions sur le module fabrication",
        "sub": "Maîtrisez votre production agroalimentaire.",
        "items": [
            {"icon": "gear", "q": "Comment fonctionne l'ordonnancement dans Hello Harel ?", "meta": "Planning, capacités, ajustements", "html": "<h3>Ordonnancement dynamique</h3><p>Le module planifie automatiquement vos ordres de fabrication en tenant compte des <strong>capacités machines</strong>, des <strong>disponibilités matières</strong> et des <strong>délais de livraison clients</strong>.</p><p>En cas de commande urgente ou de retard fournisseur, le planning se réajuste en temps réel.</p>"},
            {"icon": "dollar", "q": "Comment calculer le coût de revient d'un produit fini ?", "meta": "Matières, MO, charges, rendements", "html": "<h3>Coût de revient au centime près</h3><p>Hello Harel calcule le coût de revient en intégrant :</p><ul><li><strong>Matières premières</strong> — Au coût d'achat réel du lot utilisé</li><li><strong>Main-d'œuvre</strong> — Temps passé × coût horaire par poste</li><li><strong>Pertes et rendements</strong> — Freintes, évaporation, chutes</li><li><strong>Charges indirectes</strong> — Énergie, amortissements, emballages</li></ul>"},
            {"icon": "list", "q": "Peut-on gérer des nomenclatures multi-niveaux ?", "meta": "Recettes, sous-ensembles, composants", "html": "<h3>Nomenclatures arborescentes</h3><p>Oui. Hello Harel gère des nomenclatures sur autant de niveaux que nécessaire. Exemple : un plat cuisiné peut avoir une nomenclature principale qui référence des sous-recettes (sauces, garnitures), chacune ayant sa propre liste de composants.</p><p>Les besoins en matières sont calculés automatiquement à chaque niveau.</p>"},
            {"icon": "chart", "q": "Quels gains de productivité attendre ?", "meta": "ROI, temps, pertes, marges", "html": "<h3>Résultats mesurés chez nos clients</h3><ul><li><strong>-30% de temps de planification</strong> grâce à l'ordonnancement automatique</li><li><strong>-25% de pertes matières</strong> avec le suivi des rendements en temps réel</li><li><strong>+5 points de marge</strong> grâce au calcul précis des coûts de revient</li><li><strong>Zéro rupture de matière</strong> grâce à l'intégration stocks/production</li></ul>"},
        ]
    }
}

# ── ACHAT ──
P_ACHAT = {
    "id": 4798, "slug": "achat", "name": "Achats",
    "hero": {
        "badge": "Module Achats",
        "title_w": "Optimisez vos coûts et",
        "title_a": "sécurisez vos approvisionnements",
        "desc": "Vos achats représentent une part stratégique de vos coûts. Un logiciel de gestion des achats vous aide à mieux négocier, sécuriser vos approvisionnements et renforcer votre marge.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2025/07/Logiciel-de-grossistes-alimentaire-1.png"
    },
    "bento": {
        "overline": "Achats & Fournisseurs",
        "heading": "Pilotez vos achats avec précision",
        "sub": "Fournisseurs, comparaison des prix, commandes automatiques",
        "cards": [
            {"icon": "users", "color": "teal", "bg_icon": "cart", "title": "Gestion des fournisseurs", "desc": "Centralisez toutes vos fiches fournisseurs, historiques d'achats, conditions tarifaires et délais pour mieux négocier et sécuriser vos relations.", "checks": ["Fiches fournisseurs complètes", "Historique des achats et conditions", "Évaluation des performances fournisseurs"], "link": "/prometheus/fonctionnalites/achat/", "link_text": "Découvrir le module achats"},
            {"icon": "tag", "color": "blue", "title": "Comparaison des conditions", "desc": "Comparez en un clic les prix et conditions de plusieurs fournisseurs pour un même produit. Gagnez en pouvoir de négociation.", "link": "/prometheus/fonctionnalites/achat/"},
            {"icon": "clipboard", "color": "amber", "title": "Suivi des commandes", "desc": "Suivi en temps réel : état de traitement, délais, réceptions partielles ou complètes. Contrôle total sur votre chaîne d'approvisionnement.", "link": "/prometheus/fonctionnalites/achat/"},
            {"icon": "bell", "color": "red", "title": "Alertes et seuils", "desc": "Alertes automatiques sur seuils minimums pour anticiper vos réapprovisionnements et éviter les ruptures.", "link": "/prometheus/fonctionnalites/achat/"},
            {"icon": "cart", "color": "purple", "title": "Commandes automatiques et réappro", "desc": "Génération automatique de commandes d'achat basée sur les seuils de stock, les ventes prévisionnelles et les délais fournisseurs."},
        ]
    },
    "faq": {
        "overline": "FAQ Achats",
        "heading": "Questions sur la gestion des achats",
        "sub": "Optimisez vos approvisionnements et vos coûts.",
        "items": [
            {"icon": "cart", "q": "Qu'est-ce qu'un logiciel ERP achat ?", "meta": "Fournisseurs, commandes, négociation", "html": "<h3>Bien plus qu'un carnet de commandes</h3><p>Un ERP achat centralise toute la relation fournisseur : <strong>catalogues produits</strong>, <strong>conditions négociées</strong>, <strong>historique des prix</strong>, <strong>délais de livraison</strong>. Il automatise les commandes récurrentes et alerte sur les variations de prix.</p>"},
            {"icon": "dollar", "q": "Comment l'ERP m'aide-t-il à réduire mes coûts d'achat ?", "meta": "Comparaison prix, négociation, volume", "html": "<h3>Leviers de réduction des coûts</h3><ul><li><strong>Comparaison fournisseurs</strong> — Prix, délais et conditions côte à côte</li><li><strong>Détection des hausses</strong> — Alerte quand un fournisseur augmente ses prix au-delà d'un seuil</li><li><strong>Groupement de commandes</strong> — Consolidez les achats pour atteindre les paliers de remise</li><li><strong>Historique des prix</strong> — Base factuelle pour renégocier vos contrats</li></ul>"},
            {"icon": "bell", "q": "Les commandes d'achat peuvent-elles être automatisées ?", "meta": "Seuils, prévisions, récurrence", "html": "<h3>Réapprovisionnement intelligent</h3><p>Oui. Hello Harel génère automatiquement des propositions de commande basées sur :</p><ul><li>Les <strong>seuils de stock minimum</strong> paramétrés</li><li>Les <strong>ventes prévisionnelles</strong> des semaines suivantes</li><li>Les <strong>délais de livraison fournisseurs</strong></li></ul><p>Vous validez en un clic, le bon de commande est envoyé au fournisseur.</p>"},
            {"icon": "shield", "q": "Comment gérer les réceptions partielles ?", "meta": "Réceptions, contrôle qualité, litiges", "html": "<h3>Réceptions flexibles et traçables</h3><p>Chaque réception est enregistrée lot par lot, avec contrôle des quantités, de la qualité et des DLC. Les réceptions partielles mettent à jour les stocks et le solde de la commande en temps réel.</p><p>En cas de litige (quantité manquante, qualité insuffisante), un avoir fournisseur est généré automatiquement.</p>"},
        ]
    }
}

# ── LOGISTIQUE ──
P_LOGISTIQUE = {
    "id": 4791, "slug": "logistique", "name": "Logistique",
    "hero": {
        "badge": "Module Logistique",
        "title_w": "Gagnez en rapidité et",
        "title_a": "en efficacité",
        "desc": "Votre logistique n'a plus le droit à l'erreur. Un logiciel de gestion logistique intégré à un ERP optimise vos tournées, vos transporteurs et votre préparation de commandes.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2025/07/Logiciel-de-gestion-des-achats-1.png"
    },
    "bento": {
        "overline": "Logistique & Livraisons",
        "heading": "Optimisez vos expéditions et tournées",
        "sub": "Planification, suivi temps réel, préparation de commandes",
        "cards": [
            {"icon": "truck", "color": "cyan", "bg_icon": "arrows", "title": "Optimisation des tournées", "desc": "Planifiez vos tournées de livraison en tenant compte des contraintes géographiques, des créneaux clients et des capacités de vos véhicules.", "checks": ["Planification géographique des tournées", "Respect des créneaux de livraison", "Optimisation des chargements"], "link": "/prometheus/fonctionnalites/logistique/", "link_text": "Découvrir le module logistique"},
            {"icon": "search", "color": "blue", "title": "Suivi en temps réel", "desc": "Visualisez l'état de vos livraisons en temps réel. Informez vos clients de l'avancement et anticipez les retards.", "link": "/prometheus/fonctionnalites/logistique/"},
            {"icon": "warehouse", "color": "amber", "title": "Gestion des entrepôts (WMS)", "desc": "Organisez vos zones de picking, optimisez les parcours de préparation et réduisez les erreurs de préparation.", "link": "/prometheus/fonctionnalites/logistique/"},
            {"icon": "clipboard", "color": "emerald", "title": "Préparation des commandes", "desc": "Bons de préparation optimisés par zone, contrôle des quantités, validation par scan. Réduisez les erreurs de 80%.", "link": "/prometheus/fonctionnalites/logistique/"},
            {"icon": "arrows", "color": "purple", "title": "Gestion multi-transporteurs", "desc": "Comparez les tarifs transporteurs, générez les étiquettes et bordereaux, suivez les colis. Tout depuis un seul écran."},
        ]
    },
    "faq": {
        "overline": "FAQ Logistique",
        "heading": "Questions sur la gestion logistique",
        "sub": "Livrez plus vite, mieux et moins cher.",
        "items": [
            {"icon": "truck", "q": "Qu'est-ce qu'un logiciel ERP logistique ?", "meta": "Tournées, WMS, préparation, suivi", "html": "<h3>La logistique intégrée à votre ERP</h3><p>Un ERP logistique connecte vos entrepôts, vos transporteurs et vos clients dans un flux unique. Quand une commande est validée, la préparation est lancée, la tournée planifiée et le client informé automatiquement.</p>"},
            {"icon": "clock", "q": "Comment réduire mes délais de livraison ?", "meta": "Préparation, tournées, automatisation", "html": "<h3>Les 3 leviers de réduction des délais</h3><ul><li><strong>Préparation optimisée</strong> — Parcours de picking par zone, scan de contrôle, bons de préparation automatiques</li><li><strong>Tournées intelligentes</strong> — Regroupement géographique, respect des créneaux, chargement optimisé</li><li><strong>Automatisation</strong> — De la commande à l'étiquette transporteur, zéro intervention manuelle</li></ul>"},
            {"icon": "bell", "q": "Le module gère-t-il la chaîne du froid ?", "meta": "Température, véhicules frigorifiques, alertes", "html": "<h3>Chaîne du froid maîtrisée</h3><p>Le module logistique distingue les zones de stockage par température et affecte automatiquement les véhicules frigorifiques adaptés. Les alertes température sont intégrées au processus de livraison.</p>"},
            {"icon": "chart", "q": "Quels gains concrets attendre ?", "meta": "Erreurs, coûts, satisfaction client", "html": "<h3>Résultats mesurés</h3><ul><li><strong>-80% d'erreurs de préparation</strong> grâce au scan et contrôle</li><li><strong>-20% de coûts de transport</strong> grâce à l'optimisation des tournées</li><li><strong>+95% de taux de service</strong> (livraison complète et dans les délais)</li></ul>"},
        ]
    }
}

# ── IMPORT-EXPORT ──
P_IMPORT_EXPORT = {
    "id": 4813, "slug": "import-export", "name": "Import-Export",
    "hero": {
        "badge": "Module Import-Export",
        "title_w": "Simplifiez vos",
        "title_a": "opérations internationales",
        "desc": "Importer ou exporter, c'est gérer des réglementations complexes, des documents douaniers et des coûts élevés. Avec notre ERP, simplifiez chaque étape de vos opérations internationales.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2025/07/Logiciel-de-grossistes-alimentaire-4.png"
    },
    "bento": {
        "overline": "Import-Export",
        "heading": "Gérez vos opérations internationales",
        "sub": "Douanes, multi-devises, certificats, suivi mondial",
        "cards": [
            {"icon": "doc", "color": "orange", "bg_icon": "globe", "title": "Formalités douanières", "desc": "Déclarations douanières automatisées, gestion des nomenclatures TARIC et certificats d'origine pour une conformité totale.", "checks": ["Déclarations douanières automatiques", "Codes TARIC et certificats d'origine", "Documents phytosanitaires et vétérinaires"], "link": "/prometheus/fonctionnalites/import-export/", "link_text": "Découvrir le module import-export"},
            {"icon": "search", "color": "blue", "title": "Suivi des expéditions mondiales", "desc": "Tracking en temps réel de vos marchandises partout dans le monde. Informez vos clients à chaque étape de la chaîne logistique.", "link": "/prometheus/fonctionnalites/import-export/"},
            {"icon": "dollar", "color": "emerald", "title": "Calcul des droits et taxes", "desc": "Calcul automatique des droits de douane, TVA intracommunautaire et taxes spécifiques selon les accords internationaux.", "link": "/prometheus/fonctionnalites/import-export/"},
            {"icon": "globe", "color": "amber", "title": "Gestion multi-devises", "desc": "Transactions en multi-devises avec conversions automatiques et intégration comptable. Vision claire de vos marges à l'international.", "link": "/prometheus/fonctionnalites/import-export/"},
            {"icon": "shield", "color": "purple", "title": "Conformité réglementaire internationale", "desc": "Gestion des normes sanitaires par pays, certificats phytosanitaires, documents vétérinaires et traçabilité lot par lot pour l'export."},
        ]
    },
    "faq": {
        "overline": "FAQ Import-Export",
        "heading": "Questions sur le module import-export",
        "sub": "Simplifiez vos opérations à l'international.",
        "items": [
            {"icon": "globe", "q": "À quoi sert un ERP import-export ?", "meta": "Douanes, certificats, multi-devises", "html": "<h3>Gestion complète du commerce international</h3><p>Un ERP import-export centralise toute la documentation, les calculs de droits et taxes, le suivi des expéditions et la gestion multi-devises. Il élimine les erreurs manuelles qui peuvent coûter très cher en pénalités douanières.</p>"},
            {"icon": "doc", "q": "Quels documents peut générer l'ERP ?", "meta": "DAU, certificats, factures proforma", "html": "<h3>Documents générés automatiquement</h3><ul><li><strong>Factures proforma</strong> pour les expéditions</li><li><strong>Certificats d'origine</strong> et certificats phytosanitaires</li><li><strong>Documents d'accompagnement</strong> (DAU, carnet ATA)</li><li><strong>Listes de colisage</strong> détaillées</li><li><strong>Certificats sanitaires</strong> et vétérinaires</li></ul>"},
            {"icon": "dollar", "q": "Comment sont calculés les droits de douane ?", "meta": "TARIC, accords préférentiels, TVA", "html": "<h3>Calcul automatique et fiable</h3><p>L'ERP applique les taux de droits de douane selon la <strong>nomenclature TARIC</strong>, en tenant compte des accords préférentiels (UE, accords bilatéraux). La TVA intracommunautaire est gérée automatiquement avec les régimes d'autoliquidation.</p>"},
            {"icon": "shield", "q": "L'ERP gère-t-il les réglementations sanitaires à l'export ?", "meta": "Phytosanitaire, vétérinaire, HACCP", "html": "<h3>Conformité sanitaire internationale</h3><p>Oui. L'ERP gère les exigences sanitaires par pays de destination : certificats phytosanitaires, certificats vétérinaires, preuves de traçabilité lot par lot, et documentation HACCP complète.</p>"},
        ]
    }
}

# ── AGROALIMENTAIRE ──
P_AGRO = {
    "id": 1726, "slug": "agroalimentaire", "name": "ERP Agroalimentaire",
    "hero": {
        "badge": "ERP Agroalimentaire",
        "title_w": "Optimisez votre production,",
        "title_a": "maîtrisez vos coûts",
        "desc": "Dans l'agroalimentaire, il faut anticiper les variations saisonnières, assurer la traçabilité, garantir la qualité et protéger vos marges. Notre ERP répond à tous ces défis.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2026/02/Screenshot-2026-02-14-08.34.42.png"
    },
    "bento": {
        "overline": "ERP Agroalimentaire",
        "heading": "L'ERP conçu pour l'industrie alimentaire",
        "sub": "Traçabilité, DLC, coûts de revient, conformité HACCP",
        "cards": [
            {"icon": "search", "color": "blue", "bg_icon": "shield", "title": "Gestion des lots et traçabilité", "desc": "Chaque mouvement est tracé de l'entrée matière première au produit fini. Retrouvez instantanément l'origine ou la destination d'un lot en cas d'alerte sanitaire.", "checks": ["Traçabilité ascendante et descendante", "Historique complet par lot", "Rappel produit en quelques secondes"], "link": "/prometheus/agroalimentaire/", "link_text": "Découvrir l'ERP agroalimentaire"},
            {"icon": "calendar", "color": "amber", "title": "Gestion des DLC et DLUO", "desc": "Gestion automatique de vos dates limites. Alertes quand vos stocks approchent de la péremption. FIFO automatique pour limiter les pertes.", "link": "/prometheus/agroalimentaire/"},
            {"icon": "dollar", "color": "emerald", "title": "Calcul du coût de revient", "desc": "Coût de revient au centime près pour chaque produit fini. Maîtrisez vos marges même avec des prix matières fluctuants.", "link": "/prometheus/agroalimentaire/"},
            {"icon": "thermo", "color": "red", "title": "Gestion des stocks sensibles", "desc": "Stocks à contraintes sanitaires : température, hygrométrie. Alertes automatiques en cas de dépassement des seuils autorisés.", "link": "/prometheus/agroalimentaire/"},
            {"icon": "shield", "color": "purple", "title": "Conformité HACCP et réglementaire", "desc": "Enregistrements numériques, plans de nettoyage, documentation pour les autorités sanitaires. Soyez toujours prêt pour les contrôles."},
        ]
    },
    "faq": {
        "overline": "FAQ Agroalimentaire",
        "heading": "Questions sur l'ERP agroalimentaire",
        "sub": "Tout savoir sur la gestion ERP dans le secteur alimentaire.",
        "items": [
            {"icon": "shield", "q": "Qu'est-ce qu'un ERP agroalimentaire et pourquoi est-il différent ?", "meta": "Traçabilité, DLC, HACCP, lots", "html": "<h3>Un ERP conçu pour les contraintes alimentaires</h3><p>Un ERP agroalimentaire intègre nativement les fonctionnalités critiques du secteur que les ERP généralistes ignorent :</p><ul><li><strong>Traçabilité lot par lot</strong> — De la matière première au client final</li><li><strong>Gestion des DLC/DLUO</strong> — Alertes automatiques, FIFO forcé</li><li><strong>Calcul de freinte</strong> — Pertes matière intégrées au coût de revient</li><li><strong>Conformité HACCP</strong> — Documentation et enregistrements numériques</li></ul>"},
            {"icon": "search", "q": "Comment l'ERP gère-t-il la traçabilité ?", "meta": "Lots, rappels, ascendante/descendante", "html": "<h3>Traçabilité totale en quelques secondes</h3><p>Chaque lot entrant reçoit un numéro unique. À chaque opération (transformation, conditionnement, expédition), le lien entre lots est enregistré.</p><p>En cas de rappel produit, vous identifiez en <strong>moins de 30 secondes</strong> tous les clients ayant reçu un lot concerné.</p>"},
            {"icon": "dollar", "q": "Peut-on calculer le coût de revient avec précision ?", "meta": "Matières, MO, pertes, rendements", "html": "<h3>Coût de revient au centime</h3><p>L'ERP intègre dans le calcul : prix d'achat réel du lot, frais de transport, pertes de transformation (freintes), temps de main-d'œuvre, charges indirectes. Le coût de revient est recalculé en temps réel à chaque réception de matière première.</p>"},
            {"icon": "chart", "q": "L'ERP s'adapte-t-il à mon métier spécifique ?", "meta": "Traiteur, boulanger, charcutier, grossiste", "html": "<h3>7 métiers, un seul ERP</h3><p>Hello Harel est paramétrable pour chaque métier :</p><ul><li><strong>Traiteur</strong> — Gestion événementielle et fiches techniques</li><li><strong>Boulanger</strong> — Cycles de production et multi-points de vente</li><li><strong>Charcutier</strong> — Rendements matière et traçabilité vétérinaire</li><li><strong>Maraîcher</strong> — Prix du jour et certificats phytosanitaires</li><li><strong>Laitier</strong> — Collecte, affinage et paiement à la qualité</li><li><strong>Plats cuisinés</strong> — PRI, allergènes INCO et planning GMS</li></ul>"},
        ]
    }
}

# ── TRAITEUR ──
P_TRAITEUR = {
    "id": 2839, "slug": "traiteur", "name": "ERP Traiteur", "metier_slug": "plats-cuisines",
    "hero": {
        "badge": "ERP Traiteur",
        "title_w": "Planifiez vos événements,",
        "title_a": "sublimez vos prestations",
        "desc": "Être traiteur, c'est gérer des événements complexes, des fiches techniques, des stocks sensibles et des délais serrés. Transformez vos contraintes en avantages concurrentiels.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2025/10/ERP-logiciel-pour-les-grossistes-en-lait.png"
    },
    "bento": {
        "overline": "ERP Traiteur",
        "heading": "L'ERP conçu pour les traiteurs",
        "sub": "Événements, fiches techniques, coûts et conformité",
        "cards": [
            {"icon": "calendar", "color": "blue", "bg_icon": "fire", "title": "Gestion des événements multiples", "desc": "Planning événementiel intégré : visualisez tous vos événements, évitez les conflits et anticipez vos besoins en personnel et matières premières.", "checks": ["Planning multi-événements", "Anticipation des besoins par événement", "Gestion du personnel et des prestataires"], "link": "/prometheus/agroalimentaire/traiteur/", "link_text": "Découvrir l'ERP traiteur"},
            {"icon": "box", "color": "amber", "title": "Achats et stocks événementiels", "desc": "Stocks avec alertes DLC, suivi des matières sensibles et liens directs avec vos besoins selon les événements prévus.", "link": "/prometheus/agroalimentaire/traiteur/"},
            {"icon": "dollar", "color": "emerald", "title": "Coûts et marges par événement", "desc": "Calcul automatique du coût matière et de la marge nette par événement. Visualisez immédiatement la rentabilité de chaque prestation.", "link": "/prometheus/agroalimentaire/traiteur/"},
            {"icon": "shield", "color": "red", "title": "Traçabilité et conformité HACCP", "desc": "Chaque lot tracé, chaque DLC contrôlée. Documents sanitaires générés automatiquement pour un contrôle qualité irréprochable.", "link": "/prometheus/agroalimentaire/traiteur/"},
            {"icon": "doc", "color": "purple", "title": "Devis et fiches techniques", "desc": "Créez des devis détaillés par événement avec fiches techniques intégrées. Chiffrez vos prestations en quelques minutes avec marges garanties."},
        ]
    },
    "faq": {
        "overline": "FAQ Traiteur",
        "heading": "Questions sur l'ERP traiteur",
        "sub": "Gérez vos événements comme un pro.",
        "items": [
            {"icon": "fire", "q": "Pourquoi un ERP spécialisé traiteur est-il indispensable ?", "meta": "Événements, fiches techniques, DLC", "html": "<h3>Les défis uniques du métier de traiteur</h3><p>Un traiteur jongle entre <strong>plusieurs événements simultanés</strong>, chacun avec ses contraintes propres : menu personnalisé, allergènes spécifiques, timing de production serré, logistique de livraison.</p><p>Un ERP généraliste ne gère pas ces spécificités. Hello Harel a été conçu avec des traiteurs pour répondre à chaque aspect du métier.</p>"},
            {"icon": "dollar", "q": "Peut-on suivre la rentabilité de chaque événement ?", "meta": "Coût matière, marge, analyse", "html": "<h3>Rentabilité par prestation</h3><p>Oui. Pour chaque événement, l'ERP calcule : coût matière (sur base des fiches techniques), coût de personnel, frais logistiques, et marge nette résultante. Vous savez avant même l'événement si la prestation est rentable.</p>"},
            {"icon": "shield", "q": "Comment gérer les allergènes et la conformité HACCP ?", "meta": "Allergènes, traçabilité, contrôles", "html": "<h3>Allergènes et HACCP intégrés</h3><p>Chaque recette contient la liste des allergènes calculée automatiquement à partir des ingrédients. En cas de modification d'ingrédient, la liste est recalculée. Les fiches HACCP (températures, nettoyage, traçabilité) sont générées automatiquement.</p>"},
            {"icon": "chart", "q": "Combien de temps pour être opérationnel ?", "meta": "Déploiement, formation, migration", "html": "<h3>3 à 5 jours pour démarrer</h3><p>Import de vos recettes et fiches techniques, paramétrage de vos événements types, formation de votre équipe en 2h. Vous êtes opérationnel en moins d'une semaine, sans intégrateur.</p>"},
        ]
    }
}

# ── MARAÎCHER ──
P_MARAICHER = {
    "id": 2824, "slug": "maraicher", "name": "ERP Fruits et Légumes", "metier_slug": "fruits-legumes",
    "hero": {
        "badge": "ERP Fruits & Légumes",
        "title_w": "Gérez votre production,",
        "title_a": "vos prix et vos flux saisonniers",
        "desc": "Fraîcheur, traçabilité, variations de prix et contraintes sanitaires : notre ERP fruits et légumes centralise et optimise toutes vos opérations de la récolte au client.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2025/07/Logiciel-de-grossistes-alimentaire-4.png"
    },
    "bento": {
        "overline": "ERP Maraîcher",
        "heading": "L'ERP conçu pour les fruits et légumes",
        "sub": "Prix du jour, traçabilité parcelle, certificats phytosanitaires",
        "cards": [
            {"icon": "search", "color": "emerald", "bg_icon": "leaf", "title": "Traçabilité de la récolte au client", "desc": "Chaque lot tracé depuis la parcelle ou le fournisseur jusqu'au client final. Origine, calibre, variété : tout est enregistré.", "checks": ["Traçabilité par parcelle et fournisseur", "Calibres, variétés et origines", "Rappel produit en quelques secondes"], "link": "/prometheus/agroalimentaire/maraicher/", "link_text": "Découvrir l'ERP maraîcher"},
            {"icon": "tag", "color": "amber", "title": "Prix saisonniers en temps réel", "desc": "Les prix changent chaque jour. L'ERP met à jour vos tarifs selon le marché pour protéger vos marges automatiquement.", "link": "/prometheus/agroalimentaire/maraicher/"},
            {"icon": "doc", "color": "blue", "title": "Certificats phytosanitaires", "desc": "Génération automatique des certificats phytosanitaires exigés par vos clients ou pour l'export. Gain de temps précieux.", "link": "/prometheus/agroalimentaire/maraicher/"},
            {"icon": "clipboard", "color": "indigo", "title": "Préparation des commandes", "desc": "Conditionnements multiples (au poids, à la pièce, au colis) et chargements optimisés selon vos tournées de livraison.", "link": "/prometheus/agroalimentaire/maraicher/"},
            {"icon": "leaf", "color": "purple", "title": "Agréages et contrôle qualité", "desc": "Enregistrez les agréages à réception (calibre, maturité, aspect visuel). Refusez les lots non conformes et tracez les litiges fournisseurs."},
        ]
    },
    "faq": {
        "overline": "FAQ Maraîcher",
        "heading": "Questions sur l'ERP fruits et légumes",
        "sub": "Gérez la saisonnalité et la fraîcheur.",
        "items": [
            {"icon": "leaf", "q": "Comment l'ERP gère-t-il les prix qui changent chaque jour ?", "meta": "Cours du jour, marges, mise à jour auto", "html": "<h3>Tarification dynamique</h3><p>L'ERP permet de mettre à jour vos tarifs quotidiennement en quelques clics. Les prix d'achat sont enregistrés lot par lot, et la marge est recalculée en temps réel sur chaque vente.</p><p>Vous pouvez également définir des <strong>règles de marge minimum</strong> : si le prix d'achat du jour rend une vente non rentable, l'ERP vous alerte.</p>"},
            {"icon": "doc", "q": "L'ERP génère-t-il les certificats phytosanitaires ?", "meta": "Export, documents obligatoires", "html": "<h3>Documents phytosanitaires automatiques</h3><p>Oui. L'ERP génère automatiquement les certificats phytosanitaires à partir des données du lot (origine, variété, traitements). Les documents sont conformes aux exigences françaises et européennes pour l'export.</p>"},
            {"icon": "box", "q": "Comment gérer les conditionnements multiples ?", "meta": "Au poids, à la pièce, au colis", "html": "<h3>Flexibilité de conditionnement</h3><p>Hello Harel gère nativement le multi-conditionnement : un même produit peut être vendu <strong>au kilo</strong>, <strong>à la pièce</strong>, <strong>au colis</strong> ou <strong>à la palette</strong>. Les conversions sont automatiques et les stocks mis à jour en conséquence.</p>"},
            {"icon": "truck", "q": "Le module gère-t-il les tournées de livraison ?", "meta": "Tournées, créneaux, Rungis", "html": "<h3>Tournées optimisées</h3><p>Oui. Le module logistique planifie vos tournées en tenant compte des créneaux clients (Rungis, marchés, restaurateurs). Les bons de livraison sont générés automatiquement dans l'ordre de la tournée.</p>"},
        ]
    }
}

# ── BOULANGER ──
P_BOULANGER = {
    "id": 3309, "slug": "boulanger", "name": "ERP Boulangerie Pâtisserie", "metier_slug": "boulanger",
    "hero": {
        "badge": "ERP Boulangerie",
        "title_w": "Pilotez vos fournées,",
        "title_a": "maîtrisez vos coûts",
        "desc": "Entre matières premières sensibles, cycles de production complexes et qualité constante, seul un ERP boulangerie-pâtisserie vous donne la maîtrise que vous méritez.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2025/10/ERP-logiciel-pour-les-grossistes-en-cremerie.png"
    },
    "bento": {
        "overline": "ERP Boulangerie",
        "heading": "L'ERP conçu pour la boulangerie-pâtisserie",
        "sub": "Fournées, recettes, coûts de revient, multi-boutiques",
        "cards": [
            {"icon": "dollar", "color": "amber", "bg_icon": "bread", "title": "Coût de revient par recette", "desc": "Calcul du coût matière et de la marge nette pour chaque produit : baguette, croissant, entremets. Rentabilité exacte, même sur les recettes complexes.", "checks": ["Coût matière par recette", "Marge nette par produit fini", "Impact des variations de prix matières"], "link": "/prometheus/agroalimentaire/boulanger/", "link_text": "Découvrir l'ERP boulangerie"},
            {"icon": "calendar", "color": "blue", "title": "Planification des fournées", "desc": "Planifiez vos fournées selon les ventes prévisionnelles. Évitez le gaspillage et optimisez vos heures de main-d'œuvre.", "link": "/prometheus/agroalimentaire/boulanger/"},
            {"icon": "thermo", "color": "red", "title": "Stocks sensibles (beurre, œufs...)", "desc": "DLC surveillées, conditions de stockage contrôlées, alertes en cas d'anomalie. Vos matières premières sensibles sont maîtrisées.", "link": "/prometheus/agroalimentaire/boulanger/"},
            {"icon": "warehouse", "color": "indigo", "title": "Multi-points de vente", "desc": "Synchronisez production, stocks et ventes entre vos boutiques. Vision consolidée de votre entreprise en un clic.", "link": "/prometheus/agroalimentaire/boulanger/"},
            {"icon": "shield", "color": "purple", "title": "Traçabilité sanitaire complète", "desc": "Chaque lot tracé : fournisseur, numéro de lot, date de réception. Registres sanitaires générés automatiquement pour les contrôles."},
        ]
    },
    "faq": {
        "overline": "FAQ Boulangerie",
        "heading": "Questions sur l'ERP boulangerie-pâtisserie",
        "sub": "Industrialisez votre production sans perdre en qualité.",
        "items": [
            {"icon": "bread", "q": "Comment l'ERP optimise-t-il la production de fournées ?", "meta": "Planification, prévisions, gaspillage", "html": "<h3>Planification intelligente des fournées</h3><p>L'ERP analyse vos historiques de ventes et vos commandes en cours pour proposer un <strong>plan de production optimal</strong>. Vous produisez ce qui se vend, pas plus, pas moins.</p><p>Résultat mesuré : <strong>-25% de gaspillage</strong> en moyenne chez nos clients boulangers.</p>"},
            {"icon": "dollar", "q": "Le calcul du coût de revient est-il fiable ?", "meta": "Matières, rendements, recettes complexes", "html": "<h3>Coût de revient au centime</h3><p>L'ERP intègre le prix réel de chaque matière première (beurre AOP, farine T65, chocolat Valrhona...), les rendements de cuisson (perte de poids), et les temps de main-d'œuvre. Pour un croissant, vous connaissez le coût exact de chaque ingrédient.</p>"},
            {"icon": "warehouse", "q": "Peut-on gérer plusieurs boutiques ?", "meta": "Multi-sites, stocks, dispatch", "html": "<h3>Gestion multi-boutiques native</h3><p>Oui. Le labo central produit et dispatche vers les boutiques. Chaque boutique gère ses stocks et ses ventes indépendamment, avec consolidation au niveau central. Les transferts inter-sites sont tracés lot par lot.</p>"},
            {"icon": "shield", "q": "L'ERP gère-t-il la traçabilité HACCP ?", "meta": "Lots, températures, registres", "html": "<h3>HACCP numérique intégré</h3><p>Enregistrement des températures, traçabilité des lots (fournisseur → lot → recette → client), plans de nettoyage. Tout est archivé numériquement et exportable en cas de contrôle sanitaire.</p>"},
        ]
    }
}

# ── CHARCUTIER ──
P_CHARCUTIER = {
    "id": 2818, "slug": "charcutier", "name": "ERP Charcutier", "metier_slug": "charcutier",
    "hero": {
        "badge": "ERP Charcutier",
        "title_w": "Gérez vos lots, assurez",
        "title_a": "votre traçabilité",
        "desc": "Qualité, sécurité alimentaire, DLC courtes, normes sanitaires strictes : seul un ERP charcutier vous garantit une gestion irréprochable et des marges protégées.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2025/07/Logiciel-de-gestion-des-achats-3.png"
    },
    "bento": {
        "overline": "ERP Charcutier",
        "heading": "L'ERP conçu pour la charcuterie",
        "sub": "Traçabilité vétérinaire, rendements matière, DLC courtes",
        "cards": [
            {"icon": "search", "color": "red", "bg_icon": "knife", "title": "Traçabilité vétérinaire", "desc": "Chaque lot tracé depuis la matière première jusqu'au produit fini : numéros vétérinaires, dates d'abattage, poids, températures.", "checks": ["Numéros vétérinaires par lot", "Dates d'abattage et températures", "Historique complet pour l'administration"], "link": "/prometheus/agroalimentaire/charcutier/", "link_text": "Découvrir l'ERP charcutier"},
            {"icon": "clock", "color": "amber", "title": "DLC courtes et températures", "desc": "Alertes automatiques quand des lots approchent de la péremption (3 à 15 jours de DLC). Surveillance des températures intégrée.", "link": "/prometheus/agroalimentaire/charcutier/"},
            {"icon": "dollar", "color": "emerald", "title": "Coûts de revient et rendements", "desc": "Coût matière et marge nette sur chaque recette. Prise en compte du poids après cuisson, pertes au tranchage et coûts d'emballage.", "link": "/prometheus/agroalimentaire/charcutier/"},
            {"icon": "shield", "color": "blue", "title": "Conformité HACCP", "desc": "Registres sanitaires complets, enregistrements des températures, traçabilité pour les contrôles DGCCRF. Documentation toujours à jour.", "link": "/prometheus/agroalimentaire/charcutier/"},
            {"icon": "tag", "color": "purple", "title": "Promotions sur lots proches DLC", "desc": "Lancez des promotions ciblées sur les produits proches de leur DLC. Étiquettes spécifiques imprimées, impact commercial suivi en temps réel."},
        ]
    },
    "faq": {
        "overline": "FAQ Charcutier",
        "heading": "Questions sur l'ERP charcutier",
        "sub": "Maîtrisez votre traçabilité et vos rendements.",
        "items": [
            {"icon": "knife", "q": "L'ERP peut-il calculer mes pertes après cuisson ?", "meta": "Freintes, rendements, poids", "html": "<h3>Rendements matière intégrés</h3><p>Oui. L'ERP intègre les <strong>coefficients de rendement</strong> par type de produit : perte au désossage (15-25%), perte à la cuisson (10-20%), perte au tranchage (3-5%). Le coût de revient du produit fini tient compte de toutes ces pertes.</p>"},
            {"icon": "tag", "q": "Peut-on lancer des promotions sur produits proches DLC ?", "meta": "DLC courtes, démarque, étiquettes", "html": "<h3>Promotions ciblées anti-gaspillage</h3><p>L'ERP identifie automatiquement les lots approchant de leur DLC et propose des actions : <strong>promotion flash</strong>, <strong>transfert vers un autre site</strong>, <strong>transformation en produit fini</strong>. Les étiquettes promotionnelles sont générées en un clic.</p>"},
            {"icon": "doc", "q": "L'ERP gère-t-il les étiquettes obligatoires ?", "meta": "INCO, allergènes, composition", "html": "<h3>Étiquetage conforme automatique</h3><p>Oui. L'ERP génère les étiquettes conformes à la réglementation INCO : liste des ingrédients, allergènes en gras, valeurs nutritionnelles, numéro de lot, DLC, conditions de conservation.</p>"},
            {"icon": "shield", "q": "Comment éviter un rappel produit total ?", "meta": "Traçabilité précise, lots ciblés", "html": "<h3>Rappel ciblé grâce à la traçabilité</h3><p>Grâce à la traçabilité lot par lot, un rappel se limite aux <strong>lots réellement concernés</strong>, pas à toute la production. Vous identifiez en quelques secondes quels clients ont reçu quel lot, et lancez un rappel ciblé.</p>"},
        ]
    }
}

# ── INDUSTRIE LAITIÈRE ──
P_LAITIER = {
    "id": 5470, "slug": "industrie-laitiere", "name": "ERP Industrie Laitière", "metier_slug": "laitier",
    "hero": {
        "badge": "ERP Laitier",
        "title_w": "Maîtrisez vos marges et",
        "title_a": "vos stocks en temps réel",
        "desc": "Collecte de lait, paiement à la qualité, traçabilité des lots : découvrez comment un ERP pour l'industrie laitière centralise vos données et transforme vos process.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2025/10/ERP-logiciel-pour-les-grossistes-en-lait.png"
    },
    "bento": {
        "overline": "ERP Laitier",
        "heading": "L'ERP conçu pour l'industrie laitière",
        "sub": "Collecte, affinage, paiement qualité, traçabilité",
        "cards": [
            {"icon": "gear", "color": "blue", "bg_icon": "bottle", "title": "Production : recettes et affinage", "desc": "Pilotez les process de transformation, d'affinage et de conditionnement. Qualité constante et coûts maîtrisés pour votre laiterie ou fromagerie.", "checks": ["Fiches recettes multi-niveaux", "Suivi des cycles d'affinage", "Calcul du rendement fromager"], "link": "/prometheus/agroalimentaire/industrie-laitiere/", "link_text": "Découvrir l'ERP laitier"},
            {"icon": "shield", "color": "emerald", "title": "Traçabilité et qualité", "desc": "Traçabilité sans faille du lait collecté au produit fini. Audits et contrôles sanitaires ne paralysent plus votre activité.", "link": "/prometheus/agroalimentaire/industrie-laitiere/"},
            {"icon": "dollar", "color": "amber", "title": "Paiement à la qualité", "desc": "Automatisez le paiement du lait selon les critères de qualité : taux de matière grasse, protéines, cellules. Transparent pour vos producteurs.", "link": "/prometheus/agroalimentaire/industrie-laitiere/"},
            {"icon": "thermo", "color": "red", "title": "Chaîne du froid et DLC", "desc": "Gestion des DLC/DLUO pour les produits frais. Surveillance des températures de stockage avec alertes automatiques.", "link": "/prometheus/agroalimentaire/industrie-laitiere/"},
            {"icon": "truck", "color": "purple", "title": "Collecte et logistique laitière", "desc": "Planifiez vos tournées de collecte, enregistrez les volumes et qualités par producteur. Optimisez vos itinéraires et réduisez vos coûts de transport."},
        ]
    },
    "faq": {
        "overline": "FAQ Laitier",
        "heading": "Questions sur l'ERP industrie laitière",
        "sub": "De la collecte à la distribution.",
        "items": [
            {"icon": "dollar", "q": "Comment l'ERP gère-t-il le paiement du lait à la qualité ?", "meta": "MG, protéines, cellules, barèmes", "html": "<h3>Paiement automatisé et transparent</h3><p>L'ERP intègre les barèmes de paiement selon les analyses : <strong>taux de matière grasse</strong>, <strong>protéines</strong>, <strong>cellules somatiques</strong>, <strong>germes</strong>. Le calcul est automatique et le relevé de paiement est généré pour chaque producteur.</p>"},
            {"icon": "search", "q": "La traçabilité d'un lot de fromage est-elle assurée ?", "meta": "Lait collecté → transformation → client", "html": "<h3>Traçabilité laitière complète</h3><p>Du lait collecté au fromage livré, chaque étape est tracée : <strong>producteur</strong>, <strong>tank de collecte</strong>, <strong>cuve de fabrication</strong>, <strong>lot d'affinage</strong>, <strong>conditionnement</strong>, <strong>expédition</strong>. En cas de rappel, l'origine est identifiée en quelques secondes.</p>"},
            {"icon": "thermo", "q": "Le logiciel gère-t-il la DLC des produits frais ?", "meta": "Yaourts, fromages frais, crèmes", "html": "<h3>Gestion native des DLC courtes</h3><p>L'ERP gère les DLC courtes des produits laitiers frais avec FIFO automatique, alertes de péremption et blocage des expéditions sur lots dépassés. Idéal pour les yaourts, fromages frais et crèmes.</p>"},
            {"icon": "gear", "q": "Peut-on piloter les cycles d'affinage ?", "meta": "Caves, durée, retournements, soins", "html": "<h3>Module d'affinage intégré</h3><p>Oui. L'ERP suit chaque lot en cave d'affinage : <strong>durée</strong>, <strong>retournements</strong>, <strong>soins</strong> (lavage, brossage), <strong>conditions climatiques</strong> (température, hygrométrie). Vous savez exactement quand chaque lot sera prêt à la commercialisation.</p>"},
        ]
    }
}

# ── PLATS CUISINÉS INDUSTRIELS ──
P_PLATS = {
    "id": 5477, "slug": "plats-cuisines-industriels", "name": "ERP Plats Cuisinés", "metier_slug": "plats-cuisines",
    "hero": {
        "badge": "ERP Plats Cuisinés",
        "title_w": "Maîtrisez vos recettes,",
        "title_a": "vos coûts et votre conformité",
        "desc": "PRI (Prix de Revient Industriel), allergènes INCO, planification GMS : découvrez comment un ERP pour plats cuisinés structure votre activité et protège vos marges.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2025/07/Logiciel-de-gestion-des-achats-1.png"
    },
    "bento": {
        "overline": "ERP Plats Cuisinés",
        "heading": "L'ERP conçu pour les plats cuisinés industriels",
        "sub": "PRI, allergènes INCO, planning GMS, recettes multi-niveaux",
        "cards": [
            {"icon": "gear", "color": "blue", "bg_icon": "plate", "title": "Recettes multi-niveaux et PRI", "desc": "Gérez des recettes arborescentes avec sous-recettes. Le Prix de Revient Industriel est calculé automatiquement avec une précision au centime.", "checks": ["Nomenclatures multi-niveaux illimitées", "PRI recalculé en temps réel", "Impact des substitutions de matières"], "link": "/prometheus/agroalimentaire/plats-cuisines-industriels/", "link_text": "Découvrir l'ERP plats cuisinés"},
            {"icon": "calendar", "color": "amber", "title": "Planning de production GMS", "desc": "Anticipez les commandes GMS (volumes, promotions, DLC courtes). Planifiez votre production en fonction des délais serrés de la grande distribution.", "link": "/prometheus/agroalimentaire/plats-cuisines-industriels/"},
            {"icon": "shield", "color": "red", "title": "Conformité INCO et allergènes", "desc": "Gestion des allergènes dès la fiche matière première. À chaque modification de recette, la liste est recalculée automatiquement.", "link": "/prometheus/agroalimentaire/plats-cuisines-industriels/"},
            {"icon": "search", "color": "emerald", "title": "Traçabilité industrielle", "desc": "Traçabilité de chaque lot du fournisseur au client final. Documentation complète pour les audits GMS et les contrôles sanitaires.", "link": "/prometheus/agroalimentaire/plats-cuisines-industriels/"},
            {"icon": "doc", "color": "purple", "title": "Étiquetage et valeurs nutritionnelles", "desc": "Génération automatique des étiquettes conformes : liste d'ingrédients, allergènes en gras, valeurs nutritionnelles calculées, numéro de lot, DLC."},
        ]
    },
    "faq": {
        "overline": "FAQ Plats Cuisinés",
        "heading": "Questions sur l'ERP plats cuisinés",
        "sub": "Industrialisez vos recettes en toute conformité.",
        "items": [
            {"icon": "dollar", "q": "Comment l'ERP calcule-t-il le Prix de Revient Industriel (PRI) ?", "meta": "Matières, MO, énergie, rendements", "html": "<h3>Calcul du PRI automatisé</h3><p>L'ERP décompose le PRI en :</p><ul><li><strong>Matières premières</strong> — Au coût d'achat réel du lot utilisé</li><li><strong>Main-d'œuvre directe</strong> — Temps par opération × coût horaire</li><li><strong>Énergie</strong> — Consommation par recette (cuisson, refroidissement)</li><li><strong>Emballage</strong> — Coût unitaire par conditionnement</li><li><strong>Rendements</strong> — Pertes de cuisson, évaporation, chutes</li></ul><p>Le PRI est recalculé à chaque réception de matière première.</p>"},
            {"icon": "gear", "q": "Le logiciel gère-t-il les substitutions de matières ?", "meta": "Recettes alternatives, impact prix", "html": "<h3>Substitutions avec recalcul automatique</h3><p>Oui. Quand une matière première n'est pas disponible, vous pouvez définir des <strong>matières de substitution</strong> avec leurs coefficients d'équivalence. Le PRI et la liste des allergènes sont recalculés automatiquement.</p>"},
            {"icon": "shield", "q": "Comment l'ERP automatise-t-il la déclaration des allergènes INCO ?", "meta": "14 allergènes, recalcul, étiquettes", "html": "<h3>Allergènes INCO automatisés</h3><p>Chaque matière première est renseignée avec ses <strong>14 allergènes réglementaires</strong>. Quand vous composez une recette, l'ERP agrège automatiquement tous les allergènes présents. En cas de changement de fournisseur ou d'ingrédient, la liste est mise à jour instantanément.</p>"},
            {"icon": "calendar", "q": "Comment gérer les commandes GMS à DLC courte ?", "meta": "Planning, délais, promotions", "html": "<h3>Planning GMS intégré</h3><p>L'ERP gère les contraintes spécifiques de la GMS :</p><ul><li><strong>Commandes à J-1 ou J-2</strong> — Planification automatique de la production</li><li><strong>Promotions</strong> — Volumes exceptionnels anticipés</li><li><strong>DLC minimale exigée</strong> — Contrôle automatique à l'expédition</li><li><strong>EDI</strong> — Réception des commandes et envoi des avis d'expédition</li></ul>"},
        ]
    }
}

# ── MEDICAL (parent page) ──
P_MEDICAL = {
    "id": 6022, "slug": "medical", "name": "ERP Médical", "silo": "medical",
    "hero": {
        "badge": "ERP Médical",
        "title_w": "Simplifiez votre gestion,",
        "title_a": "soignez votre logistique",
        "desc": "Harel Medical est l'ERP conçu exclusivement pour les grossistes, distributeurs et importateurs du secteur médical. Centralisez vos stocks, assurez la traçabilité, optimisez vos ventes B2B.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2023/08/bg-line-v7.png"
    },
    "bento": {
        "overline": "Modules ERP Médical",
        "heading": "Toutes les fonctionnalités pour le médical",
        "sub": "Un ERP complet qui couvre l'intégralité de votre chaîne de valeur médicale",
        "cards": [
            {"icon": "search", "color": "blue", "bg_icon": "shield", "title": "Gestion des stocks & Traçabilité", "desc": "Le cœur de votre métier. Suivez chaque produit du fournisseur au patient. Numéros de série, gestion des lots, conformité FIFO/FEFO.", "checks": ["Numéros de série et lots", "Blocage auto des lots périmés", "Historique complet pour rappels produit"], "link": "/prometheus/medical/dispositifs-medicaux/", "link_text": "Découvrir la traçabilité"},
            {"icon": "truck", "color": "emerald", "title": "Logistique & Supply Chain", "desc": "Optimisez vos expéditions multi-entrepôts, gérez les envois prioritaires et la chaîne du froid pour les produits sensibles.", "link": "/prometheus/medical/dispositifs-medicaux/"},
            {"icon": "cart", "color": "amber", "title": "Achats & Approvisionnement", "desc": "Automatisez vos commandes fournisseurs, suivez les certificats CE et les validations réglementaires à l'import.", "link": "/prometheus/medical/dispositifs-medicaux/"},
            {"icon": "clipboard", "color": "indigo", "title": "Inventaire en temps réel", "desc": "Inventaire permanent ou tournant via PDA et scan mobile. Lecture code-barres, QR codes et Datamatrix UDI.", "link": "/prometheus/medical/dispositifs-medicaux/"},
            {"icon": "dollar", "color": "red", "title": "Gestion Tarifaire B2B complexe", "desc": "Gérez les grilles tarifaires spécifiques aux marchés publics, remises hospitalières, contrats-cadre et tarifs LPP/LPPR."}
        ]
    },
    "faq": {
        "overline": "FAQ Médical",
        "heading": "Questions sur l'ERP médical",
        "sub": "Conformité, traçabilité et distribution médicale.",
        "items": [
            {"icon": "shield", "q": "L'ERP est-il conforme aux exigences de l'ANSM ?", "meta": "Réglementation, audits, traçabilité", "html": "<h3>Conformité ANSM intégrée</h3><p>Oui. L'ERP intègre nativement les exigences de l'ANSM en matière de <strong>traçabilité des dispositifs médicaux</strong>. Chaque lot, chaque numéro de série est tracé du fournisseur au client final. Les registres sont exportables pour les audits ISO 13485.</p>"},
            {"icon": "search", "q": "Comment fonctionne la traçabilité UDI ?", "meta": "Codes UDI, Datamatrix, EUDAMED", "html": "<h3>Traçabilité UDI native</h3><p>L'ERP lit et enregistre les <strong>codes UDI (Unique Device Identification)</strong> via scan Datamatrix. Chaque produit est lié à son UDI-DI et UDI-PI, conformément au règlement MDR 2017/745. Les données sont prêtes pour déclaration EUDAMED.</p>"},
            {"icon": "clock", "q": "Quel est le délai de déploiement ?", "meta": "Migration, formation, go-live", "html": "<h3>Déploiement en 2 à 4 semaines</h3><p>Notre process éprouvé permet un déploiement rapide :</p><ul><li><strong>Semaine 1</strong> — Audit et cadrage de vos besoins</li><li><strong>Semaine 2</strong> — Migration des données et paramétrage</li><li><strong>Semaine 3</strong> — Formation des équipes</li><li><strong>Semaine 4</strong> — Go-live avec support dédié</li></ul>"},
            {"icon": "database", "q": "Les données sont-elles hébergées en HDS ?", "meta": "Hébergement, sécurité, RGPD", "html": "<h3>Hébergement HDS certifié</h3><p>Oui. Toutes vos données sont hébergées sur des serveurs <strong>certifiés HDS (Hébergeur de Données de Santé)</strong> en France. Conformité totale au RGPD. Sauvegardes quotidiennes, chiffrement AES-256, et PRA garantissant une disponibilité de 99,9%.</p>"}
        ]
    }
}

# ── DISPOSITIFS MÉDICAUX ──
P_DISPOSITIFS = {
    "id": 6023, "slug": "dispositifs-medicaux", "name": "ERP Dispositifs Médicaux", "silo": "medical",
    "hero": {
        "badge": "ERP Dispositifs Médicaux",
        "title_w": "DMI, codes UDI et",
        "title_a": "conformité MDR",
        "desc": "Grossistes et importateurs de dispositifs médicaux : gérez vos stocks par numéro de série, assurez la traçabilité UDI et restez conformes au règlement MDR 2017/745 sans effort.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2023/08/bg-line-v7.png"
    },
    "bento": {
        "overline": "ERP Dispositifs Médicaux",
        "heading": "L'ERP conçu pour les dispositifs médicaux",
        "sub": "UDI, MDR, ANSM, numéros de série, rappels produit",
        "cards": [
            {"icon": "search", "color": "blue", "bg_icon": "shield", "title": "Traçabilité UDI complète", "desc": "Chaque dispositif tracé par son UDI-DI et UDI-PI. Scan Datamatrix natif, conformité EUDAMED et historique complet pour les rappels.", "checks": ["Scan UDI Datamatrix natif", "Traçabilité du fournisseur au patient", "Rappel ciblé par numéro de série"], "link": "/prometheus/medical/dispositifs-medicaux/", "link_text": "Découvrir l'ERP DMI"},
            {"icon": "shield", "color": "emerald", "title": "Conformité MDR & ANSM", "desc": "Registres réglementaires pré-formatés, suivi des certificats CE, alertes d'expiration. Documentation prête pour les audits ISO 13485.", "link": "/prometheus/medical/dispositifs-medicaux/"},
            {"icon": "box", "color": "amber", "title": "Gestion par numéro de série", "desc": "Chaque DMI est identifié individuellement. Suivi du cycle de vie complet : réception, stockage, expédition, implantation, retour.", "link": "/prometheus/medical/dispositifs-medicaux/"},
            {"icon": "truck", "color": "indigo", "title": "Logistique prioritaire", "desc": "Gestion des expéditions urgentes pour les blocs opératoires. Suivi temps réel, conditions de transport et preuve de livraison.", "link": "/prometheus/medical/dispositifs-medicaux/"},
            {"icon": "bell", "color": "red", "title": "Alertes et rappels produit", "desc": "En cas de rappel, identifiez en secondes tous les clients ayant reçu le lot ou le numéro de série concerné. Notifications automatiques."}
        ]
    },
    "faq": {
        "overline": "FAQ Dispositifs Médicaux",
        "heading": "Questions sur l'ERP dispositifs médicaux",
        "sub": "UDI, traçabilité, conformité réglementaire.",
        "items": [
            {"icon": "shield", "q": "L'ERP gère-t-il la conformité MDR 2017/745 ?", "meta": "Règlement européen, UDI, EUDAMED", "html": "<h3>Conformité MDR native</h3><p>Oui. L'ERP intègre les exigences du <strong>règlement MDR 2017/745</strong> : enregistrement UDI obligatoire, traçabilité post-market, documentation technique et vigilance. Les données sont formatées pour déclaration EUDAMED.</p>"},
            {"icon": "search", "q": "Comment fonctionne le scan UDI Datamatrix ?", "meta": "PDA, scan mobile, identification", "html": "<h3>Scan UDI en un geste</h3><p>L'ERP lit les <strong>codes Datamatrix GS1</strong> via PDA ou smartphone. Le scan décode automatiquement : référence produit (UDI-DI), numéro de série/lot (UDI-PI), date de péremption et date de fabrication. Zéro saisie manuelle.</p>"},
            {"icon": "bell", "q": "Comment gérer un rappel de dispositif médical ?", "meta": "Traçabilité, lots, notifications", "html": "<h3>Rappel ciblé instantané</h3><p>En cas d'alerte ANSM, l'ERP identifie en quelques secondes <strong>tous les clients ayant reçu le produit concerné</strong> (par lot ou par numéro de série). Les notifications de rappel sont générées automatiquement avec les instructions de retour.</p>"},
            {"icon": "doc", "q": "L'ERP génère-t-il les documents pour les audits ISO 13485 ?", "meta": "Registres, certificats, documentation", "html": "<h3>Documentation audit-ready</h3><p>L'ERP génère et archive tous les documents requis : <strong>registres de traçabilité</strong>, <strong>certificats CE fournisseurs</strong>, <strong>fiches de données de sécurité</strong>, <strong>rapports de vigilance</strong>. Export PDF et CSV pour les auditeurs.</p>"}
        ]
    }
}

# ── LABORATOIRES ──
P_LABORATOIRES = {
    "id": 6024, "slug": "laboratoires", "name": "ERP Laboratoires", "silo": "medical",
    "hero": {
        "badge": "ERP Laboratoires",
        "title_w": "Réactifs, chaîne du froid",
        "title_a": "et diagnostic in vitro",
        "desc": "Distributeurs de réactifs et consommables de laboratoire : maîtrisez la chaîne du froid, gérez les DLC courtes et assurez la traçabilité lot par lot de vos produits DIV.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2023/08/bg-line-v7.png"
    },
    "bento": {
        "overline": "ERP Laboratoires",
        "heading": "L'ERP conçu pour les laboratoires",
        "sub": "Réactifs, chaîne du froid, DIV, traçabilité",
        "cards": [
            {"icon": "thermo", "color": "blue", "bg_icon": "shield", "title": "Chaîne du froid maîtrisée", "desc": "Suivi des températures de stockage et transport. Alertes automatiques en cas de rupture. Historique complet pour les audits qualité.", "checks": ["Monitoring température en continu", "Alertes rupture chaîne du froid", "Historique pour audits qualité"], "link": "/prometheus/medical/laboratoires/", "link_text": "Découvrir l'ERP labo"},
            {"icon": "clock", "color": "amber", "title": "Gestion des DLC/DLUO", "desc": "FIFO/FEFO automatique pour les réactifs à durée de vie courte. Blocage des lots périmés et alertes de péremption configurables.", "link": "/prometheus/medical/laboratoires/"},
            {"icon": "search", "color": "emerald", "title": "Traçabilité lot par lot", "desc": "Chaque réactif tracé du fournisseur au laboratoire client. Numéro de lot, date de fabrication, conditions de conservation.", "link": "/prometheus/medical/laboratoires/"},
            {"icon": "doc", "color": "indigo", "title": "Fiches de données de sécurité", "desc": "Gestion centralisée des FDS, fiches techniques et certificats d'analyse. Accès instantané pour vos clients et les autorités.", "link": "/prometheus/medical/laboratoires/"},
            {"icon": "shield", "color": "red", "title": "Conformité DIV & IVDR", "desc": "Documentation conforme au règlement IVDR 2017/746 pour les dispositifs de diagnostic in vitro. Registres pré-formatés pour l'ANSM."}
        ]
    },
    "faq": {
        "overline": "FAQ Laboratoires",
        "heading": "Questions sur l'ERP laboratoires",
        "sub": "Réactifs, chaîne du froid, conformité DIV.",
        "items": [
            {"icon": "thermo", "q": "L'ERP gère-t-il la chaîne du froid des réactifs ?", "meta": "Température, monitoring, alertes", "html": "<h3>Chaîne du froid intégrée</h3><p>Oui. L'ERP enregistre les <strong>conditions de température</strong> à chaque étape : réception, stockage, préparation, expédition. Les capteurs IoT compatibles permettent un monitoring en temps réel avec alertes SMS/email en cas d'écart.</p>"},
            {"icon": "clock", "q": "Comment gérer les réactifs à DLC courte ?", "meta": "FEFO, péremption, rotation", "html": "<h3>Rotation FEFO automatique</h3><p>L'ERP applique automatiquement la règle <strong>FEFO (First Expired, First Out)</strong>. Les réactifs proches de leur date de péremption sont proposés en priorité. Les lots périmés sont bloqués automatiquement et ne peuvent pas être expédiés.</p>"},
            {"icon": "shield", "q": "L'ERP est-il conforme au règlement IVDR ?", "meta": "DIV, IVDR 2017/746, ANSM", "html": "<h3>Conformité IVDR native</h3><p>L'ERP intègre les exigences du <strong>règlement IVDR 2017/746</strong> pour les dispositifs de diagnostic in vitro : classification des produits, traçabilité renforcée, documentation technique et déclaration de conformité.</p>"},
            {"icon": "database", "q": "Peut-on gérer les certificats d'analyse par lot ?", "meta": "Certificats, FDS, documentation", "html": "<h3>Gestion documentaire par lot</h3><p>Chaque lot peut être associé à ses <strong>certificats d'analyse</strong>, <strong>fiches de données de sécurité</strong> et <strong>fiches techniques</strong>. Les documents sont accessibles en un clic et transmissibles automatiquement aux clients avec les bons de livraison.</p>"}
        ]
    }
}

# ── MATÉRIEL DENTAIRE ──
P_DENTAIRE = {
    "id": 6025, "slug": "materiel-dentaire", "name": "ERP Matériel Dentaire", "silo": "medical",
    "hero": {
        "badge": "ERP Matériel Dentaire",
        "title_w": "Consommables, catalogues XXL",
        "title_a": "et tarifs cabinet",
        "desc": "Distributeurs de matériel et consommables dentaires : gérez des catalogues de milliers de références, des tarifs spécifiques par cabinet et une logistique de livraison quotidienne.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2023/08/bg-line-v7.png"
    },
    "bento": {
        "overline": "ERP Matériel Dentaire",
        "heading": "L'ERP conçu pour le matériel dentaire",
        "sub": "Catalogues XXL, tarifs cabinet, livraison quotidienne",
        "cards": [
            {"icon": "database", "color": "blue", "bg_icon": "shield", "title": "Catalogue de milliers de références", "desc": "Gérez des catalogues de 10 000 à 50 000 références avec recherche instantanée, photos, fiches techniques et codes fabricant.", "checks": ["Recherche multi-critères instantanée", "Photos et fiches techniques", "Import automatique catalogues fournisseurs"], "link": "/prometheus/medical/materiel-dentaire/", "link_text": "Découvrir l'ERP dentaire"},
            {"icon": "tag", "color": "amber", "title": "Tarification par cabinet", "desc": "Grilles tarifaires personnalisées par cabinet dentaire, groupements d'achat et centrales. Remises en cascade et promotions automatiques.", "link": "/prometheus/medical/materiel-dentaire/"},
            {"icon": "truck", "color": "emerald", "title": "Livraison quotidienne", "desc": "Tournées de livraison optimisées pour les cabinets dentaires. Préparation des commandes par tournée avec scan et validation.", "link": "/prometheus/medical/materiel-dentaire/"},
            {"icon": "cart", "color": "indigo", "title": "Commande en ligne B2B", "desc": "Portail de commande en ligne pour vos cabinets clients. Historique, favoris, réassort automatique et suivi de livraison.", "link": "/prometheus/medical/materiel-dentaire/"},
            {"icon": "chart", "color": "red", "title": "Statistiques commerciales", "desc": "Analyse des ventes par cabinet, par gamme de produit et par commercial. Identifiez les opportunités de cross-selling et upselling."}
        ]
    },
    "faq": {
        "overline": "FAQ Matériel Dentaire",
        "heading": "Questions sur l'ERP matériel dentaire",
        "sub": "Catalogues, tarifs et logistique dentaire.",
        "items": [
            {"icon": "database", "q": "L'ERP peut-il gérer un catalogue de 50 000 références ?", "meta": "Performance, recherche, import", "html": "<h3>Catalogues XXL sans ralentissement</h3><p>Oui. L'ERP est optimisé pour gérer des <strong>catalogues de plusieurs dizaines de milliers de références</strong>. La recherche est instantanée grâce à l'indexation multi-critères : désignation, code fabricant, code EAN, famille de produit.</p>"},
            {"icon": "tag", "q": "Comment gérer les tarifs spécifiques par cabinet ?", "meta": "Remises, groupements, centrales", "html": "<h3>Tarification multi-niveaux</h3><p>L'ERP gère des <strong>grilles tarifaires illimitées</strong> : tarif par cabinet, par groupement d'achat, par centrale. Les remises peuvent être en cascade (remise + remise), par palier de quantité, ou par période promotionnelle.</p>"},
            {"icon": "truck", "q": "Le module gère-t-il les tournées quotidiennes ?", "meta": "Tournées, préparation, livraison", "html": "<h3>Tournées optimisées</h3><p>Oui. Le module logistique planifie les tournées par zone géographique, prépare les commandes dans l'ordre de la tournée et génère les bons de livraison. Le livreur valide chaque livraison sur tablette avec signature client.</p>"},
            {"icon": "cart", "q": "Les cabinets peuvent-ils commander en ligne ?", "meta": "Portail B2B, historique, favoris", "html": "<h3>Portail B2B intégré</h3><p>Le portail de commande en ligne permet à vos cabinets de <strong>passer commande 24h/24</strong>, consulter leur historique, créer des listes de favoris et suivre leurs livraisons. Les commandes sont intégrées automatiquement dans l'ERP.</p>"}
        ]
    }
}

# ── MAINTIEN À DOMICILE ──
P_DOMICILE = {
    "id": 6026, "slug": "maintien-a-domicile", "name": "ERP Maintien à Domicile", "silo": "medical",
    "hero": {
        "badge": "ERP Maintien à Domicile",
        "title_w": "Location, LPPR",
        "title_a": "et tournées patients",
        "desc": "Prestataires de santé à domicile : gérez la location de matériel médical, les prescriptions LPPR, les tournées techniciens et le suivi patient en toute conformité.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2023/08/bg-line-v7.png"
    },
    "bento": {
        "overline": "ERP Maintien à Domicile",
        "heading": "L'ERP conçu pour le maintien à domicile",
        "sub": "Location, LPPR, tournées techniciens, suivi patient",
        "cards": [
            {"icon": "clipboard", "color": "blue", "bg_icon": "shield", "title": "Gestion de la location", "desc": "Parc de matériel en location : lits médicalisés, fauteuils, oxygénothérapie. Suivi des contrats, des renouvellements et de la facturation CPAM.", "checks": ["Suivi du parc matériel", "Contrats et renouvellements auto", "Facturation CPAM / mutuelle"], "link": "/prometheus/medical/maintien-a-domicile/", "link_text": "Découvrir l'ERP MAD"},
            {"icon": "doc", "color": "amber", "title": "Prescriptions LPPR", "desc": "Gestion des prescriptions médicales, codes LPPR et télétransmission aux organismes payeurs. Conformité totale avec l'Assurance Maladie.", "link": "/prometheus/medical/maintien-a-domicile/"},
            {"icon": "truck", "color": "emerald", "title": "Tournées techniciens", "desc": "Planification des installations, maintenances et récupérations chez les patients. Optimisation des itinéraires et suivi GPS.", "link": "/prometheus/medical/maintien-a-domicile/"},
            {"icon": "users", "color": "indigo", "title": "Dossier patient", "desc": "Fiche patient complète : prescriptions, matériel installé, historique des interventions, coordonnées du médecin prescripteur.", "link": "/prometheus/medical/maintien-a-domicile/"},
            {"icon": "gear", "color": "red", "title": "Maintenance préventive", "desc": "Calendrier de maintenance du matériel en location. Alertes automatiques pour les contrôles techniques obligatoires et les révisions."}
        ]
    },
    "faq": {
        "overline": "FAQ Maintien à Domicile",
        "heading": "Questions sur l'ERP maintien à domicile",
        "sub": "Location, LPPR, patients et tournées.",
        "items": [
            {"icon": "doc", "q": "L'ERP gère-t-il la facturation CPAM et mutuelles ?", "meta": "Télétransmission, LPPR, remboursement", "html": "<h3>Facturation tiers-payant intégrée</h3><p>Oui. L'ERP gère la <strong>facturation en tiers-payant</strong> : part CPAM et part mutuelle. Les flux de télétransmission sont conformes aux normes de l'Assurance Maladie. Le suivi des remboursements est automatisé.</p>"},
            {"icon": "clipboard", "q": "Comment suivre le parc de matériel en location ?", "meta": "Contrats, inventaire, amortissement", "html": "<h3>Gestion de parc complète</h3><p>Chaque appareil est identifié par son <strong>numéro de série</strong> et suivi tout au long de son cycle de vie : achat, mise en location, maintenance, retour, reconditionnement ou mise au rebut. L'amortissement est calculé automatiquement.</p>"},
            {"icon": "truck", "q": "Le module gère-t-il les tournées des techniciens ?", "meta": "Planification, GPS, interventions", "html": "<h3>Tournées optimisées</h3><p>Le module planifie les interventions (installation, maintenance, récupération) par zone géographique. Le technicien accède à sa tournée sur tablette avec <strong>itinéraire optimisé</strong>, fiche patient et historique du matériel. Le rapport d'intervention est signé sur place.</p>"},
            {"icon": "users", "q": "Peut-on gérer le dossier patient dans l'ERP ?", "meta": "Prescriptions, historique, médecin", "html": "<h3>Dossier patient centralisé</h3><p>Chaque patient dispose d'une fiche complète : <strong>coordonnées</strong>, <strong>médecin prescripteur</strong>, <strong>prescriptions en cours</strong>, <strong>matériel installé</strong>, <strong>historique des interventions</strong>. Les données sont hébergées en HDS conformément à la réglementation.</p>"}
        ]
    }
}

# ── HYGIÈNE PROFESSIONNELLE ──
P_HYGIENE = {
    "id": 6027, "slug": "hygiene-professionnelle", "name": "ERP Hygiène Professionnelle", "silo": "medical",
    "hero": {
        "badge": "ERP Hygiène Professionnelle",
        "title_w": "Gros volumes, biocides",
        "title_a": "et cadenciers clients",
        "desc": "Distributeurs de produits d'hygiène et de désinfection professionnelle : gérez les gros volumes, la réglementation biocide et les cadenciers de livraison automatique.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2023/08/bg-line-v7.png"
    },
    "bento": {
        "overline": "ERP Hygiène Professionnelle",
        "heading": "L'ERP conçu pour l'hygiène professionnelle",
        "sub": "Gros volumes, biocides, cadenciers, multi-conditionnement",
        "cards": [
            {"icon": "box", "color": "blue", "bg_icon": "shield", "title": "Gestion des gros volumes", "desc": "Palettes, rolls, conteneurs : gérez les unités logistiques adaptées aux gros volumes. Conversion automatique entre unités de vente et unités de stockage.", "checks": ["Multi-conditionnement natif", "Conversion UVC/colis/palette auto", "Seuils de réapprovisionnement intelligents"], "link": "/prometheus/medical/hygiene-professionnelle/", "link_text": "Découvrir l'ERP hygiène"},
            {"icon": "shield", "color": "emerald", "title": "Réglementation biocide", "desc": "Suivi des autorisations de mise sur le marché (AMM), fiches de données de sécurité et étiquetage CLP pour les produits biocides.", "link": "/prometheus/medical/hygiene-professionnelle/"},
            {"icon": "calendar", "color": "amber", "title": "Cadenciers de livraison", "desc": "Programmez les livraisons récurrentes pour vos clients (hôpitaux, EHPAD, cliniques). Fréquence, quantités et jours fixes configurables.", "link": "/prometheus/medical/hygiene-professionnelle/"},
            {"icon": "warehouse", "color": "indigo", "title": "Multi-entrepôts", "desc": "Gérez plusieurs dépôts régionaux avec stocks consolidés. Transferts inter-sites optimisés et réapprovisionnement automatique.", "link": "/prometheus/medical/hygiene-professionnelle/"},
            {"icon": "chart", "color": "red", "title": "Analyses de consommation", "desc": "Suivez les consommations de vos clients par famille de produit. Détectez les variations anormales et proposez des réassorts proactifs."}
        ]
    },
    "faq": {
        "overline": "FAQ Hygiène Professionnelle",
        "heading": "Questions sur l'ERP hygiène professionnelle",
        "sub": "Volumes, biocides, cadenciers et conformité.",
        "items": [
            {"icon": "shield", "q": "L'ERP gère-t-il la réglementation biocide ?", "meta": "AMM, FDS, CLP, étiquetage", "html": "<h3>Conformité biocide intégrée</h3><p>Oui. L'ERP associe à chaque produit biocide son <strong>numéro d'AMM</strong>, sa <strong>fiche de données de sécurité</strong> et ses <strong>pictogrammes CLP</strong>. Les documents réglementaires sont transmis automatiquement avec les bons de livraison.</p>"},
            {"icon": "calendar", "q": "Comment fonctionnent les cadenciers automatiques ?", "meta": "Livraisons récurrentes, fréquence", "html": "<h3>Cadenciers configurables</h3><p>Pour chaque client, définissez un <strong>programme de livraison récurrent</strong> : produits, quantités, fréquence (hebdomadaire, bimensuelle, mensuelle) et jour de livraison. L'ERP génère automatiquement les commandes et les intègre au planning logistique.</p>"},
            {"icon": "box", "q": "L'ERP gère-t-il le multi-conditionnement ?", "meta": "UVC, colis, palette, conversion", "html": "<h3>Multi-conditionnement natif</h3><p>Un même produit peut être vendu à <strong>l'unité, au colis, à la palette</strong>. Les conversions sont automatiques : si un client commande 500 unités et qu'un colis en contient 24, l'ERP calcule 20 colis + 20 unités. Les stocks sont mis à jour en conséquence.</p>"},
            {"icon": "warehouse", "q": "Peut-on gérer plusieurs dépôts régionaux ?", "meta": "Multi-sites, transferts, consolidation", "html": "<h3>Multi-entrepôts centralisé</h3><p>L'ERP gère un nombre illimité de dépôts avec <strong>vision consolidée des stocks</strong>. Les transferts inter-sites sont tracés lot par lot. Le réapprovisionnement des dépôts régionaux depuis le dépôt central est automatisé selon les seuils configurés.</p>"}
        ]
    }
}

# ── NÉGOCE (parent page) ──
P_NEGOCE = {
    "id": 6248, "slug": "negoce", "name": "ERP Négoce",
    "hero": {
        "badge": "ERP Négoce",
        "title_w": "Maîtrisez vos marges,",
        "title_a": "pilotez votre négoce",
        "desc": "Harel Négoce est l'ERP conçu pour les grossistes, distributeurs B2B et négociants. Gérez vos achats, vos ventes multicanal, votre logistique et vos tarifs complexes depuis une plateforme unique.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2023/08/bg-line-v7.png"
    },
    "bento": {
        "overline": "Modules ERP Négoce",
        "heading": "Toutes les fonctionnalités pour le négoce",
        "sub": "Un ERP complet qui couvre l'intégralité de votre chaîne de distribution B2B",
        "cards": [
            {"icon": "warehouse", "color": "blue", "bg_icon": "box", "title": "Stock multi-entrepôts", "desc": "Gérez vos stocks en temps réel sur plusieurs dépôts. Transferts inter-sites, réapprovisionnement automatique et inventaire permanent par scan.", "checks": ["Vision consolidée multi-dépôts", "Seuils de réassort automatiques", "Inventaire tournant par PDA"], "link": "/prometheus/negoce/materiaux-construction/", "link_text": "Découvrir le négoce matériaux"},
            {"icon": "cart", "color": "emerald", "title": "Gestion commerciale B2B", "desc": "Devis, commandes, bons de livraison et facturation automatisés. Gérez vos conditions commerciales par client, groupe ou contrat-cadre.", "link": "/prometheus/negoce/boissons/", "link_text": "Découvrir le négoce boissons"},
            {"icon": "tag", "color": "amber", "title": "Tarification complexe", "desc": "Grilles tarifaires multi-niveaux, remises en cascade, prix par quantité, promotions temporaires et tarifs contractuels. Chaque client voit son prix juste.", "link": "/prometheus/negoce/alimentaire/", "link_text": "Découvrir le négoce alimentaire"},
            {"icon": "truck", "color": "indigo", "title": "Logistique & tournées", "desc": "Planifiez vos tournées de livraison, optimisez le chargement des camions et suivez les expéditions en temps réel avec preuve de livraison.", "link": "/prometheus/negoce/international/", "link_text": "Découvrir le négoce international"},
            {"icon": "clipboard", "color": "purple", "title": "Achats & approvisionnement", "desc": "Centralisez vos achats fournisseurs, comparez les offres, automatisez les commandes récurrentes et suivez les réceptions lot par lot.", "link": "/prometheus/negoce/industriel/", "link_text": "Découvrir le négoce industriel"}
        ]
    },
    "faq": {
        "overline": "FAQ Négoce",
        "heading": "Questions sur l'ERP négoce",
        "sub": "Distribution B2B, marges, logistique et tarification.",
        "items": [
            {"icon": "search", "q": "Qu'est-ce qu'un ERP négoce et à qui s'adresse-t-il ?", "meta": "Grossiste, distributeur, commerce de gros", "html": "<h3>L'ERP pensé pour le négoce</h3><p>Un <strong>ERP négoce</strong> est un logiciel de gestion intégré conçu spécifiquement pour les activités de <strong>commerce de gros et distribution B2B</strong>. Il s'adresse aux :</p><ul><li><strong>Grossistes</strong> — négoce matériaux, boissons, alimentaire, fournitures industrielles</li><li><strong>Distributeurs B2B</strong> — multi-marques, multi-fournisseurs</li><li><strong>Importateurs-exportateurs</strong> — commerce international, multi-devises</li></ul><p>Contrairement à un ERP généraliste, l'ERP négoce intègre nativement la gestion des <strong>tarifs complexes</strong>, des <strong>conditionnements multiples</strong> et de la <strong>logistique de distribution</strong>.</p>"},
            {"icon": "chart", "q": "En quoi un ERP négoce diffère-t-il d'un ERP généraliste ?", "meta": "Spécificités, tarification, logistique", "html": "<h3>Des fonctions métier que les ERP généralistes n'ont pas</h3><p>Un ERP généraliste gère la comptabilité et la facturation de base. Un <strong>ERP négoce</strong> ajoute des fonctionnalités critiques :</p><ul><li><strong>Tarification multi-niveaux</strong> — prix par client, par volume, par contrat, remises en cascade</li><li><strong>Multi-conditionnement</strong> — vente à l'unité, au colis, à la palette avec conversion automatique</li><li><strong>Logistique intégrée</strong> — tournées de livraison, chargement camion, preuve de livraison</li><li><strong>Marge en temps réel</strong> — chaque ligne de commande affiche la marge réelle sur coût d'achat</li></ul>"},
            {"icon": "clock", "q": "Combien de temps pour déployer un ERP négoce ?", "meta": "Délai, migration, formation", "html": "<h3>Opérationnel en 2 à 4 semaines</h3><p>Notre processus de déploiement est rodé pour les entreprises de négoce :</p><ul><li><strong>Semaine 1</strong> — Audit de vos flux (achats, ventes, stocks, logistique)</li><li><strong>Semaine 2</strong> — Import de vos données : catalogue produits, clients, tarifs, stocks</li><li><strong>Semaine 3</strong> — Paramétrage des workflows et formation des équipes</li><li><strong>Semaine 4</strong> — Go-live avec accompagnement dédié</li></ul><p>La migration de vos données historiques (clients, tarifs, stocks) est incluse dans l'accompagnement.</p>"},
            {"icon": "link", "q": "Quelles intégrations sont disponibles ?", "meta": "Comptabilité, e-commerce, EDI, transporteurs", "html": "<h3>Connecté à tout votre écosystème</h3><p>L'ERP négoce Hello Harel s'intègre nativement avec :</p><ul><li><strong>Comptabilité</strong> — Export écritures vers Sage, Cegid, ACD, EBP</li><li><strong>E-commerce B2B</strong> — Synchronisation catalogue, stocks et commandes</li><li><strong>EDI</strong> — Échanges normalisés avec la grande distribution et les centrales d'achat</li><li><strong>Transporteurs</strong> — Connexion aux API des transporteurs pour suivi colis</li></ul><p>Notre API REST ouverte permet de connecter tout outil tiers en quelques heures.</p>"}
        ]
    }
}

# ── NÉGOCE MATÉRIAUX DE CONSTRUCTION ──
P_NEGOCE_MATERIAUX = {
    "id": 6249, "slug": "materiaux-construction", "name": "ERP Négoce Matériaux",
    "hero": {
        "badge": "ERP Négoce Matériaux",
        "title_w": "Des milliers de références,",
        "title_a": "une logistique maîtrisée",
        "desc": "Négoce de matériaux de construction, quincaillerie, sanitaire, chauffage, plomberie ou électrique : gérez votre catalogue massif, vos entrepôts régionaux et vos livraisons chantier depuis un ERP unique.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2023/08/bg-line-v7.png"
    },
    "bento": {
        "overline": "ERP Négoce Matériaux",
        "heading": "L'ERP conçu pour le négoce de matériaux",
        "sub": "BTP, quincaillerie, sanitaire, chauffage, plomberie, électrique",
        "cards": [
            {"icon": "database", "color": "blue", "bg_icon": "box", "title": "Catalogue BTP massif", "desc": "Gérez des dizaines de milliers de références avec attributs techniques : dimensions, poids, conditionnement, classe de résistance. Recherche multicritère instantanée.", "checks": ["Fiches produit avec attributs techniques", "Recherche par dimension et caractéristique", "Gestion des équivalences fournisseurs"], "link": "/prometheus/negoce/", "link_text": "Découvrir l'ERP négoce"},
            {"icon": "box", "color": "emerald", "title": "Gestion des conditionnements", "desc": "Vente à l'unité, au lot, au mètre linéaire, à la palette ou au camion complet. Conversions automatiques entre unités de vente et unités de stock.", "link": "/prometheus/negoce/"},
            {"icon": "truck", "color": "amber", "title": "Logistique chantier", "desc": "Planifiez les livraisons sur chantier avec contraintes d'accès, grue de déchargement et créneau horaire. Suivi des bons de livraison signés sur tablette.", "link": "/prometheus/negoce/"},
            {"icon": "dollar", "color": "indigo", "title": "Tarification marchés publics", "desc": "Gérez les appels d'offres publics, les bordereaux de prix unitaires et les révisions tarifaires contractuelles pour les marchés de travaux.", "link": "/prometheus/negoce/"},
            {"icon": "warehouse", "color": "purple", "title": "Multi-entrepôts régionaux", "desc": "Pilotez vos agences et dépôts régionaux avec vision consolidée. Transferts inter-sites, réassort automatique et picking optimisé par emplacement."}
        ]
    },
    "faq": {
        "overline": "FAQ Négoce Matériaux",
        "heading": "Questions sur l'ERP négoce matériaux de construction",
        "sub": "Catalogue, logistique chantier, marchés publics et multi-agences.",
        "items": [
            {"icon": "database", "q": "Comment gérer un catalogue de plusieurs dizaines de milliers de références ?", "meta": "Attributs techniques, recherche, familles", "html": "<h3>Un catalogue structuré et performant</h3><p>L'ERP structure votre catalogue par <strong>familles, sous-familles et attributs techniques</strong> (dimensions, poids, matière, norme). La recherche multicritère permet de retrouver un produit en quelques secondes parmi 50 000+ références.</p><p>Les <strong>équivalences fournisseurs</strong> sont gérées nativement : un même produit peut avoir plusieurs références selon le fournisseur, avec correspondance automatique.</p>"},
            {"icon": "truck", "q": "L'ERP gère-t-il les livraisons sur chantier ?", "meta": "Contraintes, accès, grue, créneaux", "html": "<h3>Logistique chantier intégrée</h3><p>Oui. Pour chaque livraison chantier, vous renseignez les <strong>contraintes d'accès</strong> (tonnage, hauteur, grue nécessaire), le <strong>créneau horaire</strong> et le <strong>contact sur site</strong>. Le chauffeur reçoit toutes les informations sur son terminal embarqué.</p><p>Le bon de livraison est signé sur tablette directement sur le chantier, avec horodatage et géolocalisation.</p>"},
            {"icon": "dollar", "q": "Comment gérer les tarifs pour les marchés publics ?", "meta": "Appels d'offres, BPU, révision de prix", "html": "<h3>Marchés publics et BPU</h3><p>L'ERP gère les <strong>bordereaux de prix unitaires (BPU)</strong> par marché. Pour chaque appel d'offres, vous créez une grille tarifaire dédiée avec :</p><ul><li><strong>Prix unitaires contractuels</strong> par référence</li><li><strong>Formules de révision</strong> indexées (BT, TP, index INSEE)</li><li><strong>Plafonds et seuils</strong> de déclenchement des avenants</li></ul><p>Les factures sont générées conformément aux exigences des marchés publics (Chorus Pro compatible).</p>"},
            {"icon": "warehouse", "q": "Comment piloter un réseau de plusieurs agences ?", "meta": "Multi-sites, consolidation, transferts", "html": "<h3>Gestion multi-agences centralisée</h3><p>L'ERP offre une <strong>vision consolidée de tous vos dépôts</strong> tout en permettant une gestion autonome par agence. Chaque site gère ses stocks, ses commandes et ses livraisons, avec consolidation en temps réel au siège.</p><p>Les <strong>transferts inter-sites</strong> sont tracés et optimisés : quand une agence manque d'un produit, le système identifie le dépôt le plus proche disposant du stock.</p>"}
        ]
    }
}

# ── NÉGOCE BOISSONS ──
P_NEGOCE_BOISSONS = {
    "id": 6250, "slug": "boissons", "name": "ERP Négoce Boissons",
    "hero": {
        "badge": "ERP Négoce Boissons",
        "title_w": "Consignes, accises et DRM",
        "title_a": "enfin maîtrisés",
        "desc": "Grossistes en vins, spiritueux, bières et soft drinks : gérez les consignes, les droits d'accise, la DRM et vos tournées CHR depuis un ERP pensé pour la distribution de boissons.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2023/08/bg-line-v7.png"
    },
    "bento": {
        "overline": "ERP Négoce Boissons",
        "heading": "L'ERP conçu pour le négoce de boissons",
        "sub": "Vins, spiritueux, bières, soft drinks, consignes et accises",
        "cards": [
            {"icon": "arrows", "color": "blue", "bg_icon": "bottle", "title": "Gestion des consignes", "desc": "Suivez les emballages consignés (fûts, casiers, palettes) par client. Facturation et avoir automatiques, suivi du parc consigné en temps réel.", "checks": ["Suivi du parc consigné par client", "Facturation et avoir automatiques", "Alerte consignes non retournées"], "link": "/prometheus/negoce/", "link_text": "Découvrir l'ERP négoce"},
            {"icon": "doc", "color": "emerald", "title": "Accises & DRM", "desc": "Calcul automatique des droits d'accise par catégorie fiscale. Génération de la DRM (Déclaration Récapitulative Mensuelle) et des DAE/DSA en quelques clics.", "link": "/prometheus/negoce/"},
            {"icon": "search", "color": "amber", "title": "Traçabilité lots & DLC", "desc": "Chaque lot est tracé de la réception à la livraison. Gestion FEFO des dates de consommation, alertes automatiques sur les produits proches de la DLC.", "link": "/prometheus/negoce/"},
            {"icon": "truck", "color": "indigo", "title": "Tournées de livraison CHR", "desc": "Planifiez vos tournées pour les cafés, hôtels et restaurants. Optimisation des itinéraires, chargement par ordre de livraison et preuve de remise.", "link": "/prometheus/negoce/"},
            {"icon": "list", "color": "purple", "title": "Catalogue multi-conditionnement", "desc": "Un même produit vendu à la bouteille, au pack, au carton ou à la palette. Conversions automatiques, codes-barres multiples et prix par conditionnement."}
        ]
    },
    "faq": {
        "overline": "FAQ Négoce Boissons",
        "heading": "Questions sur l'ERP négoce boissons",
        "sub": "Consignes, accises, tournées CHR et traçabilité.",
        "items": [
            {"icon": "arrows", "q": "Comment l'ERP gère-t-il les consignes de boissons ?", "meta": "Fûts, casiers, palettes, suivi du parc", "html": "<h3>Gestion complète du circuit consigné</h3><p>L'ERP suit chaque <strong>emballage consigné</strong> (fûts, casiers, palettes) par client. À chaque livraison, les consignes déposées et reprises sont enregistrées automatiquement.</p><ul><li><strong>Parc consigné par client</strong> — Nombre de fûts, casiers et palettes en circulation</li><li><strong>Facturation automatique</strong> — Avoir à la reprise, facturation si non-retour après délai</li><li><strong>Alertes</strong> — Notification quand un client dépasse son quota de consignes non retournées</li></ul>"},
            {"icon": "doc", "q": "L'ERP calcule-t-il les droits d'accise automatiquement ?", "meta": "DRM, DAE, DSA, catégories fiscales", "html": "<h3>Accises et DRM automatisées</h3><p>Oui. L'ERP associe à chaque produit sa <strong>catégorie fiscale</strong> (vin tranquille, vin effervescent, bière, spiritueux, produit intermédiaire). Les droits d'accise sont calculés automatiquement à chaque mouvement de stock.</p><p>La <strong>DRM (Déclaration Récapitulative Mensuelle)</strong> est générée en un clic à partir des mouvements du mois. Les <strong>DAE (Documents d'Accompagnement Électroniques)</strong> sont émis via EMCS/GAMMA.</p>"},
            {"icon": "truck", "q": "Comment optimiser les tournées de livraison CHR ?", "meta": "Cafés, hôtels, restaurants, itinéraires", "html": "<h3>Tournées CHR optimisées</h3><p>L'ERP planifie vos <strong>tournées de livraison CHR</strong> en tenant compte des contraintes de chaque établissement : jours de réception, créneaux horaires, accès véhicule.</p><p>Le système propose un <strong>itinéraire optimisé</strong> et un <strong>ordre de chargement inversé</strong> (le dernier client livré est chargé en premier). Le livreur valide chaque livraison sur son terminal avec signature et photo.</p>"},
            {"icon": "thermo", "q": "L'ERP gère-t-il la chaîne du froid pour les boissons ?", "meta": "Température, bières, transport frigorifique", "html": "<h3>Suivi de la chaîne du froid</h3><p>Pour les produits nécessitant une <strong>température contrôlée</strong> (bières artisanales, certains vins), l'ERP identifie les références à livrer en véhicule frigorifique et alerte si un produit sensible est affecté à un véhicule non réfrigéré.</p><p>Les <strong>relevés de température</strong> peuvent être associés aux bons de livraison pour garantir la traçabilité de la chaîne du froid.</p>"}
        ]
    }
}

# ── NÉGOCE ALIMENTAIRE ──
P_NEGOCE_ALIMENTAIRE = {
    "id": 6251, "slug": "alimentaire", "name": "ERP Négoce Alimentaire",
    "hero": {
        "badge": "ERP Négoce Alimentaire",
        "title_w": "Traçabilité, DLC et HACCP",
        "title_a": "au cœur de votre distribution",
        "desc": "Grossistes en produits frais, surgelés, épicerie et produits secs : maîtrisez la traçabilité alimentaire, les DLC, la logistique multi-température et la conformité HACCP avec un ERP dédié.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2023/08/bg-line-v7.png"
    },
    "bento": {
        "overline": "ERP Négoce Alimentaire",
        "heading": "L'ERP conçu pour la distribution alimentaire",
        "sub": "Produits frais, surgelés, épicerie, traçabilité et HACCP",
        "cards": [
            {"icon": "search", "color": "blue", "bg_icon": "leaf", "title": "Traçabilité alimentaire", "desc": "Traçabilité ascendante et descendante de chaque lot, du fournisseur au client final. Conformité au règlement européen 178/2002 et rappels produit instantanés.", "checks": ["Traçabilité lot par lot complète", "Rappel ciblé en quelques secondes", "Conformité règlement CE 178/2002"], "link": "/prometheus/negoce/", "link_text": "Découvrir l'ERP négoce"},
            {"icon": "clock", "color": "emerald", "title": "DLC/DLUO automatisées", "desc": "Gestion FEFO automatique : les produits les plus proches de la DLC sortent en priorité. Alertes sur les lots à date courte, décote automatique et gestion des dons.", "link": "/prometheus/negoce/"},
            {"icon": "thermo", "color": "amber", "title": "Multi-température", "desc": "Gérez vos zones de stockage par température (ambiant, frais, surgelé) et planifiez les livraisons en véhicule multi-compartiment avec respect de la chaîne du froid.", "link": "/prometheus/negoce/"},
            {"icon": "chart", "color": "indigo", "title": "Gestion des marges produit", "desc": "Calculez vos marges en temps réel par produit, par client et par commande. Intégrez les coûts de transport, de stockage et les pertes (casse, DLC dépassée).", "link": "/prometheus/negoce/"},
            {"icon": "shield", "color": "purple", "title": "Conformité HACCP", "desc": "Enregistrez vos points de contrôle critique, relevés de température et actions correctives. Documentation HACCP générée automatiquement pour les audits sanitaires."}
        ]
    },
    "faq": {
        "overline": "FAQ Négoce Alimentaire",
        "heading": "Questions sur l'ERP négoce alimentaire",
        "sub": "Traçabilité, DLC, logistique multi-température et EDI.",
        "items": [
            {"icon": "search", "q": "Quelles sont les obligations de traçabilité en négoce alimentaire ?", "meta": "Règlement CE 178/2002, lots, rappels", "html": "<h3>Traçabilité réglementaire intégrée</h3><p>Le <strong>règlement CE 178/2002</strong> impose à tout distributeur alimentaire une traçabilité « une étape en amont, une étape en aval ». L'ERP automatise cette obligation :</p><ul><li><strong>Réception</strong> — Chaque lot est enregistré avec son fournisseur, sa date de production et sa DLC</li><li><strong>Stockage</strong> — Suivi FEFO avec emplacement et température</li><li><strong>Expédition</strong> — Lien lot-client pour chaque livraison</li></ul><p>En cas de rappel, l'ERP identifie en quelques secondes tous les clients ayant reçu le lot concerné.</p>"},
            {"icon": "clock", "q": "Comment l'ERP gère-t-il les DLC et la rotation des stocks ?", "meta": "FEFO, alertes, décote, dons", "html": "<h3>Gestion FEFO automatisée</h3><p>L'ERP applique la règle <strong>FEFO (First Expired, First Out)</strong> : les produits les plus proches de la DLC sont proposés en priorité lors de la préparation de commande.</p><p>Des <strong>alertes automatiques</strong> vous préviennent quand un lot atteint un seuil de date configurable (ex. : J-7, J-3). Vous pouvez alors déclencher une <strong>décote automatique</strong>, un <strong>transfert vers un point de vente soldeur</strong> ou un <strong>don à une association</strong>.</p>"},
            {"icon": "thermo", "q": "L'ERP gère-t-il la logistique multi-température ?", "meta": "Froid positif, surgelé, ambiant, véhicules", "html": "<h3>Logistique multi-température native</h3><p>L'ERP distingue trois zones de température : <strong>ambiant</strong> (>15°C), <strong>froid positif</strong> (0-4°C) et <strong>surgelé</strong> (<-18°C). Chaque produit est associé à sa zone de stockage et de transport.</p><p>Lors de la planification des tournées, le système vérifie que le <strong>véhicule affecté dispose des compartiments nécessaires</strong>. Les relevés de température sont enregistrés et associés aux bons de livraison.</p>"},
            {"icon": "link", "q": "L'ERP est-il compatible avec l'EDI grande distribution ?", "meta": "GMS, centrales d'achat, DESADV, INVOIC", "html": "<h3>EDI natif pour la grande distribution</h3><p>L'ERP gère les flux EDI normalisés pour les échanges avec les <strong>centrales d'achat et enseignes GMS</strong> :</p><ul><li><strong>ORDERS</strong> — Réception automatique des commandes</li><li><strong>DESADV</strong> — Avis d'expédition avec SSCC palettes</li><li><strong>INVOIC</strong> — Factures dématérialisées conformes</li><li><strong>RECADV</strong> — Accusés de réception et gestion des litiges</li></ul><p>Les flux sont échangés via les principales plateformes EDI (SPS Commerce, Edifact, GS1 France).</p>"}
        ]
    }
}

# ── NÉGOCE INTERNATIONAL ──
P_NEGOCE_INTERNATIONAL = {
    "id": 6252, "slug": "international", "name": "ERP Négoce International",
    "hero": {
        "badge": "ERP Négoce International",
        "title_w": "Multi-devises, douanes",
        "title_a": "et supply chain mondiale",
        "desc": "Import-export, négoce multi-devises, incoterms et documents douaniers : pilotez vos opérations de commerce international depuis un ERP qui parle toutes les langues du négoce.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2023/08/bg-line-v7.png"
    },
    "bento": {
        "overline": "ERP Négoce International",
        "heading": "L'ERP conçu pour le négoce international",
        "sub": "Import-export, multi-devises, incoterms et conformité douanière",
        "cards": [
            {"icon": "globe", "color": "blue", "bg_icon": "arrows", "title": "Multi-devises temps réel", "desc": "Gérez vos achats et ventes dans toutes les devises. Taux de change mis à jour automatiquement, écarts de change calculés et comptabilisés en temps réel.", "checks": ["Taux de change automatiques (BCE)", "Écarts de change comptabilisés", "Facturation multi-devises native"], "link": "/prometheus/negoce/", "link_text": "Découvrir l'ERP négoce"},
            {"icon": "doc", "color": "emerald", "title": "Documents douaniers", "desc": "Générez vos DAU, factures pro forma, certificats d'origine, packing lists et lettres de crédit. Tous les documents nécessaires au dédouanement en quelques clics.", "link": "/prometheus/negoce/"},
            {"icon": "dollar", "color": "amber", "title": "Incoterms & frais d'approche", "desc": "Associez un incoterm à chaque transaction. Calculez le prix de revient réel en intégrant fret, assurance, droits de douane, taxes et frais de transitaire.", "link": "/prometheus/negoce/"},
            {"icon": "shield", "color": "indigo", "title": "Conformité réglementaire", "desc": "Vérification des embargos, screening des partenaires commerciaux, gestion des licences d'exportation et conformité aux réglementations sanitaires à l'import.", "link": "/prometheus/negoce/"},
            {"icon": "truck", "color": "purple", "title": "Supply chain internationale", "desc": "Suivez vos conteneurs du port d'embarquement au dépôt. Gérez les délais de transit, les documents de transport et les contrôles qualité à réception."}
        ]
    },
    "faq": {
        "overline": "FAQ Négoce International",
        "heading": "Questions sur l'ERP négoce international",
        "sub": "Multi-devises, douanes, prix de revient et conformité.",
        "items": [
            {"icon": "globe", "q": "Comment l'ERP gère-t-il les opérations multi-devises ?", "meta": "Taux de change, écarts, comptabilité", "html": "<h3>Gestion multi-devises complète</h3><p>L'ERP gère nativement les <strong>achats et ventes en devises étrangères</strong>. Les taux de change sont mis à jour automatiquement depuis la <strong>BCE (Banque Centrale Européenne)</strong>.</p><ul><li><strong>Commande fournisseur</strong> — Saisie en devise du fournisseur, conversion automatique en euros</li><li><strong>Écarts de change</strong> — Calculés et comptabilisés à chaque règlement</li><li><strong>Reporting</strong> — Analyse des marges en devise locale et en euros</li></ul><p>Vous pouvez figer un taux de change sur une commande pour vous protéger des fluctuations.</p>"},
            {"icon": "doc", "q": "Quels documents douaniers l'ERP génère-t-il ?", "meta": "DAU, certificat d'origine, packing list", "html": "<h3>Documents d'import-export automatisés</h3><p>L'ERP génère l'ensemble des documents nécessaires au <strong>dédouanement</strong> :</p><ul><li><strong>DAU (Document Administratif Unique)</strong> — Pré-rempli avec codes SH, valeurs et origines</li><li><strong>Facture pro forma</strong> — Pour l'ouverture des lettres de crédit</li><li><strong>Certificat d'origine</strong> — EUR.1, ATR, Form A selon la destination</li><li><strong>Packing list</strong> — Détail des colis, poids et dimensions</li></ul>"},
            {"icon": "dollar", "q": "Comment calculer le prix de revient réel à l'import ?", "meta": "Landed cost, fret, douane, approche", "html": "<h3>Calcul du prix de revient complet (landed cost)</h3><p>L'ERP intègre tous les <strong>frais d'approche</strong> pour calculer le coût de revient réel de chaque produit importé :</p><ul><li><strong>Prix d'achat FOB</strong> en devise d'origine</li><li><strong>Fret maritime ou aérien</strong> — Réparti au poids ou au volume</li><li><strong>Assurance transport</strong></li><li><strong>Droits de douane</strong> — Calculés selon le code SH et l'origine</li><li><strong>Frais de transitaire</strong>, manutention portuaire, transport local</li></ul><p>Le prix de revient est mis à jour en temps réel à chaque imputation de frais, vous permettant de connaître votre <strong>marge réelle</strong> avant même la réception.</p>"},
            {"icon": "shield", "q": "L'ERP vérifie-t-il la conformité des opérations internationales ?", "meta": "Embargos, licences, screening", "html": "<h3>Contrôles de conformité automatisés</h3><p>L'ERP intègre des <strong>contrôles de conformité</strong> à chaque opération internationale :</p><ul><li><strong>Screening des partenaires</strong> — Vérification contre les listes de sanctions (UE, OFAC, ONU)</li><li><strong>Contrôle des destinations</strong> — Alertes sur les pays sous embargo</li><li><strong>Licences d'exportation</strong> — Suivi des biens à double usage et des autorisations nécessaires</li></ul><p>Toutes les vérifications sont tracées et archivées pour les audits douaniers.</p>"}
        ]
    }
}

# ── NÉGOCE INDUSTRIEL ──
P_NEGOCE_INDUSTRIEL = {
    "id": 6253, "slug": "industriel", "name": "ERP Négoce Industriel",
    "hero": {
        "badge": "ERP Négoce Industriel",
        "title_w": "Références techniques,",
        "title_a": "distribution B2B maîtrisée",
        "desc": "Grossistes en fournitures industrielles, quincaillerie, EPI, outillage ou pièces détachées : gérez votre catalogue technique massif, vos tarifs contractuels et votre logistique B2B avec un ERP spécialisé.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2023/08/bg-line-v7.png"
    },
    "bento": {
        "overline": "ERP Négoce Industriel",
        "heading": "L'ERP conçu pour la distribution industrielle",
        "sub": "Fournitures industrielles, EPI, outillage, pièces détachées",
        "cards": [
            {"icon": "database", "color": "blue", "bg_icon": "gear", "title": "Catalogue technique massif", "desc": "Gérez des centaines de milliers de références avec caractéristiques techniques détaillées : normes, dimensions, matériaux, compatibilités. Recherche paramétrique instantanée.", "checks": ["Fiches techniques multi-attributs", "Recherche paramétrique avancée", "Import catalogue fournisseur automatisé"], "link": "/prometheus/negoce/", "link_text": "Découvrir l'ERP négoce"},
            {"icon": "arrows", "color": "emerald", "title": "Gestion des équivalences", "desc": "Identifiez automatiquement les produits équivalents entre fournisseurs. Proposez des alternatives en cas de rupture et optimisez vos achats par substitution.", "link": "/prometheus/negoce/"},
            {"icon": "tag", "color": "amber", "title": "Tarification contractuelle", "desc": "Gérez les contrats-cadre avec vos clients industriels : prix négociés par référence, remises par famille, accords annuels et révisions tarifaires automatiques.", "link": "/prometheus/negoce/"},
            {"icon": "cart", "color": "indigo", "title": "E-commerce B2B", "desc": "Proposez un portail de commande en ligne à vos clients professionnels. Catalogue personnalisé, tarifs contractuels et historique de commandes accessible 24h/24.", "link": "/prometheus/negoce/"},
            {"icon": "warehouse", "color": "purple", "title": "Multi-entrepôts & picking", "desc": "Optimisez votre préparation de commande avec picking par vague, par zone ou par client. Gestion des emplacements, réassort picking depuis le stock masse."}
        ]
    },
    "faq": {
        "overline": "FAQ Négoce Industriel",
        "heading": "Questions sur l'ERP négoce industriel",
        "sub": "Catalogue technique, équivalences, tarifs contractuels et e-commerce.",
        "items": [
            {"icon": "arrows", "q": "Comment l'ERP gère-t-il les équivalences produit ?", "meta": "Substitution, multi-fournisseur, alternatives", "html": "<h3>Gestion des équivalences et substitutions</h3><p>L'ERP permet d'associer à chaque référence ses <strong>produits équivalents</strong> chez d'autres fournisseurs. Lorsqu'un produit est en rupture, le système propose automatiquement les alternatives disponibles en stock.</p><ul><li><strong>Équivalences fournisseurs</strong> — Correspondance automatique entre références</li><li><strong>Substitution en commande</strong> — Proposition d'alternative avec accord client</li><li><strong>Optimisation achats</strong> — Achat de l'équivalent le moins cher disponible</li></ul>"},
            {"icon": "database", "q": "Comment gérer les caractéristiques techniques de milliers de produits ?", "meta": "Attributs, normes, recherche paramétrique", "html": "<h3>Catalogue technique structuré</h3><p>L'ERP structure votre catalogue avec des <strong>attributs techniques personnalisables</strong> par famille de produit : dimensions, matériaux, normes (ISO, DIN, NF), indices de protection (IP), classes de résistance.</p><p>La <strong>recherche paramétrique</strong> permet à vos commerciaux de trouver le bon produit en filtrant par caractéristiques : « vis inox M8x40 tête hexagonale classe 8.8 » en quelques clics.</p>"},
            {"icon": "tag", "q": "Comment fonctionnent les tarifs contractuels ?", "meta": "Contrats-cadre, prix négociés, révisions", "html": "<h3>Tarification B2B avancée</h3><p>L'ERP gère des <strong>contrats-cadre</strong> avec vos clients industriels. Chaque contrat peut définir :</p><ul><li><strong>Prix fixes</strong> par référence pour la durée du contrat</li><li><strong>Remises par famille</strong> — Pourcentage ou montant par catégorie de produit</li><li><strong>Paliers de volume</strong> — Prix dégressif selon les quantités commandées</li><li><strong>Révisions annuelles</strong> — Application automatique des indices de révision</li></ul><p>Lors de la saisie d'une commande, le système applique automatiquement les conditions du contrat en cours.</p>"},
            {"icon": "cart", "q": "L'ERP propose-t-il un portail e-commerce B2B ?", "meta": "Commande en ligne, catalogue, self-service", "html": "<h3>Portail de commande B2B intégré</h3><p>L'ERP propose un <strong>portail e-commerce B2B</strong> connecté en temps réel à votre gestion :</p><ul><li><strong>Catalogue personnalisé</strong> — Chaque client voit ses produits et ses prix contractuels</li><li><strong>Commande en ligne</strong> — Panier, historique, renouvellement de commande en 1 clic</li><li><strong>Stock en temps réel</strong> — Disponibilité affichée avec délai de livraison estimé</li><li><strong>Suivi de commande</strong> — Statut, tracking et factures téléchargeables</li></ul><p>Le portail est accessible 24h/24, permettant à vos clients de commander en dehors de vos heures d'ouverture.</p>"}
        ]
    }
}

# ── ALL NÉGOCE PAGES ──
PAGES_NEGOCE = [
    P_NEGOCE,
    P_NEGOCE_MATERIAUX,
    P_NEGOCE_BOISSONS,
    P_NEGOCE_ALIMENTAIRE,
    P_NEGOCE_INTERNATIONAL,
    P_NEGOCE_INDUSTRIEL,
]

# ── ALL PAGES LIST ──
PAGES = [
    P_FONCTIONNALITES,
    P_CRM,
    P_FACTURATION,
    P_VENTE,
    P_STOCK,
    P_FABRICATION,
    P_ACHAT,
    P_LOGISTIQUE,
    P_IMPORT_EXPORT,
    P_AGRO,
    P_TRAITEUR,
    P_MARAICHER,
    P_BOULANGER,
    P_CHARCUTIER,
    P_LAITIER,
    P_PLATS,
]

PAGES_MEDICAL = [
    P_MEDICAL,
    P_DISPOSITIFS,
    P_LABORATOIRES,
    P_DENTAIRE,
    P_DOMICILE,
    P_HYGIENE,
]

# ── NÉGOCE (page pilier) ──
P_NEGOCE = {
    "id": 0, "slug": "negoce", "name": "ERP Négoce",
    "hero": {
        "badge": "ERP Négoce",
        "title_w": "ERP Négoce — Gérez votre activité de négoce",
        "title_a": "avec Harel",
        "desc": "Pilotez l'ensemble de votre activité de négoce avec un ERP conçu pour les distributeurs, grossistes et négociants. De l'achat à la vente, en passant par la gestion des stocks et la traçabilité.",
        "bg": "https://www.helloharel.com/prometheus/wp-content/uploads/2023/08/bg-line-v7.png"
    },
    "bento": {
        "overline": "Modules Négoce",
        "heading": "Toutes les fonctionnalités pour le négoce",
        "sub": "Un ERP complet qui couvre l'intégralité de votre chaîne de valeur",
        "cards": [
            {"icon": "cart", "color": "blue", "bg_icon": "cart", "title": "Gestion des achats et approvisionnements", "desc": "Centralisez vos commandes fournisseurs, négociez vos conditions d'achat et automatisez vos réapprovisionnements. Anticipez vos besoins grâce à l'analyse de la demande.", "checks": ["Commandes fournisseurs automatisées", "Négociation tarifaire centralisée", "Historique complet des achats"], "link": "/prometheus/fonctionnalites/achat/", "link_text": "Découvrir les achats"},
            {"icon": "dollar", "color": "emerald", "title": "Gestion des ventes / devis / commandes", "desc": "Créez vos devis en quelques clics, transformez-les en commandes puis en factures. Suivez chaque étape du cycle de vente.", "link": "/prometheus/fonctionnalites/vente/"},
            {"icon": "box", "color": "amber", "title": "Gestion des stocks multi-dépôts", "desc": "Suivez vos stocks en temps réel sur plusieurs entrepôts. Transférez, inventoriez et optimisez vos niveaux de stock.", "link": "/prometheus/fonctionnalites/gestion-de-stock/"},
            {"icon": "shield", "color": "indigo", "title": "Traçabilité des lots", "desc": "Traçabilité ascendante et descendante complète. Identifiez chaque lot, de la réception fournisseur à la livraison client."},
            {"icon": "tag", "color": "purple", "title": "Gestion tarifaire, Reporting, Comptabilité & EDI", "desc": "Grilles de prix multiples, remises par volume, tableaux de bord temps réel, export comptable natif et connecteurs EDI/marketplaces.", "sub_links": [{"text": "Gestion tarifaire", "href": "/prometheus/fonctionnalites/vente/"}, {"text": "Reporting", "href": "/prometheus/fonctionnalites/crm/"}, {"text": "Comptabilité", "href": "/prometheus/fonctionnalites/facturation/"}, {"text": "EDI", "href": "/prometheus/fonctionnalites/import-export/"}]},
        ]
    },
    "faq": {
        "overline": "FAQ Négoce",
        "heading": "Questions fréquentes sur l'ERP Négoce",
        "sub": "Tout ce que vous devez savoir pour digitaliser votre activité de négoce.",
        "items": [
            {"icon": "shield", "q": "Qu'est-ce qu'un ERP Négoce et pourquoi en ai-je besoin ?", "meta": "Centralisation, automatisation, visibilité", "html": "<h3>Un ERP conçu pour les négociants</h3><p>Un ERP Négoce centralise toutes les opérations d'une entreprise de distribution : achats fournisseurs, gestion des stocks, ventes clients, facturation et logistique.</p><p>Sans ERP, ces données sont éparpillées entre tableurs, logiciels isolés et documents papier. Le risque : erreurs de saisie, ruptures de stock, marges invisibles. Un ERP Négoce unifie tout en un seul système.</p>"},
            {"icon": "box", "q": "L'ERP gère-t-il les stocks multi-dépôts et multi-sites ?", "meta": "Plusieurs entrepôts, transferts, consolidation", "html": "<h3>Multi-dépôts natif</h3><p>Oui, Hello Harel gère nativement plusieurs entrepôts avec :</p><ul><li><strong>Vision consolidée</strong> — Stock total et par dépôt en temps réel</li><li><strong>Transferts inter-dépôts</strong> — Avec traçabilité complète</li><li><strong>Inventaires par emplacement</strong> — Inventaires tournants ou complets</li></ul>"},
            {"icon": "tag", "q": "Comment fonctionne la gestion tarifaire ?", "meta": "Grilles de prix, remises, conditions commerciales", "html": "<h3>Tarification flexible et puissante</h3><p>Hello Harel supporte des grilles tarifaires complexes :</p><ul><li><strong>Prix par client ou groupe</strong></li><li><strong>Remises par volume, palier ou fidélité</strong></li><li><strong>Promotions temporaires</strong></li><li><strong>Marges calculées en temps réel</strong> sur chaque ligne de devis</li></ul>"},
            {"icon": "clock", "q": "Combien de temps pour déployer l'ERP Négoce ?", "meta": "Déploiement rapide, import données", "html": "<h3>Opérationnel en 3 à 5 jours</h3><p>Hello Harel est un ERP SaaS. Pas de serveur à installer, pas d'intégrateur externe :</p><ul><li><strong>Jour 1</strong> — Import de vos données (clients, fournisseurs, produits, tarifs)</li><li><strong>Jour 2-3</strong> — Paramétrage entrepôts, conditions commerciales, workflows</li><li><strong>Jour 4-5</strong> — Formation équipe (2h visio) et premières commandes réelles</li></ul>"},
        ]
    }
}
