# MÁS CENTER — manual de marca para piezas

> **Cliente:** Grupo IFB — red de strip centers Más Center (Chile, ~25 proyectos de Coyhaique a Copiapó)
> **Contraparte:** Sebastián Córdova (performance, briefs mensuales) · Scarlette Muñoz y Sebastián Serrano (orgánico) · **Diseño del cliente:** Diego Aguilar — su criterio manda
> **Kit en código:** `scripts/mascenter_sistema.py` (presentaciones) · `src/compositions/mascenter/MasCenterReel.tsx` (reels) · **Ficha máquina:** `clients/mascenter/marca.json`
> **Sistema de producción:** `clients/mascenter/sistema/` (gráficas paid: `build.py` → `render.sh`) · **Qué falta:** `CHECKLIST-CLIENTE.md`
> **Referencias reales:** `raw/mascenter/ref-paid/sept/` (6 piezas aprobadas, sept 2026) · `raw/mascenter/editables-paid/agosto/` (12 piezas + reel) · `raw/mascenter/ref-reels/` (4 reels)
> **Manual oficial del cliente:** `raw/mascenter-terrenos/manual-marca.pdf` (Grupo IFB 2023, sección 6)

Antes de diseñar, leer [`docs/SISTEMA-DE-MARCAS.md`](../../docs/SISTEMA-DE-MARCAS.md).

---

## 1. Qué es la marca
Más Center desarrolla y administra strip centers de barrio (supermercado ancla + farmacia +
servicios + locales). Habla a dos públicos con **dos campañas distintas**:

| Campaña | A quién | Familia gráfica |
|---|---|---|
| **Tráfico a Instagram / comunidad** (la de octubre 2026) | vecinos del barrio | «LinkAd Tráfico a IG» — foto con onda, pastilla roja, Localito |
| **Arriendo de locales** («linkad» de agosto) | locatarios / empresas | foto con velo azul oscuro, lista de íconos rojos, CTA oscuro |

No mezclarlas: la mascota **Localito** sólo aparece en la de comunidad.

## 2. ⭐ La regla madre
**La pieza de octubre es la de septiembre con otro contenido.** El esqueleto de paid media
del cliente lleva cuatro meses idéntico (medido); lo que cambia es la foto y el texto. Si una
pieza nueva no se puede poner al lado de `LinkAd Tráfico a Ig 1 - post.png` y confundirse
con la misma campaña, está mal.

## 3. Identidad — medido, no supuesto
### Colores
| Uso | Hex | Nota |
|---|---|---|
| Pastilla del titular y texto de bajada | `#DC1914` | muestreado en las 6 piezas de septiembre y en las de agosto |
| Burbuja del CTA | `#D80000` | **no es el mismo rojo** de la pastilla; en las piezas aprobadas son dos |
| Rojo de la mascota | `#DE2824` | viene en el PNG del cliente; no se toca |
| Fondo | `#FFFFFF` | blanco puro, sin crema |
| ⚠️ Rojo del manual oficial | `#E52521` | el manual 2023 dice «Vivid red»; las piezas aprobadas usan `#DC1914`. **Se extiende lo aprobado**; si Diego o el cliente quieren volver al manual, cambiar `--rojo` en `sistema/base.css` |

### Tipografía — Montserrat (medida), aunque el manual diga Poppins

⚠️ **El manual 2023 (p. 26) dice Poppins; las piezas aprobadas y los reels del cliente están en
Montserrat.** Se midió glifo a glifo el 04-09-2026 a igual altura de capital: el CTA de septiembre
mide 394 px, Montserrat Medium 392, Poppins Medium 370; la pastilla calza con Montserrat Bold
(619 vs 641; Poppins 594). Valeria lo vio a ojo antes de medirlo. **Se usa Montserrat** hasta que
Diego diga otra cosa. Archivo: `sistema/assets/fonts/Montserrat.ttf` (variable, 100–900).
| Rol | Peso | Tamaño feed 1:1 | Tamaño story 9:16 | Archivo |
|---|---|---|---|---|
| Titular en pastilla | Montserrat Bold 700, VERSALES | 43 px / interlínea 43 | 50 px / 50 | `Montserrat.ttf` |
| Bajada | Montserrat SemiBold 600 | 30,5 px / 36 | 50 px / 56 | `Montserrat.ttf` |
| CTA en burbuja | Montserrat Medium 500, VERSALES | 29 px / 33 | 33,5 px / 37 | `Montserrat.ttf` |
| Reel: titular | Montserrat Bold 700, VERSALES | — | 90 px / 98 | |
| Reel: pastilla | Montserrat Medium 500 | — | 46 px / 60 | |

