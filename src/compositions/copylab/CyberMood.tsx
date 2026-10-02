// ============================================================================
// COPYWRITERS · «CYBER MOOD» — post animado (motion graphic breve) · 4:5 · 8 s
// ----------------------------------------------------------------------------
// PEDIDO    Valeria (01-10-2026): «un post tipo Cyber Mood, no molestar… no
//           atenderemos. Algo irónico, entretenido, cool, un motion graphic breve
//           pero que nos veamos onderos». Para el domingo 04-10 en la noche, antes
//           de que parta el Cyber (lun 05 · 00:00).
//
// IDEA      El cartel de hotel. Una puerta de nogal cerrada, de noche, con luz rosa
//           escapando por debajo (adentro hay algo — fiesta o pauta). Cae un cartel
//           rosa a la manilla: «NO MOLESTAR.». Se balancea, gira, y por detrás dice
//           «NO ATENDEREMOS…» — y la mano remata: «…nada que no sea el Cyber.».
//           La ironía: el «no molestar» de una agencia en Cyber no es descanso.
//
// MOTION    El cartel se construye en código (no es foto): cae con resorte, cuelga
//           de la manilla MEDIDA (841, 568) y oscila como péndulo amortiguado. El
//           giro es 3D real (rotateY con dos caras). La sombra en la puerta sigue el
//           ángulo. Balloon se escribe por un trazado (ManoCurva, del kit).
// TIPOS     Bebas Expanded ExtraBold («CYBER») contra Bebas Light («MOOD.»); en el
//           cartel, Bebas normal y SemiExpanded; Balloon sólo en el remate.
// FOTO      Seedream 5 Pro, raw/copywriters/202610/gen/m1-puerta.png. Sin personas,
//           marcas ni letreros. El audio se agrega en la app (R-42).
// Formato 1080×1350 · 30 fps · 240 cuadros.
// ============================================================================
import React from "react";
import {AbsoluteFill, Easing, interpolate, spring, useCurrentFrame, useVideoConfig} from "remotion";
import {C2, VOZ2, SOMBRA_SOBRE_FOTO, asegurarFuentesV2, granoSVG} from "../../brand/copylab/sistemaV2";
import {Foto, ManoCurva} from "../../brand/copylab/piezasV2";

export const CYBER_MOOD_FRAMES = 240;
const M = 76;
const fijo = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;
const sale = Easing.out(Easing.cubic);

// Manilla MEDIDA sobre la foto (1770×2360 → cover 1080×1350): centro (841, 568).
const POMO = {x: 841, y: 568};
const CARTEL = {w: 300, h: 640, ojo: 74}; // ojo = del borde superior al centro del agujero
const CAE = 26;   // cuadro en que el cartel engancha
const GIRA = 118; // cuadro en que empieza a girar

/** Entrada: sube y aparece. */
const Sube: React.FC<{desde: number; children: React.ReactNode}> = ({desde, children}) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [desde, desde + 14], [0, 1], {...fijo, easing: sale});
  return <div style={{opacity: p, transform: `translateY(${(1 - p) * 28}px)`}}>{children}</div>;
};

const Tipo: React.FC<{
  px: number; voz?: "titular" | "impacto" | "bloque"; peso?: number; color?: string;
  tracking?: number; sombra?: boolean; children: React.ReactNode;
}> = ({px, voz = "impacto", peso, color = C2.offwhite, tracking = 0, sombra = false, children}) => (
  <div style={{
    fontFamily: VOZ2[voz], fontWeight: peso ?? (voz === "titular" ? 700 : 800),
    fontSize: px, lineHeight: 0.86, letterSpacing: tracking, color, whiteSpace: "nowrap",
    textTransform: "uppercase", textShadow: sombra ? SOMBRA_SOBRE_FOTO : undefined,
  }}>{children}</div>
);

/** Cara del cartel: cartulina con el agujero troquelado y la ranura. */
const Cara: React.FC<{fondo: string; atras?: boolean; children: React.ReactNode}> =
({fondo, atras = false, children}) => {
  const hueco = `radial-gradient(circle at 50% ${CARTEL.ojo}px, transparent 27px, #000 28px)`;
  return (
    <div style={{
      position: "absolute", inset: 0, background: fondo, borderRadius: "10px 10px 14px 14px",
      backfaceVisibility: "hidden", transform: atras ? "rotateY(180deg)" : undefined,
      WebkitMaskImage: hueco, maskImage: hueco,
    }}>
      <AbsoluteFill style={{backgroundImage: granoSVG(0.14, atras ? 11 : 3),
                            backgroundSize: "300px 300px", borderRadius: "inherit"}} />
      {/* Ranura del troquel: del agujero hacia el borde, como los carteles de hotel. */}
      <div style={{position: "absolute", left: CARTEL.w / 2 + 24, top: CARTEL.ojo - 3,
                   width: 70, height: 6, background: "rgba(11,11,11,0.55)",
                   transform: "rotate(-28deg)", transformOrigin: "0 50%", borderRadius: 3}} />
      <div style={{position: "absolute", left: 0, right: 0, top: 150, display: "flex",
                   flexDirection: "column", alignItems: "center", textAlign: "center"}}>
        {children}
      </div>
    </div>
  );
};

