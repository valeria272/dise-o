# SANTA GOTA — bitácora

## 2026-09-21 · Valeria (con Claude) — TV: el cliente salió con la versión de la MONJA; se le agrega el cierre de Instagram

**Qué pasó (correo «TVN / Santa Gota Virgen / 2026»):** el 15-09 Valeria mandó por WeTransfer el paquete de TVN; el
16-09 mandó `final-santagota screen.mp4` («UNA SOLA GOTA / LO CAMBIA TODO», hecho fuera del repo); el 20-09 Gonzalo
avisó: «mandé al canal el anterior porque este no me tincó». **El anterior = el full de 18 s con la monja** y cierre
lima («EL ACEITE DE OLIVA QUE LLEGÓ A REVOLUCIONAR TU COCINA» → logo → «COMPRA EN TODO CHILE / EN SANTAGOTA.CL»).
Toda la ruta «UNA GOTA. CAMBIA TODO.» (keyframes V1–V3, animatics V1–V5) queda archivada: no salió.

⚠️ Esa versión NO es la Fase 2 del repo (commit `4eb07bd`, que no tiene envases en pantalla): la hizo otro agente y su
proyecto no está versionado. La única fuente es el MP4 que Valeria bajó de WhatsApp
(`WhatsApp Video 2026-09-14 at 18.18.00.mp4`, 1920×1080 · 29,97 · 540 cuadros · 3 Mb/s, cuadros duplicados de a pares),
copiado a `public/assets/santagota/tv-cliente/full_cliente_whatsapp.mp4`. Sigue con la botella verde ensanchada que
reclamó Gonzalo el 15-09: no se tocó porque no se pidió.

**Pedido:** agregar al final el ícono de Instagram con «Síguenos» y el perfil `santagota.cl`.
**Hecho** (`src/compositions/santagota/tv-cliente/FullClienteIG.tsx`, `SG-FULL-CLIENTE-IG` y `…-CAPA`): tercer estado
del cierre con la misma mecánica del original, sin alargar los 18 s: en el cuadro 440 un parche del color exacto del
panel (rgb 5,37,44) apaga «COMPRA EN TODO CHILE» y desde el 450 suben por máscara «SÍGUENOS EN» (Montserrat 700/58) ·
«INSTAGRAM» (800/102) · glifo + «@SANTAGOTA.CL» (800/56, lima 190,212,1); columna en x = 1319, el subrayado naranja
original (y 680) se conserva.
⛔ **Remotion decodifica ese MP4 un cuadro atrasado** (PSNR 24 dB contra el original): se rinde SÓLO la capa con alfa
(`--sequence --image-format=png --frames=436-539`) y se monta con ffmpeg `overlay` sobre los cuadros originales
(`setpts=PTS+436/fps/TB`, `eof_action=pass`) → PSNR 51 dB, 540 cuadros, audio original copiado sin recomprimir.

⛔ **El video de ese MP4 arranca en 0,0667 s (2 cuadros después que el audio).** La primera entrega cerraba 2 cuadros en
el texto ORIGINAL (Valeria lo vio al pausar al final): la capa quedaba 2 cuadros adelantada y `eof_action=pass` dejaba
pasar el original. Corrección: desfase de la capa = (436 + 2) cuadros (`setpts=PTS+(438*1001/30000)/TB`) y
`eof_action=repeat`; NO usar `-shortest` ni `-t` (se comen cuadros del final). Verificado cuadro a cuadro: 540 cuadros,
los últimos 72 en «SÍGUENOS», último cuadro incluido, también en el MXF.

**Entrega** (`out/santagota/tv-cliente/` + Escritorio): `SANTA_GOTA_FULLSCREEN_con_Instagram.mp4` (H.264 crf 12) y
`SANTA_GOTA_FULLSCREEN_1920x1080_2997_con_Instagram.mxf` (OP1a XDCAM HD422 50 Mb/s, TFF, BT.709, PCM 16/48, −24 LKFS).

## 2026-09-15 (noche, 7) · Valeria (con Claude) — SPOT TV · ANIMATIC V5 (segundo feedback de voz)

**Lo que dijo Valeria (voz):** la escena 1 es muy similar a la 2 → partir con la 2 y darle más tiempo; el copy «UNA SOLA
GOTA… LO CAMBIA TODO.» en grande y que se entienda que hablamos de aceite de oliva; la persona echando aceite se ve muy
falsa → más natural, botella más chica, de lejos; la botella sola definitivamente no funciona; que el cierre sea el
placement de los cuatro y que aparezca «cómpralo en todo Chile, santagota.cl».

**Entrega:** `out/santagota/spot/animatic-v5/SANTA_GOTA_ANIMATIC_V5_{con-cama-temporal,sin-musica}.mp4` (+ WAV) y copia
en el Escritorio. Composición `SG-ANIMATIC-V5` (`AnimaticV5.tsx`); mezcla `… --v5` con `SG_MUSICA=musica-v4`.
Página: https://claude.ai/artifact/7JPexiPCeBJ7f3qscXYnax (misma URL, versión 5).

**Montaje V5 (cuadros):** 01 gota 0–84 · 02 PLOP 84–108 «UNA SOLA GOTA / DE ACEITE DE OLIVA…» · 03 cambio 108–150
«LO CAMBIA TODO.» · 04 pizza 150–195 · 05 sartén 195–249 · 06 pasta 249–306 · 07 la mesa 306–375 · 08 PLOP + onda →
placement de los cuatro 375–449 · 09 claim 449/480 · gota final 509–528 · 10 onda → logo + CTA 528–599 HOLD.

