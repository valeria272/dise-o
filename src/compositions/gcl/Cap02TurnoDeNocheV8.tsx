// ============================================================================
// G.CL / CAP.02 — «TURNO DE NOCHE» · CORTE 8 · «volvamos a la primera versión»
// 30 fps · 1080×1920 · 25-09-2026 · ~28,5 s de historia + cierre de serie
// ----------------------------------------------------------------------------
// Pasada final de storytelling (Valeria, 25-09 noche): «editar con más crueldad».
// Cada plano responde «¿la situación acaba de cambiar?». Si no, sobra.
//   0–3    HOOK          URGENTE · MAÑANA 09:00 → Pancho (de espaldas) cierra y se va. Sin música, sólo CLAC
//   3–6    PROBLEMA BAJA tubo → Marta recibe, «mm» → Rolo en crisis
//   6–8    G HERO        halo → calma a Rolo → le entran los códigos: ENTRA LA CANCIÓN
//   8–11   SATISFACTION  COPY ✓ → puños → DISEÑO ✓ → Marta ARCHIVA V1 (el plante) → LISTO ✓
//   11–16  PRIMER GIRO   DING. Mute brutal. «¿Puede ser más WOW?» G se congela. Marta abre el cajón:
//                        MÁS WOW · 2019. G mira la carpeta. Mira a Marta. Marta ni lo mira.
//   16–20  ESCALADA      la canción vuelve más rápida: Rolo cada vez peor, torre, pelea, tokens 24→11→3, glitch
//   20–22  FALSA VICTORIA APROBADO ✓ · golpe final · silencio · Rolo se desploma
//   22–24  PICO          DING. «Mejor volvamos a la primera versión.» Música muerta. G ✕✕
//   24–27  RESOLUCIÓN    Marta abre el archivo y saca la V1. Sting deadpan. G se reenciende
//   27–30  EPÍLOGO       09:00, Pancho abre el laptop: FINAL_APROBADO_V1 ✓, sonríe. Corte abajo:
//                        Rolo destruido, G al 1 %, Marta imprime. TRRRR. Negro. Cierre de serie.
// ============================================================================
import React from "react";
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from "remotion";
import {VOZ, asegurarFuentes} from "../../brand/copylab/sistema";
import {Superficie, Track, frameClip} from "./superficie";
import {SuperficieCurva, Perfil} from "./superficie-curva";
import {CierreSerie, cierreFrames} from "./CierreSerie";
import trackP04 from "./track/P04.json";
import trackP11a from "./track/P11a.json";
import POSTITS from "./track/postits.json";

const ROSA = "#FF2D8B";
const CORAL = "#FF6B3D";
const v = (n: string) => staticFile(`assets/gcl/cap02-v3/video/${n}.mp4`);
const fx = (n: string) => staticFile(`assets/gcl/cap02-v3/sfx/${n}.mp3`);
const clamp = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;

const TAGLINE = "COPYLAB\nDepartamento de cosas imposibles.";
const PROXIMO = "Batalla campal: G vs humanos"; // ← por definir con Valeria
const CIERRE_TW0 = 84;
const CIERRE = cierreFrames(PROXIMO, CIERRE_TW0);

