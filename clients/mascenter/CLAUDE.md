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

### Tipografía — GOTHAM (leída en el editable, sistema migrado el 28-09-2026)

La fuente sale de los `.ai` y `.aep` de Diego Aguilar, no de medir glifos (ver §9, 28-09). Cuerpos e
interlineados tomados del `PAID SEPT IFB.ai` con PyMuPDF; el reel, del `PERFOMANCE MASCENTER AGOSTO.aep`
y del grosor de trazo sobre `r-performance-agosto.mp4`.

| Rol | Fuente | Feed 1:1 | Story / reel 9:16 | Archivo |
|---|---|---|---|---|
| Titular en pastilla (VERSALES) | **Gotham Black** | 43,3 / 43,3 | 50,3 / 50,3 | `Gotham-Black.ttf` |
| Bajada | **GothamRnd Medium** | 32 / 36 | 56 / 56 | `GothamRnd-Medium.ttf` |
| CTA en burbuja (VERSALES) | **GothamRounded Medium** | 29,6 / 33,3 | 33,3 / 37,4 | `GothamRounded-Medium.ttf` |
| Reel: titular (VERSALES) | **GothamRounded Bold** | 60 / 66 | 90 / 98 | `GothamRounded-Bold.ttf` |
| Reel: pastilla y cierre | **GothamRnd Book** | 38 · 40 | 46 · 57 | `GothamRnd-Book.ttf` |
| Orgánico y arriendo | GothamRnd Bold/Book/Medium, GothamRounded Light — ver [`ADN-EDITABLES.md`](ADN-EDITABLES.md) §3 | | | |

- **Archivos:** `sistema/assets/fonts/` y `public/assets/fonts/mascenter/`, en TTF. Se generan con
  `python scripts/mascenter-gotham-ttf.py`, que busca los `.otf` instalados o en el disco KINGSTON y
  convierte los contornos CFF a TrueType, porque Chrome rechaza algunos CFF en silencio (caso Brushwell).
- **Calibración:** `python scripts/mascenter-calibrar-gotham.py` renderiza la pieza `CTRL` (textos de
  septiembre) y la compara contra el `.ai`: ±3 px en vertical y ±1,5 % en horizontal. Pasó el 28-09.
  Diego aprieta a mano algunas líneas (−10/1000 em); el sistema no copia ese tracking.
- En el reel, titular y pastilla usan `text-wrap: balance` (sin palabra sola), «Más Center» va unido
  con un espacio que no corta, y el cierre fija sus cortes con el texto completo antes de tipearse.
- Excepción E-04: landings y presentación comercial siguen en **Poppins** (brochure de Algarrobal).
- Historia: 04-09 se midió Montserrat contra Poppins y ganó Montserrat; Gotham nunca estuvo entre las
  candidatas. El manual 2023 dice Poppins. Ninguna de las dos es la fuente de la marca.
- Fuente de verdad del diseño: `D:\DIEGO 2023\COPYWRITERS\MAS CENTER\` (disco de Diego) y el Drive
  `GRUPO IFB - MÁS CENTER / 2026` (`1ODBfU0HUbvdwlKuwllcQ39QbR4V_qbSj`).

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
arriba (tinta 211 px, y=118), titular en versales GothamRounded Bold 90 px alineado a x=110
en el tercio inferior (⚠️ **la caja termina en y=1480 y no pasa de x=900**: ver §9, 24-09), pastilla roja (627 px, radio 48) con **ícono en círculo blanco
montado en el borde superior** y texto GothamRnd Book 46 px, cierre en rojo pleno (~3 s) con el
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
texto se escribe a ~80 caracteres/s en **GothamRnd Book ~57 px**, interlínea 59, centrado
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

### Orgánico de Instagram (grilla mensual) — plantillas y constructores

**Regla madre del orgánico (R-55):** antes de diseñar, busca en los `.ai` de Diego la pieza anterior del mismo tema
(`PyMuPDF get_text()` por mesa) y úsala de plantilla. La REF de la grilla da la idea; la plantilla manda el estilo.

| Tema | Plantilla medida (`sistema/plantillas/`) | Constructor de ejemplo (`sistema/`) |
|---|---|---|
| Carrusel de locatarios | `carrusel-locatarios-c-19-08.json` (AGOSTO mesas 11–15) | `carrusel_ruta_cafetera.py` (01-10) |
| Carrusel de mascotas / tema con banda de color | `carrusel-mascotas-c-08-08.json` (AGOSTO 6–10) | `carrusel_dia_mascota.py` (04-10) |
| Carrusel de eventos (fecha + dirección) | `carrusel-eventos-c-31-07.json` (AGOSTO 1–4) | `carrusel_panoramas_halloween.py` (20-10) |
| Post Mercado Campesino | `post-mercado-campesino-julio.json` (JULIO 22) | `post_mercado.py` (26-10) |
| Checklist de temporada | — (sobre c-19-08) | `carrusel_halloween.py` (08-10) |
| Post de proyecto (render) | — (portada de c-19-08) | `post_algarrobal.py` (14-10) |

- **Banda de color por tema (R-33):** rojo `#DC1914` por defecto · verde `#299A80` servicios/súper · cian `#01B8C1`
  clases · mostaza `#CFAF30` mascotas · rosa `#D64E74` madre · naranja `#EE7A22` Halloween (propuesta, sin medir).
  **El logo de Más Center va siempre sobre rojo (R-50)**, aunque la banda sea de otro color.
