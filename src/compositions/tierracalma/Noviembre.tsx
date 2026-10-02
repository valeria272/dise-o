import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {tierracalma as TC} from "../../brand/tierracalma";
import {
  POST, STORY, CARR, SANS, SERIF, IVY,
  Lienzo, Foto, Degradado, Marco, MarcoTenido, MarcoTramos, Cuerpo, Modulado, Aire,
  IWsp, Pildora, Globo, Indicador, Serie, cuerpoSans, sinPartir,
} from "./OctubreV3";

// =============================================================================
// TIERRA CALMA · NOVIEMBRE 2026 — grilla de Carlos Figueroa (propuesta 25-09,
// modificada 30-09). Instantánea verbatim: clients/tierra-calma/grilla-noviembre-2026.md
//
// ESTE ARCHIVO EXTIENDE EL SISTEMA DE OCTUBRE, NO LO REINVENTA. Todas las
// primitivas —`Modulado` con su escala 50–70 / IvyOra 68, `Globo`, `Cabecera`,
// `Pildora`, el marco bloqueado— se importan de `OctubreV3.tsx`. Lo que hay acá
// son las piezas del mes y cuatro componentes chicos que octubre no necesitó.
//
// TODO EL COPY SALE VERBATIM DE LA GRILLA (R-08). Donde una oración se reparte
// entre titular y globo, se reparte en el orden en que está escrita.
//
// ⚠️ DATOS QUE NO ESTÁN EN LA LISTA BLANCA DEL MANUAL (§ 2). La grilla los trae
// citando la «Ficha Técnica (BVM Propiedades)» y fuentes públicas; entran por el
// brief y quedan DECLARADOS acá para que se confirmen con Fran o Blanca antes de
// publicar (R-03):
//   · ROL individual · constructibilidad 10 % · máx. dos pisos · dos casas
//   · portería · gasto común $60.000 aprox. · entrega en 60 días
//   · reserva $1.000.000 (abonable y reembolsable) · pie hasta UF 800 en 24 cuotas
//   · crédito hipotecario, contado o leasing · «todos los bancos»
//   · WhatsApp +56 9 9158 6643
//   · externos: depto. nuevo RM 49 m² / UF 3.928 (Inciti) · tasa 3,97 % (BCCh vía Emol)
//
// LAS IMÁGENES: Seedream 5 Pro (`scripts/tc-nov-imagenes.py`), instaladas al
// tamaño exacto del lienzo (`scripts/tc-nov-instalar.py`) para que la fila de la
// foto SEA la fila del lienzo. Las aéreas y el acceso son FOTO REAL con cambio
// mínimo (R-24). Ninguna repite una de octubre (R-20).
// =============================================================================

const NOV = (n: string) => staticFile(`assets/tierracalma/nov/${n}.jpg`);
const NAVY = TC.colors.navy;
const CREMA = TC.colors.cream;
const ARENA = TC.colors.sand;

// -----------------------------------------------------------------------------
// Lo que noviembre agrega al sistema
// -----------------------------------------------------------------------------

/**
 * Titular anclado en la fila 205, sin número. Es la `Cabecera` de octubre para
 * los carruseles cuyo brief no numera las slides: el titular cae en la misma
 * fila al deslizar (R-15), y no se centra.
 */
const Encabezado: React.FC<{y?: number; children: React.ReactNode}> = ({y = CARR.sinLogo, children}) => (
  <div
    style={{
      position: "absolute",
      left: 0,
      right: 0,
      top: y,
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      textAlign: "center",
    }}
  >
    {children}
  </div>
);

/**
 * Pastilla de CTA de cierre. Es la `Pastilla` de octubre con el cuerpo a la
 * vista: los CTA de noviembre son más largos y el copy NO se acorta (R-08), así
 * que lo que cede es el tamaño — medido para dejar ≥ 70 px al filete (R-34).
 */
const Cta: React.FC<{y: number; size?: number; tinta?: string; icono?: React.ReactNode; children: React.ReactNode}> = ({
  y,
  size = 23,
  tinta = "#fff",
  icono,
  children,
}) => (
  <div
    style={{
      position: "absolute",
      left: "50%",
      top: y,
      transform: "translateX(-50%)",
      display: "flex",
      alignItems: "center",
      gap: 13,
      border: `1.5px solid ${tinta}`,
      borderRadius: 999,
      padding: "15px 34px",
    }}
  >
    {icono}
    <span
      style={{
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: size,
        letterSpacing: "0.09em",
        color: tinta,
        textTransform: "uppercase",
        whiteSpace: "nowrap",
      }}
    >
      {children}
    </span>
  </div>
);

/** La letra chica de fuente. Etiqueta, no texto de cuerpo: fuera de la escala. */
const Pie: React.FC<{y: number; tinta?: string; children: React.ReactNode}> = ({
  y,
  tinta = "rgba(255,255,255,0.82)",
  children,
}) => (
  <div
    style={{
      position: "absolute",
      left: 0,
      right: 0,
      top: y,
      textAlign: "center",
      fontFamily: SANS,
      fontWeight: 300,
      fontSize: 22,
      letterSpacing: "0.04em",
      color: tinta,
      textShadow: tinta.startsWith("rgba(255") ? "0 1px 12px rgba(0,0,0,0.7)" : "none",
    }}
  >
    {children}
  </div>
);

/**
 * ⭐ LA LETRA DEL LETRERO. La IA hizo la tabla EN BLANCO; el nombre lo pone el
 * código (R-27). `multiply` hace que la tinta tome la veta y la sombra de la
 * madera pintada en vez de flotar encima. `x`,`y` son el CENTRO del cuerpo de la
 * tabla, medido por píxel sobre el JPG instalado; `giro` es su inclinación.
 */
const Letrero: React.FC<{x: number; y: number; giro?: number; size: number; children: React.ReactNode}> = ({
  x,
  y,
  giro = 0,
  size,
  children,
}) => (
  <div
    style={{
      position: "absolute",
      left: x,
      top: y,
      transform: `translate(-50%, -50%) rotate(${giro}deg)`,
      mixBlendMode: "multiply",
      fontFamily: SERIF,
      fontWeight: 500,
      fontSize: size,
      letterSpacing: "0.07em",
      textTransform: "uppercase",
      color: "#22302B",
      whiteSpace: "nowrap",
    }}
  >
    {children}
  </div>
);

// =============================================================================
// E · 09/11 · CARRUSEL 5 SLIDES · «49 m² o 5.000 m²: ¿cómo quieres vivir?»
// Brief: letrero de camino con dos flechas en direcciones opuestas
// («Departamento» / «Parcela»), fotografía + gráfica, tipografía grande.
//
// ⭐ La IA hizo los letreros EN BLANCO; «Departamento» y «Parcela» los escribe el
// código sobre el centro medido de cada tabla (R-27, R-52). Si se regenera una
// foto, hay que volver a medir: la medida está en el comentario de cada slide.
// =============================================================================

/**
 * ⭐ E1 · la portada, 2ª VERSIÓN (01-10). Diego: *«la portada del carrusel del
 * 09-11 déjala como esta referencia»* — el pin que ya traía la grilla:
 * clients/tierra-calma/referencias/nov2026/c-09-11.jpg («casa | VS | departamento»).
 *
 * Su estructura, calcada: el título arriba; las DOS OPCIONES lado a lado, cada
 * una en su mitad; un círculo sobre la costura; y abajo, sobre campo claro, el
 * rótulo de cada una.
 *
 * Con la estética de Tierra Calma (R-49), y con el copy de la grilla repartido
 * sin agregar nada —«49 m² o 5.000 m²: ¿cómo quieres vivir?»—:
 *   · la pregunta va arriba, en IvyOra versales;
 *   · «49 m²» rotula el departamento y «5.000 m²» la parcela — cada cifra bajo
 *     su foto, que es justo lo que la referencia hace con sus dos nombres;
 *   · el círculo no dice «VS»: dice la «o» de la frase. No es un combate, es la
 *     pregunta del titular;
 *   · su rojo y su turquesa no entran: navy, crema y el café de la paleta.
 *
 * «Departamento» y «Parcela» salen del visual del brief (los dos letreros); la 1ª
 * versión los escribía en el letrero, y siguen en las slides 2 y 3.
 *
 * ⚠️ CAMPO CLARO ABAJO ⇒ MARCO TEÑIDO POR TRAMOS (R-47): el filete blanco no se
 * ve sobre el papel, así que pasa a navy donde la foto ya se fundió en crema.
 *
 * GEOMETRÍA medida sobre los dos JPG (1080×1350, fila = fila): la torre ocupa
 * x 300–775 y la casa x 382–720; cada mitad muestra 540 px centrados en su
 * sujeto. El papel sube por un degradado que cierra en la fila 1010: tapa la
 * calle del edificio —donde había peatones y un auto (R-26)— sin tocar la casa,
 * que termina en la 930.
 */
