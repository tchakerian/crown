# Scènes des activités, dessinées en SVG dans l'esprit du voilier de l'accueil.
# Toutes partagent le même cadre (1440 x 1024), le même ciel gris et un sujet placé à droite,
# entre x = 960 et x = 1440, pour rester visible sur téléphone et dans le cadre 4/5 des pages.
import math, random

LARGEUR, HAUTEUR = 1440, 1024


def _flou(p, ecart):
    return f'<filter id="{p}-flou{ecart}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="{ecart}"/></filter>'


def _vague(y, a):
    return "M0 %d Q60 %d 120 %d %s" % (y, y - a, y, " ".join("T%d %d" % (x, y) for x in range(240, 1700, 120)))


# ---------- Outils communs ----------
def _bord(p, nom, freq, echelle, graine=3):
    """Bord naturel : déforme légèrement une forme (feuillage, collines, nuages)."""
    return (f'<filter id="{p}-{nom}" x="-20%" y="-20%" width="140%" height="140%">'
            f'<feTurbulence type="fractalNoise" baseFrequency="{freq}" numOctaves="3" seed="{graine}" result="b"/>'
            f'<feDisplacementMap in="SourceGraphic" in2="b" scale="{echelle}" xChannelSelector="R" yChannelSelector="G"/></filter>')


def _amas(cx, cy, rx, ry, n, rmin, rmax, graine, haut=.75):
    """Un amas de ronds en ellipse, plus dense en haut : feuillage d'arbre."""
    r = random.Random(graine)
    out = f'<ellipse cx="{cx}" cy="{cy}" rx="{rx * .8:.0f}" ry="{ry * .75:.0f}"/>'
    for _ in range(n):
        a = r.uniform(math.pi, 2 * math.pi) if r.random() < haut else r.uniform(0, math.pi)
        d = r.uniform(.45, 1)
        out += f'<circle cx="{cx + rx * d * math.cos(a):.0f}" cy="{cy + ry * d * math.sin(a):.0f}" r="{r.uniform(rmin, rmax):.0f}"/>'
    return out


# ---------- I. Demeure : une villa à l'heure bleue, pins parasols, cyprès et piscine ----------
def _cypres(x, base, h, l):
    return (f'M{x} {base} C{x - l} {base - h * .26:.0f} {x - l * .6:.0f} {base - h * .8:.0f} {x} {base - h} '
            f'C{x + l * .6:.0f} {base - h * .8:.0f} {x + l} {base - h * .26:.0f} {x} {base} Z')


