# EBEMA / EBEMA CLICK — bitácora

> Una entrada por jornada, la más nueva arriba. Lo de hoy se escribe hoy: el
> relevo de mañana lee esto antes de abrir cualquier archivo.

## 2026-09-01 — Serena Abarca

**Qué se hizo:** Paulina pidió por Slack generar las 12 campañas ARIEL de WhatsApp
de septiembre desde una pieza madre suya (`ebema_wtsp_piazza.png`, 2500×4510,
armada con la info de A1), cambiando enunciado ferretero/contratista, precios y
dirección. Se produjeron **6 de 12**: el bloque completo de **LÍNEA PORTEZUELO
(A1–A6)**, por parcheo sobre el píxel de la diseñadora — 0 píxeles modificados
fuera de las zonas de precio, enunciado y dirección. Las tipografías se
identificaron midiendo, no suponiendo: enunciado Raleway SemiBold, dirección
Raleway en peso 450 (que no existe como archivo estático, hubo que traer la
Raleway variable de Google Fonts).

**Dónde quedó:** entrega en `out/ebema/20260901_wsp_A1-A12_piazza/` (`BRIEF.md`
con el brief verbatim del Sheet, `ENTREGA.md` con el QA, `madre/`, `piezas/`,
`qa/`); generador en `scripts/ebema-wsp-piazza-variantes.py`; Raleway variable en
`clients/ebema/sistema/fonts/`. Copia para revisión en el Escritorio de Serena
(`EBEMA Click - WhatsApp Septiembre 2026/`) con `LEEME.txt` y hoja de contacto.
Las 6 piezas de Portezuelo están **rendidas y revisadas**; no hay nada a medias.

**Qué sigue:** cuando Paulina mande **la pieza madre de LÍNEA AZTECA Y CALYX**,
medir su geometría con el mismo método y extender el generador con el bloque
A7–A12 (envío 04/09). La receta de parcheo ya está resuelta, es rápido.

**Abierto:**
- **A7–A12 no son variantes de la madre de Portezuelo** — otro título, otros
  packshots y 3 productos en vez de 4. Esperan su propia madre. Diseñarlas por
  cuenta propia es el error nº1 de §9 de este manual.
- La planilla marca la **Llave Individual Azteca (529779)** como «PRECIO
  PENDIENTE, no incluir hasta recibirlo» → se le pide a Ariel antes del 04/09.
- El brief pide **añadir el logo Piazza** en el bloque Azteca y Calyx.
- **EBEMA no tiene `clients/ebema/reglas.yaml`**, así que `qa/motor.py --marca
  ebema` se niega a correr y el QA de hoy se hizo a mano contra el checklist de
  §8. Queda por escribirlas y firmarlas con Paulina.
