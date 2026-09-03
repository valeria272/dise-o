// ============================================================================
// GCL CARRUSEL — el formato largo del feed de Grupo Copylab (@copywriters.cl)
// ----------------------------------------------------------------------------
// `GclPost` resuelve la pieza suelta. Esto resuelve lo otro que hace la cuenta:
// el carrusel de 5 a 8 láminas donde la agencia demuestra que sabe — un rubro,
// una campaña ajena leída con criterio, un caso propio contado por dentro.
//
// Por qué una composición aparte y no una plantilla más de GclPost: un carrusel
// no es un montón de piezas sueltas puestas en fila. Tiene arco (gancho →
// desarrollo → remate) y continuidad visual entre láminas — el mismo halo en el
// mismo lugar, la numeración que avanza, la barra de progreso. Eso hay que
// resolverlo mirando el conjunto, no lámina por lámina.
//
// Render de una lámina:
//   npx remotion still GclCarrusel out/gcl/l1.png --props='{"indice":0,...}'
//
// Render del carrusel entero: `bash scripts/gcl-carrusel.sh <archivo.json>`
// ============================================================================
import React from "react";
import {AbsoluteFill, Img, useVideoConfig, staticFile} from "remotion";
import {C, TITULAR, CUERPO, CALOR, asegurarFuentesGcl} from "../../brand/gcl";
import {Halo, AnilloLed, Firma, Velo} from "../../brand/gclUI";

/** Los cinco papeles que puede jugar una lámina. Con estos cinco se arma
 *  cualquiera de los carruseles del plan editorial; si aparece un sexto,
 *  primero hay que preguntarse si no es uno de estos con otro texto. */
export type GclRolLamina =
  | "portada"   // el gancho. Es la única que decide si alguien desliza.
  | "punto"     // un ítem numerado del desarrollo.
  | "dato"      // una cifra sola, a toda página, sobre el gradiente de calor.
  | "cita"      // una frase ajena o propia que sostiene el argumento.
  | "cierre";   // el remate y la firma. Nunca lleva información nueva.

export type GclLamina = {
  rol: GclRolLamina;
  titulo: string;
  bajada?: string;
  /** La cifra de `dato` ("471%", "7 de 13"). */
  cifra?: string;
  /** De dónde sale el dato. En `dato` es OBLIGATORIA: una cifra sin fuente en
   *  una cuenta de agencia es exactamente el error que la cuenta critica. */
  fuente?: string;
  autor?: string;
  foto?: string;
};

export type GclCarruselProps = {
  /** Rótulo de la serie, arriba a la izquierda ("MARKETING POR RUBRO"). */
  serie: string;
  laminas: GclLamina[];
  /** Qué lámina pintar. El script lo recorre de 0 a laminas.length - 1. */
  indice: number;
  acento?: "rosado" | "coral" | "purpura";
  /** Texto chico del cierre ("HABLEMOS DE TU MARCA"). */
  cta?: string;
};

const ACENTOS = {rosado: C.rosado, coral: C.coral, purpura: C.purpura} as const;

/** Mismo criterio que en GclPost: quien escribe el copy no debería tener que
 *  contar caracteres para que el titular no se desborde. */
const escala = (texto: string, base: number, corte = 42) => {
  const n = texto.length;
  if (n <= corte) return base;
  if (n <= corte * 1.6) return base * 0.82;
  if (n <= corte * 2.3) return base * 0.68;
  return base * 0.56;
};

/** La barra de progreso del carrusel. Es lo que le dice a alguien que hay más
 *  adelante, y es la razón principal por la que la gente llega a la última. */
const Progreso: React.FC<{i: number; total: number; ancho: number; y: number; m: number; acento: string; oscuro?: boolean}> = ({
  i, total, ancho, y, m, acento, oscuro = false,
}) => (
  <div style={{position: "absolute", left: m, right: m, top: y, display: "flex", gap: 8}}>
    {Array.from({length: total}).map((_, k) => (
      <div
        key={k}
        style={{
          flex: 1, height: 5, borderRadius: 3,
          background: k === i ? acento : oscuro ? "rgba(8,15,20,0.16)" : "rgba(255,255,255,0.18)",
        }}
      />
    ))}
  </div>
);

