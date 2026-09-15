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
 *     Texto en pantalla (Por cuadrante, acompañando al ícono):
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
 * No es un descuido de lectura: los otros dos existían y **el cliente los
 * TACHÓ** —«(Ícono señal wifi) WiFi Premium» y «(Ícono smartphone) Check-in
 * Digital»— junto con el titular viejo «BENEFICIOS / HILTON HONORS». La línea
 * del «6» quedó sin actualizar.
 *
 * Se arma con **4 cuadrantes (2×2)**, que es lo único que el brief permite:
 * poner 6 obligaría a inventar dos beneficios, y en esta cuenta el contenido no
 * es nuestro. **Queda informado en la entrega para que el cliente decida** si
 * quiere que vuelvan los dos tachados.
 *
 * ⛔ Y dos cosas más que el brief nombra y el banco no tiene, así que se toma la
 * alternativa que el propio brief ofrece en la misma frase:
 *   · **cenital** — no hay ninguna toma aérea del hotel («o angular elegante»);
 *   · **piscina** — el complejo no la tiene fotografiada («instalaciones, lobby
 *     o habitación»). Se usó el LOBBY.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA REFERENCIA: QUÉ SE TOMA Y QUÉ SE DEJA
 * ══════════════════════════════════════════════════════════════════════════
 * `REFERENCIAS S4 DT` (`13h9GWkz1cjGRFUfViUf1dMZTxJD55Fls`) trae dos archivos, y
 * el que manda es **`Ref post s4.jpg`, que Eli subió el 15-09 a las 13:43** — o
 * sea, para esta pieza. Es un folleto de hotel (LAAYAM Vagamone), y resulta ser
 * **el mismo pin que el brief enlaza en su celda LINKS**, sólo que a 736 px. Dos
 * fuentes independientes apuntando a la misma referencia: no hay ambigüedad.
 * Copia de trabajo a 1080×1350 en `raw/hilton/dt/ref-s4/`.
 *
 * SE TOMA (es la gramática que pidió Eli, y además es 4:5 como la pieza):
 *   · foto a sangre, protagonista, con fuga;
 *   · titular en **versales, alineado a la izquierda**, sobre la caja;
 *   · **caja de cristal con filete fino y cuadrantes divididos por hairlines**,
 *     cada uno con ícono de línea a la izquierda y rótulo a la derecha;
 *   · **regla fina al pie** separando el llamado.
 *
 * NO SE TOMA:
 *   · su sans geométrica → en DT el titular es **Stag** y el cuerpo **Trade**;
 *   · su pie con teléfono y marca → el brief pide una sola línea;
 *   · sus 6 cuadrantes → el brief dejó 4 (ver arriba);
 *   · su logotipo arriba a la izquierda → en DT el logo va CENTRADO, y su
 *     posición sale de la plantilla de márgenes de Eli, no de la referencia.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA GEOMETRÍA — MEDIDA, NO ESTIMADA
 * ══════════════════════════════════════════════════════════════════════════
 * ⭐ La referencia es 1080×1350 y la pieza también, así que su geometría se
 * traslada **1:1** en vez de proporcionalmente. Medido sobre el pin con realce
 * de línea fina (fila menos el promedio de las filas a ±3):
 *
 *   caja           x 100→980 (ancho **880**, centrada) · y 842→1148 (alto 306)
 *   divisor horiz. y ≈ 989  (mitad de la caja)
 *   titular        línea 1 y 662→710 · línea 2 y 730→777 · x desde 116
 *                  altura de versal **49**, salto entre líneas **68**
 *   regla del pie  y ≈ 1258
 *   pie            y 1296→1313
 *
 * ⚠️ El titular de la referencia arranca en x=116 y su caja en x=100: son 16 px
 * de desfase que es puro prosa de la letra. Acá los dos se alinean a **100**.
 *
 * ⭐⭐ **Y la caja de la referencia (880) es MÁS ANCHA que el panel medido de DT
 * (730 en `DT FT S3`).** Se adopta el 880 de la referencia, por dos razones:
 *   1. es el precedente de esta misma cuenta — en la historia del Día del
 *      Turismo, cuando la referencia y el panel de DT no coincidían, Eli pidió
 *      «hazlo más similar a la referencia» y se adoptó la medida del pin;
 *   2. con 730 los cuadrantes quedan de 365 y «Acumula puntos en cada estadía»
 *      no entra sin partirse en tres líneas.
 *
 * ⛔ **LA CAJA VA DE CRISTAL, NO OPACA — y eso NO es apartarse de DT.** Medido,
 * el panel de `DT FT S3` es prácticamente macizo (α ≈ 0,84 en el cuerpo y 0,90
 * en la fila de íconos sobre `#09194E`). Acá va en **0,30** porque el brief lo
 * pide con todas sus letras —«estilo cristal o translúcida»— y la referencia
 * hace exactamente eso. El contenedor de DT sigue siendo el mismo objeto
 * (esquinas redondeadas + filete blanco + divisor interior); lo que cambia es su
 * densidad, y la manda el brief.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LAS TINTAS — MEDIDAS POR TERCIOS SOBRE LA FOTO YA RECORTADA
 * ══════════════════════════════════════════════════════════════════════════
 * Regla `la-tinta-la-manda-el-fondo`: luminancia por tercios de la banda y manda
 * el peor tercio. Con el velo azul de DT ya aplicado (`dt-ft-honors-foto.py`):
 *
 * | banda | α velo | blanco | azul DT |
 * |---|---|---|---|
 * | logotipo  (111-241) | 0,14 | 3,48:1 ⛔ | **4,59:1 ✅** |
 * | titular   (592-777) | 0,48 | **7,94:1 ✅** | 2,01:1 |
 * | caja      (842-1148)| 0,55 | **7,64:1 ✅** | 2,09:1 |
 * | pie       (1240-1320)| 0,58 | **9,66:1 ✅** | 1,65:1 |
 *
 * ⭐ **El logotipo va AZUL.** No es gusto: cae sobre el cielorraso blanco del
 * lobby y el blanco no llega a 4,5. Es la §B.4 del manual —«va en azul
 * DoubleTree cuando el fondo es demasiado blanco y el logo se pierde»— y el
 * mismo caso, por la misma medición, que la historia del Día del Turismo.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * EL TITULAR
 * ══════════════════════════════════════════════════════════════════════════
 * Texto LITERAL del brief, partido en tres líneas por corte semántico —la
 * promesa arriba, la condición abajo— y nunca por lo que caiga:
 *
 *     MÁS BENEFICIOS          ← Stag **Medium**
 *     EN CADA ESTADÍA         ← Stag **Light**
 *     CON HILTON HONORS       ← Stag **Light**
 *
 * Es el recurso de DT de siempre: **dos pesos de la misma familia a un mismo
 * cuerpo** (corregido con Eli el 10-09: «me refería al tamaño de la tipografía,
 * no a cambiar el grosor»), con la línea corta arriba.
 *
 * Cuerpo 68 ⇒ versal 47,6, contra los 49 de la referencia. Medido en Stag a
 * cuerpo 100: `CON HILTON HONORS` da 1015 px, o sea **690 a cuerpo 68**, más el
 * tracking = 736 — entra en los 880 de la caja con aire a los dos lados.
 *
 * ⛔ Verificado glifo a glifo con `fontTools`: el titular no lleva `¡` `¿` `$`
 * `%` ni nada de lo que a Stag le falta. **No hace falta `volteaApertura()`**.
 * `Á` e `Í` sí están en los 354 glifos.
 *
 * ⚠️ El brief dice «Zona superior izquierda» y la referencia pone su titular al
 * 49 % de la altura, a la izquierda, justo encima de la caja. Se siguió **la
 * referencia**, que es lo que Eli mandó hoy para esta pieza; el titular queda a
 * la IZQUIERDA como pide el brief, y arriba de la caja. Queda anotado en la
 * entrega por si ella lo quiere más arriba.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LA REJILLA (mesa 1080×1350; se entrega a 2250, ×2,0833)
 * ══════════════════════════════════════════════════════════════════════════
 *    111 ─ tope del logotipo   ← plantilla `logo-post.png` de Eli
 *    242 ─ pie del logotipo
 *    597 ─ tope de la tinta del titular     = 44,2 %
 *    777 ─ pie de la tinta del titular      (la referencia: 777)
 *    842 ─ tope de la caja de cristal
 *    995 ─ divisor horizontal
 *   1148 ─ pie de la caja
 *   1258 ─ regla del pie
 *   1296 ─ tinta del llamado
 *
 * ⚠️ Esto es FEED ORGÁNICO: **no hay zona segura de Instagram** que reservar —
 * las de 250/340 px son de historia. Las de Meta Ads sólo valdrían si esta pieza
 * se pautara, y la grilla no lo dice.
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
 * La caja de cristal. Medidas del pin, que es 1080×1350 igual que la pieza.
 */
