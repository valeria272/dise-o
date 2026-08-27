---
name: traverso-estado-septiembre
description: "Traverso — dónde quedó la grilla de septiembre 2026, qué está listo, qué falta y cómo retomar"
metadata: 
  node_type: memory
  type: project
  originSessionId: 8b4065fd-54fd-46aa-b992-b9f72cce6ffa
  modified: 2026-08-19T17:54:43.442Z
---

# Traverso · estado de la grilla de septiembre (al 19-08-2026)

Trabajo en curso para @traversochile. Contexto de marca y reglas: [[traverso-brand]].

## Dónde vive todo
`EDITOR VIDEOS/raw/traverso/`
- `PLAN-SEPTIEMBRE.md` — **el documento maestro**: 4 capas, calendario día a día, campaña de feria en 3 fases, pendientes
- `GRILLA-SEPTIEMBRE.md` — inventario de piezas con copys y guiones de reels
- `FEED-MOCKUP-SEPTIEMBRE.png` — mockup de las 24 publicaciones (▶ marca las 11 en video)
- `brandbook_traverso.pdf` — manual oficial (De Bianchi ADV)
- `grilla-septiembre/` — 16 piezas v1 (más de producto)
- `v2-creativas/` — piezas creativas (corpóreos 21-28), lifestyle/orgánicas (31-35), videos de feed (41-43), feria (44-45) + `reel-limon-alfombra-roja-9x16.mp4`
- `mostaza-kaiju-surf.mp4` — reel corpóreo mostaza inundando Santiago (1:1, falta versión 9:16)

**Plan publicado como artifact:** https://claude.ai/code/artifact/af499107-0947-4404-9ff5-c2649aa9e195 (título "El 18 que nos une"). Para actualizarlo desde otra sesión hay que pasar esa URL como `url`, si no crea uno nuevo.

## ⚠️ Créditos Higgsfield AGOTADOS (19-08, plan Plus mensual) — no se puede generar imagen/video hasta recargar o que renueve el ciclo. Pendientes cuando vuelvan: re-editar stills del carrito quitando el letrero Cristal en la fuente (hoy resuelto por reencuadre), y rehacer el plano de mesa con la botella real de mostaza como única salsa.

## Primer reel ENTREGADO — versión final v5: **`SPOT-TODAS-LAS-MESAS.mp4`** (~29 s · 1080×1920)
Cambios v5 (feedback Vale): (1) **audio de clips MUTEADO** — cada clip de seedance trae su propia música de fondo y el spot sonaba a música distinta por corte; ahora la única banda sonora es la pista continua (regla permanente para reels multi-clip); (2) **máximo 2 risas**: se eliminaron los planos del mordisco y de la fuente de soda; ríen solo obreros y abuela-nieto; (3) **letrero "Cristal" (cerveza) eliminado por reencuadre**: `zoom: 1.32` con `transformOrigin 50% 92%` en el plano del carrito lo deja fuera de cuadro — nunca marcas de terceros en pantalla; (4) **plano de mesa con botellas eliminado** (el envase de ají que generaba no existe en el catálogo); el payoff cae directo en el plano del abrazo sin producto. Secuencia final: carrito (zoom) → fonda → once → obreros (risa 1) → asado padre-hijo → ramada → abuela-nieto (risa 2) → abrazo + payoff → logo.

