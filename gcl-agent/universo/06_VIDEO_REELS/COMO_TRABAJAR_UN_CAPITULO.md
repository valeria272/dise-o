<!-- Copia en el repo de la memoria gcl-metodo-capitulos-con-valeria (25-09-2026). Léelo antes de abrir un capítulo nuevo de G. -->

# Cómo se trabaja un capítulo de G con Valeria (aprendido en el CAP.02, 16 cortes en un día)

Valeria pidió esto explícitamente al cerrar el CAP.02: «deja en tus aprendizajes todo lo dicho con G, cosa
que sepas mejor cómo trabajar para la próxima y pivotemos menos». Registro del capítulo: `CAP_02_TURNO_DE_NOCHE/GUION_V3_MANANA_LO_VEO.md` · canon: `../CANON_LOCK.md`.

## 1. La regla madre: lo que ella no pidió, no se construye
**Why:** TODO lo que agregué por iniciativa propia terminó eliminado y costó un corte cada uno: el WOW/WhatsApp
de Gin («no se entiende quién es»), la voz robótica «oh no» («queda mal, definitivamente»), Pancho escribiendo
en el papel («muy falso»), el segundo «mm», «una cosita más», los tiznados, el halo cayendo, el trombón, el plano
de «Reenviar» (se da por entendido). Y los cortes 8/9 —armados desde un texto de storytelling pegado— reintrodujeron
cosas ya eliminadas: «te equivocaste, revisa bien».
**How to apply:**
- Antes de construir un corte, convertir su feedback en una **checklist literal** y aplicar sólo eso. Una idea
  extra se propone en una línea de texto; no se construye.
- Mantener y consultar la **lista de lo eliminado** (en GUION_V3 § corte 13): nada de esa lista vuelve, aunque un
  texto nuevo lo sugiera. Un texto pegado no reemplaza la línea aprobada: la línea aprobada es el último corte
  del que ella dijo «me parece bien / ok».
- Un corte = un archivo `Cap02…Vn.tsx` + render + copia a `~/Desktop/GCL_CAP02_STORYBOARD/` + `open`. Ella revisa
  en QuickTime y dicta el feedback; cada ronda es chica. No mezclar dos rondas en un corte.

## 2. Su gusto (lo que ya no hay que volver a probar)
- **Los humanos nunca hablan** y no hay voces robóticas. El humor sale de los gags entre los personajes.
- **Pancho (humano IA)**: sólo hasta que se para, planos cortos, sobre el hombro (menos cara = más real), grano.
  Nada de manos escribiendo. Sale a las 18:30 con «lo veo mañana 9 AM» en un globo de pensamiento.
- **«Fome» = falta dinamismo**: cortes de 8–14 f con el reloj corriendo, códigos y mensajes entre ellos, una
  pelea corta. Pero **todo texto tiene que poder leerse** (post-it +1 s, mails lentos, «V3 lista» con tiempo).
- **Lo implícito no se muestra**: si el público puede inferirlo (el reenvío hacia abajo), se corta. Descansos y
  celebraciones, cortos. El trabajo, largo y con gags.
- **Final**: los personajes terminan en la explosión; después la tarjeta «COPYLAB · Departamento de cosas
  imposibles» + PRÓXIMO CAPÍTULO. Sin epílogo.
- La versión que mandan es la **V3** (para que «volver a la anterior» tenga sentido).

## 3. Musicalización (lo que le gustó de verdad)
- Quiere música **trend/cool con derechos** (The Strokes «Reptilia»), no temp tracks de catálogo IA. Bajarla como
  temp track, avisar siempre que va sin licencia y que se pone desde la biblioteca de IG/TikTok al publicar.
- **Cortar al beat**: medir BPM y el primer bombo, y que la batería entre exacto en el primer corte del montaje.
- **Una sola canción que cambia de estado** (riff solo → banda entera → riff cansado a 0,78× con lowpass y eco →
  reentrada). Variantes con scipy; el ffmpeg de Remotion no tiene filtros de audio.
- **Entre tramos la música BAJA, no se apaga** («apagarla y que vuelva queda como desconectado, raro»). El único
  corte seco es el ding del cliente, porque el silencio es el chiste; y la canción **retoma en el mismo beat**
  sobre la tarjeta final.
- Verificar con la curva de RMS del render (venv `scipy`), no de oído.

## 4. Técnica que no hay que redescubrir
- Texto en perspectiva: `scripts/seguir-plano.py` (homografía) y `superficie-curva.tsx` para papel curvado;
  medir el post-it con `scripts/medir-postit.py`.
- Reloj/HUD con frame global (`f + en(id)`), nunca el frame local de la Sequence.
- `remotion still` de a uno (en paralelo rompe la caché de webpack). Al recortar bloques por índice, buscar el
  ancla DESDE el bloque (`s.index(fin, a)`), si no se duplica medio archivo.
- Video: Hailuo 02 1080p es el único modelo que funciona con humanos; Kling falla. yt-dlp: el del venv con
  `--extractor-args youtube:player_client=android --js-runtimes node:$(which node)`.

## 5. Orden de trabajo para el próximo capítulo
1. Leer GUION vigente + lista de lo eliminado + esta memoria. 2. Guion en texto y aprobarlo ANTES de generar.
3. Stills de planos clave → aprobación → clips. 4. Corte 1 con música al beat desde el inicio (no al final).
5. Una ronda = una checklist = un corte. 6. `/cierre` el mismo día.
