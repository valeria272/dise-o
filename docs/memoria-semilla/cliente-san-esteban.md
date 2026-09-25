---
name: cliente-san-esteban
description: "SAN-ESTEBAN — cerebro del cliente: 18 reglas firmes, última cosecha 2026-09-25. Generado desde clients/san-esteban/APRENDIZAJES.md; leerlo antes de diseñar para san-esteban"
metadata:
  type: project
---

⚙️ **Nota generada por `scripts/memoria-cliente.py` en cada /cierre. No se edita acá:**
la fuente es `clients/san-esteban/APRENDIZAJES.md` (léelo completo antes de producir; esto es
sólo lo más confirmado). ⛔ Vale sólo para san-esteban: no se traspasa a otra marca.

Criterio: **Diego Aguilar** · Aprueba: **Sebastián Córdova** (medios, cuenta REM) · Orgánico: Scarlette Muñoz

## Reglas más confirmadas
- **R-01** · Compone **centrado sobre el abanico**: foto real arriba y abanico abajo en feed; en story el orden se invierte — _medición de Claude sobre las 7 gráficas aprobadas de sept, 07-09-2026_ · ✔×1
- **R-02** · Escudo y sello 110 **juntos**, nunca uno solo. Feed: escudo 120×143 en x=72, sello 174×152 en x=44, ~26 px de aire — _medición 07-09-2026_ · ✔×1
- **R-03** · El abanico lleva **los seis colores medidos**, sin agregar ni sustituir — _medición 07-09-2026_ · ✔×1
- **R-04** · Barra de CTA en **#011689**; #2A3E76 es sólo del escudo. No son intercambiables — _medición 07-09-2026_ · ✔×1
- **R-05** · Caja roja **#C0191A** con «Colegio San Esteban» en Poppins Bold blanco; «Hrvatska Skola San Esteban» sólo aparece en el escudo — _medición 07-09-2026_ · ✔×1
- **R-06** · Story: la barra de CTA se apoya por abajo en **y=1540** (340 px del botón de Meta + 40 de respiro), no en y=1739/1659 como septiembre — _Sebastián Córdova, 23-09-2026, stories P03, P04, P06, P07: «Moverlo más hacia arriba para que el botón de CTA no cubra el texto»_ · ✔×1
- **R-07** · Story y reel: **14 % arriba y 14 % abajo** sin texto ni logo; en reel, columna derecha libre — _brief del cliente, octubre 2026_ · ✔×1
- **R-08** · Todo texto en pantalla sale **verbatim** de la columna «TEXTO SOBRE LA IMAGEN». En el cierre del reel va el texto literal: el botón lo pone Meta, no se inventan barras — _brief; QA 24-09-2026 (P02 y P05)_ · ✔×1
- **R-09** · Nunca «San / Esteban» partido ni palabra sola en la última línea (`SIN_CORTE` en `build.py` + `text-wrap: balance`) — _QA 24-09-2026, P01, P04, P06, P07_ · ✔×1
- **R-10** · La story es la **adaptación del post**: misma foto, sólo cambia el encuadre, y va en el mismo envío — _brief: «ADAPTAR POST A FORMATO HISTORIA»_ · ✔×1
- **R-11** · Reel: ≤7 palabras por pantalla, se entiende sin sonido, gancho en los primeros 3 s y **primer fotograma legible solo** (la primera escena entra sin animación) — _brief de octubre; 07-09-2026_ · ✔×1
- **R-12** · En reel el escudo y el sello van **dentro del abanico** (y=490), no sobre la foto — _07-09-2026, reels de octubre_ · ✔×1
- **R-13** · Foto real de los alumnos con su uniforme. IA sólo para ambiente y objetos: nunca alumnos, uniforme ni escudo — _manual, 07-09-2026_ · ✔×1
- **R-14** · El uniforme (damero rojo y blanco, blazer azul marino, corbata a rayas) no se recolorea, no se retoca ni se cambia por stock — _manual, 07-09-2026_ · ✔×1
- **R-15** · Si el sello 110 cae sobre caras en story, **se corre la foto** hasta que caiga en el hueco entre dos personas; el sello no se mueve — _medido en las stories de sept, 07-09-2026_ · ✔×1
- **R-16** · Emojis sí en el copy del anuncio (🌐 web, 📲 WhatsApp); **en la gráfica, nunca** — _grilla de septiembre_ · ✔×1
- **R-17** · La línea de San Esteban se verifica en su **grilla de performance** (`1HoGFUlz7myLWdl0g0uq4X9lIGRkFtP7H`, piezas incrustadas), no en la carpeta del mes — _error del 07-09-2026_ · ✔×1
- **R-18** · Entrega a **1080 exacto** (septiembre salió a 1081, export de Canva) — _medición 07-09-2026_ · ✔×1

## Lo que ya costó rondas
- **X-01** · Barra de CTA de story en y=1739 / 1659 (como septiembre): el botón del anuncio la tapa — _stories P03, P04, P06, P07 de octubre, 23-09-2026, 1 ronda_
- **X-02** · Confundir el sistema con el de Rendic al buscar «la línea de septiembre» en el Drive: lo primero que aparece son piezas de Rendic (burdeo) — _07-09-2026, antes de diseñar_
- **X-03** · Barras de cierre inventadas en reel («Infórmate en nuestro sitio web», «Escríbenos por WhatsApp») y CTA recortado a tres palabras — _reels P02 y P05, QA interno 24-09-2026_
- **X-04** · «…de San / Esteban» partido — _P01, P04, P06, P07, QA interno 24-09-2026_
- **X-05** · Escudo sobre la foto en el reel: con una foto distinta cada 3,75 s tapaba una cara tras otra — _reels de octubre, 07-09-2026_
- **X-06** · Titular con *spring* en la primera escena: el fotograma 1 sale vacío y la miniatura no dice nada — _reels de octubre, 07-09-2026_
- **X-07** · Div de la foto a lienzo completo: `cover` escala al alto total y sólo se ven piernas y zapatos. Banda de foto: feed 0→700, story/reel 830→1920 — _07-09-2026_
- **X-08** · Dar por buena la carpeta de material del brief: «ADS San Esteban Octubre» (`16mznOKZjkKV7D53uKiKSOrc9T45wdwBh`) estaba **vacía** — _07-09-2026_
- **X-09** · El sistema anterior (azul marino degradado, caja roja, CTA ámbar, Admisión 2026) está **derogado** — _`marca.json`, grilla de septiembre_
- **X-10** · Una foto de Antonio Rendic (uniforme burdeo y gris) en una pieza de San Esteban — _manual, 07-09-2026_
