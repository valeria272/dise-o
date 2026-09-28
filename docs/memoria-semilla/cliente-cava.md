---
name: cliente-cava
description: "CAVA — cerebro del cliente: 22 reglas firmes, última cosecha 2026-09-26. Generado desde clients/cava/APRENDIZAJES.md; leerlo antes de diseñar para cava"
metadata:
  type: project
---

⚙️ **Nota generada por `scripts/memoria-cliente.py` en cada /cierre. No se edita acá:**
la fuente es `clients/cava/APRENDIZAJES.md` (léelo completo antes de producir; esto es
sólo lo más confirmado). ⛔ Vale sólo para cava: no se traspasa a otra marca.

Criterio: **Constanza Lizana «Coni»** (diseño) · Aprueba: **la ejecutiva de cuentas de CAVA, dueña del brief mensual** (ver §8: falta nombre y confirmar si aprueba ella o la viña)

## Reglas más confirmadas
- **R-01** · Toda pieza lleva el recuadro ADVERTENCIA del Ministerio de Salud arriba a la derecha, pegado al borde superior; sin él no se entrega (es ilegal, no feo). Bloqueante en `reglas.yaml` (`franja-ministerio`) — _ejecutiva de cuentas, cabecera del brief, 17-08-2026: «SIEMPRE, PERO SIEMPRE AGREGAR FRANJA MINISTERIO»; medido en Cyber nov-2025, mailing ago-2026 y KV Fiestas Patrias 2025_ · ✔×3
- **R-02** · La leyenda vigente es la del **embarazo** («TODO CONSUMO DE ALCOHOL ES DAÑINO DURANTE EL EMBARAZO»); la de menores de 18 es la del Cyber 2025. Confirma cuál va antes de producir el mes y no mezcles la leyenda de una campaña con la estética de otra — _mailing ago-2026 y brief 1 sep-2026, levantado 27-08-2026_ · ✔×2
- **R-03** · La banda del legal es **azul y rojo tocándose, sin blanco entre medio** — _medido sobre `CYBER_LLEVATEVINOS.png` y `KV_FIESTAS PATRIAS_2025.png`, 27-08-2026_ · ✔×2
- **R-05** · Las botellas no se tocan: ni tamaño relativo entre ellas, ni etiqueta (año, cepa, valle, letra), ni estirar ni espejar. Sólo recortar, escalar el conjunto con **un solo factor** y ajustar sombra. El ratio final tiene que ser igual al del archivo (±0,005; `pegar_botella()` aborta si no) — _medido en los editables de Coni: Black Series Syrah 0,338 = 0,338 y Chardonnay 0,370 = 0,370, 25-08-2026_ · ✔×2
- **R-18** · Abre **cada link del brief** y contrasta con `cavamorande.cl/products/<slug>.json`: los slugs están desactualizados y redirigen a otro vino. Manda el nombre escrito en la celda, verificado — _briefs 7 y 8 de septiembre 2026, 27-08-2026_ · ✔×2
- **R-04** · El legal se compone en **gobCL Bold** (tipografía oficial del Gobierno de Chile), no en una sans cualquiera — _/adn sobre los editables de Coni, 25-08-2026_ · ✔×1
- **R-06** · Los sellos de premio no se inventan, no se les cambia el puntaje y no se pasan de un vino a otro: son de certificadores externos y valen para **esa cosecha** — _manual CAVA §2, 25-08-2026_ · ✔×1
- **R-07** · Si falta un bottle shot, **se pide, no se genera** (SharePoint de Morandé o disco de la diseñadora) — _manual CAVA §2, 25-08-2026_ · ✔×1
- **R-08** · Un KV al mes; los derivados son el mismo KV donde cambia sólo la barra dorada del llamado, más botellas y precios. El fondo, el logo, el lockup y el legal no cambian — _medido en las piezas del Cyber, 25-08-2026_ · ✔×1
- **R-09** · En los mailings, el **nombre del vino y el precio van en sans bold**, no en Butler; la serif es sólo para el titular de campaña — _mailing de agosto 2026 de Coni, medido 27-08-2026_ · ✔×1
- **R-10** · Mailings: Authentic Signature para jugar con títulos y Butler (thin) como la general — _ejecutiva de cuentas al mandar las fuentes, 27-08-2026: «signature es para jugar con títulos y butler en thin es la general»_ · ✔×1
- **R-11** · Las tipografías del cliente en `.otf` CFF se convierten a TTF y se verifica el render con acentos, Ñ y cifras antes de usarlas (Chrome las rechaza en silencio) — _Butler y Authentic Signature, 27-08-2026_ · ✔×1
- **R-12** · En el bodegón las **botellas son las protagonistas y la barrica es el mueble**: botellas al 52 % del alto de la pieza, barrica de borde a borde cortada por el pie — _medido sobre `KV_FIESTAS PATRIAS_2025` de Coni, 27-08-2026_ · ✔×1
- **R-13** · Las botellas van **apoyadas sobre la tapa del barril**: la tapa es una elipse (la del centro apoya más abajo), cada botella con sombra de contacto, y el fondo se genera con la tapa visible y despejada. La elipse se mide a ojo con `scripts/cava-calibrar-tapa.py --grilla` una vez por fondo — _Valeria, 27-08-2026, tercera vuelta del lote de septiembre: «los montajes absurdos que hiciste, las botellas no están sobre el barril»_ · ✔×1
- **R-14** · El fondo **no compite en nitidez con el producto**: desenfoque por profundidad (horizonte al máximo, plano de apoyo casi nítido) — _medido 28-08-2026: en el KV de Coni el fondo da 1,4–3,0 de varianza del laplaciano y el producto 7,1–9,2_ · ✔×1
- **R-15** · La luz sobre la botella se integra **por código** (`integra_luz()`: penumbra, rim light, rebote cálido), nunca con `image-relight` — _28-08-2026: el relight dejó el tinto ámbar y la etiqueta amarilla_ · ✔×1
- **R-16** · Para ampliar bottle shots, **upscaler de precisión** (`scripts/cava-botellas-2x.py`), nunca el creativo (redibuja letras) ni LANCZOS ×1,9 (ablanda la etiqueta) — _28-08-2026_ · ✔×1
- **R-17** · El apilado de botellas va **de derecha a izquierda**, porque los bottle shots del e-commerce traen el sello incrustado hacia la derecha del hombro — _28-08-2026_ · ✔×1
- **R-19** · Verifica que `precio final = lista × (1 − %)`. Si no cuadra, se produce con la cifra corregida y **no se programa el envío** hasta que la ejecutiva confirme (tema SERNAC) — _decisión de Valeria, 27-08-2026, briefs 5, 8 y 9_ · ✔×1
- **R-20** · Precios en CLP chileno ($10.990), el anterior tachado; **MORANDÉ con tilde** y **7Colores junto**. Bloqueantes en `reglas.yaml` — _Dirección de área y catálogo técnico, 25/27-08-2026_ · ✔×1

