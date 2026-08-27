---
name: between-sistema-grilla
description: "✅ BETWEEN (Hilton) — grilla sept REHECHA y publicada 27-08 tras 2 rechazos. Causa raíz: Brushwell no cargaba en Chrome. Gramática corregida (titular 117 ExtraBold, script 1,0× ARRIBA). Las cifras válidas están en clients/hilton/CLAUDE.md"
metadata:
  node_type: memory
  type: project
  originSessionId: c9861545-183e-4e37-8eb2-5fc2400e2f48
---

---

# 🔴 LEER PRIMERO — corrección del 27-08-2026

**Buena parte de las cifras que están MÁS ABAJO en esta memoria quedaron OBSOLETAS.**
Si abajo lees «titular 97», «script 186», «relación 1,92 ×» o «las dos líneas se
solapan»: **está mal**. Eso produjo la segunda grilla rechazada.

**Las cifras válidas viven en `clients/hilton/CLAUDE.md` § LA GRAMÁTICA MEDIDA
(corregida 27-08-2026).** Esa es la única fuente. Resumen:

| | Correcto |
|---|---|
| Titular | Raleway **ExtraBold 800**, **117 px**, tracking −0,024em |
| Script | Brushwell **≈123 px**, tracking +0,036em, **ARRIBA y más chica** |
| Relación script/caps | **≈ 1,0 ×** (antes decía 1,92 ×) |
| Aire script→titular | **9 px de tinta** (antes decía «se solapan») |
| Caja taupe | alto **66**, padX **54**, radio **16**, texto ExtraBold 45 |
| Alineación | **centrada** (antes decía izquierda x=114) |
| Entrega | **2250 px** de ancho |

**Y la causa raíz de todo:** Chrome rechazaba `Brushwell.otf` y las piezas salían
con una serif de reemplazo, en silencio → [[brushwell-no-cargaba-en-chrome]].

**Lo otro que faltaba:** el repertorio de composición de la marca (flechas con
etiqueta, pila en esquina, composición partida) →
[[between-repertorio-composicion]].

## Estado al 27-08-2026

- 27 piezas rehechas a 2250 px en `out/hilton-between-sept-v3/`.
- Publicadas en https://portal-hilton.vercel.app/between-revision.html
- Valeria las aprobó visualmente («lo veo mucho mejor») y las mandó a revisión con
  la diseñadora de la cuenta.
- **Feedback de Elisabet (28-08) — 4 puntos, todos resueltos:**
  1. `BW-S-HumorToGo`: el titular caía sobre la cara de la modelo (medido: cara en
     y 620–720, texto en 600–700). La foto es 9:16 completa, así que no había margen
     para bajarla: se **regeneró el montaje** pidiendo el tercio superior vacío.
  2. `BW-S-Strudel`: la caja del texto tapaba el logo → se achicó a 760 de ancho y
     bajó a y 432.
  3. `BW-F-ToGo-1` (portada): el bloque tapaba la cara → `topBloque={470}`.
  4. `BW-F-ToGo-2`: **el vaso To Go era el ANTIGUO.** Hay dos vasos y el banco
     graduado tiene el viejo en 5 fotos → ver `clients/hilton/CLAUDE.md`
     § EL VASO TO GO. Se reemplazaron las fotos por reales de la sesión
     25-jul-2025, que sí trae el vigente.
- Pendientes que yo mismo marqué: la composición partida de `BW-S-ToGoDulce` no
  logra el efecto «Good Morning» (la costura no se lee); los montajes de personas
  son IA porque no existen las fotos reales (portada To Go, manos del cumpleaños);
  la caja de emergencia quedó blanda.

---

Sistema de diseño BETWEEN Coffee & Bar (marca del complejo [[hilton-cliente-4-marcas]]) para producir la grilla mensual en Remotion.

## Dónde vive la verdad

**No duplicar valores acá.** El feedback escrito de Eli (24-08-2026) quedó codificado en:
- `src/brand/hilton-between.ts` — colores, escala tipográfica, pesos, tamaños de logo, formatos.
- `src/compositions/hilton/BetweenSistema.tsx` — plantillas y componentes (`PiezaFeed`, `PiezaStory`, `PiezaPaid` 1080×1080, `StoryAnimada`, `CTA`, `Legal`, `TituloMixto`).
- **`clients/hilton/CLAUDE.md` § Brand kit BETWEEN** — el porqué y las reglas de trato con el cliente (las de Javier: vaso To Go con tapa negra, café nunca canela, vapor solo en invierno, no enfocar trabajadores en estáticos, máximo 2 familias tipográficas, títulos sin punto final).

