// ============================================================================
// COPYWRITERS — Kit gráfico del Sistema Visual (29-09-2026)
// ----------------------------------------------------------------------------
// Las piezas del board que se repiten entre composiciones: los trazos a mano,
// la cinta, el papel, el rótulo mono y el fondo con grano.
//
// Esto NO es una plantilla: no compone nada ni decide jerarquía. Es el kit de
// herramientas. Cada pieza sigue siendo un archivo con su dirección de arte.
//
// ⛔ El subrayado va SIEMPRE bajo la línea de base, nunca sobre la letra:
//    cruzando la palabra deja de ser subrayado y se lee como TACHADO. Y cambiar
//    el peso del titular obliga a recalibrarlo — Bebas Neue Pro Bold tiene más
//    altura de caja que la Bebas libre.
// ============================================================================
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {C2, VOZ2, granoSVG, pathSubrayado, pathsFlecha} from "./sistemaV2";

/** Subrayado de marcador. Un solo trazo por debajo de la palabra que manda. */
export const Subrayado: React.FC<{
  x: number; y: number; ancho: number; alto?: number; color?: string;
  grosor?: number; giro?: number;
}> = ({x, y, ancho, alto = 34, color = C2.rosa, grosor = 13, giro = 0}) => (
  <svg
    width={ancho} height={alto}
    style={{position: "absolute", left: x, top: y, overflow: "visible",
            transform: giro ? `rotate(${giro}deg)` : undefined}}
  >
    <path d={pathSubrayado(ancho, alto)} stroke={color} strokeWidth={grosor}
          strokeLinecap="round" fill="none" />
  </svg>
);

/** Flecha de anotación: cuerpo curvo + dos plumas. Nunca un icono. */
export const Flecha: React.FC<{
  x: number; y: number; ancho: number; alto: number; giro?: number;
  color?: string; grosor?: number;
}> = ({x, y, ancho, alto, giro = 0, color = C2.rosa, grosor = 9}) => {
  const p = pathsFlecha(ancho, alto);
  return (
    <svg width={ancho} height={alto}
         style={{position: "absolute", left: x, top: y, overflow: "visible",
                 transform: `rotate(${giro}deg)`}}>
      {[p.cuerpo, p.pluma1, p.pluma2].map((d, i) => (
        <path key={i} d={d} stroke={color} strokeWidth={grosor}
              strokeLinecap="round" fill="none" />
      ))}
    </svg>
  );
};

/** Cinta adhesiva: translúcida, girada, con los bordes irregulares. */
export const Cinta: React.FC<{
  x: number; y: number; ancho: number; alto: number; giro: number; color?: string;
}> = ({x, y, ancho, alto, giro, color = "rgba(184,184,184,0.62)"}) => (
  <div style={{
    position: "absolute", left: x, top: y, width: ancho, height: alto,
    background: color, backgroundImage: granoSVG(0.24, 3),
    transform: `rotate(${giro}deg)`,
    clipPath: "polygon(2% 6%, 99% 0%, 98% 94%, 1% 100%)",
    boxShadow: "0 2px 10px rgba(0,0,0,0.3)",
  }} />
);

/** Sticker: rectángulo rosa levemente girado. Caja alta, siempre. */
export const Sticker: React.FC<{
  x: number; y: number; giro?: number; cuerpo?: number; children: React.ReactNode;
}> = ({x, y, giro = -3, cuerpo = 38, children}) => (
  <div style={{
    position: "absolute", left: x, top: y, background: C2.rosa,
    padding: `${cuerpo * 0.34}px ${cuerpo * 0.62}px`,
    transform: `rotate(${giro}deg)`,
    fontFamily: VOZ2.titular, fontWeight: 700, fontSize: cuerpo,
    color: C2.negro, textTransform: "uppercase", letterSpacing: 1,
    whiteSpace: "nowrap", boxShadow: "0 6px 22px rgba(0,0,0,0.35)",
  }}>{children}</div>
);

