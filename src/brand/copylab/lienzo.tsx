// ============================================================================
// COPYWRITERS — lienzo y tratamiento fotográfico
// ----------------------------------------------------------------------------
// El tratamiento de imagen es UNA de las siete columnas que sostienen la
// consistencia (COPYWRITERS_CREATIVE_OS §1). Por eso vive acá y no dentro de
// cada pieza: dos fotos de universos distintos tienen que sentirse de la misma
// cuenta aunque una sea un packshot de vino y la otra un escritorio en B&N.
//
// Lo que NO hay acá, a propósito: gradientes decorativos, halos, glassmorphism,
// sombras difusas de card, viñetas automáticas. Están prohibidos en tokens.json.
// El único degradado permitido es el VELO, y sólo cuando hay que poder LEER
// sobre una foto — es una función, no un adorno.
// ============================================================================
import React from "react";
import {AbsoluteFill, Img, useVideoConfig} from "remotion";
import {C, src} from "./sistema";

// ---------------------------------------------------------------------------
// Texturas
// ---------------------------------------------------------------------------

/** Grano de película. Lo que separa un plano digital perfecto —que huele a
 *  render— de una imagen que parece haber pasado por una cámara. */
export const Grano: React.FC<{op?: number; escala?: number; mezcla?: "overlay" | "soft-light"}> = ({
  op = 0.3, escala = 1, mezcla = "overlay",
}) => (
  <div
    style={{
      position: "absolute", inset: 0, pointerEvents: "none",
      backgroundImage: `url(${src("assets/copylab/textura/grano.png")})`,
      backgroundSize: `${512 * escala}px ${512 * escala}px`,
      backgroundRepeat: "repeat",
      opacity: op, mixBlendMode: mezcla,
    }}
  />
);

/** Fibra de papel. Para las piezas en off-white, donde el grano de película
 *  sería mentira: ahí el referente es una hoja impresa, no un negativo. */
export const Papel: React.FC<{op?: number}> = ({op = 0.5}) => (
  <div
    style={{
      position: "absolute", inset: 0, pointerEvents: "none",
      backgroundImage: `url(${src("assets/copylab/textura/papel.png")})`,
      backgroundSize: "768px 768px", backgroundRepeat: "repeat",
      opacity: op, mixBlendMode: "multiply",
    }}
  />
);

// ---------------------------------------------------------------------------
// El lienzo
// ---------------------------------------------------------------------------

export const Pieza: React.FC<{
  fondo?: string;
  /** Grano de película. `false` para las piezas 100% tipográficas sobre color plano. */
  grano?: number | false;
  papel?: number | false;
  children: React.ReactNode;
}> = ({fondo = C.tinta, grano = 0.26, papel = false, children}) => (
  <AbsoluteFill style={{background: fondo, overflow: "hidden"}}>
    {children}
    {papel !== false ? <Papel op={papel} /> : null}
    {grano !== false ? <Grano op={grano} /> : null}
  </AbsoluteFill>
);

// ---------------------------------------------------------------------------
// Fotografía
// ---------------------------------------------------------------------------

/**
 * Los grados. No son "filtros bonitos": son las cuatro maneras en que esta
 * marca mira una imagen, y cada familia de contenido tiene la suya.
 *
 *   editorial → METÁFORA y WORK. Contraste alto, saturación bajada, negros densos.
 *   flash     → PEOPLE. B&N duro de flash directo, como una foto de prensa.
 *   frio      → cuando la imagen aporta clima y el protagonista es el texto.
 *   crudo     → cuando la imagen ya viene gradada (packshot aprobado del cliente).
 */
export const GRADOS = {
  editorial: "contrast(1.16) saturate(0.82) brightness(0.94)",
  flash: "grayscale(1) contrast(1.42) brightness(0.98)",
  frio: "grayscale(0.55) contrast(1.1) brightness(0.8)",
  crudo: "none",
} as const;

export type Grado = keyof typeof GRADOS;

export const Foto: React.FC<{
  src: string;
  grado?: Grado;
  /** Encuadre. `objectPosition` de CSS: "50% 50%", "left top"… */
  encuadre?: string;
  ajuste?: "cover" | "contain";
  /** Escala > 1 para forzar un recorte más cerrado. El recorte inesperado es
   *  parte del lenguaje: una foto centrada y completa es una foto de stock. */
  zoom?: number;
  dx?: number;
  dy?: number;
  op?: number;
  style?: React.CSSProperties;
}> = ({src: s, grado = "editorial", encuadre = "50% 50%", ajuste = "cover",
       zoom = 1, dx = 0, dy = 0, op = 1, style}) => (
  <AbsoluteFill style={{overflow: "hidden", ...style}}>
    <Img
      src={src(s)}
      style={{
        width: "100%", height: "100%", objectFit: ajuste, objectPosition: encuadre,
        filter: GRADOS[grado], opacity: op,
        transform: zoom !== 1 || dx || dy ? `scale(${zoom}) translate(${dx}px, ${dy}px)` : undefined,
      }}
    />
  </AbsoluteFill>
);

