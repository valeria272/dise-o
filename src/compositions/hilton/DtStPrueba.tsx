/**
 * DOUBLETREE — HISTORIA DE PRUEBA · «Escapada Romántica»
 *
 * ⚠️⚠️ ESTO **NO** ES UNA PIEZA DE GRILLA. Es el banco de pruebas que pidió Eli
 * el 17-09-2026 para ver si se puede mejorar una edición suya de Premiere desde
 * código: «mejorar la edición de esa historia de prueba... no cambies nada de
 * grilla es para hacer prueba antes de seguir. No es para grilla.»
 *
 * El original vive en
 * `F:\Carpeta de grillas Hilton 2026\SEPTIEMBRE\DT\S5\ST PRUEBA PARA CLOUDE CODE\
 *  ST PRUEBA CLOUDE.prproj` y es a su vez una copia de la ST n°2 de la S2.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * DE DÓNDE SALEN LOS DATOS — leídos del .prproj, no estimados
 * ══════════════════════════════════════════════════════════════════════════
 * El `.prproj` es XML comprimido con gzip. Se descomprimió y se resolvieron las
 * referencias de objeto para sacar la línea de tiempo exacta, y los textos se
 * decodificaron del base64 del parámetro «Texto de origen» de cada gráfico.
 *
 * Mesa 1080×1920 · **9,64 s** · 8 pistas de video · **0 keyframes en todo el
 * proyecto**.
 *
 * | pista | objeto | in→out (s) | qué |
 * |---|---|---|---|
 * | V1 | 111 | 0,00→3,00 | foto cama + macarons |
 * | V1 | 112 | 3,00→5,24 | foto bar |
 * | V1 | 113 | 5,24→9,64 | foto desayuno |
 * | V2 | 114 | 0,00→5,24 | «Escápate en pareja» · transición **Animador de texto** 0,00→1,00 |
 * | V2 | 115 | 5,24→9,64 | «Escapada Romántica» · **sin transición** |
 * | V3 | 117 | 0,00→5,24 | «Habitación para dos» · **Máquina de escribir** 0,00→0,96 |
 * | V4 | 119 | 0,52→3,00 | «+Botella de espumante.» · **Máquina de escribir** 0,52→1,52 |
 * | V4 | 120 | 5,24→9,64 | «Incluye desayuno buffet para dos.» · **Máquina de escribir** 5,24→6,24 |
 * | V5 | 123 | 0,00→9,64 | logotipo DT |
 * | V6 | 124 | 0,00→9,64 | «Deslizar para reservar» |
 * | V7 | 125 | 0,00→9,64 | `image (26).png` — **guía de zona segura de Reels**, no es contenido |
 * | V8 | 126 | 1,00→9,64 | «desde $99.000 IVA Inc.» (Trade Gothic BdCn20) |
 *
 * ⛔ **LOS TEXTOS VAN LITERALES** (§G: en DT sólo se DISEÑA). No se corrigió el
 * punto final de «+Botella de espumante.» ni se tocó el «+». La edición es lo
 * único que cambia.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LOS SIETE PROBLEMAS DE LA EDICIÓN ACTUAL
 * ══════════════════════════════════════════════════════════════════════════
 * 1 · **El corte de foto de los 3,00 s es mudo.** Ningún texto cambia ahí: el
 *     titular y «Habitación para dos» siguen hasta 5,24 y cruzan por encima de
 *     DOS fotos. La historia se parte en 5,24 + 4,40 con un corte gratis al
 *     medio.
 * 2 · **Los incluidos caen sobre la foto equivocada.** «+Botella de espumante.»
 *     va de 0,52 a 3,00 — o sea sobre la CAMA — y la foto del BAR, que es
 *     justamente la del espumante, se queda sin texto propio. Es el hallazgo
 *     grande: el orden de fotos de Eli ya cuenta la historia bien y la edición
 *     no lo respeta.
 * 3 · **Cero movimiento.** 0 keyframes en el proyecto: las tres fotos están
 *     clavadas. Lo único que se mueve en 9,6 s es la tipografía.
 * 4 · **Cuatro transiciones y tres son la misma.** Máquina de escribir ×3 —el
 *     preset más reconocible de Premiere— y es lineal: con 1,00 s fijo escribe
 *     «Habitación para dos» (19 caracteres) y «Incluye desayuno buffet para
 *     dos.» (33) a cadencias muy distintas.
 * 5 · **Tres animaciones encimadas en el primer segundo y medio** (0,00–1,00 ·
 *     0,00–0,96 · 0,52–1,52) y después **nada** hasta 5,24.
 * 6 · **Ningún texto tiene salida.** Los seis cortan seco al terminar su clip.
 *     Entran con gracia y desaparecen de golpe.
 * 7 · **El segundo titular aparece sin animación.** El clip 115 no tiene
 *     transición: «Escapada Romántica» hace *pop* en el frame de 5,24.
 *
 * (Y una octava, que es de export y no de edición: `image (26).png` en V7 es la
 * guía de zona segura de Reels, opaca y por encima de casi todo. Va apagada al
 * exportar.)
 *
 * ══════════════════════════════════════════════════════════════════════════
 * LO QUE CAMBIA EN LA VERSIÓN NUEVA — y lo que NO
 * ══════════════════════════════════════════════════════════════════════════
 * **Igual en las dos:** las fotos, los textos, la tipografía, el color, el
 * velo, la posición del logotipo y la diagramación del bloque. Se dejaron
 * idénticas A PROPÓSITO, para que la comparación aísle exactamente lo que ella
 * preguntó: la edición y las transiciones.
 *
 * **Distinto:**
 * · El corte de los 3,00 s pasa a llevar un cambio de texto — «Habitación para
 *   dos» releva a «+Botella de espumante.» justo cuando entra el bar. Cada
 *   incluido cae sobre la foto que lo muestra: cama → habitación, bar →
 *   espumante, desayuno → desayuno.
 * · Las tres fotos llevan cámara lenta con frenada (`CAMARA`), el mismo recurso
 *   del carrusel de la S5.
 * · Los cortes secos pasan a disolvencia de 10 fotogramas.
 * · Las cuatro transiciones enlatadas salen. Entra el recurso de la casa:
 *   fundido + subida con retardo (`usaEntrada`), escalonado por línea.
 * · Cada texto ahora tiene SALIDA.
 * · La CTA y el precio ya no arrancan encima del titular: entran después, que
 *   es el orden en que se lee una oferta.
 *
 * ══════════════════════════════════════════════════════════════════════════
 * MEDICIONES (el velo y las tintas, regla `la-tinta-la-manda-el-fondo`)
 * ══════════════════════════════════════════════════════════════════════════
 * Luminancia por tercios de la columna del texto, manda el tercio más CLARO.
 * **Sin velo, la tinta blanca no da**: en la foto de la cama el plumón blanco
 * deja el bloque bajo en **1,59–1,69:1** contra varas de 3:1 (titular) y 4,5:1
 * (subtexto).
 *
 * Con la rampa APROBADA de la ST del Día del Turismo (0 arriba → 0,58 al pie,
 * cóncava) las tres fotos pasan con margen:
 *
 * |  | titular | incluido | precio | CTA |
 * |---|---|---|---|---|
 * | cama     | 5,98 | 5,41 | 5,69 | 5,52 |
 * | bar      | 8,18 | 8,68 | 8,57 | 12,56 |
 * | desayuno | 7,47 | 6,49 | 6,51 | 7,15 |
 *
 * No se cargó más el velo aunque se probaron rampas de 0,73 y 0,80: la
 * aprobada ya pasa, y «un velo que tapa la foto contradice el encargo».
 *
 * ⚠️ **LO QUE NO SE PUDO RESOLVER Y QUEDA PARA ELI:** el LOGOTIPO cae en
 * **4,13–5,09:1** sobre las tres fotos, bajo el 6,7–9,3 que pide §B.4. La rampa
 * de DT nace en 0 arriba y ahí el logo no recibe ayuda. Para llegar a 6,7 haría
 * falta α ≈ 0,36–0,46 en la banda del logo, o sea un velo superior de verdad —
 * y eso contradice la regla del velo que aprobó Eli. Cambiar la regla no lo
 * decide una pieza de prueba. En azul es peor (3,13–3,86:1). Queda medido y
 * dicho.
 *
 * ⛔ **Y UN HALLAZGO DE TIPOGRAFÍA, verificado glifo a glifo con fontTools:
 * STAG NO TRAE EL SIGNO `+`.** Los nueve cortes comparten el mismo subconjunto
 * de 354 glifos y a todos les falta `U+002B` (además de `$ % @ € º ª # *`, que
 * ya estaba documentado). O sea que «+Botella de espumante.» en Stag-Regular
 * **no puede dibujar su primer carácter**: PIL lo come entero. En Premiere se
 * verá con la fuente de reemplazo que elija el sistema, que no es Stag. Acá el
 * `+` se compone en **Trade Gothic**, que sí lo trae — la misma salida que ya
 * usa la marca para el `$` del precio y para `¡`/`¿` con `volteaApertura()`.
 */
