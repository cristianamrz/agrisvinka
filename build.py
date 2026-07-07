# Generator simplu: 5 pagini dintr-un singur template.
# Rulează `python3 build.py` după orice modificare de conținut.
import os

MEDIA = "https://static.wixstatic.com/media/"
IMG = {
    "logo":      MEDIA + "cf3315_97afd674a9c3471aa1fcede0f466e962~mv2.png",
    "hero":      MEDIA + "cf3315_a79ed3cc3c09474aa5b45bba25acf822~mv2.png",
    "ferma1":    MEDIA + "cf3315_3933378d44a64c5ba4e20211959ab1e3~mv2.jpg",
    "ferma2":    MEDIA + "cf3315_976a11a9bedb45d5bd4ca09b6e537e86~mv2.jpg",
    "sat":       MEDIA + "cf3315_64e01c122cce4168b17b68d81fe98c4c~mv2.jpg",
    "poveste1":  MEDIA + "cf3315_760c6ebc396843879cfb363bb8e48ecc~mv2.jpg",
    "poveste2":  MEDIA + "cf3315_431bde1193db4191b0a56ee0e23253d3~mv2.jpg",
    "misiune":   MEDIA + "cf3315_50de6a44670d4272bf94a59a7e620bef~mv2.jpeg",
    "morcov":    MEDIA + "cf3315_41c7a06b455d4367b67647a643e2928d~mv2.jpg",
    "telina":    MEDIA + "cf3315_4cdcd81c8c9e4239aff2a82cb69486b7~mv2.jpg",
    "patrunjel": MEDIA + "8fdada96ee7c41c596963f5cf2c9360d.jpg",
    "pastarnac": MEDIA + "f78d3aa3ae0243a6a59faff1c134715e.jpg",
    "cartof":    MEDIA + "cf3315_59af98ad1baf418abc223e3ed64a0197~mv2.jpg",
    "ceapa":     MEDIA + "64e795a1fbff44ffb91a5741b8d6ddad.jpg",
    "parteneri": MEDIA + "cf3315_e7b20741b9d24992a435571464875e90~mv2.jpg",
    "gal1":      MEDIA + "cf3315_eb2c580c4fbf449eae15864b3d7da26d~mv2.jpg",
    "gal2":      MEDIA + "cf3315_ab196b9018dc4d5baf1c0b04bf2e309a~mv2.jpg",
    "contact1":  MEDIA + "cf3315_2823e809ad7d4f9caac5631b98cacd0f~mv2.jpg",
    "contact2":  MEDIA + "cf3315_fe216d27fed24f9c9f115cb6e0612817~mv2.jpg",
    "auchan":    MEDIA + "cf3315_c2b5e24ed92a4b8e8ac83a91d1c17834~mv2.png",
    "lidl":      MEDIA + "cf3315_33340e6c0b2b412d8be677f40d5c8cea~mv2.png",
    "ig":        MEDIA + "cf3315_353d2a5be06244a7ba10f95d4f4cc5a3~mv2.png",
    "fb":        MEDIA + "cf3315_b30586bcfac0498790d758c7fc8bc5cd~mv2.png",
    "tt":        MEDIA + "cf3315_46ea1bc241134facb6a8394f726e0c48~mv2.png",
}

SOCIAL = {
    "ig": "https://www.instagram.com/agrisvinka",
    "fb": "https://www.facebook.com/share/1BPo2JPoHg/",
    "tt": "https://www.tiktok.com/@ferma.agrisvinka",
}

# Linia solului: pământ + rădăcini care coboară (semnătura vizuală a site-ului)
SOIL = """<svg class="linia-solului" viewBox="0 0 1440 70" preserveAspectRatio="none" aria-hidden="true">
<path d="M0 22 Q 240 12 480 20 T 960 18 T 1440 22 V70 H0 Z" fill="{fill}"/>
<g stroke="{fill}" stroke-width="3" stroke-linecap="round" fill="none">
<path d="M180 24 q -4 16 2 30 q 4 8 -2 14"/><path d="M420 22 q 5 14 -1 26 q -5 10 1 18"/>
<path d="M700 20 q -3 18 3 32"/><path d="M980 20 q 4 16 -2 28 q -4 8 2 16"/>
<path d="M1240 24 q -5 14 1 26 q 5 10 -1 16"/>
</g></svg>"""

