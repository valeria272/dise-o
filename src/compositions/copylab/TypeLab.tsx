// ============================================================================
// 07 · TYPE LAB — «Escribe igual»
// ----------------------------------------------------------------------------
// REGLA    Piezas donde la tipografía ES la imagen. Experimenta con escala,
//          contraste, espacio, peso — manteniendo la legibilidad.
// IDEA     El argumento no está en lo que dice la línea, está en que la línea
//          se repite. Seis veces idéntica, cada una un poco más apagada: una
//          copia de una copia de una copia. La degradación por repetición es
//          exactamente lo que le pasa al contenido generado en serie.
// ANOMALÍA La repetición. Una sola, y ocupa la pieza entera.
// COLOR    Pieza íntegramente rosada — el sistema la permite «cuando
//          conceptualmente lo justifique». Acá lo justifica: el rosa es la
//          firma de la marca, y la pieza que habla de la falta de firma es la
//          que se pinta entera de firma.
// INTERV.  Cero, y es una regla del sistema, no una omisión: la marca a mano
//          es rosada. Sobre un campo rosado no existe. En una pieza 100% rosa
//          la intervención ES la pieza.
// ============================================================================
import React from "react";
import {useVideoConfig} from "remotion";
import {C, asegurarFuentes, margen} from "../../brand/copylab/sistema";
import {Bloque, Indice, Linea} from "../../brand/copylab/tipografia";
import {Pieza} from "../../brand/copylab/lienzo";

const ECOS = [1, 0.68, 0.46, 0.31, 0.2, 0.12];

export const TypeLab: React.FC = () => {
  asegurarFuentes();
  const {width: W} = useVideoConfig();
  const M = margen(W);

  return (
    <Pieza fondo={C.rosa} grano={0.14}>
      <Indice familia="Type Lab" ref="004" color="rgba(8,15,20,0.55)"
        style={{position: "absolute", left: M, top: M}} />

      <div style={{position: "absolute", left: M, top: 228}}>
        <Bloque
          base={150}
          lineas={[{t: "La IA no escribe mal.", wdth: 82, esc: 0.36, color: C.tinta}]}
        />
      </div>

      {/* La copia de la copia de la copia. */}
      <div style={{position: "absolute", left: M, top: 356, marginLeft: -150 * 0.045}}>
        {ECOS.map((op, i) => (
          <Linea
            key={i}
            base={150}
            l={{t: "Escribe igual.", wdth: 64, color: C.tinta, op, alto: 0.8}}
          />
        ))}
      </div>

      <div style={{position: "absolute", left: M, top: 1160}}>
        <Bloque
          base={150}
          sangria={0.012}
          lineas={[{t: "Ese es el problema.", voz: "editorial", esc: 0.5, color: C.tinta}]}
        />
      </div>
    </Pieza>
  );
};