**Qué cambió**
- Fuera el cliché; `GotaLibre` abre con 84 cuadros (cuelga 14, cae 70, push 7 %).
- Copy: «UNA SOLA GOTA» 150/900 + «DE ACEITE DE OLIVA…» 64/300 en el PLOP; «LO CAMBIA TODO.» 176/900 (TODO en lima).
- **La mesa** (`santagota-spot-ensalada-nano.py --abierto`): Nano Banana con la referencia del packshot CHICO (h 300 de
  768) en pose de vertido → `v8_mesa_v1` (salió letterboxed 2,2:1: se recorta a 16:9 `v8_mesa_v1_169`, 2× precisión;
  ⚠️ el primer upscale del original completo falló «sin entregar imagen», el del recorte anduvo). Packshot oficial
  pegado con `--punta 998,736 --base 1002,548 --escala 1.05` → `public/assets/santagota/spot/mesa_still/0001.png`;
  push-in 6 % + travelling ±8 px + hilo vivo (placa en screen, w 420, sx 0,35).
- Inserto macro de la botella sola: eliminado. La onda 1 del set descubre a los CUATRO (latas incluidas).
- CTA con el logo (cuadro 546): «CÓMPRALO EN TODO CHILE» 34/700 + «SANTAGOTA.CL» 60/900 lima, bajo el claim.
- Audio v5: PLOP 84 · cambio 108 · mesa con aire cálido 306–375 · PLOP 381 + sting · PLOP 528 + sting final.

**Pendiente:** OK de Valeria → producción (rodar la mesa con mano real; placas finales; gotas reales) → master MXF.
Nada commiteado aún (`/cierre`).

## 2026-09-15 (noche, 6) · Valeria (con Claude) — SPOT TV · ANIMATIC V4 (feedback de voz sobre la V3)

**Lo que dijo Valeria (voz):** un plano parece lava y no comida; la botella sola sin mano se ve rara → mejor una persona
echándole aceite a una ensalada con amigos, más real; al final el placement completo que se luzca; que todo tenga una
tonalidad y suene acorde a los tiempos, que conecte, que haya storytelling.

**Entrega:** `out/santagota/spot/animatic-v4/SANTA_GOTA_ANIMATIC_V4_{con-cama-temporal,sin-musica}.mp4` (+ WAV) y copia
en el Escritorio. Composición `SG-ANIMATIC-V4` (`AnimaticV4.tsx`); mezcla `… --v4` con `SG_MUSICA=musica-v4`.
Página: https://claude.ai/artifact/7JPexiPCeBJ7f3qscXYnax (misma URL, versión 4).

**Qué cambió**
- **CAMBIA TODO = comida.** Placa `v4_universo_comida_v1` (Mystic: el MISMO plato de burrata y tomate sobre piedra negra
  con luz dura dorada y el anillo en el aceite) → Kling `universo_comida` (el anillo se expande, una hoja tiembla). Fuera
  la «lava» (`v4_universo_v2`).
- **Reveal con amigos.** `scripts/santagota-spot-ensalada-nano.py`: Nano Banana con REFERENCIA del packshot oficial en
  pose de vertido (16:9, `rotate(150)` = boquilla ABAJO). ⛔ La primera referencia (`rotate(-125)`) dio una botella con
  el aceite saliendo por la BASE y Kling la siguió; con la boquilla abajo y el prompt «el hilo cae DESDE la boquilla
  amarilla, la boquilla es el punto más bajo» las tres variantes salieron bien. Elegida `v7_ensalada_v1` (2× precisión).
  ⛔ Kling (3 intentos, «cámara fija, no reencuadrar») siempre mueve la botella 100–200 px y la deforma: el clip no sirve
  para pegar el packshot. Solución: **foto compuesta** (`santagota-spot-mano-video.py --lifestyle --punta 1105,525
  --base 1385,38 --escala 1.04` → `public/assets/santagota/spot/amigos_still/0001.png`: packshot oficial anclado a la
  punta con puntos manuales, dedos delante por piel ∧ alfa, hilo por banda) + en Remotion push-in 4 % + travelling
  −10 px + el hilo VIVO (placa en screen fluyendo desde la boquilla). 10:20–11:71. Después inserto macro de la última
  gota (11:71–12:51) → aterriza en el hero → PLOP → onda. En producción esta toma se rueda.
- **Placement final más grande:** grupo de productos corrido a la izquierda (750 cx 570 · 500 cx 845 · lata cocinar cx 315
  h 610 · lata aderezar cx 1000 h 595, descubre hasta 0,96) y claim a 100/44/46 px para que REVOLUCIÓN no pise la lata.
- **Tono común:** velo radial cálido en `soft-light` (zIndex 35) sobre 0–351 (toda la comida); el estudio negro no se toca.
- **Cama musical más actual:** `musica-v4` (percusión orgánica, bajo cálido, piano eléctrico, energía constante hasta el
  s 15 y se apaga sola bajo el hero). `musica-v5` (trap/808) descartada por irregular.

**Pendiente:** OK de Valeria → producción (rodar la escena con amigos con mano real + proxy + tracking; placas finales;
gotas reales) → master MXF OP1a 50 Mbps + PCM 24/48. Nada commiteado aún (`/cierre`).

## 2026-09-15 (noche, 5) · Valeria (con Claude) — SPOT TV · ANIMATIC V3 (última ronda de refinamiento → GO a master si pasa)

**Feedback a la V2: «muy bien encaminada, no rehacer, última V3».** Regla final: no agregar efectos; menos aceite, cero
deformación, movimiento por cámara/luz/foco/montaje/sonido. Después de esta V3: GO a producción/master si el packaging
y las latas siguen 100 % fieles.

**Entrega:** `out/santagota/spot/animatic-v3/SANTA_GOTA_ANIMATIC_V3_{con-cama-temporal,sin-musica}.mp4` (+ WAV) y copia
en el Escritorio. Composición `SG-ANIMATIC-V3` (`AnimaticV3.tsx`); mezcla `… --v3` (el PLOP del reveal cae en 381 = al
aterrizar en el hero). Página: https://claude.ai/artifact/7JPexiPCeBJ7f3qscXYnax (misma URL, versión 3).

