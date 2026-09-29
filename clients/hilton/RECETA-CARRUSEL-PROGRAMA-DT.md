# Receta — carrusel de PROGRAMA de DoubleTree (Escapada Romántica 07-10, aprobado 29-09-2026)

Cómo se hizo el carrusel «Escapada Romántica» del FEED 07-10 (grilla DT octubre,
`13yYW5QacnSRaV422SeBTgFVGwLN5mhTg0anDJzkvaK0`, columna C). Sirve igual para Family Time,
Noche de Bodas o cualquier programa con precio y adicionales. Aprobado por Eli en 3 rondas:
la composición y la foto pasaron a la primera, y las rondas 2 y 3 fueron sólo tipografía.

| Qué | Dónde |
|---|---|
| Composición (2 láminas) | `src/compositions/hilton/DtCEscapadaOct.tsx` · entry `src/DtOct3Entry.tsx` |
| Fotos | `scripts/dt-oct3-escapada-fotos.py` → `public/assets/hilton/dt/oct3/` (en git) |
| Crudos de la IA | `raw/hilton/dt/oct3-escapada/` (no viaja) |
| Referencias | `raw/hilton/dt/ref-oct2/fd-07-10-escapada-{1,2}.jpg` |
| Render | `scripts/still-por-chrome.py` (ver §5) |
| Página de revisión | `scripts/dt-oct3-escapada-revision.py` → https://claude.ai/artifact/9oZT3AsCsYwnrGgmTxYfSi |
| Máster entregado | `out/hilton/dt/entrega-oct3/C1 S2 DT n°{1,2}.png` (2250×2812) |

## 1 · Leer la grilla y el brief

- La grilla es un Sheet nativo y se lee por API: `scripts/sheet-instantanea.py <id> clients/hilton/grillas/api/dt-oct-AAAAMMDD.json`. La ronda nueva sale del diff **por conjunto de cadenas** contra la instantánea anterior.
- Los comentarios de diseño de esta columna estaban **tachados**: contenido ya los había resuelto reescribiendo el brief (titular nuevo, post atemporal). Se diseña lo que dice el brief, y el comentario queda como criterio (R-74: *escaparse*, no noche de bodas).
- El REF de Pinterest se baja con Chrome headless (`--dump-dom`), como en `scripts/dt-oct2-refs.py`. El pin traía **dos imágenes de la misma cuenta**: la portada y una lámina interior con tabla. Esa segunda sirvió de referencia para la lámina 2.

## 2 · La foto de la portada: habitación REAL + pareja IA

1. Primera parada, la sesión **SEP 2026** (`raw/hilton/sesion-sep2026/`). Hojas de contacto de las 523 miniaturas → se eligió **`sep_26-505`**: king con lámparas cálidas y ventanal a la ciudad, y **sin usar en el feed** (R-75). Se baja en alta con `drive.usercontent.google.com/download?id=<id del indice.json>&confirm=t`.
2. Recorte 4:5 centrado en ventana + cama (`cx=0.47`).
3. **Nano Banana Pro** (`scripts/magnific.py pro`, 2K, la foto como `--refs`) con los bloques `KEEP` / `ANAT` / `NAT` de `scripts/dt-familia/ronda3.py` (R-69/R-70): sólo agrega la pareja, la cubeta con el espumante en primer plano y el atardecer en la ventana. Pareja **nueva**, distinta de la familia y de la del feriado. Prompt en tono de escapada: ropa de fin de semana y, explícito, *no rose petals, no bathrobes, no candles, no bridal details*. Se sacaron 2 variantes; se eligió la **a**.
4. Las caras quedaban a la altura del titular y sobraba alfombra: **Flux Pro expand** (Freepik) **sólo arriba** (+11 % de techo), la variante original pegada encima con borde suave y el mismo alto recortado de la alfombra (`… fotos.py subir a`). La pareja baja sin redibujarse.

