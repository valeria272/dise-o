/**
 * AdvertiqHero.tsx — Video hero de ADVERTIQ (1920×1080, 30fps, ~31s).
 *
 * Estilo publicitario fintech (tipo FPay / Pago Fácil): tipografía cinética, marco de
 * producto (browser), count-up de dinero, gradientes en movimiento, glow y crossfades.
 * Recreación del backoffice: hook → conectar OAuth → chat+guardián → aprobar+bitácora → cierre.
 *
 * VO en public/advertiq/vo.wav (regrabar: ver scripts/process-vo.sh → actualizar LINE_SECONDS).
 * Subtítulos siempre visibles (el hero parte silenciado). Identidad violeta/lila = sitio.
 */
import React from "react";
import {
  AbsoluteFill, Sequence, interpolate, spring, staticFile,
  useCurrentFrame, useVideoConfig, Easing,
} from "remotion";
import {Audio} from "@remotion/media";
import {loadGoogleFont} from "../presets/fonts";
import {AudioTrack} from "../components/media/AudioTrack";

export const ADVERTIQ_HERO_FPS = 30;

// Cortes de escena (seg), alineados a los silencios reales de la VO (ElevenLabs).
// vo.wav = public/advertiq/vo.wav (voz pro). Para re-cuadrar con otra voz: correr
// silencedetect sobre el nuevo audio y ajustar estos boundaries.
const SCENE_BOUNDS_SECONDS = [0, 7.67, 13.08, 20.35, 24.23, 29.1526];

const C = {
  bg: "#f4f2fb", surface: "#ffffff", ink: "#1f1a2e", muted: "#6b6480",
  accent: "#7c5cff", accentDeep: "#6d28d9", lila: "#b9a7ff", border: "#e6e1f2",
  ok: "#1f9d78", danger: "#e5484d",
};
const DISPLAY = "'Fraunces', serif";
const SANS = "'Figtree', sans-serif";
const MONO = "'JetBrains Mono', monospace";
const ease = {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)} as const;
const fmt = (n: number) => "$" + Math.round(n).toLocaleString("es-CL");

const CAPTIONS = [
  "Conoce al agente experto en paid media — entrenado por especialistas con +15 años de trayectoria.",
  "Conectas Meta o Google con un click. Seguro, sin entregar contraseñas.",
  "Le pides: «súbele 15% al ganador». El guardián valida la moneda y tu tope antes de mover un peso.",
  "Tú apruebas con un click. Todo queda en bitácora, en tiempo real.",
  "ADVERTIQ. Pauta como un senior, cuida la plata como un CFO.",
];

