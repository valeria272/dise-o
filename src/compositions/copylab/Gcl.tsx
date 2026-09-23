// ============================================================================
// 06 · G.CL WORLD — «Revisión 7»
// ----------------------------------------------------------------------------
// REGLA    G.CL no es mascota corporativa. Es un personaje secundario que
//          aparece cuando la historia lo amerita, con humor absurdo del mundo
//          agencia. Nunca «porque toca poner la mascota».
// IDEA     El chiste no lo cuenta la tipografía, lo cuenta la postura. El texto
//          sólo pone la fecha del crimen y la frase del cliente. Por eso el
//          titular es corto y la voz editorial hace de bocadillo.
// CANON    La imagen se generó con el CANDADO 1 de gcl-agent/GCL_CHARACTER_BIBLE.md:
//          referencia obligatoria del master en TODA generación, nunca text-only.
//          Master: character-master/gcl_master_frontal_logo.png + turnaround.
//          Se descartó una primera generación por tener el visor descolocado y
//          el anillo de audífonos rojo en vez de coral (la biblia manda coral).
// INTERV.  Cero. G.CL ya es el elemento raro de la grilla; sumarle una marca a
//          mano sería subrayar el chiste.
// ============================================================================
import React from "react";
import {useVideoConfig} from "remotion";
import {C, asegurarFuentes, margen} from "../../brand/copylab/sistema";
import {Bloque, Indice} from "../../brand/copylab/tipografia";
import {Pieza, Foto, Velo} from "../../brand/copylab/lienzo";

export const Gcl: React.FC = () => {
  asegurarFuentes();
  const {width: W} = useVideoConfig();
  const M = margen(W);

  return (
    <Pieza fondo={C.tinta} grano={0.22}>
      <Foto
        src="assets/copylab/gcl/revision7-02.png"
        grado="crudo"
        encuadre="56% 50%"
        zoom={1.02}
      />
      <Velo desde="arriba" fuerza={0.72} corte={0.3} />

      <Indice familia="G.CL" ref="En servicio" acento={C.coral}
        style={{position: "absolute", left: M, top: M}} />

      <div style={{position: "absolute", left: M, top: 210}}>
        <Bloque
          base={168}
          lineas={[{t: "Revisión 7.", wdth: 70}]}
        />
      </div>

      <div style={{position: "absolute", left: M, top: 396, width: 720}}>
        <Bloque
          base={168}
          sangria={0.012}
          lineas={[
            {t: "«Volvamos a", voz: "editorial", esc: 0.44, color: C.rosa},
            {t: "la primera».", voz: "editorial", esc: 0.44, color: C.rosa},
          ]}
        />
      </div>
    </Pieza>
  );
};