def page(depth, active, title, desc, hero_html, body_html, soil_fill="#231710"):
    r = "../" * depth
    def nav(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<li><a href="{r}{href}"{cur}>{label}</a></li>'
    soil = SOIL.format(fill=soil_fill)
    return f"""<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Young+Serif&family=Karla:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}style.css">
</head>
<body>
<div class="topbar">
  <nav class="nav" aria-label="Meniu principal">
    <a class="brand" href="{r}"><img src="{IMG['logo']}" alt="Agrisvinka"></a>
    <ul class="nav-links">
      {nav('', 'Acasă', 'home')}
      {nav('povestea-fermei/', 'Povestea fermei', 'povestea')}
      {nav('legumele-noastre/', 'Legumele noastre', 'legume')}
      {nav('parteneri/', 'Parteneri', 'parteneri')}
      {nav('contact/', 'Contact', 'contact')}
    </ul>
  </nav>
</div>

{hero_html}

{body_html}

{soil}
<footer>
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h2>AGRISVINKA</h2>
        <p>Cultivăm cu grijă, oferim cu drag!<br>Legume din inima Dobrogei, din 2007.</p>
        <div class="social">
          <a href="{SOCIAL['ig']}" aria-label="Instagram"><img src="{IMG['ig']}" alt="Instagram"></a>
          <a href="{SOCIAL['fb']}" aria-label="Facebook"><img src="{IMG['fb']}" alt="Facebook"></a>
          <a href="{SOCIAL['tt']}" aria-label="TikTok"><img src="{IMG['tt']}" alt="TikTok"></a>
        </div>
      </div>
      <div>
        <h2>Contact</h2>
        <p>Gloriei 26, Sarichioi, Tulcea<br>
        <a href="tel:0743111795">0743 111 795</a><br>
        <a href="mailto:contact@agrisvinka.ro">contact@agrisvinka.ro</a></p>
      </div>
      <div>
        <h2>Ne găsiți la</h2>
        <div class="footer-logos">
          <img src="{IMG['auchan']}" alt="Auchan">
          <img src="{IMG['lidl']}" alt="Lidl">
        </div>
      </div>
    </div>
    <div class="copy">
      <span>© 2026 Agrisvinka · Sarichioi, Tulcea</span>
      <span>#AGRISVINKA</span>
    </div>
  </div>
</footer>
</body>
</html>"""

# ---------------- ACASĂ ----------------
home_hero = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="fondat">Fondat 2007 · Dobrogea</span>
      <h1>Cultivăm cu grijă, oferim cu drag!</h1>
      <p class="lead">Rădăcini de aur din inima Dobrogei: morcov, pătrunjel, păstârnac, cartofi, ceapă și țelină — cultivate cu grijă și oferite cu drag.</p>
      <a class="btn" href="legumele-noastre/">Descoperă legumele</a>
      <a class="btn secundar" href="povestea-fermei/">Povestea noastră</a>
    </div>
    <div class="hero-img"><img src="{IMG['hero']}" alt="Legumele fermei Agrisvinka"></div>
  </div>
</section>"""

home_body = f"""<section>
  <div class="wrap">
    <p class="eyebrow">Descoperă ferma</p>
    <h2>Păstrăm tradiția pământului dobrogean</h2>
    <p style="max-width:62ch">Transformăm fiecare rădăcină într-un dar plin de gust și prospețime. Vă invităm să descoperiți legumele noastre — crescute în câmp deschis, verificate și ambalate cu grijă, ca să ajungă proaspete pe masa voastră.</p>
    <div class="grid-3">
      <article class="card">
        <div class="foto"><img src="{IMG['ferma1']}" alt="Câmpurile fermei" loading="lazy"></div>
        <div class="body"><h3>Descoperă ferma</h3><p>O afacere de familie, crescută de la 4 la peste 300 de hectare.</p><p><a class="leg" href="povestea-fermei/">Povestea noastră →</a></p></div>
      </article>
      <article class="card">
        <div class="foto"><img src="{IMG['hero']}" alt="Rădăcinoase Agrisvinka" loading="lazy"></div>
        <div class="body"><h3>Rădăcini de aur</h3><p>Morcov, pătrunjel, păstârnac, cartofi, ceapă și țelină din câmpurile Dobrogei.</p><p><a class="leg" href="legumele-noastre/">Descoperă legumele →</a></p></div>
      </article>
      <article class="card">
        <div class="foto"><img src="{IMG['ferma2']}" alt="Ferma din Sarichioi" loading="lazy"></div>
        <div class="body"><h3>Vizitează ferma</h3><p>Ne găsești în Sarichioi, pe malul lacului Razim, în județul Tulcea.</p><p><a class="leg" href="contact/">Locația noastră →</a></p></div>
      </article>
    </div>
  </div>
</section>"""

# ---------------- POVESTEA ----------------
pov_hero = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Povestea Agrisvinka</p>
      <h1>De la 4 hectare la 300</h1>
      <p class="lead">Agrisvinka s-a născut în 2007, din pasiunea noastră pentru pământul fertil al Dobrogei.</p>
    </div>
    <div class="hero-img"><img src="{IMG['poveste1']}" alt="Munca în câmp la Agrisvinka"></div>
  </div>
</section>"""

pov_body = f"""<section>
  <div class="wrap" style="max-width:760px">
    <p>De la primele 4 hectare cultivate, ferma a crescut pas cu pas și astăzi lucrează peste 300 de hectare, dintre care 185 de hectare sunt dedicate legumelor de calitate.</p>
    <p style="margin-top:1em">Suntem o afacere de familie, crescută din drag de pământ și din respect pentru natură. Zi de zi, fiecare dintre noi contribuie cu suflet — de la munca din câmp și irigații, până la recoltare și ambalare. Alături de o echipă dedicată, cultivăm cu grijă și responsabilitate, pentru ca legumele noastre să păstreze gustul curat al pământului dobrogean.</p>
    <p style="margin-top:1em">Pe câmpurile noastre însorite prind viață legume esențiale în bucătăria românească: morcov, pătrunjel, păstârnac, cartofi, ceapă și țelină. Fiecare rădăcină este atent crescută, verificată și ambalată în cadrul sistemului nostru modern de ambalare, care ne ajută să păstrăm prospețimea și calitatea până la raft.</p>
    <p style="margin-top:1em">Ne bucurăm să știm că produsele Agrisvinka se regăsesc în rețelele de supermarketuri, ajungând astfel pe mesele oamenilor din toată țara. Investim constant în tehnologii moderne de irigare, recoltare și procesare, pentru a răspunde provocărilor climatice și pentru a menține un standard înalt de calitate.</p>
  </div>
</section>
<section class="sect-camp">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Misiunea noastră</p>
      <h2>Mai mult decât agricultură</h2>
      <p>La Agrisvinka, credem că munca pământului înseamnă mai mult decât agricultură — este o promisiune de grijă față de natură și față de oamenii care se bucură de roadele ei.</p>
      <p style="margin-top:1em">Misiunea noastră este să cultivăm legume autentice, sănătoase și gustoase, cu respect pentru sol, pentru tradiție și pentru fiecare consumator. Prin fiecare recoltă, dorim să aducem în casele oamenilor prospețimea câmpului și bucuria simplității naturale.</p>
    </div>
    <div class="hero-img"><img src="{IMG['misiune']}" alt="Recolta Agrisvinka" loading="lazy"></div>
  </div>
</section>"""

# ---------------- LEGUME ----------------
LEGUME = [
    ("Morcov", "morcov", "Crescut pe câmpurile însorite ale Dobrogei, morcovul nostru îmbină gustul dulce, textura crocantă și prospețimea naturală. Fiecare morcov este atent îngrijit, recoltat și ambalat cu grijă, pentru ca savoarea autentică să ajungă direct pe masa ta."),
    ("Țelină", "telina", "Cu aromă intensă și textură bogată, țelina noastră este esențială în bucătăria românească. Cultivată cu atenție și drag, aduce în farfurie un gust natural și echilibrat, plin de prospețime."),
    ("Pătrunjel", "patrunjel", "Aromat, proaspăt și plin de gust, pătrunjelul nostru adaugă vitalitate fiecărui preparat. Cultivat cu grijă și respect pentru natură, el poartă în frunze și rădăcini esența pământului dobrogean."),
    ("Păstârnac", "pastarnac", "Alb, dulce și parfumat, păstârnacul nostru este o adevărată comoară a câmpurilor. Cu o textură fină și un gust echilibrat, aduce profunzime și savoare naturală mâncărurilor de acasă."),
    ("Cartof", "cartof", "Hrănitor, versatil și gustos, cartoful nostru este crescut cu grijă pe soluri fertile, bogate în minerale. De la piureuri fine la rețete tradiționale, oferă mereu gustul curat al pământului."),
    ("Ceapă", "ceapa", "Ceapa noastră, crocantă și aromată, dă savoare oricărui preparat. Cultivată cu grijă și recoltată la maturitate, păstrează gustul autentic și prospețimea câmpurilor dobrogeane."),
]
leg_items = "\n".join(
    f'''<div class="leguma">
      <div class="foto"><img src="{IMG[key]}" alt="{nume}" loading="lazy"></div>
      <div><h3>{nume}</h3><p>{text}</p></div>
    </div>''' for nume, key, text in LEGUME)

leg_hero = """<section class="hero">
  <div class="wrap" style="padding-bottom:48px">
    <p class="eyebrow">Legumele noastre</p>
    <h1>Descoperă colecția de bunătăți<br>din câmpurile Agrisvinka</h1>
    <p class="lead">Ferma Agrisvinka este specializată în cultivarea legumelor care nu lipsesc din nicio bucătărie românească. Cultivate în câmp deschis, îngrijite zi de zi, recoltate la momentul potrivit.</p>
  </div>
</section>"""

leg_body = f"""<section>
  <div class="wrap">
    {leg_items}
  </div>
</section>"""

# ---------------- PARTENERI ----------------
part_hero = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Parteneri</p>
      <h1>Partenerii noștri</h1>
      <p class="lead">De la câmp la raft, fiecare pas din drumul legumelor noastre este susținut de parteneri dedicați — oameni și companii care împărtășesc aceleași valori: grijă pentru calitate, inovație și respect pentru natură.</p>
    </div>
    <div class="hero-img"><img src="{IMG['parteneri']}" alt="Colaborare la Agrisvinka"></div>
  </div>
</section>"""

part_body = f"""<section>
  <div class="wrap">
    <div class="parteneri-grid">
      <div class="partener"><h3>Retail</h3><p>Legumele noastre ajung zilnic pe rafturile Auchan și Lidl, păstrând prospețimea și gustul autentic al câmpurilor dobrogeane.</p></div>
      <div class="partener"><h3>Semințe &amp; Cultivare</h3><p>Colaborăm cu parteneri de încredere pentru semințe de calitate și soluții agricole moderne, adaptate solului și climei Dobrogei.</p></div>
      <div class="partener"><h3>Utilaje &amp; Ambalare</h3><p>Cu sprijinul partenerilor noștri în tehnică agricolă și linii de ambalare, transformăm munca din câmp într-un proces eficient și precis.</p></div>
      <div class="partener"><h3>Tehnologie &amp; Software</h3><p>Folosim soluții digitale moderne pentru gestionarea terenurilor, planificarea culturilor și monitorizarea producției în timp real.</p></div>
    </div>
    <div class="logo-strip">
      <img src="{IMG['auchan']}" alt="Auchan">
      <img src="{IMG['lidl']}" alt="Lidl">
    </div>
  </div>
</section>
<section class="sect-camp">
  <div class="wrap">
    <p class="eyebrow">Împreună pentru calitate</p>
    <h2>O rețea de oameni care cred în muncă cinstită</h2>
    <p style="max-width:64ch">Fiecare partener este parte din povestea noastră — o rețea de oameni și companii care cred în muncă cinstită, inovație și respect față de pământ. Împreună, aducem pe mesele oamenilor legume proaspete, sănătoase și pline de gust.</p>
    <div class="galerie">
      <img src="{IMG['gal1']}" alt="Ferma Agrisvinka" loading="lazy">
      <img src="{IMG['gal2']}" alt="Recolta din câmp" loading="lazy">
      <img src="{IMG['ferma1']}" alt="Câmpurile din Dobrogea" loading="lazy">
    </div>
  </div>
</section>"""

# ---------------- CONTACT ----------------
con_hero = f"""<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Contact</p>
      <h1>Contactează-ne</h1>
      <p class="lead" style="margin-bottom:.6em"><a class="contact-mare" href="tel:0745035996">0745 035 996</a></p>
      <p><a href="mailto:contact@agrisvinka.ro">contact@agrisvinka.ro</a><br>Gloriei 26, Sarichioi, jud. Tulcea</p>
    </div>
    <div class="hero-img"><img src="{IMG['contact1']}" alt="Echipa Agrisvinka"></div>
  </div>
</section>"""

# TODO: creează un formular gratuit pe formspree.io și înlocuiește ID-ul de mai jos
con_body = f"""<section>
  <div class="wrap">
    <h2>Scrie-ne un mesaj</h2>
    <form action="https://formspree.io/f/INLOCUIESTE_ID" method="POST">
      <div class="f-row">
        <div><label for="nume">Nume *</label><input id="nume" name="nume" required></div>
        <div><label for="prenume">Prenume *</label><input id="prenume" name="prenume" required></div>
      </div>
      <div class="f-row">
        <div><label for="telefon">Telefon</label><input id="telefon" name="telefon" type="tel"></div>
        <div><label for="email">Email *</label><input id="email" name="email" type="email" required></div>
      </div>
      <div><label for="mesaj">Mesaj</label><textarea id="mesaj" name="mesaj"></textarea></div>
      <div><button class="btn" type="submit">Trimite mesajul</button></div>
    </form>
  </div>
</section>"""

PAGES = [
    (0, "home",     "AGRISVINKA — Legume din inima Dobrogei",
     "Ferma Agrisvinka din Sarichioi, Tulcea. Morcov, pătrunjel, păstârnac, cartofi, ceapă și țelină, cultivate cu grijă din 2007.",
     home_hero, home_body, "index.html"),
    (1, "povestea", "Povestea fermei | AGRISVINKA",
     "De la 4 hectare la peste 300: povestea fermei de familie Agrisvinka din Dobrogea.",
     pov_hero, pov_body, "povestea-fermei/index.html"),
    (1, "legume",   "Legumele noastre | AGRISVINKA",
     "Morcov, țelină, pătrunjel, păstârnac, cartof și ceapă — legume rădăcinoase din câmpurile Dobrogei.",
     leg_hero, leg_body, "legumele-noastre/index.html"),
    (1, "parteneri","Parteneri | AGRISVINKA",
     "Partenerii Agrisvinka: retail (Auchan, Lidl), semințe, utilaje, ambalare și tehnologie.",
     part_hero, part_body, "parteneri/index.html"),
    (1, "contact",  "Contact | AGRISVINKA",
     "Contactează ferma Agrisvinka: Gloriei 26, Sarichioi, Tulcea. Telefon și formular de mesaj.",
     con_hero, con_body, "contact/index.html"),
]

base = os.path.dirname(os.path.abspath(__file__))
for depth, key, title, desc, hero, body, path in PAGES:
    full = os.path.join(base, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(page(depth, key, title, desc, hero, body))
    print("scris:", path)
