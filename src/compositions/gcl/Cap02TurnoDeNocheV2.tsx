// ============================================================================
// G.CL / CAP.02 — «TURNO DE NOCHE» · CORTE 2 · «volvamos a la primera versión»
// 843 frames · 28,1 s · 30 fps · 1080×1920 · 25-09-2026
// ----------------------------------------------------------------------------
// Manda: gcl-agent/universo/06_VIDEO_REELS/CAP_02_TURNO_DE_NOCHE/GUION_V2_PRIMERA_VERSION.md
// Candado 20: los humanos NO hablan; el universo sonoro es de los robots.
// Se edita como editor: sólo lo que cuenta algo. El corte 1 (Cap02TurnoDeNoche)
// queda como registro.
//
//   HOOK        P01 (zoom al post-it) · P02 CLAC y se va
//   OH NO       P04 Marta imprime (mismo CLAC = match cut) · «mm.» · P05 Rolo en crisis
//   G HERO      P06 halo (entra la música) · P07 calma a Rolo
//   TODO FLUYE  COPY · Rolo corre · DISEÑO · Marta ARCHIVA V1 (el plante) · EXPORT
//   DING        P09 «¿Puede ser más WOW?» · corte musical total
//   GAG MARTA   P10 cajón · P11a MÁS WOW · 2019 · G mira · Marta «mm» · G «mm»
//   ESCALADA    P20 torre de papeles · tokens 24→11→3 % · P20 peor
//   VICTORIA    P13 APROBADO ✓ · P14 Rolo cae
//   DING        P15 «Mejor volvamos a la primera versión.» · la música muere
//   REMATE      G mira · P21 Marta saca la carpeta · P11a V1 (rima con MÁS WOW) + sting · G se reenciende
//   DESENLACE   Rolo revive (P14 al revés) · FINAL ✓
//   CIERRE      P17 Pancho, APROBADO_FINAL_V1, sin voz · P22 los tres destruidos · TRRRR · negro
// ============================================================================
import React from "react";
import {AbsoluteFill, Audio, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from "remotion";
import {VOZ, ancho, asegurarFuentes} from "../../brand/copylab/sistema";

const ROSA = "#FF2D8B";
const CORAL = "#FF6B3D";
const v = (n: string) => staticFile(`assets/gcl/cap02-v3/video/${n}.mp4`);
const fx = (n: string) => staticFile(`assets/gcl/cap02-v3/sfx/${n}.mp3`);
const Y = (y: number) => y - 12; // clips a 1080×1944 → cover recorta 12 px arriba

type Plano = {id: string; clip?: string; dur: number; desde?: number; vel?: number; zoom?: {s: number; x: string; y: string}};
const PLANOS: Plano[] = [
  {id: "P01", dur: 30, zoom: {s: 1.45, x: "47%", y: "67%"}},
  {id: "P02", dur: 42, desde: 0.6, vel: 2.6},
  {id: "P04", dur: 24, vel: 0.9},
  {id: "P05", dur: 30},
  {id: "P06", dur: 36, desde: 0.3, vel: 2},
  {id: "P07", dur: 27, vel: 1.6},
  {id: "P08a", dur: 15, desde: 0.5, vel: 1.8},
  {id: "RUN", clip: "P05", dur: 15, desde: 2.6, vel: 2},
  {id: "P08b", dur: 15, desde: 0.5, vel: 1.8},
  {id: "P19", dur: 24, desde: 1.5, vel: 2.5},
  {id: "P08c", dur: 18, desde: 0.5, vel: 1.5},
  {id: "P09", dur: 30, desde: 0.3},
  {id: "P10", dur: 30, desde: 0.3, vel: 1.3},
  {id: "P11a", dur: 30, vel: 0.6},
  {id: "P11b", dur: 27, desde: 0.3, vel: 1.3},
  {id: "MARTA", clip: "P04", dur: 18, desde: 0.05, vel: 0.15},
  {id: "P11c", clip: "P11b-alt", dur: 21, desde: 3.0},
  {id: "P20", dur: 36, vel: 1.4},
  {id: "P12", dur: 24, desde: 0.5, vel: 1.6},
  {id: "P20b", clip: "P20", dur: 18, desde: 2.0, vel: 1.6},
  {id: "P13", dur: 33, desde: 1.0, vel: 1.2},
  {id: "P14", dur: 24, desde: 1.8, vel: 2.4},
  {id: "P15", clip: "P09", dur: 36, desde: 2.0},
  {id: "MIRA", clip: "P16", dur: 18, vel: 0.6},
  {id: "P21", dur: 30, desde: 0.8, vel: 1.3},
  {id: "V1", clip: "P11a", dur: 30, vel: 0.6},
  {id: "REENCIENDE", clip: "P06", dur: 24, desde: 0.8, vel: 1.5},
  {id: "REVIVE", clip: "P14-revive", dur: 21, desde: 0.8, vel: 3},
  {id: "FINAL", clip: "P19", dur: 18, desde: 3.2, vel: 1.5},
  {id: "P17", dur: 39, desde: 0.5, vel: 1.3},
  {id: "P22", dur: 36, desde: 0.5},
  {id: "FIRMA", dur: 24},
];
const INICIO: Record<string, number> = {};
{let t = 0; for (const p of PLANOS) {INICIO[p.id] = t; t += p.dur;}}
export const TURNO_V2_FRAMES = PLANOS.reduce((a, p) => a + p.dur, 0); // 843
const en = (id: string, extra = 0) => INICIO[id] + extra;

// ── TEXTO DIEGÉTICO (pegado a la superficie, se escala con el zoom) ─────────

/** Post-it de P01, medido: t=0 → (391,1160)–(629,1435) · t=1,5 s → (384,1170)–(630,1454). */
const PostItUrgente: React.FC<{f: number}> = ({f}) => {
  const k = interpolate(f, [0, 45], [0, 1], {extrapolateRight: "clamp"});
  const x0 = 391 - 7 * k, x1 = 629 + k, y0 = Y(1160 + 10 * k), y1 = Y(1435 + 19 * k);
  const w = x1 - x0;
  return (
    <div style={{position: "absolute", left: x0, top: y0, width: w, height: y1 - y0, mixBlendMode: "multiply", color: "#1d1a33",
      fontFamily: VOZ.mano, textAlign: "center", transform: "rotate(-2deg)", filter: "blur(0.4px)",
      display: "flex", flexDirection: "column", justifyContent: "center", lineHeight: 0.95}}>
      <div style={{fontSize: w * 0.23, fontWeight: 700, color: "#b3122e", textDecoration: "underline", textDecorationThickness: 4}}>URGENTE</div>
      <div style={{fontSize: w * 0.14, fontWeight: 600, marginTop: w * 0.05}}>ajustar campaña</div>
      <div style={{fontSize: w * 0.15, fontWeight: 700, marginTop: w * 0.04}}>MAÑANA 09:00</div>
    </div>
  );
};

const HojaMarta: React.FC = () => (
  <div style={{position: "absolute", left: 400, top: Y(815), width: 260, textAlign: "center", mixBlendMode: "multiply",
    fontFamily: VOZ.data, color: "#2a2a2a", fontSize: 30, letterSpacing: 3, lineHeight: 1.15, transform: "rotate(-3deg)", filter: "blur(0.5px)"}}>
    URGENTE<br />09:00
  </div>
);

/** Rótulo blanco de la carpeta de P11a: (285,1190)–(445,1265). Sirve para MÁS WOW y para V1. */
const Rotulo: React.FC<{l1: string; l2?: string}> = ({l1, l2}) => (
  <div style={{position: "absolute", left: 285, top: Y(1188), width: 162, height: 80, mixBlendMode: "multiply",
    display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", transform: "rotate(-7deg)",
    fontFamily: VOZ.mano, color: "#1d1a33", lineHeight: 0.9, filter: "blur(0.4px)"}}>
    <div style={{fontSize: l2 ? 38 : 64, fontWeight: 700}}>{l1}</div>
    {l2 && <div style={{fontSize: 26, fontWeight: 600}}>{l2}</div>}
  </div>
);

// ── TEXTO EN PANTALLA (no se escala) ────────────────────────────────────────
const Cabecera: React.FC<{hora?: string}> = ({hora}) => (
  <div style={{position: "absolute", left: 64, top: 150, fontFamily: VOZ.data, letterSpacing: 4}}>
    <div style={{fontSize: 22, color: "rgba(242,244,246,0.7)"}}>TEMPORADA 1 · CAPÍTULO 02</div>
    {hora && <div style={{fontSize: 30, color: ROSA, marginTop: 10}}>{hora}</div>}
  </div>
);

const Notif: React.FC<{quien: string; hora: string; msj: string}> = ({quien, hora, msj}) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [0, 5], [0, 1], {extrapolateRight: "clamp"});
  return (
    <div style={{position: "absolute", left: 190, top: 960 - (1 - p) * 60, width: 760, opacity: p, padding: "28px 32px",
      borderRadius: 34, background: "rgba(22,22,26,0.9)", boxShadow: "0 18px 50px rgba(0,0,0,0.6)", fontFamily: VOZ.funcional, color: "#F2F4F6"}}>
      <div style={{display: "flex", alignItems: "center", gap: 14, fontSize: 24, color: "rgba(242,244,246,0.6)"}}>
        <div style={{width: 34, height: 34, borderRadius: 9, background: "#25D366"}} />
        <span>WhatsApp</span><span style={{marginLeft: "auto"}}>{hora}</span>
      </div>
      <div style={{fontSize: 36, fontWeight: 700, marginTop: 12}}>{quien}</div>
      <div style={{fontSize: 42, marginTop: 4, lineHeight: 1.2}}>{msj}</div>
    </div>
  );
};

