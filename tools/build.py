"""Genera las páginas de Tundra Studio con el mismo menú y pie de página."""
import pathlib

OUT = pathlib.Path(__file__).parent.parent
X_USER = "[USUARIO_DE_TUNDRA]"            # <- cambia por tu usuario de X, sin @
X_ID = "1475353969329385472"
X_URL = "https://x.com/messages/compose?recipient_id=" + X_ID + "&text=Hola%20Tundra%20Studio%2C%20me%20interesa%20su%20servicio%20de%20edici%C3%B3n%20y%20quiero%20mi%20prueba%20gratis."
EMAIL = "tundrastudio3@gmail.com"

TO_EN = {"index.html": "index.html", "servicios.html": "services.html", "portafolio.html": "portfolio.html",
         "paquetes.html": "packages.html", "preguntas.html": "faq.html", "contacto.html": "contact.html"}

PAGES = [
    ("index.html", "Inicio"),
    ("servicios.html", "Servicios"),
    ("portafolio.html", "Portafolio"),
    ("paquetes.html", "Paquetes"),
    ("preguntas.html", "Preguntas"),
]

LOGO = '<svg width="42" height="30" viewBox="0 0 44 32" aria-hidden="true"><path d="M4 27 L17 9 L23 17 L30 6 L41 27" fill="none" stroke="#9B5CFF" stroke-width="5" transform="translate(1.5 2.5)"/><path d="M4 27 L17 9 L23 17 L30 6 L41 27" fill="none" stroke="#F4F2F8" stroke-width="5"/></svg>'
PLAY = '<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5l11 7-11 7z"/></svg>'
ARROW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
MAIL_ICON = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>'
X_ICON = '<svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 3h3.1l-6.8 7.8L21.8 21h-6.3l-4.9-6.4L5 21H1.9l7.3-8.3L1.5 3h6.4l4.4 5.9L17.5 3zm-1.1 16.2h1.7L7.1 4.7H5.3l11.1 14.5z"/></svg>'

ICONS = {
    "largo": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M10 9l5 3-5 3z"/></svg>',
    "short": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 9l3 2-3 2z"/></svg>',
    "mini": '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-8 8"/></svg>',
}


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Michroma&family=Exo+2:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
"""


def nav(current):
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in PAGES[1:]
    )
    cur = ' aria-current="page"' if current == "contacto.html" else ""
    return f"""<header class="nav">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="Tundra Studio, inicio">{LOGO}<span class="logo-text"><b>TUNDRA</b><small>STUDIO</small></span></a>
    <button class="menu-btn" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="menu">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <nav class="nav-links" id="menu" aria-label="Principal">
      {links}
      <a class="lang" href="en/{TO_EN[current]}" hreflang="en" lang="en" aria-label="View in English">EN</a>
      <a class="btn btn-primary" href="contacto.html"{cur}>Prueba gratis</a>
    </nav>
  </div>
</header>
"""


FOOT_LINKS = "".join(f'<a href="{h}">{l}</a>' for h, l in PAGES) + '<a href="contacto.html">Contacto</a>'
FOOTER = f"""<footer>
  <div class="wrap">
    <div class="foot">
      <a class="logo" href="index.html" aria-label="Tundra Studio, inicio">{LOGO}<span class="logo-text"><b>TUNDRA</b><small>STUDIO</small></span></a>
      <nav aria-label="Pie de página">{FOOT_LINKS}</nav>
    </div>
    <div class="foot-bottom">© 2026 Tundra Studio · Create • Inspire • Connect</div>
  </div>
</footer>
<script>
(function(){{
  var btn=document.querySelector('.menu-btn'), menu=document.getElementById('menu');
  function close(){{menu.classList.remove('open');btn.setAttribute('aria-expanded','false');btn.setAttribute('aria-label','Abrir menú');}}
  btn.addEventListener('click',function(){{
    var open=menu.classList.toggle('open');
    btn.setAttribute('aria-expanded',open?'true':'false');
    btn.setAttribute('aria-label',open?'Cerrar menú':'Abrir menú');
  }});
  document.addEventListener('keydown',function(e){{if(e.key==='Escape')close();}});
}})();
</script>
</body>
</html>
"""


def page(fname, title, desc, body):
    (OUT / fname).write_text(head(title, desc) + nav(fname) + "<main>\n" + body + "</main>\n" + FOOTER, encoding="utf-8")


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
    <p class="eyebrow">Sin compromiso</p>
    <h2>Tu primer short o miniatura, gratis</h2>
    <p>Mándanos un crudo y te lo editamos sin costo para que veas cómo trabajamos. Si te gusta, platicamos.</p>
    <a class="btn btn-primary" href="contacto.html">Quiero mi prueba gratis</a>
  </div>
</section>
"""