**Qué cambió**
- **00–03 gota libre.** ⛔ Ni Mystic (3 placas «gota libre, sin hilo») ni Kling (2 intentos con prompt explícito)
  entregan una gota sin hilo: siempre la cuelgan. Solución 2D: de `v4_gota_libre_v1` se recorta la gota con elipse
  plumada (`v5_gota_libre_gota.png`, caja 1230,320–1540,820) y el hueco + el hilo se rellenan interpolando el bokeh por
  filas (`v5_gota_libre_fondo.png`); en Remotion (`GotaLibre`) la gota cae 181 px con ease-in hasta el borde de la
  burrata y el grupo hace un push de 5 %. El cliché se escala 1,15 anclado abajo para sacar el hilo del borde.
- **06 sartén con comida** (`v4_sarten_food_v1` → Kling `sarten5`, entra a 2,4 s): camarones, cherry, ajo, romero;
  el flare dura ~15 cuadros y muere solo.
- **07 pasta** (`pasta5`, prompt «NO droplets»): sólo el hilo. Entra a 0,3 s.
- **08 reveal parcial:** cámara z 2,2 → 1,35 centrada en (tip+330, tip−40): boquilla + hombro + arranque de la
  etiqueta (se lee SANTA GOTA); la botella nunca se ve entera. Última gota → la cámara la sigue → sin negro: el fondo
  ya es negro y la botella sale por arriba.
- **Transición al hero:** la gota del reveal entra por arriba del hero (x 514), aterriza al pie de la botella naranja en
  el cuadro 6, PLOP, y una **onda 1** (anillo + luz radial) descubre las botellas (estaban a brightness 0,02). Mismo
  dispositivo que el cierre = gesto de marca.
- **Claim jerárquico:** SOMOS LA 48/700 tracking 0,2 em · REVOLUCIÓN 112/900 lima · DEL ACEITE DE OLIVA. 50/300; bloque
  a la derecha a SAFE_X. Logo 320 px arriba (top 330) con la onda final.
- **Family shot:** sin cambios de mecánica (luz descubre latas + logo), la cámara se frena con ease-out hasta el HOLD.

**Pendiente:** OK de Valeria a la V3 → producción: rough cut con placas finales (rodar/regenerar lo que no pase
«nada parece IA», bajar el universo del cambio, gotas reales en macro) → master MXF OP1a 50 Mbps + PCM 24/48.

## 2026-09-15 (noche, 4) · Valeria (con Claude) — SPOT TV · ANIMATIC V2 (feedback consolidado V1 → V2)

**Ruta y storytelling aprobados; la V2 refina.** Regla: MENOS ACEITE, MÁS IMPACTO. Nada se rehizo desde cero.

**Entrega:** `out/santagota/spot/animatic-v2/SANTA_GOTA_ANIMATIC_V2_{con-cama-temporal,sin-musica}.mp4` (+ WAV) y copia en
el Escritorio. Composición `SG-ANIMATIC-V2` (`AnimaticV2.tsx`); mezcla `santagota-animatic-mezcla.py … --v2`.
Página: https://claude.ai/artifact/7JPexiPCeBJ7f3qscXYnax (misma URL que la V1, republicada).

**Qué cambió**
- Placas V4 (`scripts/santagota-spot-plates-v4-freepik.py` → Mystic, 3 variantes c/u; Kling 2.5 encima): gota
  delicada (v1), impacto chico (plop v3), universo del cambio (v2, anillo con luz y brasas, sin llamas grandes —
  igual quedó con una columna de luz que en el rough cut se baja), pizza con hilo fino y queso mate (v1).
- **CAMBIA TODO** = onda de luz: `clip-path: circle()` que crece desde el punto de impacto (14 cuadros, ease-out)
  abriendo el universo nuevo sobre el plop, con un borde de luz dorada que viaja con el círculo. Sin explosión.
- Sartén: el clip entra a 3,0 s (flare muriendo: unos cuadros y se apaga). Pasta: 0,2–2,1 s, antes del splash.
- **REVEAL SIN MANO.** La mano generada se eliminó siguiendo la regla de Valeria («mejor sin mano que una
  interacción IA mediocre»; ella vio deformación del packaging en la V1). La botella es el packshot oficial
  RÍGIDO (`hero4-750`, −100°, tip (470,600), h 1480) cruzando el cuadro entero: la mano queda fuera. Respira
  0,5°. Hilo fino (sx 0,5) → último squeeze (cuadro 340) → el hilo se adelgaza y corta → gota se desprende (354,
  placa `v2_gota_firma` a w 420 recortada al 52 % superior, punta en la boquilla) → la cámara la acompaña
  (tilt 0,9 × caída, g = 3,6 px/f²) → negro (364–373) → PLOP al corte (375) → HERO.
- **HERO en un solo set 375–599:** travelling lateral 18 → −22 px + push-in 1,00 → 1,04; recorrido de luz sobre el
  packaging (banda en `screen` recortada con `mask-image: url(packshot)`); rack focus al 2º beat (la de atrás
  1,4 → 0,3, la de adelante 0 → 0,9), la gota final se lleva el foco, vuelve delante tras el PLOP.
- **CIERRE:** gota en primer plano (x 1330, cae 509–528 con ease-in, blur 7 → 0) → PLOP (528) → anillo elíptico en
  el piso (screen, se apaga solo) + luz radial que recorre el set → las latas (`hero4-lata-*`, rim 0,30, Δ 3,9)
  ya estaban en el set a brightness 0,02 y se descubren por distancia a la onda → logo (544) → último recorrido de
  luz (568–594) → HOLD hasta 599. Sin fades, sin slides, nada entra.