def demeure(p="d"):
    fx = [1072 + 42 * k for k in range(6)]  # fenêtres de la façade principale
    haut = ''.join(f'<rect x="{x}" y="488" width="16" height="34"/>' for x in fx)
    bas = ''.join(f'<path d="M{x - 1} 596 V547 A9 9 0 0 1 {x + 17} 547 V596 Z"/>' for x in fx)
    volets = ''.join(f'<rect x="{x - 8}" y="487" width="6" height="36"/><rect x="{x + 18}" y="487" width="6" height="36"/>'
                     f'<rect x="{x - 9}" y="539" width="6" height="57"/><rect x="{x + 19}" y="539" width="6" height="57"/>' for x in fx)
    cote = ''.join(f'<path d="M{x} {y0 + (x - 1310) * .1:.1f} L{x + 12} {y0 + (x + 12 - 1310) * .1:.1f} L{x + 12} {y0 + h - (x + 12 - 1310) * .07:.1f} L{x} {y0 + h - (x - 1310) * .07:.1f} Z"/>'
                   for x in (1326, 1360) for y0, h in ((490, 32), (546, 46)))
    fenetres = haut + bas
    balustres = ''.join(f'<rect x="{x}" y="603" width="3" height="10" rx="1.2"/>' for x in range(986, 1440, 9))
    flaques = ''.join(f'<ellipse cx="{x + 8}" cy="606" rx="26" ry="5"/>' for x in fx)
    lumieres = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(96, 598, 1.4), (132, 594, 1.1), (150, 600, 1.6), (386, 610, 1.2), (420, 606, 1.5), (702, 618, 1.3), (736, 612, 1.1), (770, 620, 1.6)])
    pins = (_amas(952, 434, 140, 30, 90, 8, 18, 21) + _amas(1012, 454, 70, 18, 40, 7, 14, 22)
            + _amas(808, 548, 74, 16, 50, 6, 12, 23))
    return f'''<defs>
        <linearGradient id="{p}-ciel" x1="0" y1="0" x2="0" y2="640" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#0A1015"/><stop offset=".38" stop-color="#1D2A35"/><stop offset=".7" stop-color="#4A5A66"/><stop offset=".86" stop-color="#8E8580"/><stop offset=".95" stop-color="#C79E7E"/><stop offset="1" stop-color="#D9AE86"/></linearGradient>
        <radialGradient id="{p}-lum" cx="520" cy="630" r="760" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#F6BE8C" stop-opacity=".55"/><stop offset=".3" stop-color="#D59C78" stop-opacity=".2"/><stop offset="1" stop-color="#D59C78" stop-opacity="0"/></radialGradient>
        <linearGradient id="{p}-mont1" x1="0" y1="540" x2="0" y2="640" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#6C7378"/><stop offset="1" stop-color="#8D8682"/></linearGradient>
        <linearGradient id="{p}-mont2" x1="0" y1="570" x2="0" y2="660" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#3D4850"/><stop offset="1" stop-color="#4E5459"/></linearGradient>
        <linearGradient id="{p}-sol" x1="0" y1="600" x2="0" y2="1024" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#1F282D"/><stop offset=".25" stop-color="#11181C"/><stop offset="1" stop-color="#06090B"/></linearGradient>
        <linearGradient id="{p}-facade" x1="0" y1="470" x2="0" y2="600" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#C9BFAE"/><stop offset=".55" stop-color="#ABA08F"/><stop offset="1" stop-color="#8A7D6C"/></linearGradient>
        <linearGradient id="{p}-cote" x1="1310" y1="0" x2="1400" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#7E7568"/><stop offset="1" stop-color="#5C564E"/></linearGradient>
        <linearGradient id="{p}-toit" x1="0" y1="440" x2="0" y2="474" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#6A5850"/><stop offset="1" stop-color="#3B302B"/></linearGradient>
        <linearGradient id="{p}-vitre" x1="0" y1="486" x2="0" y2="598" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFE7BC"/><stop offset=".5" stop-color="#F9C786"/><stop offset="1" stop-color="#EE9F58"/></linearGradient>
        <linearGradient id="{p}-mur" x1="0" y1="612" x2="0" y2="648" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#6E655A"/><stop offset="1" stop-color="#2A2724"/></linearGradient>
        <linearGradient id="{p}-eau" x1="0" y1="650" x2="0" y2="740" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#6F8790"/><stop offset=".4" stop-color="#3D5560"/><stop offset="1" stop-color="#16242B"/></linearGradient>
        <linearGradient id="{p}-cyp" x1="0" y1="380" x2="0" y2="640" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#0B1012"/><stop offset=".75" stop-color="#151A19"/><stop offset="1" stop-color="#3E3326"/></linearGradient>
        <clipPath id="{p}-bassin"><path d="M930 742 L1440 742 L1440 652 L968 652 Z"/></clipPath>
        {_flou(p, 2)}{_flou(p, 6)}{_flou(p, 14)}{_flou(p, 30)}
        {_bord(p, "colline", ".012", 16, 4)}{_bord(p, "feuille", ".14", 11, 8)}{_bord(p, "fin", ".09", 5, 2)}
        <filter id="{p}-onde" x="0" y="-10%" width="100%" height="120%"><feTurbulence type="fractalNoise" baseFrequency=".004 .09" numOctaves="2" seed="5" result="b"/><feDisplacementMap in="SourceGraphic" in2="b" scale="16" xChannelSelector="R" yChannelSelector="G"/><feGaussianBlur stdDeviation="1.2"/></filter>
      </defs>
      <rect width="1440" height="660" fill="url(#{p}-ciel)"/>
      <circle class="brume" cx="520" cy="630" r="760" fill="url(#{p}-lum)"/>
      <g class="nuages" filter="url(#{p}-flou6)">
        <ellipse cx="300" cy="120" rx="640" ry="60" fill="#0A0F13" opacity=".7"/><ellipse cx="1180" cy="86" rx="560" ry="70" fill="#0A0E12" opacity=".7"/>
        <ellipse cx="820" cy="300" rx="520" ry="14" fill="#2B3843" opacity=".7"/><ellipse cx="840" cy="306" rx="480" ry="5" fill="#B88F78" opacity=".35"/>
        <ellipse cx="260" cy="430" rx="420" ry="9" fill="#9C8578" opacity=".35"/><ellipse cx="1220" cy="400" rx="330" ry="8" fill="#5D6268" opacity=".5"/>
      </g>
      <circle cx="380" cy="214" r="1.3" fill="#F2F0EA" opacity=".8"/><circle cx="1040" cy="178" r="1" fill="#F2F0EA" opacity=".6"/><circle cx="640" cy="152" r="1.1" fill="#F2F0EA" opacity=".5"/>
      <path filter="url(#{p}-colline)" fill="url(#{p}-mont1)" d="M-40 600 C80 570 160 548 260 556 C340 562 400 540 480 532 C560 524 620 552 700 566 C800 584 900 560 1000 550 C1100 540 1200 556 1480 580 L1480 680 L-40 680 Z"/>
      <ellipse cx="560" cy="604" rx="700" ry="20" fill="#D9C2AA" opacity=".18" filter="url(#{p}-flou14)"/>
      <path filter="url(#{p}-colline)" fill="url(#{p}-mont2)" d="M-40 628 C120 610 240 604 360 614 C480 624 560 618 660 608 C760 598 860 604 940 616 L940 700 L-40 700 Z"/>
      <g fill="#F7C98E">{lumieres}</g>
      <g fill="#F7C98E" opacity=".5" filter="url(#{p}-flou2)">{lumieres}</g>
      <path fill="url(#{p}-sol)" d="M-40 650 C180 640 420 642 640 650 C760 654 860 634 940 612 L1480 600 L1480 1060 L-40 1060 Z"/>
      <g fill="#0E1416" filter="url(#{p}-feuille)">
        <path d="M812 560 C814 576 816 590 816 612 L822 612 C821 590 820 574 818 560 Z"/>
        {pins}
      </g>
      <path fill="#0E1416" d="M934 640 C940 600 944 540 950 470 C952 456 958 446 962 440 L966 442 C962 452 958 466 958 480 C954 540 948 600 946 640 Z M956 470 C940 458 920 452 900 446 L902 442 C924 446 944 452 960 464 Z M958 462 C980 456 1000 454 1020 452 L1020 456 C1000 458 982 462 962 468 Z"/>
      <g>
        <path fill="url(#{p}-cote)" d="M1310 472 L1394 482 L1394 594 L1310 602 Z"/>
        <rect x="1050" y="472" width="260" height="130" fill="url(#{p}-facade)"/>
        <rect x="1050" y="532" width="260" height="3" fill="#D8CEBE" opacity=".8"/><path d="M1310 532 L1394 538 L1394 541 L1310 535 Z" fill="#9C9284" opacity=".8"/>
        <rect x="1050" y="472" width="8" height="130" fill="#D2C7B6" opacity=".6"/><rect x="1302" y="472" width="8" height="130" fill="#D2C7B6" opacity=".45"/>
        <path fill="url(#{p}-toit)" d="M1040 474 L1320 474 L1286 444 L1088 444 Z"/>
        <path fill="#2A221F" d="M1320 474 L1402 484 L1374 464 L1286 444 Z"/>
        <rect x="1040" y="471" width="281" height="4" fill="#E2D8C8"/><path d="M1320 471 L1402 481 L1402 485 L1320 475 Z" fill="#A69C8E"/>
        <rect x="1118" y="426" width="12" height="22" fill="#4A3E38"/><rect x="1246" y="426" width="12" height="22" fill="#4A3E38"/>
        <g fill="#56635D" opacity=".9">{volets}</g>
        <g class="lueur" fill="#F6B064" filter="url(#{p}-flou6)">{fenetres}</g>
        <g fill="url(#{p}-vitre)">{fenetres}</g>
        <g fill="#2E2A26" opacity=".35">{''.join(f'<rect x="{x + 7}" y="488" width="2" height="34"/><rect x="{x}" y="504" width="16" height="2"/><rect x="{x + 7}" y="540" width="2" height="56"/>' for x in fx)}</g>
        <g fill="#E9B477" opacity=".75">{cote}</g>
        <g class="lueur" fill="#F7B46A" opacity=".55" filter="url(#{p}-flou14)">{flaques}</g>
        <rect x="980" y="600" width="460" height="4" fill="#DCD2C2"/>
        <g fill="#BDB2A2" opacity=".85">{balustres}</g>
        <rect x="980" y="612" width="460" height="4" fill="#CFC5B5" opacity=".9"/>
        <rect x="980" y="616" width="460" height="34" fill="url(#{p}-mur)"/>
      </g>
      <g fill="url(#{p}-cyp)" filter="url(#{p}-fin)"><path d="{_cypres(1020, 616, 200, 17)}"/><path d="{_cypres(1416, 616, 250, 21)}"/><path d="{_cypres(1446, 616, 196, 18)}"/><path d="{_cypres(870, 640, 118, 10)}"/></g>
      <g fill="#F2B470" opacity=".5" filter="url(#{p}-flou14)"><ellipse cx="1020" cy="612" rx="16" ry="40"/><ellipse cx="1416" cy="610" rx="18" ry="46"/></g>
      <path fill="url(#{p}-eau)" d="M930 742 L1440 742 L1440 652 L968 652 Z"/>
      <g clip-path="url(#{p}-bassin)"><g filter="url(#{p}-onde)" opacity=".7">
        <g transform="translate(0 1252) scale(1 -1)">
          <rect x="1050" y="472" width="260" height="130" fill="#8F8576" opacity=".35"/>
          <g fill="url(#{p}-vitre)">{fenetres}</g>
        </g>
      </g></g>
      <path d="M968 652.5 L1440 652.5" stroke="#E6DED0" stroke-width="1.6" opacity=".7"/>
      <path fill="#0B1012" d="M-40 790 C200 770 520 764 760 772 C880 776 980 754 1060 748 L1480 744 L1480 1060 L-40 1060 Z"/>
      <g fill="#05080A" opacity=".85" filter="url(#{p}-feuille)">{_amas(1150, 820, 210, 22, 60, 8, 16, 51)}{_amas(1400, 812, 120, 20, 40, 8, 15, 52)}</g>'''


