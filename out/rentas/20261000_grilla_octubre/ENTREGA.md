# RENTAS NUEVA URBE · VALLE ALTIPLÁNICO — grilla OCTUBRE 2026

> Producido el 02-09-2026. Sistema: `clients/nueva-urbe/CLAUDE.md` · criterio vigente:
> **Paulina Bustamante (septiembre 2026)**, decidido por Valeria.

## Qué está listo

| Pieza | Fecha | Archivos | Estado |
|---|---|---|---|
| **Carrusel Halloween** | mar 27-oct | `feed/rentas_c-halloween1..5.png` · 4500×5625 | ✅ **Listo para revisión** |
| **Historia Halloween** | jue 29-oct | `story/rentas_st-halloween-29-10.png` · 4500×8000 | ✅ **Lista para revisión** |
| **Historia proyecto** | jue 2-oct | `story/rentas_st-proyecto-02-10.png` · 4500×8000 | ✅ **Lista para revisión** |
| **Estático «Sin comisión»** | mar 13-oct | `feed/rentas_estatico-sin-comision-13-10.png` · 4500×5625 | ✅ **Listo para revisión** |
| **Reel comercial** | mar 6-oct | `reel/rentas_reel-octubre-06-10.mp4` · 1080×1920 · 30 s | ✅ **Listo para revisión** |

Los 5 fondos son **imágenes IA** (Nano Banana Pro, 4K), por decisión de Valeria: el brief
pide personas manipulando cinta, ganchos y telarañas, y eso no existe en el banco del cliente.
Se ambientaron para que se lean como un departamento de Valle Altiplánico —muro beige claro,
porcelanato claro, persiana zebra, luz natural cálida— y **sin marcas legibles** en los envases.

**Corregido tras la revisión de Valeria:** la caja del logo estaba **65 % más alta de la cuenta**
(1088×1351 en vez de 1088×821) y el logotipo quedaba hundido contra el borde inferior — el padding
porcentual del CSS peleaba con el `aspect-ratio`. Ahora va en píxeles y calza con la referencia:
ratio 0,755 contra 0,754, aire superior 17,8 %.

**QA hecho:**
- Las 5 piezas a **4500×5625** exactos y con los hex medidos (`#1372F1` / `#CCDC00`).
- **Manos revisadas con zoom 4×** en las cuatro láminas que las muestran: anatomía correcta,
  cinco dedos, nudillos y uñas bien formados. Ninguna se descartó.
- **Contraste** del titular de la portada contra su fondo: **9,63:1** (mínimo legible 4,5:1).
- **Margen inferior libre 6,4 %–7,0 %**, dentro del rango propio de Paulina (5,8 %–16 %).
- Cortes de línea **a mano**: al dejar envolver solo quedaban huérfanas («removibles», «pared.»).
- Cero `style=""` suelto en el HTML: todo sale de `base.css`.

### El reel del 6-oct
30 s, 1080×1920, con la estructura y el **cierre canónico** medidos sobre el reel de
septiembre: caja de logo arriba todo el reel, subtítulos en caja azul, la cifra grande en
itálica con la unidad en caja lima, la placa azul con curvas de nivel y el ícono `$` en disco
lima con cursor, y el cierre en fondo blanco con el logo centrado y `¡Escríbenos por WhatsApp!`.

**Sin franjas.** La primera versión ponía la panorámica del dormitorio como banda nítida sobre
fondo desenfocado y Valeria la rechazó — «no pueden existir esas franjas arriba y abajo, se ve muy
amateur». Ahora **toda foto que entra al reel llena el 9:16**; la panorámica quedó fuera y el
tramo del precio pasó a la cocina.

**Música, sin locución.** Por ahora va **sólo música y subtítulos** (decisión de Valeria). La
pista se eligió midiendo: sus reels de julio, agosto y septiembre dan centroide espectral
**1711–2330 Hz** y relación grave/medio **0,16–0,28** —pista clara y liviana, sin bajo pesado—.
La elegida mide 2555 Hz y 0,10, lo más cercano de la biblioteca Mixkit del estudio. *(Ojo: la
`musica_mixkit32` que estaba asociada a INU mide 628 Hz y 0,62 — mucho más oscura, no servía.)*
Va normalizada a −16 LUFS y el reel queda en **−16,4 dBFS RMS**, sin clipping, con fundido de
entrada y de salida.

