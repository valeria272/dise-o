// ============================================================================
// G.CL / CAP.02 — «TURNO DE NOCHE» · CORTE 3 · «mañana lo veo»
// 30 fps · 1080×1920 · 25-09-2026
// ----------------------------------------------------------------------------
// Manda: gcl-agent/universo/06_VIDEO_REELS/CAP_02_TURNO_DE_NOCHE/GUION_V3_MANANA_LO_VEO.md
// Candado 20: los humanos NO hablan. Candado 21: el TUBO es el canal entre pisos.
//
//   HOOK        P01 post-it del cliente · N01 Pancho escribe en azul «mañana lo veo 9 AM» · P02 CLAC
//   EL TUBO     N02 la cápsula baja · N03 cae junto a Marta · P04 Marta lo imprime (mismo texto)
//   OH NO       P05 Rolo · G HERO P06 halo (entra la música) · P07 lo calma
//   V1          COPY · DISEÑO · V1 ✓
//   21:20 DING  P09 «¿Puede ser más WOW?» (grande) · la música se corta
//   MÁS WOW     P10 Marta la saca · P11a MÁS WOW 2019 (texto trackeado en perspectiva)
//   REVELACIÓN  N04 G piensa · N05 rayo del techo · N06 el robot dios · N07 le entran los códigos
//   CAOS        cortes de 8–14 f, el reloj corre de 21:40 a 05:58
//   AMANECER    N10 G manda la cápsula · N02 al revés (sube) · N11 llega al escritorio: «Todo listo. Revisar»
//   09:00       P17 Pancho · correo: ENVIAR · DING «Volvemos a la versión anterior» · REENVIAR ↓
//   BOOM        N02 baja · P16 G ✕✕ · N13 explota · N14 hollín
//   CIERRE      «Departamento de cosas imposibles.» · PRÓXIMO CAPÍTULO «Batalla campal: G vs humanos»
// ============================================================================
import React from "react";
import {AbsoluteFill, Audio, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame} from "remotion";
import {VOZ, asegurarFuentes} from "../../brand/copylab/sistema";
import {Superficie, Track, frameClip} from "./superficie";
import {CierreSerie, cierreFrames} from "./CierreSerie";
import trackP11a from "./track/P11a.json";
import trackP04 from "./track/P04.json";

const ROSA = "#FF2D8B";
const CORAL = "#FF6B3D";
const AZUL_LAPIZ = "#1f3fb8";
const v = (n: string) => staticFile(`assets/gcl/cap02-v3/video/${n}.mp4`);
const fx = (n: string) => staticFile(`assets/gcl/cap02-v3/sfx/${n}.mp3`);
const Y = (y: number) => y - 12; // clips a 1080×1944 → cover recorta 12 px arriba
const clamp = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;

const TAGLINE = "Departamento de cosas imposibles.";
const PROXIMO = "Batalla campal: G vs humanos";
const CIERRE_TW0 = 84;
const CIERRE = cierreFrames(PROXIMO, CIERRE_TW0);

