// ============================================================================
// COPYLAB — la pieza del feed según el MASTER SYSTEM v1.0
// ----------------------------------------------------------------------------
// Reemplaza a GclPost, que era del sistema anterior. Las diferencias no son
// cosméticas, son de criterio:
//
//   · No hay firma automática. El master dice que el logo NO va por inercia en
//     toda pieza: «el feed completo ya construye la marca».
//   · No hay gradiente de fondo por defecto, ni partículas, ni cajas, ni
//     botones falsos, ni flechas decorativas.
//   · El rosado nunca decora. Entra como intervención —circula, subraya,
//     tacha, mide— o no entra.
//   · Dos colores por pieza. Tres si hay una razón.
//   · El vacío es parte del diseño: acá NO se rellena.
//
// Cuatro voces tipográficas con trabajos distintos: `display` (Archivo
// apretado) afirma, `editorial` (DM Serif itálica) opina, `sans` (Inter)
// informa, `mono` (IBM Plex) rotula. La manuscrita es la mano al margen.
//
// Render:
//   npx remotion still GclPieza out/gcl/p.png --props='{...}'
// ============================================================================
import React from "react";
import {AbsoluteFill, Img, useVideoConfig, staticFile} from "remotion";
import {C, EDITORIAL, SANS, narrow, asegurarFuentesGcl} from "../../brand/gcl";
import {Circulo, Subrayado, Tachado, Flecha, Nota, Rotulo} from "../../brand/gclMarcas";

/** Los layouts salen de las piezas de referencia aprobadas por Valeria. Cada
 *  uno es una forma distinta de decir una sola cosa — nunca un contenedor
 *  genérico al que se le cambia el relleno. */
export type GclLayout =
  | "declaracion"  // fondo plano, display enorme + segunda voz en serif itálica
  | "dato"         // una cifra a toda página con su curva o su barra
  | "obra"         // trabajo de cliente: foto full bleed, rótulo mínimo
  | "campo";       // FIELD NOTES: el dato dibujado, con la lectura al lado

export type GclPiezaProps = {
  layout: GclLayout;
  /** Rótulo de sección: pilar + detalle. «SEÑAL» / «025», «WORK» / «MY ZOO». */
  pilar: string;
  detalle?: string;
  /** La afirmación, en display. Puede ser enorme; puede salirse. */
  titular?: string;
  /** La segunda voz, en DM Serif itálica. El contrapunto humano. */
  contrapunto?: string;
  /** Info funcional, en Inter. Corta. */
  bajada?: string;
  cifra?: string;
  unidad?: string;
  fuente?: string;
  foto?: string;
  /** Nota manuscrita al margen + a dónde apunta su flecha. */
  nota?: string;
  /** Qué palabra del titular se interviene, y con qué verbo. La intervención va
   *  UNA por pieza: dos ya no marcan nada. */
  marca?: {
    verbo: "circular" | "subrayar" | "tachar";
    /** Posición y tamaño en fracción del lienzo (0-1), medidos sobre la palabra. */
    x: number; y: number; ancho: number; alto?: number;
  };
  /** Fondo: tinta (negro), rosado, papel (claro) o grafito. */
  fondo?: "tinta" | "rosado" | "papel" | "grafito";
  /** Color del acento cuando no es el rosado (en pieza rosada, es la tinta). */
  acento?: string;
};

/** Nota manuscrita + la flecha que la ata a lo que señala. En la referencia
 *  nunca aparece una sin la otra: una nota suelta es una frase más, no una
 *  anotación sobre algo. */
const NotaAlMargen: React.FC<{
  texto: string; x: number; y: number; tam: number; ancho: number;
  color: string; hacia?: "abajo-izq" | "abajo-der";
}> = ({texto, x, y, tam, ancho, color, hacia = "abajo-izq"}) => (
  <>
    <Nota texto={texto} x={x} y={y} tam={tam} color={color} ancho={ancho} />
    <Flecha
      x={hacia === "abajo-izq" ? x - tam * 0.2 : x + ancho * 0.5}
      y={y + tam * 2}
      ancho={tam * 1.5}
      alto={tam * 1.7}
      giro={hacia === "abajo-izq"}
      color={color}
      grosor={tam * 0.1}
    />
  </>
);

