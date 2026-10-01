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
import {AbsoluteFill, Easing, Img, interpolate, staticFile, useCurrentFrame} from "remotion";
import {C2, VOZ2, SOMBRA_SOBRE_FOTO, granoSVG, pathSubrayado,
        pathTrazoGrueso, pathsFlecha} from "./sistemaV2";

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

/**
 * Trazo grueso de plumón — el subrayado de la referencia del 30-09.
 *
 * Va como ÁREA, no como línea: un plumón real deja la marca ancha en el medio
 * y afilada en las puntas. Un trazo de grosor parejo se lee como un `border`.
 */
export const Trazo: React.FC<{
  x: number; y: number; ancho: number; grosor?: number; color?: string;
  giro?: number;
}> = ({x, y, ancho, grosor = 22, color = C2.rosa, giro = -1}) => (
  <svg
    width={ancho} height={grosor * 2.6}
    style={{position: "absolute", left: x, top: y, overflow: "visible",
            transform: `rotate(${giro}deg)`}}
  >
    <path d={pathTrazoGrueso(ancho, grosor * 2.6, grosor)} fill={color} />
  </svg>
);

/**
 * Una línea de titular.
 *
 * `voz` decide el ancho, y no es decoración: la referencia del 30-09 NO es
 * condensada. Un KPI en el ancho normal se lee flaco y pierde presencia.
 *   · `impacto` (SemiExpanded) — titulares y KPI. El de uso corriente.
 *   · `bloque`  (Expanded ExtraBold) — cuando el número ES la pieza.
 *   · `titular` (ancho normal) — sólo para líneas largas que deben caber.
 */
export const Linea: React.FC<{
  children: React.ReactNode; cuerpo: number; color?: string; peso?: number;
  voz?: "impacto" | "bloque" | "titular"; sombra?: boolean; tracking?: number;
}> = ({children, cuerpo, color = C2.offwhite, peso = 800, voz = "impacto",
       sombra = false, tracking = 0}) => (
  <div style={{
    fontFamily: VOZ2[voz], fontWeight: voz === "titular" ? 700 : peso,
    fontSize: cuerpo, lineHeight: 0.84, color, textTransform: "uppercase",
    letterSpacing: tracking, whiteSpace: "nowrap",
    textShadow: sombra ? SOMBRA_SOBRE_FOTO : undefined,
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
    fontFamily: VOZ2.mano, fontWeight: 800, fontSize: cuerpo, color,
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
  src: string; foco?: string; oscurecer?: number; zoom?: number;
}> = ({src, foco = "center", oscurecer = 0, zoom = 1}) => (
  <>
    <Img src={staticFile(src)}
         style={{position: "absolute", inset: 0, width: "100%", height: "100%",
                 objectFit: "cover", objectPosition: foco,
                 transform: zoom === 1 ? undefined : `scale(${zoom})`,
                 transformOrigin: foco}} />
    {oscurecer > 0 && (
      <AbsoluteFill style={{background: `rgba(11,11,11,${oscurecer})`}} />
    )}
  </>
);

/**
 * LA MANO CON CURVA — Balloon corriendo por un trazado (textPath).
 *
 * Nació con la ronda 3 de CW-01 (01-10-2026, Valeria: «dale curvas, intención»).
 * Se ESCRIBE: una máscara barre el trazado de izquierda a derecha entre `desde` y
 * `desde + dura` (con dura = 1 queda escrita desde el primer cuadro: piezas fijas).
 * ⚠️ El trazado tiene que ser MÁS LARGO que el texto: lo que sobra se corta.
 */
export const ManoCurva: React.FC<{
  id: string; d: string; px: number; texto: string; color?: string;
  desde?: number; dura?: number; sombra?: boolean;
}> = ({id, d, px, texto, color = C2.rosa, desde = 0, dura = 22, sombra = false}) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [desde, desde + dura], [0, 1],
    {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  return (
    <svg width={1080} height={1350} viewBox="0 0 1080 1350"
         style={{position: "absolute", left: 0, top: 0, overflow: "visible",
                 filter: sombra ? "drop-shadow(0 5px 14px rgba(0,0,0,0.6))" : undefined}}>
      <defs>
        <path id={id} d={d} />
        <clipPath id={`${id}-m`}><rect x={-200} y={-200} width={1480 * p} height={1750} /></clipPath>
      </defs>
      <text clipPath={`url(#${id}-m)`} fill={color}
            style={{fontFamily: VOZ2.mano, fontWeight: 800, fontSize: px, textTransform: "uppercase"}}>
        <textPath href={`#${id}`}>{texto}</textPath>
      </text>
    </svg>
  );
};