type Plano = {
  id: string; clip?: string; dur: number; desde?: number; vel?: number;
  zoom?: {s: number; x: string; y: string; s1?: number}; sacudir?: number;
};
const PLANOS: Plano[] = [
  // HOOK
  {id: "P01", dur: 24, zoom: {s: 1.5, x: "47%", y: "67%", s1: 1.62}},
  {id: "N01", dur: 42, desde: 0, vel: 1.6},
  {id: "P02", dur: 27, desde: 0.8, vel: 2.8},
  // EL TUBO
  {id: "N02", dur: 18, desde: 0.3, vel: 2.2},
  {id: "N03", dur: 24, desde: 0.4, vel: 1.8},
  {id: "P04", dur: 30, desde: 1.8, zoom: {s: 1.55, x: "535px", y: "640px"}},
  // OH NO + G HERO
  {id: "P05", dur: 21, vel: 1.2},
  {id: "P06", dur: 27, desde: 0.3, vel: 2},
  {id: "P07", dur: 18, vel: 1.8},
  // V1
  {id: "P08a", dur: 9, desde: 0.5, vel: 2},
  {id: "P08b", dur: 9, desde: 0.5, vel: 2},
  {id: "P08c", dur: 12, desde: 0.5, vel: 1.6},
  // 21:20
  {id: "P09", dur: 36, desde: 0.3, sacudir: 8},
  {id: "P10", dur: 18, desde: 0.3, vel: 1.6},
  {id: "P11a", dur: 24, vel: 0.8},
  // REVELACIÓN
  {id: "N04", dur: 24, desde: 0.3, vel: 1.4},
  {id: "N05", dur: 24, desde: 0.3},
  {id: "N06", dur: 27, desde: 0.3, vel: 1.2},
  {id: "N07", dur: 24, desde: 0.4, vel: 1.4},
  // CAOS
  {id: "C1", clip: "N08", dur: 12, desde: 0.1, vel: 2, sacudir: 3},
  {id: "C2", clip: "N09", dur: 10, desde: 0.5, vel: 2},
  {id: "C3", clip: "P08b", dur: 8, desde: 1.5, vel: 2.5},
  {id: "C4", clip: "P20", dur: 10, desde: 0.5, vel: 2},
  {id: "C5", clip: "N08", dur: 8, desde: 0.7, vel: 2.4, sacudir: 3},
  {id: "C6", clip: "P19", dur: 8, desde: 1.0, vel: 2.5},
  {id: "C7", clip: "N09", dur: 8, desde: 2.5, vel: 2},
  {id: "C8", clip: "P12", dur: 14, desde: 0.5, vel: 1.8},
  {id: "C9", clip: "P20", dur: 8, desde: 2.5, vel: 2},
  {id: "C10", clip: "P08a", dur: 10, desde: 1.0, vel: 2.5, sacudir: 4},
  // AMANECER
  {id: "N10", dur: 24, desde: 0.8, vel: 1.5},
  {id: "SUBE", clip: "N02-sube", dur: 15, desde: 3.8, vel: 2.2},
  {id: "N11", dur: 30, desde: 1.4, vel: 1.4},
  // 09:00
  {id: "P17", dur: 30, desde: 0.5, vel: 1.5},
  {id: "MAIL", clip: "P17", dur: 45, desde: 3.5, vel: 0.3},
  {id: "RESP", clip: "P17", dur: 48, desde: 4.2, vel: 0.2},
  // BOOM
  {id: "BAJA", clip: "N02", dur: 15, desde: 0.3, vel: 2.5},
  {id: "MIRA", clip: "P16", dur: 18, vel: 0.9},
  {id: "N13", dur: 54, desde: 1.9, vel: 1.8},
  {id: "N14", dur: 40, desde: 0.2},
  {id: "CIERRE", dur: CIERRE},
];
const INICIO: Record<string, number> = {};
{let t = 0; for (const p of PLANOS) {INICIO[p.id] = t; t += p.dur;}}
export const TURNO_V3_FRAMES = PLANOS.reduce((a, p) => a + p.dur, 0);
const en = (id: string, extra = 0) => INICIO[id] + extra;
const P = (id: string) => PLANOS.find((p) => p.id === id)!;

// ── TEXTO DIEGÉTICO ─────────────────────────────────────────────────────────

/** El pedido del cliente, en plumón rojo/negro. Deja libre el cuarto de abajo para Pancho. */
const TextoCliente: React.FC<{w: number}> = ({w}) => (
  <>
    <div style={{fontSize: w * 0.22, fontWeight: 700, color: "#b3122e", textDecoration: "underline", textDecorationThickness: 4}}>URGENTE</div>
    <div style={{fontSize: w * 0.105, fontWeight: 600, marginTop: w * 0.03, color: "#b3122e"}}>pedido del cliente:</div>
    <div style={{fontSize: w * 0.135, fontWeight: 600}}>ajustar campaña</div>
    <div style={{fontSize: w * 0.14, fontWeight: 700, marginTop: w * 0.01}}>ENTREGA 09:00</div>
  </>
);