# Portafolio: reemplaza cada [..] con tus trabajos reales y pon el link al video.
WORKS = [
    ("largo", "Video largo", "ME LLEVARON A LOS BACKROOMS… | PHOTOMALY", "STRAKGG · Photomaly", "https://www.youtube.com/watch?v=18Lm7Ccf6cQ", "18Lm7Ccf6cQ", "12:05"),
    ("short", "Short", "Odio atender a estos clientes 😤", "STRAKGG · Retro Rewind", "https://www.youtube.com/shorts/kuqUZBEv6M8", "kuqUZBEv6M8", "0:28"),
    ("largo", "Video largo", "Este juego de Roblox NO es tan fácil como parece… (Bite by Night)", "Central Crew Games · Roblox", "https://www.youtube.com/watch?v=r1h4St_ZX4w", "r1h4St_ZX4w", "12:54"),
    ("largo", "Video largo", "Abrí mi propio videoclub (no sé nada de videoclubs)", "STRAKGG · Retro Rewind", "https://www.youtube.com/watch?v=r_qhTcBpmF8", "r_qhTcBpmF8", "11:39"),
    ("short", "Short", "Los Jackson 2", "STRAKGG · Humor", "https://www.youtube.com/shorts/pWATZK5H4AU", "pWATZK5H4AU", "0:29"),
]


def work_card(kind, label, title, sub, url, vid, dur):
    return f"""<a class="work" href="{url}" target="_blank" rel="noopener" data-type="{kind}" aria-label="Ver en YouTube: {title} {label.lower()}">
  <div class="thumb has-img"><img src="assets/yt-{vid}.jpg" alt="" loading="lazy" width="480" height="360"><span class="play">{PLAY}</span><span class="dur">{dur}</span></div>
  <div class="work-body"><span class="type">{label}</span><h3>{title}</h3><span>{sub}</span></div>
</a>"""


# ---------------- Inicio ----------------
page("index.html", "Tundra Studio · Edición para creadores de gaming",
     "Tundra Studio edita videos largos, shorts y miniaturas para streamers y creadores de gaming.",
     f"""<section class="hero" style="border-top:0">
  <div class="wrap">
    <svg class="hero-mark" width="120" height="86" viewBox="0 0 44 32" aria-hidden="true"><path d="M4 27 L17 9 L23 17 L30 6 L41 27" fill="none" stroke="#9B5CFF" stroke-width="4" transform="translate(1.2 1.8)"/><path d="M4 27 L17 9 L23 17 L30 6 L41 27" fill="none" stroke="#F4F2F8" stroke-width="4"/></svg>
    <p class="eyebrow">Agencia de edición para creadores</p>
    <h1>Tú crea.<br><span>Nosotros editamos.</span></h1>
    <p class="lead">Videos largos, shorts y miniaturas para streamers y creadores de gaming. Sube tu material, dinos qué quieres y recíbelo listo para publicar.</p>
    <div class="ctas">
      <a class="btn btn-primary" href="contacto.html">Pide tu prueba gratis</a>
      <a class="btn btn-ghost" href="portafolio.html">Ver portafolio</a>
    </div>
    <p class="tagline">CREATE <i>•</i> INSPIRE <i>•</i> CONNECT</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="head-row">
      <div class="section-head"><p class="eyebrow">Servicios</p><h2>Lo que hacemos</h2></div>
      <a class="link-arrow" href="servicios.html">Ver servicios {ARROW}</a>
    </div>
    <div class="grid cols-3">
      <a class="card" href="servicios.html" style="text-decoration:none;color:inherit"><div class="icon">{ICONS['largo']}</div><h3>Videos largos</h3><p>Tus crudos convertidos en videos para YouTube.</p></a>
      <a class="card" href="servicios.html" style="text-decoration:none;color:inherit"><div class="icon">{ICONS['short']}</div><h3>Shorts</h3><p>Clips verticales para TikTok, Shorts y Reels.</p></a>
      <a class="card" href="servicios.html" style="text-decoration:none;color:inherit"><div class="icon">{ICONS['mini']}</div><h3>Miniaturas</h3><p>Miniaturas que dan ganas de hacer clic.</p></a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="head-row">
      <div class="section-head"><p class="eyebrow">Portafolio</p><h2>Nuestro trabajo</h2></div>
      <a class="link-arrow" href="portafolio.html">Ver todo el portafolio {ARROW}</a>
    </div>
    <div class="grid cols-3">
      {''.join(work_card(*w) for w in WORKS[:3])}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="banner">
      <div><p class="eyebrow">Paquetes</p><h2 style="margin-top:10px">Desde $199 USD al mes</h2><p>Videos largos, shorts y miniaturas en un solo paquete. Mes a mes, sin contratos largos.</p></div>
      <a class="btn btn-primary" href="paquetes.html">Ver paquetes</a>
    </div>
  </div>
</section>
{TRIAL}""")