import React from 'react';
import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
} from 'remotion';

import {DT, cargarFuentesDT} from '../../brand/doubletree';

cargarFuentesDT();

// ───────────────────────────────────────────────────────────────────────────
// Constantes
// ───────────────────────────────────────────────────────────────────────────

/** 9,64 s a 30 fps — la duración exacta del proyecto de Premiere. */
export const DURACION = 289;

const MARGEN = DT.geometria.margenLateral; // 88 @1080
const SOMBRA = '0 2px 7px rgba(9,25,78,0.60), 0 0 2px rgba(9,25,78,0.45)';

const FOTO = {
  cama: staticFile('assets/hilton/dt/prueba-st/1-cama.jpg'),
  bar: staticFile('assets/hilton/dt/prueba-st/2-bar.png'),
  desayuno: staticFile('assets/hilton/dt/prueba-st/3-desayuno.png'),
};
const LOGO = staticFile('assets/hilton/dt/prueba-st/logo-st.png');

/** Los cortes del original, en fotogramas: 3,00 s y 5,24 s. */
const CORTE_1 = 90;
const CORTE_2 = 157;

/**
 * El velo APROBADO de la ST del Día del Turismo: nace en 0 arriba y sube
 * cóncavo hasta 0,58 al pie. Paradas cada 10 % para que no quede ningún codo a
 * la vista — el error de la ronda 4 que Eli marcó como «forzado».
 */