- Audio V2: tres PLOP hermanos (96 · 375 · 528) como firma sonora; impacto del cambio en 118; squeeze 336 /
  click 340; sting suave 375 y sting pleno 531.

**Pendiente:** OK de Valeria → rough cut (placas finales, gotas sobre negro real, mano real con proxy + tracking si
se rueda, universo con menos fuego) → master MXF.

## 2026-09-15 (noche, 3) · Valeria (con Claude) — SPOT TV · ANIMATIC completo (V3 aprobada, storyboard cerrado)

**V3 aprobada.** Dos condiciones de ejecución: REVEAL con mano que se mueve de verdad (entra, microinclinación,
presión, aceite físico, packaging intacto) y HERO con negro más profundo, botellas asentadas (sombra + reflejo +
contacto), rim mínimo, micro push-in óptico. Siguiente entrega: animatic 1920×1080 · 29,97 · 19–20 s con montaje
real, copy, música temporal y sound design completo.

**Entrega:** `out/santagota/spot/animatic/` — `SANTA_GOTA_ANIMATIC_con-cama-temporal.mp4` y `_sin-musica.mp4`
(599 cuadros = 19,987 s, 29,97, H.264 + AAC) + las dos mezclas en WAV 24/48. Composición `SG-ANIMATIC`
(`src/compositions/santagota/spot/Animatic.tsx`); se renderiza en el sandbox y el audio se mezcla aparte con
`scripts/santagota-animatic-mezcla.py` (mux con `tools/ffmpeg`).

**Montaje (cuadros):** 01 cliché 0–60 · 02 gota 60–96 · 03 PLOP 96–114 («UNA GOTA.») · 04 big bang 114–150
(«CAMBIA TODO.») · 05 pizza 150–195 · 06 sartén 195–249 · 07 pasta 249–306 · 08 reveal 306–381 (CLICK 352) ·
09 hero 381–465 · 10 hero 465–546 · 11 firma 546–599 (PLOP 584, negro desde 588). Todo a corte seco.

**Placas en movimiento** (`scripts/santagota-animatic-clips.py` → `public/assets/santagota/spot/clips/`): Kling
2.5 Pro vía Freepik, 5 s, 1928×1072 a 24 fps. ⚠️ **Kling 2.1 Pro falló 12/12 con `error: null`** esa noche,
incluso con `magnific-video.py`; la 2.5 anduvo pero no acepta `image_tail`. Sólo se animaron placas SIN producto.

**08 REVEAL en movimiento — cómo se hizo sin tocar el packaging** (`scripts/santagota-spot-mano-video.py`): Kling
animó el ensayo de la mano con el envase GENÉRICO (`mano_gesto.mp4`: muñeca que inclina, dedos que aprietan, hilo
que fluye). Cuadro a cuadro: PCA del cuerpo dibujado (inclinación −2,9°…3,7°, centro que baja 66 px), la punta
dibujada se mide como el amarillo saturado más a la izquierda y **el packshot oficial se ancla a esa punta**
(anclarlo al centro del cuerpo dejaba el hilo 35 px al lado de la boquilla); matte a negro de todo lo que no es
piel / packshot / aceite; dedos e hilo vuelven delante. El hilo generado es dorado OSCURO y poco saturado
(s 0,16–0,37): la máscara del aceite va con umbrales bajos. Salida: 121 PNG en `public/assets/santagota/spot/reveal/`.
En Remotion es UN plano: cámara de macro del hilo (z 2,4) a plano entero, bezier óptico; el hilo → la boquilla →
la mano → la botella sin cortes; al CLICK un cabeceo de 0,9°.

**09/10 HERO:** set a brightness 0,55 (negro casi absoluto), packshots `hero4-*` (rim al 0,30 de fuerza, un solo
color por botella, Δ etiqueta 4,9 / 4,4), sombra ancha + contacto apretado + reflejo largo que se apaga rápido,
push-in 1,000 → 1,045 lineal en 165 cuadros con el copy fijo fuera del grupo.

**Audio temporal** (`scripts/santagota-animatic-audio.py` → `public/assets/santagota/spot/audio/`): 12 SFX de
Freepik `sound-effects` + cama de `music-generation`. ⚠️ Los generados llegan con picos entre 0,01 y 1,4: el
mezclador **normaliza cada uno a pico 1,0** antes de aplicar ganancia y alinea por ONSET (el PLOP del archivo
está a 0,71 s). La música v1 salió como dos golpes que decaen a silencio; se rehizo pidiendo energía constante.
El master de TV va SIN música (decisión anterior): la cama es sólo para leer el ritmo.

**Pendiente:** OK de Valeria al animatic → rough cut (placas finales, hilo/gota más finos, mano de verdad si se
rueda) → master MXF OP1a 50 Mbps 4:2:2 + PCM 24/48. Latas sólo si el cliente confirma. Plantilla del virtual
sigue sin llegar.

## 2026-09-15 (noche, 2) · Valeria (con Claude) — SPOT TV · V3: los 4 cuadros críticos

**V2 aprobada en concepto (8,5/10).** Última ronda de storyboard antes del animatic, sólo 06/07/08/09.
Regla global: «menos efectos = más premium; nada debe parecer generado por IA».

- **06 SARTÉN:** fuego −60 %. Una lengua de fuego lateral en el borde lejano, casi todo negro, sin partículas.
- **07 PASTA:** giro del tenedor con el hilo de aceite REAL goteando (translúcido, irregular); se recortó la
  punta de dedo que asomó en la esquina. Adiós a la «cinta dorada CGI».
