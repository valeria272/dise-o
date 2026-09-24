# Bitácora — San Esteban (Hrvatska Skola San Esteban)

## 2026-09-24 — Serena Abarca (con Claude)

**Qué se hizo:** El 23-09 se subió octubre a Drive por primera vez: 10 gráficas y
3 reels. Sebastián Córdova comentó las stories P03, P04, P06 y P07: *«Moverlo más hacia
arriba para que el botón de CTA no cubra el texto»*. La barra de CTA de las story pasó
a apoyarse por abajo en y=1540 (340 px del botón de Meta + 40 de respiro), en las cinco
stories, incluida la P01. El QA del 24-09 corrigió además los cierres de los reels P02
y P05, que traían barras que el brief no pide («Infórmate en nuestro sitio web»,
«Escríbenos por WhatsApp»); en el P05 el texto venía recortado. También quedaron sin
partir «San / Esteban» y sin palabras solas (`SIN_CORTE` + `text-wrap: balance`).
**Dónde quedó:** en Drive, en `ADS San Esteban Octubre / SAN ESTEBAN - Octubre 2026`
(`1nUO2yEjxNTz1oREE8wMj165axdaS_hy6`), con 1 GRAFICAS, 2 STORIES y 3 REELS. Se verificó
que los 13 archivos son idénticos a `out/san-esteban/octubre2026/` (md5). Los 4 comentarios
quedaron respondidos y **sin resolver**. El sistema se reproduce con
`sistema/build.py` + `render.sh` y los reels con `npx remotion render SE-Reel-*`, pasando
`--browser-executable` con el Chrome del sistema. El QA de la marca pasa las 10 piezas.
**Qué sigue:** esperar la revisión de Sebastián y leer sus comentarios nuevos en Drive.
**Abierto:** la sesión de fotos es de mayo de 2024: el colegio tiene que confirmar que
las autorizaciones de imagen de los alumnos cubren pauta pagada. Los copys de anuncio
del brief dicen «más de 100 años» y las piezas «110 años»: hay que igualarlos al pegarlos
en Meta. Falta el material de mudanza (cajas, camión) para P06, P07 y P08. `foto-estirada`
salta en los PNG por el abanico liso de arriba, que no es una foto estirada; en los JPG de
entrega no salta.
