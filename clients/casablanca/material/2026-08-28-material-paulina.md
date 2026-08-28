# Material de Paulina — 28-08-2026

16 imágenes que Paulina Bustamante subió al Drive el 28-08 entre 13:30 y 13:39,
dentro de `Diseño Casablanca Septiembre 2026` (`13pOfaekruRWq8PEHrG0be20Bq6eG4yCB`).

Bajadas con `scripts/bajar-de-drive.py --publico` (el conector MCP no sirve para
bytes y el token OAuth local no está en esta máquina). **Los 16 archivos coinciden
byte a byte con el tamaño que reporta Drive.**

## Compuerta de material — resultado

| Control | Resultado |
|---|---|
| Cabecera real (`verificar-material.py`) | 16/16 PNG reales · 0 rotos · 0 vacíos |
| Tamaño contra el Drive | 16/16 exacto |
| Hoja de contacto | `out/_verificacion/casablanca-material-28ago.png` |
| Zoom 3× al letrero de las 4 fachadas | logo, «by GRUPOREVEX», «Pisos de Madera» y «6359» legibles y sin deformar |
| ¿Es el local real? | **Sí.** Coincide con `public/assets/casablanca/sep/sr2_1_feed.jpg`: mismo panel de piedra crema, mismo logo a la izquierda con «Pisos de Madera» a la derecha, misma banda charcoal, mismo 6359 en la misma posición, mismo arbusto y misma reja |

## Carpeta `fotos_casablanca_suc` → `suc-*`

Origen Drive: `1qtNt898ah1cEho4LXXAVbHAQSHQgWWs4`

| Local | Original en Drive | px | Qué es |
|---|---|---|---|
| `suc-ia-01.png` | ChatGPT Image 28 ago 2026, 09_36_35 a.m. (1).png | 941×1672 | Fachada IA, **9:16 nativo** |
| `suc-ia-02.png` | ChatGPT Image 28 ago 2026, 09_36_35 a.m. (2).png | 1122×1402 | Fachada IA, **4:5 nativo** |
| `suc-ia-03.png` | ChatGPT Image 28 ago 2026, 09_36_36 a.m. (3).png | 941×1672 | Fachada IA, 9:16, contrapicado con mucho cielo |
| `suc-ia-04.png` | ChatGPT Image 28 ago 2026, 09_36_36 a.m. (4).png | 1122×1402 | Fachada IA, 4:5, plano más frontal |
| `suc-foto-lascondes-6.png` | lascondes-6.png | 2160×3840 | **Foto real** (junio), interior del expositor de tablas |
| `suc-foto-lascondes-8.png` | lascondes-8.png | 2048×2048 | **Foto real** (junio), mismo expositor, plano abierto |

## Carpeta `casablanca fondos` → `fondo-*`

Origen Drive: `1bYr0wqetBxk-khAT_cG4O5_H86pVIlz6` · todas 1122×1402 (4:5) ·
generadas con ChatGPT el **28-jul**, subidas el 28-ago.

| Local | Original en Drive | Qué es |
|---|---|---|
| `fondo-ia-01.png` | ChatGPT Image 28 jul 2026, 06_06_49 p.m..png | Tablas sueltas sobre estuco, luz de sombra vegetal |
| `fondo-ia-02.png` | ChatGPT Image 28 jul 2026, 06_08_33 p.m..png | Tablas en corona sobre fondo crema, centro vacío |
| `fondo-ia-03.png` | ChatGPT Image 28 jul 2026, 06_14_10 p.m..png | Piso instalado en diagonal, junta a la vista |
| `fondo-ia-04.png` | ChatGPT Image 28 jul 2026, 06_14_20 p.m..png | Macro de veta con nudo |
| `fondo-ia-05.png` | ChatGPT Image 28 jul 2026, 06_24_48 p.m. (1).png | Tablas cruzadas, tonos claro y oscuro |
| `fondo-ia-06.png` | ChatGPT Image 28 jul 2026, 06_24_48 p.m. (2).png | Damero de tablas tipo parquet |
| `fondo-ia-07.png` | ChatGPT Image 28 jul 2026, 06_24_49 p.m. (3).png | Bodegón de muestras con rama seca y cuenco |
| `fondo-ia-08.png` | ChatGPT Image 28 jul 2026, 06_24_49 p.m. (4).png | Macro de veta, muy plano |
| `fondo-ia-09.png` | ChatGPT Image 28 jul 2026, 06_24_49 p.m. (5).png | Abanico de tablas escalonadas |
| `fondo-ia-10.png` | ChatGPT Image 28 jul 2026, 06_24_49 p.m. (6).png | **Interior con piso instalado**: sala luminosa, mesa y vano al jardín |

## Escalado a resolución de entrega

Las 14 imágenes de IA vienen a 1122 px (4:5) y 941 px (9:16). La entrega de
Casablanca septiembre es **2250×2812** (feed 4:5) y **2250×4000** (story), o sea
que faltaba entre 2,0× y 2,4×.

Escaladas con `scripts/magnific.py escalar --precision --escala 2x`. Se usó el
upscaler **de precisión** justo porque las fachadas llevan logo y el número 6359:
el upscaler normal regenera detalle y puede corromper letras. Verificado con zoom
3× a las 4 fachadas **después** de escalar — logo, «by GRUPOREVEX», «Pisos de
Madera» y «6359» intactos y más nítidos.