# ---------------- Servicios ----------------
page("servicios.html", "Servicios · Tundra Studio",
     "Edición de videos largos, shorts y miniaturas para creadores de gaming.",
     page_hero("Servicios", "Todo lo que tu canal necesita",
               "Editores enfocados en gaming y streaming: Minecraft, Fortnite, Roblox y lo que juegues.")
     + f"""<section>
  <div class="wrap">
    <div class="grid cols-3">
      <article class="card"><div class="icon">{ICONS['largo']}</div><h3>Videos largos</h3><p>Convertimos tus crudos en videos para YouTube.</p>{checks(['Cortes y ritmo para retener', 'Subtítulos en momentos clave', 'Efectos, zooms y memes', 'Música y sonido'])}</article>
      <article class="card"><div class="icon">{ICONS['short']}</div><h3>Shorts</h3><p>Clips verticales listos para publicar.</p>{checks(['Gancho desde el primer segundo', 'Subtítulos dinámicos', 'Formato para TikTok, Shorts y Reels'])}</article>
      <article class="card"><div class="icon">{ICONS['mini']}</div><h3>Miniaturas</h3><p>Diseños pensados para el clic.</p>{checks(['Varias opciones para elegir', 'Con tu cara, avatar o personaje', 'Tamaño listo para YouTube'])}</article>
    </div>
    <div class="card extra">
      <div style="flex:1 1 380px">
        <div style="display:flex;flex-wrap:wrap;gap:10px;align-items:center"><h3 style="margin:0;font-size:20px">Extra: clips automáticos de tus streams</h3><span class="badge">Hecho por bot · puede tener errores</span></div>
        <p style="margin-top:8px">Un bot saca clips de tus streams de forma automática. Es más barato porque no lo revisa un editor.</p>
      </div>
      <a class="btn btn-ghost" href="contacto.html">Preguntar por el extra</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Cómo funciona</p><h2>Así de fácil</h2></div>
    <div class="grid cols-4 steps">
      <div class="step"><h3>Sube tu material</h3><p>Mándanos tus crudos, material extra y tus instrucciones con un formulario.</p></div>
      <div class="step"><h3>Un editor lo toma</h3><p>Un editor de nuestro equipo trabaja tu video con tu estilo y tus referencias.</p></div>
      <div class="step"><h3>Revisamos la calidad</h3><p>Antes de que te llegue, revisamos que esté bien hecho y siga tus instrucciones.</p></div>
      <div class="step"><h3>Recibes y publicas</h3><p>Te llega listo para subir. Incluye 2 rondas de correcciones.</p></div>
    </div>
  </div>
</section>
{TRIAL}""")

