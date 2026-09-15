/**
 * DOUBLETREE — POST ESTÁTICO · HILTON HONORS (FEED col K · 23-09 · 18:00)
 *
 * Encargo de Eli, 15-09-2026: «Trabajaremos diseñando el post estático de la
 * grilla de Doubletree by Hilton […] la S4, debes tomar de referencia [la
 * carpeta REFERENCIAS S4 DT] y subirla una vez termines de diseñar [a S4 › DT]».
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL BRIEF, LITERAL — no se toca ni una palabra (§G: en DT sólo se DISEÑA)
 * ══════════════════════════════════════════════════════════════════════════
 * Hoja FEED, columna K. **Leído de la grilla VIVA el 15-09 a las 10:46**, no de
 * la instantánea de la mañana: entre las dos lecturas el cliente volvió a
 * editar la celda y el estado pasó de `APROBADO` a `OK PARA DISEÑO`.
 *
 *     ESTÁTICO HILTON HONORS, TODOS LOS BENEFICIOS
 *
 *     SECCIÓN 1 – FONDO Y TÍTULO (GANCHO)
 *     Visual: Fotografía real de alta calidad ocupando todo el fondo
 *     (idealmente una perspectiva cenital o angular elegante de las
 *     instalaciones, piscina, lobby o habitación de DoubleTree by Hilton
 *     Santiago Vitacura).
 *     Texto en pantalla (Zona superior izquierda):
 *     MÁS BENEFICIOS EN CADA ESTADÍA CON HILTON HONORS
 *
 *     SECCIÓN 2 – CAJA CENTRAL (BENEFICIOS)
 *     Visual: Caja superpuesta (estilo cristal o translúcida) dividida en 6
 *     cuadrantes con líneas finas. Cada cuadrante debe tener un ícono minimalista.
 *     (Ícono etiqueta de descuento) "Tarifas exclusivas"
 *     (Ícono cama o flecha arriba) "Upgrades de habitación"
 *     (Ícono luna o regalo) "Canje de noches gratis"
 *     (Ícono moneda o puntos) "Acumula puntos en cada estadía"
 *
 *     Sección 3 - Footer
 *     Texto: Inscríbete gratis en el link de la bio
 *
 * ⚠️⚠️ **LA DISCREPANCIA QUE HAY QUE INFORMARLE A ELI, NO RESOLVER (§G).**
 * El brief dice «dividida en **6** cuadrantes» y la lista de rótulos trae **4**.
 * Los otros dos existían y **el cliente los TACHÓ** —«WiFi Premium» y «Check-in
 * Digital»— junto con el titular viejo. La línea del «6» quedó sin actualizar.
 * Se arma con **4 (2×2)**: poner 6 obligaría a inventar dos beneficios.
 *
 * ⛔ Y dos cosas que el brief nombra y el banco no tiene, así que se toma la
 * alternativa que el propio brief ofrece en la misma frase: no hay toma
 * **cenital** («o angular elegante») y no hay **piscina** fotografiada
 * («instalaciones, lobby o habitación» → se usó el LOBBY).
 *
 * ══════════════════════════════════════════════════════════════════════════
 * ⭐⭐ RONDA 2 (15-09) — LAS SEIS MARCAS DE ELI, Y DE DÓNDE SALE CADA ARREGLO
 * ══════════════════════════════════════════════════════════════════════════
 * «Te falta añadir el logo de Hilton honors, ya que es de los beneficios. Trata
 * de utilizar iconos ya utilizados en mis piezas gráficas, busca en los
 * editables. El título déjalo centrado. Logo blanco y conserva la imagen del
 * fondo, la transparencia azul más abajo y sutil. Si los textos no se leen usa
 * una sombra paralela muy sutil en los textos.»
 *
 * 1 · **LOGO DE HILTON HONORS**, en la cajita que dibujó: centrado, entre la
 *     caja de beneficios y la regla del pie. Ver `HONORS` más abajo.
 *
 * 2 · ⭐⭐ **LOS ÍCONOS SALEN DE SUS PIEZAS, Y ESO CORRIGIÓ ALGO MÁS.**
 *     `C1 FT N2` (Family Time, aprobada) trae la **cama** —«Habitación doble»—
 *     y se usa ESA, extraída del PNG aprobado a resolución completa, no una
 *     dibujada de nuevo. Vive en `public/assets/hilton/dt/icono-cama-eli.png`.
 *
 *     Y al medirla apareció el resto de su gramática de cuadrante, que la
 *     ronda 1 no tenía:
 *       · **trazo 2,4 px @1080**, uniforme, esquinas redondeadas, con detalle
 *         interior (no es un ícono geométrico plano);
 *       · caja del ícono ≈ **70,6 × 57,1** @1080;
 *       · entre ícono y rótulo va una **REGLA VERTICAL fina** (1,9 px), con
 *         11,5 px de aire antes y 12,9 después;
 *       · el rótulo va en **DOS LÍNEAS**.
 *
 *     ⛔⛔ **Y el rótulo NO es Trade Gothic: es STAG.** La ronda 1 lo había
 *     puesto en Trade siguiendo «Trade para cuerpo». Medido glifo a glifo sobre
 *     «Desayuno buffet» de `DT FT S3` (IoU 2D, 14 letras):
 *
 *         Stag-Regular 0,701 · Stag-Medium 0,608 · Stag-Light 0,476
 *         arial 0,389 · Trade Gothic Regular 0,285 · Trade BoldCn 0,285
 *
 *     No hay duda posible. En el panel de DT el cuerpo va en Stag; Trade se
 *     queda con las VERSALES y las CIFRAS (en esa misma pieza, «IVA INCLUIDO»
 *     y la dirección son Trade, y el texto corrido es Stag).
 *
 *     Los otros tres íconos —etiqueta, luna y monedas— **no están en ningún
 *     editable al que se pueda llegar**, así que se dibujan calcando ese trazo.
 *
 * 3 · **TITULAR CENTRADO.** La ronda 1 lo alineó a la izquierda siguiendo la
 *     referencia y el «zona superior izquierda» del brief. Manda Eli.
 *
 * 4 · **LOGOTIPO DT EN BLANCO.** La ronda 1 lo puso azul por la §B.4 del manual
 *     («va en azul cuando el fondo es demasiado blanco»), y medido daba blanco
 *     3,30:1 contra azul 4,84:1. **Eli levanta esa regla para esta pieza** y da
 *     ella misma la salida: la sombra paralela. Queda anotado: es excepción de
 *     PIEZA, no cambio de la regla de marca.
 *
 * 5 · **EL VELO, MÁS ABAJO Y MÁS SUTIL.** Ver `VELO`.
 *
 * 6 · **SOMBRA PARALELA MUY SUTIL** en todas las tintas blancas. Ver `SOMBRA`.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA GEOMETRÍA — MEDIDA SOBRE LA REFERENCIA, QUE ES DEL MISMO TAMAÑO
 * ══════════════════════════════════════════════════════════════════════════
 * `REFERENCIAS S4 DT` trae `Ref post s4.jpg`, que Eli subió el 15-09 a las
 * 13:43, y que resulta ser **el mismo pin que el brief enlaza en su celda
 * LINKS**. Dos fuentes independientes. Copia de trabajo a 1080×1350 en
 * `raw/hilton/dt/ref-s4/`. Como la referencia es 1080×1350 y la pieza también,
 * su geometría se traslada **1:1**:
 *
 *   caja           x 100→980 (ancho **880**, centrada) · y 842→1148 (alto 306)
 *   titular        altura de versal **49**, salto entre líneas **68**
 *   regla del pie  y ≈ 1258
 *
 * ⭐⭐ La caja de la referencia (880) es más ancha que el panel medido de DT
 * (730 en `DT FT S3`). Se adopta el 880, con el precedente del Día del Turismo:
 * cuando las dos medidas chocaron, Eli pidió parecerse a la referencia.
 *
 * ⛔ **La caja va de CRISTAL, no opaca.** Medido, el panel de `DT FT S3` es
 * prácticamente macizo (α ≈ 0,84 en el cuerpo, 0,90 en la fila de íconos). Acá
 * va en 0,30 porque el brief lo pide con todas sus letras —«estilo cristal o
 * translúcida»— y la referencia hace eso.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA REJILLA (mesa 1080×1350; se entrega a 2250×2813, escala 2,0837)
 * ══════════════════════════════════════════════════════════════════════════
 *    111 ─ tope del logotipo DT   ← plantilla `logo-post.png` de Eli
 *    242 ─ pie del logotipo
 *    597 ─ tope de la tinta del titular
 *    777 ─ pie de la tinta del titular
 *    842 ─ tope de la caja de cristal
 *    995 ─ divisor horizontal
 *   1148 ─ pie de la caja
 *   1186 ─ tope del logotipo de Hilton Honors   ← ronda 2
 *   1258 ─ regla del pie
 *   1283 ─ tinta del llamado
 *
 * ⚠️ Esto es FEED ORGÁNICO: **no hay zona segura de Instagram** que reservar.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';

import {DT, cargarFuentesDT} from '../../brand/doubletree';

cargarFuentesDT();

const G = DT.geometria;
const MESA = {ancho: 1080, alto: 1350} as const;

/** Textos LITERALES del brief. No se editan (§G). */
const TITULO = [
  {t: 'MÁS BENEFICIOS', peso: DT.pesos.medium},
  {t: 'EN CADA ESTADÍA', peso: DT.pesos.light},
  {t: 'CON HILTON HONORS', peso: DT.pesos.light},
] as const;

