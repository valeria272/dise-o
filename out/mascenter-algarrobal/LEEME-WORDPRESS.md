# Strip Center Algarrobal — landing para WordPress

Paquete autocontenido: se abre con doble clic en `index.html`, sin instalar nada.
Todo lo que la página necesita (tipografías, imágenes, texturas, video) viaja dentro
de `assets/`. **No llama a ningún servidor externo.**

---

## 1. Qué trae el paquete

```
index.html                          la landing completa (HTML + CSS + JS en un solo archivo)
assets/
├── fonts/    poppins-light · regular · medium · semibold · bold  (.woff2)
├── img/      fotos de sección, mapa, masterplan, logos y galería
│   └── iconos/   los 12 iconos del diseño, PNG con transparencia
└── video/    algarrobal-hero-loop.mp4 · algarrobal-video-completo.mp4 · hero-poster.jpg
```

**Peso total: ~19 MB**, de los cuales 14,7 MB son los dos videos.
Lo que se descarga al abrir la página es mucho menos: **2,1 MB** (el loop del hero
más el poster y el propio HTML). El resto entra en diferido con `loading="lazy"`,
y el video completo **solo se descarga si alguien aprieta play**.

---

## 2. El video: qué se hizo y por qué

El master entregado (`video-algarrobal-v6.mp4`) pesa **292 MB** — 62 segundos en
1920×1080 a 60 fps. Ese archivo no puede ir en una web tal cual.

Además tiene una característica que define todo: **es un video narrado, con locución
y subtítulos quemados en la imagen, y termina con una placa blanca de logo.** Por eso
no sirve como fondo mudo en bucle: se verían los subtítulos detrás del titular y la
placa final cortaría el loop.

La solución fue partirlo en dos:

| Archivo | Qué es | Peso | Dónde se usa |
|---|---|---|---|
| `algarrobal-hero-loop.mp4` | 14 s del tramo cinematográfico (39,5 s → 53,5 s), **sin audio**, recortado arriba para eliminar la banda de subtítulos | **1,9 MB** | Fondo del hero, en bucle automático |
| `algarrobal-video-completo.mp4` | Los 62 s íntegros con locución, comprimidos a 1600×900 | **12,8 MB** | Se abre a pantalla completa al apretar «Ver el video del proyecto» |
| `hero-poster.jpg` | Primer fotograma del loop | 200 KB | Imagen de carga y **reemplazo del video en móvil** |

**Sobre el GIF: no.** Un GIF de 14 s en esa calidad pesaría entre 30 y 80 MB —bastante
más que el video original comprimido—, no tiene audio y se ve peor. El MP4 en bucle,
mudo y con `playsinline` es lo correcto y es lo que usa el propio sitio de Pirque
Nogales Poniente (su video de portada pesa 23 MB; el nuestro pesa 1,9 MB).

**En pantallas de menos de 820 px el video no se descarga**: se muestra el poster.
Es la misma decisión que tomó el desarrollador de Pirque (`mobile-video-image`).

---

## 3. Subirlo a WordPress

El sitio de referencia corre **WordPress + tema Salient + WPBakery + Contact Form 7 +
Float Menu**. Hay dos caminos según cómo quieran mantenerla.

### Opción A — Página nueva con un bloque HTML (la más rápida)

1. **Sube los assets.** Por FTP o el Administrador de archivos de Hostinger, copia la
   carpeta `assets/` completa a:
   `/wp-content/uploads/algarrobal/assets/`
2. **Ajusta las rutas.** Abre `index.html` en un editor de texto y reemplaza todas las
   apariciones de `assets/` por la URL pública:
   `https://algarrobal.mascenter.cl/wp-content/uploads/algarrobal/assets/`
   (busca y reemplaza `"assets/` → `"https://…/algarrobal/assets/`)
3. **Crea la página** en WordPress → Páginas → Añadir nueva.
4. Elige una plantilla **a ancho completo, sin cabecera ni pie del tema**
   (en Salient: *Page Settings → Header → Transparent* y *Full Width*), porque la
   landing trae su propio header y su propio footer.
5. Pega en un bloque **HTML personalizado** (o *Raw HTML* de WPBakery) todo el
   contenido que está **entre `<body>` y `</body>`**, y el bloque `<style>…</style>`
   completo justo antes.

> El `<style>` puede ir dentro del mismo bloque HTML: WordPress no lo elimina en un
> bloque *HTML personalizado*. Si el editor te lo borra, pega el CSS en
> **Apariencia → Personalizar → CSS adicional**.

### Opción B — HTML plano fuera de WordPress (lo más fiel y lo más rápido de cargar)

Sube la carpeta completa por FTP a una subcarpeta o a un subdominio
(`algarrobal.mascenter.cl`) y listo. No hay que tocar nada: las rutas ya son
relativas. Es la opción recomendada si no necesitan editar los textos desde el
panel de WordPress.

---

## 4. Conectar el formulario

Hoy el formulario **valida los campos pero no envía correo** — avisa en pantalla que
falta conectarlo. Los campos ya están calcados de los de Pirque Nogales Poniente para
que el equipo reutilice el mismo formulario de Contact Form 7:

| Campo de la landing | `name` | Equivalente en Pirque |
|---|---|---|
| Nombre y apellido | `nombre` | Nombre y Apellido *(obligatorio)* |
| Correo | `email` | Email *(obligatorio, valida formato)* |
| Teléfono | `telefono` | Teléfono *(obligatorio)* |
| Motivo | `motivo` | Motivo *(obligatorio)* |
| Proyecto | `proyecto` | Campo de solo lectura — acá dice **Strip Center Algarrobal** |
| Mensaje | `mensaje` | Mensaje *(obligatorio)* |