// ── icons / logo ──────────────────────────────────────────────────────────────
function LogoMark({size = 64}: {size?: number}) {
  return (
    <svg width={size} height={size} viewBox="0 0 32 32" fill="none">
      <defs><linearGradient id="vh-g" x1="0" y1="0" x2="32" y2="32" gradientUnits="userSpaceOnUse"><stop stopColor="#9B7CFF" /><stop offset="1" stopColor="#6D28D9" /></linearGradient></defs>
      <rect width="32" height="32" rx="9" fill="url(#vh-g)" />
      <path d="M16 6.5 L23.5 9.6 V16 C23.5 20.8 16 25.5 16 25.5 C16 25.5 8.5 20.8 8.5 16 V9.6 Z" fill="#fff" fillOpacity="0.2" />
      <path d="M11.6 18.4 L16 12.8 L20.4 18.4" stroke="#fff" strokeWidth="2.3" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
}
const Shield = ({s = 22, color = C.ok}: {s?: number; color?: string}) => (
  <svg width={s} height={s} viewBox="0 0 24 24" fill="none"><path d="M12 3 L19 6 V12 C19 16.5 12 20 12 20 C12 20 5 16.5 5 12 V6 Z" fill={color} fillOpacity="0.16" stroke={color} strokeWidth="1.6"/><path d="M8.7 12.2 l2.4 2.4 4.2-4.6" stroke={color} strokeWidth="1.8" fill="none" strokeLinecap="round" strokeLinejoin="round"/></svg>
);
const Check = ({s = 18, color = C.ok}: {s?: number; color?: string}) => (
  <svg width={s} height={s} viewBox="0 0 24 24" fill="none"><path d="M5 12.5 l4 4 L19 6.5" stroke={color} strokeWidth="2.4" fill="none" strokeLinecap="round" strokeLinejoin="round"/></svg>
);

// Logos de plataforma (reconocibles → el demo no se ve falso)
const FbLogo = ({s = 32}: {s?: number}) => (
  <svg width={s} height={s} viewBox="0 0 40 40"><rect width="40" height="40" rx="10" fill="#1877F2"/><path d="M25.6 20.6h-3.4V32h-4.7V20.6h-2.4v-4h2.4v-2.7c0-3.2 1.4-5.2 5.2-5.2h3.3v4h-2c-1.5 0-1.6.6-1.6 1.7l-.1 2.2h3.8l-.5 4z" fill="#fff"/></svg>
);
const IgLogo = ({s = 32}: {s?: number}) => (
  <svg width={s} height={s} viewBox="0 0 40 40">
    <defs><linearGradient id="ig-g" x1="2" y1="38" x2="38" y2="2" gradientUnits="userSpaceOnUse"><stop stopColor="#FEDA75"/><stop offset="0.25" stopColor="#FA7E1E"/><stop offset="0.5" stopColor="#D62976"/><stop offset="0.75" stopColor="#962FBF"/><stop offset="1" stopColor="#4F5BD5"/></linearGradient></defs>
    <rect width="40" height="40" rx="11" fill="url(#ig-g)"/>
    <rect x="10" y="10" width="20" height="20" rx="6" fill="none" stroke="#fff" strokeWidth="2.4"/>
    <circle cx="20" cy="20" r="5" fill="none" stroke="#fff" strokeWidth="2.4"/>
    <circle cx="26.6" cy="13.4" r="1.7" fill="#fff"/>
  </svg>
);
const GoogleG = ({s = 32}: {s?: number}) => (
  <svg width={s} height={s} viewBox="0 0 48 48">
    <path fill="#4285F4" d="M45.12 24.5c0-1.56-.14-3.06-.4-4.5H24v8.51h11.84c-.51 2.75-2.06 5.08-4.39 6.64v5.52h7.11c4.16-3.83 6.56-9.47 6.56-16.17z"/>
    <path fill="#34A853" d="M24 46c5.94 0 10.92-1.97 14.56-5.33l-7.11-5.52c-1.97 1.32-4.49 2.1-7.45 2.1-5.73 0-10.58-3.87-12.31-9.07H4.34v5.7C7.96 41.07 15.4 46 24 46z"/>
    <path fill="#FBBC05" d="M11.69 28.18C11.25 26.86 11 25.45 11 24s.25-2.86.69-4.18v-5.7H4.34C2.85 17.09 2 20.45 2 24s.85 6.91 2.34 9.88l7.35-5.7z"/>
    <path fill="#EA4335" d="M24 10.75c3.23 0 6.13 1.11 8.41 3.29l6.31-6.31C34.91 4.18 29.93 2 24 2 15.4 2 7.96 6.93 4.34 14.12l7.35 5.7c1.73-5.2 6.58-9.07 12.31-9.07z"/>
  </svg>
);

// ── background con orbes + grid (movimiento continuo) ───────────────────────────
const Bg: React.FC<{children?: React.ReactNode}> = ({children}) => {
  const frame = useCurrentFrame();
  const t = frame / ADVERTIQ_HERO_FPS;
  const x1 = 82 + Math.sin(t * 0.35) * 12, y1 = 6 + Math.cos(t * 0.24) * 8;
  const x2 = 10 + Math.cos(t * 0.28) * 12, y2 = 92 + Math.sin(t * 0.22) * 8;
  const x3 = 50 + Math.sin(t * 0.18) * 18, y3 = 50 + Math.cos(t * 0.2) * 14;
  return (
    <AbsoluteFill style={{backgroundColor: C.bg, fontFamily: SANS}}>
      <AbsoluteFill style={{background:
        `radial-gradient(ellipse 50% 46% at ${x1}% ${y1}%, ${C.accent}30 0%, transparent 60%),
         radial-gradient(ellipse 48% 44% at ${x2}% ${y2}%, ${C.lila}40 0%, transparent 62%),
         radial-gradient(ellipse 60% 55% at ${x3}% ${y3}%, ${C.accentDeep}14 0%, transparent 65%)`}} />
      <AbsoluteFill style={{opacity: 0.5, backgroundImage:
        `linear-gradient(${C.border}55 1px, transparent 1px), linear-gradient(90deg, ${C.border}55 1px, transparent 1px)`,
        backgroundSize: "64px 64px", maskImage: "radial-gradient(ellipse 80% 80% at 50% 45%, #000 30%, transparent 75%)"}} />
      {children}
      {/* progreso publicitario + marca persistente */}
      <ProgressBar />
      <div style={{position: "absolute", bottom: 26, right: 34, display: "flex", alignItems: "center", gap: 10, opacity: 0.8}}>
        <LogoMark size={26} /><span style={{fontFamily: DISPLAY, fontWeight: 600, fontSize: 24, color: C.ink}}>ADVERTIQ</span>
      </div>
    </AbsoluteFill>
  );
};
const ProgressBar: React.FC = () => {
  const f = useCurrentFrame(); const {durationInFrames} = useVideoConfig();
  const w = interpolate(f, [0, durationInFrames], [0, 100], {extrapolateRight: "clamp"});
  return (
    <div style={{position: "absolute", top: 0, left: 0, right: 0, height: 5, background: `${C.border}`}}>
      <div style={{height: "100%", width: `${w}%`, background: `linear-gradient(90deg, ${C.lila}, ${C.accent}, ${C.accentDeep})`}} />
    </div>
  );
};

// ── building blocks ─────────────────────────────────────────────────────────────
const SceneWrap: React.FC<{dur: number; children: React.ReactNode}> = ({dur, children}) => {
  const f = useCurrentFrame();
  const inO = interpolate(f, [0, 10], [0, 1], ease);
  const outO = interpolate(f, [dur - 12, dur], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.in(Easing.cubic)});
  const scale = interpolate(f, [0, 14], [0.965, 1], ease);
  return <AbsoluteFill style={{opacity: Math.min(inO, outO), transform: `scale(${scale})`}}>{children}</AbsoluteFill>;
};

