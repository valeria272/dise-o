# MÁS CENTER · GRUPO IFB — cómo se corre una grilla mensual

> Destilado de la grilla de **octubre 2026** (28 al 30-09-2026, Diego Aguilar con Claude): 4 carruseles de IG,
> posts, stories, 4 carruseles de LinkedIn y el reel del 23-10, con unas 12 rondas de comentarios de Diego.
> Las reglas con número (R-xx) están completas, con su cita, en [`APRENDIZAJES.md`](APRENDIZAJES.md), y la
> gramática medida en [`CLAUDE.md`](CLAUDE.md). Este documento es el **orden de trabajo**: qué se hace, en qué
> orden y qué se revisa antes de mostrarle algo a Diego.

---

## 1. Arranque del mes

1. **La grilla.** Es el Excel `GRILLA DE CONTENIDOS IFB - <MES> <AÑO>.xlsx` en el Drive de la agencia. Tiene las
   pestañas CALENDARIO, GRILLA INSTAGRAM, GRILLA STORIES DE INSTAGRAM, ORGÁNICOS y GRILLA LINKEDIN.
   - Se baja la **xlsx** y se lee con `openpyxl`. El conector de Drive no muestra los **hipervínculos de celda**,
     y ahí vive la REF de cada pieza (`cell.hyperlink.target`, R-57).
   - ⚠️ Las fechas de la fila de encabezado vienen mal leídas (octubre salió como «2010-03-23» = 23-10). La fecha
     real se saca del orden de las columnas y del CALENDARIO, no del valor de la celda.
   - El texto de la celda es **verbatim**. Los rótulos «Slide N – …», «CORTE N», «REF», «Texto:» y «Visual:»
     organizan el brief y **no van en la gráfica** (R-51).
2. **La carpeta de entrega.** Es `DISEÑO GRILLAS/<AÑO>/<N>. <MES>` en Drive (octubre: «10. OCTUBRE»,
   `1h7_dB1HxA2KBThQhUuUinHG24DP9wHwK`). Ahí va todo, con la nomenclatura de Diego (R-58):
   - `c-dd-mm-n.png` para los carruseles de IG;
   - `p-dd-mm.png` para los posts;
   - `st-…` para las stories;
   - `lk-dd-mm-n.png` o `lk-dd-mm.mp4` para LinkedIn.
3. **La plantilla viva.** Antes de diseñar un tema que ya existió, se busca la pieza anterior en los `.ai` de Diego
   (`D:\DIEGO 2023\COPYWRITERS\MAS CENTER`, `PyMuPDF get_text()` por mesa) y se usa de plantilla (R-55). Las ya
   medidas están en `sistema/plantillas/` (tabla en `CLAUDE.md` § Orgánico).
4. **Lo que queda fuera.** Lo que la grilla marca en stand by (en octubre, el reel del 19-10 y la story de la
   corrida) no se hace hasta que Scarlette lo libere.

## 2. Orden de producción

Por pestaña, en este orden. Cada pieza es un constructor Python propio en `sistema/` (HTML → Chrome headless → PNG)
o una composición Remotion en `src/compositions/mascenter/`.

| Pestaña | Qué sale | Constructor de referencia (octubre) |
|---|---|---|
| Grilla Instagram | Carruseles 1080×1350 y posts | `carrusel_ruta_cafetera.py` · `carrusel_dia_mascota.py` · `carrusel_halloween.py` · `carrusel_panoramas_halloween.py` · `post_mercado.py` · `post_algarrobal.py` · cierres en `cierres_octubre.py` |
| Stories | 1080×1920, fijas o video | `stories_octubre.py` · `KiosclubStoryHalloween.tsx` |
| LinkedIn | Carruseles IFB 1080×1080 y reel 1080×1920 | `linkedin_octubre.py` · `IfbReelNuevosProyectos.tsx` |

Para arrancar un mes nuevo se **copia el constructor del mes anterior del mismo tipo** y se cambia el contenido.
No se crea una composición genérica.

## 3. La gramática que quedó aprobada (resumen)

