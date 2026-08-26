import React from "react";
import {
  AbsoluteFill,
  Audio,
  Img,
  OffthreadVideo,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {ensureNuevaUrbeFonts, nuevaurbe as NU} from "../brand/nuevaurbe";

// ============================================================
// INMOBILIARIA NUEVA URBE — Reel "Facilidades de pago"
// Grilla SEPTIEMBRE 2026 · pieza del 25-09 · 1080×1920 · 30 fps · 18 s
// Brief (slide 7): T1 "Comprar tu casa en Calama no tiene por qué ser un
// dolor de cabeza" → T2 "aseguras tu hogar con el 10% de pie" → T3 "hasta
// en 120 cuotas, en pesos y 0% de interés" → T4 "Desde 4.818* UF" →
// T5 "Planifiquemos tu proyecto de vida" + CTA WhatsApp.
//
// Sistema de la marca (copiado de sus reels/stories, feedback 22-08):
//  · Montserrat en todo (nada de serif), azul royal #2050B4 + lima + blanco
//  · logo INU a color dentro de una caja blanca redondeada arriba-centro
//  · textos de apoyo entran con blur→nítido; titulares letra por letra
//    deslizando desde la derecha con desenfoque; cifras/píldoras hacen pop
//  · cierre: caja de logo grande + CTA, tercio inferior libre para el sticker
// ============================================================

export const NU_REEL_FPS = 30;
export const NU_REEL_DURATION = 540; // 18 s

const C = NU.colors;
const SANS = NU.fonts.display;

const T = {
  hook: [0, 80],
  pie: [80, 170],
  cuotas: [170, 275],
  precio: [275, 360],
  vida: [360, 445],
  cta: [445, 540],
} as const;

const clamp = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;

// ---------- animaciones del sistema ----------
const useSpring = (delay = 0, stiffness = 120, damping = 15) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  return spring({fps, frame: frame - delay, config: {stiffness, damping, mass: 0.8}});
};

// Texto de apoyo: aparece desenfocado y se enfoca (como "¡QUEDA UNA SEMANA PARA…")
const BlurIn: React.FC<{delay?: number; dur?: number; children: React.ReactNode; style?: React.CSSProperties}> = ({
  delay = 0,
  dur = 14,
  children,
  style,
}) => {
  const frame = useCurrentFrame();
  const p = interpolate(frame, [delay, delay + dur], [0, 1], clamp);
  return (
    <div style={{opacity: p, filter: `blur(${(1 - p) * 14}px)`, ...style}}>{children}</div>
  );
};

// Titular: cada letra entra deslizando desde la derecha con desenfoque de movimiento
const Letters: React.FC<{
  text: string;
  delay?: number;
  stagger?: number;
  style?: React.CSSProperties;
}> = ({text, delay = 0, stagger = 2, style}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  // Se parte por palabras (cada palabra es un bloque que no se corta) y dentro,
  // letra por letra con el retraso acumulado.
  const words = text.split(" ");
  let idx = 0;
  return (
    <div style={{display: "flex", flexWrap: "wrap", columnGap: "0.28em", ...style}}>
      {words.map((w, wi) => (
        <span key={wi} style={{display: "inline-flex", whiteSpace: "nowrap"}}>
          {Array.from(w).map((ch, ci) => {
            const i = idx++;
            const p = spring({fps, frame: frame - delay - i * stagger, config: {stiffness: 170, damping: 18, mass: 0.6}});
            const x = interpolate(p, [0, 1], [90, 0]);
            const blur = interpolate(p, [0, 0.7, 1], [10, 4, 0], clamp);
            return (
              <span
                key={ci}
                style={{
                  display: "inline-block",
                  opacity: p,
                  transform: `translateX(${x}px)`,
                  filter: `blur(${blur}px)`,
                }}
              >
                {ch}
              </span>
            );
          })}
        </span>
      ))}
    </div>
  );
};