Las capitales se midieron sobre la pieza (31 px feed, 36 px story) y se convirtieron con
la altura de capital de Montserrat (0,70 em). ⚠️ Grupo IFB usa Helvetica Neue + Cera Pro:
son marcas distintas del mismo manual, no mezclar.

### Logos — cuál va en cada fondo
| Archivo | Cuándo |
|---|---|
| `sistema/assets/logo-mascenter-blanco.svg` | siempre sobre foto o sobre rojo. La tinta ocupa el 85,6 % del ancho del SVG y su centro está 1,9 % a la derecha del centro del archivo — `build.py` ya lo compensa |
| `out/mascenter-algarrobal/assets/img/logo-mascenter-color.svg` | sobre blanco (web, presentaciones) |

Usos indebidos (manual p. 34): no inclinar, no degradar, no sombra, no 3D, no varios colores,
no estirar, no contornear.

## 4. La gramática — cómo se compone (px sobre 1080 de ancho)
Familia **«LinkAd Tráfico a IG»**, de arriba abajo:

| Elemento | Feed 1080×1080 | Story 1080×1920 |
|---|---|---|
| **Foto** a sangre por arriba, termina en **onda en S** que sube de izquierda a derecha | borde en y=786 (x=0) → ~630 (centro) → 250 (x=1080) | 1270 → ~1190 → 620 |
| **Logo blanco** centrado, tinta 205–211 px de ancho | borde superior de la tinta en y=64 | y=117 |
| **Pastilla roja** del titular, centrada, ancho al contenido, radio 22–28 | y 570–688 (2 líneas), pad 47 lateral | y 999–1201 (3 líneas), pad 22 lateral |
| **Bajada** en rojo, centrada, sin caja | líneas en y 718 y 754 | 1252 / 1309 / 1364 |
| **Burbuja del CTA** abajo-izquierda, radio 15, cola hacia la mascota | x 170–649, y 841–970 | x 80–620, y 1491–1636 |
| **Localito** abajo-derecha, sangrado por el borde inferior | x 648–884, y 809→ | x 620–950, y 1469→ |

La onda exacta está en `sistema/assets/onda.json` (envolvente medida columna a columna;
bajo la pastilla se interpola). La pastilla **monta sobre la onda**: tapa el borde de la
foto en el centro. **Las cifras de la tabla salen de `sistema/build.py` (dict `GEO`)** —
si se cambia una, cambiarla ahí.

### Formatos
| Uso | Medida | Nombre de entrega |
|---|---|---|
| Post feed | 1080×1080 (⚠️ el cliente entrega 1081; se corrige) | `MASCENTER_P01_Feed_1080x1080.png` |
| Story | 1080×1920 | `MASCENTER_P01_Story_1080x1920.png` |
| Reel | 1080×1920 · 30 fps · mp4 | `MASCENTER_P02_Reel_1080x1920.mp4` |
| Reel en feed | 1080×1080 | `MASCENTER_P02_Feed_1080x1080.mp4` |

Nomenclatura del brief: `CLIENTE_Pieza_Formato_Medida`. Entrega en Drive:
`PERFORMANCE/2026/<MES>/ADS <MES>/`.

### Reels (familia «r-performance»)
**Lo que se conserva del reel de agosto del cliente (medido a 60 fps):** logo blanco
arriba (tinta 211 px, y=118), titular en versales Montserrat Bold 90 px alineado a x=110
en el tercio inferior (⚠️ **la caja termina en y=1480 y no pasa de x=900**: ver §9, 24-09), pastilla roja (627 px, radio 48) con **ícono en círculo blanco
montado en el borde superior** y texto Medium 46 px, cierre en rojo pleno (~3 s) con el
logo grande (tinta 405 px, centrado) y una línea Medium ~50 px, pista de ~81 BPM.
Los reels del cliente duran 15–20 s aunque el brief diga 10 s.