const VELO: readonly (readonly [number, number])[] = [
  [0, 0], [10, 0.11], [20, 0.22], [30, 0.33], [40, 0.42], [50, 0.48],
  [60, 0.52], [70, 0.55], [80, 0.57], [90, 0.58], [100, 0.58],
];

const rampa = (paradas: readonly (readonly [number, number])[]) =>
  `linear-gradient(to bottom, ${paradas
    .map(([p, a]) => `rgba(9,25,78,${a}) ${p}%`)
    .join(', ')})`;

/** Frenada del carrusel de la S5: llega y se queda quieta. */
const CAMARA = Easing.bezier(0.16, 0.62, 0.24, 1);
/** Suavizado de las entradas de texto. */
const ENTRADA = Easing.bezier(0.22, 0.9, 0.3, 1);

// ───────────────────────────────────────────────────────────────────────────
// Diagramación — IDÉNTICA en las dos versiones
// ───────────────────────────────────────────────────────────────────────────

/**
 * Zonas seguras de historia: 250 arriba, 340 abajo (`DT.seguras.story`), o sea
 * que el bloque tiene que cerrar antes de y=1580. Cierra en 1564.
 *
 * El logotipo va donde lo pone la plantilla de márgenes de Eli (`logo-ST.png`):
 * ancho 167, tope 241, centrado, a su proporción real 1,2254 — se escala
 * uniforme, jamás por geometría. Y va SIN sombra (ronda 3 del estático).
 */
const Y = {
  incluido: 1223,
  precio: 1308,
  cta: 1494,
} as const;

/**
 * ⭐ LOS DOS TITULARES VAN A UNA MISMA MEDIDA (840 px), y el cuerpo es la
 * consecuencia — el criterio que dictó Eli el 15-09 para un titular de varias
 * líneas, aplicado acá entre los dos tiempos de la historia. A cuerpo igual
 * medirían 773 y 872 px y el cambio de titular se leería como un salto de
 * tamaño; a medida igual se lee como un relevo.
 *
 * ⚠️ Cuerpos calculados con PIL y CORREGIDOS contra el render, porque «Chrome
 * compone Stag más angosto que PIL» y el cálculo sobre el .ttf deja la medida
 * corta.
 */
