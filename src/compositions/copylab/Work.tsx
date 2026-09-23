// ============================================================================
// 03 · WORK — Cava Morandé
// ----------------------------------------------------------------------------
// REGLA    WORK muestra el trabajo del cliente COMO PUBLICIDAD, nunca como
//          ficha de portafolio. No hay «cliente / servicio / resultado».
//          La estética la manda el universo del cliente; Copywriters sólo
//          agrega una capa editorial mínima.
// POR ESO  Acá la voz que titula es la EDITORIAL, no la de impacto: el mundo
//          de Cava es cálido y sereno, y gritarle en condensada negra sería
//          imponerle el sistema de la agencia encima. En la pieza de Traverso
//          la decisión sería la contraria.
// PRODUCTO La botella es el packshot REAL del e-commerce del cliente
//          (public/assets/cava/bottles/2x/), recortada a su alfa. La IA hizo
//          SÓLO el ambiente. Regla dura: docs/SISTEMA-DE-MARCAS.md §2 — la IA
//          nunca hace el producto, ni el logo, ni un dato.
// LUZ      El ambiente viene iluminado desde arriba a la derecha, así que la
//          sombra de contacto cae hacia la IZQUIERDA. Sin eso el packshot
//          flota y la pieza se lee como collage.
// ANOMALÍA Ninguna tipográfica. La composición asimétrica 50/50 (texto a la
//          izquierda en la banda oscura, botella a la derecha) ya es la
//          decisión fuerte.
// ============================================================================
import React from "react";
import {Img, useVideoConfig} from "remotion";
import {C, asegurarFuentes, margen, src} from "../../brand/copylab/sistema";
import {Bloque, Indice} from "../../brand/copylab/tipografia";
import {Pieza, Foto} from "../../brand/copylab/lienzo";

export const Work: React.FC = () => {
  asegurarFuentes();
  const {width: W} = useVideoConfig();
  const M = margen(W);

  const altoBotella = 800;
  const anchoBotella = altoBotella * 0.384;   // aspecto medido del recorte alfa
  const baseBotella = 1162;                   // dónde apoya sobre la mesa
  const xBotella = 700;

  return (
    <Pieza fondo={C.tinta} grano={0.2}>
      <Foto src="assets/copylab/work/cava-ambiente-01.png" grado="crudo" encuadre="50% 50%" />

      {/* Sombra de contacto: elipse ancha, desplazada a la izquierda porque la
          práctica del ambiente entra por la derecha. Dos capas — una dura y
          corta al pie, otra larga y difusa — que es como cae una sombra real. */}
      <div
        style={{
          position: "absolute",
          left: xBotella - anchoBotella * 0.55,
          top: baseBotella - 34,
          width: anchoBotella * 2.5,
          height: 96,
          background: "radial-gradient(ellipse at 62% 50%, rgba(6,4,2,0.78) 0%, rgba(6,4,2,0.34) 42%, rgba(6,4,2,0) 72%)",
          filter: "blur(9px)",
        }}
      />
      <div
        style={{
          position: "absolute",
          left: xBotella - anchoBotella * 0.1,
          top: baseBotella - 16,
          width: anchoBotella * 1.2,
          height: 34,
          background: "radial-gradient(ellipse at 50% 40%, rgba(4,2,1,0.9) 0%, rgba(4,2,1,0) 78%)",
          filter: "blur(4px)",
        }}
      />

      <Img
        src={src("assets/copylab/work/cava-botella.png")}
        style={{
          position: "absolute",
          left: xBotella, top: baseBotella - altoBotella,
          width: anchoBotella, height: altoBotella,
        }}
      />

      <Indice familia="Work" ref="Cava Morandé" style={{position: "absolute", left: M, top: M}} />

      <div style={{position: "absolute", left: M, top: 296, width: 620}}>
        <Bloque
          base={112}
          sangria={0.02}
          lineas={[
            {t: "Nadie brinda", voz: "editorial"},
            {t: "por un", voz: "editorial"},
            {t: "descuento.", voz: "editorial", color: C.rosa},
          ]}
        />
      </div>
    </Pieza>
  );
};
