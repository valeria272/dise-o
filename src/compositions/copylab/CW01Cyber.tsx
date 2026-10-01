// ============================================================================
// COPYWRITERS · CW-01 — «72 HORAS.» · así vive un Cyber una agencia · 5 láminas
// ----------------------------------------------------------------------------
// BRIEF     clients/copywriters/briefs/202610_BRIEF_ESTUDIO_copywriters.md (CW-01,
//           grilla v3). Pilar «Cómo trabajamos». Sale viernes 02-10 · 11:00.
// RONDA 3   Valeria (01-10), sobre la v2 fotográfica: «queda mejor», pero
//           · los textos de cuerpo «estándar de IA se ven muy básicos» → FUERA la
//             Neue Haas. Sólo las dos voces del sistema Copylab: Bebas y Balloon;
//           · Balloon con más dinamismo: «dale curvas, intención» → la mano corre
//             por TRAZADOS (textPath): rodea el reloj, se arquea, ondula, y se
//             escribe en pantalla;
//           · «añade videos al carrusel» → 01, 03 y 04 son MP4 (Kling 2.5 Pro
//             desde las fotos aprobadas);
//           · «más corto, sobre cómo trabaja una agencia el Cyber y cómo
//             monitoreamos» → el copy se reescribió corto, con el monitoreo al
//             centro. Valeria pidió el cambio de texto: manda sobre el brief.
//
// IDEA      La misma mesa de nogal durante el Cyber. 72 horas (lun 5 → mié 7).
//           01 muro de pruebas · 02 fichas (3 semanas antes) · 03 reloj de arena
//           (los tres tiempos giran alrededor) · 04 laptop con la pantalla real de
//           pauta y su ALERTA rodeada a mano · 05 la mañana siguiente.
// PANTALLA  04: vista principal REAL de Paid Media Pro (captura 01-10), difuminada
//           r = 7 px: con zoom 2× no se lee cifra ni cliente. Montada con la
//           homografía MEDIDA de la pantalla (R-33). La franja roja que se rodea es
//           la alerta de pacing real del dashboard (gasto diario sobre presupuesto).
// MOTION    Cada lámina dura 5 s. La mano se ESCRIBE (máscara que avanza por el
//           trazado) y el anillo de 03 gira lento. Las láminas fijas (02, 05) se
//           exportan como PNG desde el último cuadro.
// FOTOS     Seedream 5 Pro (raw/copywriters/202610/gen/c1–c5) · video Kling 2.5
//           Pro (v1, v3, v4). Sin personas, marcas ni datos generados.
// Formato 1080×1350 · 30 fps · 150 cuadros.
// ============================================================================
import React from "react";
import {AbsoluteFill, Img, OffthreadVideo, interpolate, staticFile, useCurrentFrame,
        Easing} from "remotion";
import {C2, VOZ2, SOMBRA_SOBRE_FOTO, asegurarFuentesV2, granoSVG} from "../../brand/copylab/sistemaV2";
import {Foto, Linea, ManoCurva} from "../../brand/copylab/piezasV2";

export const CW01_FRAMES = 150;
const M = 76;
const F = (n: string) => `assets/copywriters/202610/${n}`;
const fijo = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;
const sale = Easing.out(Easing.cubic);

const Grano: React.FC = () => (
  <AbsoluteFill style={{backgroundImage: granoSVG(0.05, 5), backgroundSize: "300px 300px"}} />
);

const En: React.FC<{x: number; y: number; giro?: number; children: React.ReactNode}> =
({x, y, giro = 0, children}) => (
  <div style={{position: "absolute", left: x, top: y,
               transform: giro ? `rotate(${giro}deg)` : undefined}}>{children}</div>
);

/** Fondo de video a sangre, recortado igual que la foto (cover, centrado). */
const FondoVideo: React.FC<{src: string}> = ({src}) => (
  <OffthreadVideo src={staticFile(src)} muted
    style={{position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover"}} />
);

/** Entrada de un bloque Bebas: sube 24 px y aparece. */
const Sube: React.FC<{desde: number; children: React.ReactNode}> = ({desde, children}) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [desde, desde + 14], [0, 1], {...fijo, easing: sale});
  return <div style={{opacity: p, transform: `translateY(${(1 - p) * 24}px)`}}>{children}</div>;
};

/** Trazo de plumón que se dibuja (dasharray). Para rodear algo. */
const Rodea: React.FC<{d: string; desde: number; largo?: number; grosor?: number}> =
({d, desde, largo = 1800, grosor = 8}) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [desde, desde + 20], [0, 1], {...fijo, easing: sale});
  return (
    <svg width={1080} height={1350} style={{position: "absolute", inset: 0, overflow: "visible"}}>
      <path d={d} fill="none" stroke={C2.rosa} strokeWidth={grosor} strokeLinecap="round"
            strokeDasharray={largo} strokeDashoffset={largo * (1 - p)} />
    </svg>
  );
};

