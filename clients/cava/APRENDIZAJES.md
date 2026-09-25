# CAVA MORANDÉ — lo que el estudio sabe de este cliente

> **Qué es este archivo.** El cerebro de la cuenta: lo que se aprendió de este cliente
> sesión tras sesión, destilado. La bitácora cuenta **qué pasó**; esto dice **qué
> sabemos**. Si la diseñadora que lleva la cuenta falta mañana, con esto (más el
> manual `CLAUDE.md` y `marca.json`) otra persona retoma sin llamar a nadie.
>
> **Vale SOLO para CAVA MORANDÉ.** Nada de acá se copia a otra marca, ni a una hermana.
> Se alimenta en cada `/cierre` — ver `docs/MEMORIA-POR-CLIENTE.md`.
>
> Criterio: **Constanza Lizana «Coni»** (diseño) · Aprueba: **la ejecutiva de cuentas de CAVA, dueña del brief mensual** (ver §8: falta nombre y confirmar si aprueba ella o la viña)
> Última cosecha: **2026-09-25** · Cosechas: **1**

## 1. Quién es el cliente

CAVA es el **e-commerce de vinos de Viña Morandé**: no es una marca de vino, es la
tienda que vende el portafolio de la viña (Morandé, 7Colores, Adventure, entre otras;
49 vinos en el catálogo técnico). Vende un **producto regulado**: la publicidad de
alcohol en Chile exige advertencia del Ministerio de Salud (Ley 19.925), y las etiquetas
y los sellos de premio son material oficial de terceros. El tono es comercial y de
urgencia (descuentos, embudo PRE → YA COMENZÓ → POCAS HORAS → ÚLTIMO DÍA → SE AGOTAN),
con una capa premium en el dorado y el bodegón.

## 2. Cómo trabaja

| | |
|---|---|
| Quién pide / KAM | Ejecutiva de cuentas de CAVA (escribe el Sheet «CAVA \| Briefs <mes> <año>») · Medios: Ignacio Retamal |
| Quién aprueba (cliente) | Sin nombre registrado — ver §8 |
| Por dónde llega el feedback | Sheet de briefs (cabecera y celdas) + editables y comentarios en el Drive de Coni |
| Dónde se entrega | Carpeta de cliente `1CniZND61f_D1jgHzMh-ZLUVDOPPFKw27` · editables `1Gbpi9zyKanxpLOsslBKTzbcAlBmMAcjd` · email marketing `1G7QfHxjTO8TDd3URxsQBsFkmE8QpC2W-` |
| Ritmo | KV + derivados: **un KV al mes** y ~8 briefs numerados (mailings Mailchimp, post, story, banner) |
| Rondas típicas | Internas, no del cliente: el lote de septiembre 2026 se hizo **tres veces** por no mirar mailings anteriores y por dirección de arte del bodegón |

Nomenclatura: `CAVA_<MES3>_BRIEF<N>-<NN>.png`, **una carpeta por brief** y el `-NN`
corre continuo a través de los ocho briefs (01→18). Campañas grandes: `CYBER_CAVA_<MOMENTO>`.

## 3. Identidad en corto

- **Logo:** CAVA en versales blancas espaciadas + triángulo de puntos naranjos `#DD660E`
  sobre la A + MORANDÉ debajo. Siempre del PNG oficial (`1IhUJwgtAYsgAdfR2qWrH1rySmE5tWOw1`).
- **Dorado:** degradado metálico en diagonal `#5F3C12` → `#C9A24E` → `#FFF7C1`. Nunca plano.
- **Fondo de campañas (Cyber, Black):** satén negro texturado `#333234` → `#1A1A1B` → `#070707`, nunca negro plano.
- **Dos sistemas tipográficos que conviven:**
  - Campañas: **Bebas Neue Pro** (versales, condensada; con SemiExpanded/Expanded) + **Brandon Grotesque**. Adobe Fonts.
  - Mailings mensuales: **Authentic Signature** (script, títulos) + **Butler** (serif, la general).
- **Legal:** caja negra arriba a la derecha, pegada al borde, en **gobCL Bold**, con banda azul `#0063AF` + rojo `#E73439`.
- **Formatos:** KV master 1080×1350 · KV apaisado 4040×1932 · mailing 2250 de ancho (vertical largo) · banner web 4600×2200 · 300×250.

## 4. Reglas firmes