const MITAD = {edificio: 265, casa: 281};
/** El rótulo de cada mitad: el nombre en versales chicas y la cifra en IvyOra. */
const Rotulo: React.FC<{x: number; label: string; children: React.ReactNode}> = ({x, label, children}) => (
  <div style={{position: "absolute", left: x, top: 1052, width: 540, textAlign: "center"}}>
    <div
      style={{
        fontFamily: SANS,
        fontWeight: 400,
        fontSize: 25,
        letterSpacing: "0.22em",
        textTransform: "uppercase",
        color: TC.colors.brown,
      }}
    >
      {label}
    </div>
    <div
      style={{
        marginTop: 10,
        fontFamily: SERIF,
        fontWeight: 500,
        fontSize: IVY + 22,
        lineHeight: 1.05,
        textTransform: "uppercase",
        color: NAVY,
        whiteSpace: "nowrap",
      }}
    >
      {children}
    </div>
  </div>
);

const E1: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <div style={{position: "absolute", left: 0, top: 0, width: 540, height: CARR.h, overflow: "hidden"}}>
      <Img
        src={NOV("e-edificio")}
        style={{position: "absolute", left: -MITAD.edificio, top: 0, width: 1080, height: 1350}}
      />
    </div>
    <div style={{position: "absolute", left: 540, top: 0, width: 540, height: CARR.h, overflow: "hidden"}}>
      <Img src={NOV("e-casa")} style={{position: "absolute", left: -MITAD.casa, top: 0, width: 1080, height: 1350}} />
    </div>
    {/* la costura */}
    <div style={{position: "absolute", left: 538.5, top: 0, width: 3, height: 1010, backgroundColor: CREMA}} />
    {/* Velo parejo sobre las fotos. El cielo del edificio es casi blanco: sin
        velo el filete del marco no se ve contra él, y la compuerta leía ese
        cielo pálido pegado al borde como «texto en el margen» (15 % de la tinta,
        columnas 0–59). Medido, no supuesto. */}
    <AbsoluteFill style={{backgroundColor: "rgba(6,14,20,0.14)"}} />
    {/* arriba, sombra para el logo y la pregunta; abajo, el papel */}
    <AbsoluteFill
      style={{
        background: `linear-gradient(to bottom, rgba(6,14,20,0.62) 0%, rgba(6,14,20,0.36) 22%, rgba(6,14,20,0) 40%),
                     linear-gradient(to bottom, rgba(243,238,227,0) 62%, ${CREMA} 75%)`,
      }}
    />

    <div style={{position: "absolute", left: 0, right: 0, top: 232, display: "flex", justifyContent: "center"}}>
      <Modulado ancho={960} tramos={[{t: "¿cómo quieres vivir?", ivy: true, cursiva: true}]} />
    </div>

    {/* el círculo sobre la costura */}
    <div
      style={{
        position: "absolute",
        left: 540 - 70,
        top: 620,
        width: 140,
        height: 140,
        borderRadius: 999,
        backgroundColor: NAVY,
        border: `3px solid ${CREMA}`,
        boxSizing: "border-box",
        boxShadow: "0 18px 40px rgba(0,0,0,0.34)",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        fontFamily: SERIF,
        fontStyle: "italic",
        fontWeight: 500,
        fontSize: 74,
        lineHeight: 1,
        textTransform: "uppercase",
        color: CREMA,
        paddingBottom: 6,
      }}
    >
      o
    </div>

    {/* los dos rótulos, cada uno bajo su mitad. Van escritos uno por uno y no en
        un `.map()` de objetos: así el extractor del QA lee las cifras, que es
        justo lo que la lista blanca existe para vigilar. */}
    <Rotulo x={0} label="Departamento">
      49 m²
    </Rotulo>
    <Rotulo x={540} label="Parcela">
      5.000 m²
    </Rotulo>

    <MarcoTramos
      archivo="MARCO-CARRUSEL-1"
      alto={CARR.h}
      cortes={[
        {y: 960, color: "#FFFFFF"},
        {y: CARR.h, color: NAVY},
      ]}
    />
  </Lienzo>
);

const E2: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={NOV("e-depto")} />
    <Degradado arriba={0.78} abajo={0.5} velo={0.2} />
    <Marco archivo="MARCO-CARRUSEL-2" />
    <Encabezado>
      <Modulado
        ancho={900}
        tramos={[
          {t: "Un departamento nuevo"},
          {t: "en la RM promedia", salto: true},
          {t: "49 m² por UF 3.928.", ivy: true, salto: true},
        ]}
      />
    </Encabezado>
    <Globo y={560} max={760} size={40}>
      {"Sin patio propio y con poco\nmargen para ampliar."}
    </Globo>
    {/* Tabla: cuerpo x 200–1000 · y 912–1130, centro (600, 1021), +1,3°. */}
    <Letrero x={610} y={1022} giro={1.3} size={74}>
      Departamento
    </Letrero>
    {/* NOTA del brief: «Fuente depto: Inciti… (letra chica en slide 2)». */}
    <Pie y={1212}>Fuente: Inciti, stock de departamentos nuevos RM, septiembre 2026.</Pie>
  </Lienzo>
);

const E3: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={NOV("e-parcela")} />
    <Degradado arriba={0.62} abajo={0.42} velo={0.1} />
    <Marco archivo="MARCO-CARRUSEL-3" />
    <Encabezado>
      <Modulado
        ancho={900}
        tramos={[
          {t: "En Tierra Calma,"},
          {t: "~5.000 m²", ivy: true, salto: true},
          {t: " de terreno"},
          {t: "propio en Padre Hurtado", salto: true},
        ]}
      />
    </Encabezado>
    <Globo y={560} max={760} size={40} destacado="desde UF 2.500,">
      con ROL individual.
    </Globo>
    {/* Tabla: cuerpo x 103–780 · y 905–1165, centro (442, 1035). */}
    <Letrero x={442} y={1036} giro={-1.6} size={74}>
      Parcela
    </Letrero>
  </Lienzo>
);

/**
 * E4 · el plano. «Plano simple de la parcela con la casa dibujada».
 *
 * ⭐ EL PLANO VA A ESCALA, no a ojo (manual § 7 bis: «la casa va a escala»).
 * La parcela es un rectángulo de 100 × 50 m = 5.000 m² a **7,6 px/m**. Lo
 * construido son dos casas —la regla del proyecto— de 300 y 140 m²: **440 m²,
 * el 8,8 %**, bajo el 10 % que dice la slide. Si alguien cambia un rectángulo,
 * la cuenta está acá para rehacerla.
 *
 * Fondo verde y tinta crema: una slide sin fotografía va en el verde del manual
 * (R-19), y el marco se tiñe con ella.
 */
