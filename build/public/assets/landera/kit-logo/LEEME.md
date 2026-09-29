# Landera — kit de logo con la paleta aprobada

Lo genera `scripts/landera_kit_logo.py` desde `raw/landera/editables/LOGO_LANDERA.ai`.
**40 piezas × 3 formatos (PDF vector · SVG · PNG con fondo transparente) = 120 archivos.**

## Por qué existe

El editable de la diseñadora y sus 4 PNG exportados están **con la paleta vieja**:
el isotipo va en verde oscuro `#1C4907`. El manual que el cliente aprobó el
03-09-2026 usa el **verde oliva `#687B5D`**. El logo se recoloreó entre el
editable y el manual, y el editable nunca se actualizó.

## Qué trae

| Carpeta | Qué | Piezas |
|---|---|---|
| `policromo/` | El logo a color, ya con el oliva | 5 |
| `monocromo/` | Las **cinco** que declara el manual: tinta `#33353E`, terracota `#E4361F`, gris `#666461`, crema `#FAF1E8`, verde `#687B5D` | 25 |
| `monocromo-fuera-de-manual/` | ⚠️ Blanco puro y negro puro | 10 |

Las 5 piezas de cada juego son `HOR-FARM`, `HOR-GESA`, `VER-FARM`, `VER-GESA` e
`ISO` — la nomenclatura que ya usa la diseñadora, para no inventar otra.

⚠️ **Blanco y negro NO están en el manual.** Se generaron porque un kit sin blanco
puro no sirve sobre fotografía oscura y sin negro puro no sirve para impresión a
una tinta, pero **van aparte hasta que el cliente los apruebe**. No meterlos en
una entrega como si fueran del sistema.

## Lo que este kit NO es

**No reemplaza el `.ai` maestro.** El entregable del contrato —*«archivos abiertos
entregados, propiedad 100 % del cliente»*— tiene que salir del archivo de Coni,
con sus capas y sus mesas. Acá el color se corrigió sobre el content stream, que
sirve para componer pero no entrega un editable con capas ordenadas.

**Lo que falta pedirle a Coni:** que aplique el verde oliva en el `.ai` fuente y
sume las mesas del isotipo y de las monocromáticas.

## Verificado

- Ninguna de las 40 piezas conserva `#1C4907`.
- Las policromas rinden `#687A5D` / `#666360` / `#E3361F` / `#33353D` — un punto
  por debajo de los declarados, que es el desvío conocido del rasterizador.
- Las monocromas aplanan a un solo color.
- El PNG se dimensiona por el **lado largo** (2000 px): fijándolo por el ancho, el
  isotipo salía de 2000 × 3377 px.

## La proporción

El bloqueo horizontal mide 731,4 × 170,5 pt en el `.ai` y 235,33 × 54,85 pt
extraído del manual: los dos dan **1 : 4,29**. Ese es el número con el que se
escriben el área de reserva y el tamaño mínimo — no uno inventado.

⚠️ La licencia de Barkentina sigue abierta: ver `clients/landera/CLAUDE.md` §2.