const PIE = 'Inscríbete gratis en el link de la bio';

/**
 * ⭐⭐ RONDA 2 · EL VELO: «LA TRANSPARENCIA AZUL MÁS ABAJO Y SUTIL».
 *
 * La ronda 1 usaba la rampa aprobada en la historia del Día del Turismo, que
 * nace en 0 arriba y sube **cóncava** hasta 0,58 al pie: en el 20 % de la
 * altura ya iba en 0,22 y en el 50 % en 0,48. Eso es justo lo que ella marcó.
 *
 * Ahora la rampa es **convexa**: sigue naciendo en 0 en el borde de arriba,
 * pero arranca casi plana y acelera hacia abajo, y el pie baja de 0,58 a
 * **0,50**. En el 20 % va en 0,03 (era 0,22) y en el 50 % en 0,23 (era 0,48).
 *
 * ⛔ Lo que NO se hace, y es el error a no repetir de la ronda 4 del Día del
 * Turismo: dejarlo PLANO en 0 una franja y hacerlo arrancar de golpe más abajo.
 * Ese codo es una banda visible — «se ve muy forzado». Por eso «más abajo» se
 * resuelve **curvando** la rampa, no cortándola: el velo sigue naciendo en el
 * borde, sólo que casi no pesa hasta pasada la mitad.
 *
 * Paradas cada 10 % para que no quede ningún quiebre a la vista.
 */
