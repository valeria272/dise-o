# Landera — los bloqueos de logo, en vector

Extraídos de `raw/landera/PROPUESTA-BASE-V2.pdf`, **pág. 2**, con
`scripts/landera_extraer_logos.py`. Son los del propio cliente: en esa lámina no
hay ni una imagen rasterizada (30 · 256 · 30 objetos vectoriales en las págs. 1, 2
y 6), así que el logotipo se reproduce **sin tener instalada Barkentina**.

| # | Archivo | Medida | Color medido |
|---|---|---|---|
| 01 | principal-farmland-management | 235,3 × 54,9 pt | policromo |
| 02 | principal-gestion-agricola | 235,3 × 54,9 pt | policromo |
| 03 | secundaria-farmland-management | 169,2 × 134,8 pt | policromo, apilado |
| 04 | secundaria-gestion-agricola | 169,2 × 134,8 pt | policromo, apilado |
| 05 | isotipo | 47,4 × 80,0 pt | policromo |
| 06 | mono-blue-grey-farmland | 235,3 × 54,9 pt | `#33353D` |
| 07 | mono-terracota-gestion | 235,3 × 54,9 pt | `#E3361F` |
| 08 | mono-gris-piedra-farmland | 235,3 × 54,9 pt | `#666360` |
| 09 | mono-crema-gestion | 235,3 × 54,9 pt | `#F8EFE7` — **para fondo oscuro** |
| 10 | mono-verde-oliva-farmland | 235,3 × 54,9 pt | `#687A5D` |

**La retícula.** Los seis bloqueos horizontales miden exactamente lo mismo,
235,3 × 54,9 pt, y los dos apilados 169,2 × 134,8. No es casualidad: la
diseñadora los construyó sobre una retícula, y esa proporción **1 : 4,29** es el
dato con el que hay que escribir la lámina de *área de reserva* y la de *tamaño
mínimo*, en vez de inventar una.

⚠️ **Los hex de arriba son los RENDERIZADOS, un punto por debajo de los
declarados** (`#33353E`, `#E4361F`, `#666461`, `#FAF1E8`, `#687B5D`). La
diferencia es del conversor de color al rasterizar, no del archivo: el original
rinde exactamente lo mismo. Para especificar en el manual van **los declarados**.

⚠️ **Son assets de trabajo, no entregables al cliente todavía.** Cada archivo
lleva la página 2 completa recortada por máscara, así que pesa ~50 KB y contiene
los otros nueve bloqueos escondidos detrás del recorte. Sirve para componer; si
alguna vez hay que entregarle los logos sueltos al cliente, se piden los
originales a la diseñadora.

⚠️ **La licencia de Barkentina sigue abierta** — ver `clients/landera/CLAUDE.md` §2.
Que el logo esté trazado resuelve lo técnico, no lo legal.
