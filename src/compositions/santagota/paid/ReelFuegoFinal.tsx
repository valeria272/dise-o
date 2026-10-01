/**
 * SANTA GOTA · R2 de pauta «FUEGO Y FINAL» — reel 9:16 (1080×1920 · 24 fps · 15,6 s). 01-10-2026.
 *
 * Etapa «entender»: un solo aceite para todo es pecado; uno es para el fuego (750) y otro para el final (500).
 * Material 100 % real de la jornada del 10-09 (tramos: scripts/santagota-r2-tramos.sh). Sin IA.
 * Audio: la mezcla del spot aprobado de Diego (public/assets/santagota/reel-v2/audio-v2.wav), 112,5 BPM:
 * cada corte cae en un pulso (12,84 cuadros). Cortes secos (R-11). Sin estrellitas (R-26).
 * Texto dentro de la zona segura de Reels: entre y 250 y y 1580, ≥ 115 px del borde derecho.
 * Precio del Pack Squeeze leído de santagota.cl el 01-10-2026.
 */
import React from "react";
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";
import {LIMA, Precio, brush, mano} from "./CarruselPecado";

export const DUR_R2 = 374;
const T = (f: string) => staticFile(`assets/santagota/r2/${f}.mp4`);

/** Un tramo de video a pantalla completa. */
const Tramo: React.FC<{src: string; desde: number; hasta: number}> = ({src, desde, hasta}) => (
  <Sequence from={desde} durationInFrames={hasta - desde}>
    <OffthreadVideo src={T(src)} muted style={{width: 1080, height: 1920, objectFit: "cover"}} />
  </Sequence>
);

/** Texto de plumón que entra de golpe en el pulso (escala con rebote) y sale con el corte. */
const Golpe: React.FC<{desde: number; hasta: number; x: number; y: number; lineas: {t: string; c: string; s: number}[]; rot?: number; sub?: string}> = ({desde, hasta, x, y, lineas, rot = -5, sub}) => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  if (f < desde || f >= hasta) return null;
  const k = spring({frame: f - desde, fps, config: {damping: 11, stiffness: 220, mass: 0.6}});
  const subK = interpolate(f, [desde + 4, desde + 8], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <div style={{position: "absolute", left: x, top: y, transform: `rotate(${rot}deg) scale(${0.55 + 0.45 * k})`, transformOrigin: "0% 50%"}}>
      {lineas.map((l, i) => (
        <div key={i} style={{...brush, fontSize: l.s, color: l.c, textShadow: "0 5px 22px rgba(20,0,5,0.55)"}}>{l.t}</div>
      ))}
      {sub && <div style={{...mano, fontSize: 44, color: "#fff", marginTop: 14, opacity: subK, textShadow: "0 3px 14px rgba(20,0,5,0.7)", whiteSpace: "nowrap"}}>{sub}</div>}
    </div>
  );
};

/** Golpe de palabra en el cierre: entra grande y desenfocada, aterriza en el pulso con un leve temblor. */
const Slam: React.FC<{f: number; desde: number; children: React.ReactNode; style: React.CSSProperties}> = ({f, desde, children, style}) => {
  const {fps} = useVideoConfig();
  if (f < desde) return null;
  const k = spring({frame: f - desde, fps, config: {damping: 12, stiffness: 260, mass: 0.5}});
  const temblor = f - desde < 5 ? Math.sin((f - desde) * 2.4) * (5 - (f - desde)) * 2.2 : 0;
  return (
    <div style={{...style, transform: `${style.transform ?? ""} translate(${temblor}px, ${-temblor * 0.6}px) scale(${2.1 - 1.1 * k})`, opacity: Math.min(1, k * 2.5), filter: `blur(${(1 - k) * 10}px)`}}>
      {children}
    </div>
  );
};

/** Cierre de compra (v2, 01-10: el anterior «quedó plano, fome»): corte seco a Cami gritando con el 500,
 *  COMPRA → EN → SANTAGOTA.CL cada uno en un pulso, plumón que se dibuja, precio de los dos, y la imagen late
 *  en cada golpe hasta el final. Pulsos (desde el cuadro 259): 0 · 13 · 26 · 39 · 51 · 64 · 77 · 90 · 103. */