// Pop elástico (cifras, píldoras, logos)
const Pop: React.FC<{delay?: number; children: React.ReactNode; style?: React.CSSProperties; from?: number}> = ({
  delay = 0,
  children,
  style,
  from = 0.6,
}) => {
  const p = useSpring(delay, 150, 13);
  return (
    <div style={{opacity: interpolate(p, [0, 0.3], [0, 1], clamp), transform: `scale(${interpolate(p, [0, 1], [from, 1])})`, ...style}}>
      {children}
    </div>
  );
};

const useExit = (sceneLen: number) => {
  const frame = useCurrentFrame();
  return interpolate(frame, [sceneLen - 8, sceneLen], [1, 0], clamp);
};

// Clip real (vertical, ya tonemapeado) con zoom lento y velo azul
const Clip: React.FC<{src: string; from?: number; zoom?: [number, number]; darken?: number; mirror?: boolean}> = ({
  src,
  from = 0,
  zoom = [1, 1.08],
  darken = 0.5,
  mirror = false,
}) => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  const s = interpolate(frame, [0, durationInFrames], zoom, clamp);
  return (
    <AbsoluteFill style={{overflow: "hidden", background: C.blue}}>
      <AbsoluteFill style={{transform: `scale(${s}) ${mirror ? "scaleX(-1)" : ""}`, transformOrigin: "50% 60%"}}>
        <OffthreadVideo
          src={staticFile(src)}
          startFrom={Math.round(from * NU_REEL_FPS)}
          muted
          style={{width: "100%", height: "100%", objectFit: "cover"}}
        />
      </AbsoluteFill>
      <AbsoluteFill
        style={{
          background: `linear-gradient(180deg, rgba(32,80,180,${darken * 0.75}) 0%, rgba(32,80,180,${darken * 0.3}) 22%, rgba(20,55,140,${darken * 0.85}) 52%, rgba(12,35,110,${Math.min(1, darken + 0.35)}) 100%)`,
        }}
      />
    </AbsoluteFill>
  );
};

// Logo INU a color en caja blanca arriba-centro (igual que sus piezas)
const LogoBox: React.FC<{width?: number; top?: number; delay?: number}> = ({width = 190, top = 84, delay = 0}) => (
  <Pop delay={delay} from={0.8} style={{position: "absolute", top, left: 0, right: 0, display: "flex", justifyContent: "center"}}>
    <div style={{background: C.paper, borderRadius: 18, padding: "16px 26px", boxShadow: "0 10px 30px rgba(0,0,0,0.18)"}}>
      <Img src={staticFile(NU.logos.inu)} style={{width, display: "block"}} />
    </div>
  </Pop>
);

const Pill: React.FC<{children: React.ReactNode; bg?: string; color?: string; size?: number; style?: React.CSSProperties}> = ({
  children,
  bg = C.lime,
  color = C.blue,
  size = 42,
  style,
}) => (
  <span
    style={{
      display: "inline-block",
      background: bg,
      color,
      fontFamily: SANS,
      fontWeight: 800,
      fontSize: size,
      lineHeight: 1.1,
      padding: "12px 28px",
      borderRadius: 999,
      ...style,
    }}
  >
    {children}
  </span>
);

const H = (size: number, weight = 800, extra: React.CSSProperties = {}): React.CSSProperties => ({
  fontFamily: SANS,
  fontWeight: weight,
  fontSize: size,
  lineHeight: 1.05,
  letterSpacing: -size * 0.02,
  color: C.paper,
  ...extra,
});