type Plano = {
  id: string; clip?: string; dur: number; desde?: number; vel?: number;
  zoom?: {s: number; x: string; y: string; s1?: number}; sacudir?: number;
  still?: boolean; grano?: boolean; negro?: boolean;
};
const PLANOS: Plano[] = [
  // HOOK — 18:30
  {id: "P01", dur: 21, zoom: {s: 1.0, x: "50%", y: "50%", s1: 1.06}},
  {id: "P02b", dur: 54, desde: 1.2, vel: 1.2, grano: true},
  // PROBLEMA BAJA — 18:33
  {id: "N02", dur: 15, desde: 0.3, vel: 2.4},
  {id: "N03", dur: 18, desde: 0.4, vel: 2},
  {id: "P04", dur: 30, desde: 1.8, zoom: {s: 1.55, x: "535px", y: "640px"}},
  {id: "P05", dur: 21, vel: 1.2},
  // G HERO — 18:36
  {id: "P06", dur: 24, desde: 0.3, vel: 2},
  {id: "P07", dur: 15, vel: 1.8},
  {id: "N07", dur: 21, desde: 0.5, vel: 1.6},
  // SATISFACTION MONTAGE — tres impactos y fuera
  {id: "T1", clip: "N08", dur: 15, desde: 0.1, vel: 2, sacudir: 3},
  {id: "COPY", clip: "P08a", dur: 12, desde: 0.5, vel: 2},
  {id: "PUNOS", clip: "N20", dur: 15, desde: 0.3, vel: 1.8},
  {id: "DISENO", clip: "P08b", dur: 12, desde: 0.5, vel: 2},
  {id: "P19", dur: 18, desde: 1.5, vel: 2.5},
  {id: "LISTO", clip: "P08c", dur: 18, desde: 0.5, vel: 1.6},
  // PRIMER GIRO — DING · silencio · MÁS WOW · 2019
  {id: "P09", dur: 39, desde: 0.3},
  {id: "P10", dur: 24, desde: 0.3, vel: 1.4},
  {id: "P11a", dur: 30, vel: 0.7},
  {id: "P11b", dur: 21, desde: 0.3, vel: 1.4},
  {id: "P11c", clip: "P11b-alt", dur: 18, desde: 3.0},
  {id: "MARTA", clip: "P04", dur: 15, desde: 0.05, vel: 0.15},
  // ESCALADA — impecable → caos → destruidos
  {id: "E1", clip: "N09", dur: 12, desde: 0.5, vel: 2.2},
  {id: "E2", clip: "P20", dur: 14, desde: 0.5, vel: 2.2},
  {id: "E3", clip: "N24", dur: 18, desde: 2.2, vel: 1.5},
  {id: "E4", clip: "P12", dur: 24, desde: 0.5, vel: 1.8},
  {id: "E5", clip: "N09", dur: 10, desde: 2.5, vel: 2.4},
  {id: "E6", clip: "P20", dur: 12, desde: 2.5, vel: 2.2},
  {id: "E7", clip: "N19", dur: 12, desde: 0.3, vel: 2},
  {id: "E8", clip: "N08", dur: 10, desde: 0.7, vel: 2.4, sacudir: 4},
  // FALSA VICTORIA
  {id: "P13", dur: 36, desde: 1.0, vel: 1.2},
  {id: "P14", dur: 24, desde: 1.8, vel: 2.4},
  // PICO
  {id: "P15", clip: "P09", dur: 42, desde: 2.0},
  {id: "MIRA", clip: "P16", dur: 24, vel: 0.8},
  // RESOLUCIÓN — Marta cierra su arco
  {id: "P21", dur: 30, desde: 0.8, vel: 1.3},
  {id: "V1", clip: "P11a", dur: 27, vel: 0.7},
  {id: "REENCIENDE", clip: "P06", dur: 18, desde: 0.8, vel: 1.5},
  // EPÍLOGO — 09:00, visual, sin voz
  {id: "P17", dur: 36, desde: 0.5, vel: 1.3, grano: true},
  {id: "P22", dur: 36, desde: 0.5},
  {id: "NEGRO", dur: 12, negro: true},
  {id: "CIERRE", dur: CIERRE},
];
const INICIO: Record<string, number> = {};
{let t = 0; for (const p of PLANOS) {INICIO[p.id] = t; t += p.dur;}}
export const TURNO_V8_FRAMES = PLANOS.reduce((a, p) => a + p.dur, 0);
const en = (id: string, extra = 0) => INICIO[id] + extra;
const P = (id: string) => PLANOS.find((p) => p.id === id)!;

// ── TEXTO DIEGÉTICO ─────────────────────────────────────────────────────────

/** El pedido, en plumón: grande y en tres líneas, se lee en medio segundo. */
const TextoCliente: React.FC<{w: number}> = ({w}) => (
  <>
    <div style={{fontSize: w * 0.24, fontWeight: 700, color: "#b3122e", textDecoration: "underline", textDecorationThickness: 4}}>URGENTE</div>
    <div style={{fontSize: w * 0.15, fontWeight: 600, marginTop: w * 0.05}}>ajustar campaña</div>
    <div style={{fontSize: w * 0.17, fontWeight: 700, marginTop: w * 0.02}}>MAÑANA 09:00</div>
  </>
);