Entry point propio: `npx remotion still src/BetweenEntry.tsx <id> <out>` — rinde todo Between sin depender de Root.tsx. Sandbox de render fuera de iCloud: `~/copylab-work/between-render/` (espejo del código + assets; sincronizar tras cada cambio).

## Tipografía — RESUELTO

**Brushwell.otf** (381 glifos, v1.000) instalada; el provisional se fue. Trae tildes, Ñ, números y `!` `?`, y **le faltan solo `¡` y `¿`** — resueltos con la técnica de Eli: girar 180° el `!` y el `?` (helper `signosVolteados` dentro del componente `Script`, automático).

Verificar fuentes **renderizando** (Ñ, tildes, signos, números), no confiando en el nombre: "Brushwell" suena a brush pero es una script elegante de alto contraste.

⚠️ **Legal:** la **Cherolina** que Eli dejó en el Drive es una **demo de uso personal** (Almarkhatype Studio) — no sirve para piezas de cliente sin licencia corporativa. No hace falta: era solo para darle Ñ a Kallimata (91 glifos, sin tildes ni números), y Brushwell ya la trae.

## Logo — el error que más se notaba

Eli daba "262 px" y yo lo leí como **alto**, poniendo 150 px: casi el doble de su máximo real. **El 262 es ANCHO.** Medidas confirmadas por dos fuentes independientes (su texto + la medición PIL de sus plantillas): post máx **262,90 × 86,77**, historia máx **281,57 × 92,93**; mínimos 162,42 × 53,61 y 196,68 × 64,92. Se escala **por ancho** y el alto sale del ratio, para que nunca se vea achatado. Va centrado y con margen, con dos plantillas por formato (arriba/abajo) en `BETWEEN.margenes`.

## Estado

- **Ronda 1 (13 piezas) fue rechazada por Valeria** — el sistema servía, la fidelidad no. De ahí salió el cuestionario a Eli.
- **Ronda 3 publicada 26-08** (Brushwell real + signos + logo corregido): https://portal-hilton.vercel.app/between-revision.html (archivo en `~/copylab-work/portal-hilton/between-revision.html`, deploy `npx vercel --prod --yes`). Muestra qué cambió, qué falta y las 13 piezas.
- **Los links de claude.ai/code/artifact NO sirven para terceros** (dan "Página no encontrada"): para compartir con Eli o el cliente, siempre el portal en Vercel.

## Material de Eli — YA DESCARGADO (25-08)

Todo salió de la carpeta **GRILLA IA BETWEEN** `10Wyq-JrVAwkIItMUJH2De6wuxTiBDuDh` del Drive de Eli, bajado con `scripts/hilton-drive-pull.sh <folder-id> <destino>` (usa el visor público, sin auth; **no cortar su salida con `head` — SIGPIPE mata la descarga a medias**). El conector de claude.ai se cayó y volvió solo; el token del monorepo (`drive.file`) nunca sirve para archivos ajenos.

En `raw/hilton/between/`:
- `globos/` — su .ai + .svg de **Flechas y trazados, globos BETWEEN**.
- `espacios/` (12) — terraza e interior reales, para fidelidad de los montajes.
- `desayunos-ago2026-drive/` (28) — sesión cruda de agosto.
- `ediciones-ia-eli/` (42) — **sus propias ediciones con IA**: la mejor referencia de su técnica.
- `modelos-25jul2025/` — sesión más actual con personas (353 archivos; descarga larga).
- `platos-3enero/` — pendiente de bajar (202).

**Ilustraciones extraídas y en producción:** el SVG se renderizó con Chrome headless a 2× con fondo transparente y se recortaron los 8 elementos **midiendo el canal alfa** (bandas de columnas/filas con hueco mínimo). Quedaron en `public/assets/hilton/between/recursos/`: `globo`, `globo-alt`, `globos-par`, `confeti`, `corazon`, `flecha-bucle`, `flecha-grande`, `flecha-circulo`. Se usan con `<Ilustra>` y `<Globos>` de `BetweenRecursos.tsx`. Regla de Eli: acompañan, no dominan (~20% de las historias).

## ⛔ Las 6 reglas de Eli que se me pasaron (25-08) — no repetir

Valeria rechazó la primera versión de la grilla: «no están bien las tipografías, jerarquías, está rara». Al auditar contra el feedback completo aparecieron seis incumplimientos. **Todos están ahora codificados en el sistema, pero conviene revisarlos en cada entrega:**

