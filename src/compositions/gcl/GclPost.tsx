// ⚠️⚠️ DEPRECADO — 03-09-2026 ⚠️⚠️
// ============================================================================
// Este archivo es el SISTEMA VIEJO del feed de @copywriters.cl. Lo reemplaza el
// COPYWRITERS CREATIVE OPERATING SYSTEM v1.0:
//
//     creative-system/COPYWRITERS_CREATIVE_OS.md   ← la ley
//     src/brand/copylab/                           ← el motor
//     src/compositions/copylab/                    ← las piezas (una por archivo)
//
// POR QUÉ SE DEPRECÓ. El brief del 03-09-2026 pide explícitamente lo contrario
// de lo que hace este archivo. Contradicciones puntuales, todas en la lista de
// prohibiciones de src/brand/copylab/tokens.json:
//
//   · `Halo` — orbe rosado difuso con blur: gradiente decorativo.
//   · `AnilloLed` — 46 puntos en círculo: partículas.
//   · `Pastilla` — etiqueta con borderRadius: chip de SaaS.
//   · `CALOR` / `PROFUNDO` — gradientes de fondo.
//   · `Firma` pintada en TODAS las piezas: el logo se gana su lugar, no se pone
//     por costumbre (CREATIVE_OS §7 — en el lote nuevo va en 1 de 9).
//   · Y lo de fondo: `plantilla: "statement" | "resultado" | "tip" | ...`, seis
//     layouts fijos con campos que se rellenan. Eso ES una plantilla, y el
//     sistema nuevo existe justamente para no tener una.
//
// POR QUÉ NO SE BORRÓ. `AGENTE SOCIAL MEDIA/tools/remotion_render.py` invoca
// esta composición: borrarla hoy deja al agente social sin poder publicar.
// Sigue registrada en Root.tsx y sigue funcionando.
//
// PENDIENTE PARA VALERIA: decidir cuándo se migra el agente social a las
// composiciones CL-*. Es una decisión de operación, no de diseño.
// Detalle completo: creative-system/AUDITORIA.md
// ============================================================================

// ============================================================================
// GCL POST — las plantillas estáticas del feed de Grupo Copylab (@copywriters.cl)
// ----------------------------------------------------------------------------
// Una sola composición con 6 plantillas. El agente social le pasa las props y
// saca un PNG; no hay que tocar código para publicar una pieza nueva.
//
// Render (desde EDITOR VIDEOS/):
//   npx remotion still GclPost out/gcl/pieza.png --props='{"plantilla":"resultado",...}'
//
// Normalmente no se llama a mano: lo hace
//   AGENTE SOCIAL MEDIA/tools/remotion_render.py
//
// Las 6 plantillas salen de los pilares de contenido definidos en gcl.tokens.json:
//   statement  → gancho/opinión           (pilar: agencia, tendencias)
//   resultado  → cifra dura de un caso    (pilar: resultados)
//   tip        → educativo con bullets    (pilar: estrategia)
//   tendencia  → lista numerada, fondo claro (pilar: tendencias & IA)
//   testimonio → cita de cliente          (pilar: clientes)
//   cultura    → foto del equipo + titular (pilar: detrás de la agencia)
// ============================================================================
import React from "react";
import {AbsoluteFill, Img, useVideoConfig, staticFile} from "remotion";
import {C, TITULAR, CUERPO, CALOR, PROFUNDO, asegurarFuentesGcl} from "../../brand/gcl";
import {Halo, AnilloLed, Pastilla, Firma, Velo} from "../../brand/gclUI";

export type GclPlantilla =
  | "statement" | "resultado" | "tip" | "tendencia" | "testimonio" | "cultura";

export type GclPostProps = {
  plantilla: GclPlantilla;
  titulo: string;
  /** Segunda línea del titular. En `statement` se pinta en rosado. */
  bajada?: string;
  /** La cifra de la plantilla `resultado` ("471%", "+250"). */
  cifra?: string;
  /** Texto de la pastilla de esquina: TIPS, CASO REAL, TENDENCIA… */
  etiqueta?: string;
  /** Bullets de `tip` o ítems numerados de `tendencia`. Máximo 4: más no se lee. */
  puntos?: string[];
  autor?: string;
  cargo?: string;
  /** Texto chico de la esquina inferior derecha ("VER CASO COMPLETO"). */
  cta?: string;
  /** Ruta en public/ o URL pública. Sin foto, `cultura` cae a un gradiente. */
  foto?: string;
  acento?: "rosado" | "coral" | "purpura";
};

