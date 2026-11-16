# Scènes des activités, dessinées en SVG dans l'esprit du voilier de l'accueil.
# Toutes partagent le même cadre (1440 x 1024), le même ciel gris et un sujet placé à droite,
# entre x = 960 et x = 1440, pour rester visible sur téléphone et dans le cadre 4/5 des pages.
import math, random

LARGEUR, HAUTEUR = 1440, 1024


def _flou(p, ecart):
    return f'<filter id="{p}-flou{ecart}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="{ecart}"/></filter>'


def _vague(y, a):
    return "M0 %d Q60 %d 120 %d %s" % (y, y - a, y, " ".join("T%d %d" % (x, y) for x in range(240, 1700, 120)))


# ---------- I. Demeure : une villa au crépuscule, cyprès et piscine ----------
def _cypres(x, base, h, l, couleur="#0B1114"):
    return (f'<path fill="{couleur}" d="M{x} {base} C{x - l} {base - h * .28:.0f} {x - l * .55:.0f} {base - h * .82:.0f} {x} {base - h} '
            f'C{x + l * .55:.0f} {base - h * .82:.0f} {x + l} {base - h * .28:.0f} {x} {base} Z"/>')


def demeure(p="d"):
    fen_haut = [1082 + 34 * k for k in range(7)]
    fen_bas = [1080 + 42 * k for k in range(6)]
    arche = lambda x, y, l, h: f'M{x} {y + h} V{y + l / 2} A{l / 2} {l / 2} 0 0 1 {x + l} {y + l / 2} V{y + h} Z'
    fenetres = (''.join(f'<rect x="{x}" y="500" width="14" height="30"/>' for x in fen_haut)
                + ''.join(f'<path d="{arche(x, 546, 18, 54)}"/>' for x in fen_bas)
                + '<rect x="1022" y="556" width="14" height="28"/><rect x="1364" y="556" width="14" height="28"/>')
    reflets = ''.join(f'<rect x="{x + 2}" y="664" width="12" height="34"/>' for x in fen_bas)
    lumieres = ''.join(f'<circle cx="{x}" cy="{y}" r="1.6"/>' for x, y in [(118, 612), (166, 606), (402, 624), (452, 628), (690, 640), (744, 636), (812, 630)])
    return f'''<defs>
        <linearGradient id="{p}-ciel" x1="0" y1="0" x2="0" y2="640" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#0D1216"/><stop offset=".42" stop-color="#222C33"/><stop offset=".78" stop-color="#58646B"/><stop offset=".93" stop-color="#9C8C80"/><stop offset="1" stop-color="#C2A58C"/></linearGradient>
        <radialGradient id="{p}-lum" cx="560" cy="640" r="680" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#F2B48A" stop-opacity=".5"/><stop offset=".4" stop-color="#C99A7E" stop-opacity=".18"/><stop offset="1" stop-color="#C99A7E" stop-opacity="0"/></radialGradient>
        <linearGradient id="{p}-sol" x1="0" y1="600" x2="0" y2="1024" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#263238"/><stop offset=".3" stop-color="#141C20"/><stop offset="1" stop-color="#080C0E"/></linearGradient>
        <linearGradient id="{p}-facade" x1="0" y1="470" x2="0" y2="610" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#CFC8BC"/><stop offset=".6" stop-color="#A9A398"/><stop offset="1" stop-color="#7C7870"/></linearGradient>
        <linearGradient id="{p}-cote" x1="1000" y1="0" x2="1400" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#E8E1D4" stop-opacity=".22"/><stop offset="1" stop-color="#000" stop-opacity=".18"/></linearGradient>
        <linearGradient id="{p}-eau" x1="0" y1="652" x2="0" y2="716" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#9DB0B3"/><stop offset=".5" stop-color="#5C7177"/><stop offset="1" stop-color="#2C3B40"/></linearGradient>
        {_flou(p, 3)}{_flou(p, 8)}{_flou(p, 18)}
      </defs>
      <rect width="1440" height="640" fill="url(#{p}-ciel)"/>
      <circle class="brume" cx="560" cy="640" r="680" fill="url(#{p}-lum)"/>
      <g class="nuages">
        <ellipse cx="320" cy="140" rx="560" ry="80" fill="#0C1114" opacity=".6"/><ellipse cx="1160" cy="96" rx="520" ry="96" fill="#0B1013" opacity=".65"/>
        <ellipse cx="820" cy="330" rx="460" ry="34" fill="#232E35" opacity=".5"/><ellipse cx="300" cy="460" rx="380" ry="16" fill="#8D7F78" opacity=".22"/>
        <ellipse cx="1240" cy="420" rx="340" ry="20" fill="#3B474E" opacity=".45"/>
      </g>
      <path fill="#56636A" opacity=".75" d="M0 618 C140 596 260 590 380 604 C500 618 600 612 720 600 C840 588 960 586 1080 598 L1080 660 L0 660 Z"/>
      <path fill="#36434A" d="M0 640 C160 624 300 626 440 636 C560 644 700 642 820 632 C880 627 920 624 960 622 L960 680 L0 680 Z"/>
      <g fill="#F4C890" opacity=".7">{lumieres}</g>
      <path fill="url(#{p}-sol)" d="M0 656 C200 646 420 650 640 656 C760 659 860 640 950 616 L1440 608 L1440 1024 L0 1024 Z"/>
      {_cypres(890, 640, 120, 11, "#10171A")}{_cypres(912, 640, 92, 9, "#10171A")}
      <g>
        <path fill="#252B2F" d="M994 540 L1012 524 L1062 524 L1062 540 Z M1338 524 L1388 524 L1406 540 L1338 540 Z"/>
        <rect x="1000" y="538" width="62" height="72" fill="url(#{p}-facade)"/><rect x="1338" y="538" width="62" height="72" fill="url(#{p}-facade)"/>
        <path fill="#2A3034" d="M1050 490 L1084 462 L1316 462 L1350 490 Z"/>
        <rect x="1060" y="488" width="280" height="122" fill="url(#{p}-facade)"/>
        <rect x="1000" y="488" width="400" height="122" fill="url(#{p}-cote)"/>
        <rect x="1054" y="486" width="292" height="5" fill="#DDD6CA"/><rect x="1060" y="538" width="280" height="3" fill="#BDB6AA"/>
        <g class="lueur" fill="#F7B871" filter="url(#{p}-flou8)" opacity=".75">{fenetres}</g>
        <g fill="#F6D2A0">{fenetres}</g>
        <rect x="990" y="606" width="420" height="5" fill="#D6CFC2" opacity=".8"/>
      </g>
      {_cypres(972, 614, 214, 19)}{_cypres(1000, 614, 160, 15)}{_cypres(1414, 614, 236, 20)}{_cypres(1440, 614, 186, 17)}
      <path fill="#1C2428" d="M940 612 L1440 612 L1440 652 L940 652 Z"/>
      <path fill="url(#{p}-eau)" d="M930 716 L1440 716 L1440 652 L972 652 Z"/>
      <g class="lueur" fill="#F2C08A" opacity=".45" filter="url(#{p}-flou3)">{reflets}</g>
      <path d="M972 653 L1440 653" stroke="#DDE4E2" stroke-width="1.4" opacity=".6"/>
      <g stroke="#C9D5D6" fill="none" opacity=".25"><path d="M960 676 C1100 680 1260 678 1440 674"/><path d="M948 696 C1120 700 1280 698 1440 694"/></g>
      <path fill="#0D1316" d="M0 760 C220 740 520 736 760 744 C900 748 1000 730 1080 724 L1440 720 L1440 1024 L0 1024 Z"/>
      <ellipse cx="1120" cy="760" rx="220" ry="34" fill="#070A0C" opacity=".8"/><ellipse cx="1400" cy="770" rx="160" ry="30" fill="#070A0C" opacity=".8"/>'''