# ---------------- Portafolio ----------------
page("portafolio.html", "Portafolio · Tundra Studio",
     "Videos largos, shorts y miniaturas editados por Tundra Studio.",
     page_hero("Portafolio", "Nuestro trabajo", "Una muestra de los videos, shorts y miniaturas que hacemos para creadores.")
     + f"""<section>
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filtrar portafolio">
      <button class="chip" type="button" data-filter="all" aria-pressed="true">Todo</button>
      <button class="chip" type="button" data-filter="largo" aria-pressed="false">Videos largos</button>
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

# ---------------- Paquetes ----------------
def plan(name, price, items, featured=False):
    tag = '<span class="tag">Más popular</span>' if featured else ""
    cls = " featured" if featured else ""
    btn = "btn-primary" if featured else "btn-ghost"
    return f"""<article class="card plan{cls}">{tag}<h3>{name}</h3><div class="price">${price} <small>/ mes</small></div>{checks(items)}<a class="btn {btn}" href="contacto.html">Quiero este</a></article>"""

page("paquetes.html", "Paquetes · Tundra Studio",
     "Paquetes mensuales de edición desde $199 USD.",
     page_hero("Paquetes", "Paga al mes y ahorra", "Precios en dólares (USD). Sin contratos largos: mes a mes.")
     + f"""<section>
  <div class="wrap">
    <div class="grid plans">
      {plan('Inicio', 199, ['2 videos largos', '2 miniaturas', '8 shorts'])}
      {plan('Creador', 379, ['4 videos largos', '4 miniaturas', '16 shorts'], True)}
      {plan('Pro', 699, ['8 videos largos', '8 miniaturas', '30 shorts'])}
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Por pieza</p><h2>¿Solo necesitas algo suelto?</h2></div>
    <div class="single">
      <div><span>Video largo</span><b>$50</b></div>
      <div><span>Short</span><b>$12</b></div>
      <div><span>Miniatura</span><b>$12</b></div>
    </div>
  </div>
</section>
{TRIAL}""")

# ---------------- Preguntas ----------------
FAQ = [
    ("¿Cómo les mando mi material?", "Con un formulario donde pones el tipo de trabajo, el link a tus crudos (Google Drive, WeTransfer o similar), tu material extra y tus instrucciones."),
    ("¿Cuánto tardan en entregar?", "Como referencia: miniaturas en 1 día, shorts en 1 a 2 días y videos largos en 3 a 5 días. Depende de la duración y de lo que pidas."),
    ("¿Y si no me gusta cómo quedó?", "Cada pedido incluye 2 rondas de correcciones para dejarlo como lo quieres."),
    ("¿Puedo cancelar cuando quiera?", "Sí. Los paquetes son mes a mes, sin contratos largos."),
    ("¿Qué pasa si no uso todo mi paquete?", "Los trabajos de tu paquete son para el mes en curso. Si necesitas más, puedes pedir piezas sueltas."),
    ("¿Solo editan gaming?", "Nos especializamos en gaming y streaming, pero si tienes otro tipo de contenido escríbenos y lo platicamos."),
]
page("preguntas.html", "Preguntas frecuentes · Tundra Studio",
     "Respuestas a las preguntas más comunes sobre Tundra Studio.",
     page_hero("Preguntas frecuentes", "Lo que más nos preguntan", "Si tu duda no está aquí, escríbenos por X o por correo.")
     + '<section><div class="wrap"><div class="faq">'
     + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
     + '</div></div></section>\n' + TRIAL)

# ---------------- Contacto ----------------
page("contacto.html", "Contacto · Tundra Studio",
     "Escríbele a Tundra Studio por X o por correo.",
     page_hero("Contacto", "Hablemos de tu canal", "Escríbenos por X o por correo y te respondemos lo antes posible.")
     + f"""<section style="border-top:0;padding-top:0">
  <div class="wrap">
    <div class="grid contact-cards">
      <div class="card x-card">
        <div class="x-logo">{X_ICON}</div>
        <span class="x-handle" style="font-size:clamp(20px,3vw,28px)">Mensaje directo en X</span>
        <p>Mándanos mensaje directo: cuéntanos de tu canal, qué necesitas y si quieres tu prueba gratis.</p>
        <a class="btn btn-primary" href="{X_URL}" style="align-self:flex-start" target="_blank" rel="noopener">Mándanos mensaje</a>
      </div>
      <div class="card x-card">
        <div class="x-logo" style="background:#24123A;border-color:#4A2F6E;color:#E0C8FF">{MAIL_ICON}</div>
        <span class="x-handle" style="font-size:clamp(18px,2.6vw,24px)">{EMAIL}</span>
        <p>¿Prefieres correo? Escríbenos y te respondemos lo antes posible.</p>
        <a class="btn btn-ghost" href="mailto:{EMAIL}" style="align-self:flex-start">Mandar correo</a>
      </div>
    </div>
  </div>
</section>
""")
print("ok")
