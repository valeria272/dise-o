// ============================================================================
// SANTA GOTA · KV 01 — HUINCHA TV · 1920×216 · TARGA + alfa · 7 s
// ----------------------------------------------------------------------------
// IDEA      La monja asoma desde la banda como desde la ventanilla de un
//           confesionario. No hay tiempo para un video: basta la cornette y los
//           lentes redondos, que son la firma del personaje. Sobre ella, el halo
//           del feed («Bendita sea»).
// LECTURA   Una frase en dos pesos, como el feed: «Llegó a» en Light y el
//           concepto en Black. El plumón naranja marca REVOLUCIONAR, la palabra
//           que carga la campaña.
// MARCA     Bloque botella a la derecha con el logo a color y la URL en lima.
//           Sobre la banda lima el logo a color desaparecería.
// AIRE      Cuatro cosas y nada más: monja · frase · trazo · marca.
// ⚠ ALFA    Todo lo que no es la banda queda transparente: la pieza va SOBRE
//           el programa.
// ============================================================================
import React from "react";
import {AbsoluteFill} from "remotion";
import {santagota as SG} from "../../brand/santagota";
import {Halo, Trazo, Monja, MONJA, Titular, LogoColor, Url, useSantaGota} from "../../brand/santagotaUI";

export const HuinchaTV: React.FC = () => {
  const C = useSantaGota();
  const {width: W, height: H} = SG.formatos.huincha;

  // La monja a escala 0,5: cabeza de ~150 px, arranca en y=40, centrada en x=250.
  const s = 0.5;
  const ty = 40 - MONJA.cabezaTop * s;
  const tx = 250 - MONJA.cabezaCx * s;

  const bloqueMarca = 360; // ancho del bloque botella
  const xTexto = 430;

  return (
    <AbsoluteFill style={{overflow: "hidden"}}>
      {/* La banda */}
      <div style={{position: "absolute", left: 0, top: 0, width: W - bloqueMarca, height: H, background: C.lima}} />
      <div style={{position: "absolute", left: W - bloqueMarca, top: 0, width: bloqueMarca, height: H, background: C.botella}} />

      {/* El personaje, con su aureola */}
      <Monja s={s} tx={tx} ty={ty} />
      <Halo cx={250} cy={22} w={96} h={22} grosor={5} />

      {/* La frase: Light + Black, como el feed */}
      <div style={{position: "absolute", left: xTexto, top: 30}}>
        <Titular size={50} weight={300} track={0} style={{textTransform: "none"}}>Llegó a</Titular>
        <Titular size={64} weight={800} style={{marginTop: 6}}>Revolucionar tu cocina.</Titular>
      </div>
      <Trazo x={xTexto - 4} y={172} w={556} grosor={10} />

      {/* La marca */}
      <LogoColor x={W - bloqueMarca + 80} y={14} w={200} />
      <Url x={W - bloqueMarca + 60} y={152} size={30} align="left" />
    </AbsoluteFill>
  );
};
