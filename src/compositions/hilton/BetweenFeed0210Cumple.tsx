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
  ven: [165, 255], // 3 s
  legal: [255, 400], // 4 s: se enciende la vela + legal en botones (sin salida: queda quieto)
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

/**
 * Ilustraciones ORIGINALES de Eli (su trazo de pincel, `BetweenRecursos.ILUSTRACIONES`).
 * Ronda 2 (29-09): «que sea más bonito, mejores trazados… globitos, cosas que vayan
 * surgiendo». Mis rayos de SVG se fueron: entran sus globos, confeti y corazón.
 * Cada una SURGE (sube y se destapa de abajo hacia arriba) y después flota suave.
 */
const RECURSO = (n: string) => staticFile(`assets/hilton/between/recursos/${n}.png`);
const Surge: React.FC<{
  src: string; x: number; y: number; ancho: number; desde: number; sube?: number; rot?: number;
  fase?: number; destape?: 'abajo' | 'centro';
}> = ({src, x, y, ancho, desde, sube = 220, rot = 0, fase = 0, destape = 'abajo'}) => {
  const f = useCurrentFrame();
  if (f < desde) return null;
  const t = interpolate(f, [desde, desde + 26], [0, 1], {extrapolateRight: 'clamp', easing: Easing.out(Easing.cubic)});
  const flota = Math.sin((f - desde) / 16 + fase) * 7;
  const gira = Math.sin((f - desde) / 22 + fase) * 2.2;
  const mascara = destape === 'abajo'
    ? `linear-gradient(0deg, #000 ${t * 120 - 12}%, transparent ${t * 120}%)`
    : `radial-gradient(circle, #000 ${t * 70}%, transparent ${t * 70 + 12}%)`;
  return (
    <Img src={src} style={{
      position: 'absolute', left: x, top: y, width: ancho,
      transform: `translateY(${(1 - t) * sube + flota}px) rotate(${rot + gira}deg) scale(${destape === 'centro' ? 0.6 + 0.4 * t : 1})`,
      transformOrigin: '50% 100%', opacity: Math.min(1, t * 1.4),
      WebkitMaskImage: mascara, maskImage: mascara,
      filter: 'drop-shadow(3px 4px 3px rgba(0,0,0,0.25))',
    }} />
  );
};

/** La llama: la foto encendida entra sólo en la zona de la vela y los dedos, con un golpe de luz. */
const LLAMA = {x: 556, y: 772};
const Encendido: React.FC<{desde: number}> = ({desde}) => {
  const f = useCurrentFrame();
  if (f < desde) return null;
  const t = interpolate(f, [desde, desde + 7], [0, 1], {extrapolateRight: 'clamp', easing: Easing.out(Easing.quad)});
  const golpe = interpolate(f, [desde, desde + 5, desde + 22], [0, 1, 0.35], {extrapolateRight: 'clamp'});
  const titila = 0.9 + 0.1 * Math.sin((f - desde) * 0.9) * Math.sin((f - desde) * 0.37);
  const mascara = `url(${staticFile('assets/hilton/between/oct/f-cumple-mascara-llama.png')})`;
  return (
    <>
      <Img src={staticFile('assets/hilton/between/oct/f-cumple-reel.jpg')} style={{
        position: 'absolute', width: 1080, height: 1920, opacity: t,
        WebkitMaskImage: mascara, maskImage: mascara, WebkitMaskSize: '100% 100%', maskSize: '100% 100%',
      }} />
      <AbsoluteFill style={{
        mixBlendMode: 'screen', opacity: golpe * titila,
        background: `radial-gradient(circle at ${LLAMA.x}px ${LLAMA.y}px, rgba(255,190,110,0.55) 0px, rgba(255,150,70,0.18) 150px, rgba(0,0,0,0) 330px)`,
      }} />
    </>
  );
};

/**
 * Confeti de Eli como destello de la vela (ronda 3: «que estén mirando hacia la vela»).
 * El PNG converge en su esquina inferior derecha (93 % · 89 %, medido en el alfa): ese
 * vértice va pegado a la llama y el de la derecha es el PNG espejado (`confeti-espejo.png`) y gira al revés, así los dos abren desde ella.
 */
const VERTICE = {x: 0.93, y: 0.89};
const Abanico: React.FC<{desde: number; lado: 'izq' | 'der'; ancho: number; gira: number}> = ({desde, lado, ancho, gira}) => {
  const f = useCurrentFrame();
  if (f < desde) return null;
  const s = spring({frame: f - desde, fps: 30, config: {damping: 10, stiffness: 150, mass: 0.6}});
  const alto = ancho * (455 / 429);
  const vx = LLAMA.x + (lado === 'izq' ? -40 : 40);
  const vy = LLAMA.y + 16;
  const late = 1 + 0.035 * Math.sin((f - desde) / 7);
  return (
    <Img src={RECURSO(lado === 'izq' ? 'confeti' : 'confeti-espejo')} style={{
      position: 'absolute', width: ancho, height: alto,
      left: lado === 'izq' ? vx - ancho * VERTICE.x : vx - ancho * (1 - VERTICE.x),
      top: vy - alto * VERTICE.y,
      transformOrigin: `${(lado === 'izq' ? VERTICE.x : 1 - VERTICE.x) * 100}% ${VERTICE.y * 100}%`,
      transform: `rotate(${lado === 'izq' ? gira : -gira}deg) scale(${s * late})`,
      opacity: Math.min(1, s * 2),
      filter: 'drop-shadow(0 0 10px rgba(255,190,120,0.35))',
    }} />
  );
};