**Lo que NO se copia (feedback de Valeria, 04-09-2026):** el reel de agosto escribe y borra
el titular letra a letra (0,32 s) y corta con un golpe de rojo pleno de 0,30 s. Se
reprodujo tal cual y Valeria lo rechazó: «los textos llegan y aparecen, no tienen una
transición suave, lo mismo con los frames». **El montaje del estudio es otro:** planos
que se funden entre sí en 0,67 s con un zoom lento continuo (1,00 → 1,07), textos que
entran palabra a palabra con fundido y desplazamiento de 26 px (curva ease-out), salen
con fundido, pastilla que entra con resorte sin rebote. Velo oscuro suave abajo cuando hay
titular. Todo en `src/compositions/mascenter/MasCenterReel.tsx` (constantes `FUNDIDO`,
`ENTRA_TEXTO`, `SALE_TEXTO`).

**El cierre SÍ es la réplica exacta del cierre del cliente** (pedido de Valeria, 04-09:
«el cierre sácalo de las carpetas editables»), medido a 60 fps sobre el reel de agosto:
panel rojo que entra desde la izquierda en 0,25 s · el logo baja desde arriba (~220 px) y
se asienta en 0,23 s con la tinta de 405 px y su borde superior en y=840 · 0,1 s después el
texto se escribe a ~80 caracteres/s en **Montserrat Regular ~57 px**, interlínea 59, centrado
en una caja de 665 px desde y=1310 · se queda 3,1 s hasta el final, sin fundido. El último
plano sigue vivo bajo el barrido (si no, queda un hueco negro).