1. **Mayúsculas a destajo.** Su regla: título sutil = 40–74 pt **y solo la primera letra en mayúscula**; todo mayúscula es solo para el que debe destacar (~100). Yo tenía TODO en mayúscula. → El componente `Titulo` ahora decide la caja por el tamaño (≥78 → mayúscula).
2. **Piezas saturadas.** Ella: «jamás mucho texto o saturado, el respiro es lo ideal, destacar lo que se ve primero». Yo apilaba título + bajada + horario + CTA + legal. → Máximo 3 bloques, un solo protagonista.
3. **Parecían 3 familias.** Javier reclama por «muchas tipografías diferentes aunque sean de la misma familia; acepta 2». Caps + script + regular + caps con tracking + itálica se leía como cinco estilos.
4. **Tracking fijo.** El tracking 5–10 es **solo si hace falta** compensar jerarquía, y solo para horarios. Yo lo tenía por defecto y aplicado a precios y nombres de producto. → `Dato` con `espaciado` opcional (apagado por defecto).
5. **Logo repetido.** «Cuando hay fotos con vasos To Go con el logo… se omite el uso». Iba el logo arriba en 9 piezas donde el vaso ya lo traía. → `conLogo={false}` en todas esas.
6. **Brushwell en frases largas.** Es para títulos o **acompañamiento de una palabra clave**, no frases completas de apoyo.

Además: el multiply va «lo menos notable posible» (bajado a 0,30–0,36) y el texto **no debe atravesar ni tapar rostros u ojos**.

## Grilla septiembre 2026 — ENTREGADA (25-08)

**27 piezas rendidas** (16 feed + 11 historias) en `out/hilton-between-sept/` y en el sandbox. Página de entrega: https://portal-hilton.vercel.app/between-revision.html

El brief salió del xlsx del Drive (`1wNF6qLil9qMFCGgXPlVqHBQcabfmCWWY`, bajado con `curl "https://drive.google.com/uc?export=download&id=..."` y leído con openpyxl; **ojo con las celdas combinadas** — usar `get_column_letter`, no `cell.column_letter`). Textos literales, hoja FEED fila 11 = diseño, 13 = copy; hoja STORIES fila 10 = diseño, 12 = interacción; fila 16 = estado.

**Fotos:** la sesión **modelos 25-jul-2025** trae los **vasos To Go reales de cartón con tapa negra y logo** — se usan esas en vez de IA (Javier pide fotos reales). Espacios del local para cowork. Los desayunos de agosto se gradaron con un script (baja altas quemadas, levanta sombras, calidez, +3% contraste) → `raw/hilton/between/desayunos-gradados/`. Solo se generó con IA lo que no existe en el banco: Strudel (4 ingredientes), Plateada, milkshake, torta empezada y las dos tazas.

**Componentes nuevos** en `BetweenRecursos.tsx`: `Cuadrantes` (composición editorial en 4), `Etiqueta` (texto anclado sobre la foto) y `StickerQuiz` (encuesta de Instagram).

**Fuera a propósito** (por su estado en la grilla): reel Café Bombón (EN REVISIÓN), «Así se hace tu café» (POR GRABAR), promociones de desayuno feed y story (PENDIENTE POR CLIENTE).

**Faltan 3 fotos que el brief pide y no existen:** persona saliendo con el To Go en mano, las dos manos entregando el café de cumpleaños, y la mesa con calculadora. Van con sustituta hasta que las saquen.

**How to apply:** al retomar, primero revisar si llegó Brushwell; si llegó, dejarlo en `public/assets/hilton/between/fonts/Brushwell.otf`, sincronizar al sandbox, rendir y republicar la misma página del portal. Después: fotos reales por brief, piezas EN REVISIÓN/PENDIENTE POR CLIENTE, y replicar el sistema para QB y P18. Ver [[between-cumple-tecnica-eli]], [[paid-media-zonas-seguras]] y [[ctas-verbatim-del-brief]].


## Ronda 3 — feedback escrito de Eli (25-08-2026), todo codificado

**Scripts, cobertura verificada con fontTools:** Cherolina es **la única completa**
(345 glifos: Ñ ñ ¿ ¡ tildes). **Brushwell** (382) es la principal pero **le falta el `¡`**.
Kallimata original (88 glifos) casi no sirve para español; Kallimata-ES (95) tiene ñ y
tildes pero no Ñ mayúscula ni ¿.

⭐ **El truco de Eli:** para `¡` y `¿` usa el signo de cierre **rotado 180°** — calza
porque las fuentes están bien construidas. Codificado en `volteaApertura(texto)`, más
`scriptSirve(texto, script)` para saber antes de renderizar. En `src/brand/hilton-between.ts`.

