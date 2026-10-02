# MYZOO — bitácora

> Una entrada por jornada, la más nueva arriba. Lo de hoy se escribe hoy: el
> relevo de mañana lee esto antes de abrir cualquier archivo.

## 2026-10-02 — Paulina Bustamante (con Claude) · paid Fase 3, fondos de los 6 estáticos

**Qué se hizo:**
- **Cambio de método, propuesto por Paulina:** se dejó de pelear escena y envases a la vez. Se generaron **todos los fondos sin producto**, con el animal cerca y mirando a cámara; el producto entra después.
- Fondos de P01, P02, P07, P08, P09 y P10 (6 estáticos). Paulina: «muy buenas, muy realistas y acorde a los key visual de la fase 1 y fase 2».
- Ronda 2, por tres comentarios suyos en Drive (respondidos y resueltos): P01 más cálida (escena nueva), P07 manta caramelo y P08 sofá caramelo (misma foto, una pasada de edición).
- `/al-dia`: las 4 solicitudes de la grilla de octubre pasaron a «Por diseñar» (Story 1 Cyber Mercado Libre para el **lunes 5-10**, Story 2 Cyber 9-10, post «Perro promedio en Chile», 2 portadas de destacadas). No se tocaron hoy.

**Dónde quedó:**
- Drive `MYZOO/IMÁGENES FONDO FASE 3` (`1IL9OZal_kTHoDS3m0QICoWwDroDeie7l`): las 6 vigentes en la raíz, el resto en `otras tomas` y `ronda 2 · alternativas`.
- Fuentes vigentes versionadas en `public/assets/myzoo/fase3/fondos/` (2048 px). Todas las tomas en `raw/myzoo/fase3/fondos/` (no viaja). Generador: `scripts/myzoo-f3-fondos.py`. Página de revisión local: `out/myzoo/paid-fase3/fondos/REVISION.html`.

**Qué sigue:**
1. Paulina monta texto y logos en Illustrator sobre los fondos y **muestra cómo lo hizo**, para que sirva de referencia en los próximos encargos.
2. Producto sobre los fondos de P01, P02, P09 y P10 (por definir con ella si lo pone ella o se integra con IA).
3. Los 4 reels (03 a 06) no tienen nada generado.
4. Story 1 del Cyber, que sale el lunes 5-10.

**Abierto:**
- Los fondos de la ronda 2 no tienen veredicto explícito; Paulina dijo «por ahora con esto estamos ok». No se revisaron con zoom (pelaje, manos).
- El brief pide P09 «sin mascota o muy secundaria», P10 «sin mascota» y P02 «fondo limpio y claro»; se hicieron con el animal protagonista por indicación de Paulina. → avisar a Sebastián Córdova.
- La P01 v7 del 01-10 quedó superada por este método; `IMÁGENES APROBADAS FASE 3` sigue con la P01 del 30-09.
- Las 4 solicitudes nuevas de la grilla vienen sin fecha, sin copy y sin «ok» del cliente al texto. → Nicolás.

## 2026-10-01 — Paulina Bustamante (con Claude) · post 20/10 Parque Pet

**Qué se hizo:** el cliente rechazó la imagen del post del 20/10 («se ve muy falso, muuuy IA») y pidió que pareciera el Parque Pet. Se rehízo la imagen limpia desde cero y, tras 6 rondas con Paulina, quedó **aprobada por ella**: los dos perros de pie al centro, carpas sin marca alrededor, tutores con perros y el cerro San Cristóbal.

**Dónde quedó:**
- Local: `out/myzoo/octubre-2026/20_parquepet/` (`…perros-de-pie_2250x2813.png` y `…_ALTA_3536x4421.png`; las versiones descartadas en `_descartadas/`; historial en `ENTREGA.md`).
- Drive: `MATERIAL DISEÑO PAULINA/MYZOO/5-en-revision/2026-10_octubre/20_post-parquepet_imagen-limpia_01-10` (`1GOh8v-eBwxmlMAR3eXIUcAVlrJ6vrGIt`).
- Scripts: `myzoo-parquepet-depie.py` → `myzoo-parquepet-depie-fondo.py` (y `myzoo-parquepet-stand.py`, de la versión con stand que se descartó). `magnific.py`: el escalador de precisión ya no «falla» cuando marca COMPLETED antes de entregar la imagen.

**Qué sigue:** Paulina monta logos, titular y píldoras sobre la imagen y la pieza va al cliente.

