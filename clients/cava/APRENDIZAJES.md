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
> Última cosecha: **2026-09-30** · Cosechas: **5**

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
- **Coni trabaja desde Drive, no desde el Mac** (pidió el 28-09-2026: «quiero que todo esté en Drive»): lo que se rinde se sube a la carpeta de la cuenta con subcarpetas (`VERSIONES ANTERIORES/`, `ARCHIVOS DE TRABAJO/`) y, comprobado por md5, se borra de `out/`. Para re-rendir, correr el script o bajar de Drive — _Coni, 28-09-2026_

## 3. Identidad en corto

- **Logo:** CAVA en versales blancas espaciadas + triángulo de puntos naranjos + MORANDÉ
  debajo. Siempre del PNG oficial (`1IhUJwgtAYsgAdfR2qWrH1rySmE5tWOw1`). ⚠️ revisada
  2026-09-30: el naranjo **NO es `#DD660E`** (anotado a ojo) — es **`#E1670E`**, leído del
  vector del logo en `CAVA_SEPT.ai` y comprobado contra dos piezas publicadas
  (`CAVA_SEPT_BRIEF3.png` y `CYBER_CAVA_ST.png`) — _hallazgo técnico, 23-09-2026,
  `marca.json` ya lo trae corregido_. El logo tiene **dos tintas**: el texto en blanco
  y el racimo de la V + la tilde de MORANDÉ en este naranjo — un logo todo blanco está mal.
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
- **R-23** · Los sellos de premio van **superpuestos como gráfica plana** sobre la botella: no siguen su perspectiva ni llevan resplandor, sólo una sombra corta que los despegue del fondo — _Coni, comentario en Drive sobre las 3 propuestas del Cyber de octubre, 23-09-2026: «no es necesario que sea realista... quítale el resplandor al sello»_ · ✔×1
- **R-24** · El descuento de campaña es un **bloque editorial centrado** — «50% OFF» en Butler Light, el titular corto en Authentic Signature (script), filete con ✦, y la bajada en Butler Regular versales espaciadas en dos líneas — y **no** un disco. La escala y la tinta se adaptan a cada escena (verificado con contraste WCAG), pero el estilo no cambia. **El nombre del vino y los precios NO entran al bloque**: siguen en sans bold (R-09) — _Coni lo ajustó a mano en Illustrator, 25-09-2026; reemplaza el disco del 24-09-2026 (manual §11 bis)_ · ✔×2 _(dos cosechas independientes —la nocturna del 30-09 y la de Coni del 28-09— llegaron a la misma regla por separado)_
- **R-25** · Una fuente **extraída de un `.ai`** es un subconjunto: trae el mapa de caracteres completo pero puede tener glifos con el **contorno vacío**, sin dar error — siempre renderizar el texto y mirarlo antes de dar una fuente por buena — _hallazgo técnico, 23–24-09-2026 (de 9 variables de Raleway sólo la Black estaba entera; Bebas Neue Pro hubo que fundirla de dos editables)_ · ✔×1
- **R-26** · **Una sola advertencia del Ministerio por pieza** — las variantes de la Ley 19.925 son alternativas y rotan, no se suman dos recuadros en la misma gráfica — _Coni, 24-09-2026, corrigiendo un error propio (se había entendido «agregar otro recuadro» y se pusieron dos)_ · ✔×1
- **R-27** · Para la advertencia de «conducir», **no sirve cualquier página** de `ADVERTENCIAS_BEBIDAS-ALCOHOLICAS.pdf`: las 27 y 43 traen una errata («LIMITA LA CAPACIDA», sin la D), las 6/10/30/34/38 llevan el Ministerio arriba (al revés que en CAVA) y la 22 es cuadrada y la banda cae fuera de la zona que revisa `franja_legal`. Sirve la **página 18**, exportada a **940 px** de ancho (a 808 la banda da 56 px y el check exige 60, rechaza) — _medido 24-09-2026 contra `qa/motor.py --marca cava`_ · ✔×1
- **R-28** · Para que un producto compuesto se vea apoyado no basta la sombra proyectada: hace falta la **oclusión de contacto** — el objeto tapa la luz rasante y oscurece la superficie alrededor de su base. Sin eso queda un halo claro y el producto se lee flotando — _hallazgo técnico, escenas del Cyber de octubre sobre piedra, 23-09-2026_ · ✔×1

