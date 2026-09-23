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
// GCL — componentes compartidos del sistema visual (JSX).
// Los tokens y las fuentes viven en `gcl.ts`; acá solo lo que se dibuja.
// ============================================================================
import React from "react";
import {C, CUERPO} from "./gcl";

// ---------------------------------------------------------------------------
// Piezas compartidas del sistema
// ---------------------------------------------------------------------------

/** Halo rosado difuso. Es el gesto que hace que una pieza se lea como GCL. */
export const Halo: React.FC<{x: number; y: number; r: number; color?: string; op?: number}> = ({
  x, y, r, color = C.rosado, op = 0.55,
}) => (
  <div
    style={{
      position: "absolute", left: x - r, top: y - r, width: r * 2, height: r * 2,
      borderRadius: "50%", background: color, opacity: op, filter: `blur(${r * 0.62}px)`,
    }}
  />
);

/** Anillo de puntos LED — la firma del Agente G, en versión gráfica. */
export const AnilloLed: React.FC<{x: number; y: number; r: number; puntos?: number; color?: string}> = ({
  x, y, r, puntos = 46, color = C.rosado,
}) => (
  <div style={{position: "absolute", left: x, top: y, width: 0, height: 0}}>
    {Array.from({length: puntos}).map((_, i) => {
      const a = (i / puntos) * Math.PI * 2;
      const d = 5 + (i % 3);
      return (
        <div
          key={i}
          style={{
            position: "absolute", left: Math.cos(a) * r, top: Math.sin(a) * r,
            width: d, height: d, borderRadius: "50%", background: color,
            opacity: 0.25 + ((i * 7) % 10) / 14,
          }}
        />
      );
    })}
  </div>
);

/** Etiqueta de esquina: TIPS, CASO REAL, TENDENCIA… */
export const Pastilla: React.FC<{texto: string; fondo?: string; color?: string}> = ({
  texto, fondo = C.rosado, color = "#fff",
}) => (
  <div
    style={{
      display: "inline-block", background: fondo, color, fontFamily: CUERPO, fontWeight: 700,
      fontSize: 24, letterSpacing: 3, textTransform: "uppercase", padding: "10px 22px",
      borderRadius: 6,
    }}
  >
    {texto}
  </div>
);

/** Firma inferior. Va en TODA pieza: es lo que hace que la grilla se lea como una sola cuenta. */
export const Firma: React.FC<{oscuro?: boolean; cta?: string; acento?: string}> = ({
  oscuro = false, cta, acento = C.rosado,
}) => (
  <div
    style={{
      position: "absolute", left: 76, right: 76, bottom: 64, display: "flex",
      alignItems: "center", justifyContent: "space-between",
      fontFamily: CUERPO, fontSize: 26, fontWeight: 600,
      color: oscuro ? "rgba(8,15,20,0.62)" : "rgba(255,255,255,0.62)",
    }}
  >
    <span style={{letterSpacing: 1}}>
      <span style={{color: acento, fontWeight: 700}}>gcl</span>copylab
    </span>
    {cta ? <span style={{letterSpacing: 2, textTransform: "uppercase", fontSize: 23}}>{cta}</span> : null}
  </div>
);

/** Velo para poder poner texto encima de una foto y que se LEA. */
export const Velo: React.FC<{desde?: string}> = ({desde = "38%"}) => (
  <div
    style={{
      position: "absolute", inset: 0,
      background: `linear-gradient(180deg, rgba(8,15,20,0.12) 0%, rgba(8,15,20,0.05) ${desde}, rgba(8,15,20,0.93) 100%)`,
    }}
  />
);
