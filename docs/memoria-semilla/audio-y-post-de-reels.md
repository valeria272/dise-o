---
name: audio-y-post-de-reels
description: "Reglas duras de mezcla (ruido, ducking, limpieza de voz) y de post-producción (gradación, bloom, transiciones) para reels; aprendidas rehaciendo R01 de G.CL"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 087497ee-2e54-422c-92f3-244e8dea3cc9
  modified: 2026-08-19T20:43:57.163Z
---

Feedback de Valeria sobre el capítulo 1 de G.CL, 19-08-2026: *«la post producción
sigue plana, la música a veces baja y sube de la nada, el destello rosado está
pegado con chicle, la voz sigue limpiándola, el ruido de fondo suena como eso,
ruido»*. Cada queja tenía una causa técnica concreta y todas se repiten en
cualquier reel, no solo en este.

**Sonido**

1. **Nunca ruido blanco continuo en una cama musical sintetizada.** La capa de
   "aire" (ruido gaussiano pasa-altos) sonaba los 57 s a −28 dB en 8–16 kHz,
   26 dB más fuerte que el residuo de la locución. Lo que la usuaria oía como
   "ruido de la voz" era la música. Textura = armónicos o ráfagas cortas.
2. **Nunca ducking siguiendo la envolvente de la voz.** Con silencios largos
   entre bloques, la música sube y baja en cada frase. Se reemplaza por
   (a) hueco de EQ fijo de −4,5 dB entre 300 Hz y 3,5 kHz y (b) dinámica por
   arreglo, con cambios solo en el compás y rampa de medio compás. Máximo ~6 dB
   entre secciones.
3. **Limpieza de voz con MMSE-LSA, no con sustracción espectral.** La
   sustracción agresiva deja *musical noise* (burbujeo). Con LSA + SNR a priori
   decision-directed + suavizado de ganancia en frecuencia + sobre-sustracción
   **por banda** (dura bajo 300 Hz y sobre 5 kHz, suave donde vive la voz) el
   índice de burbujeo bajó de 14,2 dB a 4,1 dB. Sumar **cama de sala continua**
   a −62 dBFS: el silencio digital absoluto entre bloques delata el procesado.
   Implementación en `EDITOR VIDEOS/scripts/procesa-vo-gcl.py` (numpy puro, sin
   scipy — `exp1` está aproximada con Abramowitz & Stegun).

**Imagen**

4. **La rejilla musical arregla la "post plana".** Montar a 120 BPM (compás de
   2 s = 60 frames a 30 fps) y escribir la música a la misma rejilla. La
   locución es el esqueleto y no se mueve; los cortes se llevan al tiempo fuerte
   más cercano que deje ≥0,4 s de aire antes de la frase.
5. **Cuatro capas obligatorias sobre planos generados por IA:** gradación *por
   plano* (split-tone, sombras frías / luces cálidas), floración (bloom con
   `backdropFilter: blur() brightness()` + `mixBlendMode: screen` — una sola
   decodificación de video), cámara viva en todos los planos, grano + caída de
   bordes. Un solo look para todo el reel es lo que lo aplana.
6. **Nunca teñir de rosado un plano que ya es rosado** — queda monocromo y sin
   profundidad. El personaje pone el color; la gradación pone contraste.
7. **Prohibido el destello de color superpuesto.** Se lee como pegado con
   chicle. Un golpe se hace con luz *motivada* (nace en un punto del cuadro y se
   expande) + golpe de cámara + impacto de música, los tres en el mismo frame.
   Las transiciones de acto van con latigazo (4–5 frames de desenfoque
   direccional + empuje), no con overlays.

8. **Antes de subrayar un momento, verificar que el momento exista en el
   material.** En R01 el clip del visor venía con la G **ya encendida desde el
   frame cero**: el golpe de música, el destello y el empuje de cámara caían
   sobre una imagen que no cambiaba, y por eso ninguna cantidad de post lo
   arreglaba. La solución fue hacer que **el corte sea el evento**: plano oscuro
   sostenido + un LED que late y crece → corte seco a la imagen encendida, con
   el impacto en el mismo frame. Salto de brillo medido: 18 → 108 en 0,2 s.
   Regla: extraer una tira de fotogramas del clip fuente y mirarla ANTES de
   montar. Los clips de Kling también suelen degradarse después de ~2 s (el
   personaje se da vuelta, la luz parpadea): usar solo el tramo bueno con
   `playbackRate`.

9. **Los senos graves desafinados zumban.** Dos osciladores casi idénticos
   (55 y 55,3 Hz) baten entre sí y el oído lo lee como zumbido, no como peso.
   Medido en R01: +29 dB sobre el fondo espectral, presente el 70% del reel.
   Un solo seno, a la mitad de nivel y con respiración por compás. Chequeo
   rápido de mezcla: **ningún tramo bajo 45 Hz debería llevar más del ~1% de la
   energía**, y el pico de la curva va en 120–500 Hz, no en el sub. En R01 pasó
   de 26% bajo 45 Hz a 0,1%.
10. **Un golpe grave solo no se escucha en teléfono.** Al impacto hay que
   sumarle un transitorio brillante (ruido de banda 900 Hz–9 kHz con caída
   rápida). Sin eso el golpe existe en el medidor y no en el parlante.