- **R-29** · Cuando alguien ajusta una pieza a mano, **se mide SU archivo**, no se estima: se aísla la tinta por luminancia —y el oro por COLOR, porque una script dorada de trazo fino se cae de un umbral de luz— y se despeja por bisección qué cuerpo y qué tracking la producen — _Coni, 25-09-2026; su export venía a 2,0836× y de ahí salieron los cuerpos 310 / 240 / 94_ · ✔×1
- **R-30** · El cuerpo se resuelve contra el **ANCHO Y EL ALTO** de la caja de tinta, no sólo el ancho; y la tinta se mide **renderizando**, no con `getbbox`. Con el ancho solo, el script salía 58 puntos de más —ella lo había trackeado— y el bloque quedaba a 4 px de la cápsula de la botella — _25-09-2026_ · ✔×1
- **R-31** · Antes de llevar un lineamiento a otra escena, **se mide la escena**: el bloque pide una franja libre de borde a borde bajo el logo. Sobre fondo naranja el blanco da 2,76:1 y el dorado 1,15:1 → ahí va el **negro del Cyber `#1D1D1B`** (5,8:1), que `marca.json` ya declara para ese caso — _medido sobre las tres propuestas del Cyber, 25-09-2026_ · ✔×1
- **R-32** · El dorado de CAVA es un **degradado metálico**, nunca un color plano — lo dice `marca.json` con sus cinco topes. Pintado plano en el tono medio, el script se lee apagado: pasó de 5,31:1 a 10,93:1 al aplicar la rampa. ⚠️ Pero sobre texto va la mitad LUMINOSA (medio → luz → brillo → luz → medio): el tope sombra `#5F3C12` borra los extremos de la palabra — _Coni, 25-09-2026: «no se lee bien»_ · ✔×1
- **R-33** · El KV del Cyber son **4040 × 1932** y su esqueleto es fijo: fondo negro satén · logo arriba a la izquierda · barra dorada con el llamado · titular en versales con contorno dorado + palabra en script · fechas · bajada · botellas a la derecha con sus sellos · advertencia arriba a la derecha. Del KV salen los mailings cambiando **sólo la barra** (R-08), y el material se organiza por etapa del embudo — _medido sobre `CYBER_CAVA_KV.png`, disco KINGSTON, 28-09-2026_ · ✔×1

- **R-34** · Los montajes de botella del Cyber se hacen **en Magnific, en el space de Coni** (página KV CYBER), con SU key visual como referencia de escena y el packshot oficial como referencia de producto: la botella tiene que quedar parada sobre las losas de piedra del set. Los VIP llevan destellos dorados y los del público **no** — es la diferencia que ella marcó entre las dos versiones — _Coni, 30-09-2026_ · ✔×1
- **R-35** · El montaje se genera **en la proporción de la pieza**, no en 9:16. Los mailings corren entre 1:2,2 y 1:2,6 y un montaje 9:16 no da de alto ni de ancho: rellenar estirando el borde «se ve muy feo». Con dos botellas y una sola ficha de precio, **se extiende el fondo en Magnific** y se entrega el par ya centrado — _Coni, 30-09-2026: «trabajémosla junto a Magnific y a esto me refiero con extender el fondo»_ · ✔×1
- **R-36** · La botella se coloca **por cálculo, no por tanteo**: la pieza declara dónde está dentro de su montaje (canto, tapa y base en fracciones) y dónde debe quedar en la pieza, y de ahí salen escala y desplazamiento. Ajustar a ojo no converge porque escala y posición están acopladas — cada corrección de tamaño rompe la alineación horizontal — _30-09-2026, tras cuatro vueltas sobre la misma pieza_ · ✔×1
- **R-37** · Las piezas de una campaña se afinan **contra el mismo patrón, nunca una contra otra**. Afinando pieza por pieza «hasta que cupiera», cada mail terminó con su propia escala de botella y de tipografía — _Coni, 30-09-2026: «empecemos a educarnos con la visual que estamos trabajando»_ · ✔×1
- **R-38** · El logo CAVA MORANDÉ va **arriba y pegado a la izquierda**, al mismo canto que la «C» de CYBERWINE, y el gancho mide **lo mismo que el logo** (de la C al final de la E). Vale también en las piezas de maqueta centrada: que el cuerpo sea centrado no cambia la cabecera — _Coni, 30-09-2026_ · ✔×1
- **R-39** · Nada de texto puede tapar la botella, y la botella se ve **completa**: entre la cursiva del logo y el cupón. Cuando el producto es más ancho —el House frente al Ranquil— el que cede es el encuadre, no la botella — _Coni, 30-09-2026_ · ✔×1

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
- **A-02** · Mailing «titular protagonista»: la tipografía manda, `50%off` gigante en Butler itálica, sin precio ni badge — _`CAVA_AGO_BRIEF3` «Grandes Tintos», ago-2026_ · ✔×2 _(confirmado 25-09-2026: la referencia editorial que trajo Coni para el Cyber y este layout son el MISMO recurso — el bloque extiende el sistema, no inventa uno)_
- **A-03** · Mailing de packs: KV arriba y abajo **tarjetas oscuras con filete dorado** — _mailing del dúo 7Colores, 2026_
- **A-04** · KV con titular en dos registros: línea 1 en Butler y línea 2 en Authentic Signature, **la del script es la más grande** — _`KV_FIESTAS PATRIAS_2025`_

