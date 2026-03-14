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
            {"icon": "users", "color": "blue", "bg_icon": "users", "title": "Gestion de la relation client (CRM)", "desc": "Centralisez vos contacts clients, l'historique des commandes et les relances commerciales. Fidélisez vos clients et développez vos ventes récurrentes.", "checks": ["Historique complet des interactions", "Relances commerciales automatisées", "Tarifs personnalisés par client"], "link": "/fonctionnalites/crm/", "link_text": "Découvrir notre CRM"},
            {"icon": "doc", "color": "indigo", "title": "Gestion de la facturation", "desc": "Générez devis, bons de livraison, factures et suivez vos règlements en temps réel. Conformité légale garantie.", "link": "/fonctionnalites/facturation/"},
            {"icon": "dollar", "color": "emerald", "title": "Gestion commerciale", "desc": "Organisez vos catalogues produits, promotions et tarifs spécifiques par client ou groupe.", "link": "/fonctionnalites/vente/"},
            {"icon": "box", "color": "amber", "title": "Gestion des stocks", "desc": "Suivez vos stocks en temps réel sur plusieurs entrepôts. Évitez les ruptures et optimisez votre trésorerie.", "link": "/fonctionnalites/gestion-de-stock/"},
            {"icon": "gear", "color": "purple", "title": "Fabrication, Achats, Logistique & Import-Export", "desc": "Gérez gammes et recettes, anticipez vos approvisionnements, optimisez vos tournées et prenez en charge vos documents douaniers.", "sub_links": [{"text": "Fabrication", "href": "/fonctionnalites/fabrication/"}, {"text": "Achats", "href": "/fonctionnalites/achat/"}, {"text": "Logistique", "href": "/fonctionnalites/logistique/"}, {"text": "Import-Export", "href": "/fonctionnalites/import-export/"}]},
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
            {"icon": "database", "color": "blue", "bg_icon": "users", "title": "Centralisation des données clients", "desc": "Regroupez tous vos contacts, devis, historiques d'achats et échanges commerciaux en un seul endroit. Vous gagnez en fiabilité et en rapidité d'accès à l'information.", "checks": ["Fiche client complète et unifiée", "Historique des commandes et échanges", "Conditions tarifaires personnalisées"], "link": "/fonctionnalites/crm/", "link_text": "Découvrir le module CRM"},
            {"icon": "chart", "color": "emerald", "title": "Pipeline commercial en temps réel", "desc": "Visualisez votre pipeline commercial, suivez vos opportunités et anticipez vos prévisions de chiffre d'affaires grâce à des tableaux de bord clairs.", "link": "/fonctionnalites/crm/"},
            {"icon": "bell", "color": "amber", "title": "Automatisation des relances", "desc": "Programmez vos relances, e-mails et rappels téléphoniques. Votre ERP CRM travaille pour vous, même lorsque vous êtes sur d'autres tâches.", "link": "/fonctionnalites/crm/"},
            {"icon": "clipboard", "color": "indigo", "title": "Analyse et reporting", "desc": "Pilotez votre activité avec des rapports détaillés : performances commerciales, clients les plus rentables, périodes creuses.", "link": "/fonctionnalites/crm/"},
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
            {"icon": "clock", "color": "blue", "bg_icon": "doc", "title": "Gain de temps considérable", "desc": "Créez vos devis, transformez-les en factures, enregistrez les paiements : tout se fait en quelques clics. Vous éliminez les doubles saisies et libérez du temps.", "checks": ["Transformation devis → facture en 1 clic", "Numérotation automatique conforme", "Export comptable automatisé"], "link": "/fonctionnalites/facturation/", "link_text": "Découvrir la facturation"},
            {"icon": "shield", "color": "emerald", "title": "Moins d'erreurs, plus de sécurité", "desc": "TVA appliquée automatiquement, mentions légales conformes, cohérence des données contrôlée. Vous évitez les erreurs coûteuses et les pénalités fiscales.", "link": "/fonctionnalites/facturation/"},
            {"icon": "bell", "color": "amber", "title": "Suivi des paiements clients", "desc": "Identifiez instantanément qui vous doit quoi. Relances automatisées, échéanciers, alertes sur impayés : sécurisez votre trésorerie.", "link": "/fonctionnalites/facturation/"},
            {"icon": "chart", "color": "indigo", "title": "Vision claire du chiffre d'affaires", "desc": "Tableaux de bord intégrés pour piloter vos revenus mois par mois, suivre vos meilleures ventes et anticiper votre trésorerie.", "link": "/fonctionnalites/facturation/"},
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
            {"icon": "chart", "color": "emerald", "bg_icon": "dollar", "title": "Vision globale et instantanée", "desc": "Gérer ses ventes avec des fichiers Excel, c'est courir après l'information. Un ERP spécialisé change la donne avec des tableaux de bord en temps réel.", "checks": ["Dashboard CA en temps réel", "Marges par produit et par client", "Prévisions de ventes automatiques"], "link": "/fonctionnalites/vente/", "link_text": "Découvrir la gestion commerciale"},
            {"icon": "arrows", "color": "blue", "title": "Processus commerciaux fluides", "desc": "Devis, commandes, livraisons, factures : tout est relié. Vous évitez les erreurs et donnez une image professionnelle à vos clients.", "link": "/fonctionnalites/vente/"},
            {"icon": "users", "color": "amber", "title": "Collaboration inter-équipes", "desc": "Les informations commerciales sont accessibles à tous : service commercial, production, logistique, comptabilité. Moins d'erreurs, plus de réactivité.", "link": "/fonctionnalites/vente/"},
            {"icon": "tag", "color": "indigo", "title": "Multi-tarifs et promotions", "desc": "Gérez des grilles tarifaires illimitées par client, groupe ou volume. Appliquez automatiquement remises et promotions selon vos règles.", "link": "/fonctionnalites/vente/"},
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
            {"icon": "warehouse", "color": "amber", "bg_icon": "box", "title": "Multi-entrepôts", "desc": "Pilotez vos stocks sur plusieurs sites depuis une seule interface. Vision globale ou détaillée par entrepôt, avec transferts inter-sites tracés.", "checks": ["Stocks par entrepôt en temps réel", "Transferts inter-sites avec traçabilité", "Consolidation multi-sites en 1 clic"], "link": "/fonctionnalites/gestion-de-stock/", "link_text": "Découvrir la gestion de stock"},
            {"icon": "search", "color": "blue", "title": "Traçabilité lots et séries", "desc": "Traçabilité totale des lots et numéros de séries. Indispensable pour les secteurs soumis à des normes strictes comme l'agroalimentaire.", "link": "/fonctionnalites/gestion-de-stock/"},
            {"icon": "bell", "color": "red", "title": "Alertes seuils mini/maxi", "desc": "Alertes automatiques dès que vos stocks passent en dessous ou au-dessus des seuils définis. Anticipez vos achats et évitez ruptures ou surstock.", "link": "/fonctionnalites/gestion-de-stock/"},
            {"icon": "clipboard", "color": "emerald", "title": "Inventaires simplifiés", "desc": "Interface intuitive pour le comptage physique, cohérence des écarts, inventaires tournants ou complets.", "link": "/fonctionnalites/gestion-de-stock/"},
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
            {"icon": "calendar", "color": "red", "bg_icon": "gear", "title": "Ordonnancement de la production", "desc": "Ajustez vos plannings en fonction des commandes, ressources disponibles et délais. Garantissez une fluidité maximale sur vos lignes de production.", "checks": ["Planning dynamique par atelier", "Gestion des capacités machines", "Ajustement temps réel aux commandes"], "link": "/fonctionnalites/fabrication/", "link_text": "Découvrir le module fabrication"},
            {"icon": "list", "color": "blue", "title": "Suivi des ordres de fabrication", "desc": "Chaque OF est tracé en temps réel, du lancement au produit fini. Visibilité sur l'avancement, consommations matières et temps de fabrication.", "link": "/fonctionnalites/fabrication/"},
            {"icon": "gear", "color": "amber", "title": "Nomenclatures et gammes", "desc": "Gérez des nomenclatures complexes multi-niveaux et des gammes opératoires détaillées pour calculer précisément vos besoins et temps.", "link": "/fonctionnalites/fabrication/"},
            {"icon": "dollar", "color": "emerald", "title": "Calcul des coûts de production", "desc": "Calcul automatique des coûts : matières premières, main-d'œuvre, charges. Analysez vos marges et repérez les postes d'économie.", "link": "/fonctionnalites/fabrication/"},
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
            {"icon": "users", "color": "teal", "bg_icon": "cart", "title": "Gestion des fournisseurs", "desc": "Centralisez toutes vos fiches fournisseurs, historiques d'achats, conditions tarifaires et délais pour mieux négocier et sécuriser vos relations.", "checks": ["Fiches fournisseurs complètes", "Historique des achats et conditions", "Évaluation des performances fournisseurs"], "link": "/fonctionnalites/achat/", "link_text": "Découvrir le module achats"},
            {"icon": "tag", "color": "blue", "title": "Comparaison des conditions", "desc": "Comparez en un clic les prix et conditions de plusieurs fournisseurs pour un même produit. Gagnez en pouvoir de négociation.", "link": "/fonctionnalites/achat/"},
            {"icon": "clipboard", "color": "amber", "title": "Suivi des commandes", "desc": "Suivi en temps réel : état de traitement, délais, réceptions partielles ou complètes. Contrôle total sur votre chaîne d'approvisionnement.", "link": "/fonctionnalites/achat/"},
            {"icon": "bell", "color": "red", "title": "Alertes et seuils", "desc": "Alertes automatiques sur seuils minimums pour anticiper vos réapprovisionnements et éviter les ruptures.", "link": "/fonctionnalites/achat/"},
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
            {"icon": "truck", "color": "cyan", "bg_icon": "arrows", "title": "Optimisation des tournées", "desc": "Planifiez vos tournées de livraison en tenant compte des contraintes géographiques, des créneaux clients et des capacités de vos véhicules.", "checks": ["Planification géographique des tournées", "Respect des créneaux de livraison", "Optimisation des chargements"], "link": "/fonctionnalites/logistique/", "link_text": "Découvrir le module logistique"},
            {"icon": "search", "color": "blue", "title": "Suivi en temps réel", "desc": "Visualisez l'état de vos livraisons en temps réel. Informez vos clients de l'avancement et anticipez les retards.", "link": "/fonctionnalites/logistique/"},
            {"icon": "warehouse", "color": "amber", "title": "Gestion des entrepôts (WMS)", "desc": "Organisez vos zones de picking, optimisez les parcours de préparation et réduisez les erreurs de préparation.", "link": "/fonctionnalites/logistique/"},
            {"icon": "clipboard", "color": "emerald", "title": "Préparation des commandes", "desc": "Bons de préparation optimisés par zone, contrôle des quantités, validation par scan. Réduisez les erreurs de 80%.", "link": "/fonctionnalites/logistique/"},
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
            {"icon": "doc", "color": "orange", "bg_icon": "globe", "title": "Formalités douanières", "desc": "Déclarations douanières automatisées, gestion des nomenclatures TARIC et certificats d'origine pour une conformité totale.", "checks": ["Déclarations douanières automatiques", "Codes TARIC et certificats d'origine", "Documents phytosanitaires et vétérinaires"], "link": "/fonctionnalites/import-export/", "link_text": "Découvrir le module import-export"},
            {"icon": "search", "color": "blue", "title": "Suivi des expéditions mondiales", "desc": "Tracking en temps réel de vos marchandises partout dans le monde. Informez vos clients à chaque étape de la chaîne logistique.", "link": "/fonctionnalites/import-export/"},
            {"icon": "dollar", "color": "emerald", "title": "Calcul des droits et taxes", "desc": "Calcul automatique des droits de douane, TVA intracommunautaire et taxes spécifiques selon les accords internationaux.", "link": "/fonctionnalites/import-export/"},
            {"icon": "globe", "color": "amber", "title": "Gestion multi-devises", "desc": "Transactions en multi-devises avec conversions automatiques et intégration comptable. Vision claire de vos marges à l'international.", "link": "/fonctionnalites/import-export/"},
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
            {"icon": "search", "color": "blue", "bg_icon": "shield", "title": "Gestion des lots et traçabilité", "desc": "Chaque mouvement est tracé de l'entrée matière première au produit fini. Retrouvez instantanément l'origine ou la destination d'un lot en cas d'alerte sanitaire.", "checks": ["Traçabilité ascendante et descendante", "Historique complet par lot", "Rappel produit en quelques secondes"], "link": "/agroalimentaire/", "link_text": "Découvrir l'ERP agroalimentaire"},
            {"icon": "calendar", "color": "amber", "title": "Gestion des DLC et DLUO", "desc": "Gestion automatique de vos dates limites. Alertes quand vos stocks approchent de la péremption. FIFO automatique pour limiter les pertes.", "link": "/agroalimentaire/"},
            {"icon": "dollar", "color": "emerald", "title": "Calcul du coût de revient", "desc": "Coût de revient au centime près pour chaque produit fini. Maîtrisez vos marges même avec des prix matières fluctuants.", "link": "/agroalimentaire/"},
            {"icon": "thermo", "color": "red", "title": "Gestion des stocks sensibles", "desc": "Stocks à contraintes sanitaires : température, hygrométrie. Alertes automatiques en cas de dépassement des seuils autorisés.", "link": "/agroalimentaire/"},
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
    "id": 2839, "slug": "traiteur", "name": "ERP Traiteur",
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
            {"icon": "calendar", "color": "blue", "bg_icon": "fire", "title": "Gestion des événements multiples", "desc": "Planning événementiel intégré : visualisez tous vos événements, évitez les conflits et anticipez vos besoins en personnel et matières premières.", "checks": ["Planning multi-événements", "Anticipation des besoins par événement", "Gestion du personnel et des prestataires"], "link": "/agroalimentaire/traiteur/", "link_text": "Découvrir l'ERP traiteur"},
            {"icon": "box", "color": "amber", "title": "Achats et stocks événementiels", "desc": "Stocks avec alertes DLC, suivi des matières sensibles et liens directs avec vos besoins selon les événements prévus.", "link": "/agroalimentaire/traiteur/"},
            {"icon": "dollar", "color": "emerald", "title": "Coûts et marges par événement", "desc": "Calcul automatique du coût matière et de la marge nette par événement. Visualisez immédiatement la rentabilité de chaque prestation.", "link": "/agroalimentaire/traiteur/"},
            {"icon": "shield", "color": "red", "title": "Traçabilité et conformité HACCP", "desc": "Chaque lot tracé, chaque DLC contrôlée. Documents sanitaires générés automatiquement pour un contrôle qualité irréprochable.", "link": "/agroalimentaire/traiteur/"},
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
    "id": 2824, "slug": "maraicher", "name": "ERP Fruits et Légumes",
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
            {"icon": "search", "color": "emerald", "bg_icon": "leaf", "title": "Traçabilité de la récolte au client", "desc": "Chaque lot tracé depuis la parcelle ou le fournisseur jusqu'au client final. Origine, calibre, variété : tout est enregistré.", "checks": ["Traçabilité par parcelle et fournisseur", "Calibres, variétés et origines", "Rappel produit en quelques secondes"], "link": "/agroalimentaire/maraicher/", "link_text": "Découvrir l'ERP maraîcher"},
            {"icon": "tag", "color": "amber", "title": "Prix saisonniers en temps réel", "desc": "Les prix changent chaque jour. L'ERP met à jour vos tarifs selon le marché pour protéger vos marges automatiquement.", "link": "/agroalimentaire/maraicher/"},
            {"icon": "doc", "color": "blue", "title": "Certificats phytosanitaires", "desc": "Génération automatique des certificats phytosanitaires exigés par vos clients ou pour l'export. Gain de temps précieux.", "link": "/agroalimentaire/maraicher/"},
            {"icon": "clipboard", "color": "indigo", "title": "Préparation des commandes", "desc": "Conditionnements multiples (au poids, à la pièce, au colis) et chargements optimisés selon vos tournées de livraison.", "link": "/agroalimentaire/maraicher/"},
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
    "id": 3309, "slug": "boulanger", "name": "ERP Boulangerie Pâtisserie",
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
            {"icon": "dollar", "color": "amber", "bg_icon": "bread", "title": "Coût de revient par recette", "desc": "Calcul du coût matière et de la marge nette pour chaque produit : baguette, croissant, entremets. Rentabilité exacte, même sur les recettes complexes.", "checks": ["Coût matière par recette", "Marge nette par produit fini", "Impact des variations de prix matières"], "link": "/agroalimentaire/boulanger/", "link_text": "Découvrir l'ERP boulangerie"},
            {"icon": "calendar", "color": "blue", "title": "Planification des fournées", "desc": "Planifiez vos fournées selon les ventes prévisionnelles. Évitez le gaspillage et optimisez vos heures de main-d'œuvre.", "link": "/agroalimentaire/boulanger/"},
            {"icon": "thermo", "color": "red", "title": "Stocks sensibles (beurre, œufs...)", "desc": "DLC surveillées, conditions de stockage contrôlées, alertes en cas d'anomalie. Vos matières premières sensibles sont maîtrisées.", "link": "/agroalimentaire/boulanger/"},
            {"icon": "warehouse", "color": "indigo", "title": "Multi-points de vente", "desc": "Synchronisez production, stocks et ventes entre vos boutiques. Vision consolidée de votre entreprise en un clic.", "link": "/agroalimentaire/boulanger/"},
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
    "id": 2818, "slug": "charcutier", "name": "ERP Charcutier",
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
            {"icon": "search", "color": "red", "bg_icon": "knife", "title": "Traçabilité vétérinaire", "desc": "Chaque lot tracé depuis la matière première jusqu'au produit fini : numéros vétérinaires, dates d'abattage, poids, températures.", "checks": ["Numéros vétérinaires par lot", "Dates d'abattage et températures", "Historique complet pour l'administration"], "link": "/agroalimentaire/charcutier/", "link_text": "Découvrir l'ERP charcutier"},
            {"icon": "clock", "color": "amber", "title": "DLC courtes et températures", "desc": "Alertes automatiques quand des lots approchent de la péremption (3 à 15 jours de DLC). Surveillance des températures intégrée.", "link": "/agroalimentaire/charcutier/"},
            {"icon": "dollar", "color": "emerald", "title": "Coûts de revient et rendements", "desc": "Coût matière et marge nette sur chaque recette. Prise en compte du poids après cuisson, pertes au tranchage et coûts d'emballage.", "link": "/agroalimentaire/charcutier/"},
            {"icon": "shield", "color": "blue", "title": "Conformité HACCP", "desc": "Registres sanitaires complets, enregistrements des températures, traçabilité pour les contrôles DGCCRF. Documentation toujours à jour.", "link": "/agroalimentaire/charcutier/"},
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
    "id": 5470, "slug": "industrie-laitiere", "name": "ERP Industrie Laitière",
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
            {"icon": "gear", "color": "blue", "bg_icon": "bottle", "title": "Production : recettes et affinage", "desc": "Pilotez les process de transformation, d'affinage et de conditionnement. Qualité constante et coûts maîtrisés pour votre laiterie ou fromagerie.", "checks": ["Fiches recettes multi-niveaux", "Suivi des cycles d'affinage", "Calcul du rendement fromager"], "link": "/agroalimentaire/industrie-laitiere/", "link_text": "Découvrir l'ERP laitier"},
            {"icon": "shield", "color": "emerald", "title": "Traçabilité et qualité", "desc": "Traçabilité sans faille du lait collecté au produit fini. Audits et contrôles sanitaires ne paralysent plus votre activité.", "link": "/agroalimentaire/industrie-laitiere/"},
            {"icon": "dollar", "color": "amber", "title": "Paiement à la qualité", "desc": "Automatisez le paiement du lait selon les critères de qualité : taux de matière grasse, protéines, cellules. Transparent pour vos producteurs.", "link": "/agroalimentaire/industrie-laitiere/"},
            {"icon": "thermo", "color": "red", "title": "Chaîne du froid et DLC", "desc": "Gestion des DLC/DLUO pour les produits frais. Surveillance des températures de stockage avec alertes automatiques.", "link": "/agroalimentaire/industrie-laitiere/"},
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
    "id": 5477, "slug": "plats-cuisines-industriels", "name": "ERP Plats Cuisinés",
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
            {"icon": "gear", "color": "blue", "bg_icon": "plate", "title": "Recettes multi-niveaux et PRI", "desc": "Gérez des recettes arborescentes avec sous-recettes. Le Prix de Revient Industriel est calculé automatiquement avec une précision au centime.", "checks": ["Nomenclatures multi-niveaux illimitées", "PRI recalculé en temps réel", "Impact des substitutions de matières"], "link": "/agroalimentaire/plats-cuisines-industriels/", "link_text": "Découvrir l'ERP plats cuisinés"},
            {"icon": "calendar", "color": "amber", "title": "Planning de production GMS", "desc": "Anticipez les commandes GMS (volumes, promotions, DLC courtes). Planifiez votre production en fonction des délais serrés de la grande distribution.", "link": "/agroalimentaire/plats-cuisines-industriels/"},
            {"icon": "shield", "color": "red", "title": "Conformité INCO et allergènes", "desc": "Gestion des allergènes dès la fiche matière première. À chaque modification de recette, la liste est recalculée automatiquement.", "link": "/agroalimentaire/plats-cuisines-industriels/"},
            {"icon": "search", "color": "emerald", "title": "Traçabilité industrielle", "desc": "Traçabilité de chaque lot du fournisseur au client final. Documentation complète pour les audits GMS et les contrôles sanitaires.", "link": "/agroalimentaire/plats-cuisines-industriels/"},
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
