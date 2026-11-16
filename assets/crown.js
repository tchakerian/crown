// Crown : petits comportements du site (menu, apparitions, formulaires)
(function () {
  'use strict';
  var racine = document.documentElement;
  racine.classList.add('js');

  // Menu sur téléphone
  var bouton = document.querySelector('.menu-bouton');
  var menu = document.getElementById('menu');
  if (bouton && menu) {
    var fermer = function () {
      menu.classList.remove('ouvert');
      bouton.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    };
    bouton.addEventListener('click', function () {
      var ouvert = menu.classList.toggle('ouvert');
      bouton.setAttribute('aria-expanded', String(ouvert));
      document.body.style.overflow = ouvert ? 'hidden' : '';
    });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) fermer(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') fermer(); });
  }

  // Ombre de l'en-tête au défilement ; à l'accueil, l'en-tête se pose sur la scène puis se fixe en haut
  var entete = document.querySelector('.entete');
  var scene = document.querySelector('.voile');
  if (entete) {
    var surveiller = function () {
      entete.classList.toggle('ombre', window.scrollY > 40);
      if (scene) entete.classList.toggle('colle', window.scrollY > scene.offsetHeight - 80);
    };
    window.addEventListener('scroll', surveiller, { passive: true });
    surveiller();
  }

  // Accueil : les quatre activités défilent, 8 secondes chacune, avec pause
  if (scene) {
    var diapos = scene.querySelectorAll('.diapo');
    var onglets = scene.querySelectorAll('.onglet');
    var noms = Array.prototype.map.call(onglets, function (o) { return o.querySelector('.onglet-nom').textContent; });
    var compteur = scene.querySelector('.compteur');
    var numero = scene.querySelector('.compteur-n');
    var suivante = scene.querySelector('.suivante-nom');
    var pause = scene.querySelector('.voile-pause');
    var calme = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var actif = 0, arrete = calme, survol = false;
    var montrer = function (n) {
      actif = (n + diapos.length) % diapos.length;
      diapos.forEach(function (d, i) {
        var on = i === actif;
        d.classList.toggle('actif', on);
        if (on) d.removeAttribute('aria-hidden'); else d.setAttribute('aria-hidden', 'true');
        d.querySelectorAll('a').forEach(function (a) { if (on) a.removeAttribute('tabindex'); else a.setAttribute('tabindex', '-1'); });
      });
      onglets.forEach(function (o, i) {
        o.classList.remove('actif');
        if (i === actif) { void o.offsetWidth; o.classList.add('actif'); }
      });
      scene.setAttribute('data-actif', String(actif));
      numero.textContent = '0' + (actif + 1);
      compteur.setAttribute('data-nom', noms[actif]);
      if (suivante) suivante.textContent = noms[(actif + 1) % noms.length];
    };
    var etat = function () {
      scene.classList.toggle('en-pause', arrete || survol);
      pause.setAttribute('aria-label', arrete ? 'Reprendre le défilement' : 'Mettre le défilement en pause');
    };
    onglets.forEach(function (o, i) {
      o.querySelector('.onglet-prog').addEventListener('animationend', function () {
        if (i === actif && !arrete && !survol) montrer(actif + 1);
      });
      o.addEventListener('mouseenter', function () { if (i !== actif) montrer(i); });
      o.addEventListener('focus', function () { if (i !== actif) montrer(i); });
    });
    scene.querySelector('.voile-contenu').addEventListener('mouseenter', function () { survol = true; etat(); });
    scene.querySelector('.voile-contenu').addEventListener('mouseleave', function () { survol = false; etat(); });
    pause.addEventListener('click', function () { arrete = !arrete; etat(); });
    if (calme) pause.hidden = true;
    montrer(0);
    etat();
  }

  // Apparition des sections
  var blocs = document.querySelectorAll('.revele');
  if ('IntersectionObserver' in window) {
    var obs = new IntersectionObserver(function (entrees) {
      entrees.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('vu'); obs.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
    blocs.forEach(function (b) { obs.observe(b); });
  } else {
    blocs.forEach(function (b) { b.classList.add('vu'); });
  }

  // Formulaire de contact : objet prérempli depuis l'adresse
  var params = new URLSearchParams(window.location.search);
  var choix = document.getElementById('activite');
  if (choix) {
    var voulu = params.get('activite') || params.get('objet');
    if (voulu && choix.querySelector('option[value="' + voulu.replace(/[^a-z-]/g, '') + '"]')) choix.value = voulu;
  }

  // Formulaires : vérification avant envoi. Ils ne sont pas encore reliés à un service d'envoi.
  document.querySelectorAll('form[data-a-relier]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var message = f.querySelector('.message-formulaire');
      var premier = null;
      f.querySelectorAll('[required]').forEach(function (c) {
        var ok = c.type === 'checkbox' ? c.checked : c.value.trim() !== '' && (!c.validity || c.validity.valid);
        c.setAttribute('aria-invalid', ok ? 'false' : 'true');
        if (!ok && !premier) premier = c;
      });
      if (premier) {
        if (message) message.textContent = 'Merci de compléter les champs indiqués.';
        premier.focus();
        return;
      }
      if (message) message.textContent = "Ce formulaire n'est pas encore relié : votre demande n'a pas été envoyée.";
    });
  });
})();