const Golpe: React.FC<{texto: string}> = ({texto}) => (
  <div style={{position: "absolute", left: 0, right: 0, top: 1300, textAlign: "center", fontFamily: VOZ.narrow, fontWeight: 800,
    fontSize: 132, letterSpacing: 2, color: "#F2F4F6", textShadow: "0 4px 30px rgba(0,0,0,0.7)"}}>
    {texto} <span style={{color: ROSA}}>✓</span>
  </div>
);

/** Sello grande (APROBADO / FINAL): entra golpeando, un poco torcido. */
const Sello: React.FC<{texto: string; color?: string}> = ({texto, color = ROSA}) => {
  const f = useCurrentFrame();
  const s = interpolate(f, [0, 4], [1.6, 1], {extrapolateRight: "clamp"});
  const op = interpolate(f, [0, 2], [0, 1], {extrapolateRight: "clamp"});
  return (
    <div style={{position: "absolute", left: 0, right: 0, top: 1180, display: "flex", justifyContent: "center", opacity: op}}>
      <div style={{transform: `rotate(-6deg) scale(${s})`, border: `10px solid ${color}`, borderRadius: 18, padding: "10px 42px",
        fontFamily: VOZ.narrow, fontWeight: 800, fontSize: 150, letterSpacing: 6, color, textShadow: "0 0 30px rgba(0,0,0,0.5)"}}>
        {texto} ✓
      </div>
    </div>
  );
};