export const GclCarrusel: React.FC<GclCarruselProps> = ({
  serie, laminas, indice, acento = "rosado", cta,
}) => {
  asegurarFuentesGcl();
  const {width: W, height: H} = useVideoConfig();
  const A = ACENTOS[acento] || C.rosado;
  const M = Math.round(W * 0.07);
  const total = laminas.length;
  // Un índice fuera de rango sale de un script mal llamado. Mejor pintar la
  // última que reventar en medio de un render de 8 láminas.
  const i = Math.max(0, Math.min(indice, total - 1));
  const L = laminas[i];
  const fuente = (f: string) => (/^https?:\/\//.test(f) ? f : staticFile(f));

  // El número de lámina, arriba a la derecha. En la portada no va: ahí el
  // número compite con el gancho y no aporta nada.
  const Numero = () =>
    L.rol === "portada" ? null : (
      <div style={{
        position: "absolute", right: M, top: M + 26, fontFamily: TITULAR, fontWeight: 700,
        fontSize: W * 0.052, color: L.rol === "dato" ? "rgba(255,255,255,0.5)" : "rgba(255,255,255,0.34)",
        letterSpacing: "-0.02em",
      }}>
        {String(i + 1).padStart(2, "0")}
      </div>
    );

  const Rotulo = ({oscuro = false}: {oscuro?: boolean}) => (
    <div style={{
      position: "absolute", left: M, top: M + 30, fontFamily: CUERPO, fontWeight: 700,
      fontSize: 23, letterSpacing: 3.5, textTransform: "uppercase",
      color: oscuro ? "rgba(8,15,20,0.55)" : "rgba(255,255,255,0.55)",
    }}>
      {serie}
    </div>
  );

  // ------------------------------------------------------------------ portada
  // Carga toda la responsabilidad del carrusel: si esta no engancha, las otras
  // siete no existen. Por eso es la única con el titular a tamaño máximo y con
  // el «desliza» explícito.
  if (L.rol === "portada") {
    return (
      <AbsoluteFill style={{background: C.fondo, overflow: "hidden"}}>
        {L.foto ? (
          <>
            <Img src={fuente(L.foto)} style={{width: "100%", height: "100%", objectFit: "cover"}} />
            <Velo desde="30%" />
          </>
        ) : (
          <>
            <Halo x={W * 0.9} y={H * 0.16} r={W * 0.4} op={0.5} />
            <Halo x={W * 0.06} y={H * 0.9} r={W * 0.3} color={C.purpura} op={0.36} />
            <AnilloLed x={W * 1.06} y={-H * 0.02} r={W * 0.42} puntos={62} />
          </>
        )}
        <Progreso i={i} total={total} ancho={W} y={M} m={M} acento={A} />
        <Rotulo />
        <div style={{position: "absolute", left: M, right: M, top: H * 0.36}}>
          <div style={{
            fontFamily: TITULAR, fontWeight: 700, color: C.blanco,
            fontSize: escala(L.titulo, W * 0.108, 32), lineHeight: 1.02, letterSpacing: "-0.035em",
          }}>
            {L.titulo}
          </div>
          {L.bajada ? (
            <div style={{
              fontFamily: TITULAR, fontWeight: 700, color: A, marginTop: 8,
              fontSize: escala(L.bajada, W * 0.108, 32), lineHeight: 1.02, letterSpacing: "-0.035em",
            }}>
              {L.bajada}
            </div>
          ) : null}
        </div>
        <div style={{
          position: "absolute", left: M, bottom: H * 0.155, display: "flex",
          alignItems: "center", gap: 18,
        }}>
          <div style={{
            width: 72, height: 72, borderRadius: "50%", border: `3px solid ${A}`,
            display: "flex", alignItems: "center", justifyContent: "center", color: A, fontSize: 33,
          }}>
            →
          </div>
          <span style={{
            fontFamily: CUERPO, fontWeight: 600, fontSize: 25, letterSpacing: 2.5,
            textTransform: "uppercase", color: "rgba(255,255,255,0.6)",
          }}>
            Desliza
          </span>
        </div>
        <Firma cta={undefined} acento={A} />
      </AbsoluteFill>
    );
  }

  // --------------------------------------------------------------------- dato
  // La única lámina sobre el gradiente de calor. Rompe la seguidilla oscura a
  // media lectura, que es justo donde se cae la gente.
  if (L.rol === "dato") {
    return (
      <AbsoluteFill style={{background: CALOR, overflow: "hidden"}}>
        <Halo x={W * 0.14} y={H * 0.12} r={W * 0.36} color="#fff" op={0.15} />
        <Progreso i={i} total={total} ancho={W} y={M} m={M} acento="#fff" />
        <Rotulo />
        <Numero />
        <div style={{position: "absolute", left: M, right: M, top: H * 0.26}}>
          <div style={{
            fontFamily: TITULAR, fontWeight: 700, color: "#fff", letterSpacing: "-0.05em",
            fontSize: L.cifra && L.cifra.length > 5 ? W * 0.21 : W * 0.28, lineHeight: 0.88,
          }}>
            {L.cifra}
          </div>
          <div style={{
            fontFamily: TITULAR, fontWeight: 700, color: "#fff", marginTop: 18,
            fontSize: escala(L.titulo, W * 0.058, 30), lineHeight: 1.1,
            letterSpacing: "-0.01em", textTransform: "uppercase",
          }}>
            {L.titulo}
          </div>
          {L.bajada ? (
            <div style={{
              fontFamily: CUERPO, color: "rgba(255,255,255,0.9)", marginTop: 22,
              fontSize: W * 0.031, lineHeight: 1.44, maxWidth: W * 0.78,
            }}>
              {L.bajada}
            </div>
          ) : null}
        </div>
        {/* La fuente va SIEMPRE que haya cifra. Una agencia que publica datos
            sin decir de dónde salen no puede después vender medición. */}
        {L.fuente ? (
          <div style={{
            position: "absolute", left: M, right: M, bottom: H * 0.135,
            fontFamily: CUERPO, fontSize: W * 0.021, letterSpacing: 1,
            color: "rgba(255,255,255,0.7)",
          }}>
            Fuente: {L.fuente}
          </div>
        ) : null}
        <Firma acento="#fff" />
      </AbsoluteFill>
    );
  }

  // --------------------------------------------------------------------- cita
  if (L.rol === "cita") {
    return (
      <AbsoluteFill style={{background: C.superficie, overflow: "hidden"}}>
        <Halo x={W * 0.9} y={H * 0.88} r={W * 0.34} color={C.purpura} op={0.3} />
        <Progreso i={i} total={total} ancho={W} y={M} m={M} acento={A} />
        <Rotulo />
        <Numero />
        <div style={{
          position: "absolute", left: M, top: H * 0.24, fontFamily: TITULAR,
          fontWeight: 700, fontSize: W * 0.19, lineHeight: 0.7, color: A,
        }}>
          &ldquo;
        </div>
        <div style={{position: "absolute", left: M, right: M, top: H * 0.36}}>
          <div style={{
            fontFamily: TITULAR, fontWeight: 700, color: C.blanco,
            fontSize: escala(L.titulo, W * 0.072, 46), lineHeight: 1.16, letterSpacing: "-0.02em",
          }}>
            {L.titulo}
          </div>
          {L.autor ? (
            <div style={{
              fontFamily: CUERPO, fontWeight: 600, color: A, marginTop: 30,
              fontSize: W * 0.03, letterSpacing: 1.5,
            }}>
              — {L.autor}
            </div>
          ) : null}
          {L.bajada ? (
            <div style={{
              fontFamily: CUERPO, color: C.textoSuave, marginTop: 10,
              fontSize: W * 0.026, lineHeight: 1.44, maxWidth: W * 0.76,
            }}>
              {L.bajada}
            </div>
          ) : null}
        </div>
        <Firma acento={A} />
      </AbsoluteFill>
    );
  }

  // -------------------------------------------------------------------- cierre
  // Sin información nueva y sin dato: acá solo se pide la acción. Si el cierre
  // trae un argumento más, es que faltaba una lámina antes.
  if (L.rol === "cierre") {
    return (
      <AbsoluteFill style={{background: C.fondo, overflow: "hidden"}}>
        <Halo x={W * 0.5} y={H * 0.44} r={W * 0.46} op={0.42} />
        <AnilloLed x={W * 0.5} y={H * 0.44} r={W * 0.36} puntos={54} />
        <Progreso i={i} total={total} ancho={W} y={M} m={M} acento={A} />
        <div style={{
          position: "absolute", left: M, right: M, top: H * 0.38, textAlign: "center",
        }}>
          <div style={{
            fontFamily: TITULAR, fontWeight: 700, color: C.blanco,
            fontSize: escala(L.titulo, W * 0.1, 30), lineHeight: 1.04, letterSpacing: "-0.035em",
          }}>
            {L.titulo}
          </div>
          {L.bajada ? (
            <div style={{
              fontFamily: CUERPO, color: C.textoSuave, marginTop: 24,
              fontSize: W * 0.03, lineHeight: 1.45, maxWidth: W * 0.72,
              marginLeft: "auto", marginRight: "auto",
            }}>
              {L.bajada}
            </div>
          ) : null}
          <div style={{
            display: "inline-flex", alignItems: "center", gap: 14, marginTop: 40,
            background: A, color: "#fff", fontFamily: CUERPO, fontWeight: 700,
            fontSize: W * 0.028, letterSpacing: 2, textTransform: "uppercase",
            padding: "20px 36px", borderRadius: 8,
          }}>
            {cta || "Hablemos de tu marca"} →
          </div>
        </div>
        <Firma acento={A} />
      </AbsoluteFill>
    );
  }

  // -------------------------------------------------------------------- punto
  // El caballo de batalla: el desarrollo del argumento. Número grande a la
  // izquierda para que se lea el avance aunque alguien pase rápido.
  return (
    <AbsoluteFill style={{background: C.fondo, overflow: "hidden"}}>
      <Halo x={W * 1.02} y={H * 0.72} r={W * 0.34} op={0.34} />
      <Progreso i={i} total={total} ancho={W} y={M} m={M} acento={A} />
      <Rotulo />
      {L.foto ? (
        <div style={{
          position: "absolute", left: 0, right: 0, top: H * 0.13, height: H * 0.3,
          overflow: "hidden",
        }}>
          <Img src={fuente(L.foto)} style={{width: "100%", height: "100%", objectFit: "cover"}} />
          <div style={{
            position: "absolute", inset: 0,
            background: `linear-gradient(180deg, rgba(8,15,20,0.2) 0%, ${C.fondo} 100%)`,
          }} />
        </div>
      ) : null}
      <div style={{position: "absolute", left: M, right: M, bottom: H * 0.155}}>
        <div style={{
          fontFamily: TITULAR, fontWeight: 700, color: A,
          fontSize: W * 0.13, lineHeight: 0.9, letterSpacing: "-0.04em",
        }}>
          {String(i + 1).padStart(2, "0")}
        </div>
        <div style={{
          fontFamily: TITULAR, fontWeight: 700, color: C.blanco, marginTop: 22,
          fontSize: escala(L.titulo, W * 0.075, 38), lineHeight: 1.08, letterSpacing: "-0.025em",
        }}>
          {L.titulo}
        </div>
        {L.bajada ? (
          <div style={{
            fontFamily: CUERPO, color: C.textoSuave, marginTop: 24,
            fontSize: W * 0.029, lineHeight: 1.5, maxWidth: W * 0.8,
          }}>
            {L.bajada}
          </div>
        ) : null}
        {L.fuente ? (
          <div style={{
            fontFamily: CUERPO, fontSize: W * 0.02, letterSpacing: 1, marginTop: 20,
            color: "rgba(255,255,255,0.45)",
          }}>
            Fuente: {L.fuente}
          </div>
        ) : null}
      </div>
      <Firma acento={A} />
    </AbsoluteFill>
  );
};

/** Demo: es el carrusel de la campaña de Nike del plan editorial. Sirve de
 *  vista previa en Studio y de ejemplo de cómo se escribe un carrusel. */
export const GCL_CARRUSEL_DEMO: GclCarruselProps = {
  serie: "Leemos la campaña",
  acento: "rosado",
  cta: "Hablemos de tu marca",
  indice: 0,
  laminas: [
    {
      rol: "portada",
      titulo: "Nike no compró",
      bajada: "el Super Bowl.",
    },
    {
      rol: "punto",
      titulo: "Volvió en 2025 tras 27 años. Y en 2026 no fue.",
      bajada:
        "«So Win» la puso de vuelta en el partido más caro del mundo después de casi tres décadas fuera. Un año después decidió no comprar espacio.",
    },
    {
      rol: "dato",
      cifra: "7 vs 6",
      titulo: "Avisos de IA contra cerveza y autos juntos",
      bajada:
        "El Super Bowl LX tuvo más avisos de plataformas de inteligencia artificial que de las dos categorías que lo definieron por cuarenta años.",
      fuente: "EDO · Adweek, febrero 2026",
    },
    {
      rol: "punto",
      titulo: "Apareció igual. Después del partido.",
      bajada:
        "Un spot con Oakley Meta, «Athletic Intelligence Is Here», salió apenas terminó el juego. Sin pagar el minuto más caro del año.",
    },
    {
      rol: "cierre",
      titulo: "Estar no es comprar el espacio más caro.",
      bajada: "Es saber dónde está tu gente cuando termina el partido.",
    },
  ],
};
