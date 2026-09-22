# MYZOO — bitácora

> Una entrada por jornada, la más nueva arriba. Lo de hoy se escribe hoy: el
> relevo de mañana lee esto antes de abrir cualquier archivo.

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