11. **Mirar el clip completo antes de descartarlo.** Los tres planos de oficina
   de R01 "miraban a cámara"… en los primeros 2 segundos. Del segundo 2 en
   adelante el personaje gira hacia la pantalla o hacia el equipo. Recortar el
   fuente con ffmpeg y estirar con `playbackRate` resolvió un pedido que
   parecía necesitar generar material nuevo.
12. **El PNG puede traer el error.** Un keyframe puede venir con una banda de
   negro plano abajo (en R01, el 22% inferior): en pantalla se lee como imagen
   mal encuadrada. Recortar cambia el modo de `objectFit` y come los costados;
   mejor **extender** la superficie (estirar una tira de las últimas filas
   buenas y apagarla en degradado).

13. **Con TTS, NO aplicar limpieza de ruido ni cama de sala.** La cadena de
   supresión + cama a −62 dBFS existe para grabaciones en una pieza real. Sobre
   una voz sintética solo AGREGA ruido: fue la causa del «tiene ruido de fondo»
   del 19-08. Con TTS la cadena es solo pasa-altos, de-esser, EQ, compresión
   suave y nivel.
14. **Un tono grave sostenido zumba a cualquier volumen.** Bajarle el nivel al
   sub de 55 Hz no sirvió (la queja volvió). Lo que lo resolvió fue **subirlo
   una octava**: 110 Hz se escucha en teléfono, sostiene igual y no drona. Los
   55 Hz quedan solo dentro de los impactos, que son transitorios.
15. **Cambiar el tono: cuidado con el signo.** Remuestrear con paso > 1 acelera
   la reproducción, y acelerar SUBE el tono. Para bajar n semitonos hay que
   estirar con vocoder de fase por 2^(−n/12) y remuestrear por el mismo factor.
   Verificar SIEMPRE midiendo la fundamental por autocorrelación antes de
   entregar — la primera versión subía 134 Hz a 169 Hz.
16. **Voz sobre cama musical: apuntar a 12–14 dB de separación.** Con 9,5 dB la
   voz «se pierde». Se gana bajando la cama y profundizando el hueco de EQ de
   300 Hz–3,5 kHz (−6,5 dB), no comprimiendo la voz.
17. **Al editar tablas de datos en un script, no delimitar el corte por una
   cadena que aparece antes en el archivo.** Buscar `"Con más criterio."` calzó
   primero en otra lista y el reemplazo terminó DUPLICANDO la tabla; la segunda
   definición ganó y el montaje salió con datos viejos. Verificar con
   `s.count(...) == 1` después de reemplazar.

18. **Un plano se CONGELA si `duracion_en_reel * playbackRate > duracion_del_clip`.**
   Remotion muestra el último frame quieto el resto del plano. Al auditar R01
   estaban CUATRO clips así, y tres los había roto yo al recortar los fuentes
   (quedaron con margen cero o negativo). Solución estructural: una tabla con la
   duración real de cada clip y un helper que **acota** el rate pedido al máximo
   que cabe, con 4% de margen (`rateClip()` en `GclOrigenReel.tsx`). Nunca fijar
   rates a mano.
19. **Verificar congelados automáticamente**: extraer todos los frames a baja
   resolución y medir la diferencia media entre frames consecutivos. Runs de 4+
   frames bajo ~0.45 = plano quieto. Revisar en particular los últimos 12 frames
   de cada plano.
20. **Para poner una expresión sobre la cara del personaje** (tapar los ojos y
   dibujar otros): (a) localizar los ojos con **detección de manchas** —umbral de
   rosado + dilatación para unir los puntos del dot-matrix + etiquetado por
   componentes— sobre un frame SIN el overlay; medir por centroide de una región
   grande da resultados basura. (b) El overlay tiene que **replicar exactamente**
   la transformación del plano (escala del Ken Burns Y el vaivén), con el
   contador de frames desfasado, porque el `<Sequence>` del overlay arranca
   después que el del plano. Sin eso la máscara se despega.
21. **Varias propiedades animadas a la vez que cambian el ANCHO del texto se
   leen como «doble animación».** En R01 el interletrado (0,14em → −0,025em) más
   la escala (0,9 → 1) hacían que las líneas se cerraran horizontalmente
   mientras el bloque subía: tres movimientos en direcciones distintas. Una
   entrada limpia mueve **una sola cosa** (subir + enfocar). Verificar midiendo
   el ancho del bloque frame a frame: tiene que estabilizarse y no moverse más.
22. **Antes de elegir un salto de línea, medir el ancho real de la tipografía.**
   Syne en peso 800 ocupa ~50 px por carácter en mayúscula inicial a 57 px de
   cuerpo: «Me contrataron para» pedía 942 px y solo había 900 disponibles, así
   que «para» quedaba huérfano. Estimar por caracteres no sirve; medir sobre el
   frame renderizado.

Ver [[reel-video-gotchas]] y [[copywriters-feed-plan]]. Gramática completa en
`EDITOR VIDEOS/gcl-agent/GCL_SCRIPTS.md`, parte A.