const Kinetic: React.FC<{text: string; size: number; color?: string; weight?: number; delay?: number}> = ({text, size, color = C.ink, weight = 600, delay = 0}) => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  return (
    <div style={{display: "flex", flexWrap: "wrap", justifyContent: "center", gap: "0.16em 0.28em", maxWidth: 1400}}>
      {text.split(" ").map((w, i) => {
        const s = spring({frame: f - delay - i * 2.4, fps, config: {damping: 160, stiffness: 120}});
        return <span key={i} style={{display: "inline-block", fontFamily: DISPLAY, fontSize: size, fontWeight: weight, color, lineHeight: 1.12, letterSpacing: -1, opacity: s, transform: `translateY(${interpolate(s, [0, 1], [34, 0])}px)`}}>{w}</span>;
      })}
    </div>
  );
};

const BrowserFrame: React.FC<{w: number; url: string; children: React.ReactNode}> = ({w, url, children}) => (
  <div style={{width: w, background: C.surface, borderRadius: 24, border: `1px solid ${C.border}`, boxShadow: `0 50px 120px -50px rgba(31,26,46,0.55), 0 0 0 6px #ffffff`, overflow: "hidden"}}>
    <div style={{display: "flex", alignItems: "center", gap: 9, padding: "16px 20px", borderBottom: `1px solid ${C.border}`, background: "#faf9fe"}}>
      <span style={{width: 13, height: 13, borderRadius: 99, background: "#ff5f57"}} />
      <span style={{width: 13, height: 13, borderRadius: 99, background: "#febc2e"}} />
      <span style={{width: 13, height: 13, borderRadius: 99, background: "#28c840"}} />
      <div style={{marginLeft: 14, flex: 1, background: C.bg, borderRadius: 9, padding: "8px 16px", fontFamily: MONO, fontSize: 19, color: C.muted}}>{url}</div>
    </div>
    <div style={{padding: 40}}>{children}</div>
  </div>
);