### Carruseles de Instagram
- **Portada:** foto a sangre, logo de Más Center arriba al centro, titular en Gotham Black y pastilla del color del
  tema. Si Diego manda una **referencia**, la portada sigue esa gramática, y la marca se mantiene en color,
  tipografía, logo y Localito (R-81).
  - Titular tipo sticker: contorno **redondo** y **sin sombra** (R-84).
- **Interiores:** foto arriba, banda de color desde y=968 con el círculo del logo del locatario, texto centrado en
  la banda y flecha.
  - El sujeto va **entero** sobre el círculo y la banda (R-49).
  - Sin logo de Más Center en las slides intermedias (R-64).
- **Cierre (última slide):** una **imagen de cierre, no un interior** (R-75, R-77, R-85):
  - foto hermana de la portada al atardecer (puede ser otro strip center, R-78) y logo arriba;
  - titular centrado en Gotham Black blanco **sin caja**, y **sólo la bajada** en pastilla;
  - sin banda, sin círculo, sin flecha y **sin Localito**.
- **Colores de la banda por tema (R-33):** rojo por defecto, mostaza para mascotas, naranja para Halloween, etc.
  El logo de Más Center va **siempre sobre rojo** (R-50).
- **Localito:** va en la portada o en los interiores, con una pose que responde al texto (apunta, celebra,
  pulgares, saluda). Sobre una foto va **inmerso** en la escena, nunca flotando (R-48, R-53). Se le puede poner
  disfraz de temporada (R-52). **Nunca en el cierre** (R-85).
- **Carrusel de recorrido** (ruta, paradas):
  - saltos punteados de círculo a círculo, con la cumbre en el borde del slide;
  - tablero de avance ①②③ **centrado** arriba (R-80, R-83);
  - la portada despega y el cierre recibe el último salto.

### Stories
- **Zonas seguras:** texto y CTA entre y=269 y y=1651.
- **Fondo claro de temporada:** el texto va en el rojo oscuro del manual `#65140F`, sin sombra (R-69).

### LinkedIn (Grupo IFB, corporativo)
- **Paleta y fondo:** azul `#235D80`, celeste `#BAEAEE` y navy `#112C3A`. El fondo es una foto real desenfocada bajo
  un velo azul al 90 % (R-62).
- **Lockup:** GRUPO IFB | MÁS CENTER, **sólo en la portada y la última slide** (R-64).
- **Portada de proyecto:** toma de dron al atardecer generada sobre los renders oficiales (R-74). Los renders que
  manda Diego **mandan** en toda la pieza (R-68).
- **Cajas:** se ajustan al texto, con aire (R-65, R-66). En los CTA se destaca sólo el dato accionable (R-72).
- **Fichas:** íconos de ~72 px (R-73). Los pasos numerados van alineados por la altura de mayúscula (R-67).
- **Reel:** se traslada la mecánica de la REF a la gramática IFB (R-86). Los textos son los del brief, con los
  renders reales de los proyectos y música instrumental generada con Magnific.

## 4. Imágenes: de dónde salen y cómo se tratan

**Jerarquía** (R-79):
1. **Foto real** del local o del proyecto: web oficial, Instagram (`scripts/ig-fotos-publicas.py <cuenta> <carpeta>`,
   que usa el embed público), Google o material de Diego.
2. Su **producto real**, recortado y montado en una escena. Se armoniza con Seedream en modo edición.
3. **Seedream 5 Pro** con referencias de sus fotos (su vajilla, sus tortas, su interior). Nunca un genérico de banco.

**Reglas de tratamiento:**
- **Imágenes que adjunta Diego** (R-82): se repasan siempre, sin preguntar: calidad, nitidez y encuadre al formato.
  Si hace falta, se recrean con Seedream usando la adjunta de referencia, conservando la marca y las etiquetas.
  - Las imágenes pegadas en el chat no quedan en disco: se recuperan del `.jsonl` de la sesión.
  - Si la foto tiene texto chico, se escala con Lanczos: el upscaler de IA inventa letras.
- **Límites de Seedream:**
  - no respeta tamaños ni posiciones de un objeto en primer plano, y al «armonizar» vuelve a agrandar al sujeto:
    se resuelve en la diagramación (R-76);
  - reescribe letreros de fondo: se desenfoca el fondo (R-63) o se parcha el letrero real (R-10).