const CAJA = {
  x: 100,
  ancho: 880,
  y: 842,
  alto: 306,
  /** Radio del pin y del panel de `DT FT S3`, que coinciden en el mismo orden. */
  radio: 26,
  /** Filete de 1 px, blanco pleno — igual que en la historia del Día del Turismo. */
  filete: 1,
  /** Ver el encabezado: el brief pide «estilo cristal o translúcida». */
  relleno: 0.30,
} as const;

const CAJA_DER = CAJA.x + CAJA.ancho;
const CAJA_PIE = CAJA.y + CAJA.alto;

/** Regla fina del pie y el llamado, calcados de la referencia. */
const REGLA_PIE = 1258;

/**
 * Cuerpos.
 *
 * · `titulo: 68` ⇒ versal 47,6 (Stag da cap = 0,700 × cuerpo, medido). La
 *   referencia lleva 49.
 * · `rotulo: 29` — medido, el rótulo más largo partido en dos («Canje de
 *   noches» 209 px) entra en los 300 px de columna con aire.
 * · `pie: 29` ⇒ «Inscríbete gratis en el link de la bio» da 434 px.
 */
const CUERPO = {titulo: 68, rotulo: 29, pie: 29} as const;

/**
 * Salto entre líneas del titular: 66 px sobre una versal de 47,6 ⇒ 1,39 de
 * versal, que es exactamente la proporción del pin (68 / 49 = 1,39).
 */
