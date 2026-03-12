# Déploiement Design System — Hello Harel Staging

> Staging : `helloharel.com/prometheus`
> Ref maquettes : `design-reference/menu.html` + `design-reference/homepage.html`

---

## Fichiers du design system

| Fichier | Usage |
|---|---|
| `global.css` | CSS complet à injecter (19 sections, ~700 lignes) |
| `animations.js` | Scroll reveal + FAQ accordion + mega menu interactions |
| `elementor-global-colors.json` | 17 couleurs globales Elementor à configurer |
| `elementor-global-fonts.json` | 5 typographies globales Elementor à configurer |
| `page-mapping.json` | Classes CSS à appliquer page par page |

---

## ÉTAPE 1 — Supprimer l'ancien override d'animations

Le site a actuellement cette règle dans le Kit CSS (ID 1020) qui **bloque toutes les animations** :

```css
* { animation: none !important; transition: none !important; }
```

**Action :** Elementor > Réglages du site > CSS Personnalisé → **supprimer cette règle**.

---

## ÉTAPE 2 — Injecter le CSS Global

1. Ouvrir n'importe quelle page dans Elementor
2. Cliquer sur ☰ (hamburger) → **Réglages du site** → **CSS Personnalisé**
3. **Effacer** le CSS existant (sauf le blockquote si voulu — il est inclus dans global.css)
4. **Coller** tout le contenu de `global.css`
5. **Sauvegarder**

Le CSS cible directement les templates globaux :
- `.elementor-1868` → header (auto-appliqué)
- `.elementor-1746` → footer (auto-appliqué)
- `body.single-post` → articles de blog (auto-appliqué)

**Résultat immédiat** : typo Inter, header bleu foncé, footer slate-900, boutons arrondis, cards avec hover.

---

## ÉTAPE 3 — Injecter le JavaScript

1. **WP Admin → Elementor → Custom Code** (ou via un widget HTML dans le footer)
2. Créer un snippet nommé "HH Design Animations"
3. Emplacement : **Avant `</body>`**
4. Coller :
```html
<script>
[contenu de animations.js]
</script>
```
5. Condition : Tout le site
6. Publier

---

## ÉTAPE 4 — Configurer les Global Colors

**Elementor → Réglages du site → Couleurs globales**

Voir `elementor-global-colors.json` pour la liste complète. Prioritaires :

| Nom | Hex | Rôle |
|---|---|---|
| Primary | `#1d4ed8` | Boutons, accents |
| Primary Dark | `#1e3a8a` | Header bg |
| Text Dark | `#0f172a` | Titres |
| Text Body | `#64748b` | Corps de texte |
| BG Light | `#f8fafc` | Fonds alternés |
| Border | `#e2e8f0` | Bordures cards |

---

## ÉTAPE 5 — Configurer les Global Fonts

**Elementor → Réglages du site → Polices globales**

Voir `elementor-global-fonts.json`. Résumé :

| Nom | Font | Weight | Usage |
|---|---|---|---|
| Heading Primary | Inter | 900 Black | H1, H2 |
| Heading Secondary | Inter | 700 Bold | H3, H4 |
| Body Text | Inter | 500 Medium | Paragraphes |
| Label | Inter | 700 Bold + uppercase | Badges, labels |
| Navigation | Inter | 500 Medium | Menu items |

---

## ÉTAPE 6 — Appliquer les classes CSS page par page

Le design global (typo, header, footer, boutons, cards) est automatique.
Pour aller plus loin, appliquer les classes CSS sur chaque section/widget :

### Comment appliquer une classe CSS dans Elementor :
1. Cliquer sur la section/widget
2. Onglet **Avancé** → champ **CSS Classes**
3. Taper la classe (ex: `hh-bg-slate`)

### Page d'accueil (ID 2) :

| Élément | Classe(s) à ajouter |
|---|---|
| Top bar téléphone | `hh-gradient-bar hh-py-0` |
| Section hero | `hh-hero-overlay hh-relative` |
| Badge pill du hero | `hh-badge-pill` |
| H1 (texte avec dégradé) | `hh-gradient-text` |
| Description hero | `hh-text-lg` |
| CTA primaire | `hh-btn-lg` |
| CTA secondaire | `hh-btn-secondary hh-btn-lg` |
| Carousel logos clients | `hh-logo-carousel hh-py-sm` |
| Section fonctionnalités | `hh-bg-slate` |
| Label "Notre Expertise" | `hh-label-heading` |
| Card Stocks/WMS (grande) | `hh-card-lg hh-accent-blue` |
| Card Ventes/CRM | `hh-card-blue` |
| Card Tarification B2B | `hh-card-dark` |
| Card Achats/Réassort | `hh-accent-emerald` |
| Card EDI | `hh-card-blue-light` |
| Section vidéo | `hh-bg-white` |
| Label vidéo | `hh-label-heading` |
| Section FAQ | `hh-bg-white` |

### Page Fonctionnalités (ID 4728) :

| Module | Classe accent |
|---|---|
| CRM | `hh-accent-blue` |
| Facturation | `hh-accent-indigo` |
| Vente | `hh-accent-emerald` |
| Gestion de stock | `hh-accent-amber` |
| Fabrication | `hh-accent-red` |
| Logistique | `hh-accent-teal` |
| Achat | `hh-accent-cyan` |
| Import Export | `hh-accent-orange` |

### Pages Métiers (agro, traiteur, etc.) :

| Élément | Classe(s) |
|---|---|
| Hero section | `hh-hero-overlay hh-relative` |
| Badge métier | `hh-badge-pill` |
| Section features | `hh-bg-white` ou `hh-bg-slate` en alternance |
| Cards features | `hh-accent-emerald` (agro) |
| CTA final | `hh-bg-blue` |

### Articles de blog :
→ **Automatique** via `body.single-post` dans le CSS. Aucune classe à ajouter.

---

## ÉTAPE 7 — Vérification SEO post-déploiement

Référence : `seo-baseline.md`

### Checklist par page :

- [ ] Page charge sans erreur
- [ ] Meta title identique (onglet navigateur)
- [ ] Meta description identique (vue source → `<meta name="description">`)
- [ ] H1 identique
- [ ] Contenu texte intact (même nombre de mots ±5%)
- [ ] Liens internes fonctionnels
- [ ] Images et alt text présents

### 6 pages à vérifier en priorité :

1. `/` (ID 2)
2. `/fonctionnalites/` (ID 4728)
3. `/agroalimentaire/` (ID 1726)
4. `/tarifs/` (ID 608)
5. `/contact/` (ID 661)
6. `/blog/erp-saas/` (ID 5325)

---

## Rollback

**Le CSS ne modifie aucun contenu, aucune URL, aucun lien.**

Pour revenir en arrière :
1. Supprimer le contenu de `global.css` du Custom CSS Elementor
2. Remettre `* { animation: none !important; transition: none !important; }`
3. Le site revient à son état original instantanément