const PULSOS = [0, 13, 26, 39, 51, 64, 77, 90, 103];
const Cierre: React.FC = () => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  const ultimo = Math.max(...PULSOS.filter((p) => p <= f));
  const late = 1 + 0.03 * Math.exp(-(f - ultimo) / 3);
  const flash = interpolate(f, [0, 2], [0.85, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const trazo = interpolate(f, [30, 38], [0, 100], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const pPrecio = spring({frame: f - 39, fps, config: {damping: 10, stiffness: 220}});
  return (
    <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
      <Img src={staticFile("assets/santagota/r2/cierre-cami.jpg")} style={{position: "absolute", inset: 0, width: 1080, height: 1920, transform: `scale(${late * interpolate(f, [0, 115], [1.04, 1.1])})`}} />
      <AbsoluteFill style={{background: "linear-gradient(180deg, rgba(25,0,8,0.38) 0%, rgba(25,0,8,0) 30%, rgba(25,0,8,0) 66%, rgba(25,0,8,0.5) 100%)"}} />

      <Slam f={f} desde={0} style={{position: "absolute", left: 70, top: 270, transformOrigin: "20% 50%", transform: "rotate(-6deg)"}}>
        <div style={{...brush, fontSize: 250, color: "#fff", textShadow: "0 6px 26px rgba(20,0,5,0.5)"}}>COMPRA</div>
      </Slam>
      <Slam f={f} desde={13} style={{position: "absolute", left: 96, top: 470, transformOrigin: "20% 50%", transform: "rotate(-6deg)"}}>
        <div style={{...brush, fontSize: 170, color: "#fff", textShadow: "0 6px 26px rgba(20,0,5,0.5)"}}>EN</div>
      </Slam>
      <Slam f={f} desde={26} style={{position: "absolute", left: 80, top: 1390, transformOrigin: "30% 50%", transform: "rotate(-4deg)"}}>
        <div style={{...brush, fontSize: 152, color: LIMA, textShadow: "0 6px 26px rgba(20,0,5,0.6)"}}>SANTAGOTA.CL</div>
      </Slam>
      <svg style={{position: "absolute", left: 90, top: 1528, overflow: "visible", transform: "rotate(-4deg)", clipPath: `inset(-20% ${100 - trazo}% -20% -5%)`}} width={840} height={40}>
        <path d="M4 24 C 250 10, 500 32, 836 12" stroke={LIMA} strokeWidth={16} strokeLinecap="round" fill="none" />
        <path d="M90 32 C 330 24, 520 36, 700 26" stroke={LIMA} strokeWidth={7} strokeLinecap="round" fill="none" opacity={0.85} />
      </svg>

      <div style={{position: "absolute", inset: 0, transform: `scale(${pPrecio})`, transformOrigin: "890px 620px"}}>
        <Precio x={770} y={500} d={240} arriba="los dos" precio="$18.990" rot={9} />
      </div>
      <AbsoluteFill style={{backgroundColor: "#fff", opacity: flash}} />
    </AbsoluteFill>
  );
};

export const ReelFuegoFinal: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: "#000"}}>
    {/* imagen — cada corte en un pulso */}
    <Tramo src="01-boquilla" desde={0} hasta={53} />
    <Tramo src="02-este750" desde={53} hasta={79} />
    <Tramo src="03-fuego-mano" desde={79} hasta={104} />
    <Tramo src="04-fuego-cenital" desde={104} hasta={130} />
    <Tramo src="05-final-bowl" desde={130} hasta={207} />
    <Tramo src="06-remate" desde={207} hasta={259} />
    <Sequence from={259}>
      <Cierre />
    </Sequence>

    {/* texto */}
    <Golpe desde={2} hasta={27} x={90} y={1150} lineas={[{t: "¿UN SOLO ACEITE", c: "#fff", s: 118}, {t: "PARA TODO?", c: "#fff", s: 118}]} />
    <Golpe desde={27} hasta={53} x={120} y={1160} rot={-7} lineas={[{t: "PECADO.", c: LIMA, s: 230}]} />
    <Golpe desde={53} hasta={79} x={110} y={1250} lineas={[{t: "ESTE,", c: "#fff", s: 150}]} />
    <Golpe desde={79} hasta={130} x={90} y={1230} lineas={[{t: "PARA EL", c: "#fff", s: 90}, {t: "FUEGO.", c: LIMA, s: 190}]} sub="cocinar · saltear · dorar" />
    <Golpe desde={130} hasta={156} x={110} y={1080} lineas={[{t: "Y ESTE,", c: "#fff", s: 150}]} />
    <Golpe desde={156} hasta={207} x={90} y={1020} lineas={[{t: "PARA EL", c: "#fff", s: 90}, {t: "FINAL.", c: LIMA, s: 190}]} sub="aderezar · terminar · chorrear" />
    <Golpe desde={228} hasta={259} x={120} y={1200} rot={-6} lineas={[{t: "LOS DOS.", c: LIMA, s: 200}]} />

    {/* audio: la mezcla del spot aprobado, con salida suave */}
    <Audio
      src={staticFile("assets/santagota/reel-v2/audio-v2.wav")}
      volume={(f) => 0.8 * interpolate(f, [DUR_R2 - 34, DUR_R2 - 1], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})}
    />
  </AbsoluteFill>
);