## 7. Lo que se rechaza

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
- **X-13** · Dar por faltante una fuente por buscarla en `~/Library/Fonts`: **Adobe Fonts no vive ahí**. Bebas Neue Pro estaba activada y completa; se comprueba preguntándole a Illustrator, no al sistema de archivos — _25-09-2026_

## 8. Preguntas abiertas

- **Reconectar el conector de Google Drive de claude.ai** antes de retomar el Cyber Day 2026 (Settings → Connectors, abrir chat nuevo): el 28-09 se cayó la sesión y Coni no pudo leer el brief (ni confirmar en qué se diferencian el KV VIP y el KV Cyber Público). → quien retome CAVA.
- **¿Quién aprueba del lado del cliente?** Sólo aparece «la ejecutiva de cuentas» como dueña del brief; falta su nombre y si la viña revisa aparte. → Valeria / KAM.
- **Precios de septiembre 2026 sin confirmar:** brief 5 (50 % OFF, el brief decía $16.640, se usó $9.245), brief 8 (40 %, $7.830 → $11.754) y brief 9 (40 %, $14.370 → $21.564). → ejecutiva de CAVA.
- **¿Qué leyenda va cada mes** (embarazo o menores)? ¿Tiene la ADVERTENCIA un tamaño mínimo legal? → ejecutiva de CAVA.
- ⚠️ **Contradicción interna:** `marca.json` sigue con la leyenda de **menores** y la banda **tricolor con blanco**; el manual (27-08) dice embarazo y azul+rojo sin blanco. Hay que corregir la ficha. → quien haga el próximo `/cierre` de CAVA.
- ⚠️ **Escala de la botella, tres criterios en el manual:** contra el diámetro de la tapa (0,63 en grupo · 0,70 sola), al 52 % del alto de la pieza (28-08, el más nuevo) y el KV de grupo bajado al 45 % para que no se pisen los sellos. ¿Cuál manda hoy? → Coni.
- Las **3 referencias del brief de agosto** siguen sin reponer (Coni las subió el 14-08 pero sin compartir por enlace). → Coni.
- Acceso a los **bottle shots limpios** (SharePoint de Morandé, disco de la diseñadora): sin ellos se trabaja con los del e-commerce, con el sello incrustado. → Coni / la viña.
- **Bebas Neue Pro** y **Brandon Grotesque** hay que activarlas en Creative Cloud en cada máquina; **gobCL** no está instalada en el repo; el cliente mandó sólo **Butler Bold** (los otros pesos son de la familia libre). → Coni / ejecutiva.
- Falta un **editable empaquetado de mailing** para cerrar la geometría fina del legal y la barra dorada sobre 1080. → Coni.
- **El precio real del Cyber de octubre (7Colores Limited Edition Carmenere) sigue sin llegar.** Las cuatro/tres propuestas circulan con `$9.245 / $18.490` **DE MUESTRA**, sin brief de octubre ni respaldo en los editables de 2026. Ninguna es publicable hasta que la ejecutiva lo confirme. → ejecutiva de CAVA.
- **Componer el packshot real de la etiqueta sobre la botella integrada por IA** en las escenas del Cyber de octubre: Magnific redibuja «LIMITED EDITION», «Carménère», «D.O. VALLE DEL MAULE» y «PRODUCTO DE CHILE» como garabatos al integrar la botella en la escena. Dos vías automáticas (`cava-encaja-packshot.py`, `cava-etiqueta-oficial.py`) no dieron un resultado limpio — hay que abordarlo de frente, no parchando. → quien retome el Cyber de octubre.