- **Verificar la cuenta.** Antes de usar un Instagram, se confirma que la cuenta sea la del local correcto: en
  octubre «cafeterialaparroquia» resultó ser de México.

## 5. Antes de mostrarle algo a Diego

- [ ] Textos verbatim del brief. Sin rótulos de estructura (R-51).
- [ ] Ningún texto al límite de su caja: aire ≥ 40 px (**R-65, la regla que más se repitió: 3 rondas**).
- [ ] Sujetos enteros; ni la banda, ni el círculo, ni las pastillas cortan patas, caras ni productos.
- [ ] Logo en la portada y en la última slide, y en ninguna otra.
- [ ] Cierre con la gramática de cierre (§3), no como interior.
- [ ] Las fotos de locatarios se parecen al local real.
- [ ] Revisar a zoom 1:1 los rótulos y etiquetas de terceros.
- [ ] `PYTHONIOENCODING=utf-8 ~/copylab-venv/Scripts/python.exe qa/motor.py --marca mascenter <pngs>`, sin bloqueantes.
  Avisos conocidos que no se corrigen:
  - «banda con otro foco» = profundidad de campo de una foto real;
  - «rojo fuera de sistema» = un rojo dentro de la foto (una cinta, un atardecer).

## 6. Rondas de feedback (cómo se cierra cada una)

1. **Leer.** `scripts/drive-comentarios.py --nombre <prefijo>` (por ejemplo `c-04-10`). El `anchor` dice a qué zona
   de la pieza apunta el comentario. Revisar también la celda COMENTARIOS de la grilla.
2. **Aplicar** en el constructor, no en el PNG. Si el comentario vale para «todos los cierres» o «todos los
   carruseles», se aplica a todos.
3. **Reemplazar en sitio.** `files().update(fileId, media_body)`, sin copias, y verificar el md5. Así se mantiene el
   link y los comentarios siguen colgados de la pieza.
4. **Responder y resolver** cada comentario en Drive: `replies().create(…, action="resolve")`, en tuteo, diciendo
   qué se cambió.
5. **Cosechar.** Regla nueva o confirmada en `APRENDIZAJES.md`, una entrada en `BITACORA.md` y
   `scripts/memoria-cliente.py cerrar mascenter`.

## 7. Lo que Diego corrigió en octubre, para no repetirlo

| Se hizo así | Diego pidió | Regla |
|---|---|---|
| Rótulos «Slide 2 – Decoración» en la gráfica | Omitirlos en todos los carruseles | R-51 |
| Logo de Más Center sobre mostaza | Siempre sobre rojo | R-50 |
| Localito «volando» sobre la foto | Inmerso en el strip center | R-53 |
| Cierre como slide interior (banda, collage, Localito) | Imagen de cierre como la portada, al atardecer | R-75 |
| Titular del cierre en caja | Centrado, sólo la bajada destacada | R-77 |
| Localito en el cierre | Eliminarlo | R-85 |
| Cafeterías genéricas de IA | Fotos reales de sus Instagram | R-79 |
| Línea recta entre paradas | «Jueguito» de saltar de café en café | R-80 |
| Etiqueta de parada a la izquierda | Centrada en todas las slides | R-83 |
| Fotos adjuntas usadas tal cual | Repasarlas y recrearlas si hace falta | R-82 |
| Contorno del sticker en inglete y con sombra | Contorno redondo, sin sombra | R-84 |
| Textos pegados al borde de cajas y pastillas | Aire interior siempre | R-65 |
| Logo en slides intermedias de LinkedIn | Sólo en la portada y el cierre | R-64 |
| Imágenes web en la ficha de Linderos | Los renders oficiales que mandó | R-68 |

## 8. Datos que se confirman con Scarlette antes de publicar

En octubre quedaron abiertos:
- fechas de stories;
- 2025 vs 2028 para los 49 activos;
- la URL de postulación de terrenos;
- «MAY. 2027»;
- la dirección de Linderos;
- las sedes de Halloween;
- el número de KLAB (5885 vs 5855).

Cada mes hay datos así (números, direcciones, fechas, URL). Se listan al entregar y **no se inventan**: si el brief
dice «XXX», queda «XXX» marcado.
