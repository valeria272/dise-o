/**
 * REEL SAN ESTEBAN · 1080×1920 · 15 s
 *
 * Extiende el sistema estático de septiembre 2026: abanico de 110 años arriba,
 * foto abajo entrando por el arco medido, bloque de identidad (escudo + sello)
 * al centro y barra de CTA azul. Lo único que se anima es el reencuadre lento de
 * la foto y la entrada del texto — la gramática no se mueve.
 *
 * Zonas seguras del brief del cliente para reel: 120 px arriba, 420 px abajo y
 * la columna derecha con los íconos. Todo el texto vive dentro de eso.
 *
 * Manual: clients/san-esteban/CLAUDE.md
 */
import React from "react";
import {
  AbsoluteFill,
  Img,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import {ASSETS, COLORES, FUENTES, ZONAS_REEL} from "../brand/sanesteban";

export const SE_REEL_FPS = 30;
export const SE_REEL_DURACION = 450; // 15 s exactos, el tope del brief

// Fuentes locales con @font-face inyectado (patrón del repo: sin delayRender,
// que es lo que cuelga el render — ver memoria «reel-video-gotchas»).
let seFuentesListas = false;
const cargarFuentes = () => {
  if (seFuentesListas || typeof document === "undefined") return;
  seFuentesListas = true;
  const css = ["Regular:400", "Medium:500", "Bold:700", "ExtraBold:800"]
    .map((par) => {
      const [archivo, peso] = par.split(":");
      return `@font-face{font-family:'Poppins';font-style:normal;font-weight:${peso};
        font-display:block;src:url(${staticFile(
          `assets/fonts/Poppins-${archivo}.ttf`,
        )}) format('truetype');}`;
    })
    .join("\n");
  const style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);
  const f = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (f) ["400", "500", "700", "800"].forEach((w) => f.load(`${w} 40px Poppins`));
};

export type Escena = {
  /** Nombre del archivo en public/assets/san-esteban/fotos (sin extensión). */
  foto?: string;
  /** Desplazamiento horizontal del recorte, 0–100. Nunca se deforma la foto. */
  encuadre?: number;
  /** Desplazamiento vertical, 0–100. Es el que manda en fotos verticales:
   *  ahí no hay sobrante horizontal y el eje X no mueve nada. */
  encuadreY?: number;
  /** El texto en pantalla, verbatim del brief. Máximo 7 palabras. */
  texto: string;
  /** Tarjeta de cierre: sin foto, con el bloque de identidad y el CTA. */
  cierre?: boolean;
  /** Texto de la barra de CTA (sólo en el cierre). */
  cta?: string;
};

export type PropsReel = {
  escenas: Escena[];
};

const FUENTE = FUENTES.display;

