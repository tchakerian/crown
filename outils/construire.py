# Construit le site Crown (pages statiques) dans le dossier site/.
# Usage : python3 outils/construire.py
import os, math, sys
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenes

ICI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(os.path.dirname(ICI), 'site')  # pages publiées par Render
import hashlib
VER = {n: hashlib.sha256(open(os.path.join(SITE, 'assets', n), 'rb').read()).hexdigest()[:10] for n in ('crown.css', 'crown.js')}

ENT = [  # (fichier, nom, phrase, provisoire)
    ("demeure", "Demeure", "Les propriétés les plus exceptionnelles, dans un seul portefeuille.", True),
    ("stable", "Stable", "Les actifs du monde agricole. Terres, élevage équin et exploitations.", False),
    ("capital", "Capital", "Investir pour changer le monde. Et c'est tout.", False),
    ("asset-management", "Asset Management", "Tirer le meilleur de nos fonds, à tout moment.", True),
]
NUM = ["I", "II", "III", "IV"]
ADRESSE = "56 rue Saint-Jean-du-Désert, 13012 Marseille, France"
COURRIEL = "contact@crown.ooo"
COURRIEL_INVEST = "invest@crown.ooo"
PRES = {  # présentation et trois points par activité (repris du site crown.ooo, réécrits en français)
    "demeure": ("Crown Demeure sélectionne des propriétés d'exception dans le monde entier pour constituer un portefeuille unique, appelé à grandir de façon continue.",
                [("Sélection", "Des biens rares, choisis un à un, en France et à l'international."),
                 ("Portefeuille", "Un ensemble cohérent de propriétés où l'on se sent chez soi."),
                 ("Durée", "Un patrimoine pensé pour croître dans le temps.")]),
    "stable": ("Crown Stable investit dans les actifs du monde agricole : des terres, un élevage équin et des exploitations, détenus sur le long terme.",
               [("Terres", "Du foncier agricole, détenu et exploité dans la durée."),
                ("Élevage équin", "L'élevage de chevaux, au cœur de l'activité."),
                ("Exploitations", "Des exploitations agricoles suivies au plus près.")]),
    "capital": ("Crown Capital investit dans des sociétés cotées et non cotées dotées d'un fort potentiel de long terme. Seul compte le potentiel radical d'une entreprise ; une fois la cible retenue, l'engagement est entier.",
                [("Coté et non coté", "De la jeune entreprise à la société cotée au Nasdaq."),
                 ("Concentration", "Peu de sociétés, retenues pour leur capacité à transformer le monde."),
                 ("Engagement", "Une fois la cible choisie, Crown s'engage pleinement.")]),
    "asset-management": ("Crown Asset Management gère les avoirs de la maison sur les grandes places financières internationales, à court comme à long terme, selon une double stratégie.",
                         [("Places internationales", "Les avoirs de la maison, investis sur les grandes places financières."),
                          ("Deux horizons", "Une part investie sur le long terme, une part pilotée à court terme."),
                          ("Algorithme", "La part de court terme est gérée par un algorithme de trading.")]),
}
VALEURS = [("Les personnes d'abord", "Derrière une entreprise, il y a toujours celles et ceux qui la font."),
           ("La passion du métier", "Chercher et trouver des pépites, chaque jour."),
           ("L'intégrité", "Nous n'investissons que dans des sociétés qui partagent nos valeurs.")]


def points(liste):
    return '<ol class="points">' + ''.join(f'<li><span>0{k + 1}</span><strong>{a}</strong>{b}</li>' for k, (a, b) in enumerate(liste)) + '</ol>'


def ecran_visuel(cle, legende=""):
    """Image pleine hauteur d'un écran partagé, collée au bord de la fenêtre."""
    leg = f'<figcaption>{legende}</figcaption>' if legende else ''
    return (f'<figure class="ecran-visuel visuel-scene" aria-hidden="true">{scenes.svg(cle, "scene-cadre", scenes.CADRES[cle], "xMidYMid slice")}{leg}</figure>')


