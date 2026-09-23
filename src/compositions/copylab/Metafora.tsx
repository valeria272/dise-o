// ============================================================================
// 02 · VISUAL METAPHOR — «Todos tienen las mismas herramientas»
// ----------------------------------------------------------------------------
// INSIGHT   La IA igualó el acceso a las herramientas. No igualó el criterio.
//           La ventaja dejó de estar en TENER y pasó a estar en USAR.
// RUTAS     A góndola de cajas idénticas · B campo de lápices nuevos con uno
//           gastado hasta el tocón · C karaoke masivo. Ranking en
//           creative-system/image-prompts/BRIEFS-v1.md → gana B (36/40).
// IDEA      La imagen tiene que funcionar SIN el copy, y funciona: el único
//           gastado es el único que trabajó.
// ANOMALÍA  Ninguna tipográfica. Cuando la imagen carga la idea, la tipografía
//           se aparta. Meterle además un juego de escalas sería competirle.
// INTERV.   Cero. La foto ya intervino. El rosado entra sólo por la voz
//           editorial — la firma mínima.
// FORMATO   Feed 4:5 · 70% imagen / 30% texto, en el negro que la foto dejó.
// ============================================================================
import React from "react";
import {useVideoConfig} from "remotion";
import {C, asegurarFuentes, margen} from "../../brand/copylab/sistema";
import {Bloque, Indice} from "../../brand/copylab/tipografia";
import {Pieza, Foto, Velo} from "../../brand/copylab/lienzo";

export const Metafora: React.FC = () => {
  asegurarFuentes();
  const {width: W} = useVideoConfig();
  const M = margen(W);

  return (
    <Pieza fondo={C.tinta} grano={0.24}>
      <Foto
        src="assets/copylab/metafora/lapices-02.png"
        grado="editorial"
        encuadre="50% 62%"
        zoom={1.04}
      />
      {/* Velo funcional. Se subió de 0.36/0.8 a 0.2/0.9 después de mirar el
          primer render: el remate rosado caía sobre gris medio y a tamaño de
          feed desaparecía. El velo acá no ambienta, deja leer. */}
      <Velo desde="arriba" fuerza={0.9} corte={0.2} />

      <Indice familia="Metáfora" ref="012" style={{position: "absolute", left: M, top: M}} />

      <div style={{position: "absolute", left: M, top: 190}}>
        <Bloque
          base={124}
          lineas={[
            {t: "Todos tienen", wdth: 72},
            {t: "las mismas", wdth: 72},
            {t: "herramientas.", wdth: 72},
          ]}
        />
      </div>

      <div style={{position: "absolute", left: M, top: 548}}>
        <Bloque
          base={124}
          sangria={0.012}
          lineas={[{t: "Se nota quién las usa.", voz: "editorial", esc: 0.46, color: C.rosa}]}
        />
      </div>
    </Pieza>
  );
};