## Versión v4 anterior (~33 s)
Cambios v4 (feedback Vale 19-08 tarde): (1) **transiciones por fundido encadenado** de 14 frames entre planos (componente `Shot` con crossfade de video+audio) en vez de cortes secos; (2) **packshots reales**: los envases del plano de mesa se generaron con referencias del catálogo real — **traverso.cl corre en Bootic (NO Shopify), las imágenes de producto viven en i.bolder.run** y se scrapean con `grep` del HTML de /collections/<cat>; guardadas en `EDITOR VIDEOS/raw/traverso/packshots/` (+ tira `REFERENCIA-envases-reales.png`). La línea Vintage real = **botellas squeeze de color con etiqueta ornamentada, NO porrones de vidrio**; (3) **cierre en dos tiempos**: mesa con envases reales → plano cerrado del abrazo SIN producto donde cae el payoff — porque Nano Banana, si le pides "2 botellas", igual repuebla la mesa con 5: la solución es un plano final sin envases; (4) expresiones contenidas: "sonrisas con la boca cerrada, a lo más UNA sonrisa amplia".
**Gotcha de render**: los crossfades duplican la decodificación simultánea → `--timeout=300000 --concurrency=4` (con 2 tarda >20 min; sin flag da timeout de delayRender). Para referencias de packshot en Higgsfield: `media_import_url` con la URL de i.bolder.run → `media_id`.

Versión v3 anterior (cortes secos, mesa con envases inventados)
Concepto **"Está en todas las mesas de Chile"**, dieciochero. Estructura de anáfora: cada plano es otra mesa, con el renglón fijo "EN LA MESA" en blanco chico arriba y la mesa concreta en amarillo abajo. 10 planos: carrito nocturno (*de las tres de la mañana*) → mordisco del completo → fonda de anticuchos (*de la fonda*) → once en casa (*de la once*) → obreros en la obra (*de los que madrugan*) → fuente de soda (*de toda la vida*) → asado padre-hijo → ramada con cueca (*del 18*) → abuela y nieto → mesa final con todos los personajes (*Está en todas las mesas de Chile.*) → cierre de marca.
**Clave del registro emocional:** NO todos riendo. Se alternan oficio/concentración (maestro completero, parrillero de fonda), intimidad silenciosa (la once), camaradería (obreros), calidez contenida (padre e hijo) y recién ahí celebración. Los prompts que lo logran dicen explícitamente "SIN risas ni carcajadas, gestos contenidos, nadie posa".
Música: `musica-reel2-folk.mp3` (guitarra acústica) — la cumbia sonaba a jarana y no calzaba con el tono emocional. **Igual hay que licenciar una pista propia.**

Versión v2 descartada: **`SPOT-TRAVERSO-NOS-UNE.mp4`** (27,2 s)
Spot en tres actos con 7 planos: (1) carrito nocturno "Don Lucho", el maestro lanza la mostaza · (2) un joven muerde el completo · (3) obreros en la obra se pasan el ají · (4) fuente de soda · (5) el atrape en el asado · (6) abuela y nieto · (7) **reencuentro: todos los personajes anteriores en la misma mesa**, brindando. Copy en cuatro tiempos: *"Acá la salsa no se pide." → "Se pasa." → "De mano en mano." → "Hasta que nos junta."* y cierre con el eslogan.
El truco de continuidad: pasarle a nano_banana_pro los stills de cada personaje como `medias` role `image` al generar la mesa final — reconoce y reúne a las mismas personas.

Versión anterior descartada (`REEL-PASAMELA-TRAVERSO.mp4`, 16,8 s) — concepto **"Pásame la Traverso"**: la botella viaja por Chile en match cuts entre gente real (carrito de completos nocturno → atrape en un asado → fuente de soda → abuela y nieto → brindis cenital en mesa larga). Copy en dos tiempos: *"Acá la salsa no se pide." / "Se pasa."* y cierre con el eslogan oficial.
- Composición Remotion: `src/compositions/TraversoPasamelaReel.tsx`, registrada en Root como `TraversoPasamelaReel`. Render: `npx remotion render TraversoPasamelaReel <salida>.mp4`
- Clips fuente en `public/assets/traverso/reel/` (01 a 05), stills en `EDITOR VIDEOS/raw/traverso/reel-pasamela/`
- **Logos oficiales extraídos del brandbook** a `public/assets/traverso/`: `logo.png` (color, fondo blanco) y `logo-blanco.png` (versión 1 color con transparencia, la que se usa sobre azul). Se sacaron con PyMuPDF de las páginas 3 y 8 del PDF
- Música: prestada de Abakos (`musica.mp3`) — **hay que reemplazarla por una licenciada** antes de publicar
- Receta que funcionó para el realismo: "fotografía documental cinematográfica, cámara en mano, grano de película 35 mm, luz natural/práctica, piel con poros y sudor, nadie posa, NADA de estética 3D ni brillo publicitario"
- Ojo: Nano Banana a veces devuelve el 9:16 con el contenido **rotado**; se arregla exigiendo "FOTOGRAFÍA VERTICAL EN RETRATO, el cielo arriba, personas de pie rectas"

