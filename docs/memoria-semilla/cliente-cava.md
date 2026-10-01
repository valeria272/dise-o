---
name: cliente-cava
description: "CAVA — cerebro del cliente: 49 reglas firmes, última cosecha 2026-10-01. Generado desde clients/cava/APRENDIZAJES.md; leerlo antes de diseñar para cava"
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
- **R-24** · El descuento de campaña es un **bloque editorial centrado** — «50% OFF» en Butler Light, el titular corto en Authentic Signature (script), filete con ✦, y la bajada en Butler Regular versales espaciadas en dos líneas — y **no** un disco. La escala y la tinta se adaptan a cada escena (verificado con contraste WCAG), pero el estilo no cambia. **El nombre del vino y los precios NO entran al bloque**: siguen en sans bold (R-09) — _Coni lo ajustó a mano en Illustrator, 25-09-2026; reemplaza el disco del 24-09-2026 (manual §11 bis)_ · ✔×2 _(dos cosechas independientes —la nocturna del 30-09 y la de Coni del 28-09— llegaron a la misma regla por separado)_
- **R-36** · La botella se coloca **por cálculo, no por tanteo**: la pieza declara dónde está dentro de su montaje (canto, tapa y base en fracciones) y dónde debe quedar en la pieza, y de ahí salen escala y desplazamiento. Ajustar a ojo no converge porque escala y posición están acopladas — cada corrección de tamaño rompe la alineación horizontal — _30-09-2026, tras cuatro vueltas sobre la misma pieza; confirmado 01-10-2026 en los banners del público y en las seis de WhatsApp_ · ✔×2
- **R-37** · Las piezas de una campaña se afinan **contra el mismo patrón, nunca una contra otra**. Afinando pieza por pieza «hasta que cupiera», cada mail terminó con su propia escala de botella y de tipografía — _Coni, 30-09-2026: «empecemos a educarnos con la visual que estamos trabajando»; confirmado 01-10-2026: «guiémonos en el WhatsApp 1»_ · ✔×2
- **R-43** · El cuerpo de un texto que se repite en varias piezas se decide **mirando todas las piezas a la vez**, y manda la más larga. Ajustando pieza por pieza, el nombre corto sale más grande que el largo y dejan de ser la misma familia — _Coni, 01-10-2026, sobre los dos banners de pack y después sobre las seis de WhatsApp_ · ✔×2
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

## Lo que ya costó rondas
- **X-01** · Armar el lote sobre un print de baja resolución y una referencia de cupón del Cyber: salió fondo azul marino en vez del bodegón cálido, **tarjetas blancas** que la marca no usa, una barra dorada inventada, botellas a media escala y texto centrado cuando el sistema alinea a la izquierda — _mailings de septiembre 2026, v1, 27-08-2026 · se rehízo entero_
- **X-02** · Botellas **flotando delante del barril** porque el punto de apoyo era un número a mano y el fondo regenerado lo dejó sobre el cuerpo cilíndrico — _KV de septiembre, v2, 27-08-2026 · tercera vuelta_
- **X-03** · Fondo más nítido que la botella (barril a 8,8 contra producto a 5,9): se lee como collage aunque la sombra esté bien — _KV de septiembre, 28-08-2026_
- **X-04** · Barril grande y bonito con «botellitas» encima (botellas al 36 % del alto) — _KV de septiembre, 28-08-2026_
- **X-05** · Dar por buena una referencia sin abrirla: los `.png` de `raw/cava/ref/` eran HTML de login de Google — _27-08-2026 y de nuevo 09-09-2026 · causa raíz del X-01_
- **X-06** · `image-relight` sobre el KV compuesto: tinto ámbar, etiqueta amarilla — _28-08-2026_
- **X-07** · Sombra de botella armada con **elipses superpuestas**: la suma de sus bordes difuminados dejaba un borrón que no correspondía a ninguna forma real, además desproporcionada (1632 px contra 887 de la botella) y corrida 266 px al costado. Coni la marcó tres veces; las dos primeras se diagnosticó mal (se culpó a la orientación y al fondo) — la correcta es derivar la sombra del **alfa de la propia botella** — _KV Cyber de octubre, 24-09-2026, tres rondas_
- **X-08** · Usar una **Raleway extraída del editable sin renderizarla primero**: de las nueve variables sólo la Black tenía los contornos completos y el primer render de «50% OFF» salió con «50%» y una sola «o» debajo — _Cyber de octubre, 24-09-2026_
- **X-09** · Poner **dos recuadros de advertencia** en la misma pieza por entender mal «agregar otro recuadro» — va uno solo, el de conducir — _Cyber de octubre, 24-09-2026_
- **X-10** · El **disco** del descuento (naranja, «50%» grande y «OFF» debajo), que fue la forma pedida el 24-09: al día siguiente Coni trajo una referencia editorial y lo reemplazó entero. Vivió un día — _25-09-2026 · `marca.json › descuento` reescrito_
- **X-11** · Agrandar un elemento sin volver a mirar qué quedó al lado: al subir el «50% OFF» su tinta pasó a arrancar en x=500 y el logo llega a x=709 — 209 px de solape con **16 px de aire** contra «MORANDÉ» — _25-09-2026, cazado midiendo, no mirando_
- **X-12** · Un degradado puesto sobre **texto** en un SVG: Illustrator no lo importa y el «Llegó el Cyber.» abrió en NEGRO en el `.ai`. Sobre trazados sí lo importa, así que fallaba sólo el texto — _25-09-2026, cazado exportando el .ai y comparándolo contra el PNG_
- **X-13** · Dar por faltante una fuente por buscarla en `~/Library/Fonts`: **Adobe Fonts no vive ahí**. Bebas Neue Pro estaba activada y completa; se comprueba preguntándole a Illustrator, no al s
