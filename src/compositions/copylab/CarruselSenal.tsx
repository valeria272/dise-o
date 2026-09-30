// ============================================================================
// COPYWRITERS · CARRUSEL «SEÑAL» — prueba del Sistema Visual del 29-09-2026
// ----------------------------------------------------------------------------
// DIRECCIÓN DE ARTE
//
// Territorio: EDITORIAL (negro), el que el board asigna a «insight, tendencias,
// opinión». Es una opinión de la agencia, no un caso: por eso no hay una sola
// cifra en las cinco láminas.
//
// El carrusel alterna DOS mundos y ése es todo el ritmo:
//   · las láminas impares son NEGRO PLENO y tipografía gigante — la voz alta;
//   · las pares son PAPEL sobre negro, con cinta y anotación a mano — la voz baja.
// Se lee como alguien que afirma algo fuerte y después lo anota al margen.
//
// El rosa aparece UNA vez por lámina y siempre sobre la palabra que decide la
// frase: «OTRO REEL.», «CRITERIO.», «OTRO COPY.», «DIRIGEN.». Si se borra el
// rosa, la frase cambia de sentido — ésa es la prueba de que no es adorno.
//
// Los cinco copys son LITERALES del board entregado por Valeria el 29-09. No se
// escribió ninguno nuevo: esta pieza prueba el sistema, no propone mensajes.
//
// Formato: 1080×1350 (feed 4:5). Cinco láminas.
//
// 30-09: se eliminaron paginación («SEÑAL», «VOL. 027», «02 — EL PRINCIPIO»),
// la firma COPYWRITERS.CL en cada lámina y el «TODAVÍA.» colgado — ley de
// DIRECCION-DE-ARTE-RRSS.md §2.
// ============================================================================
import React from "react";
import {AbsoluteFill} from "remotion";
import {
  C2,
  VOZ2,
  asegurarFuentesV2,
  granoSVG,
  pathSubrayado,
  pathsFlecha,
} from "../../brand/copylab/sistemaV2";

const H = 1350;
const M = 80; // margen base — punto de partida, no retícula

// ---------------------------------------------------------------------------
// Piezas del kit gráfico
// ---------------------------------------------------------------------------

/** Subrayado de marcador. Cruza por debajo de la palabra que manda. */
const Subrayado: React.FC<{
  x: number; y: number; ancho: number; alto?: number; color?: string; grosor?: number;
}> = ({x, y, ancho, alto = 34, color = C2.rosa, grosor = 13}) => (
  <svg
    width={ancho} height={alto}
    style={{position: "absolute", left: x, top: y, overflow: "visible"}}
  >
    <path
      d={pathSubrayado(ancho, alto)}
      stroke={color} strokeWidth={grosor} strokeLinecap="round" fill="none"
    />
  </svg>
);

/** Flecha de anotación: cuerpo curvo + dos plumas. Nunca un icono. */
const Flecha: React.FC<{
  x: number; y: number; ancho: number; alto: number; giro?: number; color?: string;
}> = ({x, y, ancho, alto, giro = 0, color = C2.rosa}) => {
  const p = pathsFlecha(ancho, alto);
  return (
    <svg
      width={ancho} height={alto}
      style={{position: "absolute", left: x, top: y, overflow: "visible",
              transform: `rotate(${giro}deg)`}}
    >
      {[p.cuerpo, p.pluma1, p.pluma2].map((d, i) => (
        <path key={i} d={d} stroke={color} strokeWidth={9}
              strokeLinecap="round" fill="none" />
      ))}
    </svg>
  );
};

/** Cinta adhesiva: gris translúcida, girada, con los bordes irregulares. */
const Cinta: React.FC<{
  x: number; y: number; ancho: number; alto: number; giro: number; color?: string;
}> = ({x, y, ancho, alto, giro, color = "rgba(184,184,184,0.62)"}) => (
  <div
    style={{
      position: "absolute", left: x, top: y, width: ancho, height: alto,
      background: color,
      backgroundImage: granoSVG(0.24, 3),
      transform: `rotate(${giro}deg)`,
      clipPath:
        "polygon(2% 6%, 99% 0%, 98% 94%, 1% 100%)",
      boxShadow: "0 2px 10px rgba(0,0,0,0.3)",
    }}
  />
);

/** Hoja de papel: el soporte donde vive la voz baja del carrusel. */
const Papel: React.FC<{
  x: number; y: number; ancho: number; alto: number; giro: number;
  children: React.ReactNode;
}> = ({x, y, ancho, alto, giro, children}) => (
  <div
    style={{
      position: "absolute", left: x, top: y, width: ancho, height: alto,
      background: C2.offwhite,
      backgroundImage: granoSVG(0.1, 11),
      transform: `rotate(${giro}deg)`,
      boxShadow: "0 28px 70px rgba(0,0,0,0.55)",
    }}
  >
    {children}
  </div>
);

/** Rótulo mono al pie o a la cabeza. Nunca es héroe. */
/** Fondo negro con grano editorial. */
const FondoNegro: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{background: C2.negro}}>
    <AbsoluteFill
      style={{backgroundImage: granoSVG(0.055, 5), backgroundSize: "300px 300px"}}
    />
    {children}
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------
// Titular Bebas: una línea, un tamaño, sin sorpresas.
// ---------------------------------------------------------------------------
const Linea: React.FC<{
  children: React.ReactNode; cuerpo: number; color?: string;
}> = ({children, cuerpo, color = C2.offwhite}) => (
  <div
    style={{
      fontFamily: VOZ2.titular, fontWeight: 700, fontSize: cuerpo, lineHeight: 0.86,
      color, textTransform: "uppercase", letterSpacing: 0,
      whiteSpace: "nowrap",
    }}
  >
    {children}
  </div>
);

