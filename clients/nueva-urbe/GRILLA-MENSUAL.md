# RENTAS NUEVA URBE · Valle Altiplánico — cómo se corre una grilla mensual

> Destilado de la grilla de **noviembre 2026** (30-09-2026, Diego Aguilar con Claude): reel, estático,
> carrusel PAID, carrusel orgánico, 2 historias y 2 mailings — 22 archivos, **1 ronda** de 3 comentarios.
> Las reglas con número (R-xx) están completas, con su cita, en [`APRENDIZAJES.md`](APRENDIZAJES.md) y la
> gramática medida en [`CLAUDE.md`](CLAUDE.md). Este documento es el **orden de trabajo**: qué se hace,
> en qué orden y qué se revisa antes de mostrar algo.
>
> ⛔ Vale solo para **Rentas** (`@rentasnuevaurbe`). INU (venta) no tiene manual todavía.

---

## 1. Arranque del mes

Carlos Figueroa (contenido) deja **dos documentos**, con un mes de anticipación:

| Qué | Dónde | Cómo se lee |
|---|---|---|
| **Grilla** `RENTAS_NUEVA_URBE_GRILLA_<MES>_<AÑO>.pptx` | Drive, carpeta de grillas `1BkZDL03lWNkFbqJxlKrNl5Ucq8RcJYFB` → `N. MES` | Es un .pptx de Carlos: el token del estudio **no lo ve** y no es público. Se baja con el conector de Drive (`download_file_content` → el resultado queda en un `.txt` con el base64 → se decodifica a `raw/nuevaurbe/rentas/grilla-<mes>/`) y se lee slide por slide con `zipfile` (`ppt/slides/slideN.xml`, etiquetas `<a:t>`). `read_file_content` **corta el final** — no basta |
| **Brief de mailing** `BRIEF <MES> <AÑO> MAILING RENTAS.docx` | carpeta de briefs de mailing `1sH-38q-sCZxv5yx_ryLMKbv9YsRJgjqs` → `N. MES` (puede llegar días después; pedir el enlace) | `read_file_content` alcanza: cada celda viene rotulada («Gráfica tipo banner», «Texto orgánico», «CTA») |

**Qué trae la grilla, pieza por pieza:** fecha, el copy del post (no se diseña), el brief de la gráfica con
los textos **verbatim**, una REF de Pinterest y la celda **`COMENTARIOS CLIENTE`** — ahí escribe el cliente
(R-24, y memoria `feedback-no-siempre-es-un-comentario`). Mirar el `modifiedTime` antes de cerrar el mes.

**Alcance típico** (noviembre): 1 reel · 1 estático · 1 carrusel PAID (5) · 1 carrusel orgánico (5) ·
2 historias · 2 mailings de 4 bloques.

**Las REF de Pinterest se bajan sin navegador:**
```bash
curl -sL -A "Mozilla/5.0" "https://cl.pinterest.com/pin/<id>/" | grep -o 'https://i.pinimg.com[^"]*' | head -1
```
Se guardan en `raw/nuevaurbe/rentas/<mes>/` y **se miran** antes de componer.

## 2. La carpeta del mes

Se copia la del mes anterior y se cambia el contenido — el motor no se reescribe:

```
out/rentas/<AAAAMM>00_grilla_<mes>/
  editables/   base.css · mail.css · build.py (feed + stories) · mail.py (mailings) · render.py · fonts/ · img/
  fondos/      generar_ia.sh · generar_ia_mail.sh · preparar.py · refs/ · ia/ (originales IA) · aire/ paid/ mail/ …
  feed/ story/ mail/   ← PNG finales (NO van a git: se regeneran)
  reel/        ← el MP4 (SÍ va a git: no es determinista)
  NOTAS-PARA-LA-CM.md · NOTAS-MAILING.md
```

Punto de partida vigente: **`out/rentas/20261100_grilla_noviembre/`**.

```bash
PY=~/copylab-venv/Scripts/python.exe                 # Windows; en Mac /Users/Vale/copylab-venv/bin/python3
bash  fondos/generar_ia.sh && bash fondos/generar_ia_mail.sh   # Seedream 5 Pro (cuesta créditos: solo lo nuevo)
$PY   fondos/preparar.py                              # recorta y escala a lienzo de entrega
$PY   editables/build.py && $PY editables/mail.py     # HTML
$PY   editables/render.py [patrón]                    # PNG con Chrome headless
$PY   qa/motor.py --marca nueva-urbe out/rentas/<mes>/{feed,story,mail}/*.png
```

## 3. Las imágenes — de dónde sale cada una

