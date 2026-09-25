---
name: cliente-rendic
description: "RENDIC — cerebro del cliente: 17 reglas firmes, última cosecha 2026-09-25. Generado desde clients/rendic/APRENDIZAJES.md; leerlo antes de diseñar para rendic"
metadata:
  type: project
---

⚙️ **Nota generada por `scripts/memoria-cliente.py` en cada /cierre. No se edita acá:**
la fuente es `clients/rendic/APRENDIZAJES.md` (léelo completo antes de producir; esto es
sólo lo más confirmado). ⛔ Vale sólo para rendic: no se traspasa a otra marca.

Criterio: **Diego Aguilar** (diseñador de Rendic) · Aprueba: **Sebastián Córdova** (medios, cuenta REM)

## Reglas más confirmadas
- **R-01** · El fondo es exactamente **#661D33**, no el burdeo del logo (#651D32); no se unifican sin preguntar — _medición de Claude sobre las 10 gráficas de sept, 07-09-2026_ · ✔×1
- **R-02** · La referencia son las piezas de **septiembre 2026** (`raw/rendic/ref-sept2026/`). Nada anterior a agosto 2026: las de marzo–junio son del sistema viejo — _manual, 07-09-2026_ · ✔×1
- **R-03** · En toda pieza (feed, story y reel) va el logo **ARC 7421C**: anillo burdeo macizo, disco blanco, **opaco**. Nunca el blanco calado — _Diego Aguilar, 08-09-2026, ronda 1 de octubre: «el logo está mal, es el que tiene fondo de color, eso para todos los post»_ · ✔×1
- **R-04** · El PNG oficial del logo trae 10,8 % de margen transparente por lado: se recorta con `getbbox()` **antes** de escalar — _Claude, 08-09-2026, al aplicar R-03_ · ✔×1
- **R-05** · En **feed** la foto se sube dentro de la elipse, entre 120 y 165 px según la pieza, para que la elipse no corte caras. Techo 165 px (sobre eso asoma el logo quemado del metraje) — _Diego Aguilar, 08-09-2026: «en todos los post corta la cara de los niños»_ · ✔×1
- **R-06** · Cierra con el slogan **«Educating for purpose, excellence & wellbeing»** en dos líneas, Montserrat 500 burdeo, abajo a la derecha en la banda blanca, 330 px de ancho en feed y 360 en story. La firma «Somos Familia Rendicina» está **retirada** — _Sebastián Córdova, 23-09-2026, las 13 piezas de octubre: «Eliminar "Somos familia rendicina" y colocar el slogan nuevo»_ · ✔×1
- **R-07** · En **reel** el slogan va sólo en la tarjeta de cierre, centrado y en blanco, terminando en y=1480 — _QA de Serena con Claude, 24-09-2026_ · ✔×1
- **R-08** · Reel: 120 px arriba y 420 px abajo libres, y **columna derecha de 180 px** libre: el texto centrado no pasa de x=900 (ancho útil 720) — _hoja «Zonas seguras» del brief; QA 24-09-2026_ · ✔×1
- **R-09** · Story: **268 px (14 %) arriba y abajo** sin texto ni logo. CTA y slogan se centran en la franja `banda_y → H−268` — _brief del cliente; medido 07-09-2026 (septiembre lo violaba)_ · ✔×1
- **R-10** · Textos **literales del brief**, sin reescribir. El CTA del cierre del reel va completo (el del P08 trae dos frases) — _QA 24-09-2026, P08_ · ✔×1
- **R-11** · Ninguna palabra corta sola en una línea («2027?», «MÁS») y nunca «ANTONIO / RENDIC» partido. Interlineado alineado por la altura de la H, no por el tope de la línea (las tildes lo descuadran) — _QA 24-09-2026_ · ✔×1
- **R-12** · La foto se recorta con la **elipse medida** (feed: centro 540,−80 · rx 700 · ry 645; story: 540,−660 · 980 · 1570), nunca con un arco a ojo — _medición 07-09-2026, 4,5 px de error en feed_ · ✔×1
- **R-13** · Los tres pilares van juntos, en orden **PROPÓSITO / EXCELENCIA / BIENESTAR**, con antorcha / libro abierto / flor de tres pétalos, separados por filetes — _medido en las piezas de sept, 07-09-2026_ · ✔×1
- **R-14** · Titular en **Montserrat 850**, versales, tracking +0,003 em — _identificado por superposición de glifos (IoU 0,934), 07-09-2026_ · ✔×1
- **R-15** · Se entrega a **1080** de ancho, no a 1081 como septiembre — _medición 07-09-2026_ · ✔×1
- **R-16** · No repetir la misma foto en dos gráficas del lote si hay alternativa — _Sebastián Córdova, 23-09-2026: la P04 repetía la de la P06_ · ✔×1
- **R-17** · El slogan va **compuesto** en la letra del sistema; no se imita la mano de Diego. Si Diego entrega un lettering, reemplaza al compuesto — _decisión de Serena con Claude, 23-09-2026_ · ✔×1

## Lo que ya costó rondas
- **X-01** · Logo **blanco calado** (`ARC-blanco.png`): sobre foto se pierde — _octubre, todas las piezas, 08-09-2026, 1 ronda_
- **X-02** · Elipse que corta la cara de los niños de los costados en feed — _octubre, todos los post, 08-09-2026, 1 ronda_
- **X-03** · La firma manuscrita «Somos Familia Rendicina» — _octubre, 13 piezas, 23-09-2026, 1 ronda_
- **X-04** · La misma foto en dos gráficas (P04 = P06, juegos de patio) — _octubre, 23-09-2026, 1 ronda_
- **X-05** · Titular de reel compuesto a 0,80·W: «PROGRAMAS» y «BILINGÜE,» llegaban a x≈1004, dentro de la columna de íconos — _QA interno, 24-09-2026_
- **X-06** · CTA del cierre del P08 recortado (faltaba «Escríbenos por WhatsApp») — _QA interno, 24-09-2026_
- **X-07** · Llenado codicioso de líneas: «¿TE MUDAS A ANTOFAGASTA EN / 2027?» — _QA interno, 24-09-2026_
- **X-08** · Escalar el PNG completo del logo: el círculo sale 21 % más chico y descentrado — _08-09-2026_
- **X-09** · Tomar como referencia las piezas de marzo–junio (sistema anterior al cambio de imagen) — _manual, 07-09-2026_
