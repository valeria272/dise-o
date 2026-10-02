// ============================================================================
// COPYWRITERS · CW-02 — «+3.627 SEGUIDORES EN 28 DÍAS.» · CASO 002 · 7 láminas
// ----------------------------------------------------------------------------
// BRIEF     clients/copywriters/briefs/202610_BRIEF_ESTUDIO_copywriters.md (CW-02).
//           Pilar «Resultados». Sale lunes 05-10-2026 · 10:00 · IG · FB · LinkedIn.
// RONDA 2   Valeria (02-10) sobre la v1 de volantines: «la dinámica del volantín no
//           la entendí» · «hacer hincapié en que es para un cliente de centros
//           comerciales» · «más genérico, más marketero» · «los volantines de
//           colores no combinan con nuestro rosado» → se rehace la historia y TODAS
//           las imágenes, en la paleta de la casa (neutros cálidos + rosa).
// ⛔ MARCA   NO se nombra («un strip center de Santiago»): sin KV, logo ni mascota.
// CIFRAS    Dashboard del concurso (Meta API, corte 01-10-2026 10:43), verificadas
//           a mano: 15.616 → 19.243 = +3.627 · meta 18.000 el 16-09, 12 días antes
//           del cierre (28-09) · 35.224 comentarios vs 10.605 en 2025 = 3,3x ·
//           alcance sept. 328.492, 323.731 no seguidores = 98 %.
//
// HISTORIA  Un caso contado para marketeros, en el mundo del cliente (un strip
//           center), con un objeto por idea:
//           01 el strip center al anochecer, neón rosa en el techo — el resultado
//           02 un neón rosa horizontal en la fachada ES la línea de la meta
//           03 el premio: un sobre de aguinaldo con cinta rosa — la razón real y la
//              mecánica simple («seguir + comentar. nada más.»)
//           04 la tómbola rebalsando — los comentarios
//           05 el pasillo con guirnaldas que convergen a un punto — reels, historias,
//              creadoras y pauta escritos sobre las líneas; «el post» en el centro
//           06 el estacionamiento desde arriba, estelas de autos llegando — el alcance
//           07 tres sobres en fila — tres sorteos: una conversación
// DATA      Ley del 30-09: la cifra es la pieza (Bebas Expanded); el segundo KPI
//           entra más chico, girado y pisando; ninguna cifra se corta.
// TIPOS     Bebas Light / Expanded / contorno · Balloon por trazados (ManoCurva).
//           Sin cuerpo de texto (R-44).
// FOTOS     Seedream 5 Pro (raw/copywriters/202610/gen/sc1–sc7) · video Kling 2.5
//           Pro en 01, 04, 05 y 06. Sin personas, letreros ni marcas.
// Formato 1080×1350 · 30 fps · 150 cuadros.
// ============================================================================
import React from "react";
import {AbsoluteFill, Easing, OffthreadVideo, interpolate, staticFile, useCurrentFrame} from "remotion";
import {C2, VOZ2, SOMBRA_SOBRE_FOTO, asegurarFuentesV2, granoSVG} from "../../brand/copylab/sistemaV2";
import {Foto, ManoCurva} from "../../brand/copylab/piezasV2";

export const CW02_FRAMES = 150;
const M = 76;
const A = (n: string) => `assets/copywriters/202610/${n}`;
const fijo = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;
const sale = Easing.out(Easing.cubic);

const Grano: React.FC = () => (
  <AbsoluteFill style={{backgroundImage: granoSVG(0.05, 5), backgroundSize: "300px 300px"}} />
);

/** Fondo: video si lo hay, si no la foto (mismo recorte). `sinVideo` fuerza la
 *  foto para revisar la composición mientras los clips se generan. */
