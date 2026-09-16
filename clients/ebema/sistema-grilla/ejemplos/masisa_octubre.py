#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA GRILLA · carrusel MASISA — melamina y cantos (octubre 2026).

Familia A (producto en stock). Arco fijo de 5 láminas medido en §4-bis del manual:
    L1 problema · L2 causa · L3 solución · L4 tip pro · L5 cierre

⚠️ LOS TEXTOS SON VERBATIM DEL BRIEF. Lo único que decide diseño es dónde parte
el titular entre la línea blanca y la caja roja, y a qué altura cae el bloque.

Uso:  python build_carrusel.py  &&  bash render.sh masisa
"""
import html, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- el brief ---
# CARRUSEL — Mueble o clóset que hay que renovar antes de fin de año
# Producto: línea melamina/tableros para mueblería (MDP + cantos) Masisa
# REF: @hermanasmododeco x Masisa (ripiado Carvalho)
CARRUSEL = {
    "slug": "masisa",
    "proveedor_logo": "img/proveedores/logo_masisa.png",   # oficial, del PDF vectorial
    "producto": "Masisa",
    "laminas": [
        # L1 · portada — el problema, en negativo
        # brief: «El clóset o el mueble de cocina ya se ve deslucido, y quedan
        #         pocos meses para renovarlo.»  Subtexto: Línea melamina y cantos Masisa.
        {"foto": "fotos/01.png", "y": 690, "portada": True,
         "sobre": "EL CLÓSET O EL MUEBLE DE COCINA",
         "caja": "YA SE VE DESLUCIDO",
         "capsula": "Y quedan pocos meses para renovarlo",
         "pie": "Línea melamina y cantos Masisa"},

        # L2 · el puente — brief: «Tableros MDP Masisa, listos para mueblería.»
        {"foto": "fotos/02_escena_v3.png", "y": 258,
         "sobre": "TABLEROS MDP MASISA,",
         "caja": "LISTOS PARA MUEBLERÍA",
         "bajada": "Superficie pareja para armar o revestir **muebles a medida**."},

        # L3 · la solución — brief: «Cantos a juego para una terminación prolija.»
        {"foto": "fotos/03_canto.png", "y": 214,
         "sobre": "CANTOS A JUEGO",
         "caja": "PARA UNA TERMINACIÓN PROLIJA",
         "bajada": "Los cantos Masisa sellan el borde y **evitan que se vea el corte**."},

        # L4 · tip pro — brief: «Elige el color de canto antes de cortar todas las piezas.»
        #
        # ⛔ EL TIP PRO TIENE REGISTRO PROPIO, medido el 16-09-2026 sobre las 3
        # referencias que lo traen (cintac, novoplast, surpol):
        #   · LA ORDEN va en VERSALES blancas, en DOS líneas, y manda la lámina
        #   · LA CONDICIÓN va en la caja roja y va en CAJA BAJA
        #   · la jerarquía se INVIERTE respecto de L2-L3: acá la versal es la
        #     protagonista (mayúscula ~60 contra las ~46 de las otras láminas) y la
        #     caja roja pasa a ser el complemento
        #
        #   cintac     REVISA LA / MODULACIÓN        + «antes de cortar»
        #   novoplast  REVISA Y PRUEBA / LA INSTAL.  + «antes de tapar el muro»
        #   surpol     SELLA BIEN / LOS BORDES       + «de cada plancha»
        #
        # El tip de Masisa es casi el gemelo del de cintac, así que se compone igual.
        # Paulina, 16-09-2026: «bájale al pt de la frase "elige el color de canto"
        # para que quede en una línea». A los 83px del registro de tip pro la frase
        # entera mide ~1082 y no cabe en el lienzo (1080). 59,5 la deja en el ancho
        # de la caja. Es un ajuste DE ESTA LÁMINA: el registro sigue siendo 83.
        {"foto": "fotos/04_cantos.png", "y": 196, "tip": True, "cuerpo": 59.5,
         "sobre": "ELIGE EL COLOR DE CANTO",
         "caja": "antes de cortar todas las piezas",
         "bajada": "Evita **diferencias de tono** entre tablero y canto."},

        # L5 · cierre — brief: «Masisa, disponible en Ebema.»
        {"foto": "fotos/05.png", "cierre": True},
    ],
}

# ------------------------------------------------------------------ motor ---
NUM = re.compile(r"(\$?\d[\d\.,/%]*)")


def num(t):
    """Toda cifra en Helvetica Bold. Si escribes un número fuera de acá, queda mal."""
    return NUM.sub(r'<span class="num">\1</span>', t)


def fmt(t):
    partes = t.split("**")
    return "".join((f"<b>{num(html.escape(p))}</b>" if i % 2 else num(html.escape(p)))
                   for i, p in enumerate(partes))


def lineas(t):
    """El `|` es un salto de línea decidido a mano: define el ritmo del titular."""
    return [p.strip() for p in t.split("|")] if t else []


ANCHO_TITULAR = 910   # la media de las cajas rojas de las referencias (873-948)

# ⛔ LA CAJA ROJA ES SIEMPRE EL ELEMENTO MÁS ANCHO DEL BLOQUE: las letras del
# titular, también las de la línea blanca de arriba, tienen que quedar DENTRO.
# Medido sobre las dos portadas de referencia:
#     Surpol sept  caja 948,5 · línea blanca 904,3 -> el rojo sobresale 22,1 por lado
#     Masisa junio caja 936,5 · línea blanca 851,0 -> el rojo sobresale 42,7 por lado
ANCHO_CAJA   = 942        # ancho total de la caja roja, con su padding
PADDING_CAJA = 22         # el padding lateral de la caja, el mismo del CSS

# ⛔ LAS DOS LÍNEAS DEL ENUNCIADO MIDEN LO MISMO. La de arriba se compone al ancho
# del TEXTO que va dentro de la caja roja, no a un ancho propio: por eso sube de
# cuerpo cuando es larga. El rojo envuelve a las dos con su padding.
# Comprobado en la referencia: Surpol sept, caja 948,5 y línea blanca 904,3
#   -> 948,5 − 2 × 22 = 904,5. Calza al décimo de píxel.
ANCHO_LINEA = ANCHO_CAJA - 2 * PADDING_CAJA
# ⭐ EL ANCHO DE CAJA DEL CARRUSEL — la cifra que cose las láminas de desarrollo.
# Las 5 referencias caen entre 541,4 y 802,6, y 3 repiten el MISMO valor entre su L2
# y su L3 (cedral 677,8 · cintac 541,4 · surpol 745,0/738,2). Es una decisión por
# CARRUSEL, no por lámina. Masisa va en 778: donde aterrizó su L2 aprobada, y calza
# con toro (783,4), la referencia de línea más larga.
ANCHO_CAJA_DES = 778

ANCHO_CAPSULA = 662
# Ronda 11: +10 % sobre los 601,6 que se estaban viendo, no sobre los 772 de
# sistema (0,82 de la caja roja). Entre la ronda 8 y la 10 el ajuste de ancho de
# la cápsula se perdió al reescribir el bloque del script, y quedó con el cuerpo
# fijo de 25 px del CSS: lo que Paulina corrigió era esa versión más chica.


def cuerpo(l):
    # `cuerpo`: ajuste del cuerpo de la línea blanca PARA ESA LÁMINA. El registro del
    # sistema no cambia — sólo esta lámina. Se usa cuando la frase entra en una sola
    # línea y el cuerpo por defecto la deja más ancha que el lienzo.
    cp = l.get("cuerpo")
    est = f' style="font-size:{cp}px"' if cp else ""
    bloques = "".join(f'<div class="fila"><span class="l"{est}>{fmt(x)}</span></div>'
                      for x in lineas(l.get("sobre", "")))
    caja = lineas(l.get("caja", ""))
    if caja:
        # UNA sola caja por lamina (§4-bis): si el texto va en dos renglones, el
        # rojo es un unico rectangulo, no dos pegados. Por eso el <br> va dentro.
        dentro = "<br>".join(fmt(x) for x in caja)
        bloques += f'<div class="fila rojo"><span class="l caja">{dentro}</span></div>' 
    extra = ""
    if l.get("capsula"):
        extra = (f'<div class="fila-capsula">'
                 f'<span class="capsula-bajada">{fmt(l["capsula"])}</span></div>')
    elif l.get("bajada"):
        extra = f'<div class="bajada">{fmt(l["bajada"])}</div>'
    pie = ""
    if l.get("pie"):
        pie = (f'<div class="pie-flecha"><div class="txt">{fmt(l["pie"])}</div>'
               f'<div class="pildora"><svg viewBox="0 0 190 20">'
               f'<path d="M0 10 H176 M166 3 L177 10 L166 17" fill="none" '
               f'stroke="#fff" stroke-width="3" stroke-linecap="round" '
               f'stroke-linejoin="round"/></svg></div></div>')
    # ⛔ COMO SE COMPONE CADA LAMINA (medido el 16-09-2026 sobre las 10 referencias
    # de L2 y L3, y corregido ESE MISMO DIA: la primera version daba cuerpo fijo a
    # toda la lamina y la caja de la L3 se partia en dos lineas).
    #
    #   portada        -> TODO calza en ancho fijo (942), el cuerpo cae donde caiga
    #   L2-L4 blanca   -> CUERPO fijo (65px en el CSS), el ancho cae donde caiga
    #   L2-L4 caja     -> calza al ANCHO DE CAJA DEL CARRUSEL, el cuerpo cae solo
    #
    # La prueba de que la caja se compone al ancho: cedral repite 677,8 EXACTOS en
    # su L2 y su L3, con textos de 15 y 11 caracteres — «SIN OBRA GRUESA» y «NO SE
    # PUDRE». Si mandara el cuerpo, la de 11 letras seria mucho mas angosta.
    anchos = (f'data-ancho="{ANCHO_LINEA}" data-ancho-caja="{ANCHO_CAJA}" data-tapa="0.5" data-monta="14" data-ancho-capsula="{ANCHO_CAPSULA}"'
              if l.get("portada") else f'data-ancho-caja="{ANCHO_CAJA_DES}"')   # el ajuste mide la caja CON su padding
    return f"""  <div class="bloque" style="top:{l['y']}px;">
    <div class="titular" {anchos}>{bloques}</div>
    {extra}
  </div>
  {pie}"""


def cierre(c):
    return f"""  <div class="sobre">{fmt(c["producto"])} <b>disponible en Ebema</b></div>
  <img class="anillo" src="img/logo_ebema_anillo_oscuro.png">
  <div class="cta">&iexcl;Cotiza por&nbsp;<b>whatsapp</b></div>
  <div class="bio">en el link de la bio!</div>"""


def firma(c):
    return f"""  <div class="firma">
    <img class="ebema" src="img/logo_ebema_anillo_claro.png">
    <img class="prov" src="{c['proveedor_logo']}">
  </div>"""


# El único cálculo que no se puede hacer en Python: hay que MEDIR el texto ya
# compuesto. Corre en el navegador antes de la captura (render.sh le da presupuesto
# de tiempo virtual), así que el PNG sale con los cuerpos definitivos.
AJUSTE = """<script>
// Se espera a document.fonts: con `font-display:block` el layout mide con las
// métricas de la fuente de reemplazo, y el ajuste quedaba un 15 % corto (la caja
// roja salía en 770,9 cuando las referencias están entre 873 y 948).
document.fonts.ready.then(function(){
  // 1. Cada línea del titular se lleva a un mismo ancho. La larga queda en un
  //    cuerpo menor y la corta en uno mayor: así el bloque sale simétrico.
  document.querySelectorAll('.titular').forEach(function(t){
    var objetivo = parseFloat(t.dataset.ancho);         // sólo la portada lo trae
    var objetivoCaja = parseFloat(t.dataset.anchoCaja);
    if (isNaN(objetivo) && isNaN(objetivoCaja)) return;
    t.querySelectorAll('.l').forEach(function(l){
      var esCaja = l.classList.contains('caja');
      // En las de desarrollo la línea blanca NO se ajusta: su cuerpo lo fija el CSS
      // y su ancho cae donde caiga. La que calza al ancho es la caja, y sólo ella.
      if (!esCaja && isNaN(objetivo)) return;
      var meta = esCaja ? (isNaN(objetivoCaja) ? objetivo : objetivoCaja) : objetivo;
      var lo = 24, hi = 200;
      for (var i = 0; i < 24; i++) {
        var m = (lo + hi) / 2;
        l.style.fontSize = m + 'px';
        if (l.getBoundingClientRect().width > meta) { hi = m; } else { lo = m; }
      }
      l.style.fontSize = lo + 'px';
    });
    // 1-bis. La cápsula de la bajada se lleva a su propio ancho, igual que el
    //    titular: así crece con el bloque y no queda de un cuerpo suelto.
    var anchoCap = parseFloat(t.dataset.anchoCapsula);
    var cap0 = t.parentElement.querySelector('.capsula-bajada');
    if (cap0 && !isNaN(anchoCap)) {
      var lo2 = 14, hi2 = 90;
      for (var k = 0; k < 24; k++) {
        var m2 = (lo2 + hi2) / 2;
        cap0.style.fontSize = m2 + 'px';
        if (cap0.getBoundingClientRect().width > anchoCap) { hi2 = m2; } else { lo2 = m2; }
      }
      cap0.style.fontSize = lo2 + 'px';
    }

    // 2. La caja roja CRECE HACIA ARRIBA hasta la mitad de la primera línea.
    //    Ojo con la diferencia: subir la fila entera con un margen negativo
    //    arrastra el texto y junta los renglones. Lo que hay que mover es el
    //    BORDE de la caja, no su contenido. Se consigue con el par
    //    `padding-top: X` + `margin-top: -X`: el margen sube la caja X px y el
    //    padding devuelve el texto a su sitio, así que el interlineado del
    //    enunciado no cambia y sólo crece el alto del bloque rojo.
    //    La mitad se mide sobre las MAYÚSCULAS con TextMetrics: la caja de línea
    //    incluye interlineado, acentos y descendentes, y daba entre 48 y 68 %.
    // ⛔ ESTE PASO ES SOLO DE LA PORTADA. Se reconoce por `data-tapa`: si no está,
    // la lámina no muerde nada y la caja no crece. Cuando a las de desarrollo se
    // les empezó a pasar `data-ancho-caja` dejaron de salir por el `return` de
    // arriba y entraron acá, donde `tapa` cae a 0,5 por defecto: la caja de la L2
    // pasó de 70 a 84 de alto y la de la L3 a 95, fuera de la banda de 70-80.
    if (isNaN(parseFloat(t.dataset.tapa))) return;
    var filas = Array.prototype.slice.call(t.querySelectorAll('.fila'));
    var cv = document.createElement('canvas').getContext('2d');
    filas.forEach(function(f, i){
      if (!f.classList.contains('rojo') || i === 0) return;
      var prev = filas[i-1];
      if (prev.classList.contains('rojo')) return;
      var sp = prev.querySelector('.l');
      var cs = getComputedStyle(sp);
      var fs = parseFloat(cs.fontSize);
      cv.font = cs.fontWeight + ' ' + fs + 'px ' + cs.fontFamily;
      var m = cv.measureText(sp.textContent);
      var cap = m.actualBoundingBoxAscent;
      var rp = prev.getBoundingClientRect();
      var medio = (rp.height - (m.fontBoundingBoxAscent + m.fontBoundingBoxDescent)) / 2;
      var topeLetras = rp.top + medio + m.fontBoundingBoxAscent - cap;
      var tapa = parseFloat(t.dataset.tapa);
      if (isNaN(tapa)) tapa = 0.5;
      var hasta = topeLetras + cap * (1 - tapa);      // hasta dónde tiene que llegar el rojo
      var caja = f.querySelector('.l.caja');
      var base = parseFloat(getComputedStyle(caja).paddingTop) || 0;
      var crecer = caja.getBoundingClientRect().top - hasta;
      if (crecer > 0) {
        caja.style.paddingTop = (base + crecer) + 'px';
        f.style.marginTop = (-crecer) + 'px';
      }
    });

    // 3. La cápsula se apoya en el BORDE MEDIDO del rojo, montando lo que diga
    //    `data-monta`. Así, cuando la caja crece hacia abajo (su padding-bottom)
    //    la cápsula la acompaña sola y el solape no cambia. A mano no salía: el
    //    padding ya empuja la cápsula, y sumarle margen la bajaba el doble.
    var cajaRoja = t.querySelector('.fila.rojo .l.caja');
    var cap = t.parentElement.querySelector('.fila-capsula');
    if (cajaRoja && cap) {
      var monta = parseFloat(t.dataset.monta);
      if (isNaN(monta)) monta = 14;
      var actual = parseFloat(getComputedStyle(cap).marginTop) || 0;
      // Se mide el SPAN, no el div: el blanco visible es el span, y dentro del
      // div queda desplazado por el hueco de línea base (~30 px).
      var pastilla = cap.querySelector('.capsula-bajada') || cap;
      var delta = (cajaRoja.getBoundingClientRect().bottom - monta)
                - pastilla.getBoundingClientRect().top;
      cap.style.marginTop = (actual + delta) + 'px';
    }
  });
});
</script>"""


def main():
    c = CARRUSEL
    for i, l in enumerate(c["laminas"], 1):
        es_cierre = l.get("cierre")
        clase = "pieza feed cierre-carrusel" if es_cierre else "pieza feed"
        if i == 1:
            clase += " portada"   # la ronda 2 de Paulina va sólo acá, ver el CSS
        if l.get("tip"):
            clase += " tip"      # registro propio del consejo de oficio, ver el CSS
        # El velo entra por el extremo MAS CERCANO al bloque de texto: si el bloque
        # esta en la mitad de abajo, oscurecer desde arriba no lo ayuda y ademas
        # apaga la parte de la foto que si se ve. 675 = la mitad de 1350.
        velo_lado = " abajo" if l.get("y", 0) > 675 else ""
        interior = cierre(c) if es_cierre else cuerpo(l)
        # La cápsula de co-marca sólo va en la portada: así lo muestran las 5
        # referencias de septiembre y la de Masisa de junio.
        marca = firma(c) if i == 1 else ""
        doc = f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="base-grilla.css"></head><body>
<div class="{clase}">
  <div class="bg"><img src="{l['foto']}"><div class="velo{velo_lado}"></div></div>
{marca}
{interior}
</div>
{AJUSTE}
</body></html>"""
        nom = f"{c['slug']}{i}_feed.html"
        open(os.path.join(AQUI, nom), "w", encoding="utf-8").write(doc)
        print(f"  {nom}")
    print(f"\n{len(c['laminas'])} láminas. Ahora: bash render.sh {c['slug']}")


if __name__ == "__main__":
    main()
