// ============================================================================
// G.CL / CAP.02 — «TURNO DE NOCHE» · PRIMER CORTE
// 900 frames · 30,0 s · 30 fps · 1080×1920 · 25-09-2026
// ----------------------------------------------------------------------------
// Manda: gcl-agent/universo/06_VIDEO_REELS/CAP_02_TURNO_DE_NOCHE/GUION_FINAL.md
// Planos: out/gcl/cap02-v3/video/ (Hailuo 02, desde el storyboard aprobado).
//
// Todo el TEXTO va acá, en post, nunca dentro de la generación (lock 17):
// post-it, hoja de Marta, relojes, WhatsApp, carpeta, tokens, NO MOLESTAR.
//
// Montaje: CUT → CUT → CUT. Con aire sólo la mirada G → Marta, la falsa
// victoria y el apagado (GUION §18). La MÚSICA entra por prop cuando exista
// (la API de música de Magnific está retirada: se genera a mano, ver
// MUSICA_PROMPT.md). Sin ella el corte ya lleva ambiente, FX y voces.
//
// P11b se resuelve por montaje (3 intentos de Hailuo no lograron girar a G
// sin darle la espalda): G mira la carpeta → Marta indiferente → G sostiene.
// ============================================================================
import React from "react";
import {AbsoluteFill, Audio, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from "remotion";
import {VOZ, ancho, asegurarFuentes} from "../../brand/copylab/sistema";

const ROSA = "#FF2D8B";
const v = (n: string) => staticFile(`assets/gcl/cap02-v3/video/${n}.mp4`);
const fx = (n: string) => staticFile(`assets/gcl/cap02-v3/sfx/${n}.mp3`);
const voz = (n: string) => staticFile(`assets/gcl/cap02-v3/voz/${n}.mp3`);

// Los clips salen a 1080×1944: con cover quedan a escala 1 y se recortan 12 px
// arriba y abajo. Las coordenadas medidas en el clip se corrigen con Y().
const Y = (y: number) => y - 12;

// ── EL MONTAJE ──────────────────────────────────────────────────────────────
// id del plano · clip · duración en frames · desde (s de clip) · velocidad
type Plano = {id: string; clip?: string; dur: number; desde?: number; vel?: number; zoom?: {s: number; x: string; y: string}};
const PLANOS: Plano[] = [
  {id: "P01", dur: 45},
  {id: "P02", dur: 66, desde: 0.3, vel: 1.9},
  {id: "P03", dur: 24, desde: 1.5, vel: 3},
  {id: "P04", dur: 30, desde: 0, vel: 0.75},
  {id: "P05", dur: 36},
  {id: "P06", dur: 39, desde: 0.2, vel: 1.7},
  {id: "P07", dur: 39, vel: 1.4},
  {id: "P08a", dur: 22, desde: 0.5, vel: 1.5},
  {id: "P08b", dur: 22, desde: 0.5, vel: 1.5},
  {id: "P08c", dur: 22, desde: 0.5, vel: 1.5},
  {id: "P09", dur: 45, desde: 0.3},
  {id: "P10", dur: 39, desde: 0.3, vel: 1.1},
  {id: "P11a", dur: 30, vel: 0.6},
  {id: "P11b", dur: 36, desde: 0.3, vel: 1.2},
  {id: "MARTA", clip: "P04", dur: 18, desde: 0.05, vel: 0.15},
  {id: "P11c", clip: "P11b-alt", dur: 30, desde: 3.0},
  {id: "P12", dur: 39, desde: 0.5, vel: 1.4},
  {id: "P13", dur: 45, desde: 1.0, vel: 1.2},
  {id: "P14", dur: 36, desde: 1.5, vel: 2.2},
  {id: "P15", clip: "P09", dur: 30, desde: 2.0},
  {id: "P16", dur: 60, desde: 0.8, vel: 2},
  {id: "P17", dur: 60, desde: 0.5},
  {id: "P18", dur: 51, vel: 1.6, zoom: {s: 1.7, x: "49%", y: "58%"}},
  {id: "FIRMA", dur: 36},
];
const INICIO: Record<string, number> = {};
{let t = 0; for (const p of PLANOS) {INICIO[p.id] = t; t += p.dur;}}
export const TURNO_FRAMES = PLANOS.reduce((a, p) => a + p.dur, 0); // 900
const en = (id: string, extra = 0) => INICIO[id] + extra;

// ── PIEZAS DE TEXTO ─────────────────────────────────────────────────────────

/** El post-it de P01, medido cuadro a cuadro (máscara de amarillo):
 *  t=0 → (391,1160)–(629,1435) · t=1,5 s → (384,1170)–(630,1454). */
const PostItUrgente: React.FC<{f: number}> = ({f}) => {
  const k = interpolate(f, [0, 45], [0, 1], {extrapolateRight: "clamp"});
  const x0 = 391 + (384 - 391) * k, x1 = 629 + (630 - 629) * k;
  const y0 = Y(1160 + (1170 - 1160) * k), y1 = Y(1435 + (1454 - 1435) * k);
  const w = x1 - x0;
  return (
    <div style={{position: "absolute", left: x0, top: y0, width: w, height: y1 - y0, mixBlendMode: "multiply",
      color: "#1d1a33", fontFamily: VOZ.mano, textAlign: "center", transform: "rotate(-2deg)", filter: "blur(0.4px)",
      display: "flex", flexDirection: "column", justifyContent: "center", lineHeight: 0.95}}>
      <div style={{fontSize: w * 0.23, fontWeight: 700, color: "#b3122e", textDecoration: "underline", textDecorationThickness: 4}}>URGENTE</div>
      <div style={{fontSize: w * 0.14, fontWeight: 600, marginTop: w * 0.05}}>ajustar campaña</div>
      <div style={{fontSize: w * 0.15, fontWeight: 700, marginTop: w * 0.04}}>MAÑANA 9:00</div>
    </div>
  );
};

/** La hoja que imprime Marta (P04): el papel que asoma por arriba, de frente. */
const HojaMarta: React.FC = () => (
  <div style={{position: "absolute", left: 400, top: Y(815), width: 260, textAlign: "center", mixBlendMode: "multiply",
    fontFamily: VOZ.data, color: "#2a2a2a", fontSize: 30, letterSpacing: 3, lineHeight: 1.15, transform: "rotate(-3deg)", filter: "blur(0.5px)"}}>
    URGENTE<br />9:00
  </div>
);

/** El rótulo blanco de la carpeta en P11a: (285,1190)–(445,1265), estable. */
const RotuloCarpeta: React.FC = () => (
  <div style={{position: "absolute", left: 285, top: Y(1188), width: 162, height: 80, mixBlendMode: "multiply",
    display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", transform: "rotate(-7deg)",
    fontFamily: VOZ.mano, color: "#1d1a33", lineHeight: 0.9, filter: "blur(0.4px)"}}>
    <div style={{fontSize: 38, fontWeight: 700}}>MÁS WOW</div>
    <div style={{fontSize: 26, fontWeight: 600}}>2019</div>
  </div>
);

/** El post-it de P18 en el visor: (500,1098)–(558,1176) desde que Rolo lo pega. */
const NoMolestar: React.FC<{op: number}> = ({op}) => (
  <div style={{position: "absolute", left: 500, top: Y(1098), width: 58, height: 78, opacity: op, mixBlendMode: "multiply",
    display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", transform: "rotate(-4deg)",
    fontFamily: VOZ.mano, color: "#1d1a33", lineHeight: 0.85, fontWeight: 700, fontSize: 15, textAlign: "center"}}>
    NO<br />MOLES-<br />TAR
  </div>
);

/** Cabecera de serie, igual que el CAP.01 (arriba a la izquierda, todo el capítulo). */
const Cabecera: React.FC<{hora?: string}> = ({hora}) => (
  <div style={{position: "absolute", left: 64, top: 150, fontFamily: VOZ.data, letterSpacing: 4}}>
    <div style={{fontSize: 22, color: "rgba(242,244,246,0.7)"}}>TEMPORADA 1 · CAPÍTULO 02</div>
    {hora && <div style={{fontSize: 30, color: ROSA, marginTop: 10}}>{hora}</div>}
  </div>
);

/** Subtítulo de diálogo: Inter (voz funcional), sobre la zona segura de Reels. */
const Sub: React.FC<{texto: string}> = ({texto}) => (
  <div style={{position: "absolute", left: 80, right: 80, top: 1390, textAlign: "center", fontFamily: VOZ.funcional,
    fontWeight: 600, fontSize: 50, color: "#F2F4F6", textShadow: "0 2px 18px rgba(0,0,0,0.85)"}}>{texto}</div>
);

/** Notificación de WhatsApp sobre el panel de G (P09 / P15). Entra deslizando. */
const Notif: React.FC<{f: number; quien: string; hora: string; msj: string}> = ({f, quien, hora, msj}) => {
  const p = interpolate(f, [0, 6], [0, 1], {extrapolateRight: "clamp"});
  return (
    <div style={{position: "absolute", left: 250, top: 980 - (1 - p) * 60, width: 700, opacity: p, padding: "26px 30px",
      borderRadius: 34, background: "rgba(22,22,26,0.88)", boxShadow: "0 18px 50px rgba(0,0,0,0.6)", fontFamily: VOZ.funcional, color: "#F2F4F6"}}>
      <div style={{display: "flex", alignItems: "center", gap: 14, fontSize: 24, color: "rgba(242,244,246,0.6)"}}>
        <div style={{width: 34, height: 34, borderRadius: 9, background: "#25D366"}} />
        <span>WhatsApp</span><span style={{marginLeft: "auto"}}>{hora}</span>
      </div>
      <div style={{fontSize: 34, fontWeight: 700, marginTop: 12}}>{quien}</div>
      <div style={{fontSize: 38, marginTop: 4, lineHeight: 1.2}}>{msj}</div>
    </div>
  );
};

/** Los tres golpes del montaje (P08): COPY ✓ · DISEÑO ✓ · LISTO ✓. */
const Golpe: React.FC<{texto: string}> = ({texto}) => (
  <div style={{position: "absolute", left: 0, right: 0, top: 1300, textAlign: "center", fontFamily: VOZ.narrow,
    fontWeight: 800, fontSize: 132, letterSpacing: 2, color: "#F2F4F6", textShadow: "0 4px 30px rgba(0,0,0,0.7)"}}>
    {texto} <span style={{color: ROSA}}>✓</span>
  </div>
);

/** Tokens de G (P12): rápido, sin dashboard — 23 % → 11 % → 4 %. */
const Tokens: React.FC<{f: number}> = ({f}) => {
  const valor = f < 13 ? 23 : f < 26 ? 11 : 4;
  const color = valor > 10 ? ROSA : "#FF6B3D";
  return (
    <div style={{position: "absolute", left: 64, top: 250, fontFamily: VOZ.data, letterSpacing: 4, fontSize: 30, color}}>
      TOKENS {valor} %
    </div>
  );
};

// ── UN PLANO ────────────────────────────────────────────────────────────────
const Clip: React.FC<{p: Plano}> = ({p}) => {
  const vel = p.vel ?? 1;
  const z = p.zoom;
  return (
    <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
      <div style={{position: "absolute", inset: 0, transform: z ? `scale(${z.s})` : undefined, transformOrigin: z ? `${z.x} ${z.y}` : undefined}}>
        <OffthreadVideo src={v(p.clip ?? p.id)} startFrom={Math.round((p.desde ?? 0) * 30)} playbackRate={vel} muted
          style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover"}} />
        <Sobre p={p} />
      </div>
    </AbsoluteFill>
  );
};

/** Lo que va pegado a la superficie del plano (se escala con el zoom). */
const Sobre: React.FC<{p: Plano}> = ({p}) => {
  const f = useCurrentFrame();
  if (p.id === "P01") return <PostItUrgente f={f} />;
  if (p.id === "P04") return <HojaMarta />;
  if (p.id === "P11a") return <RotuloCarpeta />;
  if (p.id === "P18") {
    const t = (f / 30) * (p.vel ?? 1); // segundos de clip
    return <NoMolestar op={interpolate(t, [0.6, 0.8], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})} />;
  }
  return null;
};

