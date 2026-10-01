// ============================================================================
// COPYWRITERS · CW-01 — «ASÍ PREPARAMOS UN CYBER.» · carrusel de 5 láminas
// ----------------------------------------------------------------------------
// BRIEF     clients/copywriters/briefs/202610_BRIEF_ESTUDIO_copywriters.md (CW-01).
//           Pilar «Cómo trabajamos», tipo IA / proceso → BEIGE. Sale 01-10 18:00.
// DIRECCIÓN Tipográfico sobre negro. Lo que manda es la SECUENCIA: el tiempo
//           (3 semanas → 1 semana → durante → después) es el diseño, así que el
//           número de cada etapa es el héroe y va en `bloque`, en beige.
//           · Beige = taxonomía de proceso: rótulo y números de etapa.
//           · Rosa = una sola cosa por lámina, la que decide la frase (R-25).
//           · Balloon UNA vez en el carrusel, en el remate final y sin caja
//             (jefa de diseño 01-10: nada de recuadro rosado con Balloon).
//           · Sin mono (jefa de diseño: «se ve IA»). El rótulo va en Bebas.
//           · Todo centrado en su caja (jefa de diseño, 01-10).
// PANTALLA  L4 lleva UNA pantalla real: la tabla de campañas de Paid Media Pro
//           (nuestro dashboard), capturada el 01-10, en gris y difuminada hasta
//           que no se lee ni una cifra ni una marca. Cruda en
//           raw/copywriters/202610/pantalla-campanas-paidmediapro-01-10.png.
// NADA      de personas, marcas de clientes ni cifras (no hay dato que mostrar).
// Formato 1080×1350.
// ============================================================================
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {C2, VOZ2, SOMBRA_SOBRE_FOTO, asegurarFuentesV2, granoSVG} from "../../brand/copylab/sistemaV2";
import {Linea, Trazo} from "../../brand/copylab/piezasV2";

const ANCHO_TEXTO = 820;

/** Columna centrada en el lienzo, un poco sobre el centro (feed: abajo 135). */
const Centro: React.FC<{children: React.ReactNode; gap?: number; sube?: number}> =
({children, gap = 0, sube = 40}) => (
  <AbsoluteFill style={{
    display: "flex", flexDirection: "column", alignItems: "center",
    justifyContent: "center", gap, paddingBottom: sube * 2, textAlign: "center",
  }}>{children}</AbsoluteFill>
);

/** Cuerpo en caja mixta — Neue Haas Text. */
const Cuerpo: React.FC<{children: React.ReactNode; px?: number; color?: string;
                        ancho?: number}> =
({children, px = 46, color = "rgba(245,243,238,0.9)", ancho = ANCHO_TEXTO}) => (
  <div style={{
    fontFamily: VOZ2.cuerpo, fontWeight: 400, fontSize: px, lineHeight: 1.32,
    color, width: ancho, letterSpacing: 0.1,
  }}>{children}</div>
);

const Negro: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{background: C2.negro}}>
    <AbsoluteFill style={{backgroundImage: granoSVG(0.055, 5), backgroundSize: "300px 300px"}} />
    {children}
  </AbsoluteFill>
);

/** Número de etapa: el héroe de las láminas de tiempo. */
const Etapa: React.FC<{n: string; resto: string}> = ({n, resto}) => (
  <div style={{display: "flex", flexDirection: "column", alignItems: "center"}}>
    <Linea cuerpo={480} voz="bloque" color={C2.beige}>{n}</Linea>
    <div style={{marginTop: 18}}>
      <Linea cuerpo={116} tracking={1}>{resto}</Linea>
    </div>
  </div>
);

// ====================== 01 · PORTADA ======================
const L1: React.FC = () => (
  <Negro>
    <Centro gap={0}>
      <div style={{marginBottom: 70}}>
        <Linea cuerpo={48} voz="titular" color={C2.beige} tracking={7}>
          05—07.10 · CYBERMONDAY
        </Linea>
      </div>
      <Linea cuerpo={300} voz="bloque" color={C2.rosa}>ASÍ</Linea>
      <div style={{height: 14}} />
      <Linea cuerpo={190}>PREPARAMOS</Linea>
      <div style={{height: 14}} />
      <Linea cuerpo={190}>UN CYBER.</Linea>
    </Centro>
  </Negro>
);

