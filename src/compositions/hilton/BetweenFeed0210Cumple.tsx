/**
 * BETWEEN · FEED 02-10 · REEL «CAFÉ DE CUMPLEAÑOS»
 *
 * Grilla BW OCT, FEED col F (S1). Comentario de diseño: «Más simple, siento que
 * con todo ese movimiento se verá muy IA, que lo animado finalmente sea la
 * información». Eli, 29-09: foto QUIETA hiperrealista (al cliente le incomoda lo
 * que se nota IA), sólo el texto anima, juvenil y sutil, tipo máquina de escribir;
 * 1.er texto 2,5 s, el resto 3–4 s según la carga; márgenes de PAID.
 *
 * Refs de animación (pins de Eli, `raw/hilton/between/oct/refs/f02-cumple/pins`):
 * la frase del hook se arma por palabras mezclando tres voces (palo grueso con
 * «pop», una palabra manuscrita que se escribe, mayúsculas finas espaciadas);
 * máquina de escribir letra a letra; el titular pasa DETRÁS del objeto.
 * Traducido a Between: sólo Raleway + Brushwell (máx. 2 familias), beige de marca
 * con la sombra café del sistema, garabatos de línea como los globos de la ST 07-10.
 *
 * La foto: `gen-f02-10-f` (vaso To Go vigente, vela encendida, sin caras). La
 * figura recortada (`f-cumple-figura.png`) va ENCIMA del titular del hook: la
 * vela cruza por delante de «CUMPLEAÑOS?».
 * ⛔ Hilton: sin punto final en títulos ni bajadas (el legal sí lo lleva).
 * Zona segura Reels: 250 px arriba, 340 abajo, 115 a la derecha, 60 a la izquierda.
 * Render: `scripts/reel-por-chrome.mjs` (remotion.exe bloqueado) + audio en
 * `scripts/bw-fd-02-10-cumple-audio.py`.
 */
import React from 'react';
import {AbsoluteFill, Easing, Img, interpolate, spring, staticFile, useCurrentFrame} from 'remotion';
import {BETWEEN} from '../../brand/hilton-between';
import {useFuentesListas} from './BetweenSistema';

const C = BETWEEN.colores;
const SANS = BETWEEN.fuentes.sans;
const SCRIPT = BETWEEN.fuentes.script;
const SOMBRA = '0 2px 16px rgba(36,26,18,0.55)';
const X0 = 76; // margen izquierdo (zona segura 60 + respiro)

/** Escenas: [inicio, fin) en fotogramas a 30 fps */
export const ESCENAS_CUMPLE = {
  hook: [0, 75], // 2,5 s
  cafe: [75, 165], // 3 s
  ven: [165, 400], // (sin salida: queda quieto hasta el final) 3 s + 4 s con el legal al lado (el cierre junta toda la info)
} as const;
export const DURACION_CUMPLE = 375;

/** Cada golpe de tecla, para que el audio caiga en el mismo fotograma. */
export const TECLEO = (texto: string, desde: number, porLetra: number) =>
  [...texto].map((ch, i) => (ch === ' ' ? -1 : desde + i * porLetra)).filter((f) => f >= 0);

/* ───────── piezas de animación ───────── */

/** Máquina de escribir: las letras que faltan ocupan su lugar (la línea no baila). */
const Maquina: React.FC<{texto: string; desde: number; porLetra: number; style: React.CSSProperties}> = ({
  texto, desde, porLetra, style,
}) => {
  const f = useCurrentFrame();
  const n = Math.max(0, Math.min(texto.length, Math.floor((f - desde) / porLetra) + 1));
  return (
    <div style={{whiteSpace: 'pre', ...style}}>
      {[...texto].map((ch, i) => {
        const aparece = desde + i * porLetra;
        const t = interpolate(f, [aparece, aparece + 3], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
        return (
          <span key={i} style={{opacity: i < n ? t : 0, display: 'inline-block', transform: `translateY(${(1 - t) * 6}px)`}}>
            {ch === ' ' ? ' ' : ch}
          </span>
        );
      })}
    </div>
  );
};

/** Manuscrita que se escribe: se destapa de izquierda a derecha con un borde suave. */
const Trazo: React.FC<{texto: string; desde: number; dura: number; style: React.CSSProperties}> = ({
  texto, desde, dura, style,
}) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [desde, desde + dura], [0, 1], {
    extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.inOut(Easing.cubic),
  });
  const borde = p * 118 - 8; // % hasta donde se ve, con 8 % de degradé
  return (
    <div
      style={{
        whiteSpace: 'pre',
        WebkitMaskImage: `linear-gradient(90deg, #000 ${borde}%, transparent ${borde + 8}%)`,
        maskImage: `linear-gradient(90deg, #000 ${borde}%, transparent ${borde + 8}%)`,
        padding: '0 0.25em 0.15em 0.1em', // que la máscara no corte las colas de Brushwell
        ...style,
      }}
    >
      {texto}
    </div>
  );
};