/** El legal en «botones» café (la caja taupe del sistema), entrando con un rebote. */
const Boton: React.FC<{texto: string; desde: number; x: number; rot: number}> = ({texto, desde, x, rot}) => {
  const f = useCurrentFrame();
  const s = spring({frame: f - desde, fps: 30, config: {damping: 12, stiffness: 170, mass: 0.7}});
  return (
    <div style={{
      alignSelf: 'center', marginLeft: x, opacity: f < desde ? 0 : Math.min(1, s * 1.5),
      transform: `translateY(${(1 - s) * 26}px) rotate(${rot * s}deg) scale(${0.8 + 0.2 * s})`, transformOrigin: 'center center',
      backgroundColor: BETWEEN.cajas.fondo, borderRadius: BETWEEN.cajas.radio, padding: '15px 32px 17px',
      fontFamily: SANS, fontWeight: 700, fontSize: 37, lineHeight: 1.1, color: C.beige, whiteSpace: 'nowrap',
      boxShadow: '0 6px 18px rgba(36,26,18,0.35)',
    }}>
      {texto}
    </div>
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
  estasPop: 12,
  deTrazo: [20, 12] as const,
  cumple: [28, 2.3] as const,
  globos: 118,
  globo: 176,
  enciende: 4,
  confeti: 262,
  elCafe: [80, 2.4] as const,
  vaPor: [98, 14] as const,
  cuenta: [112, 2.2] as const,
  ven1: [170, 2.2] as const,
  cafeGratis: [194, 14] as const,
  ven2: [210, 1.3] as const,
  legal: [268, 6] as const, // primer botón y separación entre botones
};

export const FeedOct02Cumple: React.FC = () => {
  useFuentesListas();
  const f = useCurrentFrame();
  const T = TIEMPOS;
  // el legal en cuatro botones café, cortados donde se respira
  const botones = [
    {t: 'Beneficio válido únicamente', x: 0, rot: -1.2},
    {t: 'de lunes a viernes,', x: 0, rot: 1.2},
    {t: 'el mismo día de tu cumpleaños,', x: 0, rot: -1.2},
    {t: 'presentando carnet de identidad', x: 0, rot: 1.2},
    {t: 'al momento de solicitarlo.', x: 0, rot: -1.2},
  ];
  return (
    <AbsoluteFill style={{backgroundColor: C.sombra}}>
      {/* la vela parte APAGADA y se enciende al arrancar: es el hook (ronda 3 de Eli) */}
      <Img src={staticFile('assets/hilton/between/oct/f-cumple-apagada.jpg')}
        style={{position: 'absolute', width: 1080, height: 1920, objectFit: 'cover'}} />
      <Encendido desde={T.enciende} />
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
      {f < ESCENAS_CUMPLE.hook[1] && (
        <>
          <Img src={staticFile('assets/hilton/between/oct/f-cumple-figura-apagada.png')}
            style={{position: 'absolute', width: 1080, height: 1920}} />
          <Img src={staticFile('assets/hilton/between/oct/f-cumple-figura.png')}
            style={{position: 'absolute', width: 1080, height: 1920,
              opacity: interpolate(f, [T.enciende, T.enciende + 7], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})}} />
        </>
      )}

      {/* ilustraciones de Eli que van surgiendo */}
      <Surge src={RECURSO('globos-par')} x={86} y={1010} ancho={236} desde={T.globos} rot={-8} />
      <Surge src={RECURSO('globo-alt')} x={842} y={1060} ancho={112} desde={T.globo} rot={7} fase={1.7} />
      <Abanico desde={T.confeti} lado="izq" ancho={165} gira={-34} />
      <Abanico desde={T.confeti + 2} lado="der" ancho={165} gira={-34} />

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
      </Escena>

      {/* ── 4 · LEGAL en botones ── */}
      <Escena rango={ESCENAS_CUMPLE.legal}>
        <div style={{position: 'absolute', left: 0, right: 0, top: 262, display: 'flex', flexDirection: 'column', gap: 12, transform: `translateX(${LLAMA.x - 540}px)`}}>
          {botones.map((b, i) => (
            <Boton key={i} texto={b.t} desde={T.legal[0] + i * T.legal[1]} x={b.x} rot={b.rot} />
          ))}
        </div>
      </Escena>
    </AbsoluteFill>
  );
};