# ---------- II. Stable : prairie à l'aube, chevaux, chêne et clôture ----------
CHEVAL = ("M14 54 C10 50 8 46 12 42 L28 16 L32 5 L36 13 L40 3 L45 14 C60 22 78 38 96 50 C110 56 122 60 136 58 "
          "C150 56 162 52 172 56 C178 58 182 64 184 72 C189 90 191 110 187 130 L181 129 C181 108 179 92 177 80 "
          "C177 90 175 98 171 104 L173 122 L171 145 L175 152 L163 152 L163 145 L163 124 C159 114 155 106 150 102 "
          "C140 106 112 106 98 102 L97 124 L95 145 L99 152 L87 152 L87 145 L86 122 L84 106 L79 112 L77 145 L81 152 "
          "L69 152 L69 145 L71 114 C69 102 67 92 64 84 C58 74 50 64 42 59 C36 59 28 61 22 61 C18 61 15 58 14 54 Z")
CHEVAL_PATTE = "M150 104 L153 124 L151 145 L155 152 L143 152 L143 145 L143 124 L141 106 Z"
CHEVAL_CRINIERE = "M44 13 C58 18 74 30 92 44 C80 40 66 32 56 26 C50 22 46 18 44 13 Z"
CHEVAL_BROUTE = ("M8 128 C4 126 3 121 6 118 L22 92 C28 74 36 60 50 50 L54 42 L56 50 L60 41 L62 51 C76 48 96 50 110 54 "
                 "C124 58 140 58 154 56 C166 54 176 56 182 64 C186 80 188 104 184 126 L178 125 C179 106 177 92 175 82 "
                 "C175 92 173 100 169 106 L171 124 L169 145 L173 152 L161 152 L161 145 L161 126 C157 116 153 108 148 104 "
                 "C138 108 112 108 98 104 L97 124 L95 145 L99 152 L87 152 L87 145 L86 124 L83 108 L78 114 L76 145 L80 152 "
                 "L68 152 L68 145 L70 114 C66 104 60 96 54 90 C46 100 36 114 28 124 C22 130 14 131 8 128 Z")