type DatosPostIt = {quad: [number, number][]; perfil: Perfil};
const postit = (id: string) => (POSTITS as unknown as Record<string, DatosPostIt | undefined>)[id];

/** El post-it pegado en el monitor, que se CURVA al despegarse: el texto va en tiras sobre el
 *  perfil medido (P01 y N01 son el mismo encuadre; el perfil de P01 no tiene la mano encima). */
const PostIt: React.FC = () => {
  const d = postit("P01");
  if (!d) return null;
  const yTop = d.perfil[0][0], yBot = d.perfil[d.perfil.length - 1][0];
  const W = 560, H = 520;
  return (
    <>
      <SuperficieCurva perfil={d.perfil} y0={yTop + 20} y1={yTop + (yBot - yTop) * 0.72} w={W} h={H} offsetY={-12} tiras={10}
        style={{mixBlendMode: "multiply"}}>
        <div style={{width: W, height: H, display: "flex", flexDirection: "column", justifyContent: "center", fontFamily: VOZ.mano,
          textAlign: "center", color: "#1d1a33", lineHeight: 0.95, filter: "blur(0.5px)"}}>
          <TextoCliente w={W} />
        </div>
      </SuperficieCurva>
    </>
  );
};


/** P04: Marta imprime EL pedido que bajó por el tubo. Sale de la ranura hacia arriba. */
const TIRA_QUAD: [number, number][] = [[478, 470], [594, 470], [594, 832], [478, 832]];
const TiraMarta: React.FC<{f: number}> = ({f}) => {
  const p = P("P04");
  const k = frameClip(trackP04 as Track, f, p.desde ?? 0, p.vel ?? 1);
  const sale = interpolate(f, [0, 26], [1, 0], clamp);
  const lineas = ["URGENTE", "ajustar", "campaña", "MAÑANA", "09:00"];
  return (
    <Superficie track={trackP04 as Track} k={k} quad={TIRA_QUAD} w={116} h={362} offsetY={-12}
      style={{overflow: "hidden", mixBlendMode: "multiply"}}>
      <div style={{transform: `translateY(${sale * 362}px)`, textAlign: "center", fontFamily: VOZ.data, fontWeight: 600,
        fontSize: 19, lineHeight: "40px", color: "#2a2730", letterSpacing: 1, filter: "blur(0.3px)", paddingTop: 14}}>
        {lineas.map((l, i) => <div key={i} style={{fontWeight: i === 0 ? 800 : 600, fontSize: i === 0 ? 23 : 19}}>{l}</div>)}
      </div>
    </Superficie>
  );
};


/** Rótulo trackeado sobre la carpeta de P11a: sirve para MÁS WOW · 2019 y para V1. */
const ROTULO_QUAD: [number, number][] = [[352, 1218], [482, 1228], [500, 1296], [362, 1292]];
const Rotulo: React.FC<{id: string; l1: string; l2?: string}> = ({id, l1, l2}) => {
  const f = useCurrentFrame();
  const p = P(id);
  const k = frameClip(trackP11a as Track, f, p.desde ?? 0, p.vel ?? 1);
  return (
    <Superficie track={trackP11a as Track} k={k} quad={ROTULO_QUAD} w={160} h={80} offsetY={-12} style={{mixBlendMode: "multiply"}}>
      <div style={{width: 160, height: 80, display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center",
        fontFamily: VOZ.mano, color: "#1d1a33", lineHeight: 0.85, filter: "blur(0.4px)"}}>
        <div style={{fontSize: l2 ? 44 : 66, fontWeight: 700}}>{l1}</div>
        {l2 && <div style={{fontSize: 26, fontWeight: 600}}>{l2}</div>}
      </div>
    </Superficie>
  );
};

