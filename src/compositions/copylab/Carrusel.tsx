// ============================================================================
// 09 · CARRUSEL — «Cómo matamos una idea»
// ----------------------------------------------------------------------------
// REGLA    Un carrusel cuenta una historia en secuencia. NO es «3 tips» ni
//          «5 claves», y no lleva flecha de «desliza» (prohibido en tokens.json:
//          si la primera lámina no da ganas de deslizar, una flecha no lo arregla).
// TEMA     El criterio interno del estudio para MATAR una idea. Se eligió a
//          propósito un tema sin cifras: un carrusel de caso obligaría a poner
//          resultados, y un resultado inventado es un dato falso, no un diseño.
// RITMO    Las láminas alternan tinta / off-white. El cambio de fondo al
//          deslizar es lo que da pulso a la secuencia; con cinco láminas negras
//          seguidas el carrusel se siente una sola imagen larga.
// ESTRUCTURA  01 tesis · 02–04 los tres cortes · 05 remate.
// LOGO     La lámina 05 es el ÚNICO lugar de las nueve piezas donde aparece el
//          wordmark. Es un cierre, que es uno de los cuatro casos en que el
//          sistema lo permite (COPYWRITERS_CREATIVE_OS §9). En las otras ocho
//          piezas la marca se reconoce sin logo — o el sistema no sirve.
// ============================================================================
import React from "react";
import {useVideoConfig} from "remotion";
import {C, asegurarFuentes, margen, VOZ} from "../../brand/copylab/sistema";
import {Bloque, Indice} from "../../brand/copylab/tipografia";
import {Pieza} from "../../brand/copylab/lienzo";
import {Subrayado} from "../../brand/copylab/mano";

export type CarruselProps = {slide: number};

const TOTAL = 5;

/** Paginación en mono. Ordena la secuencia sin dibujar una flecha de «desliza». */
const Folio: React.FC<{n: number; oscuro: boolean; M: number}> = ({n, oscuro, M}) => (
  <div
    style={{
      position: "absolute", right: M, bottom: M,
      fontFamily: VOZ.data, fontSize: 22, fontWeight: 400, letterSpacing: "0.16em",
      color: oscuro ? "rgba(8,15,20,0.45)" : "rgba(242,244,246,0.45)",
    }}
  >
    {String(n).padStart(2, "0")} / {String(TOTAL).padStart(2, "0")}
  </div>
);

export const Carrusel: React.FC<CarruselProps> = ({slide}) => {
  asegurarFuentes();
  const {width: W} = useVideoConfig();
  const M = margen(W);
  const n = Math.min(Math.max(slide, 1), TOTAL);
  const claro = n === 2 || n === 4;         // 01 · 03 · 05 en tinta
  const tinta = claro ? C.tinta : C.offwhite;

  const cabecera = (
    <Indice
      familia="Field notes" ref="007"
      color={claro ? "rgba(8,15,20,0.5)" : "rgba(242,244,246,0.5)"}
      style={{position: "absolute", left: M, top: M}}
    />
  );

  // ── 01 · la tesis ────────────────────────────────────────────────────────
  if (n === 1) {
    return (
      <Pieza fondo={C.tinta} grano={0.2}>
        {cabecera}
        <div style={{position: "absolute", left: M, top: 610}}>
          <Bloque
            base={224}
            lineas={[
              {t: "Cómo", wdth: 66},
              {t: "matamos", wdth: 66},
              {t: "una idea.", wdth: 66, color: C.rosa},
            ]}
          />
        </div>
        <Folio n={n} oscuro={false} M={M} />
      </Pieza>
    );
  }

  // ── 05 · el remate ───────────────────────────────────────────────────────
  if (n === 5) {
    return (
      <Pieza fondo={C.tinta} grano={0.2}>
        {cabecera}
        <div style={{position: "absolute", left: M, top: 640}}>
          <Bloque
            base={210}
            sangria={0.012}
            lineas={[{t: "Lo que sobrevive,", voz: "editorial", esc: 0.5}]}
          />
        </div>
        <div style={{position: "absolute", left: M, top: 786}}>
          <Bloque base={210} lineas={[{t: "se produce.", wdth: 66, esc: 0.88, color: C.rosa}]} />
        </div>
        {/* Único wordmark de las nueve piezas: es un cierre. */}
        <div
          style={{
            position: "absolute", left: M, bottom: M,
            fontFamily: VOZ.impacto, fontVariationSettings: "'wdth' 88, 'wght' 700",
            fontSize: 30, letterSpacing: "0.34em", textTransform: "uppercase",
            color: "rgba(242,244,246,0.9)",
          }}
        >
          Copywriters
        </div>
        <Folio n={n} oscuro={false} M={M} />
      </Pieza>
    );
  }

  // ── 02 · 03 · 04 — los tres cortes ───────────────────────────────────────
  // Las tres condiciones se reescribieron para medir lo mismo (11–13 signos por
  // línea). No fue un capricho de copy: con «Si la puede firmar» la lámina 03 se
  // salía 41 px del margen, y la salida fácil —bajarle el cuerpo sólo a esa
  // lámina— habría dejado una lámina más chica que sus dos hermanas. Igualando
  // el copy, las tres llenan la misma caja al mismo cuerpo.
  const cortes = [
    {cond: ["Si funciona", "sin la marca,"], juicio: "no es nuestra.", sub: 520},
    {cond: ["Si la firma", "otra agencia,"], juicio: "está muerta.", sub: 470},
    {cond: ["Si hay que", "explicarla,"], juicio: "no se entendió.", sub: 560},
  ][n - 2];

  return (
    <Pieza fondo={claro ? C.offwhite : C.tinta} grano={claro ? 0.1 : 0.2} papel={claro ? 0.5 : false}>
      {cabecera}
      <div style={{position: "absolute", left: M, top: 468}}>
        <Bloque
          base={146}
          lineas={cortes.cond.map((t) => ({t, wdth: 74, color: tinta}))}
        />
      </div>
      <div style={{position: "absolute", left: M, top: 812}}>
        <Bloque
          base={146}
          sangria={0.012}
          lineas={[{t: cortes.juicio, voz: "editorial", esc: 0.74, color: C.rosa}]}
        />
      </div>
      {/* Una sola marca por lámina, y siempre bajo el veredicto. */}
      <Subrayado x={M - 6} y={936} w={cortes.sub} grosor={8} semilla={n * 7} curva={0.03} />
      <Folio n={n} oscuro={claro} M={M} />
    </Pieza>
  );
};
