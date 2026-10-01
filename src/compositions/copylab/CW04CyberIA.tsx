// ============================================================================
// COPYWRITERS · CW-04 — «EN ESTE CYBER, UNA IA TAMBIÉN RECOMIENDA.» · 4 láminas
// ----------------------------------------------------------------------------
// BRIEF     clients/copywriters/briefs/202610_BRIEF_ESTUDIO_copywriters.md (CW-04).
//           Pilar «Tendencias de IA», editorial. Sale miércoles 07-10 · 12:30.
//           Serie INTERNET DEPT. (sin «VOL.» ni fecha).
// RONDA 3   Valeria (01-10): «estos textos planos son feos, parecen de IA, ¿y para
//           qué sirven?» + «en cada gráfica puedes variar, jugar».
//           · FUERA el cuerpo en Neue Haas. La fuente del dato (CCS vía BioBio y The
//             Clinic, 29-09-2026) va al CAPTION, no a la gráfica: le sirve a quien
//             verifica, no a quien mira. La línea de ChatGPT pasa a ser la mano.
//           · La tipografía juega por lámina con los extremos de Bebas Neue Pro:
//             Light 300 finísima contra Expanded ExtraBold, y Bebas en CONTORNO.
//             Balloon corre por curvas (ManoCurva, del kit).
//           · 01 y 02 son video (Kling 2.5 Pro desde las fotos): neblina en el foco,
//             lluvia en la vereda.
//
// IDEA      Una tienda de noche donde nadie atiende y alguien igual elige: entre
//           cientos de cajas iguales, un foco ilumina una sola. Después la tienda que
//           no cierra y la etiqueta del producto, que es lo que esa IA lee.
//           INTERNET DEPT. es un cabezal de papel que corta la foto como página de
//           diario. El tachado de «el mejor del mercado» es el único trazo que cruza
//           la letra a propósito: tachar es el significado (R-26).
// GEOMETRÍA Caja iluminada, vidriera y etiquetas MEDIDAS sobre cada foto (R-33).
// FOTOS     Seedream 5 Pro (raw/copywriters/202610/gen/d1–d4) · video v5, v6.
// Formato 1080×1350 · 30 fps · 150 cuadros (01 y 02 en MP4; 03 y 04 fijas).
// ============================================================================
import React from "react";
import {AbsoluteFill, OffthreadVideo, interpolate, staticFile, useCurrentFrame, Easing} from "remotion";
import {C2, VOZ2, SOMBRA_SOBRE_FOTO, asegurarFuentesV2, granoSVG} from "../../brand/copylab/sistemaV2";
import {Foto, ManoCurva, Trazo} from "../../brand/copylab/piezasV2";

export const CW04_FRAMES = 150;
const M = 76;
const F = (n: string) => `assets/copywriters/202610/${n}`;
const TINTA = "#1B1A19";
const fijo = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;

const Grano: React.FC = () => (
  <AbsoluteFill style={{backgroundImage: granoSVG(0.05, 5), backgroundSize: "300px 300px"}} />
);