const SALTO_TITULO = 66;

/**
 * ⚠️ Los cortes de línea de los rótulos van A MANO, como en la referencia: dos
 * líneas por cuadrante, la corta arriba. Dejados al navegador caen desparejos y
 * «gratis» queda de palabra viuda.
 */
type Celda = {icono: React.ReactNode; rotulo: readonly [string, string]};

/** Trazo de los íconos: fino, blanco, y que NO engorde al escalar a 2250. */
const trazo = {
  fill: 'none',
  stroke: DT.colores.blanco,
  strokeWidth: 2,
  strokeLinecap: 'round' as const,
  strokeLinejoin: 'round' as const,
  vectorEffect: 'non-scaling-stroke' as const,
};

const Icono: React.FC<{children: React.ReactNode}> = ({children}) => (
  <svg width={62} height={62} viewBox="0 0 64 64" style={{flexShrink: 0}}>
    <g {...trazo}>{children}</g>
  </svg>
);

/**
 * Los cuatro íconos. **El brief nombra cada uno**, así que no se eligen: se
 * dibujan los que pide, en línea fina, que es el estilo de la referencia.
 *
 *   «etiqueta de descuento» → la etiqueta con su ojal
 *   «cama o flecha arriba»  → la cama
 *   «luna o regalo»         → la luna
 *   «moneda o puntos»       → las monedas apiladas (es lo que dice «acumula»)
 */
const CELDAS: readonly Celda[] = [
  {
    icono: (
      <>
        <path d="M6 30 L28 8 Q30 6 33 6 L52 6 Q58 6 58 12 L58 31 Q58 34 56 36 L34 58 Q31 61 28 58 L6 36 Q3 33 6 30 Z" />
        <circle cx="46" cy="18" r="4.5" />
      </>
    ),
    rotulo: ['Tarifas', 'exclusivas'],
  },
  {
    icono: (
      <>
        <path d="M7 48 V22 a4 4 0 0 1 4-4 h12 a4 4 0 0 1 4 4 v5" />
        <rect x="7" y="33" width="50" height="15" rx="5" />
        <rect x="12" y="23" width="14" height="10" rx="3.5" />
        <path d="M11 48 v6 M53 48 v6" />
      </>
    ),
    rotulo: ['Upgrades de', 'habitación'],
  },
  {
    icono: <path d="M38 8 A24 24 0 1 0 56 42 A19 19 0 1 1 38 8 Z" />,
    rotulo: ['Canje de noches', 'gratis'],
  },
  {
    icono: (
      <>
        <ellipse cx="32" cy="17" rx="21" ry="8.5" />
        <path d="M11 17 v9 a21 8.5 0 0 0 42 0 v-9" />
        <path d="M11 26 v9 a21 8.5 0 0 0 42 0 v-9" />
        <path d="M11 35 v9 a21 8.5 0 0 0 42 0 v-9" />
      </>
    ),
    rotulo: ['Acumula puntos', 'en cada estadía'],
  },
];