/** Post-it de P01, medido: t=0 → (391,1160)–(629,1435) · t=1,5 s → (384,1170)–(630,1454). */
const PostItP01: React.FC<{f: number}> = ({f}) => {
  const k = interpolate(f, [0, 45], [0, 1], clamp);
  const x0 = 391 - 7 * k, x1 = 629 + k, y0 = Y(1160 + 10 * k), y1 = Y(1435 + 19 * k);
  const w = x1 - x0;
  return (
    <div style={{position: "absolute", left: x0, top: y0, width: w, height: (y1 - y0) * 0.74, mixBlendMode: "multiply", color: "#1d1a33",
      fontFamily: VOZ.mano, textAlign: "center", transform: "rotate(-2deg)", filter: "blur(0.4px)",
      display: "flex", flexDirection: "column", justifyContent: "center", lineHeight: 0.95}}>
      <TextoCliente w={w} />
    </div>
  );
};

/** N01: el mismo post-it en macro + la línea de Pancho en lápiz azul, al ritmo de la mano.
 *  Medido por color sobre el clip: casi quieto, levemente torcido. La mano traza de verdad
 *  una raya azul abajo (≈88 % de alto): queda como subrayado de la frase. */
const POSTIT_N01: [number, number][] = [[228, 696], [801, 684], [829, 1333], [242, 1365]];
const QUIETO: Track = {ref: 0, w: 1080, h: 1944, fps: 24, H: {"0": [1, 0, 0, 0, 1, 0, 0, 0, 1]}};
const PostItN01: React.FC<{f: number}> = ({f}) => {
  const p = P("N01");
  const t = (p.desde ?? 0) + (f / 30) * (p.vel ?? 1);
  const escrito = interpolate(t, [0.15, 2.2], [0, 1], clamp);
  const W = 580, H = 660;
  return (
    <Superficie track={QUIETO} k={0} quad={POSTIT_N01} w={W} h={H} offsetY={-12} style={{mixBlendMode: "multiply"}}>
      <div style={{width: W, height: H, fontFamily: VOZ.mano, textAlign: "center", color: "#1d1a33", lineHeight: 0.95, filter: "blur(0.6px)"}}>
        <div style={{height: H * 0.7, display: "flex", flexDirection: "column", justifyContent: "center", transform: "rotate(-1.5deg)"}}>
          <TextoCliente w={W} />
        </div>
        <div style={{fontSize: W * 0.1, fontWeight: 500, color: AZUL_LAPIZ, transform: "rotate(-2deg)", whiteSpace: "nowrap", marginTop: H * 0.05,
          clipPath: `inset(-20% ${100 - escrito * 100}% -20% 0)`}}>
          mañana lo veo, 9 AM :)
        </div>
      </div>
    </Superficie>
  );
};

/** P04: Marta imprime EL MISMO mensaje que bajó por el tubo. Sale de la ranura hacia arriba. */
const TIRA_QUAD: [number, number][] = [[478, 470], [594, 470], [594, 832], [478, 832]];
const TiraMarta: React.FC<{f: number}> = ({f}) => {
  const p = P("P04");
  const k = frameClip(trackP04 as Track, f, p.desde ?? 0, p.vel ?? 1);
  const sale = interpolate(f, [0, 26], [1, 0], clamp);
  const lineas = ["URGENTE", "ajustar", "campaña", "ENTREGA", "09:00", "- - - -", "(mañana", "lo veo", "9 AM :)"];
  return (
    <Superficie track={trackP04 as Track} k={k} quad={TIRA_QUAD} w={116} h={362} offsetY={-12}
      style={{overflow: "hidden", mixBlendMode: "multiply"}}>
      <div style={{transform: `translateY(${sale * 362}px)`, textAlign: "center", fontFamily: VOZ.data, fontWeight: 600,
        fontSize: 19, lineHeight: "38px", color: "#2a2730", letterSpacing: 1, filter: "blur(0.3px)", paddingTop: 8}}>
        {lineas.map((l, i) => <div key={i} style={{fontWeight: i === 0 ? 800 : 600, fontSize: i === 0 ? 22 : 19}}>{l}</div>)}
      </div>
    </Superficie>
  );
};