# ---------- II. Stable : prairie à l'aube, chevaux et clôture blanche ----------
CHEVAL = ("M14 54 C10 50 8 46 12 42 L28 16 L32 5 L36 13 L40 3 L45 14 C60 22 78 38 96 50 C110 56 122 60 136 58 "
          "C150 56 162 52 172 56 C178 58 182 64 184 72 C189 90 191 110 187 130 L181 129 C181 108 179 92 177 80 "
          "C177 90 175 98 171 104 L173 122 L171 145 L175 152 L163 152 L163 145 L163 124 C159 114 155 106 150 102 "
          "C140 106 112 106 98 102 L97 124 L95 145 L99 152 L87 152 L87 145 L86 122 L84 106 L79 112 L77 145 L81 152 "
          "L69 152 L69 145 L71 114 C69 102 67 92 64 84 C58 74 50 64 42 59 C36 59 28 61 22 61 C18 61 15 58 14 54 Z")
CHEVAL_PATTE = "M150 104 L153 124 L151 145 L155 152 L143 152 L143 145 L143 124 L141 106 Z"
CHEVAL_BROUTE = ("M8 128 C4 126 3 121 6 118 L22 92 C28 74 36 60 50 50 L54 42 L56 50 L60 41 L62 51 C76 48 96 50 110 54 "
                 "C124 58 140 58 154 56 C166 54 176 56 182 64 C186 80 188 104 184 126 L178 125 C179 106 177 92 175 82 "
                 "C175 92 173 100 169 106 L171 124 L169 145 L173 152 L161 152 L161 145 L161 126 C157 116 153 108 148 104 "
                 "C138 108 112 108 98 104 L97 124 L95 145 L99 152 L87 152 L87 145 L86 124 L83 108 L78 114 L76 145 L80 152 "
                 "L68 152 L68 145 L70 114 C66 104 60 96 54 90 C46 100 36 114 28 124 C22 130 14 131 8 128 Z")


