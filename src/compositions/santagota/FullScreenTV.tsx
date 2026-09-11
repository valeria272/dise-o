// ============================================================================
// SANTA GOTA · KV 03 — FULL SCREEN · 1920×1080 · 29,97 · MXF · hasta 20 s
// ----------------------------------------------------------------------------
// IDEA      No se estira el vertical: la monja se RECORTA y se planta sobre un
//           campo lima, a tamaño real, con la sartén de pasta en la mano y su
//           halo. La frase gigante ocupa el resto del cuadro en tinta botella
//           (el par del envase: etiqueta lima + botella oscura).
// LECTURA   EL ACEITE / QUE LLEGÓ A / REVOLUCIONAR / TU COCINA. — la palabra
//           grande es la del concepto y el plumón naranja la subraya y sigue
//           por detrás de la monja: gráfica y personaje se tocan ahí.
// FASE 2    Este es el frame de 8–13 s (construcción gráfica). El hook 0–3 s y
//           el montaje 3–8 s usan el video del reel dentro de la misma lógica
//           (columna 9:16 sobre lima); el cierre es SG-Cierre.
// AIRE      La mitad derecha es la monja; la izquierda, la frase. Sin más.
// ============================================================================
import React from "react";
import {AbsoluteFill} from "remotion";
import {santagota as SG} from "../../brand/santagota";
import {Halo, Trazo, Monja, MONJA, Titular, LogoPlano, useSantaGota} from "../../brand/santagotaUI";

export const FullScreenTV: React.FC = () => {
  const C = useSantaGota();
  const {height: H} = SG.formatos.full;

  // Monja a 0,95: el cuadro corta justo bajo la sartén (el borde desvanecido
  // del recorte queda fuera). Cabeza en x=1540.
  const s = 0.95;
  const ty = 1080 - (MONJA.sartenBase + 40) * s;
  const tx = 1540 - MONJA.cabezaCx * s;

  const M = 110;
  const yTexto = 226;

  return (
    <AbsoluteFill style={{background: C.lima, overflow: "hidden"}}>
      {/* La frase (detrás de la monja) */}
      <div style={{position: "absolute", left: M, top: yTexto, zIndex: 1}}>
        <Titular size={112}>El aceite</Titular>
        <Titular size={112}>que llegó a</Titular>
        <Titular size={134} weight={900} style={{marginTop: 8}}>Revolucionar</Titular>
        <Titular size={112} style={{marginTop: 24}}>tu cocina.</Titular>
      </div>
      {/* El plumón sigue por detrás de la monja */}
      <Trazo x={M - 6} y={yTexto + 110 + 110 + 8 + 128} w={1400} grosor={16} />

      {/* El personaje */}
      <Monja s={s} tx={tx} ty={ty} z={2} />
      <Halo cx={1540} cy={MONJA.cabezaTop * s + ty - 42} w={190} h={44} grosor={8} />

      {/* La marca, plana, como en el feed (allá blanca sobre foto; acá botella sobre lima) */}
      <LogoPlano x={M} y={H - 58 - 145} w={230} tono="botella" />
    </AbsoluteFill>
  );
};