- **R-01** · Toda pieza lleva el recuadro ADVERTENCIA del Ministerio de Salud arriba a la derecha, pegado al borde superior; sin él no se entrega (es ilegal, no feo). Bloqueante en `reglas.yaml` (`franja-ministerio`) — _ejecutiva de cuentas, cabecera del brief, 17-08-2026: «SIEMPRE, PERO SIEMPRE AGREGAR FRANJA MINISTERIO»; medido en Cyber nov-2025, mailing ago-2026 y KV Fiestas Patrias 2025_ · ✔×3
- **R-02** · La leyenda vigente es la del **embarazo** («TODO CONSUMO DE ALCOHOL ES DAÑINO DURANTE EL EMBARAZO»); la de menores de 18 es la del Cyber 2025. Confirma cuál va antes de producir el mes y no mezcles la leyenda de una campaña con la estética de otra — _mailing ago-2026 y brief 1 sep-2026, levantado 27-08-2026_ · ✔×2
- **R-03** · La banda del legal es **azul y rojo tocándose, sin blanco entre medio** — _medido sobre `CYBER_LLEVATEVINOS.png` y `KV_FIESTAS PATRIAS_2025.png`, 27-08-2026_ · ✔×2
- **R-04** · El legal se compone en **gobCL Bold** (tipografía oficial del Gobierno de Chile), no en una sans cualquiera — _/adn sobre los editables de Coni, 25-08-2026_ · ✔×1
- **R-05** · Las botellas no se tocan: ni tamaño relativo entre ellas, ni etiqueta (año, cepa, valle, letra), ni estirar ni espejar. Sólo recortar, escalar el conjunto con **un solo factor** y ajustar sombra. El ratio final tiene que ser igual al del archivo (±0,005; `pegar_botella()` aborta si no) — _medido en los editables de Coni: Black Series Syrah 0,338 = 0,338 y Chardonnay 0,370 = 0,370, 25-08-2026_ · ✔×2
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
- **R-18** · Abre **cada link del brief** y contrasta con `cavamorande.cl/products/<slug>.json`: los slugs están desactualizados y redirigen a otro vino. Manda el nombre escrito en la celda, verificado — _briefs 7 y 8 de septiembre 2026, 27-08-2026_ · ✔×2
- **R-19** · Verifica que `precio final = lista × (1 − %)`. Si no cuadra, se produce con la cifra corregida y **no se programa el envío** hasta que la ejecutiva confirme (tema SERNAC) — _decisión de Valeria, 27-08-2026, briefs 5, 8 y 9_ · ✔×1
- **R-20** · Precios en CLP chileno ($10.990), el anterior tachado; **MORANDÉ con tilde** y **7Colores junto**. Bloqueantes en `reglas.yaml` — _Dirección de área y catálogo técnico, 25/27-08-2026_ · ✔×1
- **R-21** · Del brief se toman **sólo** «Banner principal» y «Texto en imagen»; Tema, Asunto y Preheader son para Mailchimp — _manual CAVA §11, 27-08-2026_ · ✔×1
- **R-22** · Antes de diseñar un mailing, **mira los mailings anteriores** reales, no un print ni una referencia de otra campaña, y verifica con `file` que cada referencia sea imagen — _Valeria, 27-08-2026: «no revisaste otros mailings y la referencia»_ · ✔×1

## 5. Excepciones

- **E-01** · El fondo satén negro vale para **campañas** (Cyber, Black). El KV **mensual** sigue el brief del mes: septiembre 2026 fue Fiestas Patrias (viñedo otoñal, luz de atardecer, nunca frío ni azulado, adorno de flores rojas y espigas, sin folclor caricaturesco); desde el brief 9 (22-09) pasa a primaveral «sin detalles patrios» — _brief de septiembre 2026_
- **E-02** · La zona segura de Meta sólo aplica a las stories reales (`*_ST_*`, `*_STORY_*`), no a los mailings verticales de Mailchimp — _`reglas.yaml`, ajuste `zona-segura-meta`_
- **E-03** · El legal y el logo van **pegados al borde** por diseño: quedan fuera de la regla de respiro — _`reglas.yaml`, ajuste `respiro-borde`_
- **E-04** · En el KV del mes el bloque logo+titular va centrado en **x≈670** (sobre 2250), no al centro de la pieza, porque el legal ocupa la derecha — _medido sobre `KV_FIESTAS PATRIAS_2025`, 27-08-2026_
- **E-05** · El fondo no siempre es Magnific: el KV del Cyber enlaza 23 fondos, mezcla de IA y stock; se prueban hasta dar con el del mes — _/adn sobre el editable del Cyber, 25-08-2026_

## 6. Lo que se aprueba a la primera

No hay registro de una pieza del estudio aprobada por el cliente. Los patrones de abajo
son piezas **publicadas** de Coni, que son el estándar a replicar:

- **A-01** · Mailing «vino héroe»: bodegón cálido con props de temporada, **una** botella enorme que aparece una sola vez, y a la izquierda badge dorado, nombre en sans bold, precio grande y anterior tachado — _`CAVA_AGO_BRIEF1` «Un Pinot premiado», ago-2026_
- **A-02** · Mailing «titular protagonista»: la tipografía manda, `50%off` gigante en Butler itálica, sin precio ni badge — _`CAVA_AGO_BRIEF3` «Grandes Tintos», ago-2026_
- **A-03** · Mailing de packs: KV arriba y abajo **tarjetas oscuras con filete dorado** — _mailing del dúo 7Colores, 2026_
- **A-04** · KV con titular en dos registros: línea 1 en Butler y línea 2 en Authentic Signature, **la del script es la más grande** — _`KV_FIESTAS PATRIAS_2025`_

## 7. Lo que se rechaza

- **X-01** · Armar el lote sobre un print de baja resolución y una referencia de cupón del Cyber: salió fondo azul marino en vez del bodegón cálido, **tarjetas blancas** que la marca no usa, una barra dorada inventada, botellas a media escala y texto centrado cuando el sistema alinea a la izquierda — _mailings de septiembre 2026, v1, 27-08-2026 · se rehízo entero_
- **X-02** · Botellas **flotando delante del barril** porque el punto de apoyo era un número a mano y el fondo regenerado lo dejó sobre el cuerpo cilíndrico — _KV de septiembre, v2, 27-08-2026 · tercera vuelta_
- **X-03** · Fondo más nítido que la botella (barril a 8,8 contra producto a 5,9): se lee como collage aunque la sombra esté bien — _KV de septiembre, 28-08-2026_
- **X-04** · Barril grande y bonito con «botellitas» encima (botellas al 36 % del alto) — _KV de septiembre, 28-08-2026_
- **X-05** · Dar por buena una referencia sin abrirla: los `.png` de `raw/cava/ref/` eran HTML de login de Google — _27-08-2026 y de nuevo 09-09-2026 · causa raíz del X-01_
- **X-06** · `image-relight` sobre el KV compuesto: tinto ámbar, etiqueta amarilla — _28-08-2026_

## 8. Preguntas abiertas

- **¿Quién aprueba del lado del cliente?** Sólo aparece «la ejecutiva de cuentas» como dueña del brief; falta su nombre y si la viña revisa aparte. → Valeria / KAM.
- **Precios de septiembre 2026 sin confirmar:** brief 5 (50 % OFF, el brief decía $16.640, se usó $9.245), brief 8 (40 %, $7.830 → $11.754) y brief 9 (40 %, $14.370 → $21.564). → ejecutiva de CAVA.
- **¿Qué leyenda va cada mes** (embarazo o menores)? ¿Tiene la ADVERTENCIA un tamaño mínimo legal? → ejecutiva de CAVA.
- ⚠️ **Contradicción interna:** `marca.json` sigue con la leyenda de **menores** y la banda **tricolor con blanco**; el manual (27-08) dice embarazo y azul+rojo sin blanco. Hay que corregir la ficha. → quien haga el próximo `/cierre` de CAVA.
- ⚠️ **Escala de la botella, tres criterios en el manual:** contra el diámetro de la tapa (0,63 en grupo · 0,70 sola), al 52 % del alto de la pieza (28-08, el más nuevo) y el KV de grupo bajado al 45 % para que no se pisen los sellos. ¿Cuál manda hoy? → Coni.
- Las **3 referencias del brief de agosto** siguen sin reponer (Coni las subió el 14-08 pero sin compartir por enlace). → Coni.
- Acceso a los **bottle shots limpios** (SharePoint de Morandé, disco de la diseñadora): sin ellos se trabaja con los del e-commerce, con el sello incrustado. → Coni / la viña.
- **Bebas Neue Pro** y **Brandon Grotesque** hay que activarlas en Creative Cloud en cada máquina; **gobCL** no está instalada en el repo; el cliente mandó sólo **Butler Bold** (los otros pesos son de la familia libre). → Coni / ejecutiva.
- Falta un **editable empaquetado de mailing** para cerrar la geometría fina del legal y la barra dorada sobre 1080. → Coni.

## 9. Registro de cosechas

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-22** · destilados de `clients/cava/CLAUDE.md` (25-08 → 28-08), `reglas.yaml`, `BITACORA.md` (09-09) y las notas de memoria `cava-sistema` y `cava-mailings-septiembre-2026`.
- nuevo **X-01…X-06** · las tres vueltas del lote de septiembre 2026 (feedback de Valeria del 27 y 28-08).
- Criterio atribuido a **Coni** (manual y `reglas.yaml`); las reglas de copy y legal, a la **ejecutiva de cuentas de CAVA**. Nada tomado de otras marcas.
- Quedan anotadas como preguntas dos contradicciones internas: la leyenda en `marca.json` y el criterio de escala de botellas.