// ---------- Escena 1 · Hook ----------
const SceneHook: React.FC = () => {
  const out = useExit(T.hook[1] - T.hook[0]);
  return (
    <AbsoluteFill style={{opacity: out}}>
      <Clip src="assets/nuevaurbe/clip_patio.mp4" from={0.2} zoom={[1.04, 1.12]} darken={0.6} />
      <LogoBox />
      <div style={{position: "absolute", left: 80, right: 80, top: 760, textShadow: "0 6px 30px rgba(10,30,100,0.7)"}}>
        <BlurIn delay={2}>
          <div style={H(50, 600)}>Comprar tu casa en Calama</div>
        </BlurIn>
        <BlurIn delay={10}>
          <div style={H(50, 600, {marginTop: 6})}>no tiene por qué ser un</div>
        </BlurIn>
        <Letters text="DOLOR DE" delay={18} style={H(126, 900, {color: C.lime, marginTop: 22, letterSpacing: -3})} />
        <Letters text="CABEZA." delay={30} style={H(126, 900, {color: C.lime, letterSpacing: -3})} />
      </div>
    </AbsoluteFill>
  );
};

// ---------- Escena 2 · 10% de pie ----------
const ScenePie: React.FC = () => {
  const out = useExit(T.pie[1] - T.pie[0]);
  const big = useSpring(8, 110, 13);
  const pct = useSpring(20, 140, 13);
  return (
    <AbsoluteFill style={{opacity: out, background: C.blue}}>
      <LogoBox />
      <div style={{position: "absolute", left: 80, right: 80, top: 520}}>
        <BlurIn delay={0}>
          <div style={H(44, 600)}>Aquí el camino es simple:</div>
        </BlurIn>
        <div style={{display: "flex", alignItems: "flex-end", marginTop: 20, height: 330}}>
          <div
            style={{
              ...H(400, 900, {color: C.lime, lineHeight: 0.82, letterSpacing: -20}),
              transform: `translateY(${interpolate(big, [0, 1], [160, 0])}px)`,
              opacity: big,
              filter: `blur(${interpolate(big, [0, 1], [12, 0])}px)`,
            }}
          >
            10
          </div>
          <div
            style={{
              ...H(170, 900, {lineHeight: 0.82, marginLeft: 14, marginBottom: 10}),
              transform: `scale(${interpolate(pct, [0, 1], [0.3, 1])})`,
              transformOrigin: "0% 100%",
              opacity: pct,
            }}
          >
            %
          </div>
        </div>
        <Letters text="DE PIE" delay={28} style={H(96, 900, {marginTop: 24})} />
        <BlurIn delay={40}>
          <div style={H(44, 500, {marginTop: 24, lineHeight: 1.25})}>
            y aseguras tu hogar en <b style={{fontWeight: 800}}>Travesía del Desierto II</b>.
          </div>
        </BlurIn>
      </div>
      <Pop delay={50} style={{position: "absolute", left: 0, right: 0, bottom: 150, display: "flex", justifyContent: "center"}}>
        <Img src={staticFile(NU.logos.travesiaWhite)} style={{width: 230, opacity: 0.95}} />
      </Pop>
    </AbsoluteFill>
  );
};

// ---------- Escena 3 · 120 cuotas ----------
const SceneCuotas: React.FC = () => {
  const frame = useCurrentFrame();
  const out = useExit(T.cuotas[1] - T.cuotas[0]);
  const n = Math.round(interpolate(frame, [8, 40], [0, 120], clamp));
  const pop = useSpring(6, 110, 13);
  return (
    <AbsoluteFill style={{opacity: out}}>
      <Clip src="assets/nuevaurbe/clip_dormitorio.mp4" from={0.6} zoom={[1.06, 1.0]} darken={0.5} />
      <LogoBox />
      <div style={{position: "absolute", left: 80, right: 80, top: 540, textShadow: "0 6px 28px rgba(10,30,100,0.6)"}}>
        <BlurIn delay={0}>
          <div style={H(44, 600)}>Y lo pagas a tu ritmo:</div>
        </BlurIn>
        <div
          style={{
            ...H(320, 900, {lineHeight: 0.9, letterSpacing: -14, marginTop: 10}),
            opacity: pop,
            transform: `scale(${interpolate(pop, [0, 1], [0.8, 1])})`,
            transformOrigin: "0% 50%",
          }}
        >
          {n}
        </div>
        <Letters text="CUOTAS" delay={26} style={H(96, 900)} />
        <div style={{display: "flex", gap: 16, flexWrap: "wrap", marginTop: 34}}>
          <Pop delay={40}>
            <Pill>en pesos</Pill>
          </Pop>
          <Pop delay={46}>
            <Pill bg={C.paper} color={C.blue}>
              0% de interés
            </Pill>
          </Pop>
        </div>
        <BlurIn delay={54}>
          <div style={H(38, 500, {marginTop: 30, opacity: 0.9})}>Para el pie. Sin vueltas, sin sorpresas.</div>
        </BlurIn>
      </div>
    </AbsoluteFill>
  );
};

