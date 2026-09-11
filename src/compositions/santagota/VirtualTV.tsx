// ============================================================================
// SANTA GOTA · KV 02 — VIRTUAL TV · 775×1080 · TARGA + alfa · hasta 20 s
// ----------------------------------------------------------------------------
// IDEA      La monja se mete en el set: asoma por detrás de un bloque lima como
//           por detrás de un mesón (o de la reja del confesionario). La mitad de
//           arriba es transparente: la cabeza y el halo flotan sobre el
//           decorado del programa y eso es lo que genera la curiosidad antes de
//           que se lea nada.
// FASE 2    Desde atrás del bloque levanta la sartén de pasta por encima del
//           borde (la acción de cocina), y la gráfica reacciona: entra la frase.
// LECTURA   Cuatro líneas apiladas, REVOLUCIONAR más grande y con el plumón.
// MARCA     Zócalo botella con logo a color y URL lima.
// ⚠ PLANTILLA del canal PENDIENTE: márgenes de 48 px provisorios.
// ============================================================================
import React from "react";
import {AbsoluteFill} from "remotion";
import {santagota as SG} from "../../brand/santagota";
import {Halo, Trazo, Monja, MONJA, Titular, LogoColor, Url, useSantaGota} from "../../brand/santagotaUI";

export const VirtualTV: React.FC = () => {
  const C = useSantaGota();
  const {width: W, height: H} = SG.formatos.virtual;

  const bloqueTop = 520; // donde empieza el mesón lima — corta a la monja en el pecho, la sartén queda detrás
  const zocaloTop = 900; // zócalo de marca

  // Monja a escala 1: cabeza arranca en y=150, centrada en el ancho.
  const s = 1;
  const ty = 150 - MONJA.cabezaTop * s;
  const tx = W / 2 - MONJA.cabezaCx * s;

  const M = 48;

  return (
    <AbsoluteFill style={{overflow: "hidden"}}>
      {/* La monja va DETRÁS del bloque: asoma por arriba */}
      <Monja s={s} tx={tx} ty={ty} z={1} />
      <Halo cx={W / 2} cy={106} w={150} h={36} grosor={7} />

      {/* El mesón lima */}
      <div style={{position: "absolute", left: 0, top: bloqueTop, width: W, height: H - bloqueTop, background: C.lima, zIndex: 2}} />

      {/* La frase */}
      <div style={{position: "absolute", left: M, top: bloqueTop + 44, zIndex: 3}}>
        <Titular size={60}>El aceite que</Titular>
        <Titular size={60}>llegó a</Titular>
        <Titular size={76} weight={900} style={{marginTop: 4}}>Revolucionar</Titular>
        <Titular size={60} style={{marginTop: 20}}>tu cocina.</Titular>
      </div>
      <Trazo x={M - 2} y={bloqueTop + 44 + 59 + 59 + 4 + 72} w={W - 2 * M - 40} grosor={11} z={3} />

      {/* Zócalo de marca */}
      <div style={{position: "absolute", left: 0, top: zocaloTop, width: W, height: H - zocaloTop, background: C.botella, zIndex: 2}} />
      <LogoColor x={M - 8} y={zocaloTop + 20} w={230} />
      <Url x={M} y={zocaloTop + 74} size={34} align="right" />
    </AbsoluteFill>
  );
};