let SIN_VIDEO = false;
const Fondo: React.FC<{foto: string; video?: string}> = ({foto, video}) =>
  video && !SIN_VIDEO ? (
    <OffthreadVideo src={staticFile(A(video))} muted
      style={{position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover"}} />
  ) : <Foto src={A(foto)} />;

const Velo: React.FC<{css: string}> = ({css}) => <AbsoluteFill style={{background: css}} />;

const Tipo: React.FC<{
  px: number; voz?: "titular" | "impacto" | "bloque"; peso?: number; color?: string;
  contorno?: number; tracking?: number; sombra?: boolean; children: React.ReactNode;
}> = ({px, voz = "impacto", peso, color = C2.offwhite, contorno = 0, tracking = 0,
       sombra = true, children}) => (
  <div style={{
    fontFamily: VOZ2[voz], fontWeight: peso ?? (voz === "titular" ? 700 : 800),
    fontSize: px, lineHeight: 0.84, letterSpacing: tracking, whiteSpace: "nowrap",
    textTransform: "uppercase",
    color: contorno ? "transparent" : color,
    WebkitTextStroke: contorno ? `${contorno}px ${color}` : undefined,
    textShadow: sombra && !contorno ? SOMBRA_SOBRE_FOTO : undefined,
    filter: sombra && contorno ? "drop-shadow(0 4px 12px rgba(0,0,0,0.7))" : undefined,
  }}>{children}</div>
);

const En: React.FC<{x: number; y: number; giro?: number; desde?: number; children: React.ReactNode}> =
({x, y, giro = 0, desde, children}) => {
  const f = useCurrentFrame();
  const p = desde === undefined ? 1 : interpolate(f, [desde, desde + 14], [0, 1], {...fijo, easing: sale});
  return (
    <div style={{position: "absolute", left: x, top: y, opacity: p,
                 transform: `translateY(${(1 - p) * 26}px) rotate(${giro}deg)`}}>{children}</div>
  );
};

// ====================== 01 · EL RESULTADO (video) ======================
// El edificio ocupa y 800–1150; el cielo queda libre para la cifra.
const L1: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Fondo foto="sc1.png" video="vsc1-stripcenter.mp4" />
    <Velo css="linear-gradient(180deg, rgba(11,11,11,0.5) 0%, rgba(11,11,11,0.1) 40%, rgba(11,11,11,0) 55%)" />
    <Grano />
    <En x={M - 14} y={130} desde={0}><Tipo px={246} voz="bloque">+3.627</Tipo></En>
    <En x={M} y={358} desde={6}><Tipo px={74} voz="titular" peso={300} tracking={5}>SEGUIDORES EN 28 DÍAS.</Tipo></En>
    <ManoCurva id="s1a" d="M 64 590 C 300 480, 660 550, 1030 450" px={84}
               texto="para un strip center" desde={18} dura={22} sombra />
    <ManoCurva id="s1b" d="M 300 700 C 500 640, 760 700, 1030 630" px={84}
               texto="de santiago." desde={30} dura={16} sombra />
  </AbsoluteFill>
);

// ====================== 02 · LA META (fija) ======================
// El neón MEDIDO cruza la fachada a la altura y ≈ 700: es la línea de la meta.
const L2: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Fondo foto="sc2.png" />
    <Grano />
    <En x={M} y={300}><Tipo px={74} voz="titular" peso={300} tracking={5}>LA META ERA</Tipo></En>
    <En x={M - 14} y={392}><Tipo px={236} voz="bloque">18.000</Tipo></En>
    <ManoCurva id="s2a" d="M 64 900 C 300 800, 640 900, 1030 790" px={92}
               texto="llegamos 12 días antes." color={C2.offwhite} dura={1} sombra />
  </AbsoluteFill>
);