// ── Escena 1: HOOK ───────────────────────────────────────────────────────────────
const Hook: React.FC = () => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const logo = spring({frame: f, fps, config: {damping: 120, stiffness: 140}});
  return (
    <AbsoluteFill style={{justifyContent: "center", alignItems: "center", padding: 120, textAlign: "center"}}>
      <div style={{transform: `scale(${interpolate(logo, [0, 1], [0.4, 1])}) rotate(${interpolate(logo, [0, 1], [-25, 0])}deg)`, marginBottom: 26}}><LogoMark size={76} /></div>
      <div style={{marginBottom: 22, display: "inline-flex", alignItems: "center", gap: 10, fontSize: 24, fontWeight: 600, color: C.accentDeep, background: `${C.accent}16`, border: `1px solid ${C.accent}3a`, padding: "10px 20px", borderRadius: 999, opacity: interpolate(f, [4, 16], [0, 1], ease)}}>
        <Shield s={22} color={C.accentDeep} /> Entrenado por especialistas con +15 años en paid media
      </div>
      <Kinetic text="Un agente experto en Paid Media" size={80} delay={10} />
      <div style={{marginTop: 26, fontSize: 36, color: C.muted, maxWidth: 1180, lineHeight: 1.3, opacity: interpolate(f, [34, 48], [0, 1], ease)}}>Implementa, optimiza y reporta tus campañas. Y cuida cada peso, 24/7.</div>
    </AbsoluteFill>
  );
};

// ── Escena 2: CONECTAR (tarjetas reales de Meta y Google) ────────────────────────
const ConectadaChip = () => (
  <span style={{display: "inline-flex", alignItems: "center", gap: 8, background: `${C.ok}14`, color: C.ok, fontWeight: 700, fontSize: 18, padding: "8px 14px", borderRadius: 10, border: `1px solid ${C.ok}55`}}><Check s={18} /> Conectada</span>
);
const PlatformCard: React.FC<{anim: number; head: React.ReactNode; headBg: string; id: string; sub: string}> = ({anim, head, headBg, id, sub}) => (
  <div style={{opacity: anim, transform: `translateY(${interpolate(anim, [0, 1], [30, 0])}px)`, width: 484, borderRadius: 18, overflow: "hidden", border: `1px solid ${C.border}`, background: "#fff", textAlign: "left", boxShadow: "0 20px 50px -30px rgba(31,26,46,0.4)"}}>
    <div style={{background: headBg, padding: "16px 22px", display: "flex", alignItems: "center", gap: 12}}>{head}</div>
    <div style={{padding: "20px 22px", display: "flex", alignItems: "center", justifyContent: "space-between"}}>
      <div><div style={{fontFamily: MONO, fontSize: 18, color: C.muted}}>{id}</div><div style={{fontSize: 21, fontWeight: 600, color: C.ink}}>{sub}</div></div>
      <ConectadaChip />
    </div>
  </div>
);
const Connect: React.FC = () => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const c1 = spring({frame: f - 10, fps, config: {damping: 130, stiffness: 130}});
  const c2 = spring({frame: f - 24, fps, config: {damping: 130, stiffness: 130}});
  return (
    <AbsoluteFill style={{justifyContent: "center", alignItems: "center"}}>
      <BrowserFrame w={1180} url="andes-retail.advertiq.app/onboarding">
        <div style={{textAlign: "center"}}>
          <div style={{fontFamily: DISPLAY, fontSize: 48, fontWeight: 600, color: C.ink, opacity: interpolate(f, [0, 12], [0, 1], ease)}}>Conecta tus cuentas en un click</div>
          <div style={{display: "flex", gap: 28, marginTop: 30, justifyContent: "center"}}>
            <PlatformCard anim={c1} headBg="#0866FF" id="act_1149308…" sub="Facebook + Instagram"
              head={<><FbLogo s={30} /><IgLogo s={30} /><span style={{color: "#fff", fontWeight: 700, fontSize: 24}}>Meta Ads</span></>} />
            <PlatformCard anim={c2} headBg="#ffffff" id="699-238-9876" sub="Search · Performance Max"
              head={<><GoogleG s={28} /><span style={{color: "#3c4043", fontWeight: 700, fontSize: 24}}>Google Ads</span></>} />
          </div>
          <div style={{marginTop: 30, display: "flex", alignItems: "center", justifyContent: "center", gap: 12, fontSize: 26, color: C.muted, opacity: interpolate(f, [40, 54], [0, 1], ease)}}><Shield s={26} color={C.accent} /> OAuth oficial · sin entregar contraseñas</div>
        </div>
      </BrowserFrame>
    </AbsoluteFill>
  );
};