- ⛔ **Cyber Day 2026: son DOS KV — VIP y Cyber Público — y no se sabe en qué se diferencian.** El brief es un archivo aparte que no está registrado en el repo y no se pudo abrir (conector de Drive caído). Ni el Cyber de 2026 ni los dos de 2025 tienen rastro de dos versiones. → brief del Cyber Day / ejecutiva de CAVA.
- ⛔ **Las etiquetas de las tres propuestas del Cyber de octubre son garabatos** («LIMITED EDITION», «Carménère», «D.O. VALLE DEL MAULE»): Magnific las redibujó al integrar la botella. El packshot oficial está en el repo; falta componerlo con la perspectiva y la luz de cada escena. Dos vías automáticas fallaron. → tarea, no pregunta.
- ⛔ **Propuesta B sin solución en la posición fija del bloque de producto:** cae sobre la sombra proyectada de la botella, cuya luminancia intermedia no contrasta con nada (blanco 2,82:1 · negro 1,63:1). Subirlo al naranja limpio (negro 5,9:1) o dejar B fuera. → Coni.

## 9. Registro de cosechas

### 2026-09-30 — Coni (con Claude) · resolución del choque de cosechas

- ⚠️ **Dos cosechas independientes cubrieron las mismas sesiones** (25 y 28-09) y al
  sincronizar el repo chocaron: la nocturna en la nube (29 y 30-09) y la de Coni del
  28-09 habían escrito **R-23…R-28 y X-07…X-09 con los mismos números y contenido
  distinto**. El auto-merge de git las concatenó y el cerebro quedó con IDs duplicados.
- **Resuelto así:** manda la numeración de la nocturna, porque es la que ya está en el
  remoto y otras sesiones pueden citarla. La regla repetida —el bloque editorial— se
  **fundió** en `R-24`, que sube a **✔×2** por haber sido encontrada dos veces por
  separado, y se le sumó el detalle que sólo tenía la otra versión (el nombre y los
  precios no entran al bloque). Lo que no se repetía se **renumeró**: `R-29…R-33` y
  `X-10…X-13`. No se borró ningún aprendizaje.
- ⛔ **Aprendizaje de proceso, candidato a regla del estudio:** la cosecha nocturna y el
  `/cierre` de la sesión pueden cubrir los mismos días y **no se ven entre sí**. Antes de
  escribir reglas nuevas en un cerebro hay que mirar el último ID usado **en el remoto**,
  no sólo en la copia local.

### 2026-09-30 — Claude nocturno (nube) · sesiones de Constanza Lizana «Coni» (a8e0647)
- nuevo **R-23…R-28** · destilados de `clients/cava/BITACORA.md` (sesiones del 23, 24 y 25-09-2026), `CLAUDE.md` §11 bis y `marca.json` — llegados al repo en un respaldo automático de sesión de Diego Aguilar (commit `a8e0647`), que subió el respaldo pero **no dio el feedback**: quien habla en el texto (comentarios, decisiones, correcciones a mano) es Coni, salvo lo marcado como «hallazgo técnico».
- nuevo **X-07…X-09** · anti-patrones de las mismas sesiones (sombra por elipses, Raleway sin renderizar, doble advertencia).
- ⚠️ corregido en §3: el naranjo del logo es `#E1670E`, no `#DD660E` (medido del vector el 23-09-2026); `marca.json` ya lo tenía así desde esa fecha, este archivo no lo había cosechado todavía.
- nuevas preguntas abiertas (§8): el precio del Cyber de octubre sigue sin confirmar, y falta resolver de frente (no parchando) cómo componer el packshot oficial sobre la botella integrada por IA en esas escenas.
- Nada de §6 (aprobado a la primera): las piezas del Cyber de octubre pasaron por 8 rondas el 24-09 y 4 más el 25-09, todas correcciones de Coni sobre su propio trabajo en curso — no hay una pieza de esas fechas que el cliente haya aprobado.
- Nota para el reporte (no entra al archivo): la regla de fuentes extraídas de un `.ai` (R-25) y la de oclusión de contacto en el compuesto (R-28) leen como candidatas a **regla del estudio** — no son específicas de vino ni de botellas.