const VELO: readonly (readonly [number, number])[] = [
  [0, 0], [10, 0.01], [20, 0.03], [30, 0.08], [40, 0.15], [50, 0.23],
  [60, 0.31], [70, 0.38], [80, 0.44], [90, 0.48], [100, 0.50],
];

const velo = VELO.map(([p, a]) => `rgba(9,25,78,${a}) ${p}%`).join(', ');

/**
 * ⭐ RONDA 2 · LA SOMBRA PARALELA, Y POR QUÉ ES ÉSTA.
 *
 * «Si los textos no se leen usa una sombra paralela muy sutil.» Con el velo más
 * suave, el logotipo en blanco cae a 2,65:1 y el titular a 3,76:1 sobre el peor
 * tercio; la sombra es lo que los devuelve a terreno legible sin cargar la foto,
 * que es exactamente lo que ella pidió conservar.
 *
 * Va en **azul DoubleTree**, no en negro: negro sobre una foto cálida ensucia y
 * se lee como un contorno. Desplazamiento corto y desenfoque ancho —es sombra
 * paralela, no contorno—, más un halo sin desplazamiento que cierra el canto.
 *
 * ⚠️ Es la MISMA sombra para todas las tintas blancas de la pieza. Dos sombras
 * distintas en una misma pieza se leen como dos planos distintos.
 */
const SOMBRA = '0 2px 7px rgba(9,25,78,0.60), 0 0 2px rgba(9,25,78,0.45)';
/** La equivalente para un PNG: `text-shadow` no afecta a una imagen. */
const SOMBRA_IMG =
  'drop-shadow(0 2px 7px rgba(9,25,78,0.60)) drop-shadow(0 0 2px rgba(9,25,78,0.45))';

/**
 * ⛔⛔ RONDA 3 · EL LOGOTIPO DT VA SIN SOMBRA Y SIN HALO — Y ESTO ES HISTORIA,
 * NO CÓDIGO: acá había una `SOMBRA_LOGO` y se retiró.
 *
 * Eli: «El logo no le hagas eso del fondo o sombra azul.»
 *
 * Lo que se probó, en orden, y por qué se fue cada cosa:
 *   1. **Halo radial** detrás del logo — el recurso aprobado en la ST del Día
 *      del Turismo. Allá caía sobre un cielo con textura; acá cae sobre el
 *      **cielorraso plano** del lobby y se veía como una mancha gris. Botado.
 *   2. **Tres sombras paralelas apiladas** sobre el propio logotipo. Subía el
 *      contraste de 2,83:1 a 3,61:1 y a la vista se leía bien… pero es
 *      justamente «eso del fondo o sombra azul» que ella no quiere. Botado.
 *   3. ✅ **Nada.** Logotipo blanco, limpio, sobre la foto.
 *
 * ⚠️ El costo, medido y asumido: sobre el cielorraso el blanco da ~2,7:1, bajo
 * la vara de 4,5. **Es una decisión de dirección de arte de Eli**, tomada dos
 * veces y por escrito, y el QA la lleva declarada con su número a la vista
 * (`logo_contraste_minimo` + `logo_motivo`). La alternativa medida, si alguna
 * vez se quiere en regla, es el azul de la §B.4: 4,84:1 sobre ese mismo fondo.
 */