const TITULARES = {
  a: {fuerte: 'Escápate', suave: ' en pareja', cuerpo: 106, top: 1057},
  b: {fuerte: 'Escapada', suave: ' Romántica', cuerpo: 94, top: 1070},
} as const;

const Titular: React.FC<{
  cual: keyof typeof TITULARES;
  estilo: React.CSSProperties;
}> = ({cual, estilo}) => {
  const t = TITULARES[cual];
  return (
    <div
      style={{
        position: 'absolute',
        left: MARGEN,
        width: 1080 - MARGEN * 2,
        top: t.top,
        textAlign: 'center',
        fontFamily: DT.fuentes.titular,
        fontStyle: 'italic',
        fontSize: t.cuerpo,
        lineHeight: 1.18,
        color: DT.colores.blanco,
        textShadow: SOMBRA,
        whiteSpace: 'nowrap',
        ...estilo,
      }}
    >
      {/* Dos pesos de la misma familia — el recurso de DT. */}
      <span style={{fontWeight: DT.pesos.medium}}>{t.fuerte}</span>
      <span style={{fontWeight: DT.pesos.regular}}>{t.suave}</span>
    </div>
  );
};

/**
 * Un incluido. El `+` se compone en Trade Gothic porque **Stag no lo trae**
 * (ver cabecera). El resto va en Stag Regular, como en el gráfico original.
 */
const Incluido: React.FC<{texto: string; estilo: React.CSSProperties}> = ({
  texto,
  estilo,
}) => {
  const mas = texto.startsWith('+');
  const resto = mas ? texto.slice(1) : texto;
  return (
    <div
      style={{
        position: 'absolute',
        left: MARGEN,
        width: 1080 - MARGEN * 2,
        top: Y.incluido,
        textAlign: 'center',
        fontFamily: DT.fuentes.titular,
        fontWeight: DT.pesos.regular,
        fontSize: 44,
        lineHeight: 1.25,
        color: DT.colores.blanco,
        textShadow: SOMBRA,
        whiteSpace: 'nowrap',
        ...estilo,
      }}
    >
      {mas ? (
        <span style={{fontFamily: DT.fuentes.texto, fontWeight: 400}}>+</span>
      ) : null}
      {resto}
    </div>
  );
};

/**
 * El precio. Va entero en Trade Gothic —el `$` tampoco existe en Stag— y la
 * cifra en el Bold Condensed No. 20, que es el corte que declara el gráfico
 * original (`TradeGothicLTStd-BdCn20`).
 */
const Precio: React.FC<{estilo: React.CSSProperties}> = ({estilo}) => (
  <div
    style={{
      position: 'absolute',
      left: MARGEN,
      width: 1080 - MARGEN * 2,
      top: Y.precio,
      display: 'flex',
      alignItems: 'baseline',
      justifyContent: 'center',
      gap: 18,
      color: DT.colores.blanco,
      textShadow: SOMBRA,
      ...estilo,
    }}
  >
    <span style={{fontFamily: DT.fuentes.texto, fontSize: 34, letterSpacing: 0.5}}>
      desde
    </span>
    <span style={{fontFamily: "'Trade Gothic Cn', sans-serif", fontSize: 116}}>
      $99.000
    </span>
    <span style={{fontFamily: DT.fuentes.texto, fontSize: 28, letterSpacing: 0.5}}>
      IVA Inc.
    </span>
  </div>
);

/**
 * La CTA. Píldora blanca maciza con tinta azul: sobre foto con velo, una
 * píldora sólida es lo que la hace leerse como botón — el mismo criterio del
 * carrusel de la S5.
 */
const Cta: React.FC<{estilo: React.CSSProperties}> = ({estilo}) => (
  <div
    style={{
      position: 'absolute',
      left: 0,
      width: 1080,
      top: Y.cta,
      display: 'flex',
      justifyContent: 'center',
      ...estilo,
    }}
  >
    <div
      style={{
        background: DT.colores.blanco,
        color: DT.colores.azul,
        borderRadius: 34,
        padding: '15px 40px',
        fontFamily: DT.fuentes.titular,
        fontWeight: DT.pesos.regular,
        fontSize: 34,
        lineHeight: 1.1,
        whiteSpace: 'nowrap',
      }}
    >
      Deslizar para reservar
    </div>
  </div>
);