// ── TEXTO EN PANTALLA ───────────────────────────────────────────────────────
const Cabecera: React.FC<{hora?: string; color?: string}> = ({hora, color = ROSA}) => (
  <div style={{position: "absolute", left: 64, top: 150, fontFamily: VOZ.data, letterSpacing: 4}}>
    <div style={{fontSize: 22, color: "rgba(242,244,246,0.7)"}}>TEMPORADA 1 · CAPÍTULO 02</div>
    {hora && <div style={{fontSize: 30, color, marginTop: 10}}>{hora}</div>}
  </div>
);

const Golpe: React.FC<{texto: string}> = ({texto}) => (
  <div style={{position: "absolute", left: 0, right: 0, top: 1300, textAlign: "center", fontFamily: VOZ.narrow, fontWeight: 800,
    fontSize: 132, letterSpacing: 2, color: "#F2F4F6", textShadow: "0 4px 30px rgba(0,0,0,0.7)"}}>
    {texto} <span style={{color: ROSA}}>✓</span>
  </div>
);

const Dato: React.FC<{texto: string; top?: number; left?: number; color?: string; size?: number}> = ({texto, top = 1330, left = 64, color = ROSA, size = 30}) => (
  <div style={{position: "absolute", left, top, fontFamily: VOZ.data, fontSize: size, letterSpacing: 4, color,
    textShadow: "0 2px 14px rgba(0,0,0,0.9)"}}>{texto}</div>
);



const Tokens: React.FC = () => {
  const f = useCurrentFrame();
  const valor = f < 8 ? 24 : f < 16 ? 11 : 3;
  return <Dato texto={`TOKENS ${valor} %`} top={250} color={valor > 10 ? ROSA : CORAL} />;
};

/** La notificación: una tarjeta, seca. El DING hace el trabajo. */
const Notif: React.FC<{quien: string; hora: string; msj: string}> = ({quien, hora, msj}) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [0, 5], [0, 1], clamp);
  return (
    <div style={{position: "absolute", left: 160, width: 760, top: 960 - (1 - p) * 60, opacity: p, padding: "28px 32px",
      borderRadius: 34, background: "rgba(22,22,26,0.92)", boxShadow: "0 18px 50px rgba(0,0,0,0.6)", fontFamily: VOZ.funcional, color: "#F2F4F6"}}>
      <div style={{display: "flex", alignItems: "center", gap: 14, fontSize: 24, color: "rgba(242,244,246,0.6)"}}>
        <div style={{width: 34, height: 34, borderRadius: 9, background: "#25D366"}} />
        <span>WhatsApp</span><span style={{marginLeft: "auto"}}>{hora}</span>
      </div>
      <div style={{fontSize: 36, fontWeight: 700, marginTop: 12}}>{quien}</div>
      <div style={{fontSize: 44, marginTop: 4, lineHeight: 1.2}}>{msj}</div>
    </div>
  );
};

/** Sello grande (APROBADO): entra golpeando, un poco torcido, y se queda. */
const Sello: React.FC<{texto: string}> = ({texto}) => {
  const f = useCurrentFrame();
  const s = interpolate(f, [0, 5], [1.7, 1], clamp);
  const op = interpolate(f, [0, 2], [0, 1], clamp);
  return (
    <div style={{position: "absolute", left: 0, right: 0, top: 1150, display: "flex", justifyContent: "center", opacity: op}}>
      <div style={{transform: `rotate(-6deg) scale(${s})`, border: `12px solid ${ROSA}`, borderRadius: 22, padding: "14px 48px",
        fontFamily: VOZ.narrow, fontWeight: 800, fontSize: 150, letterSpacing: 6, color: ROSA, lineHeight: 1, textAlign: "center",
        textShadow: "0 0 30px rgba(0,0,0,0.6)", background: "rgba(8,15,20,0.35)"}}>
        {texto}
      </div>
    </div>
  );
};