const PLANO = {x: 160, y: 500, w: 760, h: 380}; // 100 m × 50 m
const E4: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <AbsoluteFill style={{backgroundColor: TC.colors.green}} />
    <MarcoTenido archivo="MARCO-CARRUSEL-2" color={CREMA} />
    <Encabezado>
      <Modulado
        ancho={880}
        tinta={CREMA}
        tramos={[{t: "Tú decides cómo"}, {t: "construir", ivy: true, salto: true}, {t: ":"}]}
      />
    </Encabezado>
    <svg
      width={CARR.w}
      height={CARR.h}
      viewBox={`0 0 ${CARR.w} ${CARR.h}`}
      style={{position: "absolute", inset: 0}}
      fill="none"
      stroke={CREMA}
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      {/* el deslinde: cerco, con sus postes */}
      <rect x={PLANO.x} y={PLANO.y} width={PLANO.w} height={PLANO.h} strokeWidth={2.6} />
      <rect
        x={PLANO.x}
        y={PLANO.y}
        width={PLANO.w}
        height={PLANO.h}
        strokeWidth={9}
        strokeDasharray="1.5 36.5"
        stroke={ARENA}
      />
      {/* acceso y sendero */}
      <path d={`M ${PLANO.x} 790 C 300 790, 330 730, 404 700`} strokeWidth={1.6} strokeDasharray="7 9" />
      <path d="M 580 690 C 640 720, 680 740, 716 742" strokeWidth={1.6} strokeDasharray="7 9" />
      {/* casa principal · 20 × 15 m = 300 m² → 152 × 114 px */}
      <rect x={404} y={596} width={152} height={114} strokeWidth={3} fill="rgba(243,238,227,0.2)" />
      <path d="M 404 653 H 556 M 480 596 V 710" strokeWidth={1.2} opacity={0.7} />
      {/* terraza */}
      <rect x={404} y={710} width={152} height={26} strokeWidth={1.4} strokeDasharray="4 5" />
      {/* segunda casa · 14 × 10 m = 140 m² → 106 × 76 px */}
      <rect x={716} y={704} width={106} height={76} strokeWidth={3} fill="rgba(243,238,227,0.2)" />
      <path d="M 716 742 H 822" strokeWidth={1.2} opacity={0.7} />
      {/* árboles */}
      {[
        [246, 570, 26], [300, 628, 18], [232, 690, 20], [640, 566, 22], [846, 580, 28],
        [780, 620, 16], [330, 820, 22], [600, 818, 26], [860, 826, 18], [676, 836, 14],
      ].map(([cx, cy, r]) => (
        <g key={`${cx}-${cy}`} stroke={ARENA}>
          <circle cx={cx} cy={cy} r={r} strokeWidth={1.8} />
          <circle cx={cx} cy={cy} r={2} fill={ARENA} strokeWidth={0} />
        </g>
      ))}
    </svg>
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 908,
        textAlign: "center",
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: 25,
        letterSpacing: "0.16em",
        textTransform: "uppercase",
        color: ARENA,
      }}
    >
      {sinPartir("~5.000 m²")}
    </div>
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 1010,
        textAlign: "center",
        fontFamily: SANS,
        fontWeight: 300,
        fontSize: 50,
        lineHeight: 1.24,
        color: CREMA,
      }}
    >
      hasta un 10% de la superficie
      <br />y hasta dos casas.
    </div>
  </Lienzo>
);

const E5: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    {/* FOTO REAL: aérea DJI_0310 del 07-08 con cambio mínimo (sin bruma, luz de
        tarde). No se inventó nada: es el loteo y el llano de Padre Hurtado. */}
    <Foto src={NOV("e-aerea")} />
    <Degradado arriba={0.52} abajo={0.56} velo={0.14} />
    <Marco archivo="MARCO-CARRUSEL-4" />
    <Cuerpo desde={205} hasta={1120}>
      <Globo max={820} size={38} destacado="En Tierra Calma te asesoramos">
        {"para que tengas un espacio a tu medida,\ncon la libertad que un departamento\nno te da."}
      </Globo>
    </Cuerpo>
    <Cta y={1160} icono={<IWsp s={28} />}>
      Escríbenos y te ayudamos a elegir tu parcela
    </Cta>
  </Lienzo>
);

// =============================================================================
// F · 11/11 · CARRUSEL 7 SLIDES · «Lo que nadie te cuenta antes de comprar una
// parcela» · 2ª VERSIÓN (01-10), sobre la referencia que pasó Diego:
// clients/tierra-calma/referencias/2026-10-01_c-11-11_editorial-dudas.jpg
// *«Básate en esta referencia pero dale con la estética de Tierra Calma.»*
//
// Es un carrusel de otra marca (ideafoster). LO QUE SE CALCÓ ES SU ESTRUCTURA:
//   · portada: un atado de HOJAS DE PAPEL con sus clips, flotando sobre una foto,
//     y todo el texto escrito en la hoja;
//   · slides: papel cuadriculado, un folio arriba (serie a la izquierda, marca a
//     la derecha), UN OBJETO arriba a la derecha, el titular grande alineado a la
//     izquierda con una palabra «seleccionada» —caja de color con sus dos
//     tiradores, como un texto marcado con el cursor—, la bajada con un tramo
//     subrayado y la flecha de «sigue» abajo a la derecha.
//
// ⛔ LO QUE NO SE CALCÓ (R-49: calcar una referencia no es copiar su color):
//   · su NARANJO no entra. La caja de la selección va en la arena de la marca y
//     los tiradores y subrayados en el café `#6C473D` de la paleta secundaria;
//   · su SANS NEGRA tampoco. Acá hay dos roles (R-11): Inter Tight Light y,
//     para lo destacado, IvyOra versales — que es justo lo que va dentro de la
//     caja. La selección de la referencia ES el «destacado» de esta cuenta;
//   · su contenido: ni una palabra. El copy es el de la grilla, verbatim.
//
// ⚠️ DOS COSAS QUE ESTA VERSIÓN DECIDE Y CONVIENE SABER:
//   · VA ALINEADO A LA IZQUIERDA, como la referencia, y no «todo centrado al
//     medio» (R-14). Es la gramática que se pidió calcar: con el objeto arriba a
//     la derecha, un titular centrado lo pisa. El titular se ancla por ABAJO en
//     la misma fila en las cinco dudas (R-15: el carrusel se alinea).
//   · EL MARCO SE QUEDA. La referencia no lleva marco; el de Tierra Calma es el
//     asset bloqueado de la marca (R-16) y lo que hace del carrusel un solo
//     objeto (R-17). Va teñido en navy porque el campo es claro (R-47).
//
// ⛔ LA IA HACE EL OBJETO, EL CÓDIGO PONE LA LETRA (R-27). Las hojas de la portada
// se generaron EN BLANCO. Los objetos de las slides se generaron sobre blanco y se
// funden con `multiply` sobre el papel. La portería de la slide 03 NO es IA: es la
// foto real del acceso (27-04), porque el dato que acompaña es «Sí, portería».
//
// NOTA del brief: las preguntas son PROVISORIAS hasta el mapeo de dudas reales de
// Fran y Blanca. Cambiar una es cambiar dos cadenas acá.
// =============================================================================

const CAFE = TC.colors.brown;
const SELECCION = "rgba(201,185,154,0.52)";

/** Papel cuadriculado: el campo de las slides. La cuadrícula es de la referencia
 *  y acá, de paso, es papel de plano. */
const Papel: React.FC = () => (
  <AbsoluteFill
    style={{
      backgroundColor: CREMA,
      backgroundImage:
        "linear-gradient(rgba(108,71,61,0.085) 1.5px, transparent 1.5px), linear-gradient(90deg, rgba(108,71,61,0.085) 1.5px, transparent 1.5px)",
      backgroundSize: "54px 54px",
      backgroundPosition: "27px 22px",
    }}
  />
);

/**
 * La palabra «seleccionada»: caja de arena con sus dos tiradores. Adentro va
 * IvyOra versales — el destacado de la marca. `ini` y `fin` dicen si este tramo
 * lleva el tirador de entrada o el de salida: cuando la selección ocupa dos
 * líneas, el primero abre y el último cierra.
 */
const Marca: React.FC<{ini?: boolean; fin?: boolean; children: React.ReactNode}> = ({ini, fin, children}) => (
  <span
    style={{
      position: "relative",
      display: "inline-block",
      padding: "2px 14px 0",
      margin: "0 3px",
      backgroundColor: SELECCION,
      fontFamily: SERIF,
      fontWeight: 500,
      fontSize: IVY,
      lineHeight: 1.14,
      letterSpacing: "0.01em",
      textTransform: "uppercase",
      whiteSpace: "nowrap",
    }}
  >
    {ini ? (
      <>
        <span style={{position: "absolute", left: -2, top: -16, bottom: 0, width: 3.5, backgroundColor: CAFE}} />
        <span style={{position: "absolute", left: -9, top: -30, width: 18, height: 18, borderRadius: 999, backgroundColor: CAFE}} />
      </>
    ) : null}
    {fin ? (
      <>
        <span style={{position: "absolute", right: -2, top: 0, bottom: -16, width: 3.5, backgroundColor: CAFE}} />
        <span style={{position: "absolute", right: -9, bottom: -30, width: 18, height: 18, borderRadius: 999, backgroundColor: CAFE}} />
      </>
    ) : null}
    {children}
  </span>
);

/** El tramo subrayado de la bajada. */
const Sub: React.FC<{children: React.ReactNode}> = ({children}) => (
  <span style={{borderBottom: `3px solid ${CAFE}`, paddingBottom: 2}}>{children}</span>
);

/** El folio: el número de la duda, arriba a la izquierda.
 *  ⛔ Sin la firma «Tierra Calma · Padre Hurtado» a la derecha (Constanza Lizana,
 *  02-10: *«borrar texto de todas las slides que está en la parte superior
 *  derecha»*). La marca ya va en el logo de la portada. */
