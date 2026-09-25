---
name: cliente-mascenter
description: "MASCENTER — cerebro del cliente: 29 reglas firmes, última cosecha 2026-09-25. Generado desde clients/mascenter/APRENDIZAJES.md; leerlo antes de diseñar para mascenter"
metadata:
  type: project
---

⚙️ **Nota generada por `scripts/memoria-cliente.py` en cada /cierre. No se edita acá:**
la fuente es `clients/mascenter/APRENDIZAJES.md` (léelo completo antes de producir; esto es
sólo lo más confirmado). ⛔ Vale sólo para mascenter: no se traspasa a otra marca.

Criterio: **Diego Aguilar (su criterio manda en las piezas; decisión final de marca: Valeria Traverso)** · Aprueba: **Sebastián Córdova (paid) · Francesca Pavissich (landings y presentación comercial)**

## Reglas más confirmadas
- **R-01** · La pieza del mes es la del mes anterior con otro contenido: el esqueleto de paid no se rediseña, se rellena, y tiene que confundirse con `LinkAd Tráfico a Ig 1 - post.png` — _medido en 4 meses de piezas aprobadas; manual §2, 04-09-2026_ · ✔×4
- **R-03** · Rojos de paid: pastilla y bajada `#DC1914`, burbuja CTA `#D80000`, ningún otro en la columna de texto — _6 piezas de septiembre + agosto; `reglas.yaml › rojo-de-sistema`, 04-09-2026_ · ✔×3
- **R-02** · En paid la tipografía es Montserrat, aunque el manual 2023 diga Poppins; la letra se identifica por glifos sobre la pieza aprobada — _Valeria lo vio a ojo y rechazó la ronda 1 («esa tipografía tampoco es»); medido glifo a glifo, 04/05-09-2026_ · ✔×2
- **R-04** · Medida exacta 1080×1080 / 1080×1920, nunca 1081 como entrega el cliente — _medición 02-09-2026; `marca.json › reglas_duras`_ · ✔×2
- **R-08** · Textos verbatim del brief; la conversión a versales la hace el sistema — _manual §6; QA del 24-09-2026 (tres pantallas pasan 7 palabras y no se tocaron)_ · ✔×2
- **R-10** · Los rótulos de locatarios reales se revisan a zoom 1:1; si la IA los reescribe, se parcha el letrero real con `parche_letrero.py` y no se insiste con el prompt — _Nano Banana Pro reescribió «cencosud» dos veces, 04-09-2026_ · ✔×2
- **R-14** · Reels con la pista de julio/agosto del cliente (~81 BPM, `pista-mascenter.m4a`); sin voz, el texto cuenta la historia — _Valeria, ronda 2 («sin música»), 05-09-2026_ · ✔×2
- **R-20** · Fotos «fachada o pasillo con gente», nunca stock genérico; los banners del home de `mascenter.cl` no sirven (stock europeo y cafetería) — _brief de octubre; landing terrenos, 02-09-2026_ · ✔×2
- **R-21** · Un cambio de cara al cliente se da por hecho sólo cuando `curl` a la URL en vivo lo muestra; commitear no es publicar — _Francesca vio el correo viejo un día entero, landing terrenos, 09-09-2026_ · ✔×2
- **R-22** · Un formulario publicado no promete lo que no hace: ni «Recibimos tu postulación» sin envío ni una subida de archivos que `mailto:` no transporta — _Francesca, rondas 5 y 6 de la landing de terrenos, 09/10-09-2026_ · ✔×2
- **R-28** · Una ronda se re-sube en sitio (mismo fileId y enlace, md5 verificado) — _paid octubre, 05-09 y 24-09-2026_ · ✔×2
- **R-05** · Logo blanco centrado, tinta 205–211 px, borde superior en y=64 (feed) / y=117 (story) — _`build.py › GEO`, medido sobre sept 2026_ · ✔×1
- **R-06** · Localito sólo en la campaña de comunidad; nunca en la de arriendo — _manual §1, 04-09-2026_ · ✔×1
- **R-07** · Localito completo, sangrado sólo por abajo, recortado por componentes conexas grandes (no por caja) — _error del 04-09-2026: arrastró «óxima visita.»_ · ✔×1
- **R-09** · CTA en la burbuja, en versales, siempre con «Síguenos»; sin emojis en gráfica — _manual §6_ · ✔×1
- **R-11** · Para feed 1:1 la foto va a nivel de calle con poco cielo, o se escala y sube (`--foto-top`) para que el logo caiga en cielo — _foto IA 3:4 con 40 % de cielo, 04-09-2026_ · ✔×1
- **R-12** · Cuerpo del reel con montaje del estudio: planos fundidos en 0,67 s con zoom lento 1,00→1,07, textos palabra a palabra con fundido y 26 px ease-out, pastilla con resorte sin rebote — _Valeria: «los textos llegan y aparecen, no tienen una transición suave, lo mismo con los frames», 05-09-2026_ · ✔×1
- **R-13** · El cierre del reel es la réplica exacta del cliente: panel rojo desde la izquierda 0,25 s, logo que baja y se asienta (tinta 405 px, y=840), texto que se escribe a ~80 car/s en Montserrat Regular ~57 px, 3,1 s sin fundido — _Valeria: «el cierre sácalo de las carpetas editables», 05-09-2026_ · ✔×1
- **R-15** · El primer frame del reel abre con logo y mensaje ya puestos: es la miniatura — _ronda 3, 05-09-2026_ · ✔×1
- **R-16** · Reel 9:16: ningún texto bajo y=1480-1500 ni a la derecha de x=900 (el brief marca 420 px abajo y 180 a la derecha); se revisa fotograma a fotograma — _QA de Serena, reels v4 → v5, 24-09-2026_ · ✔×1

## Lo que ya costó rondas
- **X-01** · Poppins en paid por seguir el manual sin medir — _paid octubre ronda 1, 04-09-2026, 1 ronda_
- **X-02** · Reels sin música — _ronda 1, 04-09-2026_
- **X-03** · Barrido y tiempos inventados; y también la copia literal del reel de agosto (tipeo letra a letra 0,32 s + golpe de rojo 0,30 s) — _rondas 1 y 2, 04/05-09-2026: costaron 2 rondas_
- **X-04** · Clip de Kling con letras finas que vibran — _Fashion's Park Coyhaique, ronda 4, 05-09-2026_
- **X-05** · Última línea del titular del reel dentro de la franja que tapa Reels (y=1606, x≈1020) — _reels v4 → v5, 24-09-2026_
- **X-06** · Rediseño «institucional» completo de la landing (grafito, filetes, comparador arrastrable) sin mostrar antes una sección de muestra: «no te quedó muy bien» — _landing de terrenos, 02-09-2026, 1 ronda; se volvió a la v1_
- **X-07** · Render de un proyecto identificable como hero de marca — _landing de terrenos, 02-09-2026_
- **X-08** · Correo genérico `contacto@mascenter.cl` en la captación de terrenos — _Francesca, 09-09-2026_
- **X-09** · Formulario que dice «Recibimos tu postulación» sin enviar nada — _landing de terrenos, 09-09-2026_
- **X-10** · Chevron como flecha flotando sobre la foto: «se veía barato» — _presentación comercial, 28-08-2026_