**Para conectarlo:** duplica el formulario CF7 de Pirque, cambia el valor fijo del
campo de proyecto a `Strip Center Algarrobal`, verifica que el destinatario sea
`arriendos@mascenter.cl` y reemplaza el bloque `<form class="formulario">…</form>`
de `index.html` por el shortcode `[contact-form-7 id="XXX"]`.

El CSS del formulario ya está escrito para que los campos de CF7 se vean igual: las
reglas apuntan a `form.formulario input, textarea, select`, así que basta con dejar
la clase `formulario` en el `<form>` que genera CF7 (se configura en la pestaña
*Additional Settings* o envolviéndolo en un `<div class="formulario">`).

---

## 5. De dónde salió cada cosa

- **El diseño** es el PDF `LANDING_ALGARROBAL_CORREGIDO.pdf` de la diseñadora
  (1900 × 11533 px). Las 12 secciones están en el mismo orden y con los textos
  literales.
- **Los movimientos** están calcados del sitio de Pirque Nogales Poniente:
  aparición `fade-up` de 40 px en 0,8 s con curva `cubic-bezier(.16,1,.3,1)`,
  retardos escalonados de 0,1 / 0,2 / 0,3 / 0,4 s, disparo con `IntersectionObserver`
  al 15 % de visibilidad y una sola vez por elemento. Es exactamente lo que hace
  la referencia, sin cargar jQuery ni ninguna librería.
- **Los colores** se midieron píxel a píxel sobre el PDF y se cruzaron con el CSS
  del sitio en vivo:

  | Color | Hex | Dónde |
  |---|---|---|
  | Rojo Más Center | `#E52521` | Hero, botones, cifras, tabla |
  | Vino | `#8B1623` | Masterplan, etiqueta de foto, caja de descripción |
  | Vino oscuro | `#631513` | Bloque de Accesibilidad |
  | Gris de sección | `#DADADA` | Ubicación |
  | Gris de sección 2 | `#D2D2D3` | Locales comerciales |
  | Claro | `#F3F1F1` | Conectividad, formulario |
  | Negro | `#000000` | Descripción, beneficios, pie |

- **La tipografía** es **Poppins** en cinco pesos (300, 400, 500, 600, 700), la misma
  del PDF y la misma que carga el sitio de Pirque. Va auto-hospedada en
  `assets/fonts/` para no depender de Google Fonts.
  *Si el tema Salient ya carga Poppins, se puede borrar el bloque `@font-face` del
  principio del CSS y la página seguirá viéndose igual.*
- **Los logos** (`logo-mascenter-color.svg`, `logo-mascenter-blanco.svg`,
  `logo-ifb.png`, `favicon.png`) son los archivos oficiales que ya usa el sitio de
  Más Center.
- **Los iconos** se extrajeron uno por uno del PDF a 5× de resolución, con
  transparencia. Son los de la diseñadora, no reemplazos.
- **El mapa y el masterplan numerado** se rindieron desde el PDF porque llevan
  gráfica vectorial (calles, etiquetas, la numeración de los locales) montada sobre
  la foto: extraer solo la foto habría dejado el mapa vacío.
- **La foto de la autopista** está recortada con las coordenadas exactas que usó ella
  en el PDF (x 42,7 %–74,1 %, y 43,7 %–80,5 % del original de 6016 × 4016).

---

## 6. Decisiones que hay que confirmar con la diseñadora

El PDF es una pieza de una sola imagen; una web necesita tres cosas que ahí no
estaban. Las resolví siguiendo la referencia de Pirque, pero conviene visarlas:

1. **Cabecera fija.** El PDF no trae una. Puse la del sitio de Pirque: logo a la
   izquierda, menú a la derecha (Ubicación · El proyecto · Masterplan · Galería) y
   botón rojo Contáctanos. Es transparente sobre el hero y se vuelve negra al bajar.
2. **Sección de formulario.** El PDF solo tiene botones «CONTÁCTANOS» y los datos en
   el pie. Como el objetivo de la landing es captar arrendatarios, agregué la sección
   de formulario antes del pie, en el mismo lugar donde la tiene Pirque.
3. **Botón «Ver el video del proyecto»** en el hero, para que el video narrado se
   pueda ver con su locución. Sin él, el video de 62 s no tendría dónde reproducirse.
4. **Menú flotante** de tres botones a la derecha (correo, mapa, WhatsApp): aparece
   dibujado en el PDF de la diseñadora y también existe en Pirque vía el plugin
   Float Menu. Acá está hecho en CSS, sin plugin.

---

## 7. Datos de contacto que quedaron cableados

- Correo: **arriendos@mascenter.cl**
- Teléfono y WhatsApp: **+56 9 4118 2947** (`wa.me/56941182947`)
- Instagram: **@mascenter**
- Dirección: **Avenida Los Fundos s/n, Colina** — el pin del mapa apunta a esa
  búsqueda en Google Maps. **Si tienen la coordenada exacta del terreno, cámbienla**
  por un enlace con `?q=lat,long`; la dirección genérica no cae en el punto justo.

---

## 8. Revisado antes de entregar

- Sin desborde horizontal en 1440, 1024 y 390 px de ancho.
- Sin errores de JavaScript ni recursos rotos.
- Las cinco variantes de Poppins cargan y traen tildes, eñes y el `²`.
- Las 64 animaciones de entrada disparan al hacer scroll y ninguna queda invisible.
- Respeta `prefers-reduced-motion`: si el visitante pidió menos movimiento en su
  sistema operativo, todo aparece fijo y sin parallax.
- Menú móvil, carrusel con arrastre, lightbox del video y validación del formulario
  probados.