const Folio: React.FC<{n?: string}> = ({n}) => (
  <div
    style={{
      position: "absolute",
      left: 84,
      right: 84,
      top: 164,
      display: "flex",
      alignItems: "baseline",
      justifyContent: "space-between",
    }}
  >
    <span
      style={{
        fontFamily: SERIF,
        fontStyle: "italic",
        fontWeight: 400,
        fontSize: 52,
        lineHeight: 1,
        color: CAFE,
      }}
    >
      {n ?? "\u00a0"}
    </span>
  </div>
);

/** El objeto de la slide, arriba a la derecha. Blanco de fondo + `multiply` =
 *  el objeto queda apoyado en el papel, con su propia sombra. */
const OBJETO = {x: 566, y: 232, lado: 430};
const Objeto: React.FC<{src: string}> = ({src}) => (
  <Img
    src={staticFile(`assets/tierracalma/nov/${src}.png`)}
    style={{
      position: "absolute",
      left: OBJETO.x,
      top: OBJETO.y,
      width: OBJETO.lado,
      height: OBJETO.lado,
      mixBlendMode: "multiply",
    }}
  />
);

/**
 * ⛔ EL TITULAR SE ANCLA POR ABAJO, en la fila `TIT_BASE`, en las cinco dudas.
 * Una pregunta de una línea y una de tres terminan en el mismo sitio, así la
 * bajada arranca siempre en la misma fila y al deslizar nada salta (R-15).
 * La caja deja libre el objeto: una línea larga pasa por debajo, no por encima.
 */
const TIT_BASE = 968;
const Titular: React.FC<{size: number; base?: number; children: React.ReactNode}> = ({
  size,
  base = TIT_BASE,
  children,
}) => (
  <div
    style={{
      position: "absolute",
      left: 84,
      top: 640,
      width: 912,
      height: base - 640,
      display: "flex",
      flexDirection: "column",
      justifyContent: "flex-end",
    }}
  >
    <div style={{fontFamily: SANS, fontWeight: 300, fontSize: size, lineHeight: 1.2, color: NAVY}}>{children}</div>
  </div>
);

const Bajada: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      position: "absolute",
      left: 84,
      top: TIT_BASE + 44,
      width: 800,
      fontFamily: SANS,
      fontWeight: 300,
      fontSize: 41,
      lineHeight: 1.34,
      color: "rgba(11,44,73,0.9)",
    }}
  >
    {children}
  </div>
);

/** La flecha de «sigue». Gráfica, sin texto. */
const Sigue: React.FC<{x?: number; y?: number; tinta?: string}> = ({x = 928, y = 1176, tinta = NAVY}) => (
  <svg width={68} height={68} viewBox="0 0 68 68" fill="none" style={{position: "absolute", left: x, top: y}}>
    <circle cx="34" cy="34" r="32" stroke={tinta} strokeWidth="2" />
    <path d="M22 34h24M38 26l8 8-8 8" stroke={tinta} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

/**
 * F1 · la portada. GEOMETRÍA MEDIDA sobre `f-papeles.jpg` (1080×1350):
 *   hoja de arriba  x 205–890 · y 245–1195      clip de papel (310, 235–310)
 *   pinza negra     x 835–940 · y 630–730       ← el texto no pasa de x 815
 * El bloque va centrado en la hoja, como la portada de la referencia. ⚠️ Si se
 * regenera el fondo hay que volver a medir `HOJA_F`.
 */
const HOJA_F = {x: 262, y: 330, w: 556, h: 800};
const F1: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={NOV("f-papeles")} />
    <AbsoluteFill
      style={{
        background:
          "linear-gradient(to bottom, rgba(6,14,20,0.5) 0%, rgba(6,14,20,0) 18%, rgba(6,14,20,0) 86%, rgba(6,14,20,0.4) 100%)",
      }}
    />
    <Marco archivo="MARCO-CARRUSEL-1" />
    <div
      style={{
        position: "absolute",
        left: HOJA_F.x,
        top: HOJA_F.y,
        width: HOJA_F.w,
        height: HOJA_F.h,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        textAlign: "center",
        mixBlendMode: "multiply",
        color: NAVY,
      }}
    >
      <div style={{fontFamily: SANS, fontWeight: 300, fontSize: 66, lineHeight: 1.14}}>
        Lo que nadie
        <br />
        te cuenta
      </div>
      <Aire h={44} />
      <div style={{display: "flex", flexDirection: "column", alignItems: "center", gap: 10}}>
        <Marca ini>antes de</Marca>
        <Marca>comprar</Marca>
        <Marca fin>una parcela</Marca>
      </div>
      <Aire h={84} />
      <svg width={76} height={76} viewBox="0 0 68 68" fill="none">
        <circle cx="34" cy="34" r="32" stroke={NAVY} strokeWidth="2" />
        <path d="M22 34h24M38 26l8 8-8 8" stroke={NAVY} strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
      </svg>
    </div>
  </Lienzo>
);

const F2: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Papel />
    <MarcoTenido archivo="MARCO-CARRUSEL-2" color={NAVY} />
    <Folio n="01." />
    <Objeto src="f-obj-plano" />
    <Titular size={cuerpoSans("¿Cuánto puedo construir?")}>
      ¿Cuánto puedo
      <br />
      <Marca ini fin>
        construir
      </Marca>
      ?
    </Titular>
    <Bajada>
      Hasta un <Sub>10% de la superficie</Sub>, con casas de máximo dos pisos.
    </Bajada>
    <Sigue />
  </Lienzo>
);

const F3: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Papel />
    <MarcoTenido archivo="MARCO-CARRUSEL-3" color={NAVY} />
    <Folio n="02." />
    <Objeto src="f-obj-casas" />
    <Titular size={cuerpoSans("¿Puedo tener una casa para mis papás o para arrendar?")}>
      ¿Puedo tener
      <Marca ini fin>
        una casa
      </Marca>
      <br />
      para mis papás
      <br />o para arrendar?
    </Titular>
    <Bajada>
      Sí: se permiten <Sub>dos casas por parcela</Sub>, una principal y una de inquilino.
    </Bajada>
    <Sigue />
  </Lienzo>
);

const F4: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Papel />
    <MarcoTenido archivo="MARCO-CARRUSEL-2" color={NAVY} />
    <Folio n="03." />
    {/* FOTO REAL del acceso (27-04-2026), en copia con paspartú. Derecha, sin
        inclinar: Diego pidió las imágenes derechas en el carrusel de octubre. */}
    <div
      style={{
        position: "absolute",
        left: OBJETO.x + 26,
        top: OBJETO.y + 30,
        width: OBJETO.lado - 52,
        padding: 13,
        boxSizing: "border-box",
        backgroundColor: "#FBF8F2",
        boxShadow: "0 18px 34px rgba(60,40,30,0.22)",
      }}
    >
      <Img
        src={staticFile("assets/tierracalma/nov/f-porteria.jpg")}
        style={{width: "100%", height: OBJETO.lado - 78, objectFit: "cover", objectPosition: "38% 50%", display: "block"}}
      />
    </div>
    <Titular size={cuerpoSans("¿Tiene gastos comunes? ¿Hay portería?")}>
      ¿Tiene
      <Marca ini fin>
        gastos comunes
      </Marca>
      ?
      <br />
      ¿Hay portería?
    </Titular>
    <Bajada>
      Sí, portería. Gasto común de <Sub>$60.000 mensuales aprox.</Sub>
    </Bajada>
    <Sigue />
  </Lienzo>
);

const F5: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Papel />
    <MarcoTenido archivo="MARCO-CARRUSEL-3" color={NAVY} />
    <Folio n="04." />
    <Objeto src="f-obj-llave" />
    <Titular size={cuerpoSans("¿Cuándo me entregan la parcela?")}>
      ¿Cuándo me
      <Marca ini fin>
        entregan
      </Marca>
      <br />
      la parcela?
    </Titular>
    <Bajada>
      Dentro de <Sub>60 días</Sub> desde la inscripción en el Conservador.
    </Bajada>
    <Sigue />
  </Lienzo>
);

