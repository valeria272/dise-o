---
name: between-octubre-2026-estado
description: "Estado de la grilla de OCTUBRE 2026 de Between (30-09: carrusel To Go 01-10 entregado) — 11 piezas aprobadas y SUBIDAS (S1–S5/BW/{STS,FEED}), qué NO se diseñó y por qué, dudas abiertas, cómo retomar"
metadata:
  node_type: memory
  type: project
  originSessionId: 88852bf5-5031-4d18-afef-60e5f9185b04
  modified: 2026-09-29T14:41:55.171Z
---

Grilla `BETWEEN _ GRILLA OCTUBRE 2026.xlsx` (`1EnZOwUptY6SftX-CF9ZFwXUuzPCGZ76L`, gid FEED
`1537718358` · STORIES `1367300884`). Diseñado y aprobado por Eli el **24-09-2026**, en 4 rondas.

## ✅ Diseñado, aprobado y SUBIDO (24-09, 14:05)

Carpetas `HILTON/CONTENIDOS/2026/10. OCTUBRE/S<n> HILTON OCT 2026/BW/{STS,FEED}`
(las S<n> las creó Eli; BW/STS/FEED las creó `scripts/between-oct-subir-drive.py`).
La semana es la de la GRILLA, no la del calendario.

| Sem | Pieza | Archivo | Qué es |
|---|---|---|---|
| S1 | ST 01-10 | `BW ST 01-10 Anuncio ganador concurso.png` | adaptación del carrusel CEO del café (lámina aprobada + papel extendido) |
| S1 | ST 02-10 ANIMADA | `BW ST 02-10 Promos To Go POV.mp4` (+ PORTADA) | POV vaso To Go + muffin, Seedance 2.5, 8 s |
| S1 | FEED 05-10 | `BW FEED 05-10 Esa reunion podria ser un cafe.png` | manos brindando sobre 2 notebooks (azul/gris), muro verde |
| S2 | ST 05-10 | `BW ST 05-10 Paso por un cafe y.png` | collage 4 razones, sin caras, con flechas |
| S2 | ST 07-10 | `BW ST 07-10 Cafe gratis por cumpleanos.png` | vaso con vela + polaroid |
| S2 | ST 08-10 | `BW ST 08-10 Trivia Between.png` | vaso dibujado lleno de emojis Noto (repite 🥐) |
| S3 | ST 19-10 | `BW ST 19-10 Cowork.png` | POV cowork real, Excel + nota; tipografía «Coffee Break»; sin logo |
| S3 | ST 20-10 | `BW ST 20-10 Lo dicen ustedes.png` | cenital + 4 tarjetas review |
| S4 | FEED 14-10 | `BW FEED 14-10 Espacios Between.png` | muro verde real + personas en línea sobre el velo |
| S4 | ST 27-10 | `BW ST 27-10 Espacio para tu evento.png` | casi cowork en la banqueta real, sin caras |
| S5 | ST 28-10 | `BW ST 28-10 Desayuno Bonjour.png` | «08:00» + croissant jamón queso + flecha con rulo |

Las **GUIAS CM** (zona del sticker marcada: 01, 02, 05, 08, 27 y 28-10) NO se subieron:
quedan en `out/hilton/between/entrega-oct/GUIAS CM/`.

## ⛔ NO diseñado (y por qué)

- ST 26-10 «WTF es tomar solo un café al día» — dice **GRABAR ORGÁNICO** y hay nota de
  Scarlette a Nicolás: «creo que la ref no corresponde».
- ST 09-10 «Por qué vienes / por qué te quedas» — REVISAR CONTENIDO («me gusta más para reel»).
- ST 22-10 Info Between — REVISAR CONTENIDO («no digamos nada del estacionamiento»).
- ST 25-10 Promos To Go animada — EN REVISIÓN (y al Mediano le falta el precio).
- ST 29-10 Latte art spooky — PENDIENTE POR CLIENTE.
- FEED 02-10 carrusel To Go y 09-10 reel cumpleaños — REVISAR CONTENIDO; 07-10 almuerzos
  y 28-10 spooky — PENDIENTE POR CLIENTE.