// ── Escena 3: CHAT + GUARDIÁN (el momento clave) ─────────────────────────────────
const Guardian: React.FC = () => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const bubble = spring({frame: f - 6, fps, config: {damping: 140}});
  const card = spring({frame: f - 30, fps, config: {damping: 130, stiffness: 120}});
  const count = interpolate(f, [40, 70], [78000, 89700], ease);
  const glow = 0.5 + 0.5 * Math.sin(f / 6);
  const row = (d: number) => interpolate(f, [d, d + 12], [0, 1], ease);
  return (
    <AbsoluteFill style={{justifyContent: "center", alignItems: "center"}}>
      <BrowserFrame w={1080} url="andes-retail.advertiq.app/meta/campañas">
        <div style={{display: "flex", alignItems: "center", justifyContent: "space-between", paddingBottom: 14, marginBottom: 18, borderBottom: `1px solid ${C.border}`, opacity: interpolate(f, [0, 10], [0, 1], ease)}}>
          <div style={{display: "flex", alignItems: "center", gap: 10}}><FbLogo s={26} /><IgLogo s={26} /><span style={{fontWeight: 700, fontSize: 22, color: C.ink}}>Meta Ads · Campañas activas</span></div>
          <div style={{display: "flex", alignItems: "center", gap: 10, fontSize: 18, color: C.muted}}><span style={{width: 9, height: 9, borderRadius: 99, background: C.ok, display: "inline-block"}} /> Ganador · <span style={{fontFamily: MONO, color: C.ink, fontWeight: 600}}>ROAS 4,8x</span></div>
        </div>
        <div style={{display: "flex", justifyContent: "flex-end", opacity: bubble, transform: `translateX(${interpolate(bubble, [0, 1], [40, 0])}px)`}}>
          <div style={{background: C.accent, color: "#fff", fontSize: 30, fontWeight: 600, padding: "16px 26px", borderRadius: "20px 20px 6px 20px"}}>Súbele 15% al ganador de Meta</div>
        </div>
        <div style={{opacity: card, transform: `translateY(${interpolate(card, [0, 1], [44, 0])}px)`, marginTop: 24, borderRadius: 20, padding: 30, border: `1px solid ${C.accent}40`, background: "#fff", boxShadow: `0 0 ${24 + glow * 26}px ${C.accent}${glow > 0.5 ? "3a" : "22"}`}}>
          <div style={{display: "flex", alignItems: "center", gap: 12, color: C.accentDeep, fontWeight: 700, fontSize: 25}}><Shield s={28} color={C.accentDeep} /> Guardián de inversión</div>
          <div style={{display: "flex", alignItems: "baseline", gap: 16, marginTop: 16, fontFamily: MONO}}>
            <span style={{fontSize: 36, color: C.muted, textDecoration: "line-through"}}>$78.000</span>
            <span style={{fontSize: 28, color: C.muted}}>→</span>
            <span style={{fontSize: 66, fontWeight: 700, color: C.ink}}>{fmt(count)}</span>
            <span style={{fontSize: 25, fontWeight: 700, color: C.ok}}>+15%</span>
            <span style={{fontSize: 23, color: C.accentDeep, background: `${C.accent}1a`, border: `1px solid ${C.accent}44`, padding: "4px 12px", borderRadius: 10}}>CLP</span>
          </div>
          <div style={{marginTop: 20, display: "flex", flexDirection: "column", gap: 13, fontSize: 27, color: C.ink}}>
            <div style={{display: "flex", alignItems: "center", gap: 12, opacity: row(48)}}><Check color={C.ok}/> Moneda CLP validada — sin error de 100×</div>
            <div style={{display: "flex", alignItems: "center", gap: 12, opacity: row(60)}}><Check color={C.ok}/> Escalamiento dentro del ≤20%</div>
            <div style={{display: "flex", alignItems: "center", gap: 12, opacity: row(72)}}><Check color={C.ok}/> Tracking sano · campaña activa</div>
          </div>
        </div>
      </BrowserFrame>
    </AbsoluteFill>
  );
};