**Abierto:**
- ⚠️ Las fuentes del render están en `raw/myzoo/2026-10_parquepet/` (no viaja en git). Para que sea reproducible hay que pasar a `public/assets/myzoo/` las que usan los scripts (`v4/s_b_2x.png`, `t0_e`, `t1_c`, `t2_d`, `bg_a`) antes del commit.
- Nada de esto está commiteado todavía.

## 2026-10-01 — Paulina Bustamante (con Claude) · paid Fase 3, P01 rehecha desde cero

**Qué se hizo:**
- **La P01 aprobada ayer se reabrió.** Al componer el texto en Illustrator, Paulina vio que la imagen no dejaba espacio: pidió más aire arriba y los envases en una **columna recta** (cada uno ladeado como en la aprobada, sin montarse ni tocarse), pegada a la izquierda, con el perro de protagonista.
- Costó **siete versiones**. Tres rondas se fueron en entender «más alineadas verticalmente» (se leyó como envases derechos, después como montados). Las tres siguientes fueron retoques sobre la imagen de ayer, y cada pasada la dejó más artificial: packs «como render», perro «plano», y al final «todo se ve muy IA».
- Paulina avisó que **la clienta está reclamando que las imágenes se ven IA** y pidió rehacer todo, hiperrealista.
- **v7: escena nueva desde cero**, en una sola generación pedida como foto de cámara real (mesa vacía, golden entero mirando a cámara, alfombra crema, aire arriba). Los envases se pusieron con un boceto de los packshots reales en la posición aprobada, una pasada de integración sólo para volumen y sombra, y la etiqueta real calzada encima.

**Dónde quedó:**
- Entrega local: `out/myzoo/paid-fase3/imagen-limpia/MYZOO_P01_imagen_v7_nueva-desde-cero_{2048,1080}.png`. **Paulina todavía no da su veredicto sobre la v7.**
- Fuentes versionadas en `public/assets/myzoo/fase3/p01v7_*` (ver `LEEME.md`; se reproduce byte a byte). Script nuevo: `scripts/myzoo-f3-grano.py`.
- **Nada subido a Drive.** La carpeta `IMÁGENES APROBADAS FASE 3` sigue con la P01 del 30-09, que ya no es la vigente.
- Pruebas descartadas en `raw/myzoo/fase3/escenas/` (`p01C`…`p02A`), no viajan.

**Qué sigue:**
1. Veredicto de Paulina sobre la v7. Si sirve: escalar a 4096 con `escalar --precision`, volver a calzar a 4K y **reemplazar** la imagen de `IMÁGENES APROBADAS FASE 3`.
2. Con la P01 compuesta por Paulina como referencia, las imágenes limpias de 02, 08, 09 y 10 — **con el método nuevo desde el principio** (manual §2c).
3. La P07 sigue sin revisar, y es de la tanda vieja: lo más probable es que haya que rehacerla con el mismo criterio de realismo.

**Abierto:**
- En la v7 los envases quedaron más chicos respecto del perro y hay madera libre entre la columna y el perro (la mesa llega a la mitad del cuadro). → Paulina.
- ¿Qué envase de Pet Wipes está vigente, «Todo Uso» o «Uso Frecuente»? Sigue sin respuesta. → Paulina / Coni.
- Del Drive (minuta y reunión del 30-09): la web y el plan de medios de Fase 3 parten cerca del **5 de octubre**; el reparto de los $800.000 sigue en discusión. Pedidos de diseño nuevos: story de Huellas Fest (24-10, Lampa; falta dirección y horario, Exequiel), portadas de destacadas de eventos, post de concurso Guau Fest. La grilla de noviembre se modificó el 30-09 y no se leyó.
- El escalador creativo de Magnific (`escalar` sin `--precision`) devolvió «image is required» con un recorte de 1268×2048. No se investigó.

## 2026-09-30 — Paulina Bustamante (con Claude)

**Qué se hizo:**
- **Recorrido completo del Drive de la agencia** (`AGENCIA COPYWRITERS/MYZOO`, 15 carpetas) → mapa en `DRIVE-AGENCIA.md`. Se leyó por primera vez el `Manual_Identidad-MyZoo-03`: Roboto es la corporativa y hay una paleta secundaria.
- Paulina confirmó que ella diseña MyZoo en digital (grilla básica y paid).
- **Paid Fase 3, P01 (Pet Wipes desde $2.990):** la imagen limpia quedó **aprobada por Paulina** tras 5 rondas. Es una vista cenital cálida: golden en la alfombra, mesa de roble, los tres Pet Wipes acostados con espacio para los precios y franjas libres arriba y abajo. Se entregó en 4096 px.
- La P07 (tip piel sensible) tiene imagen limpia, sin revisión todavía.