const F6: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Papel />
    <MarcoTenido archivo="MARCO-CARRUSEL-2" color={NAVY} />
    <Folio n="05." />
    <Objeto src="f-obj-balde" />
    <Titular size={cuerpoSans("¿Y el agua?")}>
      ¿Y el
      <Marca ini fin>
        agua
      </Marca>
      ?
    </Titular>
    {/* ⛔ R-02: nunca «agua potable». Esta respuesta es la versión correcta del
        dato, tal como la escribe la grilla. */}
    <Bajada>
      Se obtiene por <Sub>noria o pozo</Sub>, que construye cada propietario.
    </Bajada>
    <Sigue />
  </Lienzo>
);

const F7: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Papel />
    <MarcoTenido archivo="MARCO-CARRUSEL-4" color={NAVY} />
    {/* El objeto del cierre: un globo de comentario, dibujado. Va SIN texto —
        los tres puntos son «alguien está escribiendo», no copy. */}
    <svg
      width={380}
      height={300}
      viewBox="0 0 380 300"
      style={{position: "absolute", left: 590, top: 300, filter: "drop-shadow(0 18px 26px rgba(11,44,73,0.2))"}}
    >
      <path d="M48 0h284a48 48 0 0 1 48 48v124a48 48 0 0 1-48 48H150l-70 66v-66H48a48 48 0 0 1-48-48V48A48 48 0 0 1 48 0Z" fill={NAVY} />
      <circle cx="120" cy="110" r="17" fill={ARENA} />
      <circle cx="190" cy="110" r="17" fill={ARENA} opacity="0.75" />
      <circle cx="260" cy="110" r="17" fill={ARENA} opacity="0.5" />
    </svg>
    {/* Sin bajada ni flecha: el bloque baja 150 px para ocupar el lugar que en
        las otras slides ocupa la respuesta. */}
    <Titular size={cuerpoSans("¿Te quedó otra duda?")} base={TIT_BASE + 150}>
      ¿Te quedó otra duda?
      <br />
      <span style={{display: "inline-flex", flexDirection: "column", alignItems: "flex-start", gap: 10, marginTop: 26}}>
        <Marca ini>Déjala en</Marca>
        <Marca fin>los comentarios.</Marca>
      </span>
    </Titular>
  </Lienzo>
);

// =============================================================================
// G · 13/11 · HISTORIA · pie en cuotas · «Interfaz tipo glassmorphism con
// sticker de pregunta».
//
// Glassmorphism es `backdropFilter` DE VERDAD sobre la foto (R-51), y el vidrio
// se diseña con lo que queda detrás (R-48): por eso la foto va velada y el panel
// lleva su propio tinte oscuro — vidrio claro sobre cielo claro se come el texto.
//
// ⚠️ EL STICKER DE PREGUNTA es el NATIVO de Instagram y lo pone la CM al publicar.
// NO se dibuja (Diego, 01-10: «eliminar»): la pieza le deja libre la franja bajo el
// panel y el llamado del brief va en la píldora del marco.
// =============================================================================

const VIDRIO: React.CSSProperties = {
  backgroundColor: "rgba(9,22,30,0.34)",
  backdropFilter: "blur(26px) saturate(1.25)",
  WebkitBackdropFilter: "blur(26px) saturate(1.25)",
  border: "1px solid rgba(255,255,255,0.34)",
  boxShadow: "0 30px 70px rgba(0,0,0,0.34), inset 0 1px 0 rgba(255,255,255,0.28)",
};
const PANEL_G = {x: 110, y: 690, w: 860};

const G: React.FC = () => (
  <Lienzo w={STORY.w} h={STORY.h}>
    <Foto src={NOV("g-terraza")} />
    <Degradado arriba={0.5} abajo={0.5} velo={0.24} />
    <Marco archivo="MARCO-ST" />
    <Cuerpo desde={250} hasta={650}>
      <Modulado
        ancho={860}
        tramos={[{t: "¿Estás evaluando"}, {t: "crédito", ivy: true, salto: true}, {t: " para el 2027?"}]}
      />
    </Cuerpo>

    {/* el panel de vidrio con el dato */}
    <div
      style={{
        position: "absolute",
        left: PANEL_G.x,
        top: PANEL_G.y,
        width: PANEL_G.w,
        boxSizing: "border-box",
        padding: "46px 50px 50px",
        borderRadius: 44,
        textAlign: "center",
        color: "#fff",
        ...VIDRIO,
      }}
    >
      <div style={{fontFamily: SANS, fontWeight: 300, fontSize: 44, lineHeight: 1.24}}>
        El pie de tu parcela se puede pagar en
      </div>
      <div
        style={{
          fontFamily: SERIF,
          fontStyle: "italic",
          fontWeight: 500,
          fontSize: IVY + 16,
          lineHeight: 1.1,
          textTransform: "uppercase",
          margin: "10px 0 6px",
        }}
      >
        hasta 24 cuotas
      </div>
      <div style={{fontFamily: SANS, fontWeight: 300, fontSize: 44, lineHeight: 1.24}}>
        {sinPartir("(hasta UF 800).")}
      </div>
    </div>

    {/* ⛔ Diego, 01-10, comentario anclado sobre el recuadro del sticker (filas
        1095–1481): *«eliminar»*. Había dibujado el lugar del sticker de pregunta
        con el CTA adentro; el sticker NATIVO lo pone la CM al publicar y uno
        dibujado es un botón falso. Sale el recuadro; la franja 1120–1560 queda
        LIBRE a propósito, que es donde va el sticker de Instagram. El CTA del
        brief pasa a la píldora del marco — verbatim (R-08), cede el cuerpo (R-16). */}
    <Pildora caja={STORY.pill} icono={<IWsp s={24} />} size={21} gap={10}>
      Pregúntanos lo que quieras sobre el pie
    </Pildora>
  </Lienzo>
);

// =============================================================================
// H · 17/11 · POST 4:5 · «¿Cuánto necesitas para empezar?» · Brief: «Afiche
// pegado en un poste de madera, con tiras desprendibles abajo. Fondo: camino
// arbolado de Padre Hurtado desenfocado.»
//
// ⛔ LA IA HACE EL OBJETO, EL CÓDIGO PONE LA LETRA (R-27). El afiche se generó
// EN BLANCO: papel, chinche, cortes y sombra son de la escena; el texto es dato
// y lo escribe el código, con `multiply` para que la tinta tome las arrugas.
//
// «La pregunta se responde con la reserva y el pie; el resto de los datos va en
// las tiras» (NOTA del brief): cinco datos, cinco tiras.
//
// ⚠️ GEOMETRÍA MEDIDA sobre `h-afiche.jpg` (ya 1080×1350, fila = fila). Si se
// regenera el afiche hay que volver a medir `HOJA` y `TIRAS`.
// =============================================================================

// Hoja: x 248–835 · borde superior en la fila 280 · chinches en (517, 307) y
// (568, 307) · los cortes arrancan en la fila 855 y las tiras cierran en la 1130.
const HOJA = {x: 268, y: 348, w: 548, h: 490};
/** Centro de cada tira, de izquierda a derecha, y su inclinación (se abren en
 *  abanico: la primera cae 1° hacia la izquierda y la última 1° a la derecha). */
const TIRAS: {x: number; y: number; giro: number}[] = [
  {x: 301, y: 996, giro: 1.2},
  {x: 421, y: 996, giro: 0.4},
  {x: 540, y: 996, giro: 0},
  {x: 661, y: 996, giro: -0.6},
  {x: 784, y: 996, giro: -1.2},
];

/** El texto de una tira: va girado 90°, como en un afiche de verdad. */
const Tira: React.FC<{i: number; label?: string; children: React.ReactNode}> = ({i, label, children}) => (
  <div
    style={{
      position: "absolute",
      left: TIRAS[i].x,
      top: TIRAS[i].y,
      transform: `translate(-50%, -50%) rotate(${-90 + TIRAS[i].giro}deg)`,
      mixBlendMode: "multiply",
      textAlign: "center",
      whiteSpace: "nowrap",
      color: "#1B2E3F",
      fontFamily: SANS,
    }}
  >
    {label ? (
      <div style={{fontWeight: 400, fontSize: 17, letterSpacing: "0.14em", textTransform: "uppercase", opacity: 0.75}}>
        {label}
      </div>
    ) : null}
    <div style={{fontWeight: 600, fontSize: 27, letterSpacing: "0.01em", lineHeight: 1.2}}>{children}</div>
  </div>
);