/** Dato del universo, como los rótulos del CAP.01 («ARCHIVO · 2023–2026»). */
const Dato: React.FC<{texto: string; top?: number; left?: number; color?: string}> = ({texto, top = 1330, left = 64, color = ROSA}) => (
  <div style={{position: "absolute", left, top, fontFamily: VOZ.data, fontSize: 30, letterSpacing: 4, color,
    textShadow: "0 2px 14px rgba(0,0,0,0.9)"}}>{texto}</div>
);

const Tokens: React.FC = () => {
  const f = useCurrentFrame();
  const valor = f < 8 ? 24 : f < 16 ? 11 : 3;
  return <Dato texto={`TOKENS ${valor} %`} top={250} color={valor > 10 ? ROSA : CORAL} />;
};

// ── UN PLANO ────────────────────────────────────────────────────────────────
const Sobre: React.FC<{id: string}> = ({id}) => {
  const f = useCurrentFrame();
  if (id === "P01") return <PostItUrgente f={f} />;
  if (id === "P04") return <HojaMarta />;
  if (id === "P11a") return <Rotulo l1="MÁS WOW" l2="2019" />;
  if (id === "V1") return <Rotulo l1="V1" />;
  return null;
};

const Encima: React.FC<{id: string}> = ({id}) => {
  switch (id) {
    case "P01": case "P02": return <Cabecera hora="18:59" />;
    case "P06": case "P07": case "RUN": return <Cabecera hora="00:58" />;
    case "P08a": return <><Cabecera hora="00:58" /><Golpe texto="COPY" /></>;
    case "P08b": return <><Cabecera hora="00:58" /><Golpe texto="DISEÑO" /></>;
    case "P19": return <><Cabecera hora="01:12" /><Dato texto="ARCHIVADO · V1" top={1500} /></>;
    case "P08c": return <><Cabecera hora="01:40" /><Golpe texto="EXPORT" /></>;
    case "P09": return <><Cabecera /><Notif quien="Gin" hora="02:31" msj="¿Puede ser más WOW? 🙏" /></>;
    case "P12": return <><Cabecera hora="05:40" /><Tokens /></>;
    case "P20": case "P20b": return <Cabecera hora="04:15" />;
    case "P13": return <><Cabecera hora="06:40" /><Sello texto="APROBADO" /></>;
    case "P15": return <><Cabecera /><Notif quien="Cliente" hora="06:58" msj="Mejor volvamos a la primera versión." /></>;
    case "FINAL": return <Sello texto="FINAL" />;
    case "P17": return <><Cabecera hora="09:00" /><Dato texto="APROBADO_FINAL_V1.pdf ✓" top={1520} left={80} /></>;
    case "FIRMA": return null;
    default: return <Cabecera />;
  }
};