**Los interiores van en FOTO con Ken Burns, no en video, y por una razón de fondo:** el rodaje
de `CALAMA/VERTICAL` que hay en Drive **no es de Valle Altiplánico** (ver el manual, §Compuerta
de material). Así que el reel usa sólo material verificado: el dron de `videos-dron` y las fotos
del proyecto. El dormitorio existe únicamente como panorámica de 1872×805, así que va como banda
nítida sobre un fondo desenfocado de sí misma — que es lo honesto con una pano.

**Lo que le falta: la locución.** Los cinco reels del cliente —mayo a septiembre— llevan
**voz humana real**: se midió la modulación silábica de 3 a 8 Hz y da 35 %–41 %, cuando la música
instrumental se queda en 15 %–25 %. Para replicar esa voz habría que clonarla, y no se pudo:
Higgsfield quedó en **0,43 créditos** y el estudio no tiene clave de ElevenLabs. La voz sintética
que se probó (`es-CL-LorenzoNeural`, calibrada a 123 Hz contra los 138 del cliente) sonó falsa y
se sacó. **El reel va sin voz**: el guion del brief está en los subtítulos, listo para que lo
grabe el mismo locutor de los otros meses.

Tampoco hay foto de **living** en resolución usable.

### El estático del 13-oct
Pieza de **ficha**: lleva los dos logos, la **fila de atributos** y el **botón de WhatsApp**, igual
que el estático de julio que el cliente aprobó. Fondo: el quincho real (escala 1,70×).
Los discos de atributo son **blancos traslúcidos con borde e ícono AZULES** —lo hice al revés la
primera vez— y miden 10,6 % del ancho, medido sobre la pieza de julio. El WhatsApp va
**+569 9707 9951**, verbatim del brief y coincidiendo con lo que se publicó en julio.
QA: «Arrienda» 5,66:1 · rótulos 18,50:1 · margen inferior 6,60 %.

### La historia del 2-oct
Fondo: fachada con juegos y áreas verdes (escala 2,32×). Lleva **velo doble** —arriba y abajo—,
porque con velo sólo arriba el bloque de precio caía sobre la fachada clara y el contraste se iba
bajo el mínimo. QA: 7,59:1 · 10,21:1 · 16,32:1; el texto entra a **337 px** de 1920, sobre la zona
segura de 250.

### La historia del 29-oct
Fondo: fotograma 4K del **dron del cliente** (`Valle Altiplánico - Jul 24.MP4`, 93 Mbps), con el
blur fuerte que pide el brief y **luces naranjas de bokeh**. No se pegaron calabazas a la fachada:
sobre un fondo desenfocado eso se leería como fotomontaje, y el brief pide «detalles sutiles».
QA: primera tinta a **256 px** en términos de 1080×1920 —bajo la zona segura de 250 px de Instagram,
mejor que la referencia de septiembre, que entra a 220—; contraste del titular **10,26:1**; la franja
entre el precio y la caja del logo queda libre para el sticker de enlace.

**Textos:** verbatim del brief (`RENTAS_NUEVA_URBE_GRILLA_OCTUBRE_2026_1.pptx`).
Los cortes de línea son míos.

## Qué falta y por qué

| Pieza | Fecha | Bloqueo |
|---|---|---|


| Carrusel PAID «Arrienda fácil» | mar 20-oct | faltan **visita, contrato y ejecutivo** — no existen en el material verificado de Valle Altiplánico |


**Apareció la carpeta de fotos del proyecto y con ella salieron tres piezas más.**
`PROYECTOS INMOBILIARIOS / VALLE ALTIPLÁNICO` tiene **17 fotos reales del condominio**, y en
buena resolución: el **quincho a 4960×3307**, la **piscina a 5184×3456**, la cancha, las fachadas
con juegos y los estacionamientos. Los fondos se armaron con escalas de **1,6× a 2,4×**, sin
upscale forzado. Los interiores (clóset, baño, cocina, dormitorio) sí vienen chicos —1037×1555—
y no dan para 4500 px.