/**
 * ⭐ `logo ST.png` NO ES UN LOGOTIPO: es la PLANTILLA DE MÁRGENES de Eli. El
 * archivo mide 2250×4000 —el lienzo de entrega de una historia— y el logotipo
 * ocupa apenas 348×284 px dentro de él, en (951, 502). Es la misma trampa del
 * PNG de Piso18 (memoria `png-de-logo-puede-ser-plantilla`).
 *
 * Por eso NO se recorta ni se escala a un ancho: se dibuja la plantilla ENTERA
 * a mesa completa, y el logotipo cae solo donde ella lo puso. Comprobado — el
 * bbox del alfa, llevado a 1080×1920, da ancho **167,0**, tope **241,0** y
 * centro **540**: exactamente la geometría medida en `doubletree.ts`.
 *
 * Va SIN sombra (ronda 3 del estático de Honors).
 */
const Logotipo: React.FC = () => (
  <Img src={LOGO} style={{position: 'absolute', left: 0, top: 0, width: 1080, height: 1920}} />
);

const Velo: React.FC = () => (
  <AbsoluteFill style={{background: rampa(VELO)}} />
);

// ───────────────────────────────────────────────────────────────────────────
// ANTES — reconstrucción fiel del proyecto de Premiere
// ───────────────────────────────────────────────────────────────────────────

/**
 * La máquina de escribir de Premiere: revelado carácter a carácter a cadencia
 * CONSTANTE. Se reconstruye tal cual —incluida su linealidad, que es justo lo
 * que se nota— para que la comparación sea honesta.
 */
const maquinaDeEscribir = (frame: number, desde: number, dura: number, largo: number) => {
  const t = interpolate(frame, [desde, desde + dura], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return Math.round(t * largo);
};

const conCorte = (frame: number, desde: number, hasta: number): boolean =>
  frame >= desde && frame < hasta;

export const DtStPruebaAntes: React.FC = () => {
  const frame = useCurrentFrame();

  /** Cortes secos, sin movimiento — 0 keyframes en el original. */
  const foto = frame < CORTE_1 ? FOTO.cama : frame < CORTE_2 ? FOTO.bar : FOTO.desayuno;

  /** «Animador de texto», 0,00→1,00 s: fundido + escala, en bloque. */
  const animador = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const t1 = 'Habitación para dos';
  const t2 = '+Botella de espumante.';
  const t3 = 'Incluye desayuno buffet para dos.';

  return (
    <AbsoluteFill style={{backgroundColor: DT.colores.azul}}>
      <Img src={foto} style={{width: 1080, height: 1920, objectFit: 'cover'}} />
      <Velo />
      <Logotipo />

      {/* V2 · 0,00→5,24 · «Animador de texto» */}
      {conCorte(frame, 0, CORTE_2) ? (
        <Titular
          cual="a"
          estilo={{opacity: animador, transform: `scale(${0.94 + 0.06 * animador})`}}
        />
      ) : null}

      {/* V2 · 5,24→9,64 · SIN transición: aparece de golpe */}
      {conCorte(frame, CORTE_2, DURACION) ? <Titular cual="b" estilo={{}} /> : null}

      {/* V3 · 0,00→5,24 · «Máquina de escribir» 0,00→0,96 */}
      {conCorte(frame, 0, CORTE_2) ? (
        <Incluido texto={t1.slice(0, maquinaDeEscribir(frame, 0, 29, t1.length))} estilo={{}} />
      ) : null}

      {/* V4 · 0,52→3,00 · «Máquina de escribir» 0,52→1,52 — sobre la CAMA */}
      {conCorte(frame, 16, CORTE_1) ? (
        <Incluido
          texto={t2.slice(0, maquinaDeEscribir(frame, 16, 30, t2.length))}
          estilo={{top: Y.incluido + 62}}
        />
      ) : null}

      {/* V4 · 5,24→9,64 · «Máquina de escribir» 5,24→6,24 */}
      {conCorte(frame, CORTE_2, DURACION) ? (
        <Incluido
          texto={t3.slice(0, maquinaDeEscribir(frame, CORTE_2, 30, t3.length))}
          estilo={{}}
        />
      ) : null}

      {/* V8 · desde 1,00 s, sin transición */}
      {frame >= 30 ? <Precio estilo={{}} /> : null}

      {/* V6 · desde el fotograma 0, sin transición */}
      <Cta estilo={{}} />
    </AbsoluteFill>
  );
};

// ───────────────────────────────────────────────────────────────────────────
// DESPUÉS — la edición nueva
// ───────────────────────────────────────────────────────────────────────────

type Movimiento = {
  /** Escala inicial → final. Nunca bajo 1,04: la deriva no debe ver borde. */
  z: [number, number];
  /** Deriva en px sobre la mesa de 1080. */
  d: [[number, number], [number, number]];
  desde: number;
  hasta: number;
};

/**
 * Cámara con base de tiempo LOCAL a su plano: cada foto recorre su movimiento
 * completo dentro de los fotogramas en que se ve, no a lo largo de la historia.
 */
const usaCamara = (m: Movimiento) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [m.desde, m.hasta], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: CAMARA,
  });
  const escala = m.z[0] + (m.z[1] - m.z[0]) * t;
  const x = m.d[0][0] + (m.d[1][0] - m.d[0][0]) * t;
  const y = m.d[0][1] + (m.d[1][1] - m.d[0][1]) * t;
  return `translate(${x}px, ${y}px) scale(${escala})`;
};

