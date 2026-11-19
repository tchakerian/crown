# Relais : CROWN

Passation entre les deux comptes d'Anthony (compte sesterce et `[ ... ]`). Une seule session
travaille à la fois ; le cadenas en tête de `REPRISE.md` dit laquelle.

## SORTIE (la session qui rend la main)

1. `python3 outils/construire.py`, puis `git status` : rien ne doit rester en suspens.
2. Mettre `REPRISE.md` à jour : état, reste à faire, ce qui attend Anthony, une ligne au journal.
3. Remplacer le cadenas par : `🔓 Libre · CROWN · rendu par <compte> le JJ/MM HH:MM`.
4. Envoyer sur `main` **seulement avec l'accord d'Anthony** (auteur
   `tchakerian <175748602+tchakerian@users.noreply.github.com>`, jamais de force push).
   Un envoi ne publie rien : la mise en ligne Render reste manuelle.
5. Donner à Anthony le message à coller ci-dessous, rempli.

## ENTRÉE (la session qui prend la main)

1. `git pull` sur `main`, lire `CLAUDE.md`, `REPRISE.md`, puis `git log -10`.
2. Vérifier le cadenas : s'il dit « Occupé » par une autre session, s'arrêter et demander à Anthony.
3. Poser le cadenas : `🔒 Occupé · CROWN · <compte> · depuis le JJ/MM HH:MM`.
4. `python3 outils/construire.py` : le générateur doit tourner sans écart.
5. Dire à Anthony en 3 à 5 lignes où en est le site, puis attendre ses consignes.

## Cadenas

- Libre : `🔓 Libre · CROWN · rendu par <compte> le JJ/MM HH:MM`
- Occupé : `🔒 Occupé · CROWN · <compte> · depuis le JJ/MM HH:MM`

Le cadenas ne part sur `main` qu'avec l'accord d'Anthony, comme tout le reste.

## Message à coller dans la nouvelle session

```
Je reprends ici. Tu es la conversation CROWN : le site de la maison Crown (crown.ooo),
dépôt tchakerian/crown (public), séparé de Sesterce. Passe par le skill ceo d'abord ;
pour le format, les règles du dépôt priment (court, en français, le résultat d'abord).

Suis l'ENTRÉE de RELAIS.md : lire CLAUDE.md et REPRISE.md, poser le cadenas, lancer
python3 outils/construire.py, me dire où en est le site en 3 à 5 lignes, puis attendre.

Dernier envoi sur main : <empreinte> du <JJ/MM HH:MM> (<objet>).
Rien ne part sur main sans mon accord ; la mise en ligne Render est manuelle.
```