1. **Foto real primero.** Las 17 fotos de `PROYECTOS INMOBILIARIOS / VALLE ALTIPLÁNICO`
   (`1_TUAwOKmMX3vYmEJuYzipVtK1ODMKpFh`) se bajan con `scripts/drive-carpeta.py <id> raw/nuevaurbe/rentas/fotos --solo .jpg`
   (el visor público sí las entrega). Exteriores a 4000-5000 px; **interiores chicos** (1037×1555) y living y
   dormitorio solo como **panorámicas**.
2. **«Atardecer», «luz cálida», «primavera»** → la foto real con **relight de cambio mínimo**
   (`magnific.py seedream "Keep this real photo almost unchanged… only change the light… Do not add or remove anything" --refs foto.jpg`).
3. **Escenas con personas** (no existen en el banco) → Seedream 5 Pro con la **foto real en `--refs`** y la
   orden de respetar pérgola, parrillas, pasto, faroles, cocina (R-35). Tres cosas en el prompt:
   - **dónde va la gente y dónde queda libre** («people in the LOWER HALF; upper 40 % calm»): si no, las
     caras caen donde va el texto;
   - sin texto legible, sin marcas;
   - Seedream **no tiene 4:5**: se pide `--aspecto carrusel` (3:4) y se recorta.
4. **No repetir el mes anterior.** El PAID de noviembre pedía las mismas tres situaciones que el de octubre
   (visita, contrato, ejecutivo): se generaron **escenas distintas** para que el anuncio no se repita.
5. **Revisar antes de usar:** hoja de contactos + zoom a las manos. Y `qa/motor.py` puede marcar «texto
   pegado al borde» por **textura de la foto** en el filo (granito, llave): se recorta la foto, no se relaja la regla.

⚠️ `public/assets/rentas/fotos/dormitorio.jpg` **trae franjas desenfocadas** (la versión rechazada, R-18). No usarlo.

## 4. Pieza por pieza

| Pieza | Gramática | Ojo con |
|---|---|---|
| **Portada de carrusel** | Caja del logo arriba · `l1` Light + caja lima en caja baja bold | **Si la foto tiene gente, el texto NO la tapa** (R-31): bloque `alto-feed` (18,5 %, bajo la caja del logo) en vez de `abajo` |
| **Lámina numerada** (`numerada()`) | Arriba a la izquierda · `01:` / `TIP 1:` en blanco fuera · título en caja azul en **una línea** · bajada con negrita parcial · sin logo | Título largo → se reparte: parte en la caja, resto a la bajada. La gente va en la mitad baja de la foto |
| **Cierre de carrusel** | Foto oscurecida + itálica + botón `RENTAS.INU.CL` + cursor lima + caja del logo | En **PAID** no se dibuja botón: el CTA es el de Meta; el cursor apunta hacia abajo. Bloque `.paid` (16 %) |
| **Estático de ficha** | Logo Valle primer hijo del bloque · titular + caja lima · fila de atributos (discos) | Atributos **separados** de la caja (`.atributos.separados`, R-32). Rótulos largos → `.anchos`. Botón de WhatsApp **solo si el brief lo pone en la pieza** |
| **Historia** | Titular arriba (13,6 %) en versales + caja azul · precio en caja lima · caja del logo abajo | Dejar la franja del sticker de enlace. Con **encuesta arriba** → clase `encuesta` (texto al 31 %, libre 13-30 %) |
| **Reel** | `RentasReelNoviembre.tsx`: logo Valle sobre dron → áreas → interiores → placa azul → cierre blanco | Ver §5 |
| **Mailing** | Ver §6 | |

Textos **verbatim del brief, con su puntuación** (R-24). Los cortes de línea se hacen a mano.

## 5. El reel

- Copiar `src/compositions/rentas/RentasReelNoviembre.tsx`, registrar en `src/Root.tsx`.
- **La locución son los bloques `VOZ: […]` de la grilla, literales**, y esos mismos textos van de subtítulo.
  Voz: **Benjamín Soto** (catálogo Magnific/ElevenLabs id 864, `eleven_v3`, estabilidad 0,45), una toma por
  bloque, en `public/assets/rentas/vo-<mes>/`. A la voz se le escriben las cifras **en palabras**
  («setecientos quince mil pesos», «rentas punto i ene u punto ce ele»): se oye exactamente el texto del brief.
- **Primero se generan las tomas y se miden** (`remotion ffprobe`), después se arman los tiempos. La URL hablada
  dura ~5,5 s → el **cierre dura 6,8 s** (R-37).
- Ducking por **tabla de tiempos** (música 1,5 → 0,5 con rampas de 0,25 s), nunca por envolvente.
- ⚠️ `useEntrada()` llamado en el JSX del componente padre usa el **frame absoluto**: hay que pasarle
  `inicio de la escena + retardo`. (El reel de octubre lo tiene mal y los textos aparecen de golpe.)