/** Hoja de papel: el soporte de la voz baja. */
export const Papel: React.FC<{
  x: number; y: number; ancho: number; alto: number; giro: number;
  children: React.ReactNode;
}> = ({x, y, ancho, alto, giro, children}) => (
  <div style={{
    position: "absolute", left: x, top: y, width: ancho, height: alto,
    background: C2.offwhite, backgroundImage: granoSVG(0.1, 11),
    transform: `rotate(${giro}deg)`, boxShadow: "0 28px 70px rgba(0,0,0,0.55)",
  }}>{children}</div>
);

/** Rótulo mono. Metadata, índice, volumen. Nunca es héroe. */
export const Rotulo: React.FC<{
  texto: string; x: number; y: number; color?: string; cuerpo?: number;
}> = ({texto, x, y, color = C2.gris, cuerpo = 21}) => (
  <div style={{
    position: "absolute", left: x, top: y,
    fontFamily: VOZ2.data, fontSize: cuerpo, fontWeight: 500,
    letterSpacing: cuerpo * 0.16, color, textTransform: "uppercase",
    whiteSpace: "nowrap",
  }}>{texto}</div>
);

/** Una línea de titular. Bebas Neue Pro, caja alta, peso declarado. */
export const Linea: React.FC<{
  children: React.ReactNode; cuerpo: number; color?: string; peso?: number;
}> = ({children, cuerpo, color = C2.offwhite, peso = 700}) => (
  <div style={{
    fontFamily: VOZ2.titular, fontWeight: peso, fontSize: cuerpo,
    lineHeight: 0.86, color, textTransform: "uppercase", letterSpacing: 0,
    whiteSpace: "nowrap",
  }}>{children}</div>
);

/** La mano. Balloon URW, CAJA ALTA siempre — así está en las 15 tarjetas
 *  de la grilla del board. Balloon ya viene inclinada: no girarla más de 2°. */
export const Mano: React.FC<{
  x: number; y: number; cuerpo: number; color?: string; giro?: number;
  alineacion?: "left" | "right"; interlineado?: number; children: React.ReactNode;
}> = ({x, y, cuerpo, color = C2.rosa, giro = -2, alineacion = "left",
       interlineado = 1.12, children}) => (
  <div style={{
    position: "absolute", left: x, top: y,
    fontFamily: VOZ2.mano, fontWeight: 700, fontSize: cuerpo, color,
    lineHeight: interlineado, transform: `rotate(${giro}deg)`,
    textTransform: "uppercase", textAlign: alineacion,
  }}>{children}</div>
);

/** Fondo negro con grano editorial. */
export const FondoNegro: React.FC<{children: React.ReactNode}> = ({children}) => (
  <AbsoluteFill style={{background: C2.negro}}>
    <AbsoluteFill style={{backgroundImage: granoSVG(0.055, 5),
                          backgroundSize: "300px 300px"}} />
    {children}
  </AbsoluteFill>
);

/**
 * Fotografía a sangre.
 *
 * ⛔ `cover` recorta; NUNCA estira. Estirar para llenar un formato es el defecto
 * que dejó rayas verticales en el 34 % de una story de Revex. Si la foto no da
 * el formato, se recorta bien, se busca otra o se dice que falta — no se estira.
 *
 * `foco` decide QUÉ se conserva al recortar (las de Seedream salen 3:4 y hay que
 * quitarles alto para llegar a 4:5).
 */
export const Foto: React.FC<{
  src: string; foco?: string; oscurecer?: number;
}> = ({src, foco = "center", oscurecer = 0}) => (
  <>
    <Img src={staticFile(src)}
         style={{position: "absolute", inset: 0, width: "100%", height: "100%",
                 objectFit: "cover", objectPosition: foco}} />
    {oscurecer > 0 && (
      <AbsoluteFill style={{background: `rgba(11,11,11,${oscurecer})`}} />
    )}
  </>
);