/** El tubo: contador de pisos mientras la cápsula viaja. */
const Pisos: React.FC<{sube?: boolean}> = ({sube}) => {
  const f = useCurrentFrame();
  const orden = ["PISO 3", "PISO 2", "PISO 1", "PISO 0", "NIVEL −1"];
  const lista = sube ? [...orden].reverse() : orden;
  const i = Math.min(lista.length - 1, Math.floor(f / 3));
  return (
    <div style={{position: "absolute", right: 64, top: 150, textAlign: "right", fontFamily: VOZ.data, letterSpacing: 4}}>
      <div style={{fontSize: 22, color: "rgba(242,244,246,0.7)"}}>TUBO {sube ? "▲" : "▼"}</div>
      <div style={{fontSize: 30, color: ROSA, marginTop: 10}}>{lista[i]}</div>
    </div>
  );
};

// ── UN PLANO ────────────────────────────────────────────────────────────────
const Sobre: React.FC<{id: string}> = ({id}) => {
  const f = useCurrentFrame();
  if (id === "P01") return <PostIt />;
  if (id === "P04") return <TiraMarta f={f} />;
  if (id === "P11a") return <Rotulo id="P11a" l1="MÁS WOW" l2="2019" />;
  if (id === "V1") return <Rotulo id="V1" l1="V1" />;
  return null;
};

const Encima: React.FC<{id: string}> = ({id}) => {
  switch (id) {
    case "P01": case "P02b": return <Cabecera hora="18:30" />;
    case "N02": return <Pisos />;
    case "N03": case "P04": case "P05": return <Cabecera hora="18:33" />;
    case "P06": case "P07": case "N07": return <Cabecera hora="18:36" />;
    case "T1": return <Cabecera hora="19:10" />;
    case "COPY": return <><Cabecera hora="20:10" /><Golpe texto="COPY" /></>;
    case "PUNOS": return <Cabecera hora="20:12" />;
    case "DISENO": return <><Cabecera hora="22:40" /><Golpe texto="DISEÑO" /></>;
    case "P19": return <><Cabecera hora="23:05" /><Dato texto="ARCHIVADO · V1" top={1500} /></>;
    case "LISTO": return <><Cabecera hora="01:15" /><Golpe texto="LISTO" /></>;
    case "P09": return <><Cabecera hora="02:31" /><Notif quien="Gin" hora="02:31" msj="¿Puede ser más WOW? 🙏" /></>;
    case "P10": case "P11a": case "P11b": case "P11c": case "MARTA": return <Cabecera hora="02:32" />;
    case "E4": return <><Cabecera hora="04:50" /><Tokens /></>;
    case "P13": return <><Cabecera hora="06:40" /><Sello texto="APROBADO ✓" /></>;
    case "P14": return <Cabecera hora="06:41" />;
    case "P15": return <><Cabecera hora="06:58" /><Notif quien="Cliente" hora="06:58" msj="Mejor volvamos a la primera versión." /></>;
    case "MIRA": return <><Cabecera hora="06:58" /><Dato texto="TOKENS 1 %" top={250} color={CORAL} /></>;
    case "P21": case "V1": case "REENCIENDE": return <Cabecera hora="07:02" />;
    case "P17": return <><Cabecera hora="09:00" /><Dato texto="FINAL_APROBADO_V1.pdf ✓" top={1520} left={80} /></>;
    case "P22": return <><Cabecera hora="09:01" /><Dato texto="TOKENS 1 %" top={250} color={CORAL} /></>;
    default: return id.startsWith("E") ? <Cabecera hora={["02:40", "03:10", "03:35", "04:50", "05:20", "05:45", "06:05", "06:20"][Number(id.slice(1)) - 1]} /> : null;
  }
};