// ── Escena 4: APROBAR + BITÁCORA ──────────────────────────────────────────────────
const Approve: React.FC = () => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const press = spring({frame: f - 16, fps, config: {damping: 90, stiffness: 200}});
  const scale = interpolate(press, [0, 0.5, 1], [1, 0.92, 1]);
  const ripple = interpolate(f, [16, 44], [0, 1], ease);
  const done = spring({frame: f - 42, fps, config: {damping: 120}});
  return (
    <AbsoluteFill style={{justifyContent: "center", alignItems: "center", gap: 38}}>
      <div style={{position: "relative", opacity: interpolate(f, [0, 12], [0, 1], ease)}}>
        <div style={{position: "absolute", inset: 0, borderRadius: 20, border: `3px solid ${C.accent}`, opacity: 1 - ripple, transform: `scale(${1 + ripple * 0.8})`}} />
        <div style={{transform: `scale(${scale})`, background: C.accent, color: "#fff", fontWeight: 700, fontSize: 38, padding: "26px 56px", borderRadius: 20, boxShadow: `0 24px 60px -28px ${C.accent}`}}>Aprobar y ejecutar</div>
      </div>
      <div style={{opacity: done, transform: `translateY(${interpolate(done, [0, 1], [16, 0])}px)`, display: "flex", alignItems: "center", gap: 14, fontSize: 30, color: C.ink, fontWeight: 600}}><Check s={26}/> Ejecutado · registrado en bitácora</div>
      <div style={{opacity: done, display: "flex", alignItems: "center", gap: 12, fontFamily: MONO, fontSize: 23, color: C.muted}}>
        <span style={{width: 12, height: 12, borderRadius: 99, background: C.accentDeep, boxShadow: `0 0 ${6 + 6 * Math.sin(f / 5)}px ${C.accentDeep}`}} />
        14:32 · America/Santiago · en tiempo real
      </div>
    </AbsoluteFill>
  );
};

