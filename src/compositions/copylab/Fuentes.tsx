// ============================================================================
// FUENTES — comparativa de la voz HERO (24-09-2026)
// ----------------------------------------------------------------------------
// Mismo titular, mismo lienzo, misma composición, mismo cuerpo: SÓLO cambia la
// fuente. Las cuatro vienen de Adobe Fonts activadas en este Mac (Creative
// Cloud) y Chrome las lee como fuentes del sistema: no se descarga nada.
// Si una no está activada, la pieza lo DICE en rojo en vez de caer en silencio
// a una fuente de reemplazo (lección Brushwell).
// ============================================================================
import React, {useEffect, useState} from "react";
import {AbsoluteFill, continueRender, delayRender} from "remotion";
import {C, asegurarFuentes, VOZ} from "../../brand/copylab/sistema";

export type FuenteProps = {familia: string; peso: number; nombre: string; frase: 1 | 2};

const FRASES = {
  1: [["Buenos textos", false], ["venden", false], ["más.", true]],
  2: [["Ideas que", false], ["mueven", false], ["marcas.", true]],
} as const;

export const Fuente: React.FC<FuenteProps> = ({familia, peso, nombre, frase}) => {
  asegurarFuentes();
  const [ok, setOk] = useState<boolean | null>(null);
  const [h] = useState(() => delayRender("fuente " + familia));
  useEffect(() => {
    const f = (document as unknown as {fonts: {check: (s: string) => boolean; load: (s: string) => Promise<unknown>}}).fonts;
    const spec = `${peso} 100px "${familia}"`;
    f.load(spec).catch(() => null).finally(() => {
      setOk(f.check(spec) && document.fonts.check(spec));
      continueRender(h);
    });
  }, [familia, peso, h]);

  return (
    <AbsoluteFill style={{background: C.tinta, padding: 72}}>
      <div style={{position: "absolute", left: 72, top: 250}}>
        {FRASES[frase].map(([t, rosa], i) => (
          <div key={i} style={{
            fontFamily: `"${familia}", monospace`, fontWeight: peso, fontSize: i === 0 ? 150 : 250,
            lineHeight: 0.86, letterSpacing: "-0.01em", textTransform: "uppercase",
            color: rosa ? C.rosa : C.offwhite, whiteSpace: "nowrap",
          }}>{t}</div>
        ))}
      </div>
      <div style={{position: "absolute", left: 72, bottom: 64, fontFamily: VOZ.data, fontSize: 20,
        letterSpacing: "0.14em", textTransform: "uppercase", color: "rgba(242,244,246,0.7)"}}>
        {nombre}
      </div>
      {ok === false ? (
        <div style={{position: "absolute", right: 72, bottom: 64, fontFamily: VOZ.data, fontSize: 20,
          color: "#FF4D4D", letterSpacing: "0.1em"}}>NO ACTIVADA</div>
      ) : null}
    </AbsoluteFill>
  );
};
