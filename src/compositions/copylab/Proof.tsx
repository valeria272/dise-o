// ============================================================================
// 04 · PROOF — «Menos 37%»
// ----------------------------------------------------------------------------
// REGLA    Los resultados NO se muestran en dashboards ni en infografías
//          genéricas. El número tiene que volverse un objeto visual.
// IDEA     El −37% se lo aplicamos al propio número: la cifra está CORTADA y
//          el trozo de abajo se desprendió. El dato no se ilustra, se ejecuta
//          sobre sí mismo.
// COLOR    El trozo caído es el único rosado de la pieza. Ahí el acento no
//          decora: marca exactamente la parte que se fue.
// FONDO    Off-white con fibra de papel. En una grilla de piezas negras, el
//          respiro claro es lo que evita que el feed se vuelva una mancha.
// INTERV.  Cero. La fractura ya es la anomalía; una marca a mano encima sería
//          explicar un chiste que ya se entendió.
//
// ── Qué se corrigió después del primer render (03-09-2026) ──────────────────
//  1. El signo «−» de Archivo se apoya muy abajo y a 470 px se leía como un
//     guión bajo suelto, además de quedar partido por el corte. Se sacó de la
//     cifra: ahora la resta la dice la palabra MENOS y el número queda limpio.
//  2. La caída era de 52 px con 30 px de deriva lateral: el trozo se leía como
//     un segundo objeto, no como un pedazo del mismo. Bajó a 24 px y deriva 0,
//     que es lo que hace que se lea FRACTURA y no ERROR.
//  3. La cifra se desbordaba 15 px del margen derecho. 490 px de cuerpo entran.
//
// ⚠️ CIFRA DE DEMOSTRACIÓN. −37% es un valor de maqueta para probar el sistema.
//    Antes de publicar hay que reemplazarlo por un dato auditado y real, y sólo
//    entonces se puede nombrar al cliente. Ver ENTREGA.md → Pendientes.
// ============================================================================
import React from "react";
import {useVideoConfig} from "remotion";
import {C, asegurarFuentes, margen, VOZ, ancho} from "../../brand/copylab/sistema";
import {Bloque, Indice} from "../../brand/copylab/tipografia";
import {Pieza} from "../../brand/copylab/lienzo";

/** La cifra partida: dos copias del mismo texto recortadas por clip-path.
 *  La de arriba se queda en su sitio; la de abajo se desprende y cae recto. */
const CifraRota: React.FC<{
  texto: string; size: number; corte: number; caida: number;
}> = ({texto, size, corte, caida}) => {
  const comun: React.CSSProperties = {
    position: "absolute", left: 0, top: 0, whiteSpace: "pre",
    fontFamily: VOZ.impacto, fontSize: size, lineHeight: 1,
    fontVariationSettings: ancho(64, 900), fontWeight: 900,
    letterSpacing: "-0.045em",
  };
  return (
    <div style={{position: "relative", height: size * 1.02}}>
      <div style={{...comun, color: C.tinta, clipPath: `inset(0 0 ${100 - corte}% 0)`}}>{texto}</div>
      <div
        style={{
          ...comun, color: C.rosa,
          clipPath: `inset(${corte}% 0 0 0)`,
          transform: `translateY(${caida}px)`,
        }}
      >
        {texto}
      </div>
    </div>
  );
};

export const Proof: React.FC = () => {
  asegurarFuentes();
  const {width: W} = useVideoConfig();
  const M = margen(W);

  return (
    <Pieza fondo={C.offwhite} grano={0.1} papel={0.55}>
      <Indice
        familia="Case" ref="Paid Media"
        color="rgba(8,15,20,0.5)"
        style={{position: "absolute", left: M, top: M}}
      />

      <div style={{position: "absolute", left: M, top: 356}}>
        <Bloque base={116} lineas={[{t: "Menos", wdth: 74, color: C.tinta}]} />
      </div>

      <div style={{position: "absolute", left: M - 16, top: 486}}>
        <CifraRota texto="37%" size={490} corte={63} caida={24} />
      </div>

      <div
        style={{
          position: "absolute", left: M, top: 1052,
          fontFamily: VOZ.data, fontSize: 25, fontWeight: 500,
          letterSpacing: "0.16em", color: "rgba(8,15,20,0.55)",
        }}
      >
        COSTO POR ADQUISICIÓN · 90 DÍAS
      </div>

      <div style={{position: "absolute", left: M, top: 1112}}>
        <Bloque
          base={190}
          sangria={0.012}
          lineas={[
            {t: "Bajamos el costo.", voz: "editorial", esc: 0.42, color: C.tinta},
            {t: "No la ambición.", voz: "editorial", esc: 0.42, color: C.tinta},
          ]}
        />
      </div>
    </Pieza>
  );
};