def visuel(nom):
    return (f'<figure class="visuel" aria-hidden="true"><span class="visuel-horizon"></span>{couronne(140, "couronne", 1.1)}'
            f'<figcaption>{crown("mot")}{(" " + nom.upper()) if nom else ""}</figcaption></figure>')
ACCROCHE = "Crown investit dans ce qui change une vie, dans ce qui a un potentiel unique et significatif."
CITATION = "Nous cherchons, et nous finançons, ce qui nous tient à cœur."


def couronne(w, cls="couronne", e=1.6, anime=False):
    h = round(w * 28 / 40, 1)
    t = ' class="trace" pathLength="1"' if anime else ''
    p = (lambda i: f' class="perle p{i}"') if anime else (lambda i: '')
    b = ' class="barre"' if anime else ''
    return (f'<svg class="{cls}" width="{w}" height="{h}" viewBox="0 0 40 28" aria-hidden="true" focusable="false">'
            f'<path{t} d="M20 21.5 L4.2 21.5 L2 7.5 L12.5 14.5 L20 3 L27.5 14.5 L38 7.5 L35.8 21.5 Z" fill="none" stroke="currentColor" stroke-width="{e}" stroke-linejoin="miter"/>'
            f'<circle{p(1)} cx="12" cy="18.2" r="1.3" fill="currentColor"/><circle{p(2)} cx="20" cy="18.2" r="1.3" fill="currentColor"/><circle{p(3)} cx="28" cy="18.2" r="1.3" fill="currentColor"/>'
            f'<path{b} d="M4.6 25.2 L35.4 25.2" fill="none" stroke="currentColor" stroke-width="{e}"/></svg>')


def crown(cls="mot"):
    return f'<span class="{cls}">CR<span class="o">O</span>WN</span>'


def logo(racine, cls="logo"):
    return f'<a class="{cls}" href="{racine}index.html" aria-label="Crown, accueil">{couronne(32, "couronne", 2.2)}{crown()}</a>'


def rosace():
    cx, cy, n, R, r = 300, 452, 72, 150, 360
    cs = ''.join(f'<circle cx="{cx + R*math.cos(2*math.pi*k/n):.1f}" cy="{cy + R*math.sin(2*math.pi*k/n):.1f}" r="{r}"/>' for k in range(n))
    an = ''.join(f'<circle cx="{cx}" cy="{cy}" r="{rr}"/>' for rr in range(262, 700, 9))
    return (f'<g class="anneaux">{an}</g><g class="rosace">{cs}</g>'
            f'<circle cx="{cx}" cy="{cy}" r="226" class="disque"/>')


def embleme(anime=True):
    return f'''<div class="embleme">
      <div class="reflet" aria-hidden="true"></div>
      <svg class="embleme-svg" viewBox="0 0 600 904" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
        {rosace()}
        <circle class="anneau{' trace-anneau' if anime else ''}" cx="300" cy="452" r="240" transform="rotate(-90 300 452)"/>
        <circle class="anneau-fin" cx="300" cy="452" r="220"/>
        <g class="flotte"><g transform="translate(150 346.25) scale(7.5)">
          <path class="{'trace' if anime else ''}" pathLength="1" d="M20 21.5 L4.2 21.5 L2 7.5 L12.5 14.5 L20 3 L27.5 14.5 L38 7.5 L35.8 21.5 Z" fill="none" stroke="#fff" stroke-width="1.15"/>
          <circle class="{'perle p1' if anime else ''}" cx="12" cy="18.2" r="1.3" fill="#fff"/>
          <circle class="{'perle p2' if anime else ''}" cx="20" cy="18.2" r="1.3" fill="#fff"/>
          <circle class="{'perle p3' if anime else ''}" cx="28" cy="18.2" r="1.3" fill="#fff"/>
          <path class="{'barre' if anime else ''}" d="M4.6 25.2 L35.4 25.2" fill="none" stroke="#fff" stroke-width="1.15"/>
        </g></g>
      </svg>
    </div>'''


