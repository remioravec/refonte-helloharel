# Hello Harel — Refonte Site Web

ERP SaaS pour l'agroalimentaire et le médical.
Staging : `https://www.helloharel.com/prometheus/`

## Structure du projet

```
├── index.html                 # Homepage
├── style.css                  # Design system (CSS global)
├── page_data.py               # Contenu des pages (hero, bento, FAQ)
│
├── agroalimentaire.html       # Pages mères (preview local)
├── fonctionnalites.html
├── ecosysteme.html
├── qui-sommes-nous.html
├── tarifs.html
├── contact.html
├── blog.html
├── integrateurs.html
├── erp-ia.html
│
├── pages/                     # Pages générées (agro + médical)
│   ├── crm.html ... (16 pages agro)
│   └── medical.html ... (6 pages médical)
│
├── deploy-homepage.py         # Deploy homepage (id=2)
├── deploy-all-pages.py        # Deploy 16 pages agro + sections partagées
└── deploy-blog-template.py    # Appliquer le template aux articles
```

## Déploiement

```bash
# Homepage
python3 deploy-homepage.py

# 16 pages du mega menu (agro)
python3 deploy-all-pages.py

# Template articles de blog (72 posts)
python3 deploy-blog-template.py
```

Les autres pages (contact, tarifs, écosystème, médical, etc.) sont déployées via un script inline.