const Clip: React.FC<{p: Plano}> = ({p}) => {
  const f = useCurrentFrame();
  const z = p.zoom;
  const s = z ? interpolate(f, [0, p.dur], [z.s, z.s1 ?? z.s], clamp) : 1;
  const amp = p.sacudir ? p.sacudir * Math.max(0, 1 - f / 12) : 0;
  const dx = amp * Math.sin(f * 2.3), dy = amp * Math.cos(f * 3.1);
  return (
    <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
      <div style={{position: "absolute", inset: 0, transform: `translate(${dx}px, ${dy}px) scale(${s * (amp ? 1.03 : 1)})`,
        transformOrigin: z ? `${z.x} ${z.y}` : "50% 50%"}}>
        {p.still
          ? <Img src={staticFile(`assets/gcl/cap02-v3/video/${p.clip ?? p.id}.png`)} style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover"}} />
          : <OffthreadVideo src={v(p.clip ?? p.id)} startFrom={Math.round((p.desde ?? 0) * 30)} playbackRate={p.vel ?? 1} muted
              style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover"}} />}
        <Sobre id={p.id} />
      </div>
    </AbsoluteFill>
  );
};

/** Grano de película + viñeta suave sobre los planos con humanos (les quita el brillo de render). */
const Grano: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{pointerEvents: "none"}}>
      <svg width="100%" height="100%" style={{position: "absolute", inset: 0, opacity: 0.16, mixBlendMode: "overlay"}}>
        <filter id="grano"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed={f % 7} stitchTiles="stitch" />
          <feColorMatrix type="saturate" values="0" /></filter>
        <rect width="100%" height="100%" filter="url(#grano)" />
      </svg>
      <AbsoluteFill style={{background: "radial-gradient(ellipse at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.35) 100%)"}} />
    </AbsoluteFill>
  );
};


// ── SONIDO — cero voces humanas. El DING es uno solo, usado dos veces. ─────
type Pista = {src: string; desde: number; vol?: number; hasta?: number};
const SONIDO: Pista[] = [
  {src: fx("oficina-noche"), desde: 0, hasta: en("N02"), vol: 0.45},
  {src: fx("laptop-clac"), desde: en("P02b", 22)},
  {src: fx("tubo-baja"), desde: en("N02"), vol: 0.9},
  {src: fx("capsula-clonk"), desde: en("N03", 3)},
  {src: fx("marta-trrr"), desde: en("P04"), vol: 0.8, hasta: en("P05")},
  {src: fx("marta-mm"), desde: en("P04", 18)},
  {src: fx("rolo-bips"), desde: en("P05"), vol: 0.85, hasta: en("P06", 6)},
  {src: fx("rolo-servos"), desde: en("P05"), vol: 0.7, hasta: en("P06")},
  {src: fx("g-halo-hum"), desde: en("P06", 6), vol: 0.9},
  {src: fx("rolo-bips-calma"), desde: en("P07"), vol: 0.6},
  {src: fx("datos-entran"), desde: en("N07"), vol: 0.9},
  // satisfaction
  {src: fx("teclado-frenesi"), desde: en("T1"), vol: 0.6, hasta: en("COPY")},
  {src: fx("g-panel-tick"), desde: en("COPY"), vol: 1},
  {src: fx("g-panel-tick"), desde: en("PUNOS", 6), vol: 0.8},
  {src: fx("g-panel-tick"), desde: en("DISENO"), vol: 1},
  {src: fx("papel"), desde: en("P19", 2), vol: 0.6},
  {src: fx("cajon-metal"), desde: en("P19", 8), vol: 0.6},
  {src: fx("timbre-seco"), desde: en("LISTO", 2)},
  // primer giro — DING y silencio
  {src: fx("ding"), desde: en("P09")},
  {src: fx("g-eh"), desde: en("P09", 22), vol: 0.8},
  {src: fx("cajon-metal"), desde: en("P10", 4)},
  {src: fx("papel"), desde: en("P11a", 3), vol: 0.5},
  {src: fx("marta-mm"), desde: en("MARTA", 2), vol: 0.9},
  // escalada
  {src: fx("rolo-servos"), desde: en("E1"), vol: 0.6, hasta: en("E2")},
  {src: fx("papeles-caen"), desde: en("E2", 2), vol: 0.7},
  {src: fx("rolo-bips"), desde: en("E3"), vol: 0.6, hasta: en("E3", 12)},
  {src: fx("papel-rasga"), desde: en("E3", 14)},
  {src: fx("boing"), desde: en("E3", 16), vol: 0.8},
  {src: fx("g-glitch"), desde: en("E4", 10), vol: 0.5},
  {src: fx("g-glitch"), desde: en("E4", 18), vol: 0.6},
  {src: fx("rolo-servos"), desde: en("E5"), vol: 0.5, hasta: en("E6")},
  {src: fx("papeles-caen"), desde: en("E6"), vol: 0.6},
  {src: fx("marta-trrr-largo"), desde: en("E7"), vol: 0.6, hasta: en("E8")},
  {src: fx("g-glitch"), desde: en("E8", 3), vol: 0.7},
  // falsa victoria
  {src: fx("timbre-seco"), desde: en("P13")},
  {src: fx("wow-golpe"), desde: en("P13", 1), vol: 0.9},
  {src: fx("rolo-clonc"), desde: en("P14", 4), vol: 0.9},
  // pico
  {src: fx("ding"), desde: en("P15")},
  {src: fx("g-glitch"), desde: en("MIRA", 4), vol: 0.6},
  {src: fx("g-apagado"), desde: en("MIRA", 10), vol: 0.6},
  // resolución
  {src: fx("cajon-metal"), desde: en("P21", 2), vol: 0.7},
  {src: fx("papel"), desde: en("P21", 14), vol: 0.6},
  {src: fx("sting-triunfal"), desde: en("V1", 2)},
  {src: fx("g-halo-hum"), desde: en("REENCIENDE"), vol: 0.7},
  {src: fx("g-risa"), desde: en("REENCIENDE", 6), vol: 0.8},
  // epílogo
  {src: fx("oficina-manana"), desde: en("P17"), hasta: en("P22"), vol: 0.45},
  {src: fx("cafe-laptop"), desde: en("P17", 3), vol: 0.8},
  {src: fx("marta-trrr-largo"), desde: en("P22", 2), vol: 0.6, hasta: en("NEGRO", 10)},
];