- **08 REVEAL con mano:** prohibido producto flotando. Receta (`scripts/santagota-spot-mano.py`): Nano Banana
  genera «una mano sostiene ESTE squeeze horizontal» con **referencia 16:9 ya en pose** (con el packshot vertical
  de referencia el modelo devolvía 576×1792); se amplía 2× con precisión; se mide el eje del envase generado
  (PCA de los píxeles oscuros); el **packshot oficial** (`hero3-750`, rim fino) se rota (PIL gira ANTIHORARIO con
  ángulo positivo: `rotate(90)` = boquilla a la izquierda) y se pega encima; **matte**: todo lo que no sea piel ni
  packshot se va a negro (borra la tapa dibujada, el cuerpo que sobresale y el hilo CG); los dedos vuelven delante
  por máscara de piel (tono < 32°, saturación 0,16–0,58, sólo del lado de la mano — los amarillos de la tapa
  caían dentro del rango y sobrevivían); el hilo REAL entra desde Remotion en la punta medida (753, 510).
- **09/10 HERO:** set negro casi absoluto (sin nubes de color), botellas al 86 % con profundidad (la de atrás
  más chica y 1,4 px fuera de foco), rim FINO por color hecho en el packshot (`hero3-750` naranja, `hero3-500`
  lima; Δ etiqueta 3,3 / 2,9), piso húmedo apenas visible, aceite desenfocado abajo a la izquierda, copy
  editorial 64 px con «DEL ACEITE DE OLIVA.» en Light. Beauty shot, no KV promocional.

**Entrega:** `out/santagota/spot/keyframes-v3/` (5 PNG + hoja de contacto). El resto del spot sigue siendo la V2.
**Siguiente:** si estos cuatro pasan, animatic 29,97 · 19–20 s con audio temporal.

## 2026-09-15 (noche) · Valeria (con Claude) — SPOT TV · keyframes V2 (segunda dirección creativa)

**Feedback de Valeria a la V1:** «tenemos una idea pero no un MOMENTO». La V1 era una sucesión de beauty
shots (gota → aceite → comida ×3 → botella). La V2 sigue su montaje: NORMALIDAD → GOTA → IMPACTO IMPOSIBLE →
EL MUNDO CAMBIA → CAOS GASTRONÓMICO CONTROLADO → descubrimos que Santa Gota lo provocó.

**Entrega V2:** `out/santagota/spot/keyframes-v2/` — 12 cuadros + endboard con latas, hoja de contacto,
página de revisión. Sigue sin animarse nada: **no se pasa al animatic sin aprobación.**

**Qué cambió, cuadro a cuadro**
- 03/04 el impacto se partió en dos: PLOP («UNA GOTA.») y **BIG BANG («CAMBIA TODO.») = el KV**: columna de
  aceite + anillo con fuego real sobre piedra negra + el mundo mediterráneo todavía vivo en los bordes.
  Salió a la 2ª ronda de prompts (la 1ª daba corona sin periferia o el plato ardiendo — se guardó como KV
  alternativo `v2_bigbang_v2`).
- Food con tres acciones: **pizza** = squeeze en DIAGONAL (Mystic nunca dio la diagonal: se generó la pizza
  limpia y el chorro se compone desde la silueta de la boquilla oficial, desenfocada, en la esquina) ·
  **sartén** = FLASH de fuego (naranja = código de marca) · **pasta** = el tenedor gira y el hilo envuelve el
  giro y sale por arriba a la derecha hacia el reveal.
- **Reveal en dos beats:** 08a la boquilla oficial en macro (packshot ampliado 4× con el upscaler de
  precisión, alfa recompuesto del original) con el hilo cayendo de la punta → 08b CLICK: el squeeze entra
  COMPLETO a cuadro, **horizontal, como se usa un squeeze de verdad** (θ −100°: etiqueta de lado, legible).
  Se descartó la botella inclinada «flotando» de la V1.
- **Hero:** botellas al 83 % del alto, halos naranja/verde DETRÁS de cada botella (CSS radial, luz, no
  producto), piso húmedo con reflejo, aceite dorado desenfocado en primer plano; copy en dos beats (09/10).
- **Firma con gesto propietario:** la gota escultórica (generada sola sobre negro, `v2_gota_firma_v1`) como el
  PUNTO después del logo. Es el dispositivo reutilizable para bumpers/stories.

**Trampas nuevas (ya en el manual §9):**
- Envolver una capa `mix-blend-mode: screen` en un `div` con `filter` u `opacity` crea un contexto propio y
  el negro deja de desaparecer (aparece un rectángulo negro). Brillo y `clip-path` van EN la misma capa.
- Rotar alrededor de la punta de la boquilla: `transformOrigin 50% 0%` y la dirección del cuerpo es
  (−sin θ, cos θ). −100° = squeeze horizontal con la boquilla a la izquierda.
- Freepik devuelve 500 esporádicos al encolar: `post()` reintenta 4 veces.
- Mystic dibuja la fuente del chorro y frutas «decorativas» aunque se prohíban; lo que sobra se apaga con
  `opacity` + `blur` de la placa o se recorta con `scale()` anclado.

**Pendiente:** aprobación de los V2 → animatic 29,97 · 19–20 s con audio temporal (sin música; PLOP, sizzle,
squeeze, CLICK) → rough cut → master MXF. Latas: sólo si el cliente confirma. Confirmar con el canal si el
full sale limpio o con huincha encima (composición defensiva bajo y=216 mientras tanto).

## 2026-09-15 (tarde) · Valeria (con Claude) — SPOT TV «UNA GOTA. CAMBIA TODO.» · 10 keyframes (1ª entrega)