**Dónde quedó:**
- Aprobada en Drive `MYZOO/IMÁGENES APROBADAS FASE 3` (`173IB55J4Ne8CpLL3MJ8G7kN3U7rvsAfy`), en 4096×4096 PNG.
- Local: `out/myzoo/paid-fase3/imagen-limpia/`.
- Fuentes del render en `public/assets/myzoo/fase3/` (ver `LEEME.md`, se reproduce con un comando).
- Scripts: `scripts/myzoo-f3-recortar.py` (packshots sobre blanco → PNG con transparencia) y `scripts/myzoo-f3-calzar.py`. Este último calza el packshot real sobre el envase generado con SIFT + homografía, con opciones de luz, recorte y limpieza.
- Paulina deja material en `MYZOO/PACKSHOTS FASE 3 (para Claude)` (`1g5slxhZzSrwKk_aRg-aTmz7M49hDOcWC`).

**Qué sigue:**
1. Paulina compone texto y logo de la P01 en Illustrator y la devuelve a la carpeta PACKSHOTS FASE 3.
2. Con esa pieza como referencia de composición, generar las imágenes limpias de las piezas 02, 08, 09 y 10, y después ver reels (03–06) y stories.
3. Revisar la P07 con Paulina: le falta el producto y las franjas libres.

**Abierto:**
- **¿Qué envase de Pet Wipes está vigente?** Los packshots de Paulina dicen «Todo Uso»; el arte de Coni (`WIPES`, abril) y el brief dicen «Uso Frecuente». → Paulina / Coni.
- Brief Fase 3 sin links de material y con entrega vencida (29-09). → Sebastián Córdova.
- Magnific devolvió «Error consuming credits» de forma intermitente (Seedream y Nano Banana), aunque la cuenta tiene más de un millón de créditos. → avisar a Valeria si se repite.
- En la P01 aprobada asoma un borde oscuro en el costado izquierdo del envase azul. Paulina la aprobó igual; queda limpiarlo si lo pide.

## 2026-09-22 — Paulina Bustamante

**Qué se hizo:** El día partió con un encargo de Valeria —revisar cuatro estáticos
de octubre que ella generó— y **ese material nunca llegó**: no hay ningún commit de
MyZoo en las 6 ramas del remoto, ni piezas nuevas en Drive. Se decidió **rehacer los
cuatro desde cero**. Antes de producir se levantó lo que faltaba:

1. **Apareció el sistema gráfico de la marca**, que el manual daba por inexistente.
   Estaba en Drive, en `MYZOO/Compartido/BRANDING MY ZOO NCG.pdf` — documento del
   cliente. De ahí salen las **dos tipografías** (Neutraface 2 corporativa + Roboto
   complementaria) y la **paleta con sus HEX exactos**. Resolvió dos pendientes que
   el manual arrastraba desde agosto.
2. **Se midió la gramática digital** sobre las **118 piezas** que Paulina entregó de
   julio a septiembre. Resultado en `CLAUDE.md` §2-ter: el feed **no es 1080×1350
   sino 2250×2813**, el logo arranca a **145 px exactos** (7 de 7 piezas), la paleta
   oficial se usa a distancia 0, y la marca tiene **cuatro registros**, no una
   plantilla.
3. **Se produjeron las cuatro piezas** con esa gramática.

**Dónde quedó:**
- Las cuatro en `out/myzoo/octubre-2026/` y subidas a Drive →
  `MATERIAL DISEÑO PAULINA/MYZOO/5-en-revision/2026-10_octubre/v1-rehechas-22-09`
  (`14mcaXyu7wTFWWxAk-p8Ie85e_opOg88e`).
- Generador: **`scripts/myzoo-octubre.py`** — los textos viven arriba del archivo,
  corregir una pieza es cambiar una línea y volver a correr.
- Fondos y assets recortados versionados en `public/assets/myzoo/` (excepción
  declarada en `.gitignore`: Magnific no es determinista y sin ellos no se
  reproduce la entrega).
- Material de referencia en `raw/myzoo/` (118 piezas, 1,4 GB, **no viaja**) y
  respaldado entero en Drive.
- **QA pasado:** formato correcto y círculo del logo a 145 px, centrado, en las 4.

**Qué sigue:** las tres correcciones que quedaron identificadas y **sin aplicar**:
1. **Mercado Libre** comunica el partner sólo en la pastilla. En la story de agosto
   lo hacía el **mockup del teléfono con la app** — hay que conseguir una captura de
   la tienda MyZoo en Meli y montarla.
2. **Repelente:** la última línea del bloque verde queda con «salir.» sola.
3. **PREGUNTAZOO:** la bajada quedó en Bold por el defecto de fuente; con Book se
   vería como corresponde.