/** Lo que flota sobre el plano (no se escala). */
const Encima: React.FC<{p: Plano}> = ({p}) => {
  const f = useCurrentFrame();
  switch (p.id) {
    case "P01": case "P02": return <Cabecera hora="18:59" />;
    case "P06": case "P07": return <Cabecera hora="00:58" />;
    case "P08a": return <><Cabecera hora="00:58" /><Golpe texto="COPY" /></>;
    case "P08b": return <><Cabecera hora="00:58" /><Golpe texto="DISEÑO" /></>;
    case "P08c": return <><Cabecera hora="00:58" /><Golpe texto="LISTO" /></>;
    case "P09": return <><Cabecera /><Notif f={f} quien="Gin" hora="02:31" msj="¿Y si lo hacemos más WOW? 🙏" /></>;
    case "P15": return <><Cabecera /><Notif f={f} quien="Pancho" hora="07:02" msj="Oye… una cosita más." /></>;
    case "P12": return <><Cabecera hora="06:58" /><Tokens f={f} /></>;
    case "P17": return <Cabecera hora="09:00" />;
    case "FIRMA": return null;
    default: return <Cabecera />;
  }
};

const Firma: React.FC = () => {
  const f = useCurrentFrame();
  const op = interpolate(f, [4, 12], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{backgroundColor: "#080F14", justifyContent: "center", alignItems: "center"}}>
      <div style={{opacity: op, fontFamily: VOZ.impacto, fontVariationSettings: ancho(90, 900), fontSize: 96, color: "#F2F4F6", letterSpacing: 2}}>
        G.CL <span style={{color: ROSA}}>×</span> COPYLAB
      </div>
    </AbsoluteFill>
  );
};