**Cambio de ruta:** el cliente descartó la monja para TV (queda en RRSS). Se rehace desde cero un microspot
full screen 1920×1080 · 29,97 · ≤ 20 s con el handoff `~/Downloads/SANTA_GOTA_HANDOFF_CLAUDE_FINAL`
(Production Bible V2 + storyboard visual + instrucción). Concepto: **una gota cambia el universo** —
mediterráneo cálido → negro/acero/fuego/verde ácido/naranja. Cierre: **SOMOS LA REVOLUCIÓN DEL ACEITE DE OLIVA.**
Sólo full screen por ahora; huincha y virtual después.

**Entrega v1:** `out/santagota/spot/keyframes-v1/` — 10 PNG 1920×1080 (01_CLICHE … 10_ENDBOARD),
variante `10b_ENDBOARD_CON_LATAS` y `00_HOJA_DE_CONTACTO`. No se avanza al animatic sin aprobación.

**Cómo se hizo (reusable para el animatic):**
- Placas generadas con Mystic 16:9 2k (`scripts/santagota-spot-plates-freepik.py`): comida, aceite, fuego, set.
  Prompts con dos bloques de dirección de arte (ANTES / DESPUÉS) + guardas «no bottle, no text, no hands».
  **Mystic insiste en dibujar la fuente del chorro** (cuello de botella, mano, cuchara) aunque se prohíba:
  se pide «exactly one drop, no stream, no thread» y se generan 2 variantes; lo que sobra se recorta en
  composición (KF05: `scale(1.3)` anclado abajo-izquierda saca el cuello del cuadro).
- Producto SOLO packshot oficial (`public/assets/santagota/producto/`), con luz de estudio integrada por
  `scripts/santagota-spot-producto.py` (rim lima/naranja + rebote cálido; **la etiqueta se protege por
  luminancia Y saturación**, verificación Δ centro de etiqueta < 6). Escalado uniforme: `Producto` recibe sólo
  la altura y saca el ancho de `RATIO` — la proporción no se puede tocar ni por error.
- Reveal (08): fondo espejado para que la sartén quede a la izquierda + chorro generado sobre negro en
  `mix-blend-mode: screen` + botella oficial girada −135° **alrededor de la punta de la boquilla**
  (`transformOrigin 50% 0%`): el chorro nace exactamente donde termina la boquilla.
- Composición en Remotion: `src/compositions/santagota/spot/{comun,Keyframes}.tsx`, `SG-KF-01…10`, render en el
  sandbox `/private/tmp/sgrender` con el Chrome del sistema.

**Decisiones tomadas sin confirmación (a validar):**
- **Zona defensiva de 216 px arriba:** el ejemplo de TVN muestra que el canal monta la huincha del auspiciador
  sobre el full screen. Copy y logo viven bajo y=216 (el producto del 08 asoma por arriba: es producto, no copy).
- **Sin música, con pista de audio igual:** el audio de los ejemplos es 100 % voz del programa (medido: 66–71 %
  en banda de voz, pulso 0,13). El master llevará PCM 24/48 con sound design sutil (PLOP, sizzle, squeeze), sin música.
- Endboard **sin latas** por defecto; `10b` con latas lista por si el cliente las aprueba.
- Duración objetivo **599 cuadros = 19,987 s**.

**Pendiente:** aprobación de los 10 keyframes → animatic 29,97 con audio temporal → rough cut → master MXF
(perfil que ya pasó: OP1a MPEG-2 4:2:2 50 Mbps TFF, PCM 24/48). Confirmar con el canal si el full sale
limpio o con huincha encima. Logo vectorial: sigue sin existir.

## 2026-09-15 · Valeria (con Claude) — revisión completa de la cuenta: catálogo, sitio y Drive

Revisión de punta a punta del material de la marca, sin producir pieza. **Se cayeron tres supuestos
del manual y se llenaron dos vacíos** que estaban bloqueando trabajo.

**Lo que cambió**
1. ⭐ **`santagota.cl` es Shopify, no un sitio custom** — tiene API pública (`/products.json`).
   El catálogo completo (10 SKU), los precios y los packshots se leen solos. `marca.json` decía
   `"tipo": "custom", "api_publica": false`: corregido.
2. ⭐ **Los packshots PNG en alta SÍ existen.** El manual los daba por no entregados porque se
   miraron las miniaturas del sitio (~150 px). La CDN sirve el original hasta 2049×2049 con alfa
   real. Bajados los 30 a `raw/santa-gota/packshots/` y normalizados (recortados al bounding box)
   los 10 útiles a `public/assets/santagota/producto/`. **Esto desbloquea producto quieto en pantalla**,
   que era la razón por la que en TV el producto sólo aparecía en el chorro del reel.
   ⚠️ Trampa: `squeeze-500.png` y `squeeze-750.png` del sitio son **las cajas de 12**, no el envase suelto.
3. ⭐ **Existe una sesión fotográfica real de la marca** que nadie estaba usando: ~80 fotos de
   4000×5000 px en el Drive («Fotos Sesión Inicial»). Modelo real, flash directo, fondos naranja/verde,
   macros del chorro, bodegones. Muestra de 8 en `raw/santa-gota/sesion-inicial/`. Ojo: la etiqueta
   de esa sesión es **anterior** al packaging actual — sirve para gente y ambiente, no para producto.
4. ⭐ **El feed se pasó a 4:5 (1080×1350)** en la semana del 14-09. El manual estaba medido sobre
   1080×1080. Material nuevo del diseñador bajado a `raw/santa-gota/feed-sept/semana-14-18/`
   (5 piezas de la serie de recetas del 18, la pieza «Échale a la comida, no al acelerador»,
   2 stories 941×1672 y el reel del lunes 14).
5. **El repertorio de «la intervención» quedó escrito completo** (7 recursos, uno por pieza).
   El más fuerte y el peor documentado era **el logo grabado en la materia** — tallado en el pan,
   rapado en la nuca, escrito en los dientes, estampado en la polera. Es exactamente la ambición del
   Brand Soul («en tu mesa, en tu feed y en tu polera»).

