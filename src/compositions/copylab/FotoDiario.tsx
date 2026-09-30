// ============================================================================
// COPYWRITERS · «NADIE LEE EL DIARIO.» — INTERNET DEPT.
// ----------------------------------------------------------------------------
// DIRECCIÓN DE ARTE
//
// Es la pieza que prueba la regla R-17: el diseño no va ENCIMA de la foto, vive
// DENTRO del mundo fotografiado. Primero se decide dónde vive la idea (en un
// diario), después qué soporte la vuelve real (un diario en blanco, de verdad,
// sobre hormigón), y recién al final se compone.
//
// Por eso el texto está en el PLANO del papel: girado 11°, que es la
// inclinación medida del borde superior de la hoja en la fotografía. Un texto
// horizontal sobre un papel inclinado delata el montaje al instante — y ahí la
// pieza deja de ser un diario y pasa a ser un archivo con una foto de fondo.
//
// La cabecera «INTERNET DEPT.» es del board. El copy es de los aprobados por
// Valeria el 24-09 (A-04). La mano rosa es lo único que no está impreso: es
// alguien rayando el diario, que es exactamente el chiste.
//
// Territorio: EDITORIAL. Formato 1080×1350.
// Foto: Seedream 5 Pro (30-09-2026) — papel en blanco, SIN texto generado por
// IA. Toda la letra que se lee es del sistema.
// ============================================================================
import React from "react";
import {AbsoluteFill} from "remotion";
import {C2, VOZ2, asegurarFuentesV2} from "../../brand/copylab/sistemaV2";
import {Foto} from "../../brand/copylab/piezasV2";

/** La inclinación del papel en la foto, medida sobre el borde superior de la
 *  hoja: de (353,255) a (968,374) en el lienzo → atan(119/615) ≈ 11°. */
const PLANO = 11;

export const FotoDiario: React.FC = () => {
  asegurarFuentesV2();
  return (
    <AbsoluteFill style={{background: C2.negro}}>
      <Foto src="assets/copywriters/v2/03-diario.png" foco="50% 45%" />

      {/* Todo lo impreso viaja en un solo bloque girado al plano del papel:
          así la cabecera, la regla y el titular comparten una misma retícula,
          igual que en un diario real. */}
      <div style={{
        position: "absolute", left: 376, top: 300,
        transform: `rotate(${PLANO}deg)`, transformOrigin: "left top",
        width: 560,
      }}>
        <div style={{
          fontFamily: VOZ2.titular, fontWeight: 700, fontSize: 62,
          color: C2.negro, textTransform: "uppercase", letterSpacing: 0.5,
          lineHeight: 1,
        }}>
          INTERNET DEPT.
        </div>

        <div style={{
          borderTop: `2px solid ${C2.negro}`, marginTop: 10,
        }} />

        <div style={{
          marginTop: 26,
          fontFamily: VOZ2.titular, fontWeight: 700, fontSize: 92,
          lineHeight: 0.88, color: C2.negro, textTransform: "uppercase",
        }}>
          NADIE LEE<br />EL DIARIO.
        </div>
      </div>

      {/* La mano NO viaja en el plano del papel: está rayada encima, después de
          impreso. Por eso lleva su propio giro, más suave que el de la hoja. */}
      <div style={{
        position: "absolute", left: 318, top: 812,
        transform: `rotate(${PLANO - 3}deg)`, transformOrigin: "left top",
        fontFamily: VOZ2.mano, fontWeight: 700, fontSize: 52,
        color: C2.rosa, lineHeight: 1.1, textTransform: "uppercase",
      }}>
        TÚ ACABAS<br />DE LEER ESTO.
      </div>

    </AbsoluteFill>
  );
};