- **Sin rótulos de la grilla (R-51):** «Slide N – …», «CORTE N» y el nombre del local que venga sólo del rótulo no van.
- **Fotos (R-49):** el sujeto va entero sobre el círculo del logo (y<834) y la banda (y≥968). Si la IA lo deja bajo, se
  sube la foto o se regenera más chico.
- **Localito (R-48, R-52, R-53):** poses originales con máscara en `raw/mascenter/localito/` (apunta · celebra ·
  pulgares · saluda · vampiro-capa · vampiro-balde). La pose depende del texto de al lado. Sobre foto va inmerso, con
  piso, sombra y luz, nunca flotando. Disfraces con Seedream sobre la pose + recorte por croma.
- **Logos de locatarios (R-54):** carpeta de Diego → web oficial → Wikimedia; aplanados sobre su fondo antes del círculo.
- **Logo en carruseles (R-64):** sólo en la portada y la última slide; nunca en fichas, pasos ni mosaicos intermedios.
- **Espaciado (R-65/R-66/R-67):** ningún texto al límite de su caja (aire ≥ 40 px), cajas ajustadas al contenido, pasos
  numerados alineados por la altura de mayúscula y pegados al número.
- **LinkedIn IFB (R-32, R-42, R-62):** azul `#235D80` · celeste `#BAEAEE` · navy `#112C3A`; fondo = foto desenfocada bajo
  velo azul al 90 %; lockup GRUPO IFB | MÁS CENTER; constructor `sistema/linkedin_octubre.py`. Renders oficiales de Diego
  mandan (R-68).
- **Entrega (R-58):** carpeta del mes de la grilla, `c-dd-mm-n.png` / `p-dd-mm.png`, reemplazo en sitio en cada ronda.

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
- [ ] Tipografía Gotham cargada de verdad: `python scripts/mascenter-calibrar-gotham.py` da «✓ calibrado»
      (si una cara no carga, Chrome pone una de reemplazo sin avisar y la calibración falla)
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
- **28-09-2026** — **el sistema estuvo en la fuente equivocada desde el primer día.** La ronda 1 del
  04-09 salió en Poppins porque lo decía el manual; se corrigió a Montserrat midiendo glifos, pero
  Gotham nunca estuvo entre las candidatas, y el editable decía Gotham desde el principio. Además, el
  `base.css` commiteado seguía declarando Poppins aunque las piezas se entregaron en Montserrat.
  Regla: **la tipografía se lee en el editable (PyMuPDF sobre el `.ai`, texto de los `.aep`) antes de
  medir glifos, y la migración se valida renderizando contra el editable, no a ojo.**
- **24-09-2026** — los reels de octubre (v4) salieron con la **última línea del titular dentro de la
  franja que tapa Reels**: la caja terminaba en y=1606 (`titBottom` 314) y llegaba a x≈1020 (`right`
  60), cuando el propio brief marca 420 px abajo y 180 px a la derecha. Afectaba al gancho del primer
  frame, que es la miniatura. El QA no lo vio porque `qa/motor.py` sólo mira PNG, y la zona segura de
  `marca.json` estaba escrita sólo para story. Se corrigió en `MasCenterReel.tsx` (`titBottom` 440,
  `titRight` 180) y, al angostar la caja, dos titulares dejaban «EN» y «LA» solos y partían «MÁS /
  CENTER»: ahora llevan cortes editoriales en `lineas`, que el render verifica contra el texto
  del brief. Regla: **un video también se pasa por la plantilla de zonas seguras, fotograma a fotograma.**
- **28-09-2026** — **las GothamRnd (Bold, Book, Medium) traían el espacio duro U+00A0 con 25.000 unidades de
  avance** (el espacio normal mide 300). Cualquier `&nbsp;` («14:00&nbsp;hrs.», «Más&nbsp;Center») salía partido con
  un hueco de media pieza. Se corrigieron los TTF de `sistema/assets/fonts` y `public/assets/fonts/mascenter`, y
  `scripts/mascenter-gotham-ttf.py` lo corrige al regenerar (`arreglar_nbsp`). Para no partir una línea, usa
  `<span style="white-space:nowrap">`.
- **28-09-2026** — **el post del 26-10 se diseñó desde cero** existiendo la pieza de julio del mismo tema; Diego
  pidió seguirla. Regla: buscar la pieza anterior del tema en los `.ai` antes de diseñar (R-55).
- **28-09-2026** — **Seedream reescribe los letreros reales** («Litle Caesars», «Little Cagars»): R-10 vale para
  toda foto real intervenida con IA, no sólo para Nano Banana.
