# Bitácora — RENTAS NUEVA URBE (Valle Altiplánico)

> Una entrada por sesión, la más nueva arriba. Se escribe en el `/cierre`.

---

## 2026-09-02 — Valeria Traverso (con Claude)

**Qué se hizo:** Se abrió el sistema de marca de Rentas, que no existía en el estudio
(la marca estaba solo como nota suelta dentro del kit de INU). Se leyeron las grillas de
**julio, agosto, septiembre y octubre 2026** completas, se bajaron los **22 archivos de
mailing** de julio, agosto y septiembre, y sobre ellos se midió el sistema.

**Lo que se midió (no se supuso):**
· **Paleta: azul `#1372F1` + lima `#CCDC00` + blanco.** Moda exacta de píxel sobre las
  6 piezas de septiembre; los mismos dos hex salen en agosto y en julio. **No es la paleta
  de INU** (`#2050B4` / `#CCE054`), que es lo que el kit del repo tenía cargado — cualquier
  pieza de Rentas hecha con ese kit sale off-brand.
· **Montserrat confirmada por glifos**, no por parecido: se rindió el botón real
  `AGENDA TU VISITA` en cada candidata. Montserrat 700 con tracking +0,02 em da **IoU 84,7 %**;
  Poppins SemiBold 76,5 % y **empeora** al abrir el tracking; Inter 59,4 %.
· **La caja blanca del logo mide 10,2 % del ancho del lienzo**, alto 0,94× su ancho, colgada
  del borde superior, radio inferior 22,5 % de su ancho, eje x en 0,26–0,28. Idéntica en las
  cinco piezas medidas y **con tres diseñadores distintos** — es la constante más fuerte de la marca.

**Dónde quedó:** `clients/nueva-urbe/CLAUDE.md` + `marca.json` + esta bitácora;
kit `src/brand/rentas.ts` (typecheck limpio). Material en `raw/nuevaurbe/rentas/`.
También se arregló `scripts/drive-carpeta.py`, que no traía el fix de certifi y moría con
`CERTIFICATE_VERIFY_FAILED` en Mac.

**Decisiones de Valeria:** el criterio vigente es el de **Paulina (septiembre)**; el carrusel
de Halloween va con **imágenes IA fotorrealistas**; el WhatsApp va **verbatim del brief**.

**Qué sigue:** producir la grilla de octubre — reel 6-oct, estático 13-oct, carrusel PAID
20-oct, carrusel Halloween 27-oct, historias 2 y 29-oct.

**Abierto:**
1. **⛔ BLOQUEANTE — la carpeta `Artes` de Drive sigue cerrada.** Tiene permiso propio que
   anula el de la carpeta madre que Valeria compartió. Ahí están las piezas de feed y de
   historias de septiembre de Paulina, que son las que fijan la retícula 4:5 y 9:16. Lo
   medido hasta ahora sale de **banners de mailing**, no de piezas de feed.
2. **⛔ BLOQUEANTE — no hay material de Valle Altiplánico bajado.** Las fotos del condominio
   (`PROYECTOS INMOBILIARIOS/VALLE ALTIPLÁNICO`), los `videos-dron` de Paulina y los logos
   Rentas/Valle (`LOGOS INU`) están todos en el árbol `INMOBILIARIA NUEVA URBE`, cerrado.
   La marca manda **foto real del condominio**, así que no se puede reemplazar con IA.
3. **⚠️ El WhatsApp del estático del 13-oct.** La grilla dice `9951` (número de Travesía, la
   marca de venta). El brief de mailing del **mismo mes** usa `9955` dos veces y su nota final
   dice «se usa +56 9 9707 9955». Valeria eligió verbatim del brief **antes** de que apareciera
   esa nota. Hay que reconfirmarlo con ella o con Carlos.
4. **Rentas cambió de diseñador tres meses seguidos** (Coni jul · Diego ago · Paulina sept),
   con tres nomenclaturas distintas de archivo. Quedó fijado Paulina, pero conviene que el
   cliente y el equipo lo sepan.
5. **La `logos rentas` del árbol compartido está VACÍA.**