### 2026-09-29 — Claude nocturno (nube) · sesión de Coni bloqueada por el conector de Drive
- sin aprendizajes nuevos de cliente: el 28-09 Coni intentó abrir el KV del Cyber Day 2026 (son dos piezas, VIP y Cyber Público) pero el conector de Google Drive de claude.ai tenía la sesión expirada y no se pudo leer el brief — no se produjo nada — _Coni, BITACORA.md 28-09-2026_.
- nueva pregunta abierta (§8): reconectar el conector antes de retomar el Cyber Day 2026.
- nota técnica, no de marca (candidata a regla del estudio, ver el reporte de la cosecha): el token OAuth del estudio autentica como `valeria@copywriters.cl` pero su alcance es `drive.file` — sólo ve lo que la propia app creó — y por eso no sirve para leer el Drive de la agencia; sólo el conector MCP de claude.ai lo ve. El mismo día le pasó lo mismo a la sesión de Más Center — _Coni, BITACORA.md 28-09-2026_.
### 2026-09-28 — Coni (con Claude) · cosecha atrasada del 25-09 + la sesión de hoy

- ⚠️ **Esta cosecha recupera la sesión del 25-09**, que nunca se cosechó acá: su feedback
  había quedado escrito en `CLAUDE.md` §11 bis y en `marca.json`, pero no en el cerebro.
- nuevo **R-23…R-27** · el bloque editorial del descuento y su método, del ajuste que Coni
  hizo a mano en Illustrator (25-09) y de las cuatro rondas de esa sesión.
- nuevo **R-28** · el esqueleto y la medida del KV del Cyber, leídos del Cyber ya producido
  en el disco KINGSTON (28-09).
- nuevo **X-07…X-10** · el disco que duró un día, el titular que se fue encima del logo, el
  degradado que Illustrator no importa sobre texto, y Adobe Fonts buscada donde no vive.
- **A-02 sube a ✔×2**: la referencia editorial que trajo Coni y el mailing de agosto son el
  mismo recurso, así que el bloque EXTIENDE el sistema en vez de inventar uno.
- **Hoy (28-09) no hubo feedback de diseño**: la sesión se fue en abrir el KV del Cyber Day
  y quedó bloqueada por el conector de Drive. Lo que sí entró al cerebro es R-28 y las tres
  preguntas abiertas nuevas.
- ⛔ **Candidata a regla del estudio, para Valeria:** el token OAuth del monorepo tiene scope
  `drive.file` y por diseño no lee el Drive ajeno, así que TODA lectura depende del conector
  MCP de claude.ai — y hoy, con el conector caído, se bloquearon al menos dos cuentas (CAVA y
  Más Center). No lo anoto en otras marcas: es de infraestructura y lo decide ella.

### 2026-09-28 — Claude (con Coni) · orden del Drive, sin trabajo de diseño
- sin aprendizajes nuevos del cliente: hoy no hubo piezas ni comentarios de CAVA. Sólo se ordenó el Drive (`VERSIONES ANTERIORES/` y `ARCHIVOS DE TRABAJO/` en `DISEÑO ia › PRUEBA`) y se vació `out/cava`.
- §2: Coni trabaja desde Drive y no quiere archivos en el Mac.
- Las sesiones del 22 al 25-09 **no habían llegado a GitHub** (Coni no tenía la subida configurada); quedaron subidas hoy. Si la cosecha nocturna las saltó, la del 26-09 no las vio.


### 2026-09-26 — Claude nocturno (nube) · revisión de rutina, sin sesiones nuevas
- sin aprendizajes nuevos: el único commit que `memoria-cliente.py pendientes` marcó (`41b800b`) es el mismo commit que sembró este archivo por primera vez — se lista a sí mismo porque tocó `APRENDIZAJES.md` y el manual en el mismo commit, y el `--since` del script incluye ese límite. No hay contenido posterior a la siembra inicial que revisar.

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-22** · destilados de `clients/cava/CLAUDE.md` (25-08 → 28-08), `reglas.yaml`, `BITACORA.md` (09-09) y las notas de memoria `cava-sistema` y `cava-mailings-septiembre-2026`.
- nuevo **X-01…X-06** · las tres vueltas del lote de septiembre 2026 (feedback de Valeria del 27 y 28-08).
- Criterio atribuido a **Coni** (manual y `reglas.yaml`); las reglas de copy y legal, a la **ejecutiva de cuentas de CAVA**. Nada tomado de otras marcas.
- Quedan anotadas como preguntas dos contradicciones internas: la leyenda en `marca.json` y el criterio de escala de botellas.