⚠️ **Cherolina es DEMO «personal use only»** (Almarkhatype). Para cliente hay que
comprar licencia. Cherolina además es **más fina y monolineal** que Brushwell: hay que
**abrir el tracking**.

**Logo, cifras exactas de Eli** — ratio constante **3,02980** (el kit tenía 3,02778, mal):
story mín 196,6809×64,9154 / máx 281,5732×92,9345 · post mín 162,4194×53,6072 /
máx 262,9032×86,7724. Guiarse del **alto**; nunca achatado.

**Fotos — reglas duras:**
- ⛔ **La taza blanca dice KIMBO y tiene una raya negra: SIEMPRE borrar el logo.** La
  taza actual es blanca total. Es la corrección más frecuente.
- ⛔ **Sesión julio 2023: los rostros NO se publican** — hay personas sin derechos de
  imagen. Sirve de referencia; si hace falta gente, se genera un rostro de perfil
  chileno. El original jamás sale reconocible.
- ⭐ **Sesión 25-jul-2025 (modelos)** es la más actualizada: primera opción.
- **Sesión agosto 2026** viene cruda: mejorar encuadre/luz/color, **reemplazar el fondo
  por un ambiente REAL de Between**, borrar luces de flash y brillos de mesa, nada
  quemado, comida apetitosa, **conservando desayuno y plato**.

**Ilustraciones:** globos, flechas y trazados en
`public/assets/hilton/between/ilustraciones/flechas-trazados-globos.svg`
(1.811 paths + 178 polígonos, 48 grupos). **No se dibujan a mano ni con IA: ya existen.**

**Márgenes:** ningún texto sobre caras ni ojos; nada fuera de los límites del formato.

### ✅ Cherolina NO hace falta (25-08-2026)
**Brushwell tiene `Ñ ñ ¿` y todas las tildes; lo único que le falta es el `¡`** — que es
justo lo que resuelve el truco de Eli. Renderizado y comprobado: `¿Un café? ¡Mañana!`
sale perfecto con los signos volteados. **Brushwell + `volteaApertura()` = 100 % de
español**, sin comprar nada y sin cambiar el look.

⚠️ **Cherolina no está en Adobe Fonts** — la suscripción de CC no la cubre (verificado:
en el Mac de Valeria las únicas Adobe Fonts activas son las 20 de IvyOra). El archivo
del Drive es DEMO «personal use only» de Almarkhatype. Queda de respaldo, no de necesidad.

**Allura y Great Vibes** (libres, completas) NO son sustitutas estilísticas: son
caligrafía formal de alto contraste, no pincel casual. Cambian la voz de la marca.

⚠️ **Las fuentes de Adobe Fonts no se copian al repo.** Están en
`~/Library/Application Support/Adobe/CoreSync/plugins/livetype/` con nombres ofuscados
y se pueden leer, pero la licencia es por asiento: se usan en la máquina, no se
redistribuyen. Cada diseñador las activa en su propio CC.

---

# ⛔⛔ RONDA 4 — la grilla de septiembre se rechazó ENTERA (26-08-2026)

«no hemos logrado diseñar bien con between, te he dado todo el feedback, acceso a
editables, a drive, a la cuenta, y aún así no logras llegar, cambias tipografías,
estilos básicos… todo mal.»

**La causa raíz, y es la lección de toda esta memoria:** codifiqué al pie de la letra
todo lo que Eli dio **medido** (px del logo, ratio 3,0298, cobertura de glifos, márgenes)
y **estimé** todo lo que dio **descrito**. El kit decía «titular rango 40–122» y me senté
en la mitad (56–70) cuando la marca vive en el techo (**97**). No fue falta de acceso —
el acceso estaba desde el 25-08.

## Lo que faltaba: MEDIR LAS PIEZAS PUBLICADAS, no solo el brief

Las piezas terminadas de Eli estaban en el Drive todo este tiempo, en la carpeta
`Grillas fotos` (`1Iq_eArneiCfsDZXlDjVQxtua-JiyA_j_`), **dentro de la misma carpeta
compartida por link** de la que ya había bajado las fotos. 19 PNG a 2250×2813 y
2250×4000. Se bajan con `scripts/hilton-drive-pull.sh`. Ahora en
`raw/hilton/between-adn/ref-piezas/`.

> **Regla general para cualquier marca:** las *entregas terminadas* del diseñador son
> mejor fuente que el brief y que los `.ai` (que pesan 500–700 MB y no se pueden abrir).
> Buscarlas en las carpetas de entrega semanal `S1/S2/S4 <MARCA> <MES>/<SIGLA>/`.

## Las cifras medidas — están en `clients/hilton/CLAUDE.md § LA GRAMÁTICA MEDIDA`