> ⭐ **Ronda 4 (29-09, APROBADA — «excelente resultado»).** Eli: «la pareja se ve extraña, debe ser
> realista y una foto actual de sesión de habitación mejor lograda». La foto de arriba se reemplazó:
> base **`sep_26-476`** (king con banqueta, ventanal, luz de tarde real, recorte `cx=0.42` sin el minibar),
> **sin atardecer pintado** y la pareja pedida como frame sin retocar de la sesión (bloque `REAL`, NB Pro
> **4K**, pareja sentada en la banqueta). `py scripts/dt-oct3-escapada-fotos.py portada2 a` → `subir2 a`.
> **Así se hace desde ahora cualquier portada con personas en habitación.**

## 3 · La foto de la lámina 2

El brief pedía «mesa en QB al atardecer con dos tragos». La terraza de QB sólo está en miniaturas nocturnas de 400 px y la coctelería real es de barra con luz morada. Por eso se **generó** con Nano Banana Pro, con el KV **Sunset QB aprobado** como referencia del lugar: dos tragos, una entrada desenfocada, sin gente ni texto (variante **b**). ⚠️ Hay que avisarle a Eli que es generada. Si aparece una foto real, se cambia.

## 4 · La composición (lo que quedó aprobado)

**Portada** — calcada de la REF 1:
- Logo de plantilla arriba: es un programa (R-10) y firma una sola vez (R-11).
- Antetítulo `ESCAPADA ROMÁNTICA` en Trade versales, espaciado 0,34 em.
- Titular en Stag a dos pesos (SemiBold / Light), 64 px, **interlínea 1,3** (R-105), centrado.
- Abajo y centrado: **«Desde» arriba** (R-109), la píldora blanca del precio (Trade Bold Cn 56) e `IVA INCLUIDO`, los tres ✔ del brief dibujados en SVG (Stag y Trade no traen el glifo) y la píldora de contorno de la ref con la dirección.
- Velo DT arriba y abajo, que nace en α=0 (R-13).

**Lámina 2** — calcada de la REF 2:
- La foto con un velo azul DT al 50 %.
- **«Escapada Romántica» como logotipo de texto**: Stag itálica SemiBold + Light, 92 px (R-108).
- «Personaliza / tu experiencia» a 58 px, interlínea 1,28.
- Tabla con filetes de 1,5 px a lo ancho y tres columnas:
  - «Agrega / sunset» y «Agrega / masajes» en **un solo peso** (Medium, R-106).
  - Precios en Trade Bold Cn, **ambos con «+»** (R-107).
  - Detalle como **punteo con viñeta y punto final** (R-104).
- El legal en Trade, con punto.

## 5 · Render

Lo normal es `npx remotion still src/DtOct3Entry.tsx DT-C-Oct-Escapada-1 out.png --scale=2.0833`.
El 29-09 Windows bloqueó `remotion.exe` (Control de aplicaciones → `spawn UNKNOWN`), y las
rondas 2 y 3 salieron por Chrome, con el mismo tamaño y las mismas fuentes:

```bash
py scripts/still-por-chrome.py src/DtOct3Entry.tsx "DT-C-Oct-Escapada-1|DT-C-Oct-Escapada-2" \
  '{"lamina":1}|{"lamina":2}' out/.../escapada-1.png out/.../escapada-2.png --escala 2.0833 \
  --publico assets/hilton/dt/fonts assets/hilton/dt/oct3 assets/hilton/dt/logo-dt-blanco.png assets/hilton/dt/logo-dt-azul.png
```

Después: `py qa/motor.py --marca hilton <pngs>`. Un aviso de «banda desenfocada» en la lámina 2 salía por el techo fuera de foco de la propia foto; con el velo final pasa limpio.

## 6 · Lo que corrigió Eli (para acertar a la primera la próxima vez)

| Ronda | Pedido | Regla |
|---|---|---|
| 1→2 | La lámina 2 lleva el nombre del programa con su forma, como Family Time | R-108 |
| 1→2 | «Desde» arriba del precio, para que quede centrado | R-109 |
| 2→3 | «Agrega sunset» / «Agrega masajes», mismo peso | R-106 |
| 2→3 | Los textos apilados, muy juntos | R-105 |
| 2→3 | El punteo de beneficios lleva punto final | R-104 |
| 2→3 | «+$21.000» pide «+$100.000» | R-107 |