export const CyberMood: React.FC = () => {
  asegurarFuentesV2();
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();

  // Caída con resorte hasta engancharse en la manilla.
  const caida = spring({frame: f - 8, fps, config: {damping: 13, stiffness: 120, mass: 0.9}});
  const dy = interpolate(caida, [0, 1], [-1100, 0]);

  // Péndulo amortiguado: el golpe de la caída y un segundo empujón cuando gira.
  const t1 = Math.max(0, f - CAE);
  const t2 = Math.max(0, f - GIRA);
  const angulo = 13 * Math.exp(-t1 / 34) * Math.sin(t1 * 0.24)
               + (f >= GIRA ? 6 * Math.exp(-t2 / 28) * Math.sin(t2 * 0.26) : 0);

  // Giro 3D: de frente («NO MOLESTAR.») a la espalda («NO ATENDEREMOS…»).
  const giro = interpolate(f, [GIRA, GIRA + 20], [0, 180], {...fijo, easing: Easing.inOut(Easing.cubic)});

  // La luz bajo la puerta respira.
  const luz = 0.75 + 0.25 * Math.sin(f * 0.12);

  return (
    <AbsoluteFill style={{background: C2.negro}}>
      <Foto src="assets/copywriters/202610/m1-puerta.png" />
      {/* Halo rosa bajo la puerta, que respira. */}
      <AbsoluteFill style={{
        background: `radial-gradient(ellipse 46% 7% at 46% 90%, rgba(255,61,156,${0.32 * luz}) 0%, rgba(255,61,156,0) 100%)`,
        mixBlendMode: "screen",
      }} />
      <AbsoluteFill style={{
        background: "linear-gradient(90deg, rgba(11,11,11,0.55) 0%, rgba(11,11,11,0.2) 45%, rgba(11,11,11,0) 60%)",
      }} />
      <AbsoluteFill style={{backgroundImage: granoSVG(0.05, 5), backgroundSize: "300px 300px"}} />

      {/* El titular: Expanded contra Light. */}
      <div style={{position: "absolute", left: M - 10, top: 150}}>
        <Sube desde={0}><Tipo px={230} voz="bloque" sombra>CYBER</Tipo></Sube>
      </div>
      <div style={{position: "absolute", left: M - 4, top: 360}}>
        <Sube desde={6}><Tipo px={210} voz="titular" peso={300} tracking={4} sombra>MOOD.</Tipo></Sube>
      </div>

      {/* Sombra del cartel sobre la puerta: corrida a la derecha y abajo, sigue el ángulo. */}
      <div style={{
        position: "absolute", left: POMO.x - CARTEL.w / 2 + 22, top: POMO.y - CARTEL.ojo + 26,
        width: CARTEL.w, height: CARTEL.h, borderRadius: 14, background: "rgba(0,0,0,0.55)",
        filter: "blur(16px)", opacity: caida,
        transform: `translateY(${dy}px) rotate(${angulo}deg)`,
        transformOrigin: `${CARTEL.w / 2}px ${CARTEL.ojo}px`,
      }} />

      {/* El cartel. Pivota en el agujero, que calza en la manilla. */}
      <div style={{
        position: "absolute", left: POMO.x - CARTEL.w / 2, top: POMO.y - CARTEL.ojo,
        width: CARTEL.w, height: CARTEL.h, perspective: 1400,
        transform: `translateY(${dy}px) rotate(${angulo}deg)`,
        transformOrigin: `${CARTEL.w / 2}px ${CARTEL.ojo}px`,
      }}>
        <div style={{position: "absolute", inset: 0, transformStyle: "preserve-3d",
                     transform: `rotateY(${giro}deg)`}}>
          <Cara fondo={C2.rosa}>
            <Tipo px={120} voz="titular" peso={300} color={C2.negro} tracking={3}>NO</Tipo>
            <div style={{height: 14}} />
            <Tipo px={66} voz="impacto" color={C2.negro}>MOLESTAR.</Tipo>
            <div style={{height: 150}} />
            <Tipo px={30} voz="titular" color={C2.negro} tracking={7}>CYBER · ON</Tipo>
          </Cara>
          <Cara fondo={C2.offwhite} atras>
            <Tipo px={120} voz="titular" peso={300} color={C2.negro} tracking={3}>NO</Tipo>
            <div style={{height: 14}} />
            <Tipo px={56} voz="titular" color={C2.negro}>ATENDEREMOS…</Tipo>
            <div style={{height: 150}} />
            <Tipo px={30} voz="titular" color={C2.rosa} tracking={7}>05—07.10</Tipo>
          </Cara>
        </div>
      </div>

      {/* La manilla va DELANTE del cartel: se repinta encima el mismo pedazo de foto
          (círculo de 39 px sobre el centro medido). Así el cartel queda enganchado
          detrás del pomo, como en una puerta de verdad. */}
      <AbsoluteFill style={{clipPath: `circle(39px at ${POMO.x}px ${POMO.y}px)`}}>
        <Foto src="assets/copywriters/202610/m1-puerta.png" />
      </AbsoluteFill>

      {/* El remate, cuando el cartel ya giró. */}
      <ManoCurva id="cm1" d="M 70 860 C 220 750, 480 790, 660 730" px={86} texto="…nada que no"
                 desde={GIRA + 26} dura={20} sombra />
      <ManoCurva id="cm2" d="M 70 960 C 250 1040, 470 900, 670 920" px={86} texto="sea el cyber."
                 desde={GIRA + 40} dura={20} sombra />
    </AbsoluteFill>
  );
};
