"""English version of the Tundra Studio site. Writes the pages into en/."""
import pathlib

OUT = pathlib.Path(__file__).parent.parent / "en"
OUT.mkdir(exist_ok=True)
X_USER = "[TUNDRA_X_HANDLE]"            # <- X handle without @
X_ID = "1475353969329385472"
X_URL = "https://x.com/messages/compose?recipient_id=" + X_ID + "&text=Hi%20Tundra%20Studio%2C%20I%27m%20interested%20in%20your%20editing%20service%20and%20I%27d%20like%20my%20free%20trial%20%281%20short%20or%201%20thumbnail%29."
EMAIL = "tundrastudio3@gmail.com"

PAGES = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("portfolio.html", "Portfolio"),
    ("packages.html", "Packages"),
    ("faq.html", "FAQ"),
]
# English page -> Spanish page (for the ES / EN switch)
TO_ES = {"index.html": "index.html", "services.html": "servicios.html", "portfolio.html": "portafolio.html",
         "packages.html": "paquetes.html", "faq.html": "preguntas.html", "contact.html": "contacto.html"}

LOGO = '<svg width="42" height="30" viewBox="0 0 44 32" aria-hidden="true"><path d="M4 27 L17 9 L23 17 L30 6 L41 27" fill="none" stroke="#9B5CFF" stroke-width="5" transform="translate(1.5 2.5)"/><path d="M4 27 L17 9 L23 17 L30 6 L41 27" fill="none" stroke="#F4F2F8" stroke-width="5"/></svg>'
PLAY = '<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5l11 7-11 7z"/></svg>'
ARROW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
MAIL_ICON = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>'
X_ICON = '<svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 3h3.1l-6.8 7.8L21.8 21h-6.3l-4.9-6.4L5 21H1.9l7.3-8.3L1.5 3h6.4l4.4 5.9L17.5 3zm-1.1 16.2h1.7L7.1 4.7H5.3l11.1 14.5z"/></svg>'

ICONS = {
    "long": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M10 9l5 3-5 3z"/></svg>',
    "short": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 9l3 2-3 2z"/></svg>',
    "thumb": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-8 8"/></svg>',
}


def head(title, desc, fname):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="alternate" hreflang="es" href="../{TO_ES[fname]}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Michroma&family=Exo+2:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles.css">
</head>
<body>
"""


def nav(current):
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in PAGES[1:]
    )
    cur = ' aria-current="page"' if current == "contact.html" else ""
    return f"""<header class="nav">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="Tundra Studio, home">{LOGO}<span class="logo-text"><b>TUNDRA</b><small>STUDIO</small></span></a>
    <button class="menu-btn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="menu">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <nav class="nav-links" id="menu" aria-label="Main">
      {links}
      <a class="lang" href="../{TO_ES[current]}" hreflang="es" lang="es" aria-label="Ver en español">ES</a>
      <a class="btn btn-primary" href="contact.html"{cur}>Free trial</a>
    </nav>
  </div>
</header>
"""


FOOT_LINKS = "".join(f'<a href="{h}">{l}</a>' for h, l in PAGES) + '<a href="contact.html">Contact</a>'
FOOTER = f"""<footer>
  <div class="wrap">
    <div class="foot">
      <a class="logo" href="index.html" aria-label="Tundra Studio, home">{LOGO}<span class="logo-text"><b>TUNDRA</b><small>STUDIO</small></span></a>
      <nav aria-label="Footer">{FOOT_LINKS}</nav>
    </div>
    <div class="foot-bottom">© 2026 Tundra Studio · Create • Inspire • Connect</div>
  </div>
</footer>
<script>
(function(){{
  var btn=document.querySelector('.menu-btn'), menu=document.getElementById('menu');
  function close(){{menu.classList.remove('open');btn.setAttribute('aria-expanded','false');btn.setAttribute('aria-label','Open menu');}}
  btn.addEventListener('click',function(){{
    var open=menu.classList.toggle('open');
    btn.setAttribute('aria-expanded',open?'true':'false');
    btn.setAttribute('aria-label',open?'Close menu':'Open menu');
  }});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape')close();}});
}})();
</script>
</body>
</html>
"""


def page(fname, title, desc, body):
    (OUT / fname).write_text(head(title, desc, fname) + nav(fname) + "<main>\n" + body + "</main>\n" + FOOTER, encoding="utf-8")


def page_hero(eyebrow, h1, lead):
    return f"""<section class="page-hero" style="border-top:0">
  <div class="wrap">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>