// Musicalización narrativa, no una canción encima:
//   inicio sin track (ambiente + CLAC) · G activa el halo y los códigos: ENTRA la canción con
//   actitud · «¿más WOW?»: mute brutal · Marta saca la carpeta: silencio, metal y papel ·
//   escalada: la canción vuelve más rápida · APROBADO: golpe final y se corta · «volvamos a la
//   primera versión»: música muerta · Marta saca la V1: sting deadpan · final: TRRRR y negro.
const CANCION = "assets/gcl/cap02-v3/musica/temp-g-hype140.wav";
const TRAMOS_MUSICA = [
  {desde: en("N07", 6), hasta: en("P09"), desdeS: 5.0, vol: 0.62, fin: 2},
  {desde: en("E1"), hasta: en("P13", 2), desdeS: 8.0, vol: 0.66, fin: 2},
];

export const Cap02TurnoDeNocheV8: React.FC = () => {
  asegurarFuentes();
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      {PLANOS.map((p) => (
        <Sequence key={p.id} from={INICIO[p.id]} durationInFrames={p.dur}>
          {p.id === "CIERRE" ? <CierreSerie dur={p.dur} tagline={TAGLINE} titulo={PROXIMO} tw0={CIERRE_TW0} />
            : p.negro ? <AbsoluteFill style={{backgroundColor: "#000"}} />
            : <><Clip p={p} />{p.grano && <Grano />}<Encima id={p.id} /></>}
        </Sequence>
      ))}
      {SONIDO.map((s, i) => (
        <Sequence key={i} from={s.desde} durationInFrames={s.hasta ? s.hasta - s.desde : undefined}>
          <Audio src={s.src} volume={s.vol ?? 1} />
        </Sequence>
      ))}
      {TRAMOS_MUSICA.map((m, i) => (
        <Sequence key={`m${i}`} from={m.desde} durationInFrames={m.hasta - m.desde}>
          <Audio src={staticFile(CANCION)} startFrom={Math.round(m.desdeS * 30)}
            volume={(f) => m.vol * interpolate(f, [0, 5, m.hasta - m.desde - m.fin, m.hasta - m.desde], [0, 1, 1, 0], clamp)} />
        </Sequence>
      ))}
      {Array.from({length: PROXIMO.length}).map((_, i) => (
        <Sequence key={`t${i}`} from={en("CIERRE", CIERRE_TW0 + Math.round(i * 0.088 * 30))} durationInFrames={8}>
          <Audio src={fx("g-panel-tick")} volume={0.5} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