⛔ **Clips generados con letras finas:** `coyhaique.mp4` (Fashion's Park) hace vibrar las
letras del local — 2º orden temporal 8,4 en la franja quieta de arriba contra ≤ 2 en los
demás. Valeria lo vio como «tintineo». Antes de usar un clip de Kling, medir el parpadeo por
franjas (`out/_verificacion/mc/flk-*`) y descartar el que vibre donde nada se mueve. **Música:** julio y agosto llevan la misma pista
(~81 BPM, con fundidos); está extraída en `raw/mascenter/audio/pista-agosto.aac` y en
`public/assets/mascenter/pista-mascenter.m4a`, y es la que llevan los reels de octubre.
Todo está en `src/compositions/mascenter/MasCenterReel.tsx`; el contenido del mes va en
`REEL_02` / `REEL_03`.

## 5. De dónde salen las imágenes
1. **Fotos reales del cliente**: `raw/mascenter-terrenos/fotos-drive-2026-03/` (5 strip
   centers, 1200×896) y `raw/mascenter-terrenos/fotos-sitio/` (600×510, sólo referencia).
   Metraje crudo de Sebastián Serrano (20 MOV, 03-09-2026) en
   `DISEÑO GRILLAS/2026/9. SEPTIEMBRE/ORGÁNICOS/TODO EN UN MISMO LUGAR` — **no es público
   por enlace**: pedir que lo compartan antes de un reel con tomas reales.
2. **Gente sobre la foto real**: Nano Banana Pro con la foto como referencia
   (`scripts/magnific.py pro --refs`). ⛔ **Reescribe los rótulos de los locatarios**
   («cencusud», «Cicanoa Estcenida»): el letrero real se pega encima con
   `sistema/parche_letrero.py`. Revisar los rótulos a zoom 1:1 antes de entregar.
3. **Movimiento**: Kling v2.1 pro desde el recorte 9:16 de la foto real
   (`scripts/magnific-video.py`), 5 s, un movimiento de cámara y gente caminando.
4. Estilo del manual (p. 39): personas reunidas pasando un buen rato, luz natural.
   El brief de octubre pide «fachada o pasillo con gente, evitar stock genérico».

## 6. Tono y copy
Tuteo cercano de barrio. Titular en versales, siempre con una promesa concreta
(«¿Buscas promociones, tiendas y buenos datos?»). CTA en la burbuja, en versales, siempre
con «Síguenos». Sin emojis en gráfica. Los textos van **verbatim del brief**; la conversión
a versales es del sistema, no del copy.

## 7. Reels y video
Cierre oficial: rojo pleno + logo + una línea. Sin voz; el texto en pantalla cuenta la
historia. Música: la misma pista de los reels de julio y agosto del cliente (ver §4).

## 8. QA obligatorio — antes de mostrar nada
- [ ] Medida exacta: 1080×1080 / 1080×1920 (el cliente entrega 1081 — nosotros no)
- [ ] Rojos: pastilla `#DC1914`, CTA `#D80000`; ninguno otro
- [ ] Logo: tinta 205–211 px, centrado en x=540, borde superior en 64 (feed) / 117 (story)
- [ ] Rótulos de terceros legibles y correctos a zoom 1:1 (Jumbo, Cruz Verde…)
- [ ] Zonas seguras del brief en story: texto y CTA dentro de 269–1651 (14 % arriba y abajo).
      El logo va en y=117 **por sistema aprobado** (excepción declarada en `marca.json`)
- [ ] Localito completo, sin restos de la pieza de origen, sangrado sólo por abajo
- [ ] Lado a lado con `raw/mascenter/ref-paid/sept/LinkAd Tráfico a Ig 1 - post.png`
- [ ] Reel: primer frame legible solo, ≤ 7 palabras por pantalla salvo texto verbatim del brief
- [ ] Reel 9:16: ningún texto bajo y=1500 ni a la derecha de x=900 (el brief marca 420 px abajo y
      180 px a la derecha como tapados). «Más Center» nunca partido en dos líneas ni palabra sola
      en una línea: si el corte automático falla, la escena lleva `lineas`
- [ ] `python3 qa/motor.py --marca mascenter out/mascenter/<mes>/*.png`

## 9. Errores ya cometidos (no repetir)
- **04-09-2026** — el recorte de la mascota arrastró texto de la pieza de origen («óxima
  visita.») porque se recortó por caja y no por componente conexa. Ahora `localito.png`
  se extrae por componentes grandes (`build.py` no lo regenera; está en `sistema/assets/`).
- **04-09-2026** — la foto IA en 3:4 trae 40 % de cielo: en feed 1:1 el logo caía sobre
  la fachada beige. Se resolvió con `--foto-top` por formato en `build.py`. Para feed
  conviene pedirle a la IA un encuadre a nivel de calle con poco cielo.
- **04-09-2026** — Nano Banana Pro reescribió «cencosud» dos veces seguidas. No insistir con
  el prompt: parchar con el letrero real.
- **04-09-2026** — la primera ronda salió en **Poppins porque lo dice el manual**, sin medir
  las piezas. Valeria lo notó a ojo. Regla: **la tipografía se identifica por glifos sobre la
  pieza aprobada, no por lo que diga el manual** (ver memoria revex-adn-medido).
- **04-09-2026** — los reels salieron **sin música y con barrido deslizante**; el cliente los
  lleva con pista y con un golpe de rojo pleno de 0,30 s. Medir el reel de referencia a 60 fps
  antes de animar.
- **09-09-2026** — la landing de terrenos tenía el correo **genérico** de la marca. La captación
  de terrenos NO usa `contacto@mascenter.cl`: va a **`terrenos@ifbinversiones.cl`**, el buzón
  propio del área de desarrollo de Grupo IFB. Lo corrigió Francesca Pavissich por correo.
- **09-09-2026** — el cambio anterior se **commiteó y no se desplegó**: Vercel siguió sirviendo el
  build viejo un día entero y el cliente vio el correo antiguo. En esta marca hay dos landings en
  Vercel (terrenos y Algarrobal): **un cambio de cara al cliente se verifica con `curl` contra la
  URL en vivo, nunca contra el archivo local.**
- **09-09-2026** — el formulario de la landing decía «Recibimos tu postulación» y **no enviaba
  nada**. Un pendiente técnico deja de ser un pendiente cuando la página ya está publicada: si no
  se puede enviar de verdad, el mensaje no puede prometer que sí.
- **24-09-2026** — los reels de octubre (v4) salieron con la **última línea del titular dentro de la
  franja que tapa Reels**: la caja terminaba en y=1606 (`titBottom` 314) y llegaba a x≈1020 (`right`
  60), cuando el propio brief marca 420 px abajo y 180 px a la derecha. Afectaba al gancho del primer
  frame, que es la miniatura. El QA no lo vio porque `qa/motor.py` sólo mira PNG, y la zona segura de
  `marca.json` estaba escrita sólo para story. Se corrigió en `MasCenterReel.tsx` (`titBottom` 440,
  `titRight` 180) y, al angostar la caja, dos titulares dejaban «EN» y «LA» solos y partían «MÁS /
  CENTER»: ahora llevan cortes editoriales en `lineas`, que el render verifica contra el texto
  del brief. Regla: **un video también se pasa por la plantilla de zonas seguras, fotograma a fotograma.**
