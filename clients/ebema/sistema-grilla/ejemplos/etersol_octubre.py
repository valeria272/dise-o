#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA GRILLA · carrusel ETERSOL — pasto sintético (octubre 2026).

⚠️ SÓLO LA PORTADA. Las láminas 2 a 5 del brief no se arman todavía.

Familia A (producto en stock). Los textos son VERBATIM del brief: lo único que
decide diseño es dónde parte el titular entre la línea blanca y la caja roja.

Uso:  python build_carrusel.py  &&  bash render.sh etersol
"""
import html, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- el brief ---
# CARRUSEL — Pasto sintético para un patio que aguante la primavera
# Producto: Pasto sintético Etersol (distinto de la línea GEOS de cerámicas de julio)
# REF: @etersolchile (Pasto Sintético Fútbol Libre)
#      https://www.instagram.com/p/DXhHwpFjVrm/
#      Instalación paso a paso: https://cl.pinterest.com/pin/1172343965483315915/
CARRUSEL = {
    "slug": "etersol",
    "proveedor_logo": "img/proveedores/logo_etersol.png",
    "producto": "Etersol",
    "laminas": [
        # L1 · portada — el problema, en negativo
        # brief: «Llega la primavera, ¿tu patio aguanta la temporada?»
        #        Subtexto: Descubre el pasto sintético Etersol.
        #        Visual: patio con pasto natural descuidado o tierra pelada.
        #
        # Las tres zonas de la portada, y el criterio para repartir el texto:
        #   · arriba, en blanco  -> el contexto      «Llega la primavera,»
        #   · dentro del rojo    -> el gancho        «¿Tu patio aguanta la temporada?»
        #   · cápsula blanca     -> la bajada        «Descubre el pasto sintético Etersol»
        # ⛔ LA CÁPSULA BLANCA VA SIEMPRE (Paulina, 15-09-2026). El pie se queda
        # sólo con la flecha de «desliza».
        # La pregunta va en DOS renglones dentro del rojo: así la caja pesa más
        # que la línea de arriba, igual que en la portada de Masisa de junio.
        # ⛔ EL CONTEXTO VA LIBRE, FUERA DEL ROJO. El rojo sólo muerde la primera
        # línea DEL GANCHO, no la frase de contexto — así está en la portada de
        # Masisa de junio, donde «UNA AMPLIACIÓN FIRME» queda entera sobre la foto
        # y el rojo empieza a media altura de «EMPIEZA POR EL».
        # ⛔ EL PRE-ENUNCIADO NO CALZA EN ANCHO CON EL GANCHO (Paulina, 16-09-2026).
        # Va en un CUERPO MENOR — es un «pre-enunciado», no una línea más del
        # titular. Sirve para que el bloque se vea llamativo y ordenado cuando el
        # gancho solo no alcanza. Por eso viaja en su propio campo `pre` y NO
        # dentro de `sobre`: todo lo que entra en `sobre` se compone al ancho de
        # la caja, y así fue como salió tan grande como el gancho.
        {"foto": "fotos/01.png", "y": 620, "portada": True,
         "pre": "LLEGA LA PRIMAVERA,",
         "sobre": "¿TU PATIO AGUANTA",
         "caja": "LA TEMPORADA?",
         "capsula": "Descubre el pasto sintético Etersol",
         "pie": ""},
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


ANCHO_CAJA   = 942        # ancho total de la caja roja, con su padding
PADDING_CAJA = 22         # el padding lateral de la caja, el mismo del CSS

# ⛔ LAS DOS LÍNEAS DEL ENUNCIADO MIDEN LO MISMO. La de arriba se compone al ancho
# del TEXTO que va dentro de la caja roja, no a un ancho propio: por eso sube de
# cuerpo cuando es corta. El rojo envuelve a las dos con su padding.
# Comprobado en la referencia: Surpol sept, caja 948,5 y línea blanca 904,3
#   -> 948,5 − 2 × 22 = 904,5. Calza al décimo de píxel.
ANCHO_LINEA = ANCHO_CAJA - 2 * PADDING_CAJA
ANCHO_CAPSULA = 662       # sólo se usa si el brief trae subtexto de cápsula

# ⛔ EL PRE-ENUNCIADO — Paulina, 16-09-2026.
# No se compone al ancho de la caja: se compone a una FRACCIÓN DEL CUERPO del
# gancho, y su ancho cae donde caiga. Es lo que lo hace leerse como antesala del
# titular y no como otra línea del titular.
#   ⚠️ 0,47 está ESTIMADO sobre la referencia de Paulina (Masisa OLB, «UNA
#   AMPLIACIÓN FIRME»), no medido: el archivo no está en el repo todavía.
#   Cuando llegue, se mide y se fija acá.
PRE_CUERPO = 0.47         # cuerpo del pre-enunciado ÷ cuerpo del gancho
# Su interlineado (el aire que lo separa del gancho) vive en base-grilla.css,
# junto al resto de la tipografía de portada: un valor por cosa, en un solo sitio.


def cuerpo(l):
    # El pre-enunciado va PRIMERO y en su propia fila. Que sea una fila aparte es
    # lo que deja que la caja roja siga mordiendo la línea del GANCHO: el JS que
    # la hace crecer mira la fila inmediatamente anterior al rojo, y esa tiene que
    # seguir siendo el gancho, nunca el pre.
    bloques = "".join(f'<div class="fila"><span class="l pre">{fmt(x)}</span></div>'
                      for x in lineas(l.get("pre", "")))
    bloques += "".join(f'<div class="fila"><span class="l">{fmt(x)}</span></div>'
                       for x in lineas(l.get("sobre", "")))
    caja = lineas(l.get("caja", ""))
    if caja:
        # UNA sola caja por lámina (§4-bis): si el texto va en dos renglones, el
        # rojo es un único rectángulo, no dos pegados. Por eso el <br> va dentro.
        dentro = "<br>".join(fmt(x) for x in caja)
        bloques += f'<div class="fila rojo"><span class="l caja">{dentro}</span></div>'
    extra = ""
    if l.get("capsula"):
        extra = (f'<div class="fila-capsula">'
                 f'<span class="capsula-bajada">{fmt(l["capsula"])}</span></div>')
    elif l.get("bajada"):
        extra = f'<div class="bajada">{fmt(l["bajada"])}</div>'
    pie = ""
    if l.get("pie") is not None:
        # Con el subtexto ya en la cápsula, el pie se queda sólo con la flecha
        # de «desliza». Va igual: está en 4 de las 5 portadas medidas.
        txt = f'<div class="txt">{fmt(l["pie"])}</div>' if l["pie"] else ""
        pie = (f'<div class="pie-flecha">{txt}'
               f'<div class="pildora"><svg viewBox="0 0 190 20">'
               f'<path d="M0 10 H176 M166 3 L177 10 L166 17" fill="none" '
               f'stroke="#fff" stroke-width="3" stroke-linecap="round" '
               f'stroke-linejoin="round"/></svg></div></div>')
    anchos = (f'data-ancho="{ANCHO_LINEA}" data-ancho-caja="{ANCHO_CAJA}" '
              f'data-tapa="0.5" data-monta="14" data-ancho-capsula="{ANCHO_CAPSULA}" '
              f'data-pre-cuerpo="{PRE_CUERPO}"'
              if l.get("portada") else f'data-ancho="{ANCHO_CAJA - 2 * PADDING_CAJA}"')
    return f"""  <div class="bloque" style="top:{l['y']}px;">
    <div class="titular" {anchos}>{bloques}</div>
    {extra}
  </div>
  {pie}"""


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
// métricas de la fuente de reemplazo, y el ajuste quedaba un 15 % corto.
document.fonts.ready.then(function(){
  // 1. Cada línea del titular se lleva a un mismo ancho. La larga queda en un
  //    cuerpo menor y la corta en uno mayor: así el bloque sale simétrico.
  document.querySelectorAll('.titular').forEach(function(t){
    var objetivo = parseFloat(t.dataset.ancho) || 900;
    var objetivoCaja = parseFloat(t.dataset.anchoCaja) || objetivo;
    t.querySelectorAll('.l').forEach(function(l){
      if (l.classList.contains('pre')) return;   // el pre NO calza en ancho
      var meta = l.classList.contains('caja') ? objetivoCaja : objetivo;
      var lo = 24, hi = 200;
      for (var i = 0; i < 24; i++) {
        var m = (lo + hi) / 2;
        l.style.fontSize = m + 'px';
        if (l.getBoundingClientRect().width > meta) { hi = m; } else { lo = m; }
      }
      l.style.fontSize = lo + 'px';
    });

    // 1-pre. El PRE-ENUNCIADO se cuelga del cuerpo del gancho, no de un ancho.
    //    Se hace DESPUÉS de ajustar el gancho porque necesita su cuerpo ya
    //    resuelto. Si se compusiera al ancho de la caja, como el resto, saldría
    //    tan grande como el titular y el bloque pierde la jerarquía.
    var preF = parseFloat(t.dataset.preCuerpo);
    if (!isNaN(preF)) {
      var gancho = t.querySelector('.l:not(.pre):not(.caja)') || t.querySelector('.l.caja');
      if (gancho) {
        var base = parseFloat(getComputedStyle(gancho).fontSize);
        t.querySelectorAll('.l.pre').forEach(function(pl){
          pl.style.fontSize = (base * preF) + 'px';
        });
      }
    }

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
      var hasta = topeLetras + cap * (1 - tapa);
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
    //    la cápsula la acompaña sola y el solape no cambia.
    var cajaRoja = t.querySelector('.fila.rojo .l.caja');
    var cap = t.parentElement.querySelector('.fila-capsula');
    if (cajaRoja && cap) {
      var monta = parseFloat(t.dataset.monta);
      if (isNaN(monta)) monta = 14;
      var actual = parseFloat(getComputedStyle(cap).marginTop) || 0;
      // Se mide el SPAN, no el div: el blanco visible es el span.
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
        clase = "pieza feed portada" if l.get("portada") else "pieza feed"
        doc = f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="base-grilla.css"></head><body>
<div class="{clase}">
  <div class="bg"><img src="{l['foto']}"><div class="velo"></div></div>
{firma(c) if i == 1 else ""}
{cuerpo(l)}
</div>
{AJUSTE}
</body></html>"""
        nom = f"{c['slug']}{i}_feed.html"
        open(os.path.join(AQUI, nom), "w", encoding="utf-8").write(doc)
        print(f"  {nom}")
    print(f"\n{len(c['laminas'])} lámina. Ahora: bash render.sh {c['slug']}")


if __name__ == "__main__":
    main()