/** La caja de cristal. Medidas del pin, que es 1080×1350 igual que la pieza. */
const CAJA = {
  x: 100,
  ancho: 880,
  y: 842,
  alto: 306,
  radio: 26,
  /**
   * Filete. Medido en el panel de `DT FT S3`: sus verticales ocupan 3 px y sus
   * horizontales 4 px sobre el máster de 2250, o sea **≈1,5 @1080**. Escala con
   * la pieza (no lleva `non-scaling-stroke`), así que al máster vuelve a dar 3 px.
   */
  filete: 1.5,
  /** El brief: «estilo cristal o translúcida». Ver el encabezado. */
  relleno: 0.3,
  /**
   * ⭐⭐ RONDA 3 · EL DESENFOQUE DEL FONDO DENTRO DEL CUADRO.
   *
   * Eli: «falto el detalle de la referencia de ese cuadro, mira difuminado
   * dentro del cuadro el fondo». Es lo que hace que la caja se lea como CRISTAL
   * y no como un rectángulo pintado — y es lo que le faltaba a las rondas 1 y 2.
   *
   * ⭐ El radio NO se eligió a ojo: se midió sobre el pin. Se comparó la energía
   * de alta frecuencia (laplaciano) **cruzando el borde de la caja**, donde el
   * material fotográfico es el mismo a los dos lados, y se buscó qué radio de
   * desenfoque aplicado a la parte de AFUERA reproduce la nitidez de ADENTRO:
   *
   *   borde superior · pasto 1,3 · pasto 1,3 · agua 3,8 · tejas 4,3
   *   borde inferior · pasto 6,9 · grava 2,9 · tejas 3,5
   *   borde izquierdo ·          alto 2,8 · bajo 8,0
   *
   *   ⇒ mediana **3,5** · media 3,9
   *
   * Dentro de la caja la nitidez cae al **4-29 %** de la de afuera, y eso se ve
   * igual en los cuatro bordes: no es una impresión, es un desenfoque de verdad.
   *
   * ⚠️ La primera medición comparó la caja contra franjas de arriba y de abajo y
   * dio «razón 1,01» —o sea, ningún desenfoque—. Estaba mal planteada: arriba
   * hay pasto y abajo grava, dos texturas con nitidez propia distinta. **Para
   * medir un desenfoque hay que cruzar el borde, no comparar zonas lejanas.**
   */
  desenfoque: 3.5,
} as const;

const CAJA_DER = CAJA.x + CAJA.ancho;
const CAJA_PIE = CAJA.y + CAJA.alto;
const REGLA_PIE = 1258;

/**
 * ⭐ RONDA 2 · EL LOGOTIPO DE HILTON HONORS, en la cajita que dibujó Eli:
 * centrado, entre la caja de beneficios y la regla del pie.
 *
 * ⚠️⚠️ **EL ARCHIVO TODAVÍA NO ESTÁ EN ESTA MÁQUINA, Y NO SE INVENTA.**
 * El bueno es `Hilton Honors Logo_White PNG.png` (13 967 B) o `hilton honors
 * blanco.png` (13 994 B), los dos en el Drive de Eli (`GRILLA IA DT › Logos`,
 * `1juLRu6ctgw-t56kfp6uZwDE9bSqBjsLb`). Ninguno baja:
 *   · `curl` devuelve la pantalla de login de Google en las tres rutas
 *     (`uc?export=download`, `drive.usercontent`, `lh3.googleusercontent`);
 *   · el token del estudio es scope `drive.file` y no ve lo que no subió él;
 *   · el conector MCP sí los lee, pero un archivo de ~14 KB vuelve INLINE y no
 *     queda en disco — sólo los de más de ~40 KB se guardan solos.
 *
 * ⛔ Y OJO CON LA TRAMPA: en esa misma carpeta hay un `hilton honors.png` de
 * 43 KB que **SÍ** baja entero… y **NO es el logo de Hilton Honors**: es el
 * logotipo **Hilton «For The Stay»**. Está mal rotulado en el Drive. Se dejó
 * guardado como `hilton-FOR-THE-STAY (NO es Honors).png` para que nadie lo use
 * por error.
 *
 * Mientras no esté el archivo, `conHonors` va en `false` y el bloque **no se
 * dibuja**: se prefiere una pieza sin el elemento antes que una con un logotipo
 * equivocado. El hueco vertical queda reservado. En cuanto el PNG caiga en
 * `public/assets/hilton/dt/hilton-honors-blanco.png`, se pone en `true` y se
 * vuelve a rendir — no hay que tocar nada más.
 */