// ====================== 02 · 3 SEMANAS ANTES ======================
const L2: React.FC = () => (
  <Negro>
    <Centro>
      <Etapa n="3" resto="SEMANAS ANTES." />
      <div style={{height: 64}} />
      <Cuerpo>Qué producto empuja cada marca, para quién y con qué oferta.</Cuerpo>
      <div style={{height: 56}} />
      <Linea cuerpo={70} tracking={0.5}>LO QUE NO SE DECIDE AHÍ,</Linea>
      <div style={{height: 12}} />
      <Linea cuerpo={70} color={C2.rosa} tracking={0.5}>NO SE ARREGLA EL LUNES.</Linea>
    </Centro>
  </Negro>
);

// ====================== 03 · 1 SEMANA ANTES ======================
const L3: React.FC = () => (
  <Negro>
    <Centro>
      <Etapa n="1" resto="SEMANA ANTES." />
      <div style={{height: 64}} />
      <Cuerpo>Las piezas, en tres tiempos:</Cuerpo>
      <div style={{height: 34}} />
      <Linea cuerpo={88}>ANTICIPACIÓN.</Linea>
      <div style={{height: 16}} />
      <Linea cuerpo={88}>DURANTE.</Linea>
      <div style={{height: 16}} />
      <Linea cuerpo={88} color={C2.rosa}>ÚLTIMAS HORAS.</Linea>
      <div style={{height: 46}} />
      <Cuerpo>El último día también vende.</Cuerpo>
    </Centro>
  </Negro>
);

// ====================== 04 · DURANTE — LA PANTALLA ======================
const L4: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Img src={staticFile("assets/copywriters/202610/cw01-pantalla-difuminada.png")}
         style={{position: "absolute", inset: 0, width: "100%", height: "100%",
                 objectFit: "cover", objectPosition: "50% 50%",
                 transform: "scale(1.06)", opacity: 0.9}} />
    {/* La pantalla ya viene virada a tinta→beige (sin el violeta de la app):
        entra en la taxonomía de proceso y deja de ser el blanco frío de una app. */}
    {/* Velo donde va el texto, no sobre toda la pantalla. */}
    <AbsoluteFill style={{
      background: "radial-gradient(ellipse 72% 52% at 50% 47%, rgba(11,11,11,0.9) 0%, rgba(11,11,11,0.72) 50%, rgba(11,11,11,0.18) 100%)",
    }} />
    <AbsoluteFill style={{backgroundImage: granoSVG(0.06, 5), backgroundSize: "300px 300px"}} />
    <Centro>
      <Linea cuerpo={70} color={C2.beige} tracking={3} sombra>DURANTE.</Linea>
      <div style={{height: 54}} />
      <Linea cuerpo={118} sombra>EL PRESUPUESTO</Linea>
      <div style={{height: 10}} />
      <Linea cuerpo={118} sombra>SE MUEVE SEGÚN</Linea>
      <div style={{height: 10}} />
      <Linea cuerpo={118} sombra>CÓMO RESPONDE</Linea>
      <div style={{height: 10}} />
      <Linea cuerpo={118} color={C2.rosa} sombra>CADA HORA.</Linea>
      <div style={{height: 54}} />
      <div style={{textShadow: SOMBRA_SOBRE_FOTO}}>
        <Cuerpo>No según el plan de hace un mes.</Cuerpo>
      </div>
    </Centro>
  </AbsoluteFill>
);

// ====================== 05 · DESPUÉS — EL REMATE ======================
const L5: React.FC = () => (
  <AbsoluteFill style={{background: C2.offwhite}}>
    <AbsoluteFill style={{backgroundImage: granoSVG(0.09, 11), backgroundSize: "300px 300px"}} />
    <Centro>
      <Linea cuerpo={70} color={C2.carbon} tracking={3}>DESPUÉS.</Linea>
      <div style={{height: 46}} />
      <Cuerpo color={C2.negro}>
        El informe sale con lo que aprendimos, no sólo con lo que vendimos.
      </Cuerpo>
      <div style={{height: 96}} />
      <div style={{position: "relative", fontFamily: VOZ2.mano, fontWeight: 800,
                   fontSize: 134, lineHeight: 1.02, color: C2.rosa,
                   textTransform: "uppercase", transform: "rotate(-2deg)"}}>
        EL CYBER SE GANA<br />ANTES DEL CYBER.
        <Trazo x={210} y={262} ancho={620} grosor={24} giro={-1} />
      </div>
    </Centro>
  </AbsoluteFill>
);

const LAMINAS = [L1, L2, L3, L4, L5];

export const CW01Cyber: React.FC<{lamina?: number}> = ({lamina = 1}) => {
  asegurarFuentesV2();
  const L = LAMINAS[Math.min(Math.max(lamina, 1), LAMINAS.length) - 1];
  return <L />;
};