**Abierto:**
- ⛔ **Los archivos de Neutraface Text Book y Demi están defectuosos** (§ del manual):
  dejan un hueco tras cada «í». Todo se compone con Bold y Bold Italic, que están
  sanos, y por eso el cuerpo de texto va más pesado que en las piezas de referencia.
  **Hay que pedir los archivos originales de Book y Demi.**
- Los textos en pantalla los propuso el estudio a partir del copy aprobado por el
  cliente. **Falta que Paulina los valide**; el copy de la grilla no los define.
- El **`Manual_Identidad-MyZoo-03.pdf`** (331 MB) es posterior al branding NCG y no
  se pudo leer: no tiene capa de texto. Si contradice algo, ese manda.
- Hay un **rebranding 2026 en curso** (`MYZOO/Rebranding/`) cuya «nueva paleta» era
  un entregable. Confirmar si salió antes de dar la paleta por cerrada.
- La grilla de octubre tiene **dos hojas visibles casi idénticas** (`Grilla Octubre `
  con espacio y `Grilla Octubre`). El portal lee dos hojas como dos meses distintos:
  avisarle a Nicolás que esconda la que sobra.
- De los 10 estáticos del mes sólo estos 4 estaban «Por diseñar»; **5 de los otros 6
  tienen comentarios del cliente pidiendo cambios de fondo** y no se pueden producir
  hasta que contenido los resuelva.

> ⚠️ **Choque sin resolver (detectado en /abrir del 24-09-2026):** el 22-09 Paulina y Valeria
> (con Claude) hicieron por separado los mismos 4 estáticos de octubre y midieron la gramática
> digital con resultados distintos (Neutraface 2 contra Neutraface Text). Las dos entradas quedan
> abajo tal cual. Decide Paulina, que firma la marca.

## 2026-09-22 — Valeria Traverso (con Claude)

**Qué se hizo:** Se armaron los **4 estáticos de octubre** que estaban en «Por diseñar» y con «ok» del cliente al texto:

| Fecha | Pieza | Columna de la grilla |
|---|---|---|
| 01-10 | Post del repelente, «ROMPER EN CASO DE PASEO» | C |
| 02-10 | Story PREGUNTAZOO | D |
| 05-10 | Post «¡MyZoo llega a todo Chile!» con Mercado Libre | G |
| 08-10 | Post Cruelty Free con Te Protejo | I |

Antes de diseñar se **midió por primera vez la gramática digital** de la marca, sobre 23 piezas publicadas de julio a septiembre (casi todas de Paulina). Quedó en `CLAUDE.md` §2b: Neutraface Text, franja coral #FF6969, exportación a 2250 px de ancho, logo con el claim debajo y el feedback del cliente.

**Dónde quedó:**
- Las piezas están en `out/myzoo/octubre-2026/` y viajan en el repo. La guía del sticker de preguntas está en `_revision/`. Qué es cada pieza y de dónde sale cada texto: `ENTREGA.md`.
- Se rinden con `python3 scripts/myzoo-oct-armar.py`. Las escenas, los packshots y la marca están en `public/assets/myzoo/`, y las fuentes en `public/assets/fonts/myzoo/`.
- Si hay que regenerar una escena, se usa `scripts/myzoo-oct-escenas.py`. Deja el resultado en `raw/`, que no viaja.
- **No se subió nada al Drive ni al portal.**

**Qué sigue:**
1. Paulina revisa las 4 piezas y corrige lo que su criterio diga.
2. Se suben a la carpeta `10. OCTUBRE` con su nomenclatura.
3. Seguir con los estáticos que el cliente vaya pasando a «Por diseñar». Al 22-09, las columnas L, N, Q, S, W e Y siguen «En revisión». Varias traen cambios del cliente en la fila de TEXTO: L (Xtreme-Vet no es para el hogar), N (sumar «pieles sensibles»), S (cómo se sortean las entradas) y W (mostrar los productos nuevos en vez de las wipes). Y trae una idea para ampliar la pieza, no un cambio: un carrusel con más slides.

**Abierto:**
- **Sello PREGUNTAZOO:** no existe. El que va en la pieza es una propuesta del estudio y hay que aprobarlo o reemplazarlo.
- **Veterinaria:** la de la story es generada. Se reemplaza cuando haya foto de la experta real.
- **Mercado Libre:** la camioneta va sin su logo. Si se quiere el logo oficial en el llamado, hay que conseguir el archivo.
- **Punto final:** se sacó en todas las piezas por la regla que pidió el cliente el 27-08. Confirmar que también aplica a posts y stories.