"""


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


TRIAL = """<section class="trial">
  <div class="wrap">
    <p class="eyebrow">No strings attached</p>
    <h2>Your first short or thumbnail, free</h2>
    <p>Send us your raw footage and we'll edit <strong>1 short or 1 thumbnail</strong> at no cost so you can see how we work. If you like it, let's talk.</p>
    <p class="trial-note">The free trial doesn't include long videos. One trial per creator.</p>
    <a class="btn btn-primary" href="contact.html">Get my free trial</a>
  </div>
</section>
"""

# Portfolio: replace each [..] with real work and add the link to the video.
WORKS = [
    ("long", "Long video", "VACIANDO EL LAGO MÁS GRANDE DE ROBLOX", "Tio Strak · Roblox", "https://www.youtube.com/watch?v=9NWn6yytm10", "9NWn6yytm10", "10:28"),
    ("long", "Long video", "ME LLEVARON A LOS BACKROOMS… | PHOTOMALY", "STRAKGG · Photomaly", "https://www.youtube.com/watch?v=18Lm7Ccf6cQ", "18Lm7Ccf6cQ", "12:05"),
    ("short", "Short", "Odio atender a estos clientes 😤", "STRAKGG · Retro Rewind", "https://www.youtube.com/shorts/kuqUZBEv6M8", "kuqUZBEv6M8", "0:28"),
    ("long", "Long video", "Este juego de Roblox NO es tan fácil como parece… (Bite by Night)", "Central Crew Games · Roblox", "https://www.youtube.com/watch?v=r1h4St_ZX4w", "r1h4St_ZX4w", "12:54"),
    ("long", "Long video", "Abrí mi propio videoclub (no sé nada de videoclubs)", "STRAKGG · Retro Rewind", "https://www.youtube.com/watch?v=r_qhTcBpmF8", "r_qhTcBpmF8", "11:39"),
    ("short", "Short", "Los Jackson 2", "STRAKGG · Humor", "https://www.youtube.com/shorts/pWATZK5H4AU", "pWATZK5H4AU", "0:29"),
]


def work_card(kind, label, title, sub, url, vid, dur):
    return f"""<a class="work" href="{url}" target="_blank" rel="noopener" data-type="{kind}" aria-label="Watch on YouTube: {title} {label.lower()}">
  <div class="thumb has-img"><img src="../assets/yt-{vid}.jpg" alt="" loading="lazy" width="480" height="360"><span class="play">{PLAY}</span><span class="dur">{dur}</span></div>
  <div class="work-body"><span class="type">{label}</span><h3>{title}</h3><span>{sub}</span></div>
</a>"""


# ---------------- Home ----------------
page("index.html", "Tundra Studio · Video editing for gaming creators",
     "Tundra Studio edits long videos, shorts and thumbnails for streamers and gaming creators.",
     f"""<section class="hero" style="border-top:0">
  <div class="wrap">
    <svg class="hero-mark" width="120" height="86" viewBox="0 0 44 32" aria-hidden="true"><path d="M4 27 L17 9 L23 17 L30 6 L41 27" fill="none" stroke="#9B5CFF" stroke-width="4" transform="translate(1.2 1.8)"/><path d="M4 27 L17 9 L23 17 L30 6 L41 27" fill="none" stroke="#F4F2F8" stroke-width="4"/></svg>
    <p class="eyebrow">Video editing agency for creators</p>
    <h1>You create.<br><span>We edit.</span></h1>
    <p class="lead">Long videos, shorts and thumbnails for streamers and gaming creators. Upload your footage, tell us what you want and get it back ready to post.</p>
    <div class="ctas">
      <a class="btn btn-primary" href="contact.html">Get your free trial</a>
      <a class="btn btn-ghost" href="portfolio.html">See our work</a>
    </div>
    <p class="tagline">CREATE <i>•</i> INSPIRE <i>•</i> CONNECT</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="head-row">
      <div class="section-head"><p class="eyebrow">Services</p><h2>What we do</h2></div>
      <a class="link-arrow" href="services.html">See services {ARROW}</a>
    </div>
    <div class="grid cols-3">
      <a class="card" href="services.html" style="text-decoration:none;color:inherit"><div class="icon">{ICONS['long']}</div><h3>Long videos</h3><p>Your raw footage turned into YouTube videos.</p></a>
      <a class="card" href="services.html" style="text-decoration:none;color:inherit"><div class="icon">{ICONS['short']}</div><h3>Shorts</h3><p>Vertical clips for TikTok, Shorts and Reels.</p></a>
      <a class="card" href="services.html" style="text-decoration:none;color:inherit"><div class="icon">{ICONS['thumb']}</div><h3>Thumbnails</h3><p>Thumbnails people want to click.</p></a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="head-row">
      <div class="section-head"><p class="eyebrow">Portfolio</p><h2>Our work</h2></div>
      <a class="link-arrow" href="portfolio.html">See full portfolio {ARROW}</a>
    </div>
    <div class="grid cols-3">
      {''.join(work_card(*w) for w in WORKS[:3])}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="banner">
      <div><p class="eyebrow">Packages</p><h2 style="margin-top:10px">From $199 USD a month</h2><p>Long videos, shorts and thumbnails in one package. Month to month, no long contracts.</p></div>
      <a class="btn btn-primary" href="packages.html">See packages</a>
    </div>
  </div>