Titular Raleway **Black 97** (tracking −2) · script Brushwell **186** (tracking +1) ·
relación script/caps **1,92×** (no 1,2) · las dos líneas **se solapan** (tinta a 1–2 px,
no gap de 22) · caja taupe `#675b49` opaca **74 alto / padX 29 / gap 10** con texto
Raleway **Light 45** · texto en arco al pie **51** · bloque anclado **arriba** y
**alineado a la izquierda** en x=114 · el titular ocupa **55–80 %** del ancho.

**La escala del texto es absoluta, no relativa al formato:** el mismo titular mide igual
en feed 1080×1350 y en story 1080×1920.

## Componentes nuevos (usar estos, no los viejos)

`TitularBetween`, `CajaDato`, `PilaDatos`, `TextoArco`, `PiezaFeedBodegon` al final de
`BetweenSistema.tsx`. ⛔ `BloqueTexto`, `PiezaFeed` y `TituloMixto` son los que
produjeron la grilla rechazada — no usarlos en piezas nuevas.

## Calibrar contra el propio render, no solo contra el cálculo

**Brushwell sale ~20 % más ancha en Chrome que en el cálculo de PIL.** Los valores
finales salieron de renderizar mi pieza, medirla con la misma máscara de color que la de
Eli y corregir hasta que la tinta calzara: titular **447×67** contra **448×71** de ella,
script **625** contra **614**. Prueba A/B lista: `BW-P-MatchPerfecto` en
`src/compositions/hilton/BetweenPrueba.tsx`.

## Pendiente

- [ ] **Tratamiento de foto** — es la única diferencia que queda en el A/B: las de Eli
      son más cálidas, plato claro, encuadre más abierto, multiply casi nulo (≈0,10).
      Los planos generales oscuros con multiply pesado fueron parte del rechazo.
- [ ] Componentes que faltan: **líneas de llamado** (línea fina + punto hacia la foto),
      **marco de esquinas** sobre el producto, **mockups de UI en crema**.
- [ ] **Rehacer las 27 piezas de septiembre 2026** con el sistema medido y republicar
      el portal.

## ✅ Grilla rehecha y QA automatizado (26-08-2026, misma sesión)

Las **27 piezas regeneradas** con la gramática medida → `out/hilton-between-sept-v2/`
y `~/copylab-work/between-sept-v2/`. **24/27 pasan el QA limpias**; las 3 marcadas son
falsos positivos verificados a ojo (globos de cumpleaños, mockup de IG y fotos de
comida tocando el borde a propósito).

**Dos scripts nuevos que hay que correr siempre:**
- `scripts/between-gradar.py` — lleva las fotos a los números de Eli (lum 118, p95 200,
  calidez +55) con rodilla suave en altas: nada quemado, sin flash, comida intacta.
  Salida `public/assets/hilton/between/fotos-gradadas/` — **las piezas usan esa carpeta**.
  Con foto gradada el multiply baja a **0,10–0,16** (antes 0,30 y se veía apagado).
- `scripts/between-qa.py` — mide márgenes, zonas seguras de Meta y que el titular llene
  ≥50 % del ancho (el chequeo que habría cazado el rechazo). Aísla el beige **en forma de
  trazo** y exige borde oscuro cerca, si no un croissant cuenta como letra.

**Defectos que aparecieron al rehacer, todos corregidos EN EL SISTEMA:**
la script se salía del cuadro o se partía en dos líneas → ahora `nowrap` + auto-ajuste
al ancho · el remate del pincel se metía en el margen → se compensa con
`actualBoundingBoxLeft` (la «p» de «perfecto» vuela 39 px a cuerpo 186) · la caja taupe
en `nowrap` se desbordaba con datos largos → también auto-ajusta · el logo de abajo
chocaba con el bloque anclado abajo → **si el bloque baja, el logo sube**, que es
exactamente para lo que Eli tiene dos plantillas por formato.

⚠️ **Ojo con `AbsoluteFill`:** fuerza `inset: 0` y se come un `top` pasado por `style`.
Para una banda posicionada (el strudel) hay que usar un `div` plano.

## ⛔ Portal SIN republicar — `npx vercel --prod --yes` da «Not authorized»

`~/copylab-work/portal-hilton/between-revision.html` **ya está actualizado** con las 27
piezas nuevas y el texto de qué cambió (1,5 MB, imágenes embebidas a 460 px JPEG q72;
el respaldo de la versión anterior es `between-revision.bak.html`). Falta reautenticar
la CLI: `npx vercel login` y volver a desplegar. **El link es el mismo de siempre:**
https://portal-hilton.vercel.app/between-revision.html