const FONDOS = {
  tinta: C.tinta, rosado: C.rosado, papel: C.papel, grafito: C.grafito,
} as const;

/** El titular se encoge según el largo. Un display que se desborda arruina la
 *  pieza y quien escribe el copy no debería contar caracteres. */
const escala = (texto: string, base: number, corte = 26) => {
  const n = texto.length;
  if (n <= corte) return base;
  if (n <= corte * 1.7) return base * 0.8;
  if (n <= corte * 2.6) return base * 0.63;
  return base * 0.5;
};

export const GclPieza: React.FC<GclPiezaProps> = ({
  layout, pilar, detalle, titular, contrapunto, bajada, cifra, unidad, fuente,
  foto, nota, marca, fondo = "tinta", acento,
}) => {
  asegurarFuentesGcl();
  const {width: W, height: H} = useVideoConfig();
  const M = Math.round(W * 0.075);
  const bg = FONDOS[fondo];
  // Sobre rosado o papel la tinta es el contraste; sobre tinta o grafito, el
  // blanco. Nunca los cuatro colores a la vez.
  const claro = fondo === "tinta" || fondo === "grafito";
  const tinta = claro ? C.blanco : C.tinta;
  const A = acento || (fondo === "rosado" ? C.tinta : C.rosado);
  const suave = claro ? "rgba(255,255,255,0.6)" : "rgba(8,15,20,0.58)";

  const laMarca = marca ? (() => {
    const px = {x: marca.x * W, y: marca.y * H, ancho: marca.ancho * W};
    if (marca.verbo === "circular") {
      return <Circulo {...px} alto={(marca.alto ?? 0.075) * H} color={A} grosor={W * 0.008} />;
    }
    if (marca.verbo === "tachar") return <Tachado {...px} color={A} grosor={W * 0.008} />;
    return <Subrayado {...px} color={A} grosor={W * 0.007} />;
  })() : null;

  // ------------------------------------------------------------- declaracion
  // La SEÑAL. Una afirmación en display y una respuesta en serif itálica. Nada
  // más: ni logo, ni CTA, ni caja. La portada no explica, provoca.
  if (layout === "declaracion") {
    return (
      <AbsoluteFill style={{background: bg, overflow: "hidden"}}>
        {foto ? (
          <>
            <Img
              src={/^https?:\/\//.test(foto) ? foto : staticFile(foto)}
              style={{width: "100%", height: "100%", objectFit: "cover"}}
            />
            <div style={{
              position: "absolute", inset: 0,
              background: "linear-gradient(180deg, rgba(8,15,20,0.72) 0%, rgba(8,15,20,0.18) 55%, rgba(8,15,20,0.8) 100%)",
            }} />
          </>
        ) : null}

        <div style={{position: "absolute", left: M, top: M}}>
          <Rotulo pilar={pilar} detalle={detalle} color={claro || foto ? "rgba(255,255,255,0.6)" : "rgba(8,15,20,0.5)"} acento={foto ? C.rosado : A} tam={W * 0.02} />
        </div>

        <div style={{position: "absolute", left: M, right: M, top: H * 0.17}}>
          {titular ? (
            <div style={{
              ...narrow(900, 68),
              color: foto ? C.blanco : tinta,
              fontSize: escala(titular, W * 0.175, 22),
              lineHeight: 0.9, letterSpacing: "-0.015em", textTransform: "uppercase",
            }}>
              {titular}
            </div>
          ) : null}
          {contrapunto ? (
            <div style={{
              fontFamily: EDITORIAL, fontStyle: "italic", fontWeight: 400,
              color: fondo === "rosado" ? C.tinta : C.rosado,
              fontSize: escala(contrapunto, W * 0.142, 24),
              lineHeight: 1.0, marginTop: H * 0.018, letterSpacing: "-0.01em",
            }}>
              {contrapunto}
            </div>
          ) : null}
          {bajada ? (
            <div style={{
              fontFamily: SANS, fontWeight: 400, color: foto ? "rgba(255,255,255,0.8)" : suave,
              fontSize: W * 0.028, lineHeight: 1.45, marginTop: H * 0.035, maxWidth: W * 0.7,
            }}>
              {bajada}
            </div>
          ) : null}
        </div>

        {laMarca}
        {nota ? <NotaAlMargen texto={nota} x={W * 0.63} y={H * 0.05} tam={W * 0.042} ancho={W * 0.28} color={foto ? C.rosado : A} hacia="abajo-izq" /> : null}
      </AbsoluteFill>
    );
  }

  // -------------------------------------------------------------------- dato
  // PROOF. La cifra manda y ocupa el lienzo. La fuente va SIEMPRE: una agencia
  // que publica números sin decir de dónde salen no puede vender medición.
  if (layout === "dato") {
    return (
      <AbsoluteFill style={{background: bg, overflow: "hidden"}}>
        <div style={{position: "absolute", left: M, top: M}}>
          <Rotulo pilar={pilar} detalle={detalle} color={claro ? "rgba(255,255,255,0.6)" : "rgba(8,15,20,0.5)"} acento={A} tam={W * 0.02} />
        </div>

        <div style={{position: "absolute", left: M, right: M, top: H * 0.26}}>
          <div style={{display: "flex", alignItems: "flex-end", gap: W * 0.015}}>
            <span style={{
              ...narrow(900, 82), color: tinta,
              fontSize: cifra && cifra.length > 5 ? W * 0.28 : W * 0.36,
              lineHeight: 0.82, letterSpacing: "-0.03em",
            }}>
              {cifra}
            </span>
            {unidad ? (
              <span style={{
                ...narrow(800, 88), color: tinta, fontSize: W * 0.075,
                lineHeight: 1, paddingBottom: W * 0.03, textTransform: "uppercase",
              }}>
                {unidad}
              </span>
            ) : null}
          </div>
          {titular ? (
            <div style={{
              fontFamily: SANS, fontWeight: 500, color: tinta, marginTop: H * 0.012,
              fontSize: W * 0.036, letterSpacing: 3, textTransform: "uppercase",
            }}>
              {titular}
            </div>
          ) : null}
          {contrapunto ? (
            <div style={{
              fontFamily: EDITORIAL, fontStyle: "italic", color: tinta,
              fontSize: W * 0.062, lineHeight: 1.15, marginTop: H * 0.05, maxWidth: W * 0.72,
            }}>
              {contrapunto}
            </div>
          ) : null}
        </div>

        {fuente ? (
          <div style={{
            position: "absolute", left: M, bottom: M,
            fontFamily: SANS, fontSize: W * 0.021, color: suave, letterSpacing: 0.4,
          }}>
            {fuente}
          </div>
        ) : null}
        {laMarca}
      </AbsoluteFill>
    );
  }

  // -------------------------------------------------------------------- obra
  // WORK. La foto del cliente ocupa todo y NO se le encima plantilla Copylab:
  // sólo el rótulo. Si el trabajo es bueno, se muestra.
  if (layout === "obra") {
    return (
      <AbsoluteFill style={{background: C.tinta, overflow: "hidden"}}>
        {foto ? (
          <Img
            src={/^https?:\/\//.test(foto) ? foto : staticFile(foto)}
            style={{width: "100%", height: "100%", objectFit: "cover"}}
          />
        ) : null}
        {/* Velo sólo donde hay texto. Un velo parejo apaga la foto del cliente. */}
        <div style={{
          position: "absolute", inset: 0,
          background: "linear-gradient(180deg, rgba(8,15,20,0.55) 0%, rgba(8,15,20,0) 38%, rgba(8,15,20,0) 62%, rgba(8,15,20,0.72) 100%)",
        }} />
        <div style={{position: "absolute", left: M, top: M}}>
          <Rotulo pilar={pilar} detalle={detalle} color="rgba(255,255,255,0.72)" acento={C.blanco} tam={W * 0.02} />
        </div>
        <div style={{position: "absolute", left: M, right: M, bottom: M * 1.2}}>
          {titular ? (
            <div style={{
              ...narrow(900, 76), color: C.blanco,
              fontSize: escala(titular, W * 0.13, 24), lineHeight: 0.92,
              textTransform: "uppercase", letterSpacing: "-0.015em",
            }}>
              {titular}
            </div>
          ) : null}
          {contrapunto ? (
            <div style={{
              fontFamily: EDITORIAL, fontStyle: "italic", color: C.blanco,
              fontSize: escala(contrapunto, W * 0.105, 26), lineHeight: 1.04, marginTop: H * 0.008,
            }}>
              {contrapunto}
            </div>
          ) : null}
        </div>
        {laMarca}
        {nota ? <NotaAlMargen texto={nota} x={W * 0.07} y={H * 0.13} tam={W * 0.042} ancho={W * 0.32} color={C.rosado} hacia="abajo-der" /> : null}
      </AbsoluteFill>
    );
  }

  // ------------------------------------------------------------------- campo
  // FIELD NOTES. El dato DIBUJADO —la curva es el rosado midiendo, que es uno
  // de los verbos del sistema— y la lectura al lado, no debajo.
  const cx = M;
  const cw = W - M * 2;
  const cy = H * 0.5;
  const ch = H * 0.24;
  // Curva descendente con un rebote: es una serie real de CPC, no un adorno.
  const pts = [0, 0.22, 0.14, 0.46, 0.38, 0.68, 0.6, 0.86, 1];
  const d = pts
    .map((v, i) => {
      const x = cx + (cw * i) / (pts.length - 1);
      const y = cy + ch * v;
      return `${i === 0 ? "M" : "L"} ${x.toFixed(1)} ${y.toFixed(1)}`;
    })
    .join(" ");
  const fx = cx + cw;
  const fy = cy + ch;

  return (
    <AbsoluteFill style={{background: bg, overflow: "hidden"}}>
      <div style={{position: "absolute", left: M, top: M}}>
        <Rotulo pilar={pilar} detalle={detalle} color={claro ? "rgba(255,255,255,0.6)" : "rgba(8,15,20,0.5)"} acento={A} tam={W * 0.02} />
      </div>

      <div style={{position: "absolute", left: M, right: M, top: H * 0.2, display: "flex", alignItems: "flex-start", gap: W * 0.05}}>
        {titular ? (
          <div style={{
            fontFamily: EDITORIAL, fontStyle: "italic", color: tinta,
            fontSize: escala(titular, W * 0.115, 20), lineHeight: 0.98, flex: "0 1 auto",
          }}>
            {titular}
          </div>
        ) : null}
        {bajada ? (
          <div style={{
            fontFamily: SANS, fontWeight: 400, color: claro ? "rgba(255,255,255,0.78)" : suave,
            fontSize: W * 0.032, lineHeight: 1.38, maxWidth: W * 0.3, paddingTop: H * 0.012,
          }}>
            {bajada}
          </div>
        ) : null}
      </div>

      {/* La medición. Sin ejes ni grilla: la forma de la curva es el dato. */}
      <svg width={W} height={H} style={{position: "absolute", inset: 0, overflow: "visible"}}>
        <path d={d} fill="none" stroke={A} strokeWidth={W * 0.009} strokeLinecap="round" strokeLinejoin="round" />
        <circle cx={fx} cy={fy} r={W * 0.016} fill={A} />
        <circle cx={fx} cy={fy} r={W * 0.026} fill="none" stroke={A} strokeWidth={W * 0.004} opacity={0.5} />
      </svg>

      {contrapunto ? (
        <div style={{
          position: "absolute", left: M, bottom: M,
          fontFamily: EDITORIAL, fontStyle: "italic", color: tinta,
          fontSize: W * 0.05, lineHeight: 1.2, maxWidth: W * 0.6,
        }}>
          {contrapunto}
        </div>
      ) : null}
      {fuente ? (
        <div style={{
          position: "absolute", right: M, bottom: M,
          fontFamily: SANS, fontSize: W * 0.021, color: suave,
        }}>
          {fuente}
        </div>
      ) : null}
      {nota ? <NotaAlMargen texto={nota} x={W * 0.6} y={H * 0.7} tam={W * 0.04} ancho={W * 0.3} color={A} hacia="abajo-izq" /> : null}
    </AbsoluteFill>
  );
};

/** La SEÑAL / 026 de la lámina de referencia. */
export const GCL_PIEZA_DEMO: GclPiezaProps = {
  layout: "declaracion",
  fondo: "rosado",
  pilar: "SEÑAL",
  detalle: "026",
  titular: "Tu marca no necesita más contenido.",
  contrapunto: "Necesita algo que decir.",
  marca: {verbo: "circular", x: 0.052, y: 0.395, ancho: 0.3, alto: 0.088},
};