const H: React.FC = () => (
  <Lienzo w={POST.w} h={POST.h}>
    <Foto src={NOV("h-afiche")} />
    {/* sólo arriba y abajo: un velo parejo ensuciaría el blanco del papel */}
    <AbsoluteFill
      style={{
        background:
          "linear-gradient(to bottom, rgba(6,14,20,0.62) 0%, rgba(6,14,20,0) 17%, rgba(6,14,20,0) 84%, rgba(6,14,20,0.6) 100%)",
      }}
    />
    <div
      style={{
        position: "absolute",
        left: HOJA.x,
        top: HOJA.y,
        width: HOJA.w,
        height: HOJA.h,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        mixBlendMode: "multiply",
      }}
    >
      <Modulado
        ancho={540}
        base={54}
        tinta="#12283A"
        tramos={[{t: "¿Cuánto necesitas"}, {t: "para ", salto: true}, {t: "empezar", ivy: true}, {t: "?"}]}
      />
      <div style={{width: 72, height: 1.5, backgroundColor: "#8A7A5C", margin: "34px 0 30px"}} />
      <div
        style={{
          width: 500,
          textAlign: "center",
          fontFamily: SANS,
          fontWeight: 300,
          fontSize: 39,
          lineHeight: 1.26,
          color: "#12283A",
        }}
      >
        Reserva tu parcela con $1.000.000 y paga el pie en hasta 24 cuotas.
      </div>
    </div>

    <Tira i={0} label="Desde">
      UF 2.500
    </Tira>
    <Tira i={1}>~5.000 m²</Tira>
    <Tira i={2} label="ROL">
      individual
    </Tira>
    <Tira i={3}>Padre Hurtado</Tira>
    <Tira i={4} label="WhatsApp">
      +56 9 9158 6643
    </Tira>

    <Marco archivo="MARCO-POST" />
    {/* El contorno de la píldora es del marco (R-16) y el CTA va verbatim
        (R-08): cede el cuerpo del texto. */}
    <Pildora caja={POST.pill} icono={<IWsp s={20} />} size={19} gap={9}>
      Consulta el detalle de valores por WhatsApp
    </Pildora>
  </Lienzo>
);

// =============================================================================
// J · 20/11 · HISTORIA · «Todo esto cabe en tu parcela» · Brief: «Vista aérea de
// una parcela con zonas marcadas en diseño gráfico: casa principal, casa de
// huéspedes, jardín y huerto. Mostrar sólo DOS casas (reglamento).»
//
// La base es la aérea REAL DJI_0316 (caminos, vecinos y matorral son del lugar);
// Seedream dibujó dentro UNA parcela cercada con dos construcciones, jardín y
// huerto. Es una visualización del potencial, no una foto del proyecto.
// Los indicadores apuntan a coordenadas medidas sobre `j-parcela.jpg`.
// =============================================================================

const J: React.FC = () => (
  <Lienzo w={STORY.w} h={STORY.h}>
    <Foto src={NOV("j-parcela")} />
    <Degradado arriba={0.84} abajo={0.62} velo={0.08} />
    <Marco archivo="MARCO-ST" />
    <Cuerpo desde={250} hasta={560}>
      <Modulado ancho={860} tramos={[{t: "Todo esto cabe"}]} />
      {/* Sin aire entre las dos líneas (Constanza Lizana, 02-10: *«menos
          interlineado en el título»*). */}
      <Modulado ancho={900} tramos={[{t: "en tu parcela", ivy: true, cursiva: true}]} />
    </Cuerpo>
    {/* casa principal: techo x 450–735 · y 765–880 */}
    <Indicador x={690} y={792} lado="der">
      Casa principal
    </Indicador>
    {/* casa de huéspedes: x 760–875 · y 990–1100 */}
    <Indicador x={772} y={1036} lado="izq">
      Casa de huéspedes
    </Indicador>
    {/* huerto: x 260–455 · y 830–1015 */}
    <Indicador x={300} y={948} lado="izq">
      Huerto
    </Indicador>
    {/* jardín: el prado con árboles jóvenes al norte de la casa */}
    <Indicador x={520} y={684} lado="der">
      Jardín
    </Indicador>
    <Globo y={1290} max={640} size={38} destacado="~5.000 m²">
      con ROL individual
    </Globo>
    <Pildora caja={STORY.pill} icono={<IWsp s={24} />} size={22} gap={10}>
      Imagina la tuya y cotiza por WhatsApp
    </Pildora>
  </Lienzo>
);

// =============================================================================
// K · 24/11 · POST 4:5 · «Ven a conocer Tierra Calma» · Brief: «Imagen editorial
// del camino de acceso y la entrada a las parcelas, luz de tarde.»
//
// ⚠️ MANDA EL BRIEF, NO LA REFERENCIA (R-50). La REF del brief es un calendario
// en un corcho; el visual pide el camino de acceso. Y hay FOTO REAL de ese
// camino —`foto 13.jpg`, los cercos de madera oscura a los dos lados—, así que
// la pieza es esa foto con cambio mínimo (R-24), no una escena inventada.
// =============================================================================

const K: React.FC = () => (
  <Lienzo w={POST.w} h={POST.h}>
    <Foto src={NOV("k-acceso")} />
    <Degradado arriba={0.62} abajo={0.5} velo={0.1} />
    <Marco archivo="MARCO-POST" />
    {/* El cielo llega hasta la fila ~560 (el cerro); el titular vive ahí. */}
    <Cuerpo desde={250} hasta={600}>
      <Modulado ancho={860} tramos={[{t: "Ven a conocer"}]} />
      {/* Sin aire entre las dos líneas (Constanza Lizana, 02-10: *«menos
          interlineado en el título»*). */}
      <Modulado ancho={900} tramos={[{t: "Tierra Calma", ivy: true, cursiva: true}]} />
    </Cuerpo>
    <Globo y={925} max={780} size={36} destacado="A 15 min del Peaje Padre Hurtado">
      Parcelas de ~5.000 m² con ROL individual
    </Globo>
    <Pildora caja={POST.pill} icono={<IWsp s={23} />} size={26} gap={11}>
      Agenda tu visita por WhatsApp
    </Pildora>
  </Lienzo>
);

// =============================================================================
// L · 26/11 · HISTORIA · «Pase de visita» · Brief: «Ticket de "Pase de visita"
// sobre vista aérea de la parcela, con campos de datos como un boarding pass.»
//
// El ticket es gráfica, así que lo dibuja el código: un solo `<path>` con las
// dos muescas del corte. Los campos son el copy del brief repartido en
// rótulo / valor, sin agregar ni un dato:
//   «Parcelas de ~5.000 m² · ROL individual · Desde UF 2.500»
//   «Crédito hipotecario · Pie en hasta 24 cuotas»
// El código de barras es ornamento: no codifica nada.
// La aérea es REAL (DJI_0299, cambio mínimo).
// =============================================================================

const TICKET = {x: 130, y: 300, w: 820, h: 1130, r: 44, corte: 500, muesca: 34};

const Campo: React.FC<{label: string; ancho?: number; children: React.ReactNode}> = ({label, ancho, children}) => (
  <div style={{width: ancho}}>
    <div
      style={{
        fontFamily: SANS,
        fontWeight: 400,
        fontSize: 22,
        letterSpacing: "0.18em",
        textTransform: "uppercase",
        color: TC.colors.brown,
        marginBottom: 6,
      }}
    >
      {label}
    </div>
    <div
      style={{
        fontFamily: SERIF,
        fontWeight: 500,
        fontSize: 46,
        lineHeight: 1.04,
        textTransform: "uppercase",
        color: NAVY,
        whiteSpace: "nowrap",
      }}
    >
      {sinPartir(children)}
    </div>
  </div>
);

const formaTicket = () => {
  const {w, h, r, corte, muesca: m} = TICKET;
  return [
    `M ${r} 0 H ${w - r} A ${r} ${r} 0 0 1 ${w} ${r}`,
    `V ${corte - m} A ${m} ${m} 0 0 0 ${w} ${corte + m}`,
    `V ${h - r} A ${r} ${r} 0 0 1 ${w - r} ${h}`,
    `H ${r} A ${r} ${r} 0 0 1 0 ${h - r}`,
    `V ${corte + m} A ${m} ${m} 0 0 0 0 ${corte - m}`,
    `V ${r} A ${r} ${r} 0 0 1 ${r} 0 Z`,
  ].join(" ");
};

/** Barras del código: anchos fijos, escritos a mano para que no cambien. */
const BARRAS = [3, 1, 2, 4, 1, 1, 3, 2, 1, 4, 2, 1, 1, 3, 1, 2, 4, 1, 3, 1, 2, 2, 1, 4, 1, 3, 2, 1, 1, 4, 2, 3, 1, 1, 2, 4, 1, 3];