/**
 * VELO. Existe para una sola cosa: que el texto se LEA sobre la foto.
 * No es ambientación. Si la pieza necesita un velo al 90% para funcionar,
 * la foto elegida está mala — se cambia la foto, no se sube el velo.
 */
export const Velo: React.FC<{
  desde?: "arriba" | "abajo" | "izquierda";
  fuerza?: number;
  corte?: number;
  color?: string;
}> = ({desde = "abajo", fuerza = 0.88, corte = 0.42, color = C.tinta}) => {
  const rgb = (o: number) => {
    const h = color.replace("#", "");
    const n = parseInt(h, 16);
    return `rgba(${(n >> 16) & 255},${(n >> 8) & 255},${n & 255},${o})`;
  };
  const ejes = {
    abajo: `180deg, ${rgb(0)} 0%, ${rgb(0)} ${corte * 100}%, ${rgb(fuerza)} 100%`,
    arriba: `0deg, ${rgb(0)} 0%, ${rgb(0)} ${corte * 100}%, ${rgb(fuerza)} 100%`,
    izquierda: `90deg, ${rgb(fuerza)} 0%, ${rgb(0)} ${(1 - corte) * 100}%`,
  };
  return <div style={{position: "absolute", inset: 0, background: `linear-gradient(${ejes[desde]})`}} />;
};

/** CORTE. Un bloque macizo que parte el lienzo. El gesto de "composición
 *  partida": no es un contenedor, es una decisión de composición. */
export const Corte: React.FC<{
  color?: string;
  desde?: number; hasta?: number;
  eje?: "y" | "x";
  rot?: number;
}> = ({color = C.rosa, desde = 0, hasta = 0.5, eje = "y", rot = 0}) => (
  <div
    style={{
      position: "absolute",
      ...(eje === "y"
        ? {left: 0, right: 0, top: `${desde * 100}%`, height: `${(hasta - desde) * 100}%`}
        : {top: 0, bottom: 0, left: `${desde * 100}%`, width: `${(hasta - desde) * 100}%`}),
      background: color,
      transform: rot ? `rotate(${rot}deg) scale(1.2)` : undefined,
    }}
  />
);

/** Filete. Una línea de 2 px que ordena sin dibujar una retícula visible. */
export const Filo: React.FC<{
  x?: number; y?: number; largo: number; eje?: "x" | "y";
  color?: string; grosor?: number; op?: number;
}> = ({x = 0, y = 0, largo, eje = "x", color = C.offwhite, grosor = 2, op = 0.22}) => (
  <div
    style={{
      position: "absolute", left: x, top: y, opacity: op, background: color,
      ...(eje === "x" ? {width: largo, height: grosor} : {width: grosor, height: largo}),
    }}
  />
);

/** Overlay de QA: dibuja dónde Meta tapa la pieza con su interfaz.
 *  Nunca se exporta encendido — es para mirar, no para entregar. */
export const ZonaSegura: React.FC<{formato?: "story" | "feed"}> = ({formato = "story"}) => {
  const {width: W, height: H} = useVideoConfig();
  const z = formato === "story"
    ? {arriba: 250, abajo: 340, derecha: 115}
    : {arriba: 0, abajo: 135, derecha: 0};
  const k = W / 1080;
  const rojo = "rgba(255,45,141,0.22)";
  return (
    <>
      <div style={{position: "absolute", left: 0, right: 0, top: 0, height: z.arriba * k, background: rojo}} />
      <div style={{position: "absolute", left: 0, right: 0, bottom: 0, height: z.abajo * k, background: rojo}} />
      <div style={{position: "absolute", top: 0, bottom: 0, right: 0, width: z.derecha * k, background: rojo}} />
      <div style={{position: "absolute", inset: 0, border: `${2 * k}px dashed rgba(255,45,141,0.5)`}} />
      <div style={{position: "absolute", left: 8, top: 8, color: "#fff", fontSize: 20 * k, fontFamily: "monospace"}}>
        {`ZONA SEGURA ${formato.toUpperCase()} · ${W}×${H}`}
      </div>
    </>
  );
};