/** Entra de golpe con un rebote corto (el «pop» del hook). */
const Pop: React.FC<{desde: number; children: React.ReactNode; origen?: string}> = ({desde, children, origen = 'left bottom'}) => {
  const f = useCurrentFrame();
  const s = spring({frame: f - desde, fps: 30, config: {damping: 11, stiffness: 180, mass: 0.6}});
  return (
    <div style={{opacity: f < desde ? 0 : Math.min(1, s * 1.6), transform: `scale(${0.55 + 0.45 * s})`, transformOrigin: origen}}>
      {children}
    </div>
  );
};

/** Salida común de cada escena: sube un poco, se desenfoca y se va. */
const Escena: React.FC<{rango: readonly [number, number]; children: React.ReactNode; salida?: number}> = ({
  rango, children, salida = 8,
}) => {
  const f = useCurrentFrame();
  const [a, b] = rango;
  if (f < a || f >= b) return null;
  const t = interpolate(f, [b - salida, b], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{opacity: 1 - t, transform: `translateY(${-18 * t}px)`, filter: t > 0 ? `blur(${6 * t}px)` : undefined}}>
      {children}
    </AbsoluteFill>
  );
};

/** Destellos de línea alrededor de la llama, dibujados a mano (como los globos de la ST 07-10). */
const LLAMA = {x: 556, y: 790};
const Destellos: React.FC<{desde: number}> = ({desde}) => {
  const f = useCurrentFrame();
  const rayos = [
    {a: -150, r0: 78, r1: 128},
    {a: -118, r0: 92, r1: 150},
    {a: -62, r0: 92, r1: 150},
    {a: -30, r0: 78, r1: 128},
  ];
  const brillo = 0.85 + 0.15 * Math.sin((f - desde) / 5);
  return (
    <svg width={1080} height={1920} style={{position: 'absolute', inset: 0, opacity: brillo}}>
      {rayos.map((r, i) => {
        const t = interpolate(f, [desde + i * 3, desde + i * 3 + 9], [0, 1], {
          extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic),
        });
        const rad = (r.a * Math.PI) / 180;
        const x0 = LLAMA.x + Math.cos(rad) * r.r0, y0 = LLAMA.y + Math.sin(rad) * r.r0;
        const x1 = LLAMA.x + Math.cos(rad) * r.r1, y1 = LLAMA.y + Math.sin(rad) * r.r1;
        const largo = Math.hypot(x1 - x0, y1 - y0);
        return (
          <line key={i} x1={x0} y1={y0} x2={x1} y2={y1} stroke={C.beige} strokeWidth={5} strokeLinecap="round"
            strokeDasharray={largo} strokeDashoffset={largo * (1 - t)} />
        );
      })}
      {/* dos estrellitas de cuatro puntas */}
      {[{x: 676, y: 742, s: 20, d: 14}].map((e, i) => {
        const t = spring({frame: f - desde - e.d, fps: 30, config: {damping: 9, stiffness: 160}});
        const p = `M ${e.x} ${e.y - e.s} Q ${e.x} ${e.y} ${e.x + e.s} ${e.y} Q ${e.x} ${e.y} ${e.x} ${e.y + e.s} Q ${e.x} ${e.y} ${e.x - e.s} ${e.y} Q ${e.x} ${e.y} ${e.x} ${e.y - e.s} Z`;
        return <path key={i} d={p} fill={C.beige} opacity={f < desde + e.d ? 0 : 1}
          transform={`translate(${e.x} ${e.y}) scale(${t}) translate(${-e.x} ${-e.y})`} />;
      })}
    </svg>
  );
};

/* ───────── estilos ───────── */

const palo = (size: number, peso = 900, extra: React.CSSProperties = {}): React.CSSProperties => ({
  fontFamily: SANS, fontWeight: peso, fontSize: size, lineHeight: 0.95, color: C.beige,
  textShadow: SOMBRA, letterSpacing: '-0.01em', ...extra,
});
const fino = (size: number): React.CSSProperties => ({
  fontFamily: SANS, fontWeight: 400, fontSize: size, lineHeight: 1, color: C.beige,
  textShadow: SOMBRA, letterSpacing: '0.34em',
});
const mano = (size: number): React.CSSProperties => ({
  fontFamily: SCRIPT, fontSize: size, lineHeight: 1, color: C.beige, textShadow: SOMBRA,
});

/* ───────── textos (literales de la grilla, sin punto final) ───────── */
export const TXT = {
  estas: '¿ESTÁS',
  de: 'de',
  cumple: 'CUMPLEAÑOS?',
  elCafe: 'EL CAFÉ',
  vaPor: 'va por',
  cuenta: 'NUESTRA CUENTA',
  ven1: 'Ven por tu',
  cafeGratis: 'café gratis',
  ven2: 'el día de tu cumpleaños',
  legal:
    'Beneficio válido únicamente de lunes a viernes, el mismo día de tu cumpleaños, ' +
    'presentando carnet de identidad al momento de solicitarlo.',
};
/** Tiempos de cada golpe (los usa también el script de audio). */
export const TIEMPOS = {
  estasPop: 2,
  deTrazo: [12, 12] as const,
  cumple: [22, 2.6] as const,
  destellos: 136,
  elCafe: [80, 2.4] as const,
  vaPor: [98, 14] as const,
  cuenta: [112, 2.2] as const,
  ven1: [170, 2.2] as const,
  cafeGratis: [194, 14] as const,
  ven2: [210, 1.3] as const,
  legal: 256,
};

