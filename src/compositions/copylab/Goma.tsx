// ============================================================================
// GOMA — «escribimos con la goma (la de borrar)»
// ----------------------------------------------------------------------------
// FUENTE   Pack de marca del 24-09-2026 (Downloads/mnt 2 · COPYWRITERS_CLAUDE_
//          BRAND_SYSTEM). Concepto A, aprobado por Valeria el mismo día.
// IDEA     El trabajo más valioso de un copywriter es invisible: lo que saca.
//          Una redactora de noche, borrando. La goma rosada gastada hasta el
//          muñón es el ÚNICO color saturado del cuadro — el rosa existe
//          físicamente; la pieza no le agrega ningún rosa gráfico salvo UNA
//          línea de texto.
// VOCES    Tres, el tope: Archivo Narrow Bold (titular) · DM Serif Display
//          Italic (el guiño, en rosa) · IBM Plex Mono (microcopy). Sin Inter.
// SIN LOGO La firma va en el caption (02 / 04 del pack).
// IMAGEN   Magnific Mystic 4:5 (scripts/copywriters-goma-hero-magnific.py, v4)
//          + retoque Nano Banana Pro: uñas sin esmalte y una mancha fuera
//          (scripts/copywriters-goma-hero-retoque.py). v1–v3 descartadas:
//          sacaban LÁPIZ rosado, o sea escribir en vez de borrar.
// ============================================================================
import React from "react";
import {C, asegurarFuentes, VOZ} from "../../brand/copylab/sistema";
import {Pieza, Foto, Velo} from "../../brand/copylab/lienzo";

const M = 72;

export const Goma: React.FC = () => {
  asegurarFuentes();
  return (
    <Pieza fondo={C.tinta} grano={0.18}>
      <Foto src="assets/copylab/goma/hero.jpg" grado="crudo" encuadre="50% 50%" />
      {/* Sólo para que el microcopy se lea sobre el escritorio. */}
      <Velo desde="abajo" fuerza={0.55} corte={0.8} />

      <div style={{position: "absolute", left: M, top: 92}}>
        <div
          style={{
            fontFamily: VOZ.narrow, fontWeight: 700, fontSize: 118,
            lineHeight: 0.9, letterSpacing: "-0.01em", color: C.offwhite,
            textTransform: "uppercase",
          }}
        >
          Escribimos<br />con la<br />goma.
        </div>
        <div
          style={{
            fontFamily: VOZ.editorial, fontStyle: "italic", fontSize: 58,
            lineHeight: 1, color: C.rosa, marginTop: 22, marginLeft: 4,
          }}
        >
          (la de borrar)
        </div>
      </div>

      <div
        style={{
          position: "absolute", left: M, bottom: 1350 - 1262 - 6,
          fontFamily: VOZ.data, fontWeight: 400, fontSize: 22, lineHeight: 1.35,
          letterSpacing: "0.12em", color: "rgba(242,244,246,0.72)",
          textTransform: "uppercase",
        }}
      >
        Lo que sacamos<br />también es trabajo.
      </div>
    </Pieza>
  );
};
