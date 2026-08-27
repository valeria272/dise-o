---
name: casablanca-adn-medido
description: ADN de Pisos Casablanca medido sobre 55 piezas reales (26-08-2026) — tres registros, un solo gris #626260, geometría exacta, y qué quedó sin medir
metadata:
  type: project
---

El sistema de **Pisos Casablanca** quedó medido con PIL sobre **55 piezas aprobadas**
(ago-2025 → ago-2026) en `raw/casablanca/ref/`. Manual, `marca.json` y
`CHECKLIST-CLIENTE.md` en `clients/casablanca/`; medición en `medidas.json`; examen de
admisión en `out/casablanca/examen/`.

**La marca tiene TRES registros, no uno.** Confundirlos es el error caro:
- **A · Ficha de producto** (carrusel orgánico): el titular *es el nombre del piso*,
  serif itálica centrada; sin logo en las fichas intermedias.
- **B · Anuncio** (pauta): titular de beneficio en 2 líneas + botón **blanco macizo
  rectangular** (no cápsula outline) con texto gris.
- **C · Editorial** (lo publicado hoy en el feed): placa gris arriba a la izquierda,
  Didone CAJA ALTA, todo alineado a la izquierda. **NO está medido** — esas piezas no
  existen como archivo en ningún lado.

**Lo que estaba mal en el manual y ahora está corregido:** el gris único es
`#626260` (los `#4A4A48`/`#6B6B66`/`#6E6A63`/`#4A504F` no aparecen en ninguna pieza);
la caja del logo cuelga de `y=0` **también en story** (199×199 en feed, 237×306 en
story, no 160×182/204×253); la sans es geométrica ancha tipo Poppins/Futura con
**tracking cero**, no Montserrat con tracking 3,5; y el feed histórico es **1:1**
(35 de 55 piezas) — el 4:5 aparece recién en agosto 2026.

**Tipografía (identificada por glifos aislados, techo de medición 99,7 %):** las
versales son **Futura Medium** (IoU 89,2 % contra 79,7 % del segundo) y la caja baja
es **Montserrat Regular** (79,7 %) — **la marca usa DOS sans**. No es Poppins ni
Montserrat SemiBold, como decía el manual. El titular serif es una **Didone que sigue
sin identificarse**: el sustituto es `BodoniModa-Italic wght 800 / opsz 18` (77,1 %),
y se sabe que no es la real porque la **`z` de la marca es recta sin cola** (calce
29,9 %) y la **`j` baja recta** (53,4 %). Candidatas en Adobe Fonts: Bodoni URW,
Bauer Bodoni, ITC Bodoni Seventytwo, Walbaum, Didot LT Pro, Abril Display.

**Adobe Fonts en este Mac:** activar una familia en Creative Cloud la sincroniza a
`~/Library/.../CoreSync/plugins/livetype/.r/` y los scripts la leen directo (así vive
IvyOra para Tierra Calma). Sólo está instalada la app de Creative Cloud — sin
Photoshop ni Illustrator, así que "Buscar coincidencia de fuentes" no está disponible
hasta instalarlo.

**Septiembre 2026 entregado (V2, 14 gráficas).** La muestra de tabla es GRANDE:
`124,8 · 258 · 139,7 × 470` @1080 = **43,5 % del alto**, y sale de la foto oficial del
producto (ahí se ven las marcas de sierra del Aserrado), no del render del ambiente.
Recibe la luz del piso que tiene DEBAJO —medir a los costados daba la ventana y la
dejaba dorada— y se verifica con `casablanca-qa-muestra.py` (ΔE < 12: es el error
más caro de la marca). El compositor de perspectiva deja el piso con pinta de
textura pegada y no sirve para entregar; el camino bueno es Nano Banana con la foto
real del producto como referencia y verificar por ΔE.

**Truco reusable:** las gráficas incrustadas en una grilla de paid (Google Sheet de
>100 MB) se sacan exportando la hoja como ZIP HTML —
`curl -sL ".../export?format=zip"` → `resources/*.jpg`. La API de Drive no las ve.

Herramienta: `scripts/casablanca-tipografia.py` compara glifos aislados con IoU de
forma; sirve para cualquier marca.

Relacionado: [[compuerta-de-material]] (la carpeta de Casablanca volvió a tener 13
piezas de Between adentro; se movieron a `raw/hilton/between-ig-feed/`),
[[no-inventar-sistema-de-marca]], [[revex-adn-medido]], [[sistema-de-marcas]].