const Clip: React.FC<{p: Plano}> = ({p}) => {
  const z = p.zoom;
  return (
    <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
      <div style={{position: "absolute", inset: 0, transform: z ? `scale(${z.s})` : undefined, transformOrigin: z ? `${z.x} ${z.y}` : undefined}}>
        <OffthreadVideo src={v(p.clip ?? p.id)} startFrom={Math.round((p.desde ?? 0) * 30)} playbackRate={p.vel ?? 1} muted
          style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover"}} />
        <Sobre id={p.id} />
      </div>
    </AbsoluteFill>
  );
};

const Firma: React.FC = () => {
  const f = useCurrentFrame();
  const op = interpolate(f, [4, 10], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{backgroundColor: "#080F14", justifyContent: "center", alignItems: "center"}}>
      <div style={{opacity: op, fontFamily: VOZ.impacto, fontVariationSettings: ancho(90, 900), fontSize: 96, color: "#F2F4F6", letterSpacing: 2}}>
        G.CL <span style={{color: ROSA}}>×</span> COPYLAB
      </div>
    </AbsoluteFill>
  );
};

// ── SONIDO: los humanos no hablan; los robots sí suenan ─────────────────────
type Pista = {src: string; desde: number; vol?: number; hasta?: number};
const SONIDO: Pista[] = [
  {src: fx("oficina-noche"), desde: 0, hasta: en("P04"), vol: 0.45},
  {src: fx("laptop-clac"), desde: en("P02", 7)},
  {src: fx("laptop-clac"), desde: en("P04"), vol: 0.9},          // el mismo CLAC abajo (match cut)
  {src: fx("marta-trrr"), desde: en("P04"), vol: 0.8, hasta: en("P05", 6)},
  {src: fx("marta-mm"), desde: en("P04", 12)},
  {src: fx("rolo-bips"), desde: en("P05"), vol: 0.85, hasta: en("P06", 6)},
  {src: fx("rolo-servos"), desde: en("P05"), vol: 0.7, hasta: en("P06")},
  {src: fx("g-halo-hum"), desde: en("P06", 8), vol: 0.8},
  {src: fx("rolo-bips-calma"), desde: en("P07"), vol: 0.7},
  {src: fx("g-panel-tick"), desde: en("P08a"), vol: 0.9},
  {src: fx("rolo-servos"), desde: en("RUN"), vol: 0.5, hasta: en("P08b")},
  {src: fx("g-panel-tick"), desde: en("P08b"), vol: 0.9},
  {src: fx("papel"), desde: en("P19", 2), vol: 0.6},
  {src: fx("timbre-seco"), desde: en("P19", 12)},
  {src: fx("g-panel-tick"), desde: en("P08c"), vol: 0.9},
  // más WOW
  {src: fx("ding"), desde: en("P09")},
  {src: fx("g-eh"), desde: en("P09", 12), vol: 0.9},
  {src: fx("cajon-metal"), desde: en("P10", 4)},
  {src: fx("papel"), desde: en("P11a", 3), vol: 0.5},
  {src: fx("marta-mm"), desde: en("MARTA", 2)},
  {src: fx("g-mm"), desde: en("P11c", 5), vol: 0.9},
  // escalada
  {src: fx("papeles-caen"), desde: en("P20", 6), vol: 0.8},
  {src: fx("rolo-bips"), desde: en("P20"), vol: 0.5, hasta: en("P12")},
  {src: fx("g-glitch"), desde: en("P12", 16), vol: 0.35},
  {src: fx("papeles-caen"), desde: en("P20b"), vol: 0.7},
  // victoria
  {src: fx("timbre-seco"), desde: en("P13")},
  {src: fx("rolo-clonc"), desde: en("P14", 4), vol: 0.9},
  // el giro
  {src: fx("ding"), desde: en("P15")},
  // remate
  {src: fx("cajon-metal"), desde: en("P21", 2), vol: 0.6},
  {src: fx("sting-triunfal"), desde: en("V1")},
  {src: fx("g-halo-hum"), desde: en("REENCIENDE"), vol: 0.7},
  {src: fx("g-risa"), desde: en("REENCIENDE", 6)},
  {src: fx("rolo-revive"), desde: en("REVIVE", 2)},
  {src: fx("timbre-seco"), desde: en("FINAL", 2)},
  // mañana
  {src: fx("oficina-manana"), desde: en("P17"), hasta: en("P22"), vol: 0.5},
  {src: fx("cafe-laptop"), desde: en("P17", 3), vol: 0.7},
  {src: fx("marta-trrr-largo"), desde: en("P22", 4), vol: 0.4, hasta: en("FIRMA", 10)},
];