def entete(racine, actif):
    def lien(t, href):
        cur = ' aria-current="page"' if t == actif else ''
        return f'<a href="{racine}{href}"{cur}>{t}</a>'
    return f'''<a class="evitement" href="#contenu">Aller au contenu</a>
<div class="bandeau">
  <a href="{racine}contact.html?objet=compte">Ouvrir un compte</a>
  <a class="fort" href="{racine}espace-client.html">Espace client</a>
</div>
<header class="entete">
  {logo(racine)}
  <button class="menu-bouton" type="button" aria-expanded="false" aria-controls="menu">Menu <span class="menu-traits" aria-hidden="true"></span></button>
  <nav id="menu" class="menu" aria-label="Principal">
    {lien("Activités", "index.html#activites")}{lien("À propos", "a-propos.html")}{lien("Contact", "contact.html")}
    <span class="menu-secondaire"><a href="{racine}espace-client.html">Espace client</a><a href="{racine}contact.html?objet=compte">Ouvrir un compte</a></span>
  </nav>
</header>'''


def pied(racine):
    acts = ''.join(f'<li><a href="{racine}activites/{e[0]}.html">Cr<span class="o">o</span>wn {e[1]}</a></li>' for e in ENT)
    return f'''<footer class="pied">
  <div class="pied-grille">
    <div>{logo(racine)}<p>{ACCROCHE}</p></div>
    <div><h2>Activités</h2><ul>{acts}</ul></div>
    <div><h2>La maison</h2><ul><li><a href="{racine}a-propos.html">À propos</a></li><li><a href="{racine}contact.html">Contact</a></li><li><a href="{racine}contact.html">Demander une introduction</a></li></ul></div>
    <div><h2>Clients</h2><ul><li><a href="{racine}espace-client.html">Espace client</a></li><li><a href="{racine}contact.html?objet=compte">Ouvrir un compte</a></li></ul></div>
  </div>
  <div class="pied-bas">
    <span>© Crown</span>
    <span class="pied-liens"><a href="{racine}mentions-legales.html">Mentions légales</a><a href="{racine}confidentialite.html">Confidentialité</a><span class="domaine">crown.<span class="o">ooo</span></span></span>
  </div>
</footer>'''


def activites(racine, titre="Nos activités", exclure=None, ident="activites"):
    cols = ''
    k = 0
    for i, e in enumerate(ENT):
        if e[0] == exclure:
            continue
        on = ' actif' if k == 0 else ''
        k += 1
        cols += f'''
      <a class="colonne{on}" href="{racine}activites/{e[0]}.html">
        <svg class="colonne-fond" viewBox="0 0 420 420" aria-hidden="true" focusable="false"><circle cx="210" cy="210" r="200" fill="none" stroke="#fff" stroke-width="10"/><g transform="translate(60 105) scale(7.5)"><path d="M20 21.5 L4.2 21.5 L2 7.5 L12.5 14.5 L20 3 L27.5 14.5 L38 7.5 L35.8 21.5 Z" fill="none" stroke="#fff" stroke-width="1.1"/><circle cx="12" cy="18.2" r="1.3" fill="#fff"/><circle cx="20" cy="18.2" r="1.3" fill="#fff"/><circle cx="28" cy="18.2" r="1.3" fill="#fff"/><path d="M4.6 25.2 L35.4 25.2" fill="none" stroke="#fff" stroke-width="1.1"/></g></svg>
        <span class="colonne-num" aria-hidden="true">{NUM[i]}</span>
        <span class="colonne-texte">
          {crown("colonne-crown")}
          <span class="colonne-nom">{e[1]}</span>
          <span class="colonne-desc">{e[2]}</span>
          <span class="colonne-lien">Découvrir <span class="fleche" aria-hidden="true">→</span></span>
        </span>
      </a>'''
    return f'''<section class="section activites revele" id="{ident}" aria-labelledby="{ident}-titre">
    <div class="section-tete">
      <h2 id="{ident}-titre">{titre}</h2>
      <p>Quatre activités, une seule maison.</p>
    </div>
    <div class="colonnes">{cols}
    </div>
  </section>'''