**Lo que se confirmó (no cambia)**
- **El logo vectorial no existe.** La carpeta «Logo Oficial» del Drive tiene un único archivo:
  `logo_lime_naranja.png`, 36 KB. Tampoco hay SVG en el sitio. Sigue pendiente pedirlo.
- Brand Soul de Diana Meinhardt leído entero: arquetipo **La Pecadora Insolente**, propósito
  «desafiar los mandamientos de la cocina cotidiana», cancha explícita (la marca se quiere expandir
  a vinagres, sal, café, chocolate, objetos y eventos: **el aceite es sólo el comienzo**).
- Manual de respuesta en redes (QA v3) leído: tuteo, ironía a las reglas y nunca a la persona,
  máximo un emoji (🖤 y 🔥), cero emojis en reclamos, y **toda respuesta de producto deja claro
  que son dos aceites distintos**.

**Riesgo levantado**
- El feed de septiembre tiene **caras reconocibles tipo celebridad generadas con IA** (la pieza
  «Santo munchies»). Quedó como regla dura: no se produce otra sin autorización escrita — es
  derecho de imagen, no criterio estético.

**Qué se tocó**
`clients/santa-gota/CLAUDE.md` (§1b catálogo nuevo, §4 gramática 4:5 + repertorio, §5 imágenes
corregido, §8 QA con 4 chequeos nuevos) · `clients/santa-gota/marca.json` (e-commerce, catálogo,
packshots, formatos, sesión, madurez a completa en identidad/gramática/formatos/imagen/copy) ·
`src/brand/santagota.ts` (catálogo en código + feed 4:5; `npm run typecheck` limpio).

**Pendiente**
- ⛔ Logo vectorial (pedir al cliente, confirmado que no está).
- ⛔ Plantilla técnica del Virtual de TV: sigue sin llegar. No se entrega al canal sin calzarla.
- Aprobación de los previews V4 de TV → exportar másters con `scripts/santagota-entrega-tv.py`.
- `SANTA GOTA SOCIAL MEDIA MANAGEMENT.pdf` (81 MB, sin capa de texto) sigue sin leer.
- Definir si se sigue produciendo el feed con IA o se explota la sesión real ya pagada.

## 2026-09-11 (noche, 2) · Valeria (con Claude) — V4: pauta de montaje cerrada (previews)

**Los V3 no se aprobaron.** El problema pasó a ser de oficio: timing, encuadres, escala, terminaciones. Valeria
mandó una pauta de montaje cerrada («no agregues decisiones automáticas») y se ejecutó literal:
- Full: sin zooms ni empujes; recortes 16:9 estáticos; hook de fuego (3,32→3,92 a 0,5×); aceite con botella,
  chorro y sartén; ingredientes; pasta; monja + producto; cocina 2; claim sobre la monja GRANDE (K=1,0 → cut-in
  a 1,2 en REVOLUCIONAR); payoff = lanza la pasta (8,667→9,24: después la pasta se sale por la izquierda) + pinzas
  y plato; corte directo a un end frame quieto. Sin látigo lima. Sólo 2 whooshes.
- Huincha: la cara ocupa toda la altura (s=1,0, cornette fuera de cuadro), franja petróleo de 1920 px de borde a
  borde (y 40→216) con la monja superpuesta; claim 100 px; la misma franja cambia a logo 300 px + CTA 62.
- Virtual: monja al 112 % (cabeza + torso), gesto real de sartén ida y vuelta (cuadros 3→5→3, sin el «plato
  gigante»), claim tipográfico sin caja detrás de ella, losa de borde a borde para la marca. **El preview ahora la
  muestra a escala 1:1** (775×1080 a toda la altura del cuadro); al 72 % del V3 se veía chica junto al conductor.
- Previews V4 en `04_PREVIEWS/V4/`. Másters siguen sin exportar hasta la aprobación.

## 2026-09-11 (noche) · Valeria (con Claude) — V3 de los 3 placements: última ronda creativa (previews)

**Brief:** «Corrección final obligatoria»: edición publicitaria de verdad (transiciones motivadas, kinetic type,
ritmo), nada de rectángulos de video ni blur de relleno, monja grande y reconocible, huincha ≤ 7,00 s, autocontrol
cuadro a cuadro antes de entregar. Sólo previews; los másters se exportan tras la aprobación.

**Qué se hizo**
- La monja recortada EN MOVIMIENTO (11 cuadros del reel con alfa, `public/assets/santagota/monja-seq/`): entra por
  el borde, mira, lanza la pasta. Es lo que hace que el virtual sea «una monja entró al matinal» y no una pantallita.
- La cocina extendida por IA (sólo periferia) para que el claim del Full vaya sobre la monja real a cuadro completo.
- 8 efectos de sonido generados en Freepik + cama del reel; sin música (derechos).
- Huincha 209 f (6,97 s): losa petróleo con bisel, claim cinético, logo + URL grandes, resto transparente.
- Virtual 15 s: franjas apiladas para el claim, losa para la marca, la monja al 95 %.
- Full 19,95 s: fuego (burn-through) → monja → chorro → ají → camarones → pasta → producto → emplatado → claim
  sobre la monja real → lanza la pasta con empuje → plato → látigo lima → end frame petróleo.
- Previews V3 en `~/Desktop/SANTA_GOTA_TV_FINAL/04_PREVIEWS/V3/` (audio a −24 LKFS, 29,97).

**Revisión propia (hoja de contacto a 6 fps de cada MP4):** se corrigieron el hook de fuego (a 3,30 todavía no había
llamas: empieza en 3,40), el lanzamiento que se pasaba a las pinzas (corte del reel en 9,35) y el plano del plato que
llegaba al logo que trae el reel (11,0). Detalles en `CLAUDE.md` §8b y §9.