const HONORS = {
  /**
   * Tope del bloque. El alto manda; el ancho lo da la proporción real del
   * archivo (**2,3213**, medida sobre el bbox opaco), así que se escala
   * uniforme y nunca se deforma.
   *
   * Va CENTRADO en el aire que queda entre el pie de la caja (1148) y la regla
   * del pie (1258): 110 px de hueco, bloque de 52 ⇒ arranca en 1177.
   */
  y: 1177,
  alto: 52,
  archivo: 'assets/hilton/dt/hilton-honors-blanco.png',
} as const;

/**
 * Cuerpos.
 *
 * · `titulo: 68` ⇒ versal 47,6 (Stag da versal = 0,700 × cuerpo, medido). La
 *   referencia lleva 49.
 * · `rotulo: 29` en **Stag Regular** (ronda 2). Medido, el rótulo más largo
 *   partido en dos («Canje de noches») entra en la columna con aire.
 * · `pie: 29`, también Stag: en `DT FT S3` el llamado del pie va en Stag y las
 *   versales de la dirección en Trade.
 */
const CUERPO = {titulo: 68, rotulo: 29, pie: 29} as const;

/** 66 px sobre una versal de 47,6 ⇒ 1,39, que es la proporción del pin (68/49). */
const SALTO_TITULO = 66;

/**
 * ⭐ RONDA 2 · LA GRAMÁTICA DE CUADRANTE DE ELI, medida en `C1 FT N2`:
 * ícono · 11,5 de aire · regla vertical de 1,9 · 12,9 de aire · rótulo.
 */
const CELDA = {
  iconoAncho: 71,
  iconoAlto: 57,
  aireAntesRegla: 11.5,
  reglaAncho: 1.9,
  reglaAlto: 62,
  aireDespuesRegla: 13,
  padIzquierda: 30,
  padDerecha: 18,
} as const;

/** Trazo de los íconos dibujados: calca el de la cama de Eli (2,4 px @1080). */
const trazo = {
  fill: 'none',
  stroke: DT.colores.blanco,
  strokeWidth: 2.4,
  strokeLinecap: 'round' as const,
  strokeLinejoin: 'round' as const,
};

/**
 * ⭐⭐ RONDA 3 · «ESOS ÍCONOS SE VEN ACHATADOS, APLASTADOS».
 *
 * Tenía razón y la causa era de dibujo, no de escala: los tres íconos dibujados
 * se hicieron **llenando la caja de 71 × 57** de Eli, que es ancha porque su
 * contenido es una CAMA —un objeto que de verdad es más ancho que alto—. Un
 * regalo, una etiqueta y una pila de monedas no lo son, así que al estirarlos a
 * lo ancho de esa caja quedaron aplastados.
 *
 * Ahora cada ícono se dibuja en un **cuadrado de 52 × 52 centrado** dentro de la
 * ranura (`VB_ICONO`), y la cama —que sí es de Eli— va a **su proporción real
 * medida, 70,6 × 57,1** (147 × 119 px en el PNG aprobado, razón 1,2353), sin
 * estirarla ni un punto.
 *
 * ⛔ La ranura sigue siendo de 71 de ancho para que los cuatro rótulos arranquen
 * en la misma vertical; lo que cambia es cuánto de esa ranura ocupa cada dibujo.
 */
const VB_ICONO = {ancho: 71, alto: 57} as const;
/** La cama de Eli, a su proporción real. No se deforma. */
const CAMA = {ancho: 69.9, alto: 57.1} as const;
/**
 * ⚠️ RONDA 3 · LA CAMA SE VOLVIÓ A EXTRAER, y el arreglo importa para cualquier
 * ícono que se saque de una pieza aprobada.
 *
 * La primera extracción sacaba el alfa de una rampa 60→250 sobre la luminancia,
 * y arrastraba **un halo**: el panel azul de `C1 FT N2` es translúcido, así que
 * los parches de foto que se ven a través quedaban con alfa > 0 y en la pieza
 * nueva aparecía una caja oscura fantasma detrás del ícono.
 *
 * ✅ El histograma de esa región es **bimodal** —fondo 0-120, tinta 200-255, con
 * una transición delgadísima—, así que la rampa correcta es **120 → 235**:
 * separa limpio y conserva el antialias del borde. Proporción real 1,2250.
 */

/**
 * Los tres íconos que hubo que dibujar. El brief nombra cada uno, así que no se
 * eligen: se dibujan los que pide, calcando el trazo de la cama.
 *
 *   «etiqueta de descuento» → la etiqueta con su ojal y el signo de porcentaje
 *   «luna o regalo»         → la luna
 *   «moneda o puntos»       → las monedas apiladas (es lo que dice «acumula»)
 */