export const FeedOct02Cumple: React.FC = () => {
  useFuentesListas();
  const f = useCurrentFrame();
  const T = TIEMPOS;
  // el legal entra por líneas, sin máquina: es largo y tiene que leerse en paz
  const lineasLegal = [
    'Beneficio válido únicamente',
    'de lunes a viernes, el mismo',
    'día de tu cumpleaños,',
    'presentando carnet de',
    'identidad al momento',
    'de solicitarlo.',
  ];
  return (
    <AbsoluteFill style={{backgroundColor: C.sombra}}>
      <Img src={staticFile('assets/hilton/between/oct/f-cumple-reel.jpg')}
        style={{position: 'absolute', width: 1080, height: 1920, objectFit: 'cover'}} />
      {/* velo café arriba, sólo donde vive el texto */}
      <AbsoluteFill style={{background: 'linear-gradient(180deg, rgba(36,26,18,0.62) 0%, rgba(36,26,18,0.38) 30%, rgba(36,26,18,0) 50%)'}} />

      {/* ── 1 · HOOK (detrás de la figura) ── */}
      <Escena rango={ESCENAS_CUMPLE.hook}>
        <div style={{position: 'absolute', left: X0, top: 440, display: 'flex', alignItems: 'flex-end', gap: 18}}>
          <Pop desde={T.estasPop}><div style={palo(176)}>{TXT.estas}</div></Pop>
          <Trazo texto={TXT.de} desde={T.deTrazo[0]} dura={T.deTrazo[1]} style={{...mano(150), marginBottom: -34}} />
        </div>
        <Maquina texto={TXT.cumple} desde={T.cumple[0]} porLetra={T.cumple[1]}
          style={{...palo(134), position: 'absolute', left: X0 - 4, top: 700}} />
      </Escena>

      {/* la figura recortada tapa el titular: la vela pasa por delante */}
      <Img src={staticFile('assets/hilton/between/oct/f-cumple-figura.png')}
        style={{position: 'absolute', width: 1080, height: 1920}} />

      {f >= T.destellos && f < DURACION_CUMPLE && <Destellos desde={T.destellos} />}

      {/* ── 2 · EL CAFÉ VA POR NUESTRA CUENTA ── */}
      <Escena rango={ESCENAS_CUMPLE.cafe}>
        <div style={{position: 'absolute', left: X0, top: 340}}>
          <Maquina texto={TXT.elCafe} desde={T.elCafe[0]} porLetra={T.elCafe[1]} style={fino(58)} />
          <Trazo texto={TXT.vaPor} desde={T.vaPor[0]} dura={T.vaPor[1]} style={{...mano(170), marginTop: 6, marginLeft: -8}} />
          <Maquina texto={TXT.cuenta} desde={T.cuenta[0]} porLetra={T.cuenta[1]} style={{...palo(104), marginTop: -8}} />
        </div>
      </Escena>

      {/* ── 3 · VEN POR TU CAFÉ GRATIS ── */}
      <Escena rango={ESCENAS_CUMPLE.ven}>
        <div style={{position: 'absolute', left: X0, top: 300}}>
          <Maquina texto={TXT.ven1} desde={T.ven1[0]} porLetra={T.ven1[1]} style={palo(66, 500, {letterSpacing: '0.01em'})} />
          <Trazo texto={TXT.cafeGratis} desde={T.cafeGratis[0]} dura={T.cafeGratis[1]} style={{...mano(176), marginTop: 4, marginLeft: -8}} />
          <Maquina texto={TXT.ven2} desde={T.ven2[0]} porLetra={T.ven2[1]} style={{...palo(66, 500, {letterSpacing: '0.01em'}), marginTop: 6}} />
        </div>
        {/* legal: columna chica a la izquierda de la vela, entra por líneas */}
        <div style={{position: 'absolute', left: X0, top: 800, width: 420}}>
          {lineasLegal.map((l, i) => {
            const d = T.legal + i * 4;
            const t = interpolate(f, [d, d + 10], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic)});
            return (
              <div key={i} style={{fontFamily: SANS, fontWeight: 500, fontSize: 30, lineHeight: 1.45, color: C.beige,
                textShadow: SOMBRA, opacity: t, transform: `translateY(${(1 - t) * 12}px)`, whiteSpace: 'nowrap'}}>
                {l}
              </div>
            );
          })}
        </div>
      </Escena>

    </AbsoluteFill>
  );
};