→ Cuando cambien a OK PARA DISEÑAR, releer la grilla EN VIVO (CSV + gid) y diseñarlas con
  el mismo sistema.

## Abierto (no se le preguntó explícito a Eli; ella dijo «lo veo todo bien»)

1. 20-10 lleva los **textos de ejemplo del brief**: faltan reseñas reales.
2. 02-10 va «$2.990» (el brief dice «$2,990»).
3. 05-10 dice «UNA BUENA CONVERSA» (brief: «CONVERSACIÓN»).
4. 01-10: falta el @ del ganador (lo pone CM como mención).
5. 19-10 lleva «Between Coffee & Bar» con pin (calcado de la ref, no está en el brief).
6. Carpeta de historias llamada «STS» (como septiembre); Eli escribió «ST».

## Cómo retomar un cambio

- Código `src/compositions/hilton/BetweenOctubre.tsx`; rinde con
  `npx remotion still src/BetweenOctEntry.tsx BW-O-<id> <out> --scale=2.0833`
  (ids BW-O-01-Ganador … BW-O-F14-Espacios; el video con `remotion render`, sin scale).
- Fondos usados versionados en `public/assets/hilton/between/oct/`; escenas en
  `scripts/between-oct-generar.py` (claves 01-10 … f14-10b; crudos en `raw/…/oct/gen/`).
- Re-subir UNA pieza reemplazando el mismo archivo (conserva enlace):
  `python scripts/between-oct-subir-drive.py --solo "BW ST 19-10"`.
- Revisión en `out/hilton/between/oct-revision/index.html` (se arma con `_armar.py`).

## ✅ Ronda 29-09 + reel nuevo — APROBADO por Eli («quedó perfecta»)

Cliente comentó en la grilla (col C y D de STORIES pasaron a REVISAR CONTENIDO) dos
historias ya subidas. Hecho y aprobado el 29-09, en `out/hilton/between/oct-r2/`.
⛔ Se había dejado para que «Eli re-subiera ella» y Eli lo reclamó: lo aprobado SIEMPRE
se sube/reemplaza yo. **Subido 29-09 14:08** con `between-oct-subir-drive.py --ronda 2`
(md5 verificados): ST 01-10 y ST 02-10 (MP4+GIF+PORTADA) en S1/BW/STS; reel 12-10
(MP4+GIF+PORTADA) en **S4/BW/FEED** (bloque SEMANA 4 de la hoja FEED, junto al 14-10). Revisión: https://claude.ai/artifact/Sia5tJ5wXFHynRCBqYNfcq
- **ST 01-10 Ganador**: línea «Te contactaremos para entregarte la información de tu
  premio» bajo la caja del premio (nivel del premio, aire corto; cierre más separado,
  R-38). Bloque subido 30 px (el cierre pisaba el pelo de la modelo). Zona de mención de
  la GUÍA CM re-medida: estaba encima de «Te ganaste» desde la entrega del 24-09.
- **ST 02-10 To Go POV**: «muffin arriba del vaso, desproporcionado» → toma nueva: vaso
  en la mano derecha, muffin en su papel tulipa en la izquierda, a escala real (Nano
  Banana Pro 4K con refs vaso vigente + muffin real; de 2 variantes una traía la E normal
  → descartada, R-49). Animada con **Kling 2.5 Pro** 10 s. Fuera el «Yo:».
- **FEED 12-10 reel «Por qué vienes / Por qué te quedas»** (nuevo, OK PARA DISEÑAR):
  pantalla dividida como la ref, 7 clips REALES por lado, corte seco sincronizado cada
  1,6 s, 12 s, rótulo Raleway SemiBold 40 beige arriba (no al medio: R-41), sin rostros,
  sin audio. `scripts/bw-fd-12-10-porque-vienes-clips.py` (tramos + HLG→SDR) y
  `…-montaje.py` (ffmpeg, porque remotion.exe quedó bloqueado); composición gemela
  `src/compositions/hilton/BetweenFeed1210PorQue.tsx`.