const L: React.FC = () => (
  <Lienzo w={STORY.w} h={STORY.h}>
    <Foto src={NOV("l-aerea")} />
    <Degradado arriba={0.6} abajo={0.6} velo={0.22} />
    <Marco archivo="MARCO-ST" />

    <svg
      width={TICKET.w + 120}
      height={TICKET.h + 140}
      viewBox={`-60 -50 ${TICKET.w + 120} ${TICKET.h + 140}`}
      style={{position: "absolute", left: TICKET.x - 60, top: TICKET.y - 50}}
    >
      <defs>
        <filter id="sombraTicket" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="26" stdDeviation="26" floodColor="#000" floodOpacity="0.42" />
        </filter>
      </defs>
      <path d={formaTicket()} fill="#F6F1E7" filter="url(#sombraTicket)" />
      <path
        d={`M ${TICKET.muesca + 22} ${TICKET.corte} H ${TICKET.w - TICKET.muesca - 22}`}
        stroke="rgba(11,44,73,0.34)"
        strokeWidth={2}
        strokeDasharray="3 13"
        strokeLinecap="round"
      />
    </svg>

    {/* talón superior */}
    <div
      style={{
        position: "absolute",
        left: TICKET.x,
        top: TICKET.y,
        width: TICKET.w,
        height: TICKET.corte,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        textAlign: "center",
      }}
    >
      <div
        style={{
          fontFamily: SERIF,
          fontStyle: "italic",
          fontWeight: 500,
          fontSize: IVY + 20,
          lineHeight: 1,
          textTransform: "uppercase",
          color: NAVY,
          whiteSpace: "nowrap",
        }}
      >
        Pase de visita
      </div>
      <Aire h={26} />
      <div
        style={{
          fontFamily: SANS,
          fontWeight: 400,
          fontSize: 27,
          letterSpacing: "0.2em",
          textTransform: "uppercase",
          color: TC.colors.brown,
        }}
      >
        {sinPartir("Tierra Calma")} · {sinPartir("Padre Hurtado")}
      </div>
    </div>

    {/* los campos */}
    <div
      style={{
        position: "absolute",
        left: TICKET.x + 76,
        top: TICKET.y + TICKET.corte + 62,
        width: TICKET.w - 152,
        display: "flex",
        flexWrap: "wrap",
        rowGap: 44,
      }}
    >
      <Campo label="Parcelas de" ancho={368}>
        ~5.000 m²
      </Campo>
      <Campo label="ROL" ancho={300}>
        Individual
      </Campo>
      <Campo label="Desde" ancho={368}>
        UF 2.500
      </Campo>
      <Campo label="Crédito" ancho={300}>
        Hipotecario
      </Campo>
      <Campo label="Pie en">Hasta 24 cuotas</Campo>
    </div>

    {/* código de barras: ornamento */}
    <div
      style={{
        position: "absolute",
        left: TICKET.x + 76,
        top: TICKET.y + TICKET.h - 150,
        width: TICKET.w - 152,
        height: 84,
        display: "flex",
        alignItems: "stretch",
        justifyContent: "space-between",
        opacity: 0.82,
      }}
    >
      {BARRAS.map((b, i) => (
        <div key={i} style={{width: b * 3.4, backgroundColor: NAVY}} />
      ))}
    </div>

    <Pildora caja={STORY.pill} icono={<IWsp s={26} />} size={25} gap={11}>
      Escríbenos y coordinamos tu visita
    </Pildora>
  </Lienzo>
);

// =============================================================================
// M · 30/11 · CARRUSEL 6 SLIDES · «Antes de comprar tu parcela, lee esto»
// 2ª VERSIÓN (01-10), sobre el carrusel de referencia que pasó Diego —el mismo pin
// que traía la grilla, ahora con sus seis slides—:
// clients/tierra-calma/referencias/nov2026/c-30-11_carrusel/ref-1…6.jpg
// *«Ocupa este carrusel de referencia manteniendo la estética de Tierra Calma.»*
//
// LO QUE SE CALCÓ, que es su estructura:
//   · portada y cierre: foto oscurecida a sangre, el titular ALINEADO A LA
//     IZQUIERDA a media altura, y debajo una píldora de contorno;
//   · slides del medio: foto cálida a sangre y, al centro, UNA TARJETA DE APP DE
//     NOTAS —cabecera «‹ Notas» con sus dos íconos, un título con filete y el
//     punto con su check—. ⛔ Sin firma al pie (Constanza Lizana, 02-10: *«borra
//     de slide 2, 3, 4 y 5 el texto inferior que dice "Tierra Calma · Padre
//     Hurtado"»*).
//
// ⛔ LO QUE NO SE CALCÓ (R-49):
//   · su AMARILLO de iOS no entra: el filete, el check y la cabecera van en la
//     arena y el café de la marca;
//   · su sans negra para destacar tampoco: en portada y cierre destaca IvyOra
//     versales (R-10); dentro de la nota, que es interfaz, el dato va SUBRAYADO en
//     café — el mismo recurso del carrusel del 11-11, para que el mes hable igual;
//   · su copy: ni una palabra.
//
// ⚠️ TODO EL TEXTO DE LA NOTA SALE DE LA GRILLA. El título de cada nota es el
// nombre que el brief le da a la slide («Dato nacional», «Formas de pago», «Pie»,
// «Reserva»); la referencia dice «Recordatorio» en todas, y eso sería copy de otra
// marca. Lo único que es interfaz es la palabra «Notas» de la cabecera.
//
// ⚠️ La tasa de la slide 2 es de créditos PARA VIVIENDA a nivel nacional: no se
// promete tasa para la parcela (NOTA del brief). La fuente va en letra chica.
// Igual que en `c-11-11`, va alineado a la izquierda donde la referencia lo hace.
// =============================================================================

/** Un punto de la nota: el check de la app y su texto. */
const Punto: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div style={{display: "flex", alignItems: "flex-start", gap: 20, marginTop: 20}}>
    <svg width={38} height={38} viewBox="0 0 38 38" style={{flexShrink: 0, marginTop: 6}}>
      <circle cx="19" cy="19" r="19" fill={ARENA} />
      <path d="M11 19.6l5.4 5.4L27.4 14" stroke={NAVY} strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" fill="none" />
    </svg>
    <div style={{fontFamily: SANS, fontWeight: 300, fontSize: 38, lineHeight: 1.32, color: NAVY}}>{children}</div>
  </div>
);

/**
 * La tarjeta de la app de notas. Va CENTRADA en el alto del marco (filas
 * 130–1284) y se ajusta a su contenido, así una nota de una línea y una de cuatro
 * quedan igual de equilibradas sin medir nada a mano.
 */
const NotaApp: React.FC<{titulo: string; children: React.ReactNode}> = ({titulo, children}) => (
  <div
    style={{
      position: "absolute",
      left: 0,
      right: 0,
      top: 130,
      height: 1284 - 130,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
    }}
  >
    <div
      style={{
        width: 860,
        boxSizing: "border-box",
        padding: "30px 44px 46px",
        borderRadius: 40,
        backgroundColor: "#FBF8F2",
        boxShadow: "0 34px 70px rgba(0,0,0,0.42)",
      }}
    >
      <div style={{display: "flex", alignItems: "center", justifyContent: "space-between"}}>
        <div style={{display: "flex", alignItems: "center", gap: 8, fontFamily: SANS, fontWeight: 500, fontSize: 27, color: CAFE}}>
          <svg width={16} height={28} viewBox="0 0 16 28" fill="none">
            <path d="M13 3L3 14l10 11" stroke={CAFE} strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
          Notas
        </div>
        <div style={{display: "flex", alignItems: "center", gap: 26}}>
          <svg width={32} height={36} viewBox="0 0 32 36" fill="none" stroke={CAFE} strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M16 3v20M9 9.5L16 3l7 6.5M6 16H4v17h24V16h-2" />
          </svg>
          <svg width={36} height={36} viewBox="0 0 36 36" fill="none">
            <circle cx="18" cy="18" r="16" stroke={CAFE} strokeWidth="2.2" />
            <circle cx="10.5" cy="18" r="2.3" fill={CAFE} />
            <circle cx="18" cy="18" r="2.3" fill={CAFE} />
            <circle cx="25.5" cy="18" r="2.3" fill={CAFE} />
          </svg>
        </div>
      </div>
      <div
        style={{
          marginTop: 34,
          paddingLeft: 16,
          borderLeft: `4px solid ${ARENA}`,
          fontFamily: SANS,
          fontWeight: 400,
          fontSize: 44,
          lineHeight: 1.1,
          color: NAVY,
        }}
      >
        {titulo}
      </div>
      <div style={{marginTop: 14}}>{children}</div>
    </div>
  </div>
);

