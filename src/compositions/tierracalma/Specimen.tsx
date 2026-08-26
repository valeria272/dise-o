import React from "react";
import {AbsoluteFill} from "remotion";
import {tierracalma as TC, ensureTierraCalmaFonts} from "../../brand/tierracalma";

ensureTierraCalmaFonts();

// Muestrario del sistema tipográfico de Tierra Calma: IvyOra Display (Adobe
// Fonts, enlazada) + Inter Tight. Las filas de control existen para detectar
// si alguna cae a un fallback: si se ven iguales, la fuente no cargó.
const NAVY = TC.colors.navy;
const CREAM = TC.colors.cream;
const SAND = "#A8906B";

const Fila: React.FC<{et: string; st: React.CSSProperties; txt?: string}> = ({et, st, txt}) => (
  <div style={{display: "flex", alignItems: "baseline", gap: 28, borderBottom: `1px solid rgba(11,44,73,0.14)`, padding: "16px 0"}}>
    <span style={{fontFamily: "monospace", fontSize: 15, width: 250, color: "rgba(11,44,73,0.55)", flexShrink: 0}}>{et}</span>
    <span style={{color: NAVY, ...st}}>{txt ?? "Tierra Calma · 5.000 m² desde UF 2.500"}</span>
  </div>
);

export const Specimen: React.FC = () => (
  <AbsoluteFill style={{background: CREAM, padding: "48px 60px"}}>
    <div style={{fontFamily: TC.fonts.body, fontSize: 15, fontWeight: 600, letterSpacing: "0.24em", textTransform: "uppercase", color: SAND, marginBottom: 8}}>
      Tierra Calma · sistema tipográfico
    </div>
    <div style={{fontFamily: TC.fonts.display, fontSize: 46, color: NAVY, marginBottom: 20, letterSpacing: "-0.02em"}}>
      IvyOra Display <span style={{fontStyle: "italic"}}>+</span> Inter Tight
    </div>

    <Fila et="control · serif sistema" st={{fontFamily: "serif", fontSize: 40}} />
    <Fila et="IvyOra Display 300" st={{fontFamily: TC.fonts.display, fontWeight: 300, fontSize: 44}} />
    <Fila et="IvyOra Display 400" st={{fontFamily: TC.fonts.display, fontWeight: 400, fontSize: 44}} />
    <Fila et="IvyOra Display 400 itál." st={{fontFamily: TC.fonts.display, fontWeight: 400, fontStyle: "italic", fontSize: 44}} />
    <Fila et="IvyOra Display 500" st={{fontFamily: TC.fonts.display, fontWeight: 500, fontSize: 44}} />
    <Fila et="IvyOra Display 700" st={{fontFamily: TC.fonts.display, fontWeight: 700, fontSize: 44}} />

    <div style={{height: 22}} />
    <Fila et="control · Helvetica" st={{fontFamily: "Helvetica", fontSize: 26}} />
    <Fila et="Inter Tight 300" st={{fontFamily: TC.fonts.body, fontWeight: 300, fontSize: 26}} />
    <Fila et="Inter Tight 400" st={{fontFamily: TC.fonts.body, fontWeight: 400, fontSize: 26}} />
    <Fila et="Inter Tight 500" st={{fontFamily: TC.fonts.body, fontWeight: 500, fontSize: 26}} />
    <Fila et="Inter Tight 700" st={{fontFamily: TC.fonts.body, fontWeight: 700, fontSize: 26}} />
    <Fila
      et="Inter Tight 600 · etiqueta"
      st={{fontFamily: TC.fonts.body, fontWeight: 600, fontSize: 19, letterSpacing: "0.24em", textTransform: "uppercase"}}
      txt="Padre Hurtado · Región Metropolitana"
    />
  </AbsoluteFill>
);