/**
 * ⚠️ Los cuadrantes se llenan en Z —arriba izquierda, arriba derecha, abajo
 * izquierda, abajo derecha— **en el orden en que el brief lista los rótulos**,
 * que no se altera:
 *
 *     Tarifas exclusivas   |  Upgrades de habitación
 *     Canje de noches      |  Acumula puntos en cada estadía
 *
 * Y de paso la lectura queda pareja: arriba lo que se disfruta EN la estadía,
 * abajo lo que se acumula y se canjea.
 */

const Cuadrante: React.FC<{celda: Celda}> = ({celda}) => (
  <div
    style={{
      width: CAJA.ancho / 2,
      height: CAJA.alto / 2,
      display: 'flex',
      alignItems: 'center',
      gap: 22,
      paddingLeft: 36,
      paddingRight: 24,
      boxSizing: 'border-box',
    }}
  >
    <Icono>{celda.icono}</Icono>
    <div
      style={{
        fontFamily: DT.fuentes.texto,
        fontWeight: 400,
        fontSize: CUERPO.rotulo,
        lineHeight: 1.22,
        color: DT.colores.blanco,
      }}
    >
      {celda.rotulo.map((l) => (
        <div key={l}>{l}</div>
      ))}
    </div>
  </div>
);

export const DtFtHonors: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: DT.colores.azul}}>
    {/* 1 · La foto real del lobby, a sangre. Nada generado (`no-generar-producto-que-existe`). */}
    <Img
      src={staticFile('assets/hilton/dt/ft-honors-lobby.jpg')}
      style={{width: '100%', height: '100%', objectFit: 'cover'}}
    />

    {/*
      2 · El velo azul de DT.

      Es la MISMA rampa que Eli aprobó en la historia del Día del Turismo: nace
      en **0 en el borde de arriba** y sube cóncava hasta 0,58 al pie, con
      paradas cada ~10 % para que no quede ningún quiebre a la vista.

      ⛔ El error a no repetir (ronda 4 de esa historia): dejarlo PLANO en 0 una
      franja y hacerlo arrancar de golpe más abajo. Ese codo se lee como una
      máscara pegada encima de la foto — «se ve muy forzado».
    */}
    <AbsoluteFill
      style={{
        background:
          `linear-gradient(to bottom,` +
          ` rgba(9,25,78,0) 0%,` +
          ` rgba(9,25,78,0.11) 10%,` +
          ` rgba(9,25,78,0.22) 20%,` +
          ` rgba(9,25,78,0.33) 30%,` +
          ` rgba(9,25,78,0.42) 40%,` +
          ` rgba(9,25,78,0.48) 50%,` +
          ` rgba(9,25,78,0.52) 60%,` +
          ` rgba(9,25,78,0.55) 72%,` +
          ` rgba(9,25,78,0.57) 86%,` +
          ` rgba(9,25,78,0.58) 100%)`,
      }}
    />

    {/*
      3 · Logotipo principal, CENTRADO y en AZUL DoubleTree (§B.4: el cielorraso
      del lobby es demasiado claro para el blanco — 3,48:1 contra 4,59:1).
      Geometría de la plantilla `logo-post.png` de Eli: ancho 160, tope 111.
      Se escala UNIFORME desde su proporción real 1,2254 — nunca por geometría.
    */}
    <Img
      src={staticFile('assets/hilton/dt/logo-dt-azul.png')}
      style={{
        position: 'absolute',
        top: G.logoYFeed,
        left: (MESA.ancho - G.logoAncho) / 2,
        width: G.logoAncho,
        height: G.logoAncho / G.logoProporcion,
      }}
    />

    {/*
      4 · El titular, alineado a la IZQUIERDA sobre el canto de la caja.

      El bloque se ancla por su PIE (`bottom`) y no por su tope: así la tinta
      cierra en 777 —donde la cierra la referencia— sin depender de cuántas
      líneas tenga el titular. Los 65 px hasta la caja son los del pin.
    */}
    <div
      style={{
        position: 'absolute',
        left: CAJA.x,
        bottom: MESA.alto - 777,
        width: CAJA.ancho,
        fontFamily: DT.fuentes.titular,
        fontSize: CUERPO.titulo,
        lineHeight: SALTO_TITULO / CUERPO.titulo,
        letterSpacing: '0.035em',
        color: DT.colores.blanco,
      }}
    >
      {TITULO.map(({t, peso}) => (
        <div key={t} style={{fontWeight: peso, whiteSpace: 'nowrap'}}>
          {t}
        </div>
      ))}
    </div>

    {/*
      5 · La caja de cristal. El relleno va aparte del filete porque el filete es
      de 1 px real de la mesa y tiene que seguir siendo de 1 px al escalar a
      2250 — por eso el borde se dibuja en SVG con `non-scaling-stroke` y no con
      un `border` de CSS, que sí engorda.
    */}
    <div
      style={{
        position: 'absolute',
        left: CAJA.x,
        top: CAJA.y,
        width: CAJA.ancho,
        height: CAJA.alto,
        borderRadius: CAJA.radio,
        background: `rgba(9,25,78,${CAJA.relleno})`,
      }}
    />

    {/* 5b · Los cuatro cuadrantes */}
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
      5c · El filete y los divisores, en SVG.

      ⚠️ Los divisores van más tenues que el contorno (0,45 contra 1). En la
      referencia pasa lo mismo: el marco cierra la caja y las líneas de adentro
      sólo separan, no dibujan. Con los dos al mismo peso la caja se lee como una
      tabla y pierde el aire de cristal.
    */}
    <svg
      width={MESA.ancho}
      height={MESA.alto}
      viewBox={`0 0 ${MESA.ancho} ${MESA.alto}`}
      style={{position: 'absolute', top: 0, left: 0}}
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
        vectorEffect="non-scaling-stroke"
      />
      {/* divisor horizontal, a media caja */}
      <path
        d={`M ${CAJA.x} ${CAJA.y + CAJA.alto / 2} L ${CAJA_DER} ${CAJA.y + CAJA.alto / 2}`}
        stroke={DT.colores.blanco}
        strokeWidth={CAJA.filete}
        strokeOpacity={0.45}
        vectorEffect="non-scaling-stroke"
      />
      {/* divisor vertical, al eje */}
      <path
        d={`M ${MESA.ancho / 2} ${CAJA.y} L ${MESA.ancho / 2} ${CAJA_PIE}`}
        stroke={DT.colores.blanco}
        strokeWidth={CAJA.filete}
        strokeOpacity={0.45}
        vectorEffect="non-scaling-stroke"
      />
      {/* regla del pie — calcada de la referencia, al mismo ancho que la caja */}
      <path
        d={`M ${CAJA.x} ${REGLA_PIE} L ${CAJA_DER} ${REGLA_PIE}`}
        stroke={DT.colores.blanco}
        strokeWidth={CAJA.filete}
        strokeOpacity={0.55}
        vectorEffect="non-scaling-stroke"
      />
    </svg>

    {/*
      6 · El llamado. Texto LITERAL del brief, y NADA MÁS: no entra dirección,
      ni correo, ni legal. El brief no los pide y agregarlos sería inventar
      contenido — el mismo criterio con el que se resolvió la historia del Día
      del Turismo.
    */}
    <div
      style={{
        position: 'absolute',
        left: 0,
        top: 1283,
        width: MESA.ancho,
        textAlign: 'center',
        fontFamily: DT.fuentes.texto,
        fontWeight: 400,
        fontSize: CUERPO.pie,
        letterSpacing: '0.01em',
        color: DT.colores.blanco,
      }}
    >
      {PIE}
    </div>

    {/*
      7 · Guía de QA — sólo para revisar, NO se entrega. Dibuja las bandas
      medidas para poder comparar contra la referencia de un vistazo.

      ⚠️ No dibuja zonas seguras de Instagram porque esto es FEED ORGÁNICO: las
      de 250/340 px son de historia y las de Meta Ads sólo valen si se pauta.
    */}
    {guia ? (
      <>
        {[
          {y: G.logoYFeed, alto: G.logoAncho / G.logoProporcion, c: 'rgba(255,0,110,0.75)'},
          {y: 597, alto: 777 - 597, c: 'rgba(0,200,255,0.75)'},
          {y: CAJA.y, alto: CAJA.alto, c: 'rgba(163,205,57,0.85)'},
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
        {/* el eje y el margen de 100 */}
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