La API falló en 4 de las 14 en la primera pasada (`fondo-ia-01`, `-06`, `-09`,
`-10`) con «la tarea terminó sin entregar imagen». El script salta lo ya hecho,
así que se reintentó y las 4 salieron. **Si vuelves a correrlo, revisa el conteo:
14 archivos en `2250/`, no 10.**

Magnific devuelve 2240×2800 para el 4:5 (0,4% bajo destino) y 1880×3344 para el
9:16 (1,2× bajo destino). Ese resto se cubre con Lanczos, sin artefactos.

Las dos fotos reales (`suc-foto-lascondes-*`) ya vienen sobre 2000 px y no se tocan.

## Dónde quedó todo

| Ruta | Qué es |
|---|---|
| `raw/casablanca/material-paulina-28ago/` | los 16 originales tal como los subió Paulina |
| `raw/casablanca/material-paulina-28ago/2250/` | los 14 de IA escalados con Magnific |
| `public/assets/casablanca/sep/nuevo-28ago/` | **listo para montar**, a medida exacta de entrega |
| `out/_verificacion/casablanca-material-28ago.png` | hoja de contacto de los originales |
| `out/_verificacion/casablanca-listo-28ago.png` | hoja de contacto de lo listo |
| `out/_verificacion/logo-*.png`, `logos-escalados.png` | los zoom 3× del letrero, antes y después |

Nombres en `nuevo-28ago/`: `<origen>_<formato>.jpg`, con `feed45` = 2250×2812,
`story` = 2250×4000, `feed` = 2250×2250.

⚠️ **Nada de esto está en git.** `raw/` está ignorado entero y
`public/assets/casablanca/sep/nuevo-28ago/` no cae en ninguna de las excepciones
del `.gitignore` (son ~70 MB, contra los 39 MB de la excepción vigente). Se puede
reconstruir completo desde este documento: los IDs de Drive están en las tablas de
arriba y el comando es

```bash
~/copylab-venv/bin/python3 scripts/bajar-de-drive.py --publico <lista-de-ids> <destino>
```

Cuando se decida **cuáles** de estas imágenes entran en las piezas, esas —y sólo
esas— se agregan al `.gitignore` como excepción, igual que se hizo con
`sr2_*.jpg`. Versionar las 16 candidatas antes de elegir es cargar el repo con
material que se va a descartar.

## ⚠️ Cuatro cosas que Serena tiene que decidir

**1. La regla del sistema dice que la IA no hace ni el logo ni un dato.**
`docs/SISTEMA-DE-MARCAS.md` §2: *«la IA hace ambiente y fondo. Nunca el producto,
nunca el logo, nunca un dato»*. Estas cuatro fachadas llevan las dos cosas: el
logo de Casablanca y la dirección 6359, ambos dibujados por el modelo, no
compuestos desde el asset oficial. Salieron correctos —verificado a zoom 3× antes
y después de escalar— pero son una reproducción, no el vector.

Lo hizo Paulina, que es quien firma Casablanca, así que su criterio manda sobre
sus marcas. Queda anotado porque es una excepción a una regla dura, no un descuido.

**2. «Fotos reales, nunca generadas» — la regla del showroom.**
`CLAUDE.md` §4 Showroom, línea 367, textual: *«Fotos **reales**, nunca generadas»*.
Las piezas de C2 SON las del showroom, y las cuatro fachadas nuevas son generadas.
Es la regla más directamente cruzada de las dos: la del §2 habla del logo y del dato,
ésta habla exactamente de estas fotos.

Otra vez: las hizo Paulina y ella firma la marca. Pero son dos reglas escritas del
manual, no una, y conviene que quede dicho antes de entregar al cliente — sobre todo
porque la pieza invita a visitar un local físico y la foto que lo muestra no es una
foto de ese local, sino una reconstrucción.

**3. ⛔ `suc-foto-lascondes-6/8` NO parecen ser de Casablanca.**
Son las dos únicas fotos REALES del lote y vienen nombradas «lascondes». El showroom
de Casablanca es **Juan XXIII 6359, Vitacura** — «Las Condes» no aparece en su manual
por ninguna parte. Sí aparece en **Revex**: «Las Condes Design» es una sucursal suya,
y el 27-08 Paulina creó `material_revex/suc_lascondes` con material de ese local.

Esto huele al mismo accidente que el 25-08 dejó la carpeta de Casablanca llena de
piezas de Between. **No se usaron en ninguna pieza.** Antes de tocarlas hay que
preguntarle a Paulina de qué local son: meter una sucursal de Revex en una gráfica de
Casablanca es exactamente lo que el sistema prohíbe entre estas dos marcas hermanas.

**4. El cielo.** La fachada real tiene cielo pálido y algo velado. Las cuatro de IA
traen azul intenso con nubes dramáticas. Casablanca **es aire**: gris #626260 y
serif itálica. Un cielo publicitario saturado puede leerse fuera de tono. Si
molesta, se corrige con `scripts/magnific.py reiluminar` o bajando saturación sólo
en el cielo.