- ⚠️ Eli: los reels están bien «como está todo, en las transiciones», pero **quiere
  conversar cómo mejorar los reels y va a pasar videos de referencia más adelante**.
  ✅ **Los mandó el 29-09** («tómalos de ref a futuro de animación»): ficha y tiras en
  `clients/hilton/referencias-animacion-bw/LEEME.md` (producto en mano con palabra en
  contorno, callouts de íconos, packshot con salpicadura IA, dibujo de línea → vaso real).
  Leerla ANTES de proponer cualquier reel o historia animada de Between.
- Pendiente de avisar al subir: el FEED «Esa reunión podría ser un café» la grilla lo
  corrió de 05-10 a 09-10 (R-65).

## ✅ Ronda 29-09 (tarde) — FEED 09-10 «Reúnete en Between» APROBADO y REEMPLAZADO en Drive

Es la pieza que era «Esa reunión podría ser un café» (misma foto, brindis sobre 2 notebooks);
la grilla le cambió texto y fecha. Eli, 4 vueltas en la misma sesión:
1. La bajada «Encuentra tu mesa…» se solapaba con los notebooks abajo → sube bajo «A TU
   JORNADA» (aire `tituloABajada`), corte «…en Between y» / «cambia la sala de reuniones por
   algo mejor» (la «y» ARRIBA), Raleway Bold 38 (antes SemiBold 32).
2. Pidió «un trazado» lifestyle → yo entendí una pincelada detrás (❌ no era eso).
3. Era un **contorno fino café de marca #675b49 alrededor de las letras**, relleno beige.
4. «Un poco más» y **sin puntas cuadradas** → SVG `<text>` con stroke 5 px, `paint-order:
   stroke fill` (asoman 2,5 px), `stroke-linejoin/linecap: round`, drop-shadow suave.
   `-webkit-text-stroke` NO sirve: une en inglete y deja picos en M, A, v, y.
«Quedó okey». Reemplazado 29-09 en **S1/BW/FEED** con el MISMO nombre
`BW FEED 05-10 Esa reunion podria ser un cafe.png` (conserva enlace; md5 5c632ded…).
Renders y antes/después en `out/hilton/between/oct-r3/` (entrega vieja: `f05-entrega-24-09.png`).
⚠️ Abierto → Eli: ¿renombrar a «BW FEED 09-10 Reunete en Between» y moverlo a la semana del
09-10? Se le preguntó 3 veces y no contestó; se dejó el nombre viejo.

Material de video del local: [[material-video-between-disco-f]].

Relacionadas: [[between-feedback-octubre-2026]] · [[between-sin-rostros-de-modelos]] ·
[[between-oct-tecnica-generacion]] · [[between-sistema-grilla]]

## 🔄 EN CURSO 29-09 — FEED 02-10 REEL cumpleaños (grilla col F, S1)