const IconoSvg: React.FC<{children: React.ReactNode}> = ({children}) => (
  <svg
    width={VB_ICONO.ancho}
    height={VB_ICONO.alto}
    viewBox={`0 0 ${VB_ICONO.ancho} ${VB_ICONO.alto}`}
    style={{flexShrink: 0, filter: SOMBRA_IMG}}
  >
    <g {...trazo}>{children}</g>
  </svg>
);

type Celda = {icono: React.ReactNode; rotulo: readonly [string, string]};

const CELDAS: readonly Celda[] = [
  {
    // Etiqueta de descuento: cuerpo, ojal y el «%» de dos puntos y barra.
    icono: (
      <IconoSvg>
        <path d="M11 24.5 L31.5 4 a4.6 4.6 0 0 1 3.3-1.4 H56 a4.6 4.6 0 0 1 4.6 4.6 V27 a4.6 4.6 0 0 1-1.4 3.3 L38.7 50.9 a4.6 4.6 0 0 1-6.5 0 L11 31 a4.6 4.6 0 0 1 0-6.5 Z" />
        <circle cx="51" cy="12.5" r="3.9" />
        <path d="M24.5 40 L40 24.5" />
        <circle cx="25" cy="25.5" r="2.7" />
        <circle cx="39.5" cy="39.5" r="2.7" />
      </IconoSvg>
    ),
    rotulo: ['Tarifas', 'exclusivas'],
  },
  {
    // ⭐ La CAMA es de Eli: extraída de `C1 FT N2` («Habitación doble»).
    icono: (
      <Img
        src={staticFile('assets/hilton/dt/icono-cama-eli.png')}
        style={{
          // ⚠️ A SU PROPORCIÓN REAL (147 × 119 en el PNG aprobado). El dibujo es
          // de Eli: se escala uniforme, jamás por geometría.
          width: CAMA.ancho,
          height: CAMA.alto,
          marginLeft: (VB_ICONO.ancho - CAMA.ancho) / 2,
          marginRight: (VB_ICONO.ancho - CAMA.ancho) / 2,
          flexShrink: 0,
          filter: SOMBRA_IMG,
        }}
      />
    ),
    rotulo: ['Upgrades de', 'habitación'],
  },
  {
    /**
     * ⭐ El brief da a elegir: «(Ícono luna o regalo)». Se dibujó primero la
     * LUNA y se cambió al REGALO por estilo, no por gusto: los íconos de Eli
     * —la cama, el buffet, el calendario— son **objetos con estructura
     * interior**, no siluetas. Una luna es una sola curva y al lado de su cama
     * se leía como de otra familia. El regalo tiene tapa, caja y cinta, que es
     * el mismo tipo de dibujo.
     */
    icono: (
      <IconoSvg>
        <rect x="11.5" y="20" width="48" height="10.5" rx="2.6" />
        <path d="M16 30.5 V50.5 a2.6 2.6 0 0 0 2.6 2.6 h33.8 a2.6 2.6 0 0 0 2.6-2.6 V30.5" />
        <path d="M35.5 20 V53.1" />
        <path d="M35.5 20 c-8.2 0-12.8-2-12.8-6.6 a5.1 5.1 0 0 1 9-3.4 c2.4 2.8 3.8 6.7 3.8 10 Z" />
        <path d="M35.5 20 c8.2 0 12.8-2 12.8-6.6 a5.1 5.1 0 0 0-9-3.4 c-2.4 2.8-3.8 6.7-3.8 10 Z" />
      </IconoSvg>
    ),
    rotulo: ['Canje de noches', 'gratis'],
  },
  {
    // Monedas apiladas: tres discos, que es lo que dice «acumula».
    icono: (
      <IconoSvg>
        <ellipse cx="35.5" cy="13.5" rx="23" ry="7.4" />
        <path d="M12.5 13.5 v10 a23 7.4 0 0 0 46 0 v-10" />
        <path d="M12.5 23.5 v10 a23 7.4 0 0 0 46 0 v-10" />
        <path d="M12.5 33.5 v10 a23 7.4 0 0 0 46 0 v-10" />
      </IconoSvg>
    ),
    rotulo: ['Acumula puntos', 'en cada estadía'],
  },
];