### Correcciones de Vale al v1 del reel (19-08) — reglas que valen para todo
1. **Escala de producto**: la IA agranda los envases hasta volverlos lo más grande de la mesa. Hay que exigir en el prompt "TAMAÑO REAL, unos 20 cm, más bajas que una botella de bebida y apenas más altas que un vaso, proporcionadas a platos y manos; NUNCA agrandar"
2. **No modificar el producto**: ni tamaño, ni lógica, ni textos, ni colores, ni branding. En el prompt: "sin inventar textos, sellos ni claims"
3. **Los personajes deben conectar**: no viñetas sueltas. Es un **relato de spot de TV** con arco — presentación, viaje y reencuentro, donde los personajes de cada escena convergen en la mesa final. Se logra pasando los stills previos como `medias` con role `image` a nano_banana_pro (acepta varias referencias), y funciona muy bien
4. **Más largo**: el v1 de 16 s quedó corto; el formato correcto es ~30 s de spot

## Qué está resuelto
- Concepto del mes: **"EL 18 QUE NOS UNE"** (del eslogan oficial)
- Calendario completo de las 24 publicaciones, 4 semanas con eje cada una
- Feria confirmada y calendarizada (29 sept–1 oct, Espacio Riesco)
- Mix de video subido a 11/24 con 3 videos orgánicos en el feed
- Regla de ritmo del feed: **nunca 2 gráficas IA juntas**

## Qué falta (en orden de urgencia)
1. **Agendar la jornada de content creation** — idealmente 1ª semana de septiembre; de ahí sale el material real de 7 publicaciones (V1-V3 + O1-O4). Hoy son referencias de estilo generadas con IA
2. **N° de stand** en Espacio Riesco (fechas y recinto ya confirmados)
3. **Packshots reales** → dejar en `EDITOR VIDEOS/raw/traverso/packshots/` para la pasada de fidelidad, que corrige de una vez packaging + logo bandera + titulares en Optima
4. **Confirmar cara visible/chef** antes del 23 de septiembre (de eso depende R4)
5. Animar reels que faltan: R3 (ketchup piquero) y versión 9:16 del kaiju de mostaza

## Aprendizajes de producción que conviene no repetir
- Vale pidió explícitamente **más realismo**: los prompts que funcionan dicen "grabado con celular, luz natural imperfecta, grano, sin brillo publicitario" y captions en minúsculas tipo sticker de TikTok. Las piezas 41-43 y 45 son el estándar a seguir
- Al descargar de Higgsfield: **no armar la URL a mano** — los IDs se truncan y da 404. Sacar `rawUrl` de `job_status`/`jobs_wait`. Tampoco usar `&` para paralelizar curls en un solo Bash (rompe el flujo)
- El ffmpeg que trae Remotion (`node_modules/@remotion/compositor-darwin-arm64/ffmpeg`) **no tiene los filtros `tile`, `hstack` ni `vstack`**, y falla si se invoca desde otro directorio (busca sus dylib). Para montar mockups usar Pillow con `/Users/Vale/copylab-venv/bin/python3`
- PyMuPDF (`fitz`) está en el venv compartido y sirve para rasterizar PDFs que no tienen texto embebido