// Música (cuando exista): arranca con el halo, MÁS WOW la corta, vuelve más
// intensa en el caos, APROBADO la resuelve en falso y el segundo DING la mata.
const TRAMOS_MUSICA = [
  {desde: en("P06", 6), hasta: en("P09"), desdeS: 0},
  {desde: en("P11c", 14), hasta: en("P15"), desdeS: 22},
];

export const Cap02TurnoDeNocheV2: React.FC<{musica?: string}> = ({musica}) => {
  asegurarFuentes();
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      {PLANOS.map((p) => (
        <Sequence key={p.id} from={INICIO[p.id]} durationInFrames={p.dur}>
          {p.id === "FIRMA" ? <Firma /> : <><Clip p={p} /><Encima id={p.id} /></>}
        </Sequence>
      ))}
      {SONIDO.map((s, i) => (
        <Sequence key={i} from={s.desde} durationInFrames={s.hasta ? s.hasta - s.desde : undefined}>
          <Audio src={s.src} volume={s.vol ?? 1} />
        </Sequence>
      ))}
      {musica && TRAMOS_MUSICA.map((m, i) => (
        <Sequence key={`m${i}`} from={m.desde} durationInFrames={m.hasta - m.desde}>
          <Audio src={staticFile(musica)} startFrom={Math.round(m.desdeS * 30)} volume={0.55} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