def stable(p="s"):
    rnd = random.Random(11)
    herbes = ''.join(f'<path d="M{x} {y} q{rnd.uniform(-3, 3):.1f} -{rnd.uniform(8, 16):.0f} {rnd.uniform(-6, 6):.1f} -{rnd.uniform(14, 26):.0f}"/>'
                     for x, y in [(rnd.uniform(0, 1440), rnd.uniform(930, 1024)) for _ in range(70)])
    piquets = ''
    for k in range(12):
        t = k / 11
        x = 840 + 600 * t ** 1.15
        y = 688 + 140 * t ** 1.3
        h = 18 + 52 * t ** 1.3
        piquets += f'<rect x="{x:.1f}" y="{y - h:.1f}" width="{1.6 + 3.4 * t:.1f}" height="{h:.1f}"/>'
    lisse = lambda d: "M840 %.0f C1040 %.0f 1240 %.0f 1440 %.0f" % (688 - 14 * d, 712 - 26 * d, 760 - 40 * d, 828 - 56 * d)
    chene = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(1282, 470, 62), (1222, 500, 50), (1346, 494, 54), (1250, 438, 48), (1318, 430, 50), (1180, 526, 34), (1392, 530, 38), (1286, 404, 40)])
    feuilles = random.Random(5)
    for _ in range(46):
        a = feuilles.uniform(math.pi * 1.02, math.pi * 1.98) if feuilles.random() < .8 else feuilles.uniform(0, math.pi)
        chene += f'<circle cx="{1284 + 128 * math.cos(a) * feuilles.uniform(.8, 1.02):.0f}" cy="{474 + 82 * math.sin(a) * feuilles.uniform(.8, 1.05):.0f}" r="{feuilles.uniform(12, 26):.0f}"/>'
    return f'''<defs>
        <linearGradient id="{p}-ciel" x1="0" y1="0" x2="0" y2="620" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#151B20"/><stop offset=".45" stop-color="#3C4850"/><stop offset=".82" stop-color="#8E9692"/><stop offset="1" stop-color="#D3C2A6"/></linearGradient>
        <radialGradient id="{p}-lum" cx="620" cy="600" r="700" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#F6DDB6" stop-opacity=".6"/><stop offset=".35" stop-color="#E2C9A6" stop-opacity=".2"/><stop offset="1" stop-color="#E2C9A6" stop-opacity="0"/></radialGradient>
        <linearGradient id="{p}-pre" x1="0" y1="640" x2="0" y2="1024" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#3A4646"/><stop offset=".35" stop-color="#1D2626"/><stop offset="1" stop-color="#090D0E"/></linearGradient>
        {_flou(p, 6)}{_flou(p, 14)}{_flou(p, 24)}
      </defs>
      <rect width="1440" height="640" fill="url(#{p}-ciel)"/>
      <circle class="brume" cx="620" cy="600" r="700" fill="url(#{p}-lum)"/>
      <circle cx="620" cy="590" r="30" fill="#FBEBD0" opacity=".75" filter="url(#{p}-flou6)"/>
      <g class="nuages">
        <ellipse cx="420" cy="120" rx="600" ry="70" fill="#12181C" opacity=".55"/><ellipse cx="1180" cy="170" rx="480" ry="60" fill="#1A2126" opacity=".5"/>
        <ellipse cx="860" cy="420" rx="420" ry="16" fill="#C9C1B0" opacity=".2"/><ellipse cx="240" cy="500" rx="300" ry="12" fill="#B9B3A6" opacity=".2"/>
      </g>
      <path fill="#7C8686" opacity=".7" d="M0 600 C180 584 320 580 480 592 C600 600 700 598 820 588 C980 576 1160 570 1440 586 L1440 660 L0 660 Z"/>
      <ellipse class="derive" cx="560" cy="612" rx="720" ry="20" fill="#E7E2D6" opacity=".35" filter="url(#{p}-flou14)"/>
      <path fill="#4E5A5A" d="M0 640 C160 622 340 618 520 630 C700 642 860 628 1000 616 C1160 602 1300 606 1440 614 L1440 700 L0 700 Z"/>
      <g fill="#10171A">
        <path d="M1278 600 C1276 572 1274 548 1270 522 L1290 522 C1288 548 1288 574 1292 600 Z"/>
        {chene}
      </g>
      <ellipse class="derive2" cx="900" cy="660" rx="760" ry="26" fill="#DCD8CC" opacity=".22" filter="url(#{p}-flou24)"/>
      <path fill="url(#{p}-pre)" d="M0 690 C240 664 520 662 760 672 C960 680 1140 650 1300 640 C1360 636 1400 636 1440 638 L1440 1024 L0 1024 Z"/>
      <g fill="#0C1214">
        <g transform="translate(958 606) scale(-.5 .5)"><path d="{CHEVAL_BROUTE}"/></g>
        <g transform="translate(1012 584) scale(.92)"><path d="{CHEVAL_PATTE}" opacity=".85"/><path d="{CHEVAL}"/></g>
      </g>
      <g fill="#D7DBD6" opacity=".75">{piquets}</g>
      <g fill="none" stroke="#D7DBD6" opacity=".7" stroke-linecap="round"><path stroke-width="2.2" d="{lisse(0)}"/><path stroke-width="2.2" d="{lisse(1)}"/></g>
      <g fill="none" stroke="#0E1416" stroke-width="2" stroke-linecap="round" opacity=".9">{herbes}</g>'''