// ---------- Escena 4 · Precio / ficha ----------
const ScenePrecio: React.FC = () => {
  const out = useExit(T.precio[1] - T.precio[0]);
  const card = useSpring(4, 110, 14);
  return (
    <AbsoluteFill style={{opacity: out, background: C.blue}}>
      <LogoBox />
      <div
        style={{
          position: "absolute",
          left: 80,
          right: 80,
          top: 520,
          background: C.paper,
          borderRadius: 34,
          padding: "56px 60px 50px",
          boxShadow: "0 30px 80px rgba(0,0,0,0.25)",
          opacity: card,
          transform: `translateY(${interpolate(card, [0, 1], [110, 0])}px) scale(${interpolate(card, [0, 1], [0.94, 1])})`,
          color: C.blue,
        }}
      >
        <Pop delay={12} from={0.7} style={{display: "inline-block"}}>
          <Img src={staticFile(NU.logos.travesia)} style={{width: 190, display: "block"}} />
        </Pop>
        <BlurIn delay={16}>
          <div style={H(38, 600, {color: C.blueDeep, marginTop: 34, opacity: 0.85})}>Espacios reales, hechos a tu medida</div>
        </BlurIn>
        <div style={{display: "flex", alignItems: "baseline", gap: 18, marginTop: 10}}>
          <BlurIn delay={22}>
            <span style={H(42, 700, {color: C.blue})}>Desde</span>
          </BlurIn>
          <Letters text="UF 4.818*" delay={24} stagger={3} style={H(140, 900, {color: C.blue, letterSpacing: -6})} />
        </div>
        <div style={{display: "flex", gap: 14, marginTop: 30, flexWrap: "wrap"}}>
          {[
            ["3 dorms", C.blue, C.paper],
            ["3 baños", C.blue, C.paper],
            ["desde 79,79 m²", C.lime, C.blue],
          ].map(([t, bg, col], i) => (
            <Pop key={t} delay={40 + i * 5}>
              <Pill size={36} bg={bg} color={col}>
                {t}
              </Pill>
            </Pop>
          ))}
        </div>
        <BlurIn delay={56}>
          <div style={H(28, 500, {color: C.blueDeep, marginTop: 34, opacity: 0.6, letterSpacing: 0})}>
            *Descuentos aplicados · Calama, Av. Circunvalación 1436
          </div>
        </BlurIn>
      </div>
    </AbsoluteFill>
  );
};

// ---------- Escena 5 · Proyecto de vida ----------
const SceneVida: React.FC = () => {
  const out = useExit(T.vida[1] - T.vida[0]);
  return (
    <AbsoluteFill style={{opacity: out}}>
      <Clip src="assets/nuevaurbe/clip_patio.mp4" from={1.8} zoom={[1.0, 1.1]} darken={0.65} mirror />
      <LogoBox />
      <div style={{position: "absolute", left: 80, right: 80, top: 800, textShadow: "0 6px 30px rgba(10,30,100,0.75)"}}>
        <BlurIn delay={2}>
          <div style={H(50, 600)}>Planifiquemos</div>
        </BlurIn>
        <Letters text="TU PROYECTO" delay={12} style={H(118, 900, {color: C.lime, marginTop: 14, letterSpacing: -3})} />
        <Letters text="DE VIDA." delay={26} style={H(118, 900, {color: C.lime, letterSpacing: -3})} />
        <BlurIn delay={40}>
          <div style={H(40, 500, {marginTop: 36, lineHeight: 1.3})}>
            Casa piloto en Calama.
            <br />
            Atención personalizada con cita previa.
          </div>
        </BlurIn>
      </div>
    </AbsoluteFill>
  );
};