/** Píldora de contorno bajo el titular de portada y de cierre, como la referencia. */
const Capsula: React.FC<{size?: number; icono?: React.ReactNode; children: React.ReactNode}> = ({
  size = 25,
  icono,
  children,
}) => (
  <div
    style={{
      display: "inline-flex",
      alignItems: "center",
      gap: 13,
      border: "1.5px solid rgba(255,255,255,0.9)",
      borderRadius: 999,
      padding: "14px 30px",
      fontFamily: SANS,
      fontWeight: 300,
      fontSize: size,
      letterSpacing: "0.09em",
      textTransform: "uppercase",
      color: "#fff",
      whiteSpace: "nowrap",
    }}
  >
    {icono}
    {children}
  </div>
);

/** El bloque de portada y cierre: a la izquierda y centrado en el alto del marco.
 *  Arranca en x 120: el marco de la portada cierra por la izquierda en x 50 y
 *  nada va a menos de 70 px del filete (R-34). */
const AlaIzquierda: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      position: "absolute",
      left: 120,
      width: 860,
      top: 200,
      height: 1284 - 200 - 80,
      display: "flex",
      flexDirection: "column",
      alignItems: "flex-start",
      justifyContent: "center",
      textAlign: "left",
      color: "#fff",
      textShadow: "0 2px 24px rgba(0,0,0,0.5)",
    }}
  >
    {children}
  </div>
);

const IvyIzq: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div
    style={{
      fontFamily: SERIF,
      fontStyle: "italic",
      fontWeight: 500,
      fontSize: IVY,
      lineHeight: 1.12,
      textTransform: "uppercase",
      whiteSpace: "nowrap",
    }}
  >
    {children}
  </div>
);

const M1: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    {/* ⭐ Diego, 01-10, comentario en Drive sobre esta portada: *«cambiar imagen, pon
        una toma dron de Tierra Calma, que se vea real pero calidad profesional»*.
        Es la aérea REAL DJI_0318 del rodaje del 07-08 —la ladera con su camino de
        ripio y el llano de Padre Hurtado al fondo—, con cambio mínimo: sin la
        bruma de esa mañana y con luz limpia. No se agregó ni se quitó nada (R-24);
        el corte de tierra de arriba a la derecha es del lugar.
        🗄️ Antes hubo tres portadas generadas (banca, cerco, arboleda): dos se
        cayeron por parecerse a fondos de octubre. Ésta mide +0,81 como máximo
        contra cualquier otra imagen de los dos meses (umbral 0,85).
        El velo va alto, como en la portada de la referencia: la aérea es toda
        textura y el titular tiene que leerse encima. */}
    <Foto src={NOV("m-dron")} />
    <Degradado arriba={0.56} abajo={0.4} velo={0.3} />
    <Marco archivo="MARCO-CARRUSEL-1" />
    <AlaIzquierda>
      <div style={{fontFamily: SANS, fontWeight: 300, fontSize: cuerpoSans("Antes de comprar tu parcela,"), lineHeight: 1.16}}>
        Antes de comprar
        <br />
        tu parcela,
      </div>
      <Aire h={14} />
      <IvyIzq>lee esto</IvyIzq>
      <Aire h={40} />
      <Capsula>Tierra Calma · Padre Hurtado</Capsula>
    </AlaIzquierda>
  </Lienzo>
);

const M2: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={NOV("m-escritorio")} />
    <Degradado arriba={0.5} abajo={0.56} velo={0.24} />
    <Marco archivo="MARCO-CARRUSEL-2" />
    <NotaApp titulo="Dato nacional">
      <Punto>
        La tasa hipotecaria promedio en Chile llegó a <Sub>3,97%</Sub> en junio de 2026, entre las más bajas
        desde 2021.
      </Punto>
    </NotaApp>
    <Pie y={1156}>Fuente: Banco Central de Chile, vía Emol (07/07/2026).</Pie>
  </Lienzo>
);

const M3: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={NOV("m-llaves")} />
    <Degradado arriba={0.5} abajo={0.5} velo={0.24} />
    <Marco archivo="MARCO-CARRUSEL-3" />
    <NotaApp titulo="Formas de pago">
      <div style={{marginTop: 22, fontFamily: SANS, fontWeight: 300, fontSize: 38, lineHeight: 1.32, color: NAVY}}>
        {sinPartir("En Tierra Calma puedes comprar con")}
      </div>
      <Punto>
        <Sub>crédito hipotecario</Sub>,
      </Punto>
      <Punto>
        <Sub>contado</Sub>
      </Punto>
      <Punto>
        o <Sub>leasing</Sub>.
      </Punto>
    </NotaApp>
  </Lienzo>
);

const M4: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={NOV("m-agenda")} />
    <Degradado arriba={0.5} abajo={0.5} velo={0.24} />
    <Marco archivo="MARCO-CARRUSEL-2" />
    <NotaApp titulo="Pie">
      <Punto>
        Paga el pie en <Sub>hasta 24 cuotas</Sub>{" "}
        <span style={{whiteSpace: "nowrap"}}>(hasta UF 800).</span>
      </Punto>
    </NotaApp>
  </Lienzo>
);

const M5: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={NOV("m-sobre")} />
    <Degradado arriba={0.5} abajo={0.5} velo={0.24} />
    <Marco archivo="MARCO-CARRUSEL-3" />
    <NotaApp titulo="Reserva">
      <Punto>
        Reservas con <Sub>$1.000.000</Sub>, que se abona al total y se devuelve si el banco no aprueba tu crédito.
      </Punto>
    </NotaApp>
  </Lienzo>
);

const M6: React.FC = () => (
  <Lienzo w={CARR.w} h={CARR.h}>
    <Foto src={NOV("m-camino")} />
    <Degradado arriba={0.56} abajo={0.56} velo={0.26} />
    <Marco archivo="MARCO-CARRUSEL-4" />
    <AlaIzquierda>
      {/* Constanza Lizana, 02-10: *«debe ser de la tipografía de la marca y no tan
          separadas las letras entre sí, se ve muy IA»*. Era un rótulo de sans en
          versales con tracking 0,2em; pasa a IvyOra versales con el tracking de
          todo destacado de la marca (0,01em). */}
      <div style={{fontFamily: SERIF, fontWeight: 500, fontSize: 44, lineHeight: 1.14, letterSpacing: "0.01em", textTransform: "uppercase", color: ARENA}}>
        {sinPartir("Parcelas en Padre Hurtado")}
      </div>
      <Aire h={10} />
      <div style={{fontFamily: SANS, fontWeight: 300, fontSize: 40, lineHeight: 1.3}}>
        {sinPartir("~5.000 m² · ROL individual · Desde UF 2.500")}
      </div>
      <Aire h={52} />
      <div style={{fontFamily: SANS, fontWeight: 300, fontSize: cuerpoSans("Trabajamos con todos los bancos y te asesoramos."), lineHeight: 1.16}}>
        Trabajamos con
        <br />
        todos los bancos
      </div>
      <Aire h={14} />
      <IvyIzq>y te asesoramos.</IvyIzq>
      <Aire h={44} />
      <Capsula size={22} icono={<IWsp s={27} />}>
        Revisa tu caso con nuestro equipo por WhatsApp
      </Capsula>
    </AlaIzquierda>
  </Lienzo>
);

// =============================================================================
// Agrupadores — un frame = una pieza, se rinden con `--sequence`
// =============================================================================

export const NOV_CARR_E = [E1, E2, E3, E4, E5];
export const NOV_CARR_F = [F1, F2, F3, F4, F5, F6, F7];
export const NOV_CARR_M = [M1, M2, M3, M4, M5, M6];
export const NOV_POSTS = [H, K];
export const NOV_STORIES = [G, J, L];

export const NovCarrE: React.FC = () => <Serie piezas={NOV_CARR_E} />;
export const NovCarrF: React.FC = () => <Serie piezas={NOV_CARR_F} />;
export const NovCarrM: React.FC = () => <Serie piezas={NOV_CARR_M} />;
export const NovPosts: React.FC = () => <Serie piezas={NOV_POSTS} />;
export const NovStories: React.FC = () => <Serie piezas={NOV_STORIES} />;