/** Bloque de identidad: escudo + sello, siempre juntos y en ese orden. */
const Identidad: React.FC<{y: number; escudo: number}> = ({y, escudo}) => {
  const sello = escudo * 1.46; // proporción medida entre sello y escudo en story
  return (
    <div
      style={{
        position: "absolute",
        top: y,
        left: 0,
        right: 0,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <Img src={ASSETS.escudo} style={{width: escudo, display: "block"}} />
      <Img
        src={ASSETS.sello110}
        style={{width: sello, marginTop: 30, display: "block"}}
      />
    </div>
  );
};

/**
 * La foto ocupa SOLO la banda que se ve bajo el arco (y 830 → 1920).
 * Si ocupara el lienzo completo, `cover` la escalaría al alto total y sólo se
 * vería la franja de abajo — en las primeras pruebas salían piernas y zapatos.
 */
const BANDA_FOTO = {top: 830, alto: 1090};

const Foto: React.FC<{
  nombre: string;
  encuadre: number;
  encuadreY: number;
  duracion: number;
}> = ({nombre, encuadre, encuadreY, duracion}) => {
  const frame = useCurrentFrame();
  // Reencuadre lento: 1.00 -> 1.07. Escala uniforme, la foto NUNCA se deforma.
  const escala = interpolate(frame, [0, duracion], [1, 1.07], {
    extrapolateRight: "clamp",
  });
  return (
    <div
      style={{
        position: "absolute",
        top: BANDA_FOTO.top,
        left: 0,
        width: 1080,
        height: BANDA_FOTO.alto,
        overflow: "hidden",
      }}
    >
      <div
        style={{
          position: "absolute",
          inset: 0,
          backgroundImage: `url(${ASSETS.foto(nombre)})`,
          backgroundSize: "cover",
          backgroundPosition: `${encuadre}% ${encuadreY}%`,
          transform: `scale(${escala})`,
          transformOrigin: "center center",
        }}
      />
    </div>
  );
};

const Titular: React.FC<{texto: string; retraso?: number; sinEntrada?: boolean}> = ({
  texto,
  retraso = 0,
  sinEntrada = false,
}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const p = spring({
    fps,
    frame: frame - retraso,
    config: {damping: 18, stiffness: 130},
  });
  // La PRIMERA escena entra sin animación: el brief del cliente exige que el
  // primer fotograma se lea solo, porque es el que se usa de miniatura.
  const opacidad = sinEntrada ? 1 : interpolate(p, [0, 1], [0, 1]);
  const y = sinEntrada ? 0 : interpolate(p, [0, 1], [34, 0]);
  return (
    <div
      style={{
        position: "absolute",
        top: 190,
        left: 60,
        right: 60 + ZONAS_REEL.right,
        textAlign: "center",
        opacity: opacidad,
        transform: `translateY(${y}px)`,
      }}
    >
      <div
        style={{
          fontFamily: FUENTE,
          fontWeight: 800,
          fontSize: 80,
          lineHeight: 1.0,
          letterSpacing: FUENTES.trackingTitular,
          color: COLORES.blanco,
          textShadow: "0 4px 16px rgba(0,0,0,.34)",
          // líneas parejas y «San Esteban» nunca partido (QA 24-09-2026)
          textWrap: "balance",
        } as React.CSSProperties}
      >
        {texto.replace("San Esteban", "San\u00a0Esteban")}
      </div>
    </div>
  );
};

const BarraCTA: React.FC<{texto: string; retraso: number}> = ({
  texto,
  retraso,
}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const p = spring({
    fps,
    frame: frame - retraso,
    config: {damping: 20, stiffness: 120},
  });
  return (
    <div
      style={{
        position: "absolute",
        top: 1372,
        left: 0,
        right: 0,
        display: "flex",
        justifyContent: "center",
        opacity: interpolate(p, [0, 1], [0, 1]),
        transform: `translateY(${interpolate(p, [0, 1], [26, 0])}px)`,
      }}
    >
      <div
        style={{
          background: COLORES.azulCTA,
          color: COLORES.blanco,
          fontFamily: FUENTE,
          fontWeight: 700,
          fontSize: 46,
          letterSpacing: FUENTES.trackingCaja,
          lineHeight: 1.22,
          padding: "18px 46px",
          borderRadius: 4,
          textAlign: "center",
          maxWidth: 900,
        }}
      >
        {texto}
      </div>
    </div>
  );
};

const Tarjeta: React.FC<{escena: Escena; duracion: number; primera: boolean}> = ({
  escena,
  duracion,
  primera,
}) => {
  return (
    <AbsoluteFill style={{backgroundColor: COLORES.blanco}}>
      {escena.foto ? (
        <Foto
          nombre={escena.foto}
          encuadre={escena.encuadre ?? 50}
          encuadreY={escena.encuadreY ?? 30}
          duracion={duracion}
        />
      ) : null}

      {/* El abanico de 110 años: opaco en su zona, recorta la foto por el arco.
          Es el MISMO gráfico en todas las escenas — la gramática no se mueve. */}
      <Img
        src={ASSETS.abanicoArriba}
        style={{position: "absolute", inset: 0, width: 1080, height: 1920}}
      />

      <Titular texto={escena.texto} retraso={6} sinEntrada={primera} />
      {/* En el reel el bloque de identidad va DENTRO del abanico, no sobre la
          foto: con fotos que cambian cada 3,75 s el escudo caía sobre las caras.
          Termina justo antes del arco (y≈855). */}
      <Identidad y={490} escudo={130} />
      {escena.cta ? <BarraCTA texto={escena.cta} retraso={18} /> : null}
    </AbsoluteFill>
  );
};

export const SanEstebanReel: React.FC<PropsReel> = ({escenas}) => {
  cargarFuentes();
  const {durationInFrames} = useVideoConfig();
  const porEscena = Math.floor(durationInFrames / escenas.length);
  return (
    <AbsoluteFill style={{backgroundColor: COLORES.blanco}}>
      {escenas.map((e, i) => (
        <Sequence
          key={i}
          from={i * porEscena}
          durationInFrames={
            i === escenas.length - 1 ? durationInFrames - i * porEscena : porEscena
          }
        >
          <Tarjeta escena={e} duracion={porEscena} primera={i === 0} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