// ===========================================================================
// LÁMINA 1 — negro pleno. El golpe. Calco de la referencia del board.
// ===========================================================================
const L1: React.FC = () => (
  <FondoNegro>
    <div style={{position: "absolute", left: M, top: 268}}>
      <Linea cuerpo={192}>TU MARCA</Linea>
      <Linea cuerpo={192}>NO NECESITA</Linea>
      <Linea cuerpo={192} color={C2.rosa}>OTRO REEL.</Linea>
      <Linea cuerpo={192}>NECESITA</Linea>
      <Linea cuerpo={192}>UNA IDEA.</Linea>
    </div>

    {/* El subrayado va SIEMPRE bajo la línea de base, nunca sobre la letra:
        cruzando la palabra deja de ser subrayado y se lee como tachado. */}
    <Subrayado x={M - 6} y={1106} ancho={648} alto={40} grosor={16} />
  </FondoNegro>
);

// ===========================================================================
// LÁMINA 2 — papel sobre negro. La voz baja: se anota lo que se acaba de decir.
// ===========================================================================
const L2: React.FC = () => (
  <FondoNegro>
    <Papel x={92} y={188} ancho={896} alto={980} giro={-1.6}>
      <div style={{position: "absolute", left: 76, top: 170}}>
        <div
          style={{
            fontFamily: VOZ2.cuerpo, fontWeight: 400, fontSize: 112,
            lineHeight: 1.1, color: C2.negro, textTransform: "uppercase",
            letterSpacing: -1,
          }}
        >
          MENOS<br />RUIDO.<br />MÁS<br />CRITERIO.
        </div>
      </div>
      <Subrayado x={68} y={660} ancho={438} alto={38} grosor={14} />
    </Papel>

    <Cinta x={330} y={150} ancho={230} alto={74} giro={-3.5}
           color="rgba(255,61,156,0.78)" />

  </FondoNegro>
);

// ===========================================================================
// LÁMINA 3 — off-white pleno. Se invierte el peso: negro sobre claro.
// ===========================================================================
const L3: React.FC = () => (
  <AbsoluteFill style={{background: C2.offwhite}}>
    <AbsoluteFill
      style={{backgroundImage: granoSVG(0.085, 9), backgroundSize: "300px 300px"}}
    />
    <div style={{position: "absolute", left: M, top: 430}}>
      <Linea cuerpo={168} color={C2.negro}>MISMA PAUTA.</Linea>
      <Linea cuerpo={168} color={C2.rosa}>OTRO COPY.</Linea>
    </div>

    <div
      style={{
        position: "absolute", left: M + 8, top: 790,
        fontFamily: VOZ2.mano, fontSize: 58, fontWeight: 700,
        color: C2.negro, transform: "rotate(-2deg)", lineHeight: 1.05,
        textTransform: "uppercase",
      }}
    >
      EL PRESUPUESTO NO CAMBIÓ.
    </div>

    <Flecha x={664} y={886} ancho={176} alto={126} giro={8} />

  </AbsoluteFill>
);

// ===========================================================================
// LÁMINA 4 — negro. La única lámina donde la mano sostiene el titular.
// ===========================================================================
const L4: React.FC = () => (
  <FondoNegro>
    <div style={{position: "absolute", left: M, top: 470}}>
      <Linea cuerpo={164}>LA IA ACELERA.</Linea>
      <Linea cuerpo={164}>LAS IDEAS</Linea>
      <Linea cuerpo={164} color={C2.rosa}>DIRIGEN.</Linea>
    </div>

    <Subrayado x={M - 4} y={908} ancho={468} alto={38} grosor={14} />

    <div
      style={{
        position: "absolute", left: 596, top: 968,
        fontFamily: VOZ2.mano, fontSize: 56, fontWeight: 700,
        color: C2.offwhite, transform: "rotate(-2deg)", lineHeight: 1.08,
        textAlign: "right", textTransform: "uppercase",
      }}
    >
      TODAVÍA.
    </div>

  </FondoNegro>
);

// ===========================================================================
// LÁMINA 5 — cierre. Sólo la mano y la firma. Nada de CTA.
// ===========================================================================
const L5: React.FC = () => (
  <FondoNegro>
    <div
      style={{
        position: "absolute", left: M, top: 318,
        fontFamily: VOZ2.mano, fontSize: 122, fontWeight: 700,
        color: C2.rosa, lineHeight: 1.16, transform: "rotate(-2deg)",
        textTransform: "uppercase",
      }}
    >
      IDEAS.<br />PERSONAS.<br />MARCAS.<br />RESULTADOS<br />REALES.
    </div>

    <Subrayado x={M + 6} y={1044} ancho={396} alto={40} grosor={15} color={C2.offwhite} />

    <div
      style={{
        position: "absolute", left: M, top: H - M - 74,
        fontFamily: VOZ2.titular, fontSize: 58, color: C2.offwhite,
        textTransform: "uppercase", letterSpacing: 2,
      }}
    >
      COPYWRITERS.CL
    </div>
  </FondoNegro>
);

// ---------------------------------------------------------------------------

const LAMINAS = [L1, L2, L3, L4, L5];

export const CarruselSenal: React.FC<{lamina?: number}> = ({lamina = 1}) => {
  asegurarFuentesV2();
  const L = LAMINAS[Math.min(Math.max(lamina, 1), LAMINAS.length) - 1];
  return <L />;
};

export const CARRUSEL_SENAL_LAMINAS = LAMINAS.length;