// ── Escena 5: CIERRE ───────────────────────────────────────────────────────────────
const Outro: React.FC = () => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const s = spring({frame: f, fps, config: {damping: 120, stiffness: 130}});
  const sweep = interpolate(f, [10, 40], [-120, 120], ease);
  return (
    <AbsoluteFill style={{justifyContent: "center", alignItems: "center", textAlign: "center"}}>
      <div style={{display: "flex", alignItems: "center", justifyContent: "center", gap: 22, transform: `scale(${interpolate(s, [0, 1], [0.8, 1])})`, opacity: s}}>
        <LogoMark size={92} />
        <span style={{fontFamily: DISPLAY, fontSize: 96, fontWeight: 700, color: C.ink, letterSpacing: -1, position: "relative", overflow: "hidden"}}>
          ADVERTIQ
          <span style={{position: "absolute", top: 0, bottom: 0, left: `${sweep}%`, width: 60, background: "linear-gradient(90deg, transparent, #ffffffcc, transparent)", transform: "skewX(-18deg)"}} />
        </span>
      </div>
      <div style={{marginTop: 26, fontFamily: DISPLAY, fontSize: 48, color: C.accentDeep, opacity: interpolate(f, [14, 28], [0, 1], ease)}}>Pauta como un senior. Cuida la plata como un CFO.</div>
      <div style={{marginTop: 32, opacity: interpolate(f, [28, 44], [0, 1], ease), transform: `translateY(${interpolate(f, [28, 44], [14, 0], ease)}px)`, fontSize: 30, fontWeight: 700, color: "#fff", background: C.accent, display: "inline-block", padding: "16px 38px", borderRadius: 16, boxShadow: `0 20px 50px -22px ${C.accent}`}}>Agenda una demo</div>
    </AbsoluteFill>
  );
};

const Caption: React.FC<{text: string}> = ({text}) => {
  const f = useCurrentFrame();
  const o = interpolate(f, [2, 12], [0, 1], ease);
  return (
    <div style={{position: "absolute", bottom: 72, left: 0, right: 0, display: "flex", justifyContent: "center", opacity: o}}>
      <div style={{maxWidth: 1320, textAlign: "center", fontSize: 33, fontWeight: 600, color: C.ink, background: "rgba(255,255,255,0.86)", padding: "15px 30px", borderRadius: 16, border: `1px solid ${C.border}`, boxShadow: "0 14px 36px -20px rgba(31,26,46,0.4)", lineHeight: 1.3}}>{text}</div>
    </div>
  );
};

// ── timing derivado de la VO ────────────────────────────────────────────────────
const SCENE_COMPONENTS = [Hook, Connect, Guardian, Approve, Outro];
const bounds = SCENE_BOUNDS_SECONDS;
export const ADVERTIQ_HERO_DURATION = Math.round(SCENE_BOUNDS_SECONDS[SCENE_BOUNDS_SECONDS.length - 1] * ADVERTIQ_HERO_FPS);

export const AdvertiqHero: React.FC = () => {
  loadGoogleFont("Fraunces", "400;500;600;700");
  loadGoogleFont("Figtree", "400;500;600;700");
  loadGoogleFont("JetBrains Mono", "400;500;700");
  return (
    <Bg>
      <Audio src={staticFile("advertiq/vo.wav")} volume={1} />
      <AudioTrack src={staticFile("music/bg-music.mp3")} volume={0.42} fadeInDurationSeconds={1.2} fadeOutDurationSeconds={2.2} loop={false} />
      {SCENE_COMPONENTS.map((Comp, i) => {
        const fromF = Math.round(bounds[i] * ADVERTIQ_HERO_FPS);
        const toF = Math.round(bounds[i + 1] * ADVERTIQ_HERO_FPS);
        const overlap = i > 0 ? 8 : 0; // crossfade con la escena previa
        const from = fromF - overlap;
        const dur = toF - from;
        return (
          <Sequence key={i} from={from} durationInFrames={dur} name={`Escena ${i + 1}`}>
            <SceneWrap dur={dur}>
              <Comp />
              <Caption text={CAPTIONS[i]} />
            </SceneWrap>
          </Sequence>
        );
      })}
    </Bg>
  );
};