// ── SONIDO (GUION §20–21) ───────────────────────────────────────────────────
type Pista = {src: string; desde: number; vol?: number; hasta?: number};
const SONIDO: Pista[] = [
  // arriba, noche
  {src: fx("oficina-noche"), desde: 0, hasta: en("P03"), vol: 0.45},
  {src: fx("laptop-clac"), desde: en("P02", 14)},
  {src: voz("pancho-manana"), desde: en("P02", 19), vol: 1},
  {src: fx("luces-clac"), desde: en("P03")},
  // abajo
  {src: fx("marta-trrr"), desde: en("P04"), vol: 0.8, hasta: en("P05", 10)},
  {src: voz("marta-otra-vez"), desde: en("P04", 6)},
  {src: fx("rolo-bips"), desde: en("P05"), vol: 0.8, hasta: en("P06", 8)},
  {src: fx("rolo-servos"), desde: en("P05"), vol: 0.7, hasta: en("P06")},
  {src: fx("g-halo-hum"), desde: en("P06", 12), vol: 0.8},
  {src: fx("rolo-bips-calma"), desde: en("P07"), vol: 0.7},
  {src: fx("papel"), desde: en("P07", 26), vol: 0.7},
  {src: fx("g-panel-tick"), desde: en("P08a"), vol: 0.9},
  {src: fx("g-panel-tick"), desde: en("P08b"), vol: 0.9},
  {src: fx("timbre-seco"), desde: en("P08c")},
  // primer giro
  {src: fx("ding"), desde: en("P09")},
  {src: fx("cajon-metal"), desde: en("P10", 5)},
  {src: fx("papel"), desde: en("P11a", 4), vol: 0.5},
  // escalada y falsa victoria
  {src: fx("g-glitch"), desde: en("P12", 26), vol: 0.35},
  {src: fx("rolo-clonc"), desde: en("P14", 8), vol: 0.9},
  // pico
  {src: fx("ding"), desde: en("P15")},
  {src: voz("pancho-cosita"), desde: en("P15", 5)},
  {src: fx("g-glitch"), desde: en("P16", 10)},
  {src: fx("g-apagado"), desde: en("P16", 30)},
  // mañana
  {src: fx("oficina-manana"), desde: en("P17"), hasta: en("P18"), vol: 0.5},
  {src: fx("cafe-laptop"), desde: en("P17", 2), vol: 0.7},
  {src: voz("pancho-solito"), desde: en("P17", 14)},
  // abajo, final: TRRRR de Marta hasta el negro
  {src: fx("papel"), desde: en("P18", 14), vol: 0.5},
  {src: fx("marta-trrr-largo"), desde: en("P18", 18), vol: 0.35, hasta: en("FIRMA", 12)},
];

// Música (cuando exista): entra con G, se corta con el primer DING, vuelve
// después del gag más intensa, golpe en LISTO y muere con el segundo DING.
const TRAMOS_MUSICA = [
  {desde: en("P06"), hasta: en("P09"), desdeS: 0},
  {desde: en("P11c", 20), hasta: en("P13", 6), desdeS: 22},
];

export const Cap02TurnoDeNoche: React.FC<{musica?: string}> = ({musica}) => {
  asegurarFuentes();
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      {PLANOS.map((p) => (
        <Sequence key={p.id} from={INICIO[p.id]} durationInFrames={p.dur}>
          {p.id === "FIRMA" ? <Firma /> : <><Clip p={p} /><Encima p={p} /></>}
        </Sequence>
      ))}

      {/* subtítulos de diálogo */}
      <Sequence from={en("P02", 21)} durationInFrames={48}><Sub texto="Ya… lo vemos mañana." /></Sequence>
      <Sequence from={en("P04", 8)} durationInFrames={30}><Sub texto="Otra vez." /></Sequence>
      <Sequence from={en("P17", 16)} durationInFrames={42}><Sub texto="¿Ven? Salió solito." /></Sequence>

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