Eli: foto QUIETA hiperrealista lifestyle (el cliente odia lo que se nota IA) y SÓLO el
texto anima (máquina de escribir, juvenil, sutil); 1.er texto 2,5 s, el resto 3–4 s (2 s si
es corto), ~13 s; música/SFX en tendencia que acompañen cada texto; márgenes PAID.
Refs tipográficas suyas en `raw/hilton/between/oct/refs/f02-cumple/` (titular grande
condensado + textos chicos a los costados); ref de imagen = pin del vaso con vela.
Foto elegida: `gen-f02-10-f` → `public/assets/hilton/between/oct/f-cumple-reel.jpg`
(a → limpiar persona y dedos (d) → achicar en lienzo gris + rellenar bordes (f); pedir
«extiende hacia arriba» sobre una foto que YA es 9:16 no extiende nada).
Falta: el reel de referencia de animación que Eli dijo que iba a mandar.
**v1 lista 29-09 (esperando a Eli):** `src/compositions/hilton/BetweenFeed0210Cumple.tsx`
(Thumbnail + `scripts/reel-por-chrome.mjs` fotograma a fotograma, 375 cuadros ~7 min) +
`scripts/bw-fd-02-10-cumple-audio.py` (música ElevenLabs v2 + SFX en los mismos
fotogramas, loudnorm −14) → `out/hilton/between/oct-r2/BW FEED 02-10 Cafe de cumpleanos.{mp4,gif}`
+ PORTADA. Revisión: https://claude.ai/artifact/NBkRUUAPydG7A82b2188Kz. Hook: figura
recortada (imgly) ENCIMA del titular para que la vela pase por delante. Pins de Eli
(hooks y animación) en `raw/.../refs/f02-cumple/pins/` con hojas de contacto.
Al aprobarse: subir a S1/BW/FEED (bloque SEMANA 1 de la hoja FEED).
**Ronda 2 (29-09, Eli):** hook OK («va acorde con la música»). Pidió: legal en «botones»
café (caja taupe del sistema, 5 cajas con rebote), ilustraciones MÁS LINDAS «globitos que
van surgiendo» → se usan las ORIGINALES de Eli (`recursos/globos-par`, `globo-alt`,
`confeti`), nunca trazos SVG míos; y «al final la velita encendida» → la vela parte
APAGADA (`f-cumple-apagada.jpg` = foto aprobada + sólo la elipse de vela/dedos de una
edición NB «vela apagada», desfase 1 px) y se enciende en f256 con fósforo + golpe de luz.
**Ronda 3 (29-09, Eli):** la vela se enciende AL INICIO (es el hook: fósforo f-18→f4,
«¿ESTÁS» en f12). Confeti al FINAL «mirando hacia la vela»: dos abanicos anclados por su
vértice (93 %·89 % del PNG) junto a la llama, el derecho = `confeti-espejo.png` (espejar con
CSS scaleX + rotate desde el vértice se descuadra). Legal: 5 botones café CENTRADOS sobre
el eje de la vela, giros ±1,2° alternados («mejor diagramado»). Eli: «con eso estaría bien».
✅ **APROBADO y SUBIDO 29-09** (ronda 3, «maravilloso, quedó bacán»): MP4 + GIF + PORTADA en
S1/BW/FEED, md5 verificados. Receta y análisis: [[between-reel-texto-animado-receta]].

## ✅ Ronda CONSTANZA (jefa de diseño) 29-09 — S1–S2, REEMPLAZADO en Drive el 29-09 (md5 = local)
4 comentarios NATIVOS en la grilla (FEED F10, STORIES C9/D9/H9, 16:27–16:30): no salen en el
CSV vivo, sí en `xl/comments*.xml` del blob bajado por usercontent (blob `BW-oct-20260929c.xlsx`).
- ST 01-10: 3 voces Raleway (titular 800/112 ambas líneas iguales · cajas 800/45 · texto 600/36,
  sin itálica). «No queda bien delineado» = el halo de 24 sombras salía ESCALONADO → titular en
  SVG, 2 `<text>` (trazo redondo 14 debajo, relleno encima).
- ST 02-10: `aireEntreCapsProp={-0.2}` (nueva prop opt-in del kit: la tinta incluye «¿» y tilde
  de Ñ, con 0,14 no se veía cambio); caja «Muffin…» al ancho del horario, 41 SemiBold caja baja.
  Capa de texto con alfa (`reel-por-chrome.mjs --escala 2 --transparente`) + ffmpeg sobre la toma.
- ST 07-10: `AIRE_REGALO=-4` (con −26 la «g» tocaba «TU»), bajada lineHeight 1,12.
- Reel 02-10: todo Raleway Black (fuera Brushwell y la fina espaciada); extendido por mí a
  «CAFÉ GRATIS» (avisado en la página). Mismos tiempos → misma pista de audio
  (`BW_F02_CUADROS`/`BW_F02_OUT` en el script de audio).