def bande(racine):
    return f'''<section class="bande revele">
    {couronne(64, "couronne", 1.4)}
    <p>{CITATION}</p>
    <a class="bouton bouton-blanc" href="{racine}contact.html">Demander une introduction</a>
  </section>'''


def page(chemin, titre, description, actif, corps, racine="", classe=""):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#F20823">
<link rel="icon" href="{racine}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Manrope:wght@200;300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{racine}assets/crown.css?v={VER['crown.css']}">
<script src="{racine}assets/crown.js?v={VER['crown.js']}" defer></script>
</head>
<body{f' class="{classe}"' if classe else ""}>
{entete(racine, actif)}
<main id="contenu">
{corps}
</main>
{pied(racine)}
</body>
</html>
'''


def ecrire(chemin, contenu):
    f = os.path.join(SITE, chemin)
    os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, 'w', encoding='utf-8').write(contenu)


# ---------- Accueil : Voile ----------
VOILE = [  # (fichier, nom, titre, suite, provisoire)
    ("demeure", "Demeure", "Les propriétés les plus exceptionnelles.", "Dans un seul portefeuille.", False),
    ("stable", "Stable", "Les actifs du monde agricole.", "Terres, élevage équin et exploitations.", False),
    ("capital", "Capital", "Investir pour changer le monde.", "Et c'est tout.", False),
    ("asset-management", "Asset Management", "Tirer le meilleur de nos fonds.", "À tout moment.", False),
]


def scene_accueil():
    """Une scène par activité, superposées ; celle de l'activité affichée apparaît en fondu."""
    return '\n    '.join(scenes.svg(f, f"voile-scene scene s{i}") for i, (f, *_r) in enumerate(VOILE))


def voile():
    diapos = ''
    for i, (f, nom, titre, suite, prov) in enumerate(VOILE):
        diapos += f'''
        <article class="diapo{' actif' if i == 0 else ''}" id="diapo-{i}" aria-roledescription="diapositive" aria-label="{i + 1} sur 4 : Crown {nom}"{'' if i == 0 else ' aria-hidden="true"'}>
          <p class="diapo-marque">{crown("mot")} {nom.upper()}</p>
          <h2 class="diapo-titre{' provisoire' if prov else ''}">{titre}</h2>
          <div class="diapo-suite">
            <p>{suite}</p>
            <a class="diapo-lien" href="activites/{f}.html"{'' if i == 0 else ' tabindex="-1"'}>Découvrir <span class="mot">CR<span class="o">O</span>WN {nom.upper()}</span><span class="fleche" aria-hidden="true">→</span></a>
          </div>
        </article>'''
    onglets = ''.join(f'<a class="onglet{" actif" if i == 0 else ""}" href="activites/{f}.html" data-diapo="{i}"><span class="onglet-filet"><span class="onglet-prog"></span></span><span class="onglet-nom">{nom}</span></a>' for i, (f, nom, *_r) in enumerate(VOILE))
    return f'''  <section class="voile" data-actif="0" aria-roledescription="carrousel" aria-label="Les activités de Crown">
    <h1 class="visuellement-cache">Crown, maison d'investissement : Demeure, Stable, Capital, Asset Management</h1>
    {scene_accueil()}
    <div class="voile-voile" aria-hidden="true"></div>
    <div class="voile-contenu">
      <div class="diapos">{diapos}
      </div>
      <div class="voile-bas">
        <nav class="onglets" aria-label="Activités">{onglets}</nav>
        <div class="voile-commandes">
          <p class="compteur" aria-hidden="true"><span class="compteur-n">01</span> <span class="compteur-sep">/</span> 04</p>
          <button class="voile-pause" type="button" aria-label="Mettre le défilement en pause"><span class="pause-icone" aria-hidden="true"></span></button>
        </div>
      </div>
    </div>
    <p class="voile-suivante" aria-hidden="true">Ensuite · <span class="suivante-nom">Stable</span></p>
  </section>'''


# ---------- Accueil ----------
noms = ''.join(f'<a class="nom" href="activites/{e[0]}.html">{e[1]}</a>' for i, e in enumerate(ENT))
accueil = f'''{voile()}
  {activites("")}
  {bande("")}
  <section class="clients revele" aria-label="Accès clients">
    <a class="carte" href="espace-client.html"><span class="surtitre">Espace client</span><span class="carte-titre">Retrouvez votre compte.</span><span class="carte-lien">Se connecter →</span></a>
    <a class="carte" href="contact.html?objet=compte"><span class="surtitre">Nouveau client</span><span class="carte-titre">Ouvrir un compte chez Crown.</span><span class="carte-lien">Ouvrir un compte →</span></a>
  </section>'''
ecrire("index.html", page("index.html", "Crown, maison d'investissement", ACCROCHE, "", accueil, classe="accueil"))

# ---------- Pages des activités ----------
for i, e in enumerate(ENT):
    corps = f'''  <section class="ecran">
    <div class="ecran-texte apparait">
      <nav class="fil" aria-label="Fil d'Ariane"><a href="../index.html">Accueil</a> / <a href="../index.html#activites">Activités</a> / <span aria-current="page">Crown {e[1]}</span></nav>
      <div class="ecran-corps">
        <span class="numero">{NUM[i]}</span>
        <h1 class="activite-titre"><span class="titre-crown">CR<span class="o">O</span>WN</span><span class="activite-nom">{e[1]}</span></h1>
        <p class="activite-phrase">{e[2]}</p>
        <a class="bouton" href="../contact.html?activite={e[0]}">Demander une introduction</a>
      </div>
    </div>
    {ecran_visuel(e[0], f'<span class="legende-num">{NUM[i]}</span>{crown("mot")} {e[1].upper()}')}
  </section>
  <section class="presentation revele">
    <h2>Crown {e[1]}</h2>
    <div>
      <p>{PRES[e[0]][0]}</p>
      {points(PRES[e[0]][1])}
    </div>
  </section>
  {activites("../", "Les autres activités", exclure=e[0], ident="autres")}
  {bande("../")}'''
    ecrire(f"activites/{e[0]}.html", page("", f"Crown {e[1]}", e[2], "Activités", corps, "../"))

# ---------- À propos ----------
apropos = f'''  <section class="ecran">
    <div class="ecran-texte apparait">
      <div class="ecran-corps">
        <p class="surtitre">À propos</p>
        <h1 class="ecran-titre">Crown investit dans ce qui change une vie.</h1>
        <p class="grand">{ACCROCHE} {CITATION}</p>
        <p class="suite">Les fonds de Crown partagent une même ambition : reproduire, chacun dans son domaine, des modèles de prospérité. Quatre activités, chacune experte de son métier, une seule maison.</p>
      </div>
    </div>
    {ecran_visuel("maison", crown("mot"))}
  </section>
  <section class="presentation revele">
    <h2>Nos valeurs</h2>
    <div>
      <p>Les valeurs que nous partageons sont celles qui guident nos investissements.</p>
      {points(VALEURS)}
    </div>
  </section>
  {activites("")}
  {bande("")}'''
ecrire("a-propos.html", page("", "À propos de Crown", ACCROCHE, "À propos", apropos))

# ---------- Contact ----------
opts = ''.join(f'<option value="{e[0]}">Crown {e[1]}</option>' for e in ENT)
contact = f'''  <section class="ecran ecran-inverse">
    {ecran_visuel("contact")}
    <div class="ecran-texte apparait">
      <div class="ecran-corps">
        <p class="surtitre">Contact</p>
        <h1 class="ecran-titre">Demander une introduction</h1>
        <p class="accroche">Dites-nous qui vous êtes et ce qui vous amène. Nous revenons vers vous personnellement.</p>
        <form class="formulaire" id="formulaire-contact" method="post" action="#" novalidate data-courriel="{COURRIEL}">
          <label>Prénom<input name="prenom" autocomplete="given-name" required></label>
          <label>Nom<input name="nom" autocomplete="family-name" required></label>
          <label>E-mail<input name="email" type="email" autocomplete="email" required></label>
          <label>Téléphone<input name="telephone" type="tel" autocomplete="tel"></label>
          <label class="large">Objet<select name="activite" id="activite"><option value="">Choisir</option>{opts}<option value="compte">Ouvrir un compte</option></select></label>
          <label class="large">Message<textarea name="message" rows="4" required></textarea></label>
          <label class="case large"><input type="checkbox" name="accord" required> J'accepte que Crown utilise ces informations pour me répondre.</label>
          <p class="large message-formulaire" role="status" aria-live="polite"></p>
          <div class="large"><button class="bouton bouton-plein" type="submit">Envoyer la demande</button><p class="note">Votre messagerie s'ouvre avec la demande prête à partir. Vous pouvez aussi écrire directement à <a href="mailto:{COURRIEL}">{COURRIEL}</a>.</p></div>
        </form>
        <dl class="coordonnees">
          <div><dt>Adresse</dt><dd>{ADRESSE}</dd></div>
          <div><dt>Contact</dt><dd><a href="mailto:{COURRIEL}">{COURRIEL}</a></dd></div>
          <div><dt>Investissements</dt><dd><a href="mailto:{COURRIEL_INVEST}">{COURRIEL_INVEST}</a></dd></div>
        </dl>
      </div>
    </div>
  </section>'''
ecrire("contact.html", page("", "Contact, Crown", "Demander une introduction à Crown.", "Contact", contact))

# ---------- Espace client ----------
espace = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Espace client, Crown</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#F20823">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Manrope:wght@200;300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/crown.css?v={VER['crown.css']}">
<script src="assets/crown.js?v={VER['crown.js']}" defer></script>
</head>
<body class="page-connexion">
<main class="connexion" id="contenu">
  <div class="connexion-embleme">{embleme(anime=False)}{logo("", "logo logo-blanc")}</div>
  <section class="connexion-forme">
    <a class="retour" href="index.html">← Retour au site</a>
    <div>
      <p class="surtitre">Espace client</p>
      <h1>Bienvenue chez<br><span class="titre-crown">CR<span class="o">O</span>WN</span></h1>
      <form class="formulaire formulaire-colonne" id="formulaire-connexion" method="post" action="#" novalidate data-a-relier data-message="L'espace client en ligne ouvre prochainement. Votre interlocuteur chez Crown reste joignable à {COURRIEL}.">
        <label class="large">E-mail<input name="email" type="email" autocomplete="username" required></label>
        <label class="large">Mot de passe<input name="mot_de_passe" type="password" autocomplete="current-password" required></label>
        <p class="large message-formulaire" role="status" aria-live="polite"></p>
        <div class="large ligne"><button class="bouton bouton-plein" type="submit">Se connecter</button><a href="#">Mot de passe oublié</a></div>
      </form>
      <p class="nouveau">Pas encore client ? <a href="contact.html?objet=compte">Ouvrir un compte →</a></p>
    </div>
  </section>
</main>
</body>
</html>
'''
ecrire("espace-client.html", espace)