</section>
{TRIAL}""")

# ---------------- Services ----------------
page("services.html", "Services · Tundra Studio",
     "Long video, shorts and thumbnail editing for gaming creators.",
     page_hero("Services", "Everything your channel needs",
               "Editors focused on gaming and streaming: Minecraft, Fortnite, Roblox and whatever you play.")
     + f"""<section>
  <div class="wrap">
    <div class="grid cols-3">
      <article class="card"><div class="icon">{ICONS['long']}</div><h3>Long videos</h3><p>We turn your raw footage into YouTube videos.</p>{checks(['Cuts and pacing that keep viewers watching', 'Captions on key moments', 'Effects, zooms and memes', 'Music and sound'])}</article>
      <article class="card"><div class="icon">{ICONS['short']}</div><h3>Shorts</h3><p>Vertical clips ready to post.</p>{checks(['Hook from the first second', 'Dynamic captions', 'Formatted for TikTok, Shorts and Reels'])}</article>
      <article class="card"><div class="icon">{ICONS['thumb']}</div><h3>Thumbnails</h3><p>Designs made to get the click.</p>{checks(['Several options to choose from', 'With your face, avatar or character', 'Sized and ready for YouTube'])}</article>
    </div>
    <div class="card extra">
      <div style="flex:1 1 380px">
        <div style="display:flex;flex-wrap:wrap;gap:10px;align-items:center"><h3 style="margin:0;font-size:20px">Add-on: automatic clips from your streams</h3><span class="badge">Made by a bot · may contain mistakes</span></div>
        <p style="margin-top:8px">A bot pulls clips from your streams automatically. It's cheaper because an editor doesn't review them.</p>
      </div>
      <a class="btn btn-ghost" href="contact.html">Ask about the add-on</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">How it works</p><h2>It's that easy</h2></div>
    <div class="grid cols-4 steps">
      <div class="step"><h3>Upload your footage</h3><p>Send us your raw footage, extra assets and instructions through a form.</p></div>
      <div class="step"><h3>An editor takes it</h3><p>An editor on our team works on your video with your style and references.</p></div>
      <div class="step"><h3>We check quality</h3><p>Before it reaches you, we check it's well made and follows your instructions.</p></div>
      <div class="step"><h3>You get it and post</h3><p>It arrives ready to upload. Includes 2 rounds of revisions.</p></div>
    </div>
  </div>
</section>
{TRIAL}""")

# ---------------- Portfolio ----------------
page("portfolio.html", "Portfolio · Tundra Studio",
     "Long videos, shorts and thumbnails edited by Tundra Studio.",
     page_hero("Portfolio", "Our work", "A sample of the videos, shorts and thumbnails we make for creators.")
     + f"""<section>
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filter portfolio">
      <button class="chip" type="button" data-filter="all" aria-pressed="true">All</button>
      <button class="chip" type="button" data-filter="long" aria-pressed="false">Long videos</button>
      <button class="chip" type="button" data-filter="short" aria-pressed="false">Shorts</button>
    </div>
    <div class="grid cols-3" id="works">
      {''.join(work_card(*w) for w in WORKS)}
    </div>
  </div>