Renders en `out/hilton/between/oct-r4/`; revisión https://claude.ai/artifact/J6x6wh5aiS9mrRtjJYpNJQ
Esperando visto bueno de Eli (ya está subido, como pidió).
⛔ `reel-por-chrome.mjs` compartía `raw/_reel-chrome` entre sesiones y otra sesión le pisó el
paquete a mitad de render (salió un fotograma de DT): ahora usa `tmp-<pid>`.
**Ronda 5 (Eli, 29-09):** ST 01-10 y ST 07-10 APROBADAS. ST 02-10: «la Ñ muy cerca de la M y la E»
→ `aireEntreCapsProp={-0.08}` (el −0,2 quedó demasiado junto). Reel: «VA POR» se leía «VAPOR» →
«EL CAFÉ VA POR» / «NUESTRA CUENTA» en dos líneas, `wordSpacing 0.15em` en «VA POR». Eli: «la
última (café gratis en sans) me gusta mucho como está». Con esto la grilla S1–S2 queda para
finalizar. Reemplazado en Drive (md5 = local) desde `out/hilton/between/oct-r5/`
(`between-oct-subir-drive.py --ronda 5`); revisión https://claude.ai/artifact/UfbuqNRSwGjgSv9jgwVRrz
✅✅ **APROBADO FINAL por Eli 29-09 («quedó perfecto»)**: ST 01-10, ST 02-10, ST 07-10 y reel FEED
02-10. Las 8 piezas re-verificadas en Drive contra el local (md5 igual). S1–S2 de octubre CERRADAS.

## 🔄 Ronda 6 (29-09 noche) — hilos Nicolás + Scarlette, YA REEMPLAZADO en Drive (md5 = local)
Hilos nativos del blob `BW-oct-20260929e.xlsx` (el conector no trae hilos de un .xlsx):
- STORIES!H13 Nicolás → ST 07-10: «*Imagen referencial.» abajo a la IZQUIERDA (al centro pisa el
  vaso) + «Happy Birthday ♥» en Brushwell en el margen de la polaroid (−9,8°, `POLA` en BetweenOctubre.tsx).
- FEED!F15 Scarlette → reel 02-10 «el fondo no se ve muy between»: fondo = jardín de invierno real
  (muro verde, piedra, guirnaldas) con NB Pro sobre la foto aprobada + `scripts/bw-fd-02-10-cumple-fondo.py`
  (alinea ECC, persona = imgly ∪ sweater por color, relleno por convolución normalizada, desenfoque,
  rehace `f-cumple-figura*.png`). ⚠️ `f-cumple-mascara-llama.png` es el GOLPE DE LUZ, no la llama.
- FEED!E11 Scarlette → @nicolas (carrusel To Go): contenido, no se diseña.
Renders `out/hilton/between/oct-r6/`, respaldo `oct-r6-respaldo/`; revisión https://claude.ai/artifact/LZqNpVUS8ZMyD9sbjUoMxb
Esperando visto bueno de Eli.
**Ronda 7 (Eli, 29-09):** «Happy Birthday» centrado en el margen de la polaroid → giro −10,8°,
Brushwell 24, `POLA = {x: 801.5, y: 1874.5}`; aire 50·50 lados y 45·46 arriba/abajo (medido en el eje
de la polaroid). Reemplazada en S2/BW/STS (md5 = local); revisión https://claude.ai/artifact/PEHmsoQPjpTjb7Dz89Co5S

## 🔄 Ronda 8 (30-09) — reglas nuevas desde la S3 + orden por semana, YA en Drive (md5 = local)
Eli: aplicar las reglas nuevas (R-140 voces, R-142 interlineado, R-144 cajas, R-118 bajada feed)
SÓLO de S3 en adelante; S1–S2 están en revisión y NO se tocan. `scripts/between-oct-r8.py`
(`--listar` = árbol BW S1–S5): la grilla movió el reel 12-10 y el FEED 14-10 al bloque SEMANA 3 →
movidos de S4 a **S3/BW/FEED** (mismo id/enlace); `between-oct-subir-drive.py` ya los apunta a S3.
Cambios (renders `out/hilton/between/oct-r8/`, antes en `oct-r8/antes/`): Bonjour 28-10 «11:30» se
leía «1 1:30» (caja tabular con dos 1 seguidos → el «11» va proporcional con lnum), cajas a 560 px,
bajada SemiBold, `aireEntreCapsProp={0.1}`; Evento 27-10 y Espacios 14-10 interlineado 0,1; 14-10
bajada Bold 38; 20-10 cierre sin itálica. Cowork 19-10 y reel 12-10 cumplían. Revisión:
`oct-r8/revision-r8.html` (abierta en Chrome). Esperando visto bueno de Eli.
Abierto → Eli: FEED «Reúnete» (09-10, SEMANA 2) sigue en S1 con nombre viejo.
**Ronda 9 (Eli, 30-09):** resto de la ronda 8 «lo veo bien». FEED 14-10: titular «muy junto» con 0,1 →
`aireEntreCapsProp={0.2}`; bajada «Café, comodidad y buenos» / «momentos en Between». Reemplazado en
S3/BW/FEED (md5 = local). Grilla viva 15:00 calza con Drive S3–S5; ST 26-10 WTF → POR GRABAR.