const Cuadrante: React.FC<{celda: Celda}> = ({celda}) => (
  <div
    style={{
      width: CAJA.ancho / 2,
      height: CAJA.alto / 2,
      display: 'flex',
      alignItems: 'center',
      paddingLeft: CELDA.padIzquierda,
      paddingRight: CELDA.padDerecha,
      boxSizing: 'border-box',
    }}
  >
    {celda.icono}
    {/* La regla vertical fina entre ícono y rótulo — es de `C1 FT N2`. */}
    <div
      style={{
        width: CELDA.reglaAncho,
        height: CELDA.reglaAlto,
        marginLeft: CELDA.aireAntesRegla,
        marginRight: CELDA.aireDespuesRegla,
        background: DT.colores.blanco,
        opacity: 0.85,
        flexShrink: 0,
        boxShadow: SOMBRA,
      }}
    />
    <div
      style={{
        fontFamily: DT.fuentes.titular,
        fontWeight: DT.pesos.regular,
        fontSize: CUERPO.rotulo,
        lineHeight: 1.2,
        color: DT.colores.blanco,
        textShadow: SOMBRA,
        whiteSpace: 'nowrap',
      }}
    >
      {celda.rotulo.map((l) => (
        <div key={l}>{l}</div>
      ))}
    </div>
  </div>
);

