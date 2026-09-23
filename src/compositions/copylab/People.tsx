// ============================================================================
// 05 · PEOPLE — «acá estaba la buena»
// ----------------------------------------------------------------------------
// REGLA    Vida real de la agencia. Fotografía documental, NUNCA póster
//          corporativo del equipo. Flash directo, B&N, grano, recorte inesperado.
// IDEA     No hay titular. Esta es la única de las nueve piezas donde la
//          tipografía casi desaparece — y esa ausencia es la decisión de
//          dirección de arte: si PEOPLE llevara titular sería una campaña, y
//          esto tiene que parecer una foto que alguien tomó al pasar.
// INTERV.  Dos, el máximo del sistema, y las dos con razón: la anotación dice
//          algo que la foto no dice, y la flecha señala dónde. Una anotación
//          sin flecha flotaría; una flecha sin anotación decoraría.
// RECORTE  zoom 1.28 y encuadre corrido: los bordes cortan objetos a propósito.
//          Una foto centrada y completa es una foto de stock.
//
// ⚠️ IMAGEN PLACEHOLDER. PEOPLE pide fotografía REAL del equipo. Esta se generó
//    para probar el tratamiento mientras no hay sesión, y va sin caras
//    reconocibles justamente para no fingir documentación. Ver
//    creative-system/people/README.md.
// ============================================================================
import React from "react";
import {useVideoConfig} from "remotion";
import {C, asegurarFuentes, margen, VOZ} from "../../brand/copylab/sistema";
import {Indice} from "../../brand/copylab/tipografia";
import {Pieza, Foto, Velo} from "../../brand/copylab/lienzo";
import {Anotacion, Flecha} from "../../brand/copylab/mano";

export const People: React.FC = () => {
  asegurarFuentes();
  const {width: W} = useVideoConfig();
  const M = margen(W);

  return (
    <Pieza fondo={C.tinta} grano={0.4} >
      <Foto
        src="assets/copylab/people/escritorio-01.png"
        grado="flash"
        encuadre="38% 52%"
        zoom={1.28}
        dx={-26}
      />

      {/* Dos velos cortos, arriba y abajo. No ambientan: el índice y el pie
          caían sobre papel blanco quemado por el flash y no se leían. */}
      <Velo desde="arriba" fuerza={0.62} corte={0.87} />
      <Velo desde="abajo" fuerza={0.66} corte={0.87} />

      <Indice
        familia="People" ref="Copylab"
        color="rgba(242,244,246,0.82)"
        style={{position: "absolute", left: M, top: M}}
      />

      {/* Dice lo que la foto no dice. */}
      <Anotacion x={M + 22} y={868} texto={"acá estaba\nla buena"} size={78} rot={-5} />
      {/* Y esto señala dónde. */}
      <Flecha x={M + 300} y={952} w={230} h={190} grosor={7} semilla={23} rot={8} curva={0.8} />

      <div
        style={{
          position: "absolute", left: M, bottom: M,
          fontFamily: VOZ.data, fontSize: 22, fontWeight: 400,
          letterSpacing: "0.16em", textTransform: "uppercase",
          color: "rgba(242,244,246,0.5)",
        }}
      >
        Field notes · martes 19:40
      </div>
    </Pieza>
  );
};