const ACENTOS = {rosado: C.rosado, coral: C.coral, purpura: C.purpura} as const;

/** El titular se encoge según el largo. Un texto que se desborda arruina la pieza
 *  entera, y quien escribe el copy no debería tener que contar caracteres. */
const escala = (texto: string, base: number, corte = 42) => {
  const n = texto.length;
  if (n <= corte) return base;
  if (n <= corte * 1.6) return base * 0.82;
  if (n <= corte * 2.3) return base * 0.68;
  return base * 0.56;
};

export const GclPost: React.FC<GclPostProps> = ({
  plantilla, titulo, bajada, cifra, etiqueta, puntos = [], autor, cargo, cta, foto,
  acento = "rosado",
}) => {
  asegurarFuentesGcl();
  const {width: W, height: H} = useVideoConfig();
  const A = ACENTOS[acento] || C.rosado;
  const M = Math.round(W * 0.07);          // margen lateral, proporcional al formato
  const fuente = (f?: string) =>
    !f ? undefined : /^https?:\/\//.test(f) ? f : staticFile(f);

  // ---------------------------------------------------------------- statement
  if (plantilla === "statement") {
    return (
      <AbsoluteFill style={{background: C.fondo, overflow: "hidden"}}>
        <Halo x={W * 0.92} y={H * 0.14} r={W * 0.36} op={0.5} />
        <Halo x={W * 0.08} y={H * 0.92} r={W * 0.26} color={C.purpura} op={0.34} />
        <AnilloLed x={W * 0.86} y={H * 0.13} r={W * 0.3} />
        {etiqueta ? (
          <div style={{position: "absolute", left: M, top: M}}><Pastilla texto={etiqueta} fondo={A} /></div>
        ) : null}
        <div style={{position: "absolute", left: M, right: M, top: H * 0.34}}>
          <div style={{
            fontFamily: TITULAR, fontWeight: 700, color: C.blanco,
            fontSize: escala(titulo, W * 0.105, 34), lineHeight: 1.03, letterSpacing: "-0.03em",
          }}>
            {titulo}
          </div>
          {bajada ? (
            <div style={{
              fontFamily: TITULAR, fontWeight: 700, color: A, marginTop: 6,
              fontSize: escala(bajada, W * 0.105, 34), lineHeight: 1.03, letterSpacing: "-0.03em",
            }}>
              {bajada}
            </div>
          ) : null}
        </div>
        <div style={{
          position: "absolute", left: M, bottom: H * 0.16, width: 74, height: 74,
          borderRadius: "50%", border: `3px solid ${A}`, display: "flex",
          alignItems: "center", justifyContent: "center", color: A, fontSize: 34,
        }}>
          →
        </div>
        <Firma cta={cta} />
      </AbsoluteFill>
    );
  }

  // ---------------------------------------------------------------- resultado
  if (plantilla === "resultado") {
    const barras = [0.28, 0.42, 0.36, 0.58, 0.72, 0.66, 1];
    return (
      <AbsoluteFill style={{background: CALOR, overflow: "hidden"}}>
        <Halo x={W * 0.16} y={H * 0.1} r={W * 0.34} color="#fff" op={0.14} />
        {etiqueta ? (
          <div style={{position: "absolute", left: M, top: M}}>
            <Pastilla texto={etiqueta} fondo="rgba(8,15,20,0.42)" />
          </div>
        ) : null}
        <div style={{position: "absolute", left: M, right: M, top: H * 0.2}}>
          <div style={{
            fontFamily: TITULAR, fontWeight: 700, color: "#fff", letterSpacing: "-0.05em",
            fontSize: cifra && cifra.length > 5 ? W * 0.24 : W * 0.3, lineHeight: 0.9,
          }}>
            {cifra}
          </div>
          <div style={{
            fontFamily: TITULAR, fontWeight: 700, color: "#fff", marginTop: 14,
            fontSize: escala(titulo, W * 0.062, 30), lineHeight: 1.08, letterSpacing: "-0.01em",
            textTransform: "uppercase",
          }}>
            {titulo}
          </div>
          {bajada ? (
            <div style={{
              fontFamily: CUERPO, fontWeight: 400, color: "rgba(255,255,255,0.86)",
              marginTop: 20, fontSize: W * 0.032, lineHeight: 1.42, maxWidth: W * 0.74,
            }}>
              {bajada}
            </div>
          ) : null}
        </div>
        {/* Las barras no son un dato real: son la textura del pilar «resultados».
            Nunca poner ejes ni números en ellas, o se leen como un gráfico que miente. */}
        <div style={{
          position: "absolute", left: M, right: M, bottom: H * 0.135, height: H * 0.2,
          display: "flex", alignItems: "flex-end", gap: W * 0.022, opacity: 0.9,
        }}>
          {barras.map((b, i) => (
            <div key={i} style={{
              flex: 1, height: `${b * 100}%`, borderRadius: 4,
              background: i === barras.length - 1 ? "#fff" : "rgba(255,255,255,0.34)",
            }} />
          ))}
        </div>
        <Firma cta={cta} acento="#fff" />
      </AbsoluteFill>
    );
  }

  // ---------------------------------------------------------------------- tip
  if (plantilla === "tip") {
    return (
      <AbsoluteFill style={{background: C.fondo, overflow: "hidden"}}>
        <Halo x={W * 1.02} y={H * 0.88} r={W * 0.4} op={0.4} />
        <div style={{position: "absolute", left: M, top: M}}>
          <Pastilla texto={etiqueta || "Tips"} fondo={A} />
        </div>
        <div style={{position: "absolute", left: M, right: M, top: H * 0.18}}>
          <div style={{
            fontFamily: TITULAR, fontWeight: 700, color: C.blanco, letterSpacing: "-0.03em",
            fontSize: escala(titulo, W * 0.086, 38), lineHeight: 1.06,
          }}>
            {titulo}
          </div>
          {bajada ? (
            <div style={{
              fontFamily: TITULAR, fontWeight: 700, color: A, marginTop: 4,
              fontSize: escala(bajada, W * 0.086, 38), lineHeight: 1.06, letterSpacing: "-0.03em",
            }}>
              {bajada}
            </div>
          ) : null}
        </div>
        <div style={{position: "absolute", left: M, right: M, top: H * 0.46}}>
          {puntos.slice(0, 4).map((p, i) => (
            <div key={i} style={{display: "flex", gap: 20, alignItems: "flex-start", marginBottom: 30}}>
              <div style={{
                width: 15, height: 15, borderRadius: 3, background: A, marginTop: 14, flex: "none",
                transform: "rotate(45deg)",
              }} />
              <div style={{
                fontFamily: CUERPO, fontWeight: 400, color: "rgba(255,255,255,0.9)",
                fontSize: W * 0.037, lineHeight: 1.38,
              }}>
                {p}
              </div>
            </div>
          ))}
        </div>
        <Firma cta={cta} />
      </AbsoluteFill>
    );
  }

  // --------------------------------------------------------------- tendencia
  // Única plantilla sobre fondo claro: en una grilla toda oscura, es la que
  // rompe el bloque y evita que el perfil se vea plano.
  if (plantilla === "tendencia") {
    return (
      <AbsoluteFill style={{background: C.claro, overflow: "hidden"}}>
        <div style={{
          position: "absolute", left: 0, right: 0, top: 0, height: 10, background: CALOR,
        }} />
        <div style={{position: "absolute", left: M, top: M + 16}}>
          <Pastilla texto={etiqueta || "Tendencias"} fondo={A} />
        </div>
        <div style={{position: "absolute", left: M, right: M, top: H * 0.17}}>
          <div style={{
            fontFamily: TITULAR, fontWeight: 700, color: C.textoOscuro, letterSpacing: "-0.03em",
            fontSize: escala(titulo, W * 0.082, 36), lineHeight: 1.05,
          }}>
            {titulo}
          </div>
          {bajada ? (
            <div style={{
              fontFamily: CUERPO, color: "rgba(8,15,20,0.66)", marginTop: 16,
              fontSize: W * 0.031, lineHeight: 1.45, maxWidth: W * 0.8,
            }}>
              {bajada}
            </div>
          ) : null}
        </div>
        <div style={{position: "absolute", left: M, right: M, top: H * 0.42}}>
          {puntos.slice(0, 4).map((p, i, arr) => (
            <div key={i} style={{
              display: "flex", gap: 22, alignItems: "center", background: "#fff",
              borderRadius: 14,
              // El bloque tiene que llenar el alto disponible: con 3 ítems y el
              // espaciado de 4, quedaba un cuarto de pieza en blanco abajo.
              padding: arr.length <= 3 ? "38px 28px" : "24px 26px",
              marginBottom: arr.length <= 3 ? 32 : 18,
              boxShadow: "0 2px 18px rgba(8,15,20,0.07)",
            }}>
              <div style={{
                fontFamily: TITULAR, fontWeight: 700, fontSize: W * 0.05, lineHeight: 1,
                background: CALOR, WebkitBackgroundClip: "text", backgroundClip: "text",
                color: "transparent", flex: "none", minWidth: W * 0.085,
              }}>
                {String(i + 1).padStart(2, "0")}
              </div>
              <div style={{
                fontFamily: CUERPO, fontWeight: 400, color: C.textoOscuro,
                fontSize: W * 0.032, lineHeight: 1.32,
              }}>
                {p}
              </div>
            </div>
          ))}
        </div>
        <Firma oscuro cta={cta} />
      </AbsoluteFill>
    );
  }

  // -------------------------------------------------------------- testimonio
  if (plantilla === "testimonio") {
    return (
      <AbsoluteFill style={{background: C.superficie, overflow: "hidden"}}>
        <Halo x={W * 0.06} y={H * 0.08} r={W * 0.3} op={0.4} />
        <div style={{
          position: "absolute", left: M, top: H * 0.14, fontFamily: TITULAR, fontWeight: 700,
          fontSize: W * 0.2, lineHeight: 0.7, color: A,
        }}>
          “
        </div>
        <div style={{position: "absolute", left: M, right: M, top: H * 0.3}}>
          <div style={{
            fontFamily: CUERPO, fontWeight: 400, color: C.blanco,
            fontSize: escala(titulo, W * 0.055, 90), lineHeight: 1.34, letterSpacing: "-0.01em",
          }}>
            {titulo}
          </div>
        </div>
        <div style={{position: "absolute", left: M, right: M, bottom: H * 0.16}}>
          <div style={{width: 68, height: 4, background: A, marginBottom: 20}} />
          <div style={{fontFamily: TITULAR, fontWeight: 700, color: C.blanco, fontSize: W * 0.036}}>
            {autor}
          </div>
          {cargo ? (
            <div style={{
              fontFamily: CUERPO, color: "rgba(255,255,255,0.6)", fontSize: W * 0.028, marginTop: 4,
            }}>
              {cargo}
            </div>
          ) : null}
        </div>
        <Firma cta={cta} />
      </AbsoluteFill>
    );
  }

  // ------------------------------------------------------------------ cultura
  return (
    <AbsoluteFill style={{background: foto ? C.fondo : PROFUNDO, overflow: "hidden"}}>
      {foto ? (
        <Img src={fuente(foto)!} style={{width: "100%", height: "100%", objectFit: "cover"}} />
      ) : (
        <Halo x={W * 0.8} y={H * 0.2} r={W * 0.42} color={C.coral} op={0.42} />
      )}
      <Velo />
      {etiqueta ? (
        <div style={{position: "absolute", left: M, top: M}}><Pastilla texto={etiqueta} fondo={A} /></div>
      ) : null}
      <div style={{position: "absolute", left: M, right: M, bottom: H * 0.15}}>
        <div style={{
          fontFamily: TITULAR, fontWeight: 700, color: C.blanco, letterSpacing: "-0.03em",
          fontSize: escala(titulo, W * 0.088, 36), lineHeight: 1.05,
        }}>
          {titulo}
        </div>
        {bajada ? (
          <div style={{
            fontFamily: CUERPO, color: "rgba(255,255,255,0.82)", marginTop: 14,
            fontSize: W * 0.032, lineHeight: 1.4, maxWidth: W * 0.82,
          }}>
            {bajada}
          </div>
        ) : null}
      </div>
      <Firma cta={cta} />
    </AbsoluteFill>
  );
};

export const GCL_POST_DEMO: GclPostProps = {
  plantilla: "resultado",
  etiqueta: "Caso real",
  cifra: "471%",
  titulo: "Aumento de alcance",
  bajada: "En 90 días, sin subir un peso el presupuesto.",
  cta: "Ver caso completo",
};