**Pendiente**
- Aprobación de Valeria de los V3 → exportar másters con `scripts/santagota-entrega-tv.py` (huincha a 209 cuadros).
- ⛔ Plantilla técnica del Virtual: sigue sin llegar. No se entrega al canal sin calzarla.
- Logo vectorial y packshots PNG: siguen sin llegar (el producto sólo aparece real en el chorro del reel).

## 2026-09-11 (tarde) · Valeria (con Claude) — Fase 2: PRODUCCIÓN FINAL de los 3 placements de TV

**Dirección aprobada con cambios:** nada de campo lima plano; fotografía primero (el reel), titular
blanco + REVOLUCIONAR lima, naranja sólo como gesto (halo, plumón, pastilla del CTA), logo SÓLO el PNG
oficial a color, producto SÓLO real (el chorro del squeeze del reel), la monja SÓLO la del reel.

**Entrega en `~/Desktop/SANTA_GOTA_TV_FINAL/`** (fuera del repo; el pipeline sí está versionado):
- `01_HUINCHA/` secuencia TGA 32 bit · 1920×216 · 210 cuadros @ 29,97 = 7,01 s · alfa real.
- `02_VIRTUAL_PENDIENTE_PLANTILLA/` secuencia TGA 32 bit · 775×1080 · 450 cuadros = 15,02 s · alfa real.
  ⚠ **La plantilla del canal NO llegó**: márgenes provisorios de 48 px. No enviar al canal sin calzarla.
- `03_FULLSCREEN/` MXF OP1a XDCAM HD422 50 Mb/s · 1920×1080 · 29,97 · TFF · PCM 16/48 · 19,95 s ·
  audio −23,6 LUFS / −7,7 dBTP (loudnorm a −24 LKFS, ATSC A/85).
- `04_PREVIEWS/` MP4 H.264 (huincha y virtual montadas sobre un fotograma real de TVN; posición del
  virtual ilustrativa). `05_ASSETS/` ProRes 422 HQ del full + ProRes 4444 con alfa de huincha y virtual.
- `VERIFICACION.txt` con el ffprobe de cada máster.

**Pipeline:** `src/compositions/santagota/tv/` + `scripts/santagota-entrega-tv.py`. Render en el sandbox
con Chrome del sistema; TGA con PIL; MXF con el ffmpeg de `imageio_ffmpeg` del venv compartido.

**Lo que se aprendió (ya está en el manual §8b y §9):** la lista de planos exacta del reel; `startFrom` de
Remotion va en fotogramas de la composición; los PNG de Remotion salen sin canal alfa cuando el cuadro es
opaco (se fuerza RGBA al escribir el TGA); `-ss` antes de `-i` con el ffmpeg de Remotion etiqueta mal.

**Advertencias reales para el cliente:** plantilla del virtual pendiente; el reel y las fotos de Instagram
son dos actrices distintas (se usó la del reel en las tres piezas); el reel está a 24 fps y el máster a
29,97 (conversión por cuadro más cercano, se nota apenas en los planos a cámara lenta); no llegaron
packshots PNG (no hay producto quieto en pantalla, sólo el chorro real del reel); el logo sólo existe en
PNG de 810 px (en el end frame va a 760 px, al límite).

## 2026-09-11 · Valeria (con Claude) — apertura de la cuenta + Fase 1 de los placements de TV

**Qué se hizo**
- Se abrió el sistema de la marca desde cero: `clients/santa-gota/` (manual + marca.json), `src/brand/santagota.ts` + `santagotaUI.tsx`, material real en `raw/santa-gota/` (feed sept 2026 de Luis Piano, reel de la monja, logo, ejemplos de huinchas de TVN, QA de redes, Brand Soul en Drive).
- Se midió todo antes de diseñar: lima `#C3D600` (plumón/tapa), naranja `#F26513`, botella `#0E1C03`, Montserrat Bold+Light, los cuatro recursos del feed (logo plano, botella en línea, aureola, plumón).
- **Fase 1 entregada:** dirección de arte + 3 key visuals (huincha 1920×216, virtual 775×1080, full 1920×1080) + cierre común. Renders en `out/santagota/kv-v4/`, mocks sobre el programa real, y la presentación para aprobar en https://claude.ai/code/artifact/c73bee98-7166-49bd-a3d3-9ff38b08177d
- Composiciones registradas en `Root.tsx` (`SG-Huincha`, `SG-Virtual`, `SG-Full`, `SG-Cierre`). Se renderizan con la receta del sandbox (`/private/tmp/sgrender` + Chrome del sistema).

**La idea:** la monja se mete en la tele. Campo lima, tinta botella, naranja sólo en aureola y plumón (la aureola es la O de GOTA), bloque botella con logo a color + SANTAGOTA.CL. Cambia cuánta monja cabe por formato, no la idea.

**Decisiones que conviene saber**
- La monja de TV es la del REEL (actriz real). Fotograma 8,7 s para stills (medido por foco), 9,3 s (lanza la pasta) sólo para video.
- Aureola naranja y no blanca: flota sobre el set del canal, que es blanco.
- Tinta botella sobre lima es el par del packaging; el logo a color nunca va sobre lima.

**Pendiente / bloqueado**
- ⛔ Aprobación de Valeria de los 3 KVs — **no pasar a Fase 2 (animación) sin eso.**
- Plantilla técnica del Virtual 775×1080 (no llegó). Logo en vectorial (sólo hay PNG 810 px). Packshots PNG en alta (no llegaron).
- `SANTA GOTA SOCIAL MEDIA MANAGEMENT.pdf` del Drive (81 MB, sin capa de texto) sigue sin leer.
- Fase 2: huincha 7 s, virtual ≤20 s, full 20 s a 29,97 (reel a 24 fps → blend), Targa+alfa y MXF NTSC.