const FondoVideo: React.FC<{src: string}> = ({src}) => (
  <OffthreadVideo src={staticFile(src)} muted
    style={{position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover"}} />
);

/**
 * Bebas con todos sus registros. `voz`: titular (ancho normal) · impacto
 * (SemiExpanded) · bloque (Expanded ExtraBold). `peso` 300 = Light finísima.
 * `contorno` deja sólo el trazo: la letra se vuelve dibujo.
 */
const Tipo: React.FC<{
  px: number; voz?: "titular" | "impacto" | "bloque"; peso?: number; color?: string;
  contorno?: number; tracking?: number; sombra?: boolean; children: React.ReactNode;
}> = ({px, voz = "impacto", peso, color = C2.offwhite, contorno = 0, tracking = 0,
       sombra = false, children}) => (
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

const En: React.FC<{x: number; y: number; giro?: number; children: React.ReactNode}> =
({x, y, giro = 0, children}) => (
  <div style={{position: "absolute", left: x, top: y,
               transform: giro ? `rotate(${giro}deg)` : undefined}}>{children}</div>
);

/** Entrada: sube y aparece. */
const Sube: React.FC<{desde: number; children: React.ReactNode}> = ({desde, children}) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [desde, desde + 14], [0, 1], {...fijo, easing: Easing.out(Easing.cubic)});
  return <div style={{opacity: p, transform: `translateY(${(1 - p) * 24}px)`}}>{children}</div>;
};

/** Cabezal de diario: papel con doble filete, sobre la foto. */
const Cabezal: React.FC<{alto: number; grande?: boolean; children?: React.ReactNode}> =
({alto, grande = false, children}) => (
  <div style={{position: "absolute", left: 0, top: 0, width: 1080, height: alto,
               background: C2.offwhite, boxShadow: "0 10px 30px rgba(0,0,0,0.45)"}}>
    <AbsoluteFill style={{backgroundImage: granoSVG(0.1, 11), backgroundSize: "300px 300px"}} />
    <div style={{position: "absolute", left: 0, right: 0, top: grande ? 62 : 46,
                 display: "flex", justifyContent: "center"}}>
      <Tipo px={grande ? 118 : 58} color={C2.negro} tracking={grande ? 2 : 1}>INTERNET DEPT.</Tipo>
    </div>
    {children}
    <div style={{position: "absolute", left: M, right: M, bottom: 30, height: 1.5, background: C2.negro}} />
    <div style={{position: "absolute", left: M, right: M, bottom: 18, height: 5, background: C2.negro}} />
  </div>
);

const Sigue: React.FC<{children: React.ReactNode}> = ({children}) => {
  const f = useCurrentFrame();
  const dx = interpolate(f, [0, CW04_FRAMES], [0, -172]);
  return <AbsoluteFill style={{transform: `translateX(${dx}px)`}}>{children}</AbsoluteFill>;
};

// ====================== 01 · EL FOCO (video) ======================
// Caja iluminada medida: x 574–855 · y 640–800.
const L1: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <FondoVideo src={F("v5-foco.mp4")} />
    <AbsoluteFill style={{
      background: "linear-gradient(0deg, rgba(11,11,11,0.95) 0%, rgba(11,11,11,0.72) 26%, rgba(11,11,11,0) 44%)",
    }} />
    <Grano />
    <Cabezal alto={238} grande />
    {/* La mano cae en curva sobre la caja elegida. La cámara del clip se desliza
        a la izquierda (≈ −35 px/s, MEDIDO sobre la caja): la anotación la sigue. */}
    <Sigue>
      <ManoCurva id="d1a" d="M 760 400 C 900 380, 1010 470, 920 600" px={86} texto="esta."
                 color={C2.offwhite} desde={20} dura={16} sombra />
    </Sigue>
    {/* Tres registros de Bebas en un titular: Light, Expanded, contorno. */}
    <En x={M} y={840}><Sube desde={0}>
      <Tipo px={96} peso={300} voz="titular" tracking={3} sombra>EN ESTE CYBER,</Tipo>
    </Sube></En>
    <En x={M - 8} y={938}><Sube desde={6}>
      <div style={{display: "flex", gap: 30}}>
        <Tipo px={200} voz="bloque" sombra>UNA</Tipo>
        <Tipo px={200} voz="bloque" color={C2.rosa} sombra>IA</Tipo>
      </div>
    </Sube></En>
    <En x={M} y={1124}><Sube desde={12}>
      <Tipo px={96} voz="titular" contorno={2.6} sombra>TAMBIÉN RECOMIENDA.</Tipo>
    </Sube></En>
  </AbsoluteFill>
);

// ====================== 02 · LA TIENDA QUE NO CIERRA (video) ======================
// Vidriera medida: x 227–840 · y 320–880. El papel tapa el letrero blanco.
const L2: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <FondoVideo src={F("v6-tienda.mp4")} />
    <AbsoluteFill style={{
      background: "linear-gradient(0deg, rgba(11,11,11,0.94) 0%, rgba(11,11,11,0.66) 24%, rgba(11,11,11,0) 38%)",
    }} />
    <Grano />
    <Cabezal alto={330}>
      <div style={{position: "absolute", left: M, top: 150}}>
        <Tipo px={104} voz="titular" peso={300} color={C2.negro} tracking={4}>QUÉ PASÓ.</Tipo>
      </div>
    </Cabezal>
    <ManoCurva id="d2a" d="M 72 948 C 250 790, 620 1010, 1010 836" px={64} texto="te dice qué comprar."
               desde={18} dura={22} sombra />
    <En x={M - 10} y={962}><Sube desde={0}>
      <Tipo px={172} voz="bloque" sombra>CYBERAI</Tipo>
    </Sube></En>
    <En x={M} y={1120}><Sube desde={8}>
      <Tipo px={74} voz="titular" peso={300} tracking={10} sombra>ATIENDE 24/7.</Tipo>
    </Sube></En>
  </AbsoluteFill>
);