**El dron (2,3 GB) resolvió la historia de Halloween, pero es TODO aéreo exterior.**
`videos-dron` trae tres archivos —`Valle Altiplánico - Jul 24.MP4` en 4K a 93 Mbps,
`Secuencia 01_1.mp4` en 4K a 114 Mbps y `Valle 5.MP4` en HD—, los tres limpios y sin subtítulos.
Se ven la fachada, la piscina, la cancha y las áreas verdes desde arriba. **No hay un solo
interior, ni el quincho de cerca, ni personas.** Para eso hace falta abrir
`NUEVO MATERIAL (FEB 2025)` (`1RppTkRirNZtXrpVz2qVmDrnSLzJRRgX6`), que sigue compartida como
«sólo personas de Copywriters» y no como «cualquier persona con el enlace».
Se intentó sacarlo de los 6 reels entregados (son 4K, 2160×3840, así que un fotograma sirve
como foto), pero **los reels están subtitulados casi de punta a punta**: de 611 fotogramas
analizados a 6 fps, solo **12** quedan sin gráfica encima, y son todos del mismo instante.
La marca manda **foto real del condominio**, así que no se reemplaza con IA.

Hace falta abrir en Drive:
- `PROYECTOS INMOBILIARIOS / VALLE ALTIPLÁNICO` — `1_TUAwOKmMX3vYmEJuYzipVtK1ODMKpFh`
- `VALLE ALTIPLÁNICO / videos-dron` — `1SMwy6tUMfQnqe3SpDzifg3lhyH4-AiKc`
- `MATERIAL CLIENTE 2024` — `14ztIGZ0Zxs9zo6QryXxjzVORqa6R4zf7` (los MP4 del cliente, sin subtítulos)
- `LOGOS INU` — `1fO3qfzO8FBBg7Kpr5IL-IQWO65zJrgo-` (para tener los logos oficiales)

Mientras tanto, los logos se **extrajeron de las piezas entregadas**: `logo_rentas.png`
(590×550, de la caja blanca de `rentas_c-benef1` a 4500 px) y `logo_valle_blanco.png`
(870×456, del banner `rentas-mail_1.3`). Sirven, pero conviene reemplazarlos por los oficiales.

## Decisiones que hay que confirmar

1. **⚠️ El WhatsApp del estático del 13-oct.** El brief de **grilla** dice `+56 9 9707 9951`,
   que es el número de **Travesía (INU, venta)**. El brief de **mailing del mismo mes** usa
   `9955` dos veces y su nota final dice literal «(2) número de WhatsApp (se usa +56 9 9707 9955)».
   Julio y agosto también usaron 9955. Valeria eligió «verbatim del brief» **antes** de que
   apareciera esa nota.
2. **El botón `RENTAS.INU.CL` de la lámina 5.** No está en el brief; es el cierre canónico del
   sistema (aparece en todos los carruseles y reels de Rentas). Si el cliente lo quiere fuera,
   se borra sin tocar nada más.
3. **⚠️ El precio y la superficie no calzan entre canales.** El brief y el feed de Instagram
   (post del 18-ago) dicen **desde $715.000 y desde 59 m²**; el sitio `rentas.inu.cl` publica
   **desde $780.000 y desde 74,76 m²**. Puede ser otra tipología, pero conviene alinearlo antes
   de que salga una pieza con una cifra y la web muestre otra.
4. **Valle Altiplánico SÍ tiene piscina** — se ve en el dron de mayo. El brief de septiembre la
   nombraba y el de octubre no. Vale la pena recuperarla como atributo.
5. **La torre del frente dice «LAGUNA VERDE»** en la fachada, en el metraje de mayo. Asumo que es
   el nombre de la torre dentro del condominio; conviene confirmarlo antes de publicar ese plano.

## Cómo reproducirlo

```bash
cd out/rentas/20261000_grilla_octubre/editables
python3 build.py      # genera los HTML desde los textos del brief
bash render.sh        # HTML -> PNG con Chrome headless, a 4500 px
```