- Solo material verificado de Valle: `clips/dron_*.mp4` y `fotos/` (cocina, baño, clóset, quincho, cancha,
  piscina, fachada). **Toda foto llena el 9:16** (R-18). El rodaje «CALAMA» es de Travesía (R-05).
- Render: `./node_modules/.bin/remotion render <Id> out/…/reel/<archivo>.mp4 --browser-executable="C:/Program Files/Google/Chrome/Application/chrome.exe"`
  y hoja de fotogramas para revisar.

## 6. Los mailings

- **Solo se grafica lo destacado en NARANJO** (R-33): banner · encabezado de atención · gráfica de proyecto ·
  imagen de cierre. Lo verde (texto orgánico) y lo amarillo (CTA) van escritos en Fidelizador.
- **Si el bloque trae REF, la gráfica sigue esa idea** (R-34) — la composición de la referencia, con la paleta y
  la tipografía de Rentas. En noviembre las dos fichas traían REF vertical y por eso miden **1201×1501**:
  - `ficha-dlf`: foto arriba + panel blanco de características (rótulo entre filetes, íconos en disco azul,
    nube del precio sobre el corte);
  - `ficha-addr`: foto cálida oscurecida + amenidades en tarjetas blancas giradas en arco + píldora lima al pie.
  Sin REF, la ficha es la apaisada medida de agosto/octubre (`bloque_ficha()` en el `build.py` de octubre).
- Resto de la maqueta (1201 px): banner 750 · atención 240 · cierre 551. Banners con cajas lima centradas;
  cierre con dos pesos + caja lima, a la izquierda si la gente va a la derecha.
- **Los respiros se miden** (R-16): al terminar una ficha, mirar que ningún hueco mida varias veces lo que sus hermanos.
- Se entrega con `NOTAS-MAILING.md`: el orden de armado, bloque por bloque, con los textos y botones intercalados.

## 7. Entrega en Drive

- **Dónde:** preguntarle a quien pide. En noviembre fue `NOVIEMBRE 2026 - DISEÑOS`
  (`1bX7QbCDsRFI3xq98sV4c3Tk7uKUuhAsY`) y, dentro, `MAIL` (`1DMbH3WWg46dxXavck0saGdIOnSiHs68C`).
  Carlos después las mueve (octubre terminó en `Artes/2026/OCTUBRE 2026`) — buscar dónde están **hoy** (R-28).
- **Cómo:** `scripts/rentas-nov-subir-drive.py` (copiar y cambiar la lista). `--dry-run` primero, `--mail` para
  los correos, `--solo <patrón>` en las rondas. Actualiza **por nombre → mismo fileId** (R-27).
- **Nombres:** `DD-MM TIPO Título N detalle.png` — `03-11 REEL …mp4`, `17-11 PAID Arrienda facil 1 portada.png`,
  `24-11 CARRUSEL Aire libre 2 tip 1.png`, `25-11 ST …png`, `MAIL 03-11 bloque 1 banner.png`.
- Verificar con el conector que el `fileSize` calza con el local.

## 8. La ronda de comentarios

```bash
PYTHONIOENCODING=utf-8 $PY scripts/drive-comentarios.py <carpeta> --json salida.json
```
- El **anchor** trae `[x0, y0, x1, y1]` en fracciones del lienzo: dice **a qué elemento** apunta el comentario.
  «agrandar texto» sin mirar el ancla es adivinar.
- Aplicar → render → QA → re-subir con `--solo` → **responder y resolver** (`replies().create(..., action="resolve")`).
  Las respuestas salen a nombre de **Valeria Traverso** (el token es de su cuenta).

## 9. Checklist antes de mostrar

- [ ] `qa/motor.py --marca nueva-urbe` en **0 bloqueantes** (los avisos de «otro foco» sobre cielo liso o la caja del logo son conocidos)
- [ ] Ningún texto sobre caras o cuerpos (R-31) · ningún elemento pegado a otro (R-32) · respiros parejos (R-16)
- [ ] Textos verbatim, con puntuación · WhatsApp **+56 9 9707 9951** (el 9955 quedó discontinuado)
- [ ] Manos con zoom en toda escena IA · papeles y pantallas sin texto legible
- [ ] Ninguna foto del rodaje «CALAMA» · ninguna foto con franjas
- [ ] Reel: fotogramas revisados, la voz no se pasa del final
- [ ] Notas para la CM escritas (qué es IA, qué es foto real, qué falta confirmar con el cliente)

## 10. Lo que sigue abierto con el cliente

Precio y superficie (brief $715.000 · 59 m² contra el sitio $780.000 · 74,76 m²) · redacción exacta del
reajuste cada 12 meses · fotos o video **vertical** del living y del dormitorio · si los emojis del brief
(🌿) van o no en la pieza. Detalle en `APRENDIZAJES.md` §8.