// ====================== 03 · LA ETIQUETA (fija) ======================
// Etiqueta medida: x 316–744 · y 410–1100 (cuerpo libre bajo el ojal: y 560–1090).
const L3: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Foto src={F("d3.png")} />
    <Grano />
    <Cabezal alto={250}>
      <div style={{position: "absolute", left: M, top: 134}}>
        <Tipo px={80} voz="impacto" contorno={3} color={C2.negro} tracking={2}>POR QUÉ IMPORTA.</Tipo>
      </div>
    </Cabezal>
    <div style={{position: "absolute", left: 330, top: 598, width: 400, transform: "rotate(1deg)"}}>
      <div style={{fontFamily: VOZ2.mano, fontWeight: 800, fontSize: 52, lineHeight: 1.08,
                   color: TINTA, textAlign: "center", textTransform: "uppercase",
                   mixBlendMode: "multiply", opacity: 0.92}}>
        TU FICHA YA<br />NO LA LEE SÓLO<br />UNA PERSONA.
      </div>
      <div style={{height: 34}} />
      <div style={{fontFamily: VOZ2.mano, fontWeight: 800, fontSize: 52, lineHeight: 1.08,
                   color: C2.rosa, textAlign: "center", textTransform: "uppercase"}}>
        LA LEE UNA IA<br />QUE DECIDE QUÉ<br />RECOMENDAR.
      </div>
    </div>
  </AbsoluteFill>
);

// ====================== 04 · LO QUE VA EN LA ETIQUETA (fija) ======================
// Etiqueta medida: centro ≈ (566, 736), 488 × 645, girada −10°.
const L4: React.FC = () => (
  <AbsoluteFill style={{background: C2.negro}}>
    <Foto src={F("d4.png")} />
    <AbsoluteFill style={{
      background: "linear-gradient(0deg, rgba(11,11,11,0.86) 0%, rgba(11,11,11,0.4) 14%, rgba(11,11,11,0) 24%)",
    }} />
    <Grano />
    <Cabezal alto={250}>
      <div style={{position: "absolute", left: M, top: 132, transform: "rotate(-2deg)"}}>
        <div style={{fontFamily: VOZ2.mano, fontWeight: 800, fontSize: 64, color: C2.negro,
                     textTransform: "uppercase"}}>QUÉ HACEMOS.</div>
      </div>
    </Cabezal>
    <div style={{position: "absolute", left: 380, top: 590, width: 420,
                 transform: "rotate(-10deg)", transformOrigin: "50% 50%"}}>
      <div style={{fontFamily: VOZ2.mano, fontWeight: 800, fontSize: 54, lineHeight: 1.1,
                   color: TINTA, textAlign: "center", textTransform: "uppercase",
                   mixBlendMode: "multiply", opacity: 0.92}}>
        QUÉ ES.<br />PARA QUIÉN.<br />PRECIO.<br />STOCK.
      </div>
      <div style={{height: 28}} />
      <div style={{position: "relative"}}>
        {/* Un tachado deja LEER lo que tacha: trazo fino, por el centro de cada línea. */}
        <div style={{fontFamily: VOZ2.mano, fontWeight: 800, fontSize: 44, lineHeight: 1.15,
                     color: TINTA, textAlign: "center", textTransform: "uppercase",
                     mixBlendMode: "multiply", opacity: 0.92}}>«EL MEJOR<br />DEL MERCADO»</div>
        <Trazo x={78} y={2} ancho={264} grosor={8} giro={1} />
        <Trazo x={40} y={53} ancho={340} grosor={8} giro={1} />
      </div>
    </div>
    <ManoCurva id="d4a" d="M 72 1176 C 330 1080, 640 1236, 1010 1112" px={54}
               texto="lo mismo que va a pedir chatgpt." color={C2.offwhite} sombra dura={1} />
  </AbsoluteFill>
);

const LAMINAS = [L1, L2, L3, L4];

export const CW04CyberIA: React.FC<{lamina?: number}> = ({lamina = 1}) => {
  asegurarFuentesV2();
  const L = LAMINAS[Math.min(Math.max(lamina, 1), LAMINAS.length) - 1];
  return <L />;
};