/** La disolvencia entre planos: 10 fotogramas, centrada en el corte. */
const DISOLVENCIA = 10;

/**
 * ⛔ **EL ERROR QUE HAY QUE NO REPETIR: una disolvencia NO se hace bajando la
 * capa que sale.** Si el plano saliente baja a 0,5 mientras el entrante sube a
 * 0,5, la cobertura total en el punto medio es 0,75 y **se asoma el fondo** —
 * en esta pieza, el azul DT. Es un parpadeo oscuro en cada corte, y el primer
 * render los tenía los dos.
 *
 * Se hace al revés: **el plano que sale se queda opaco** y el que entra le
 * crece encima (los planos van apilados en orden, así que el último gana). La
 * cobertura es 1 en todo momento. El saliente se desmonta recién cuando el
 * entrante ya lo tapa entero.
 */
const usaDisolvencia = (desde: number) => {
  const frame = useCurrentFrame();
  if (desde <= 0) return 1;
  return interpolate(
    frame,
    [desde - DISOLVENCIA / 2, desde + DISOLVENCIA / 2],
    [0, 1],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'},
  );
};

/**
 * Fundido + subida, con entrada y SALIDA. Es el recurso único de toda la
 * pieza: lo que separa un texto de otro es el RETARDO, no un preset distinto.
 * Reemplaza a las cuatro transiciones enlatadas del original.
 */
const usaEntrada = (
  entra: number,
  sale: number,
  {subida = 20, dura = 24, duraSalida = 12}: {subida?: number; dura?: number; duraSalida?: number} = {},
) => {
  const frame = useCurrentFrame();
  const t = interpolate(frame, [entra, entra + dura], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: ENTRADA,
  });
  const s =
    sale >= DURACION
      ? 1
      : interpolate(frame, [sale, sale + duraSalida], [1, 0], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
          easing: Easing.bezier(0.4, 0, 0.7, 0.4),
        });
  const o = Math.min(t, s);
  // Entra subiendo y sale subiendo: el bloque nunca «cae».
  const dy = (1 - t) * subida - (1 - s) * (subida * 0.45);
  return {opacity: o, transform: `translateY(${dy}px)`};
};

/**
 * ⭐ EL CAMBIO DE FONDO — los tres planos con cámara propia.
 *
 * Direcciones alternadas para que dos planos seguidos no se lean iguales: la
 * cama ASIENTA (entra ancha y se cierra), el bar EMPUJA (entra justa y se
 * abre), el desayuno vuelve a asentar. Escalas dentro de 1,04–1,11 y derivas
 * ≤ 14 px, o sea muy por dentro del sobrante que deja la escala.
 */
