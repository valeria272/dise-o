// ============================================================================
// SANTA GOTA · VIRTUAL TV · 775×1080 · 29,97 · 450 f = 15,0 s · alfa real
// ----------------------------------------------------------------------------
// V3 — «Una monja acaba de entrar al matinal». Sin pantallitas ni cajas de video:
// la monja recortada con alfa real, GRANDE, y tipografía con franjas alrededor.
//   0,0–0,6   APARICIÓN  sube desde el borde inferior con overshoot, se detiene seca
//   0,6–4,0   PERSONAJE  mira a cámara con la sartén (micro-vida), aureola, empuje lento
//   4,0–4,6   ACCIÓN     lanza la pasta (cuadros reales del reel a 0,5×) y congela arriba
//   5,0–10,0  CLAIM      ella se hunde para dejar espacio y arriba se apilan las franjas:
//                        EL ACEITE · QUE LLEGÓ A · REVOLUCIONAR (golpe, lima) · TU COCINA.
//   10,0–14,4 MARCA      las franjas salen; losa con el logo oficial + SANTAGOTA.CL
//   14,4–15,0 SALIDA     ella vuelve a meterse en la tele; la losa se barre
// ⚠ PLANTILLA DEL CANAL PENDIENTE: márgenes provisorios de 48 px.
// ============================================================================
import React from "react";
import {AbsoluteFill, Sequence} from "remotion";
import {MONJA} from "../../../brand/santagotaUI";
import {Bloque, Cta, HaloAnim, Linea, Logo, MonjaViva, Plumon, Revela, SFX, Sfx, cae, cuadroMonja, entra, fade, golpe, seg, useFrameFps} from "./comun";

export const DUR_VIRTUAL = seg(15);

const W = 775, H = 1080, M = 48;

/** Una línea del claim sobre su franja petróleo, con reveal propio. */
const Franja: React.FC<{x: number; y: number; p: number; q: number; size: number; lima?: boolean; weight?: number; golpeT?: boolean; children: React.ReactNode}> = ({
  x, y, p, q, size, lima, weight = 800, golpeT = false, children,
}) => {
  const padY = Math.round(size * 0.16), padX = Math.round(size * 0.3);
  return (
    <div style={{position: "absolute", left: x, top: y, zIndex: 4, clipPath: `inset(0 ${(1 - Math.min(1, p)) * 100}% 0 ${Math.min(1, q) * 100}%)`}}>
      <div style={{background: "#0A2A34", padding: `${padY}px ${padX}px`, clipPath: "polygon(8px 0, 100% 0, calc(100% - 8px) 100%, 0 100%)", boxShadow: "0 8px 24px rgba(0,0,0,0.35)"}}>
        <Revela p={p} modo={golpeT ? "golpe" : "abajo"} origen="0% 70%">
          <Linea size={size} weight={weight} lima={lima} sombra={false} style={golpeT ? {letterSpacing: "-0.03em"} : undefined}>{children}</Linea>
        </Revela>
      </div>
    </div>
  );
};