## Lo que ya costó rondas
- **X-01** · Armar el lote sobre un print de baja resolución y una referencia de cupón del Cyber: salió fondo azul marino en vez del bodegón cálido, **tarjetas blancas** que la marca no usa, una barra dorada inventada, botellas a media escala y texto centrado cuando el sistema alinea a la izquierda — _mailings de septiembre 2026, v1, 27-08-2026 · se rehízo entero_
- **X-02** · Botellas **flotando delante del barril** porque el punto de apoyo era un número a mano y el fondo regenerado lo dejó sobre el cuerpo cilíndrico — _KV de septiembre, v2, 27-08-2026 · tercera vuelta_
- **X-03** · Fondo más nítido que la botella (barril a 8,8 contra producto a 5,9): se lee como collage aunque la sombra esté bien — _KV de septiembre, 28-08-2026_
- **X-04** · Barril grande y bonito con «botellitas» encima (botellas al 36 % del alto) — _KV de septiembre, 28-08-2026_
- **X-05** · Dar por buena una referencia sin abrirla: los `.png` de `raw/cava/ref/` eran HTML de login de Google — _27-08-2026 y de nuevo 09-09-2026 · causa raíz del X-01_
- **X-06** · `image-relight` sobre el KV compuesto: tinto ámbar, etiqueta amarilla — _28-08-2026_