/** P11a: el rótulo MÁS WOW, trackeado sobre la carpeta (homografía por frame). */
const ROTULO_QUAD: [number, number][] = [[352, 1218], [482, 1228], [500, 1296], [362, 1292]];
const RotuloWow: React.FC<{f: number}> = ({f}) => {
  const p = P("P11a");
  const k = frameClip(trackP11a as Track, f, p.desde ?? 0, p.vel ?? 1);
  return (
    <Superficie track={trackP11a as Track} k={k} quad={ROTULO_QUAD} w={160} h={80} offsetY={-12}
      style={{mixBlendMode: "multiply"}}>
      <div style={{width: 160, height: 80, display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center",
        fontFamily: VOZ.mano, color: "#1d1a33", lineHeight: 0.85, filter: "blur(0.4px)"}}>
        <div style={{fontSize: 44, fontWeight: 700}}>MÁS WOW</div>
        <div style={{fontSize: 26, fontWeight: 600}}>2019</div>
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

/** El reloj corre durante el caos: de 21:40 a 05:58. */
const RELOJ = {desde: 21 * 60 + 40, hasta: 24 * 60 + 5 * 60 + 58};
const RelojCaos: React.FC = () => {
  const f = useCurrentFrame();
  const t0 = en("C1"), t1 = en("N10");
  const m = Math.round(interpolate(f + t0, [t0, t1], [RELOJ.desde, RELOJ.hasta], clamp)) % (24 * 60);
  const hh = String(Math.floor(m / 60)).padStart(2, "0"), mm = String(m % 60).padStart(2, "0");
  return <Cabecera hora={`${hh}:${mm}`} />;
};

/** «¿Puede ser más WOW?» — la notificación entra como golpe, y el WOW revienta. */
const NotifWow: React.FC = () => {
  const f = useCurrentFrame();
  const s = spring({frame: f, fps: 30, config: {damping: 9, stiffness: 180}});
  const wow = spring({frame: f - 8, fps: 30, config: {damping: 6, stiffness: 160}});
  const brillo = 0.5 + 0.5 * Math.sin(f / 3);
  return (
    <>
      <AbsoluteFill style={{background: `rgba(255,45,139,${interpolate(f, [0, 2, 8], [0, 0.35, 0], clamp)})`}} />
      <div style={{position: "absolute", left: 90, right: 90, top: 620, transform: `scale(${interpolate(s, [0, 1], [0.6, 1])})`,
        opacity: interpolate(f, [0, 2], [0, 1], clamp), padding: "34px 40px 40px", borderRadius: 40, background: "rgba(20,20,24,0.94)",
        boxShadow: "0 30px 80px rgba(0,0,0,0.7)", fontFamily: VOZ.funcional, color: "#F2F4F6"}}>
        <div style={{display: "flex", alignItems: "center", gap: 16, fontSize: 28, color: "rgba(242,244,246,0.6)"}}>
          <div style={{width: 40, height: 40, borderRadius: 11, background: "#25D366"}} />
          <span>WhatsApp</span><span style={{marginLeft: "auto"}}>21:20</span>
        </div>
        <div style={{fontSize: 44, fontWeight: 700, marginTop: 14}}>Gin</div>
        <div style={{fontSize: 52, marginTop: 6, lineHeight: 1.15}}>¿Puede ser más</div>
        <div style={{fontFamily: VOZ.narrow, fontWeight: 800, fontSize: 250, lineHeight: 0.95, letterSpacing: 4, color: ROSA,
          transform: `scale(${interpolate(wow, [0, 1], [0.2, 1])}) rotate(${interpolate(wow, [0, 1], [-14, -4])}deg)`, transformOrigin: "30% 60%",
          textShadow: `0 0 ${30 + 40 * brillo}px rgba(255,45,139,0.8), 0 0 4px #fff`}}>
          WOW<span style={{color: "#F2F4F6"}}>?</span> <span style={{fontSize: 120}}>🙏</span>
        </div>
      </div>
    </>
  );
};

const Golpe: React.FC<{texto: string; check?: boolean}> = ({texto, check = true}) => (
  <div style={{position: "absolute", left: 0, right: 0, top: 1300, textAlign: "center", fontFamily: VOZ.narrow, fontWeight: 800,
    fontSize: 132, letterSpacing: 2, color: "#F2F4F6", textShadow: "0 4px 30px rgba(0,0,0,0.7)"}}>
    {texto} {check && <span style={{color: ROSA}}>✓</span>}
  </div>
);

const Dato: React.FC<{texto: string; top?: number; left?: number; color?: string; size?: number}> = ({texto, top = 1330, left = 64, color = ROSA, size = 30}) => (
  <div style={{position: "absolute", left, top, fontFamily: VOZ.data, fontSize: size, letterSpacing: 4, color,
    textShadow: "0 2px 14px rgba(0,0,0,0.9)"}}>{texto}</div>
);

const Tokens: React.FC = () => {
  const f = useCurrentFrame();
  const valor = f < 4 ? 24 : f < 9 ? 11 : 3;
  return <Dato texto={`TOKENS ${valor} %`} top={250} color={valor > 10 ? ROSA : CORAL} />;
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

/** Lo que trae la cápsula al escritorio de Pancho, al amanecer. */
const NotaTubo: React.FC = () => {
  const f = useCurrentFrame();
  const p = spring({frame: f - 10, fps: 30, config: {damping: 12}});
  return (
    <div style={{position: "absolute", left: 150, right: 150, top: 1180, transform: `translateY(${(1 - p) * 60}px) rotate(-3deg)`, opacity: p,
      background: "#F4EBD0", padding: "26px 34px", borderRadius: 6, boxShadow: "0 14px 40px rgba(0,0,0,0.5)", fontFamily: VOZ.data, color: "#2a2730"}}>
      <div style={{fontSize: 22, letterSpacing: 3, opacity: 0.7}}>NIVEL −1 → PANCHO · 06:47</div>
      <div style={{fontSize: 46, fontWeight: 700, marginTop: 10}}>Todo listo.</div>
      <div style={{fontSize: 46, fontWeight: 700}}>Revisar ✓</div>
    </div>
  );
};

// ── EL CORREO DE PANCHO (inserto de pantalla) ──────────────────────────────
const Cursor: React.FC<{x: number; y: number; clic?: boolean}> = ({x, y, clic}) => (
  <svg width={54} height={70} viewBox="0 0 18 24" style={{position: "absolute", left: x, top: y, transform: clic ? "scale(0.85)" : undefined,
    filter: "drop-shadow(0 3px 6px rgba(0,0,0,0.5))"}}>
    <path d="M1 1 L1 19 L6 14.5 L9.5 22 L12.5 20.7 L9 13.3 L15.5 13.3 Z" fill="#fff" stroke="#111" strokeWidth={1.3} />
  </svg>
);

const Ventana: React.FC<{children: React.ReactNode; titulo: string}> = ({children, titulo}) => (
  <div style={{position: "absolute", left: 60, right: 60, top: 430, borderRadius: 30, overflow: "hidden", background: "#FBFBFC",
    boxShadow: "0 40px 100px rgba(0,0,0,0.65)", fontFamily: VOZ.funcional, color: "#1b1b1f", transform: "perspective(1800px) rotateX(4deg)"}}>
    <div style={{display: "flex", alignItems: "center", gap: 14, padding: "22px 30px", background: "#EDEEF1", fontSize: 26, color: "#555"}}>
      <span style={{width: 18, height: 18, borderRadius: 9, background: "#FF5F57"}} />
      <span style={{width: 18, height: 18, borderRadius: 9, background: "#FEBC2E"}} />
      <span style={{width: 18, height: 18, borderRadius: 9, background: "#28C840"}} />
      <span style={{marginLeft: 20}}>{titulo}</span>
    </div>
    <div style={{padding: "10px 40px 40px"}}>{children}</div>
  </div>
);

const Campo: React.FC<{k: string; val: React.ReactNode}> = ({k, val}) => (
  <div style={{display: "flex", gap: 18, padding: "22px 0", borderBottom: "2px solid #E6E7EA", fontSize: 34}}>
    <span style={{color: "#8a8b90", width: 120}}>{k}</span><span style={{fontWeight: 600}}>{val}</span>
  </div>
);

const Boton: React.FC<{texto: string; activo: boolean}> = ({texto, activo}) => (
  <div style={{display: "inline-block", marginTop: 34, padding: "22px 54px", borderRadius: 18, fontSize: 38, fontWeight: 700, color: "#fff",
    background: ROSA, transform: activo ? "scale(0.94)" : undefined, boxShadow: activo ? "0 0 0 10px rgba(255,45,139,0.25)" : "none"}}>
    {texto}
  </div>
);

const Fondo: React.FC = () => <AbsoluteFill style={{backdropFilter: "blur(18px)", background: "rgba(8,15,20,0.45)"}} />;

const MailEnvio: React.FC = () => {
  const f = useCurrentFrame();
  const cuerpo = "Hola, va la campaña ajustada. Saludos.";
  const letras = Math.floor(interpolate(f, [2, 16], [0, cuerpo.length], clamp));
  const cx = interpolate(f, [16, 26], [900, 190], clamp), cy = interpolate(f, [16, 26], [1500, 1128], clamp);
  const clic = f >= 26 && f < 30;
  const vuela = interpolate(f, [30, 38], [0, 1], clamp);
  return (
    <>
      <Fondo />
      <div style={{position: "absolute", inset: 0, transform: `translateY(${-vuela * 1400}px) scale(${1 - vuela * 0.3})`, opacity: 1 - vuela}}>
        <Ventana titulo="Nuevo mensaje">
          <Campo k="Para" val="Cliente" />
          <Campo k="Asunto" val="Campaña ajustada ✓" />
          <div style={{marginTop: 22, display: "inline-flex", gap: 14, alignItems: "center", padding: "14px 22px", borderRadius: 14,
            background: "#FFE3EF", color: "#B0125E", fontSize: 30, fontWeight: 600}}>📎 campaña_WOW_final.pdf</div>
          <div style={{marginTop: 26, fontSize: 34, minHeight: 90, color: "#333"}}>{cuerpo.slice(0, letras)}</div>
          <Boton texto="Enviar" activo={clic} />
        </Ventana>
      </div>
      {f >= 30 && (
        <div style={{position: "absolute", left: 0, right: 0, top: 900, textAlign: "center", fontFamily: VOZ.funcional, fontSize: 44, fontWeight: 700,
          color: "#F2F4F6", opacity: interpolate(f, [30, 34], [0, 1], clamp)}}>Enviado ✓ <span style={{color: "rgba(242,244,246,0.6)", fontWeight: 400}}>09:03</span></div>
      )}
      {vuela < 1 && <Cursor x={cx} y={cy} clic={clic} />}
    </>
  );
};

const MailRespuesta: React.FC = () => {
  const f = useCurrentFrame();
  const entra = spring({frame: f - 6, fps: 30, config: {damping: 13, stiffness: 170}});
  const cx = interpolate(f, [22, 32], [860, 700], clamp), cy = interpolate(f, [22, 32], [1560, 1238], clamp);
  const clic = f >= 32 && f < 37;
  return (
    <>
      <Fondo />
      <Ventana titulo="Recibidos">
        <div style={{transform: `translateY(${(1 - entra) * -80}px)`, opacity: entra, padding: "30px 26px", margin: "20px -16px 0", borderRadius: 20,
          background: "#FFE3EF"}}>
          <div style={{display: "flex", fontSize: 32, fontWeight: 700}}><span>Cliente</span><span style={{marginLeft: "auto", fontWeight: 400, color: "#8a8b90"}}>09:04</span></div>
          <div style={{fontSize: 30, color: "#8a8b90", marginTop: 6}}>RE: Campaña ajustada ✓</div>
          <div style={{fontSize: 46, fontWeight: 700, marginTop: 16, lineHeight: 1.2}}>¡Gracias! Volvemos a la versión anterior 🙏</div>
        </div>
        <div style={{opacity: 0.35, padding: "26px 10px", fontSize: 30, borderBottom: "2px solid #E6E7EA"}}>Gin · ¿Puede ser más WOW?</div>
        <div style={{opacity: 0.35, padding: "26px 10px", fontSize: 30}}>Cliente · URGENTE ajustar campaña</div>
        <div style={{display: "flex", justifyContent: "flex-end"}}><Boton texto="Reenviar ↓" activo={clic} /></div>
      </Ventana>
      {f >= 37 && <Dato texto="→ NIVEL −1" top={1500} left={660} size={34} />}
      <Cursor x={cx} y={cy} clic={clic} />
    </>
  );
};

// ── UN PLANO ────────────────────────────────────────────────────────────────
const Sobre: React.FC<{id: string}> = ({id}) => {
  const f = useCurrentFrame();
  if (id === "P01") return <PostItP01 f={f} />;
  if (id === "N01") return <PostItN01 f={f} />;
  if (id === "P04") return <TiraMarta f={f} />;
  if (id === "P11a") return <RotuloWow f={f} />;
  return null;
};

const Encima: React.FC<{id: string}> = ({id}) => {
  switch (id) {
    case "P01": case "N01": case "P02": return <Cabecera hora="18:59" />;
    case "N02": case "BAJA": return <Pisos />;
    case "SUBE": return <Pisos sube />;
    case "N03": case "P04": case "P05": return <Cabecera hora="19:02" />;
    case "P06": case "P07": return <Cabecera hora="19:05" />;
    case "P08a": return <><Cabecera hora="20:10" /><Golpe texto="COPY" /></>;
    case "P08b": return <><Cabecera hora="20:40" /><Golpe texto="DISEÑO" /></>;
    case "P08c": return <><Cabecera hora="21:15" /><Golpe texto="V1" /></>;
    case "P09": return <><Cabecera hora="21:20" /><NotifWow /></>;
    case "P10": case "P11a": case "N04": case "N05": case "N06": case "N07": return <Cabecera hora="21:22" />;
    case "C8": return <><RelojCaos /><Tokens /></>;
    case "N10": return <Cabecera hora="06:02" />;
    case "N11": return <><Cabecera hora="06:47" /><NotaTubo /></>;
    case "P17": return <Cabecera hora="09:00" />;
    case "MAIL": return <><Cabecera hora="09:03" /><MailEnvio /></>;
    case "RESP": return <><Cabecera hora="09:04" /><MailRespuesta /></>;
    case "MIRA": case "N13": case "N14": return <Cabecera hora="09:05" />;
    default: return id.startsWith("C") ? <RelojCaos /> : <Cabecera />;
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
        <OffthreadVideo src={v(p.clip ?? p.id)} startFrom={Math.round((p.desde ?? 0) * 30)} playbackRate={p.vel ?? 1} muted
          style={{position: "absolute", width: "100%", height: "100%", objectFit: "cover"}} />
        <Sobre id={p.id} />
      </div>
    </AbsoluteFill>
  );
};

/** Destello de la explosión (N13): se ajusta al frame en que revienta el clip. */
const BOOM_F = 8;
const Destello: React.FC = () => {
  const f = useCurrentFrame();
  return <AbsoluteFill style={{background: "#fff", opacity: interpolate(f, [BOOM_F - 1, BOOM_F, BOOM_F + 5], [0, 1, 0], clamp)}} />;
};

// ── SONIDO ──────────────────────────────────────────────────────────────────
type Pista = {src: string; desde: number; vol?: number; hasta?: number};
const SONIDO: Pista[] = [
  {src: fx("oficina-noche"), desde: 0, hasta: en("N02"), vol: 0.45},
  {src: fx("lapiz"), desde: en("N01", 4), vol: 0.9},
  {src: fx("laptop-clac"), desde: en("P02", 8)},
  {src: fx("tubo-baja"), desde: en("N02"), vol: 0.9},
  {src: fx("capsula-clonk"), desde: en("N03", 3)},
  {src: fx("marta-trrr"), desde: en("P04"), vol: 0.8, hasta: en("P05")},
  {src: fx("marta-mm"), desde: en("P04", 18)},
  {src: fx("rolo-bips"), desde: en("P05"), vol: 0.85, hasta: en("P06", 6)},
  {src: fx("rolo-servos"), desde: en("P05"), vol: 0.7, hasta: en("P06")},
  {src: fx("g-halo-hum"), desde: en("P06", 8), vol: 0.8},
  {src: fx("rolo-bips-calma"), desde: en("P07"), vol: 0.6},
  {src: fx("g-panel-tick"), desde: en("P08a"), vol: 0.9},
  {src: fx("g-panel-tick"), desde: en("P08b"), vol: 0.9},
  {src: fx("timbre-seco"), desde: en("P08c")},
  // 21:20
  {src: fx("ding"), desde: en("P09")},
  {src: fx("wow-golpe"), desde: en("P09", 8)},
  {src: fx("g-eh"), desde: en("P09", 24), vol: 0.9},
  {src: fx("cajon-metal"), desde: en("P10", 2)},
  {src: fx("marta-mm"), desde: en("P10", 8), vol: 0.8},
  // revelación
  {src: fx("g-mm"), desde: en("N04", 4), vol: 0.9},
  {src: fx("coro-celestial"), desde: en("N05"), vol: 0.9, hasta: en("N07", 10)},
  {src: fx("datos-entran"), desde: en("N07"), vol: 0.9},
  // caos
  {src: fx("reloj-rapido"), desde: en("C1"), vol: 0.5, hasta: en("N10")},
  {src: fx("teclado-frenesi"), desde: en("C1"), vol: 0.7, hasta: en("C2")},
  {src: fx("rolo-bips"), desde: en("C2"), vol: 0.6, hasta: en("C3")},
  {src: fx("papeles-caen"), desde: en("C4"), vol: 0.7},
  {src: fx("teclado-frenesi"), desde: en("C5"), vol: 0.6, hasta: en("C6")},
  {src: fx("marta-trrr"), desde: en("C6"), vol: 0.6, hasta: en("C7")},
  {src: fx("g-glitch"), desde: en("C8", 6), vol: 0.4},
  {src: fx("teclado-frenesi"), desde: en("C10"), vol: 0.6, hasta: en("N10")},
  // amanecer
  {src: fx("tubo-sube"), desde: en("N10", 10), vol: 0.9},
  {src: fx("tubo-sube"), desde: en("SUBE"), vol: 0.6},
  {src: fx("oficina-manana"), desde: en("N11"), hasta: en("BAJA"), vol: 0.35},
  {src: fx("capsula-clonk"), desde: en("N11", 4)},
  {src: fx("papel"), desde: en("N11", 10), vol: 0.6},
  // 09:00
  {src: fx("cafe-laptop"), desde: en("P17", 3), vol: 0.7},
  {src: fx("click-enviar"), desde: en("MAIL", 26)},
  {src: fx("ding"), desde: en("RESP", 6)},
  {src: fx("click-enviar"), desde: en("RESP", 32), vol: 0.8},
  // boom
  {src: fx("tubo-baja"), desde: en("BAJA"), vol: 1},
  {src: fx("riser"), desde: en("MIRA"), vol: 0.8},
  {src: fx("g-glitch"), desde: en("MIRA", 4), vol: 0.6},
  {src: fx("explosion"), desde: en("N13", BOOM_F - 1)},
  {src: fx("papeles-caen"), desde: en("N14"), vol: 0.5},
  {src: fx("chispa"), desde: en("N14", 12), vol: 0.8},
  {src: fx("marta-mm"), desde: en("N14", 30), vol: 0.7},
];

// Música: entra con el halo, el DING de las 21:20 la corta, vuelve con los códigos
// (G se pone a trabajar), sigue por el amanecer y el correo, y el DING de la
// respuesta la mata. La explosión va seca.
const MUSICA_TEMP = "assets/gcl/cap02-v3/musica/temp-a-indierock.wav";
const TRAMOS_MUSICA = [
  {desde: en("P06", 6), hasta: en("P09"), desdeS: 0},
  {desde: en("N07", 12), hasta: en("RESP", 6), desdeS: 14},
];

export const Cap02TurnoDeNocheV3: React.FC<{musica?: string}> = ({musica = MUSICA_TEMP}) => {
  asegurarFuentes();
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      {PLANOS.map((p) => (
        <Sequence key={p.id} from={INICIO[p.id]} durationInFrames={p.dur}>
          {p.id === "CIERRE" ? <CierreSerie dur={p.dur} tagline={TAGLINE} titulo={PROXIMO} tw0={CIERRE_TW0} />
            : <><Clip p={p} /><Encima id={p.id} />{p.id === "N13" && <Destello />}</>}
        </Sequence>
      ))}
      {SONIDO.map((s, i) => (
        <Sequence key={i} from={s.desde} durationInFrames={s.hasta ? s.hasta - s.desde : undefined}>
          <Audio src={s.src} volume={s.vol ?? 1} />
        </Sequence>
      ))}
      {musica && TRAMOS_MUSICA.map((m, i) => (
        <Sequence key={`m${i}`} from={m.desde} durationInFrames={m.hasta - m.desde}>
          <Audio src={staticFile(musica)} startFrom={Math.round(m.desdeS * 30)}
            volume={(f) => 0.5 * interpolate(f, [0, 4, m.hasta - m.desde - 3, m.hasta - m.desde], [0, 1, 1, 0], clamp)} />
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