// ====================== 03 · EL PREMIO (fija) ======================
// Sobre MEDIDO: centro ≈ (540, 767), y 480–1060.
const L3: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Fondo foto="sc3.png" />
    <Velo css="linear-gradient(180deg, rgba(11,11,11,0.86) 0%, rgba(11,11,11,0.5) 26%, rgba(11,11,11,0) 36%), linear-gradient(0deg, rgba(11,11,11,0.8) 0%, rgba(11,11,11,0) 20%)" />
    <Grano />
    <En x={M} y={84}><Tipo px={70} voz="titular" peso={300} tracking={5}>UNA RAZÓN REAL:</Tipo></En>
    <En x={M - 6} y={168}><Tipo px={118} voz="impacto">EL AGUINALDO</Tipo></En>
    <En x={M - 6} y={276}><Tipo px={118} voz="impacto" color={C2.rosa}>DEL 18.</Tipo></En>
    <En x={M} y={1112}><Tipo px={66} voz="impacto" contorno={2.4}>SEGUIR + COMENTAR.</Tipo></En>
    <En x={760} y={1088} giro={-6}>
      <div style={{fontFamily: VOZ2.mano, fontWeight: 800, fontSize: 64, color: C2.rosa,
                   textTransform: "uppercase", textShadow: SOMBRA_SOBRE_FOTO}}>nada más.</div>
    </En>
  </AbsoluteFill>
);

// ====================== 04 · LOS COMENTARIOS (video) ======================
const L4: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Fondo foto="sc4.png" video="vsc4-tombola.mp4" />
    <Velo css="linear-gradient(180deg, rgba(11,11,11,0.85) 0%, rgba(11,11,11,0.55) 26%, rgba(11,11,11,0) 38%)" />
    <Grano />
    <En x={M - 14} y={80} desde={0}><Tipo px={200} voz="bloque">+35 MIL</Tipo></En>
    <En x={M} y={264} desde={6}><Tipo px={58} voz="titular" peso={300} tracking={6}>COMENTARIOS EN EL POST.</Tipo></En>
    <En x={640} y={330} giro={-6} desde={20}><Tipo px={170} voz="bloque" color={C2.rosa}>3,3X</Tipo></En>
    <ManoCurva id="s4a" d="M 580 590 C 720 550, 870 600, 1030 550" px={48} texto="vs. el año pasado."
               color={C2.offwhite} desde={34} dura={18} sombra />
  </AbsoluteFill>
);

// ====================== 05 · LA CAMPAÑA (video) ======================
// Punto de fuga MEDIDO ≈ (533, 800). Los canales van escritos sobre las líneas
// de luces de la mitad de arriba, girados según su ángulo, leyendo hacia el centro.
const FUGA = {x: 533, y: 800};
const CANALES: {t: string; ang: number; r: number}[] = [
  {t: "REELS", ang: 198, r: 360},
  {t: "HISTORIAS", ang: 236, r: 330},
  {t: "2 CREADORAS", ang: 304, r: 330},
  {t: "PAUTA", ang: 342, r: 360},
];
const L5: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{background: C2.negro}}>
      <Fondo foto="sc5.png" video="vsc5-pasillo.mp4" />
      <Velo css="linear-gradient(180deg, rgba(11,11,11,0.85) 0%, rgba(11,11,11,0.35) 22%, rgba(11,11,11,0) 30%), linear-gradient(0deg, rgba(11,11,11,0.86) 0%, rgba(11,11,11,0.3) 18%, rgba(11,11,11,0) 28%)" />
      <Grano />
      <En x={M} y={70} desde={0}><Tipo px={70} voz="titular" peso={300} tracking={4}>NO FUE UN POST.</Tipo></En>
      <En x={M - 6} y={142} desde={6}><Tipo px={104} voz="impacto">FUE UNA CAMPAÑA.</Tipo></En>
      {CANALES.map((c, i) => {
        const rad = (c.ang * Math.PI) / 180;
        const x = FUGA.x + Math.cos(rad) * c.r;
        const y = FUGA.y + Math.sin(rad) * c.r;
        const derecha = Math.cos(rad) > 0;
        const giro = derecha ? c.ang : c.ang - 180;
        const p = interpolate(f, [16 + i * 6, 30 + i * 6], [0, 1], {...fijo, easing: sale});
        return (
          <div key={c.t} style={{position: "absolute", left: x, top: y, opacity: p,
                                 transform: `translate(-50%, -50%) rotate(${giro}deg)`}}>
            <Tipo px={50} voz="impacto" tracking={2}>{c.t}</Tipo>
          </div>
        );
      })}
      <div style={{position: "absolute", left: FUGA.x, top: FUGA.y - 10, transform: "translate(-50%, -50%)",
                   opacity: interpolate(f, [44, 56], [0, 1], fijo)}}>
        <div style={{fontFamily: VOZ2.mano, fontWeight: 800, fontSize: 76, color: C2.rosa,
                     textTransform: "uppercase", whiteSpace: "nowrap",
                     textShadow: "0 0 26px rgba(11,11,11,0.95), 0 4px 14px rgba(0,0,0,0.9)"}}>el post.</div>
      </div>
      <ManoCurva id="s5a" d="M 64 1190 C 320 1090, 640 1230, 1030 1110" px={64}
                 texto="todo empujaba al mismo post." desde={60} dura={24} sombra />
    </AbsoluteFill>
  );
};