def stable(p="s"):
    rnd = random.Random(11)
    herbes = ''.join(f'<path d="M{x:.0f} {y:.0f} q{rnd.uniform(-3, 3):.1f} -{rnd.uniform(8, 16):.0f} {rnd.uniform(-7, 7):.1f} -{rnd.uniform(16, 34):.0f}"/>'
                     for x, y in [(rnd.uniform(-20, 1460), rnd.uniform(900, 1030)) for _ in range(140)])
    rosee = ''.join(f'<circle cx="{rnd.uniform(0, 1440):.0f}" cy="{rnd.uniform(720, 900):.0f}" r="{rnd.uniform(.6, 1.4):.1f}" opacity="{rnd.uniform(.2, .6):.2f}"/>' for _ in range(60))
    piquets, ombres = '', ''
    for k in range(13):
        t = k / 12
        x = 820 + 640 * t ** 1.18
        y = 692 + 160 * t ** 1.35
        h = 16 + 62 * t ** 1.35
        w = 1.8 + 4.6 * t
        piquets += f'<rect x="{x:.1f}" y="{y - h:.1f}" width="{w:.1f}" height="{h + 2:.1f}" rx="{w / 4:.1f}"/>'
        ombres += f'<rect x="{x + w * .55:.1f}" y="{y - h:.1f}" width="{w * .45:.1f}" height="{h + 2:.1f}"/>'
    def lisse(d):
        return "M820 %.1f C1020 %.1f 1240 %.1f 1460 %.1f" % (692 - 12 * d, 716 - 24 * d, 770 - 42 * d, 856 - 60 * d)
    feuillage = _amas(1282, 464, 150, 96, 220, 9, 22, 31)
    clair = _amas(1210, 440, 76, 60, 70, 7, 15, 32, haut=.9)
    rayons = ''.join(f'<path d="M620 588 L{620 + 1400 * math.cos(a):.0f} {588 + 1400 * math.sin(a):.0f} L{620 + 1400 * math.cos(a + .035):.0f} {588 + 1400 * math.sin(a + .035):.0f} Z"/>'
                     for a in (-2.9, -2.62, -2.3, -1.95, -1.4, -1.05, -.72, -.44, -.2))
    return f'''<defs>
        <linearGradient id="{p}-ciel" x1="0" y1="0" x2="0" y2="640" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#10171C"/><stop offset=".4" stop-color="#34414A"/><stop offset=".72" stop-color="#7D8784"/><stop offset=".9" stop-color="#C6B596"/><stop offset="1" stop-color="#E4CBA2"/></linearGradient>
        <radialGradient id="{p}-lum" cx="620" cy="590" r="760" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FBE3BC" stop-opacity=".75"/><stop offset=".2" stop-color="#F0D1A6" stop-opacity=".3"/><stop offset="1" stop-color="#E2C9A6" stop-opacity="0"/></radialGradient>
        <linearGradient id="{p}-loin" x1="0" y1="560" x2="0" y2="640" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#8F938A"/><stop offset="1" stop-color="#A9A493"/></linearGradient>
        <linearGradient id="{p}-mi" x1="0" y1="600" x2="0" y2="700" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#55605C"/><stop offset="1" stop-color="#3C4643"/></linearGradient>
        <linearGradient id="{p}-pre" x1="0" y1="640" x2="0" y2="1024" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#3B4642"/><stop offset=".3" stop-color="#1E2725"/><stop offset="1" stop-color="#070B0B"/></linearGradient>
        <radialGradient id="{p}-pre-lum" cx="620" cy="660" r="700" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#E9CFA4" stop-opacity=".28"/><stop offset="1" stop-color="#E9CFA4" stop-opacity="0"/></radialGradient>
        {_flou(p, 4)}{_flou(p, 10)}{_flou(p, 22)}{_flou(p, 40)}
        {_bord(p, "colline", ".01", 14, 6)}{_bord(p, "feuille", ".12", 13, 9)}{_bord(p, "herbe", ".06", 8, 12)}
      </defs>
      <rect width="1440" height="680" fill="url(#{p}-ciel)"/>
      <circle class="brume" cx="620" cy="590" r="760" fill="url(#{p}-lum)"/>
      <g fill="#FFF1D6" opacity=".05" filter="url(#{p}-flou10)">{rayons}</g>
      <g class="nuages" filter="url(#{p}-flou10)">
        <ellipse cx="420" cy="110" rx="640" ry="58" fill="#0F151A" opacity=".6"/><ellipse cx="1160" cy="168" rx="500" ry="40" fill="#1A2227" opacity=".55"/><ellipse cx="900" cy="380" rx="460" ry="10" fill="#D8C6A8" opacity=".28"/>
        <ellipse cx="220" cy="470" rx="320" ry="8" fill="#C9B898" opacity=".3"/>
      </g>
      <circle cx="620" cy="582" r="26" fill="#FFF3DC" opacity=".9" filter="url(#{p}-flou4)"/>
      <circle cx="620" cy="582" r="90" fill="#FBE0B4" opacity=".35" filter="url(#{p}-flou22)"/>
      <path filter="url(#{p}-colline)" fill="url(#{p}-loin)" opacity=".85" d="M-40 600 C120 584 260 572 420 586 C540 596 640 596 760 584 C900 570 1060 560 1220 568 C1320 572 1400 578 1480 584 L1480 680 L-40 680 Z"/>
      <ellipse class="derive" cx="560" cy="606" rx="760" ry="22" fill="#F1E6D2" opacity=".42" filter="url(#{p}-flou22)"/>
      <path filter="url(#{p}-colline)" fill="url(#{p}-mi)" d="M-40 640 C140 622 320 618 500 630 C680 642 840 630 980 616 C1140 600 1300 604 1480 612 L1480 720 L-40 720 Z"/>
      <g fill="#262E2D" filter="url(#{p}-feuille)">{_amas(160, 618, 60, 18, 14, 8, 14, 41)}{_amas(330, 624, 40, 14, 10, 7, 12, 42)}{_amas(1020, 606, 50, 14, 12, 8, 13, 43)}</g>
      <g fill="#10171A">
        <path d="M1272 604 C1274 576 1270 548 1262 520 C1250 500 1230 488 1210 480 L1214 474 C1236 482 1254 492 1266 506 C1268 486 1278 470 1296 458 L1300 464 C1286 476 1280 494 1282 512 C1292 500 1312 492 1334 488 L1336 494 C1314 500 1298 510 1288 526 C1286 556 1288 580 1294 604 Z"/>
      </g>
      <g filter="url(#{p}-feuille)">
        <g fill="#121A1C">{feuillage}</g>
        <g fill="#3B3F36" opacity=".55">{clair}</g>
      </g>
      <ellipse class="derive2" cx="900" cy="664" rx="820" ry="26" fill="#E6E0D2" opacity=".26" filter="url(#{p}-flou22)"/>
      <path filter="url(#{p}-herbe)" fill="url(#{p}-pre)" d="M-40 694 C240 666 520 664 760 674 C960 682 1140 652 1300 642 C1360 638 1420 638 1480 640 L1480 1060 L-40 1060 Z"/>
      <path fill="url(#{p}-pre-lum)" d="M-40 694 C240 666 520 664 760 674 C960 682 1140 652 1300 642 C1360 638 1420 638 1480 640 L1480 1060 L-40 1060 Z"/>
      <ellipse cx="1000" cy="740" rx="110" ry="6" fill="#05090A" opacity=".5" filter="url(#{p}-flou4)"/>
      <g>
        <g transform="translate(958 606) scale(-.5 .5)"><path d="{CHEVAL_BROUTE}" fill="none" stroke="#E9C695" stroke-width="5" opacity=".45" transform="translate(-2 -2)"/><path d="{CHEVAL_BROUTE}" fill="#0D1315"/></g>
        <g transform="translate(1012 584) scale(.92)">
          <path d="{CHEVAL}" fill="none" stroke="#EDCB9A" stroke-width="3.2" opacity=".55" transform="translate(-2.2 -1.6)"/>
          <path d="{CHEVAL_PATTE}" fill="#080C0D"/><path d="{CHEVAL}" fill="#0D1315"/>
          <path d="{CHEVAL_CRINIERE}" fill="#060909"/>
          <path d="M70 60 C80 52 96 54 120 60 C100 62 84 64 74 70 Z" fill="#2A2C27" opacity=".55"/>
        </g>
      </g>
      <g fill="#E4E2D9" opacity=".82">{piquets}</g>
      <g fill="#6E6E66" opacity=".55">{ombres}</g>
      <g fill="none" stroke="#E4E2D9" stroke-linecap="round" opacity=".78"><path stroke-width="2.6" d="{lisse(0)}"/><path stroke-width="2.6" d="{lisse(1)}"/></g>
      <g fill="none" stroke="#5C5D57" stroke-linecap="round" opacity=".5"><path stroke-width="1.2" d="{lisse(-.08)}"/><path stroke-width="1.2" d="{lisse(.92)}"/></g>
      <g fill="#F3E3C6">{rosee}</g>
      <g fill="none" stroke="#070B0B" stroke-width="2.2" stroke-linecap="round" filter="url(#{p}-herbe)">{herbes}</g>'''