const PLANOS: {src: string; desde: number; hasta: number; m: Movimiento}[] = [
  {
    src: FOTO.cama,
    desde: 0,
    hasta: CORTE_1,
    m: {z: [1.11, 1.04], d: [[0, 14], [0, -2]], desde: 0, hasta: CORTE_1 + DISOLVENCIA},
  },
  {
    src: FOTO.bar,
    desde: CORTE_1,
    hasta: CORTE_2,
    m: {z: [1.04, 1.11], d: [[12, 0], [-6, 4]], desde: CORTE_1 - DISOLVENCIA, hasta: CORTE_2 + DISOLVENCIA},
  },
  {
    src: FOTO.desayuno,
    desde: CORTE_2,
    hasta: DURACION,
    m: {z: [1.11, 1.04], d: [[-10, -6], [8, 2]], desde: CORTE_2 - DISOLVENCIA, hasta: DURACION},
  },
];

const Plano: React.FC<(typeof PLANOS)[number]> = ({src, desde, hasta, m}) => {
  const frame = useCurrentFrame();
  const opacity = usaDisolvencia(desde);
  const transform = usaCamara(m);
  // Se desmonta cuando el plano siguiente ya lo tapa entero, no en su corte.
  const tapado = hasta < DURACION && frame > hasta + DISOLVENCIA / 2;
  if (opacity <= 0 || tapado) return null;
  return (
    <AbsoluteFill style={{opacity}}>
      <Img
        src={src}
        style={{width: 1080, height: 1920, objectFit: 'cover', transform}}
      />
    </AbsoluteFill>
  );
};

export const DtStPruebaDespues: React.FC = () => {
  /**
   * ⭐ EL ESCALONADO. Cada corte lleva ahora un cambio de texto, y dentro de
   * cada tiempo las líneas entran una detrás de otra en el orden en que se lee
   * una oferta: gancho → qué incluye → cuánto → qué hacer.
   *
   * | fotograma | qué pasa |
   * |---|---|
   * | 6   | entra «Escápate en pareja» |
   * | 20  | entra «Habitación para dos» |
   * | 38  | entra el precio |
   * | 58  | entra la CTA |
   * | 80  | sale «Habitación para dos» |
   * | 90  | **corte a bar** (disolvencia 85→95) |
   * | 96  | entra «+Botella de espumante.» — sobre la foto que lo muestra |
   * | 146 | salen el titular y el espumante |
   * | 157 | **corte a desayuno** (disolvencia 152→162) |
   * | 163 | entra «Escapada Romántica» |
   * | 177 | entra «Incluye desayuno buffet para dos.» |
   *
   * El precio y la CTA no se vuelven a tocar: son el ancla de la historia.
   */
  const titularA = usaEntrada(6, 146);
  const incluido1 = usaEntrada(20, 80);
  const espumante = usaEntrada(96, 146);
  const titularB = usaEntrada(163, DURACION);
  const incluido3 = usaEntrada(177, DURACION);
  const precio = usaEntrada(38, DURACION);
  const cta = usaEntrada(58, DURACION, {subida: 14});

  return (
    <AbsoluteFill style={{backgroundColor: DT.colores.azul}}>
      {PLANOS.map((p) => (
        <Plano key={p.src} {...p} />
      ))}
      <Velo />
      <Logotipo />

      <Titular cual="a" estilo={titularA} />
      <Titular cual="b" estilo={titularB} />

      <Incluido texto="Habitación para dos" estilo={incluido1} />
      <Incluido texto="+Botella de espumante." estilo={espumante} />
      <Incluido texto="Incluye desayuno buffet para dos." estilo={incluido3} />

      <Precio estilo={precio} />
      <Cta estilo={cta} />
    </AbsoluteFill>
  );
};

/** Guía de zonas seguras — para mirar, nunca para entregar. */
export const DtStPruebaGuia: React.FC = () => (
  <AbsoluteFill>
    <DtStPruebaDespues />
    <AbsoluteFill style={{pointerEvents: 'none'}}>
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: 1080,
          height: DT.seguras.story.arriba,
          background: 'rgba(255,0,110,0.22)',
        }}
      />
      <div
        style={{
          position: 'absolute',
          bottom: 0,
          left: 0,
          width: 1080,
          height: DT.seguras.story.abajo,
          background: 'rgba(255,0,110,0.22)',
        }}
      />
      <div
        style={{
          position: 'absolute',
          top: 0,
          left: MARGEN,
          width: 1080 - MARGEN * 2,
          height: 1920,
          border: '1px dashed rgba(163,205,57,0.85)',
        }}
      />
    </AbsoluteFill>
  </AbsoluteFill>
);