</section>
<script>
(function(){{
  var chips=document.querySelectorAll('.chip'), works=document.querySelectorAll('#works .work');
  chips.forEach(function(c){{c.addEventListener('click',function(){{
    var f=c.getAttribute('data-filter');
    chips.forEach(function(o){{o.setAttribute('aria-pressed',o===c?'true':'false');}});
    works.forEach(function(w){{w.classList.toggle('is-hidden', f!=='all' && w.getAttribute('data-type')!==f);}});
  }});}});
}})();
</script>
{TRIAL}""")

# ---------------- Packages ----------------
def plan(name, price, items, featured=False):
    tag = '<span class="tag">Most popular</span>' if featured else ""
    cls = " featured" if featured else ""
    btn = "btn-primary" if featured else "btn-ghost"
    return f"""<article class="card plan{cls}">{tag}<h3>{name}</h3><div class="price">${price} <small>/ month</small></div>{checks(items)}<a class="btn {btn}" href="contact.html">I want this one</a></article>"""

page("packages.html", "Packages · Tundra Studio",
     "Monthly editing packages from $199 USD.",
     page_hero("Packages", "Pay monthly and save", "Prices in US dollars (USD). No long contracts: month to month.")
     + f"""<section>
  <div class="wrap">
    <div class="grid plans">
      {plan('Starter', 199, ['2 long videos', '2 thumbnails', '8 shorts'])}
      {plan('Creator', 379, ['4 long videos', '4 thumbnails', '16 shorts'], True)}
      {plan('Pro', 699, ['8 long videos', '8 thumbnails', '30 shorts'])}
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Per piece</p><h2>Just need one thing?</h2></div>
    <div class="single">
      <div><span>Long video</span><b>$50</b></div>
      <div><span>Short</span><b>$12</b></div>
      <div><span>Thumbnail</span><b>$12</b></div>
    </div>
  </div>
</section>
{TRIAL}""")

# ---------------- FAQ ----------------
FAQ = [
    ("How do I send you my footage?", "Through a form where you choose the type of work and add the link to your raw footage (Google Drive, WeTransfer or similar), your extra assets and your instructions."),
    ("How long does delivery take?", "As a guide: thumbnails in 1 day, shorts in 1 to 2 days and long videos in 3 to 5 days. It depends on the length and what you ask for."),
    ("What does the free trial include?", "We edit 1 short or 1 thumbnail at no cost, your choice. It doesn't include long videos, and it's one trial per creator."),
    ("What if I don't like how it turned out?", "Every order includes 2 rounds of revisions so it ends up the way you want."),
    ("Can I cancel anytime?", "Yes. Packages are month to month, with no long contracts."),
    ("What if I don't use my whole package?", "The work in your package is for the current month. If you need more, you can order single pieces."),
    ("Do you only edit gaming content?", "We specialize in gaming and streaming, but if you make other kinds of content, message us and let's talk."),
]
page("faq.html", "FAQ · Tundra Studio",
     "Answers to the most common questions about Tundra Studio.",
     page_hero("FAQ", "What people ask us most", "If your question isn't here, message us on X or by email.")
     + '<section><div class="wrap"><div class="faq">'
     + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
     + '</div></div></section>\n' + TRIAL)

# ---------------- Contact ----------------
page("contact.html", "Contact · Tundra Studio",
     "Contact Tundra Studio on X or by email.",
     page_hero("Contact", "Let's talk about your channel", "Message us on X or by email and we'll get back to you as soon as we can.")
     + f"""<section style="border-top:0;padding-top:0">
  <div class="wrap">
    <div class="grid contact-cards">
      <div class="card x-card">
        <div class="x-logo">{X_ICON}</div>
        <span class="x-handle" style="font-size:clamp(20px,3vw,28px)">Direct message on X</span>
        <p>Send us a DM: tell us about your channel, what you need and whether you want your free trial.</p>
        <a class="btn btn-primary" href="{X_URL}" style="align-self:flex-start" target="_blank" rel="noopener">Send us a DM</a>
      </div>
      <div class="card x-card">
        <div class="x-logo" style="background:#24123A;border-color:#4A2F6E;color:#E0C8FF">{MAIL_ICON}</div>
        <span class="x-handle" style="font-size:clamp(18px,2.6vw,24px)">{EMAIL}</span>
        <p>Prefer email? Write to us and we'll get back to you as soon as we can.</p>
        <a class="btn btn-ghost" href="mailto:{EMAIL}" style="align-self:flex-start">Send an email</a>
      </div>
    </div>
  </div>
</section>
""")
print("ok en")