// ====================== 06 · EL ALCANCE (video) ======================
const L6: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Fondo foto="sc6.png" video="vsc6-estacionamiento.mp4" />
    <Velo css="linear-gradient(90deg, rgba(11,11,11,0.6) 0%, rgba(11,11,11,0.2) 50%, rgba(11,11,11,0) 70%)" />
    <Grano />
    <En x={M - 14} y={300} desde={0}><Tipo px={210} voz="bloque">328 MIL</Tipo></En>
    <En x={M} y={490} desde={6}><Tipo px={58} voz="titular" peso={300} tracking={6}>CUENTAS ALCANZADAS.</Tipo></En>
    <En x={M - 6} y={780} giro={-5} desde={18}><Tipo px={200} voz="bloque" color={C2.rosa}>98%</Tipo></En>
    <ManoCurva id="s6a" d="M 64 1090 C 260 1010, 480 1080, 720 1000" px={56}
               texto="no seguían la cuenta." color={C2.offwhite} desde={32} dura={20} sombra />
  </AbsoluteFill>
);

// ====================== 07 · LA CONVERSACIÓN (fija) ======================
// Sobres MEDIDOS: x 107–973 · y 550–1033. Arriba hay carteles de pared: el velo
// los apaga para que nada se lea como texto.
const L7: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Fondo foto="sc7.png" />
    <Velo css="linear-gradient(180deg, rgba(11,11,11,0.94) 0%, rgba(11,11,11,0.86) 30%, rgba(11,11,11,0.2) 42%, rgba(11,11,11,0) 48%), linear-gradient(0deg, rgba(11,11,11,0.8) 0%, rgba(11,11,11,0) 16%)" />
    <Grano />
    <En x={M} y={96}><Tipo px={84} voz="titular" peso={300} tracking={4}>UN SORTEO ES UN PICO.</Tipo></En>
    <ManoCurva id="s7a" d="M 60 340 C 260 220, 660 230, 1030 330" px={104} texto="tres son una" dura={1} sombra />
    <ManoCurva id="s7b" d="M 70 470 C 360 400, 700 490, 1030 410" px={104} texto="conversación." dura={1} sombra />
    <En x={M} y={1112}><Tipo px={62} voz="impacto" contorno={2.4}>3 SORTEOS SEMANALES.</Tipo></En>
  </AbsoluteFill>
);

const LAMINAS = [L1, L2, L3, L4, L5, L6, L7];

export const CW02Concurso: React.FC<{lamina?: number; sinVideo?: boolean}> = ({lamina = 1, sinVideo = false}) => {
  asegurarFuentesV2();
  SIN_VIDEO = sinVideo;
  const L = LAMINAS[Math.min(Math.max(lamina, 1), LAMINAS.length) - 1];
  return <L />;
};