// ====================== 01 · 72 HORAS (video) ======================
const L1: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <FondoVideo src={F("v1-muro.mp4")} />
    <AbsoluteFill style={{
      background: "linear-gradient(10deg, rgba(11,11,11,0.95) 0%, rgba(11,11,11,0.78) 36%, rgba(11,11,11,0) 64%)",
    }} />
    <Grano />
    <En x={M - 10} y={104} giro={-3}>
      <div style={{
        background: "rgba(214,206,196,0.92)", backgroundImage: granoSVG(0.22, 3),
        padding: "14px 26px 10px", clipPath: "polygon(1% 8%, 99% 0%, 98% 92%, 0% 100%)",
        boxShadow: "0 6px 20px rgba(0,0,0,0.45)",
      }}>
        <Linea cuerpo={40} voz="titular" color={C2.negro} tracking={4}>05—07.10 · CYBERMONDAY</Linea>
      </div>
    </En>
    {/* La mano sube en arco y cae sobre el número. */}
    <ManoCurva id="c1a" d="M 62 800 C 260 560, 700 520, 1010 690" px={96} texto="así se vive un cyber"
               desde={10} dura={24} sombra />
    <En x={M - 18} y={790}>
      <Sube desde={2}>
        <div style={{display: "flex", alignItems: "flex-end", gap: 24}}>
          <Linea cuerpo={330} voz="bloque" sombra>72</Linea>
          <div style={{paddingBottom: 8}}><Linea cuerpo={128} sombra>HORAS.</Linea></div>
        </div>
      </Sube>
    </En>
  </AbsoluteFill>
);

// ====================== 02 · LAS FICHAS (fija) ======================
const FICHAS: {cx: number; cy: number; giro: number; texto: React.ReactNode}[] = [
  {cx: 198, cy: 662, giro: -3.0, texto: <>QUÉ<br />PRODUCTO.</>},
  {cx: 537, cy: 652, giro: -1.6, texto: <>PARA<br />QUIÉN.</>},
  {cx: 877, cy: 650, giro: -1.0, texto: <>CON QUÉ<br />OFERTA.</>},
];

const L2: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Foto src={F("c2.png")} />
    <AbsoluteFill style={{
      background: "linear-gradient(180deg, rgba(11,11,11,0.88) 0%, rgba(11,11,11,0.55) 24%, rgba(11,11,11,0) 34%)",
    }} />
    <Grano />
    <En x={M - 8} y={74}>
      <div style={{display: "flex", alignItems: "flex-end", gap: 20}}>
        <Linea cuerpo={230} voz="bloque" sombra>3</Linea>
        <div style={{paddingBottom: 4}}>
          <Linea cuerpo={88} sombra>SEMANAS</Linea>
          <div style={{height: 8}} />
          <Linea cuerpo={88} sombra>ANTES.</Linea>
        </div>
      </div>
    </En>
    {/* La mano baja en curva hacia las fichas: ahí se decide. */}
    <ManoCurva id="c2a" d="M 560 150 Q 960 110 1000 440" px={84} texto="acá se gana."
               desde={0} dura={1} sombra />
    {FICHAS.map((f, i) => (
      <div key={i} style={{position: "absolute", left: f.cx - 150, top: f.cy - 82, width: 300,
                           transform: `rotate(${f.giro}deg)`}}>
        <div style={{fontFamily: VOZ2.mano, fontWeight: 800, fontSize: 56, lineHeight: 1.08,
                     color: "#1B1A19", textAlign: "center", textTransform: "uppercase",
                     mixBlendMode: "multiply", opacity: 0.9}}>{f.texto}</div>
      </div>
    ))}
  </AbsoluteFill>
);

// ====================== 03 · LOS TRES TIEMPOS (video) ======================
// Reloj medido en el clip: centro ≈ (765, 600). El anillo es un CÍRCULO exacto
// en sentido HORARIO: la mitad de arriba —la que se lee primero— queda derecha.
// El radio deja el anillo a ≥ 38 px del borde derecho. El texto se estira a la circunferencia (textLength) y
// gira el anillo entero: nunca queda un hueco ni una palabra cortada.
const CX = 744, CY = 600, R = 258;
const ANILLO = `M ${CX} ${CY - R} A ${R} ${R} 0 1 1 ${CX} ${CY + R} A ${R} ${R} 0 1 1 ${CX} ${CY - R}`;
const L3: React.FC = () => {
  const f = useCurrentFrame();
  const giro = interpolate(f, [0, CW01_FRAMES], [0, -40]);
  const aparece = interpolate(f, [6, 26], [0, 1], fijo);
  return (
    <AbsoluteFill style={{background: C2.negro}}>
      <FondoVideo src={F("v3-arena.mp4")} />
      <AbsoluteFill style={{
        background: "linear-gradient(0deg, rgba(11,11,11,0.9) 0%, rgba(11,11,11,0.5) 22%, rgba(11,11,11,0) 38%), linear-gradient(90deg, rgba(11,11,11,0.55) 0%, rgba(11,11,11,0) 45%)",
      }} />
      <Grano />
      <div style={{opacity: aparece}}>
        <svg width={1080} height={1350} style={{position: "absolute", inset: 0, overflow: "visible",
                                               filter: "drop-shadow(0 4px 12px rgba(0,0,0,0.6))"}}>
          <defs><path id="anillo" d={ANILLO} /></defs>
          <g transform={`rotate(${giro} ${CX} ${CY})`}>
            <text fill={C2.rosa} textLength={2 * Math.PI * R * 0.995} lengthAdjust="spacing"
                  style={{fontFamily: VOZ2.mano, fontWeight: 800, fontSize: 46,
                          textTransform: "uppercase"}}>
              <textPath href="#anillo">
                antes · durante · últimas horas · antes · durante · últimas horas ·
              </textPath>
            </text>
          </g>
        </svg>
      </div>
      <En x={M - 8} y={76}><Sube desde={0}>
        <div style={{display: "flex", alignItems: "flex-end", gap: 20}}>
          <Linea cuerpo={230} voz="bloque" sombra>3</Linea>
          <div style={{paddingBottom: 4}}><Linea cuerpo={88} sombra>TIEMPOS.</Linea></div>
        </div>
      </Sube></En>
      <En x={M} y={1012}><Sube desde={30}>
        <Linea cuerpo={80} sombra>EL ÚLTIMO DÍA</Linea>
        <div style={{height: 12}} />
        <Linea cuerpo={80} color={C2.rosa} sombra>TAMBIÉN VENDE.</Linea>
      </Sube></En>
    </AbsoluteFill>
  );
};

