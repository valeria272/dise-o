// ============================================================================
// HERO — las tres piezas que fijan el estándar de la cuenta (24-09-2026)
// ----------------------------------------------------------------------------
// Board: creative-system/FEED-12/BOARD.md §D. Una pieza = una función:
//   HeroGoma       CONCEPTO   · Seedream 5 Pro (out/copylab/hero/h1/seedream-a.png).
//                  Mystic salió dos veces con LÁPIZ: el prompt v2 prohíbe
//                  cualquier objeto que no sea hoja, goma, migas y mano.
//   HeroNadie01    CULTURA    · ⚠️ RECREACIÓN con Nano Banana Pro. NO SE PUBLICA:
//                  la propiedad exige un cartel real fotografiado. Sirve para
//                  aprobar encuadre y terminación. Lleva el sello en el arte.
//   HeroSantaGota  TRABAJO    · cuadro real del seg. 7 del spot + Magnific
//                  Precision 2×. Sólo crédito verificable: «spot para TVN».
// ============================================================================
import React from "react";
import {C, asegurarFuentes, VOZ} from "../../brand/copylab/sistema";
import {Pieza, Foto, Velo} from "../../brand/copylab/lienzo";

const M = 72;

const mono: React.CSSProperties = {
  fontFamily: VOZ.data, fontSize: 22, lineHeight: 1.35, letterSpacing: "0.12em",
  textTransform: "uppercase",
};

export const HeroGoma: React.FC = () => {
  asegurarFuentes();
  return (
    <Pieza fondo={C.tinta} grano={0.16}>
      <Foto src="assets/copylab/hero/h1-goma.jpg" grado="crudo" />
      <Velo desde="arriba" fuerza={0.55} corte={0.8} />
      <div style={{
        position: "absolute", left: M, top: 64, fontFamily: VOZ.narrow, fontWeight: 700,
        fontSize: 100, lineHeight: 0.9, letterSpacing: "-0.01em", color: C.offwhite, textTransform: "uppercase",
      }}>
        Escribir<br />es fácil.
      </div>
      <div style={{
        position: "absolute", left: M, bottom: 118, fontFamily: VOZ.editorial, fontStyle: "italic",
        fontSize: 54, lineHeight: 1.04, color: C.rosa,
      }}>
        Lo difícil es saber<br />qué borrar.
      </div>
    </Pieza>
  );
};

export const HeroNadie01: React.FC = () => {
  asegurarFuentes();
  return (
    <Pieza fondo={C.tinta} grano={0.2}>
      <Foto src="assets/copylab/hero/h2-recreacion.jpg" grado="crudo" />
      <Velo desde="abajo" fuerza={0.5} corte={0.82} />
      <div style={{...mono, position: "absolute", left: M, bottom: 92, color: C.offwhite}}>
        Nadie lo firmó · Nº01<br />Santiago
      </div>
      {/* Sello de revisión interna. Se quita sólo cuando la foto sea REAL. */}
      <div style={{
        ...mono, position: "absolute", right: 0, top: 0, background: C.tinta, color: C.rosa,
        padding: "14px 20px", fontSize: 18,
      }}>
        Recreación · no se publica
      </div>
    </Pieza>
  );
};

export const HeroSantaGota: React.FC = () => {
  asegurarFuentes();
  return (
    <Pieza fondo={C.tinta} grano={0.1}>
      <Foto src="assets/copylab/hero/h3-santagota.jpg" grado="crudo" />
      <Velo desde="abajo" fuerza={0.6} corte={0.76} />
      <div style={{...mono, position: "absolute", left: M, bottom: 92, color: C.offwhite}}>
        Santa Gota<br />Spot para TVN · 2026
      </div>
    </Pieza>
  );
};