# ---------- Page introuvable ----------
ecrire("404.html", page("", "Page introuvable, Crown", "Page introuvable.", "", f'''  <section class="intro apparait">
    <p class="surtitre">Erreur 404</p>
    <h1>Cette page n'existe pas.</h1>
    <p class="accroche"><a class="lien-fleche" href="/index.html">Revenir à l'accueil →</a></p>
  </section>''', "/"))

# ---------- Pages légales ----------
mentions = f'''  <section class="intro apparait">
    <p class="surtitre">Informations légales</p>
    <h1>Mentions légales</h1>
  </section>
  <section class="texte-legal">
    <h2>Éditeur du site</h2>
    <p>Le site crown.ooo est édité par CROWN FRANCE, société par actions simplifiée au capital de 12 176 001 euros, immatriculée au Registre national des entreprises sous le numéro SIREN 101 540 714. Numéro de TVA intracommunautaire : FR56 101 540 714.</p>
    <p>Siège : {ADRESSE}.<br>Contact : <a href="mailto:{COURRIEL}">{COURRIEL}</a>.</p>
    <h2>Directeur de la publication</h2>
    <p>Anthony Tchakerian, président de CROWN FRANCE.</p>
    <h2>Hébergement</h2>
    <p>Render Services, Inc., 525 Brannan Street, Suite 300, San Francisco, CA 94107, États-Unis (render.com).</p>
    <h2>Propriété intellectuelle</h2>
    <p>Les textes, le logo, la couronne et les illustrations de ce site appartiennent à Crown. Toute reproduction, même partielle, demande une autorisation écrite préalable.</p>
    <h2>Informations sur les investissements</h2>
    <p>Les informations publiées sur ce site sont données à titre indicatif. Elles ne constituent ni une offre, ni une sollicitation, ni un conseil en investissement. Tout investissement comporte un risque de perte en capital.</p>
  </section>'''