export const DtFtHonors: React.FC<{guia?: boolean; conHonors?: boolean}> = ({
  guia = false,
  conHonors = true,
}) => (
  <AbsoluteFill style={{backgroundColor: DT.colores.azul}}>
    {/*
      1 · La foto real del lobby, a sangre. Ronda 2: Eli pidió CONSERVARLA, así
      que el encuadre y el revelado no se tocan. Nada generado con IA.
    */}
    <Img
      src={staticFile('assets/hilton/dt/ft-honors-lobby.jpg')}
      style={{width: '100%', height: '100%', objectFit: 'cover'}}
    />

    {/* 2 · El velo azul — ronda 2: más abajo y más sutil. Ver `VELO`. */}
    <AbsoluteFill style={{background: `linear-gradient(to bottom, ${velo})`}} />


    {/*
      3 · Logotipo DT, centrado y **BLANCO** (ronda 2), con la sombra paralela.
      Geometría de la plantilla `logo-post.png` de Eli: ancho 160, tope 111.
      Se escala UNIFORME desde su proporción real 1,2254 — nunca por geometría.
    */}
    <Img
      src={staticFile('assets/hilton/dt/logo-dt-blanco.png')}
      style={{
        position: 'absolute',
        top: G.logoYFeed,
        left: (MESA.ancho - G.logoAncho) / 2,
        width: G.logoAncho,
        height: G.logoAncho / G.logoProporcion,
        // ⭐⭐ RONDA 3: SIN sombra y SIN halo. «El logo no le hagas eso del fondo
        // o sombra azul.» Ver la nota de `SOMBRA_LOGO`, que queda documentada
        // como lo que se probó y ella descartó.
      }}
    />

    {/*
      4 · El titular, CENTRADO (ronda 2). El bloque se ancla por su PIE, así la
      tinta cierra donde la cierra la referencia sin depender de cuántas líneas
      tenga el titular.
    */}
    <div
      style={{
        position: 'absolute',
        left: CAJA.x,
        bottom: MESA.alto - 777,
        width: CAJA.ancho,
        textAlign: 'center',
        fontFamily: DT.fuentes.titular,
        fontSize: CUERPO.titulo,
        lineHeight: SALTO_TITULO / CUERPO.titulo,
        letterSpacing: '0.035em',
        color: DT.colores.blanco,
        textShadow: SOMBRA,
      }}
    >
      {TITULO.map(({t, peso}) => (
        <div key={t} style={{fontWeight: peso, whiteSpace: 'nowrap'}}>
          {t}
        </div>
      ))}
    </div>

    {/* 5 · La caja de cristal: el relleno va aparte del filete. */}
    <div
      style={{
        position: 'absolute',
        left: CAJA.x,
        top: CAJA.y,
        width: CAJA.ancho,
        height: CAJA.alto,
        borderRadius: CAJA.radio,
        background: `rgba(9,25,78,${CAJA.relleno})`,
        // ⭐⭐ RONDA 3 · EL DETALLE QUE FALTABA DE LA REFERENCIA: el fondo va
        // DIFUMINADO DENTRO DEL CUADRO. Ver `CAJA.desenfoque`.
        backdropFilter: `blur(${CAJA.desenfoque}px)`,
        WebkitBackdropFilter: `blur(${CAJA.desenfoque}px)`,
      }}
    />

    {/* 5b · Los cuatro cuadrantes, en el orden en que el brief lista los rótulos */}
    <div
      style={{
        position: 'absolute',
        left: CAJA.x,
        top: CAJA.y,
        width: CAJA.ancho,
        height: CAJA.alto,
        display: 'flex',
        flexWrap: 'wrap',
      }}
    >
      {CELDAS.map((c) => (
        <Cuadrante key={c.rotulo[0]} celda={c} />
      ))}
    </div>

    {/*
      5c · El filete, los divisores y la regla del pie.

      ⚠️ Los divisores van más tenues que el contorno (0,45 contra 1). En la
      referencia pasa lo mismo: el marco cierra la caja y las líneas de adentro
      sólo separan. Con los dos al mismo peso la caja se lee como una tabla y
      pierde el aire de cristal.
    */}
    <svg
      width={MESA.ancho}
      height={MESA.alto}
      viewBox={`0 0 ${MESA.ancho} ${MESA.alto}`}
      style={{position: 'absolute', top: 0, left: 0, filter: SOMBRA_IMG}}
    >
      <rect
        x={CAJA.x}
        y={CAJA.y}
        width={CAJA.ancho}
        height={CAJA.alto}
        rx={CAJA.radio}
        fill="none"
        stroke={DT.colores.blanco}
        strokeWidth={CAJA.filete}
      />
      <path
        d={`M ${CAJA.x} ${CAJA.y + CAJA.alto / 2} L ${CAJA_DER} ${CAJA.y + CAJA.alto / 2}`}
        stroke={DT.colores.blanco}
        strokeWidth={CAJA.filete}
        strokeOpacity={0.45}
      />
      <path
        d={`M ${MESA.ancho / 2} ${CAJA.y} L ${MESA.ancho / 2} ${CAJA_PIE}`}
        stroke={DT.colores.blanco}
        strokeWidth={CAJA.filete}
        strokeOpacity={0.45}
      />
      {/* La regla del pie — de la referencia, al mismo ancho que la caja */}
      <path
        d={`M ${CAJA.x} ${REGLA_PIE} L ${CAJA_DER} ${REGLA_PIE}`}
        stroke={DT.colores.blanco}
        strokeWidth={CAJA.filete}
        strokeOpacity={0.7}
      />
    </svg>

    {/*
      6 · El logotipo de Hilton Honors — ronda 2, en la cajita que dibujó Eli.
      Sólo se dibuja si el archivo REAL está; ver la nota larga en `HONORS`.
    */}
    {conHonors ? (
      <Img
        src={staticFile(HONORS.archivo)}
        style={{
          position: 'absolute',
          top: HONORS.y,
          left: 0,
          width: MESA.ancho,
          height: HONORS.alto,
          objectFit: 'contain',
          filter: SOMBRA_IMG,
        }}
      />
    ) : null}

    {/*
      7 · El llamado. Texto LITERAL del brief, y NADA MÁS: no entra dirección,
      ni correo, ni legal. El brief no los pide y agregarlos sería inventar
      contenido — el mismo criterio de la historia del Día del Turismo.
    */}
    <div
      style={{
        position: 'absolute',
        left: 0,
        top: 1283,
        width: MESA.ancho,
        textAlign: 'center',
        fontFamily: DT.fuentes.titular,
        fontWeight: DT.pesos.regular,
        fontSize: CUERPO.pie,
        letterSpacing: '0.01em',
        color: DT.colores.blanco,
        textShadow: SOMBRA,
      }}
    >
      {PIE}
    </div>

    {/*
      8 · Guía de QA — sólo para revisar, NO se entrega.
      ⚠️ No dibuja zonas seguras de Instagram porque esto es FEED ORGÁNICO.
    */}
    {guia ? (
      <>
        {[
          {y: G.logoYFeed, alto: G.logoAncho / G.logoProporcion, c: 'rgba(255,0,110,0.75)'},
          {y: 597, alto: 777 - 597, c: 'rgba(0,200,255,0.75)'},
          {y: CAJA.y, alto: CAJA.alto, c: 'rgba(163,205,57,0.85)'},
          {y: HONORS.y, alto: HONORS.alto, c: 'rgba(255,120,255,0.9)'},
          {y: REGLA_PIE, alto: 1320 - REGLA_PIE, c: 'rgba(255,204,0,0.85)'},
        ].map((b) => (
          <div
            key={b.y}
            style={{
              position: 'absolute',
              top: b.y,
              left: 0,
              width: MESA.ancho,
              height: b.alto,
              border: `2px dashed ${b.c}`,
              boxSizing: 'border-box',
            }}
          />
        ))}
        <div
          style={{
            position: 'absolute',
            top: 0,
            left: MESA.ancho / 2,
            width: 1,
            height: MESA.alto,
            background: 'rgba(255,0,110,0.6)',
          }}
        />
        {[CAJA.x, CAJA_DER].map((x) => (
          <div
            key={x}
            style={{
              position: 'absolute',
              top: 0,
              left: x,
              width: 1,
              height: MESA.alto,
              background: 'rgba(255,255,255,0.45)',
            }}
          />
        ))}
      </>
    ) : null}
  </AbsoluteFill>
);

export const DtFtHonorsGuia: React.FC = () => <DtFtHonors guia />;
