# Crown : règles du projet

Ce dossier est l'environnement de travail de **Crown**, séparé de Sesterce. Rien de Sesterce ici
(ni charte, ni code, ni comptes), rien de Crown dans Sesterce.

## La maison

- Crown est une maison d'investissement. Éditeur du site : **CROWN FRANCE**, SAS au capital de
  12 176 001 €, SIREN 101 540 714, TVA FR56 101 540 714, 56 rue Saint-Jean-du-Désert, 13012 Marseille.
  Directeur de la publication : Anthony Tchakerian.
- Contacts publics : contact@crown.ooo, invest@crown.ooo.
- Quatre activités, toujours dans cet ordre, chiffres romains I à IV :
  1. **Crown Demeure** : « Les propriétés les plus exceptionnelles. Dans un seul portefeuille. »
  2. **Crown Stable** : « Les actifs du monde agricole. Terres, élevage équin et exploitations. »
  3. **Crown Capital** : « Investir pour changer le monde. Et c'est tout. »
  4. **Crown Asset Management** : « Tirer le meilleur de nos fonds. À tout moment. »
  Capital, Estate et Hedge sont les noms de l'ancien site : ne plus les utiliser.

## Le design (décidé par Anthony, ne pas changer sans son accord)

- **Seul le O de « Crown » est rouge** (`#F20823`), partout : ni le C, ni les points, ni les chiffres.
  Le site est crown.ooo, « triple O » : le O est le signe de la maison.
- **Logo X01** : la couronne K15 à gauche, puis « CROWN » en **Marcellus**, capitales, interlettrage
  0,1 em, O rouge. Couronne et mot séparés. Jamais de gras Manrope pour « Crown ».
- **Couronne K15**, boîte 40 × 28, au trait :
  `M20 21.5 L4.2 21.5 L2 7.5 L12.5 14.5 L20 3 L27.5 14.5 L38 7.5 L35.8 21.5 Z`, trois ronds pleins en
  (12, 18.2), (20, 18.2), (28, 18.2) rayon 1.3, barre séparée de 4.6 à 35.4 à y 25.2.
- Chaque « Crown » s'écrit comme le logo (Marcellus, capitales, O rouge). Le texte courant est en Manrope.
- **Accueil « Voile »** : voilier sur mer grise en plein écran ; les quatre activités défilent toutes
  les 8 s, avec onglets, compteur et bouton pause. Le panneau rouge à rosace ne reste que sur la page
  de connexion de l'espace client.
- **Ne jamais semer « Marseille »** ni de coordonnées GPS dans les pages. L'adresse n'apparaît qu'au
  contact et aux mentions légales.

## Les textes

- En français, courts, sur un ton de maison d'investissement (« non, plus pro »), jamais poétique.
- Jamais de tiret long (cadratin).
- Jamais de promesse de rendement, jamais de répartition chiffrée d'un fonds sur le site.
- N'inventer aucun fait : ce qui manque s'écrit `[ ... ]` et se demande à Anthony.
- Proposer en options numérotées (comme K15, X01, D02, V01) avec deux ou trois variantes ; il choisit.

## Le code

- `outils/construire.py` génère toutes les pages dans `site/`. On modifie le générateur et
  `site/assets/crown.css` / `crown.js`, jamais les pages HTML à la main.
- Aucun attribut `style=` dans les pages (la politique de sécurité les bloque) ; aucun script tiers.
- Les liens vers `crown.css` et `crown.js` portent `?v=<empreinte>` (calculée par le générateur).
- Avant tout envoi : `python3 outils/construire.py`, puis regarder les pages à 320, 390, 820 et
  1440 px, en vérifiant la console et le menu du téléphone.
- `design/` (planche Claude Design, essais de logos et de couronnes) reste sur ce Mac : il est exclu
  du dépôt, qui est public.

## La mise en ligne

- Hébergement **Render** (site statique « crown », Blueprint « crown »), publié depuis `site/` sur la
  branche `main` de ce dépôt. Les en-têtes de sécurité et les adresses courtes sont dans `render.yaml`.
- Un envoi sur `main` ne se publie pas seul : sur Render, Blueprint « Manual sync », puis sur le site
  « Manual Deploy » > « Deploy latest commit ». Retirer un en-tête se fait à la main (page Headers).
- Domaine **crown.ooo** chez OVH : A `216.24.57.1`, `www` en CNAME vers `crown-7j8e.onrender.com`.
  **Ne jamais toucher aux MX Google** ni aux réglages de messagerie.
- Rien ne part sur `main`, rien n'est publié et aucun réglage de domaine ne change sans l'accord
  d'Anthony. Auteur des commits : `tchakerian <175748602+tchakerian@users.noreply.github.com>`.
- Ne jamais taper de mot de passe ni écrire de secret dans ce dépôt.