ecrire("mentions-legales.html", page("", "Mentions légales, Crown", "Mentions légales du site crown.ooo.", "", mentions))

confid = f'''  <section class="intro apparait">
    <p class="surtitre">Informations légales</p>
    <h1>Politique de confidentialité</h1>
  </section>
  <section class="texte-legal">
    <h2>En bref</h2>
    <p>Ce site ne dépose aucun cookie et ne mesure pas son audience. Il ne garde aucune donnée vous concernant. Les seules informations que nous recevons sont celles que vous nous envoyez par e-mail.</p>
    <h2>Responsable du traitement</h2>
    <p>CROWN FRANCE, SAS, SIREN 101 540 714, {ADRESSE}. Contact : <a href="mailto:{COURRIEL}">{COURRIEL}</a>.</p>
    <h2>Le formulaire de contact</h2>
    <p>Le formulaire n'envoie rien au site : il prépare un e-mail dans votre messagerie, que vous choisissez d'envoyer. Nous utilisons ce que vous nous écrivez uniquement pour vous répondre, et le conservons au plus trois ans après notre dernier échange.</p>
    <h2>Prestataires techniques</h2>
    <p>L'hébergeur, Render, enregistre des journaux techniques (adresse IP, pages demandées, date) pour assurer la sécurité du site. Les polices de caractères sont chargées depuis Google Fonts, qui reçoit à cette occasion l'adresse IP du visiteur. Ces deux prestataires peuvent traiter ces données hors de l'Union européenne.</p>
    <h2>Vos droits</h2>
    <p>Vous pouvez demander l'accès à vos données, leur rectification, leur effacement, la limitation de leur traitement ou vous y opposer, en écrivant à <a href="mailto:{COURRIEL}">{COURRIEL}</a>. Vous pouvez aussi adresser une réclamation à la CNIL (cnil.fr).</p>
  </section>'''
ecrire("confidentialite.html", page("", "Confidentialité, Crown", "Politique de confidentialité du site crown.ooo.", "", confid))

# ---------- Icône ----------
ecrire("assets/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="8" fill="#F20823"/><g transform="translate(4 6)" fill="none" stroke="#fff" stroke-width="2.4"><path d="M20 21.5 L4.2 21.5 L2 7.5 L12.5 14.5 L20 3 L27.5 14.5 L38 7.5 L35.8 21.5 Z" transform="scale(.8) translate(0 2)"/></g></svg>')
print("site construit dans", SITE)

# ---------- Grain photographique posé sur les scènes ----------
ecrire("assets/grain.svg", '<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 240 240"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="240" height="240" filter="url(#g)"/></svg>')