export const VirtualTV: React.FC = () => {
  const {frame, fps} = useFrameFps();

  // — la monja —
  const s = 0.95;
  const tx = W / 2 - MONJA.cabezaCx * s;
  const tyArriba = 150 - MONJA.cabezaTop * s;        // cornette en y=150 (aparición y acción)
  const sube = golpe(frame, fps, 0, 20);
  const hundeClaim = fade(frame, seg(5.0), seg(5.7)) ; // baja para dejar el espacio del claim
  const ease = hundeClaim * hundeClaim * (3 - 2 * hundeClaim);
  const salida = cae(frame, DUR_VIRTUAL - 18, DUR_VIRTUAL - 1) * 760;
  const ty = tyArriba + (1 - sube) * 950 + ease * 300 + salida;
  const empuje = 1 + 0.035 * fade(frame, seg(1.0), seg(4.0));
  const cuadro = cuadroMonja(frame - 20, seg(4.0) - 20, 0.5, 8, 9);
  const halo = fade(frame, seg(1.3), seg(1.7)) * (1 - ease);

  // — claim (franjas) —
  const t0 = seg(5.05);
  const pF = [0, 8, 16, 28].map((d, i) => (i === 2 ? golpe(frame, fps, t0 + d, 16) : entra(frame, fps, t0 + d, 14)));
  const qF = [0, 4, 8, 12].map((d) => fade(frame, seg(10.0) + d, seg(10.0) + d + 9));
  const plumon = fade(frame, seg(6.3), seg(6.8));
  const plumonOp = 1 - qF[2];

  // — marca —
  const losaIn = golpe(frame, fps, seg(10.35), 14);
  const losaOut = cae(frame, DUR_VIRTUAL - 16, DUR_VIRTUAL - 4);
  const l1 = golpe(frame, fps, seg(10.55), 18);
  const l2 = golpe(frame, fps, seg(10.8), 18);
  const marcaOp = fade(frame, DUR_VIRTUAL - 16, DUR_VIRTUAL - 9, 1, 0);

  return (
    <AbsoluteFill style={{overflow: "hidden"}}>
      {/* La monja (alfa real) */}
      <div style={{position: "absolute", left: 0, top: 0, width: W, height: H, overflow: "hidden", zIndex: 2,
        transform: `scale(${empuje})`, transformOrigin: `${W / 2}px 760px`}}>
        <MonjaViva cuadro={cuadro} s={s} tx={tx} ty={ty} z={2} />
      </div>
      <HaloAnim cx={W / 2 + 6} cy={118 + (1 - sube) * 950} w={190} h={40} p={halo} grosor={8} z={5} />

      {/* El claim: franjas apiladas, arriba */}
      <Franja x={M} y={54} p={pF[0]} q={qF[0]} size={66}>El aceite</Franja>
      <Franja x={M + 30} y={146} p={pF[1]} q={qF[1]} size={66}>que llegó a</Franja>
      <Franja x={M} y={238} p={pF[2]} q={qF[2]} size={76} weight={900} lima golpeT>Revolucionar</Franja>
      <Franja x={M + 60} y={350} p={pF[3]} q={qF[3]} size={66}>tu cocina.</Franja>
      <div style={{opacity: plumonOp}}>
        <Plumon x={M + 18} y={332} w={600} grosor={10} p={plumon} z={6} />
      </div>

      {/* La marca: losa petróleo con el logo oficial + SANTAGOTA.CL */}
      <Bloque x={M} y={64} w={W - 2 * M} h={310} p={losaIn} q={losaOut} z={3}>
        <div style={{opacity: marcaOp}}>
          <Logo x={(W - 2 * M - 470) / 2} y={6} w={470} op={Math.min(1, l1 * 2)} sc={0.7 + 0.3 * l1} sombra={false} />
        </div>
      </Bloque>
      <div style={{opacity: marcaOp * Math.min(1, l2 * 2)}}>
        <Cta x={(W - 440) / 2} y={352} size={46} sc={0.7 + 0.3 * l2} z={7} />
      </div>

      {/* Sonido (solo preview; el virtual se entrega mudo) */}
      <Sequence from={0} layout="none">
        <Sfx src={SFX.whoosh2} at={0} vol={0.9} />
        <Sfx src={SFX.pan} at={4.0} vol={0.9} />
        <Sfx src={SFX.whoosh} at={5.0} vol={0.7} />
        <Sfx src={SFX.impact} at={5.6} vol={0.9} />
        <Sfx src={SFX.marker} at={6.3} vol={0.7} />
        <Sfx src={SFX.whoosh2} at={10.0} vol={0.6} />
        <Sfx src={SFX.sting} at={10.5} vol={0.9} />
        <Sfx src={SFX.whoosh2} at={14.4} vol={0.6} />
      </Sequence>
    </AbsoluteFill>
  );
};
