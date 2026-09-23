// ============================================================================
// 01 · SIGNAL — «Nadie recuerda tu último post»
// ----------------------------------------------------------------------------
// INSIGHT   El mercado premia el volumen y olvida el contenido. Lo que queda no
//           es la publicación, es la idea que había detrás.
// IDEA      Decirlo tachando literalmente la publicación.
// ANOMALÍA  Una sola: el salto brutal de escala entre «RECUERDA» (250 px) y
//           «TU ÚLTIMO POST.» (130 px). Todo lo demás se comporta.
// INTERV.   Una: el tachado sobre la línea chica. Es semántico — anula aquello
//           de lo que la frase dice que nadie se acuerda. Si se sacara, la
//           pieza seguiría funcionando; con dos marcas, no.
// FORMATO   Feed 4:5 · tipografía pura, sin imagen. El aire negro de arriba es
//           la mitad del diseño.
// ============================================================================
import React from "react";
import {useVideoConfig} from "remotion";
import {C, asegurarFuentes, margen} from "../../brand/copylab/sistema";
import {Bloque, Indice} from "../../brand/copylab/tipografia";
import {Pieza} from "../../brand/copylab/lienzo";
import {Tachado} from "../../brand/copylab/mano";

export const Signal: React.FC = () => {
  asegurarFuentes();
  const {width: W} = useVideoConfig();
  const M = margen(W);
  const base = 250;

  return (
    <Pieza fondo={C.tinta} grano={0.2}>
      <Indice familia="Señal" ref="041" style={{position: "absolute", left: M, top: M}} />

      <div style={{position: "absolute", left: M, top: 560}}>
        <Bloque
          base={base}
          lineas={[
            {t: "Nadie", wdth: 66},
            {t: "recuerda", wdth: 66},
            {t: "tu último post.", wdth: 74, esc: 0.52, dy: 6},
          ]}
        />
      </div>

      {/* Anula la publicación, no la idea. */}
      <Tachado x={M - 12} y={1026} w={886} grosor={9} semilla={11} angulo={-1.4} />

      <div style={{position: "absolute", left: M, top: 1150}}>
        <Bloque
          base={base}
          sangria={0.012}
          lineas={[{t: "Se acuerdan de tu última idea.", voz: "editorial", esc: 0.3, color: C.rosa}]}
        />
      </div>
    </Pieza>
  );
};