## ✅ 30-09 tarde — FEED 01-10 carrusel PROMOS TO GO (col E, S1) — APROBADO A LA PRIMERA («me encantó»), en Drive · receta [[between-carrusel-producto-receta]]
4 láminas 2250×2812 en `out/hilton/between/oct-fd01/` y YA en **S1/BW/FEED** (md5 = local,
`between-oct-subir-drive.py --ronda fd01`). Revisión `oct-fd01/revision-fd01.html` (abierta en Chrome).
Escenas NB Pro 4K (claves `fd01-1..4` y `fd01-4e` en `between-oct-generar.py`) con el trío de vasos
aprobado 22-09 + comida de la sesión 25-jul-2025; mesa + muro verde. Código `FeedOct01ToGo1..4` en
BetweenOctubre.tsx (ids `BW-O-F01-ToGo-1..4`). Lám. 1 = rótulo nombre+precio sobre cada vaso (calco
de la ref «NON COFFE»); 2–4 = fila de 3 precios bajo título, horario al pie, «*Imágenes referenciales.».
La celda de refs dice «REF - REF 2 - REF 3» pero el xlsx sólo trae un enlace (pin 678706606388884542).
Dudas abiertas en la página: variar café (vasos tapados), jamón queso y brownie generados, R-62 vs brief.
⚠️ El xlsx por `drive.usercontent…&confirm=t` SÍ trae los hilos nativos (xl/comments1.xml) y los enlaces.
**Ronda 2 (Eli, 30-09):** «Café» antes de Mediano/Grande/XL; rótulos de la portada centrados en el eje
de cada vaso (225/531/844); flechas punteadas con rulo + acentos como la ref. Reemplazado en S1/BW/FEED
(md5 = local), respaldo `oct-fd01/antes/`, revisión `oct-fd01/revision-fd01-r2.html`. Eli: «con eso ya estaría».
**Ronda 3 (Eli, 30-09):** rayitas de acento «más grandes y mejor diseñadas» (muestra de 3 cuñas) → cuñas en abanico. Reemplazado en S1/BW/FEED (md5 = local), respaldo `oct-fd01/antes-r2/`, revisión `revision-fd01-r3.html`.
✅✅ **APROBADO FINAL por Eli 30-09 («me gustó el resultado»)**: las 4 láminas del carrusel To Go 01-10 (ronda 3) en S1/BW/FEED, re-verificadas contra el local (md5 igual, un archivo por nombre).
📁 **30-09 (Eli):** renombrado y movido en Drive a **S1/BW/FEED/C1 togo S1/** (`1ExY-2WHkqduzgAdi2Eo7nARAFIbucPIM`) como `C1 n°1…4 togo S1.png` (mismos enlaces, md5 = local). Regla: [[carrusel-nombre-y-carpeta-c1]].
**Ronda 4 (Eli, 30-09):** portada con 3 flechas punteadas, una a cada rótulo de café; láminas 2–4 sin flechas (quedan las cuñas). Reemplazado en `C1 togo S1` (md5 = local), respaldo `oct-fd01/antes-r3/`.
**Ronda 5 (Eli, 30-09, con garabato):** portada — cada flecha sale del precio, rulo sobre la tapa, entra al vaso; lo demás «bien». Reemplazada en `C1 togo S1` (md5 = local), respaldo `antes-r4/`.
**Ronda 6 — FINAL (Eli, 30-09, «y terminamos»):** rótulos Mediano y Grande a la altura del XL; flechas alargadas. Portada reemplazada en `C1 togo S1` (md5 = local), respaldo `antes-r5/`.