# ---------- III. Capital : la Terre vue de l'orbite, au lever du soleil ----------
def capital(p="c"):
    cx, cy, R = 900, 2620, 2060
    rnd = random.Random(7)
    limbe_y = lambda x, r=R: cy - math.sqrt(max(r * r - (x - cx) ** 2, 0))
    etoiles = ''
    for _ in range(260):
        x, y = rnd.uniform(0, 1440), rnd.uniform(0, 600)
        if y > limbe_y(x) - 40:
            continue
        r = rnd.choice([.5, .6, .7, .8, 1, 1.3, 1.7])
        etoiles += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" opacity="{rnd.uniform(.15, .85):.2f}"/>'
    villes = ''
    for _ in range(26):  # foyers de lumière sur la face encore dans la nuit
        bx, by = rnd.uniform(160, 1000), rnd.uniform(0, 1)
        y0 = limbe_y(bx) + 30 + by * 300
        for _ in range(rnd.randint(4, 14)):
            villes += f'<circle cx="{bx + rnd.gauss(0, 14):.0f}" cy="{y0 + rnd.gauss(0, 3 + by * 6):.0f}" r="{rnd.uniform(.5, 1.3):.1f}"/>'

    def arc(x1, x2, r=R):
        return f'M{x1} {limbe_y(x1, r):.1f} A{r} {r} 0 0 1 {x2} {limbe_y(x2, r):.1f}'
    sx, sy = 1180, limbe_y(1180)
    return f'''<defs>
        <linearGradient id="{p}-nuit" x1="0" y1="0" x2="0" y2="620" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#020305"/><stop offset=".8" stop-color="#070C11"/><stop offset="1" stop-color="#0E1820"/></linearGradient>
        <radialGradient id="{p}-terre" cx="{sx}" cy="{sy:.0f}" r="1250" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#6F8E9C"/><stop offset=".08" stop-color="#3D5968"/><stop offset=".3" stop-color="#18262F"/><stop offset=".6" stop-color="#0A1015"/><stop offset="1" stop-color="#040608"/></radialGradient>
        <linearGradient id="{p}-limbe" x1="0" y1="0" x2="1440" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#4E86B8" stop-opacity="0"/><stop offset=".4" stop-color="#5B95C6" stop-opacity=".35"/><stop offset=".78" stop-color="#9FD0F0" stop-opacity="1"/><stop offset="1" stop-color="#7FB4DA" stop-opacity=".6"/></linearGradient>
        <linearGradient id="{p}-aube" x1="860" y1="0" x2="1440" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#F08A4A" stop-opacity="0"/><stop offset=".55" stop-color="#F9B36E" stop-opacity="1"/><stop offset="1" stop-color="#F08A4A" stop-opacity=".1"/></linearGradient>
        <radialGradient id="{p}-soleil" cx="{sx}" cy="{sy:.0f}" r="520" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFE9C8" stop-opacity=".75"/><stop offset=".18" stop-color="#F8C894" stop-opacity=".25"/><stop offset="1" stop-color="#F8C894" stop-opacity="0"/></radialGradient>
        <clipPath id="{p}-sol"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath>
        <filter id="{p}-nuees" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".004 .022" numOctaves="4" seed="9"/><feColorMatrix type="matrix" values="0 0 0 0 .78  0 0 0 0 .86  0 0 0 0 .9  0 0 0 2.6 -1.35"/></filter>
        <radialGradient id="{p}-nuees-masque" cx="{sx}" cy="{sy:.0f}" r="760" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset=".55" stop-color="#fff" stop-opacity=".25"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
        <mask id="{p}-masque"><rect width="1440" height="1024" fill="url(#{p}-nuees-masque)"/></mask>
        {_flou(p, 1)}{_flou(p, 2)}{_flou(p, 5)}{_flou(p, 12)}{_flou(p, 30)}
      </defs>
      <rect width="1440" height="1024" fill="url(#{p}-nuit)"/>
      <g fill="#E8EEF2" class="scintille">{etoiles}</g>
      <circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#{p}-terre)"/>
      <g clip-path="url(#{p}-sol)"><rect y="540" width="1440" height="484" filter="url(#{p}-nuees)" mask="url(#{p}-masque)" opacity=".55"/></g>
      <g clip-path="url(#{p}-sol)" fill="#FFC27A">{villes}</g>
      <g clip-path="url(#{p}-sol)" fill="#FFB060" opacity=".6" filter="url(#{p}-flou2)">{villes}</g>
      <path d="{arc(80, 1440, R + 14)}" fill="none" stroke="url(#{p}-limbe)" stroke-width="34" opacity=".28" filter="url(#{p}-flou12)"/>
      <path d="{arc(80, 1440, R + 5)}" fill="none" stroke="url(#{p}-limbe)" stroke-width="7" opacity=".9" filter="url(#{p}-flou2)"/>
      <path d="{arc(80, 1440, R + 1)}" fill="none" stroke="#CFE8F8" stroke-width="1.2" opacity=".55"/>
      <path d="{arc(860, 1440, R + 1)}" fill="none" stroke="url(#{p}-aube)" stroke-width="5" filter="url(#{p}-flou1)"/>
      <circle class="lueur" cx="{sx}" cy="{sy:.0f}" r="520" fill="url(#{p}-soleil)"/>
      <ellipse cx="{sx}" cy="{sy - 2:.0f}" rx="520" ry="2.2" fill="#FFF3E0" opacity=".85" filter="url(#{p}-flou1)"/>
      <ellipse cx="{sx}" cy="{sy - 2:.0f}" rx="180" ry="10" fill="#FFE3BC" opacity=".5" filter="url(#{p}-flou5)"/>
      <circle cx="{sx}" cy="{sy - 3:.0f}" r="26" fill="#FFF7EA" filter="url(#{p}-flou12)"/>
      <circle cx="{sx}" cy="{sy - 3:.0f}" r="7" fill="#FFFFFF" filter="url(#{p}-flou2)"/>
      <circle cx="{sx - 260}" cy="{sy + 110:.0f}" r="18" fill="#9FC6E6" opacity=".08" filter="url(#{p}-flou5)"/><circle cx="{sx - 420}" cy="{sy + 180:.0f}" r="34" fill="#F6C48E" opacity=".05" filter="url(#{p}-flou5)"/>'''