// ====================== 04 · EL MONITOREO (video) ======================
const PANTALLA =
  "matrix3d(0.370046502,-0.0006120080998,0,3.570532578e-05,0.01894831912,0.3442950326,0,-4.014049172e-06,0,0,1,0,242,575,0,1)";
// Franja de alerta real del dashboard, mapeada a la foto: x 347–782 · y 578–634.
const ELIPSE_ALERTA =
  "M 352 640 C 300 600, 420 558, 600 560 C 744 561, 796 586, 778 616 C 760 646, 620 658, 470 652 C 382 648, 330 630, 364 594";

const L4: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <FondoVideo src={F("v4-laptop.mp4")} />
    <Img src={staticFile(F("cw01-pantalla-laptop.png"))}
         style={{position: "absolute", left: 0, top: 0, width: 1600, height: 1000,
                 transformOrigin: "0 0", transform: PANTALLA}} />
    <AbsoluteFill style={{
      background: "radial-gradient(ellipse 30% 22% at 66% 46%, rgba(255,236,210,0.16) 0%, rgba(255,236,210,0) 100%)",
    }} />
    <AbsoluteFill style={{
      background: "linear-gradient(180deg, rgba(11,11,11,0.8) 0%, rgba(11,11,11,0.4) 26%, rgba(11,11,11,0) 36%), linear-gradient(0deg, rgba(11,11,11,0.86) 0%, rgba(11,11,11,0.3) 18%, rgba(11,11,11,0) 28%)",
    }} />
    <Grano />
    <En x={M} y={80}><Sube desde={0}>
      <Linea cuerpo={104} sombra>MONITOREO</Linea>
      <div style={{height: 12}} />
      <Linea cuerpo={104} color={C2.rosa} sombra>HORA A HORA.</Linea>
    </Sube></En>
    {/* El plumón rodea la alerta real de la pantalla. */}
    <Rodea d={ELIPSE_ALERTA} desde={34} grosor={7} largo={1500} />
    <ManoCurva id="c4a" d="M 74 1180 C 300 1010, 600 1250, 1010 1070" px={64}
               texto="si algo se dispara, lo vemos." desde={52} dura={26} sombra />
  </AbsoluteFill>
);

// ====================== 05 · LA MAÑANA SIGUIENTE (fija) ======================
const L5: React.FC = () => (
  <AbsoluteFill style={{background: C2.offwhite}}>
    <Foto src={F("c5.png")} />
    <Grano />
    <En x={M} y={84}>
      <Linea cuerpo={92} color={C2.negro}>DESPUÉS,</Linea>
      <div style={{height: 10}} />
      <Linea cuerpo={92} color={C2.negro}>LO QUE APRENDIMOS.</Linea>
    </En>
    {/* La mano barre la pared en dos curvas que se cruzan de intención: la
        primera sube en arco, la segunda cae y remonta como un trazo de plumón. */}
    <ManoCurva id="c5a" d="M 84 590 C 250 360, 640 330, 1040 470" px={112}
               texto="el cyber se gana" desde={0} dura={1} />
    <ManoCurva id="c5b" d="M 90 664 C 380 790, 640 440, 1030 580" px={112}
               texto="antes del cyber." desde={0} dura={1} />
  </AbsoluteFill>
);

const LAMINAS = [L1, L2, L3, L4, L5];

export const CW01Cyber: React.FC<{lamina?: number}> = ({lamina = 1}) => {
  asegurarFuentesV2();
  const L = LAMINAS[Math.min(Math.max(lamina, 1), LAMINAS.length) - 1];
  return <L />;
};