// ---------- Escena 6 · Cierre (como sus reels: caja de logo + CTA en lima) ----------
const SceneCTA: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const pulse = 1 + 0.02 * Math.sin((frame / fps) * Math.PI * 2 * 0.8);
  return (
    <AbsoluteFill style={{background: C.blue}}>
      <LogoBox width={380} top={330} delay={0} />
      <div style={{position: "absolute", left: 80, right: 80, top: 720, textAlign: "center"}}>
        <BlurIn delay={10}>
          <div style={H(40, 600)}>¿Listo para el siguiente paso?</div>
        </BlurIn>
        <Letters
          text="CONVERSEMOS POR WHATSAPP"
          delay={16}
          stagger={1}
          style={H(60, 900, {justifyContent: "center", marginTop: 18, letterSpacing: -1})}
        />
        <Pop delay={44}>
          <div
            style={{
              display: "inline-block",
              marginTop: 36,
              background: C.lime,
              color: C.blue,
              fontFamily: SANS,
              fontSize: 64,
              fontWeight: 900,
              padding: "22px 54px",
              borderRadius: 999,
              letterSpacing: -1,
              transform: `scale(${pulse})`,
            }}
          >
            {NU.whatsapp}
          </div>
        </Pop>
        <BlurIn delay={58}>
          <div style={H(34, 500, {marginTop: 30, opacity: 0.9, letterSpacing: 0})}>Agenda tu visita · ingreso con cita previa</div>
        </BlurIn>
      </div>
      {/* Tercio inferior (y ≳ 1250) libre: ahí va el sticker de enlace de Instagram */}
      <BlurIn delay={64} style={{position: "absolute", bottom: 90, left: 0, right: 0, textAlign: "center"}}>
        <div style={H(34, 800, {color: C.lime, letterSpacing: 2})}>INU.CL</div>
      </BlurIn>
    </AbsoluteFill>
  );
};

// ---------- Composición ----------
export const NuevaUrbeFacilidadesReel: React.FC = () => {
  ensureNuevaUrbeFonts();
  const frame = useCurrentFrame();
  const musicVol = interpolate(frame, [0, 12, NU_REEL_DURATION - 45, NU_REEL_DURATION], [0, 0.7, 0.7, 0], clamp);
  return (
    <AbsoluteFill style={{background: C.blue}}>
      <Audio src={staticFile("assets/nuevaurbe/musica_mixkit32.mp3")} volume={musicVol} />
      <Sequence from={T.hook[0]} durationInFrames={T.hook[1] - T.hook[0]}>
        <SceneHook />
      </Sequence>
      <Sequence from={T.pie[0]} durationInFrames={T.pie[1] - T.pie[0]}>
        <ScenePie />
      </Sequence>
      <Sequence from={T.cuotas[0]} durationInFrames={T.cuotas[1] - T.cuotas[0]}>
        <SceneCuotas />
      </Sequence>
      <Sequence from={T.precio[0]} durationInFrames={T.precio[1] - T.precio[0]}>
        <ScenePrecio />
      </Sequence>
      <Sequence from={T.vida[0]} durationInFrames={T.vida[1] - T.vida[0]}>
        <SceneVida />
      </Sequence>
      <Sequence from={T.cta[0]} durationInFrames={T.cta[1] - T.cta[0]}>
        <SceneCTA />
      </Sequence>
    </AbsoluteFill>
  );
};