# ---------- IV. Asset Management : le voilier, cap tenu à toute heure ----------
def voilier(p="v"):
    return f'''<defs>
        <linearGradient id="{p}-ciel" x1="0" y1="0" x2="0" y2="566" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#0F1418"/><stop offset=".45" stop-color="#25323B"/><stop offset=".85" stop-color="#5D727C"/><stop offset="1" stop-color="#8399A1"/></linearGradient>
        <radialGradient id="{p}-lum" cx="560" cy="500" r="520" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#E6EDEC" stop-opacity=".55"/><stop offset=".35" stop-color="#B4C4C8" stop-opacity=".22"/><stop offset="1" stop-color="#B4C4C8" stop-opacity="0"/></radialGradient>
        <radialGradient id="{p}-teinte" cx="560" cy="500" r="620" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#E9A066" stop-opacity=".4"/><stop offset="1" stop-color="#E9A066" stop-opacity="0"/></radialGradient>
        <linearGradient id="{p}-mer" x1="0" y1="566" x2="0" y2="1024" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#557079"/><stop offset=".12" stop-color="#34494F"/><stop offset=".45" stop-color="#1A262C"/><stop offset="1" stop-color="#0A0F12"/></linearGradient>
        <linearGradient id="{p}-reflet" x1="0" y1="566" x2="0" y2="820" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#D6E2E2" stop-opacity=".45"/><stop offset="1" stop-color="#D6E2E2" stop-opacity="0"/></linearGradient>
        <linearGradient id="{p}-gv" x1="1060" y1="0" x2="1320" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#F4F5F2"/><stop offset=".55" stop-color="#D5DCDD"/><stop offset="1" stop-color="#8E9DA3"/></linearGradient>
        <linearGradient id="{p}-foc" x1="1040" y1="0" x2="1180" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#A9B6BA"/><stop offset=".6" stop-color="#E3E8E7"/><stop offset="1" stop-color="#C3CDD0"/></linearGradient>
        <linearGradient id="{p}-voileref" x1="0" y1="700" x2="0" y2="900" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#DCE3E2" stop-opacity=".3"/><stop offset="1" stop-color="#DCE3E2" stop-opacity="0"/></linearGradient>
      </defs>
      <rect x="0" y="0" width="1440" height="570" fill="url(#{p}-ciel)"/>
      <circle class="brume" cx="560" cy="500" r="520" fill="url(#{p}-lum)"/>
      <circle cx="560" cy="500" r="620" fill="url(#{p}-teinte)"/>
      <g class="nuages">
        <ellipse cx="380" cy="150" rx="520" ry="90" fill="#0E1317" opacity=".55"/><ellipse cx="1100" cy="110" rx="560" ry="110" fill="#0D1215" opacity=".6"/>
        <ellipse cx="760" cy="300" rx="420" ry="40" fill="#1F2B32" opacity=".55"/><ellipse cx="260" cy="380" rx="360" ry="22" fill="#2A3940" opacity=".5"/>
        <ellipse cx="1260" cy="420" rx="380" ry="24" fill="#33444C" opacity=".45"/><ellipse cx="640" cy="452" rx="300" ry="10" fill="#C9D6D7" opacity=".18"/>
      </g>
      <path fill="#3D5058" opacity=".8" d="M0 566 C80 560 160 552 240 556 C300 559 340 562 400 566 Z"/>
      <rect x="0" y="566" width="1440" height="458" fill="url(#{p}-mer)"/>
      <path fill="url(#{p}-reflet)" d="M300 566 H820 L980 820 H140 Z"/>
      <g class="vagues2" stroke="#9FB3B8" fill="none" stroke-linecap="round" opacity=".35"><path stroke-width="1" d="{_vague(590, 4)}"/><path stroke-width="1" d="{_vague(614, 5)}"/><path stroke-width="1.2" d="{_vague(646, 6)}"/></g>
      <g class="vagues1" stroke="#7F969C" fill="none" stroke-linecap="round" opacity=".28"><path stroke-width="1.4" d="{_vague(700, 8)}"/><path stroke-width="1.6" d="{_vague(772, 10)}"/><path stroke-width="2" d="{_vague(870, 12)}"/><path stroke-width="2.4" d="{_vague(980, 14)}"/></g>
      <path fill="url(#{p}-voileref)" d="M1080 704 L1300 704 L1250 900 L1110 900 Z"/>
      <g class="bateau"><g transform="rotate(7 1190 690)">
        <path d="M1190 150 V690" stroke="#1A2024" stroke-width="3"/>
        <path fill="url(#{p}-gv)" d="M1196 160 C1250 300 1300 470 1322 664 L1198 668 Z"/>
        <path fill="#FFFFFF" opacity=".25" d="M1196 160 C1214 300 1222 470 1226 666 L1198 668 Z"/>
        <path fill="url(#{p}-foc)" d="M1184 196 C1140 340 1090 500 1052 654 L1182 666 Z"/>
        <path d="M1196 330 L1262 330 M1196 470 L1296 470" stroke="#9AA8AD" stroke-width="1" opacity=".6"/>
        <path fill="#0B1013" d="M1028 668 C1100 686 1290 688 1360 664 L1344 690 C1270 712 1100 712 1046 690 Z"/>
        <path fill="#C9D3D5" opacity=".55" d="M1036 676 C1110 690 1280 692 1352 672 L1350 676 C1280 698 1110 696 1038 680 Z"/>
      </g></g>
      <g stroke="#E4ECEC" fill="none" stroke-linecap="round" opacity=".55"><path stroke-width="2" d="M1040 704 C980 708 900 712 820 716"/><path stroke-width="1.2" d="M1050 712 C960 722 880 730 760 736"/><path stroke-width="1" opacity=".6" d="M1360 696 C1390 700 1420 702 1440 702"/></g>'''


SCENES = {"demeure": demeure, "stable": stable, "capital": capital, "asset-management": voilier}
PREFIXES = {"demeure": "d", "stable": "s", "capital": "c", "asset-management": "v"}
# Cadrage 4/5 des pages d'activité, serré sur le sujet (x, y, largeur, hauteur)
CADRES = {"demeure": "860 250 580 725", "stable": "800 230 600 750", "capital": "760 200 680 850", "asset-management": "820 100 620 775"}


def svg(activite, cls, cadre="0 0 1440 1024", ajuste="xMaxYMid slice"):
    contenu = SCENES[activite](PREFIXES[activite])
    return (f'<svg class="{cls}" viewBox="{cadre}" preserveAspectRatio="{ajuste}" aria-hidden="true" focusable="false">\n      '
            f'{contenu}\n    </svg>')