# ---------- III. Capital : la Terre vue de l'orbite, au lever du soleil ----------
def capital(p="c"):
    cx, cy, R = 900, 2620, 2060
    rnd = random.Random(7)
    etoiles = ''
    for _ in range(170):
        x, y = rnd.uniform(0, 1440), rnd.uniform(0, 560)
        if y > cy - math.sqrt(max(R * R - (x - cx) ** 2, 0)) - 30:
            continue
        etoiles += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(.5, 1.4):.1f}" opacity="{rnd.uniform(.18, .8):.2f}"/>'

    def arc(x1, x2, r=R):
        y = lambda x: cy - math.sqrt(r * r - (x - cx) ** 2)
        return f'M{x1} {y(x1):.1f} A{r} {r} 0 0 1 {x2} {y(x2):.1f}'
    sx, sy = 1180, cy - math.sqrt(R * R - (1180 - cx) ** 2)
    nuees = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}"/>' for x, y, rx, ry in
                    [(1010, 612, 120, 6), (1250, 604, 150, 5), (1370, 626, 110, 7), (900, 650, 180, 9), (1150, 664, 200, 11), (760, 700, 220, 14), (1320, 700, 160, 12), (1040, 760, 260, 18)])
    return f'''<defs>
        <linearGradient id="{p}-nuit" x1="0" y1="0" x2="0" y2="600" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#030507"/><stop offset="1" stop-color="#0B1218"/></linearGradient>
        <radialGradient id="{p}-terre" cx="{sx}" cy="{sy:.0f}" r="1300" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#53707C"/><stop offset=".12" stop-color="#2A3F4A"/><stop offset=".45" stop-color="#121D24"/><stop offset="1" stop-color="#05080A"/></radialGradient>
        <linearGradient id="{p}-limbe" x1="0" y1="0" x2="1440" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#6FA8D4" stop-opacity="0"/><stop offset=".45" stop-color="#6FA8D4" stop-opacity=".35"/><stop offset=".82" stop-color="#9DCBEA" stop-opacity="1"/><stop offset="1" stop-color="#8CBEE0" stop-opacity=".7"/></linearGradient>
        <linearGradient id="{p}-aube" x1="900" y1="0" x2="1440" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#F3A86B" stop-opacity="0"/><stop offset=".5" stop-color="#F6B77E" stop-opacity="1"/><stop offset="1" stop-color="#F3A86B" stop-opacity=".2"/></linearGradient>
        <radialGradient id="{p}-soleil" cx="{sx}" cy="{sy:.0f}" r="460" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#FFE6C2" stop-opacity=".7"/><stop offset=".25" stop-color="#F8C894" stop-opacity=".22"/><stop offset="1" stop-color="#F8C894" stop-opacity="0"/></radialGradient>
        <clipPath id="{p}-sol"><circle cx="{cx}" cy="{cy}" r="{R}"/></clipPath>
        {_flou(p, 2)}{_flou(p, 5)}{_flou(p, 12)}{_flou(p, 26)}
      </defs>
      <rect width="1440" height="1024" fill="url(#{p}-nuit)"/>
      <g fill="#E8EEF2" class="scintille">{etoiles}</g>
      <circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#{p}-terre)"/>
      <g clip-path="url(#{p}-sol)" fill="#8FA9B4" opacity=".16" filter="url(#{p}-flou5)">{nuees}</g>
      <path d="{arc(120, 1440, R + 10)}" fill="none" stroke="url(#{p}-limbe)" stroke-width="26" opacity=".35" filter="url(#{p}-flou12)"/>
      <path d="{arc(120, 1440, R + 3)}" fill="none" stroke="url(#{p}-limbe)" stroke-width="5" filter="url(#{p}-flou2)"/>
      <path d="{arc(900, 1440, R + 2)}" fill="none" stroke="url(#{p}-aube)" stroke-width="4" filter="url(#{p}-flou2)"/>
      <circle class="lueur" cx="{sx}" cy="{sy:.0f}" r="460" fill="url(#{p}-soleil)"/>
      <ellipse cx="{sx}" cy="{sy - 2:.0f}" rx="420" ry="2.6" fill="#FFF2DE" opacity=".8" filter="url(#{p}-flou2)"/>
      <circle cx="{sx}" cy="{sy - 3:.0f}" r="22" fill="#FFF7EA" filter="url(#{p}-flou12)"/>
      <circle cx="{sx}" cy="{sy - 3:.0f}" r="6" fill="#FFFFFF" filter="url(#{p}-flou2)"/>'''


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
CADRES = {"demeure": "860 250 580 725", "stable": "860 210 580 725", "capital": "760 200 680 850", "asset-management": "820 100 620 775"}


def svg(activite, cls, cadre="0 0 1440 1024", ajuste="xMaxYMid slice"):
    contenu = SCENES[activite](PREFIXES[activite])
    return (f'<svg class="{cls}" viewBox="{cadre}" preserveAspectRatio="{ajuste}" aria-hidden="true" focusable="false">\n      '
            f'{contenu}\n    </svg>')
