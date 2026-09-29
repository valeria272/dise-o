/**
 * QB · ST 17-10 · 25-10 · 31-10 · ESTÁTICA — «ST BANCO FALABELLA | CMR 40% LOS SÁBADOS»
 *
 * GRILLA (STORIES, 3 columnas en APROBADO, sin brief propio): contenido marca que se
 * republica la ST aprobada de CMR 40 %. El texto sale del brief de la misma promo
 * (col. 15-10, «ST ESTÁTICA – CMR FALABELLA 40% SÁBADOS»):
 *   ¡AHORA LOS SÁBADOS SE DISFRUTAN MÁS! · CMR FALABELLA · 40% dcto. · 30% dcto.
 *   pagando con débito Banco Falabella · Bajada: Tu panorama de sábado ahora tiene
 *   un nuevo beneficio · Legal: *Válido los sábados de octubre pagando con CMR…
 *   Visual: mesa servida, cocktails y platos para compartir, nocturno y cálido.
 *
 * Eli 29-09: «guíate de las referencias que da contenido, pero hay elementos que
 * conservar: logos, nombres importantes y legales».
 *
 * DIRECCIÓN DE ARTE
 *   · PLANTILLA APROBADA: «Pantallas QB CMR 40-30OFF 1080x1920» (Eli, ago-2026;
 *     `raw/hilton/qb/aprobadas/CMR 40-30OFF 1080x1920 150.png`). Se CALCA midiendo
 *     sobre la aprobada llevada a mesa (R-37, X-13): logo, titular de dos pesos
 *     (versal ExtraBold + Light del mismo cuerpo), sello «Oportunidad única», caja
 *     de filete #354A3A con «¡Pagando con CMR!» en curva, 40 % enorme con «dcto.»,
 *     franja verde «30% dcto. CON TU TARJETA DE DÉBITO BANCO FALABELLA», las cuatro
 *     tarjetas (recortadas de la aprobada, no redibujadas), bajada y legal.
 *   · Cambia sólo lo del brief: «miércoles» → «sábados», la bajada y el legal.
 *   · FOTO: el shooting de la carta de enero 2026 (R-40, va casi sin tocar), una
 *     por fecha para que la historia no salga idéntica tres veces: la mesa con
 *     schop + cóctel + carne (igual a la aprobada), el brindis y la mesa con papas
 *     trufadas. Foto real → sin «Imagen referencial».
 *   · PROMO → paid: todo el texto entre 250 y 1580 (E-06). Para que quepa, las
 *     tarjetas suben pegadas a la franja (en la aprobada flotaban 195 px más abajo).
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {QB_ASSETS, QB_CIFRAS} from "../../../brand/qb";
import {cargarFuentesQbOct, FotoQB, Legal, Linea, MESA, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_CMR40_DATA = {
  titular1: "¡AHORA LOS SÁBADOS",
  titular2: "SE DISFRUTAN MÁS!",
  etiqueta: "¡Pagando con CMR!",
  debito: ["CON TU TARJETA", "DE DÉBITO BANCO", "FALABELLA"],
  legal: "*Válido los sábados de octubre pagando con CMR. *Excluye compras con factura. *No contempla tope de descuento. *Promoción no acumulable con otras ofertas y beneficios.",
};

/** Una foto por fecha (todas del shooting de la carta, enero 2026). */
const FOTOS = {
  "17": {src: "ap-cmr17.jpg", zoom: 1.0, cx: 0.5, cy: 0.52},  // American Baby ribs 1
  "25": {src: "ap-cmr25.jpg", zoom: 1.0, cx: 0.5, cy: 0.45},  // Cerveza Atenea 2 (brindis)
  "31": {src: "ap-cmr31.jpg", zoom: 1.0, cx: 0.5, cy: 0.5},   // Papas trufadas 5
} as const;
export type QbCmr40Fecha = keyof typeof FOTOS;

/** Medidas de la aprobada en mesa, +30 px (el logo entra en la zona segura). */
const DY = 30;
const CAJA = {x: 268, y: 702 + DY, w: 549, h: 1202 - 702};
const FRANJA = {y: 1082 + DY, h: 120};
const FILETE = "#354A3A";
/** Las tarjetas suben 135 px: quedan a 30 px de la franja. */
const TARJETAS = {x: 352, y: 1262, w: 380};

/** Cifra en caja alta: `top`/`left` son el tope y el borde del GLIFO (métrica de
 *  Raleway ExtraBold medida en la ST 08: tope a 0,135 em, sangría 0,037 em). */
const Cifra: React.FC<{top: number; left: number; cuerpo: number; peso?: number; tracking?: string;
  children: React.ReactNode}> = ({top, left, cuerpo, peso = 800, tracking = "0", children}) => (
  <div style={{position: "absolute", top: top - 0.135 * cuerpo, left: left - 0.037 * cuerpo,
    whiteSpace: "nowrap", color: "#fff", fontFamily: "Raleway", fontWeight: peso, fontSize: cuerpo,
    lineHeight: 1, letterSpacing: tracking, ...QB_CIFRAS}}>
    {children}
  </div>
);

export const QbStAprobadaCmr40: React.FC<{fecha: QbCmr40Fecha}> = ({fecha}) => {
  const f = FOTOS[fecha];
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <FotoQB src={`assets/hilton/qb/oct/${f.src}`} ratio={3840 / 5760} zoom={f.zoom} cx={f.cx} cy={f.cy} />
      <Velo arriba={[700, 0.8]} abajo={[640, 0.85]} plano={0.12} />
      <Img src={staticFile(QB_ASSETS.logoBlanco)} style={{position: "absolute", top: 250, left: (MESA.w - 175) / 2, width: 175}} />
      {/* titular de dos pesos del mismo cuerpo, como la aprobada (versal 45 px) */}
      <Linea top={395 + DY - 17} cuerpo={63} peso={800} tracking="0.01em" interlinea={1}>{QB_CMR40_DATA.titular1}</Linea>
      <Linea top={470 + DY - 17} cuerpo={63} peso={300} tracking="0.01em" interlinea={1}>{QB_CMR40_DATA.titular2}</Linea>
      {/* caja: filete verde, vidrio oscuro, y la franja de débito que la cierra */}
      <div style={{position: "absolute", left: CAJA.x, top: CAJA.y, width: CAJA.w, height: CAJA.h,
        border: `4px solid ${FILETE}`, borderBottom: "none", borderRadius: "18px 18px 0 0",
        background: "rgba(0,0,0,.34)"}} />
      <div style={{position: "absolute", left: CAJA.x, top: FRANJA.y, width: CAJA.w, height: FRANJA.h, background: FILETE}} />
      <Img src={staticFile("assets/hilton/qb/oct/ou-logo.png")}
        style={{position: "absolute", left: 460, top: 595 + DY, width: 165, height: 163}} />
      {/* «¡Pagando con CMR!» en arco suave, como la aprobada (x 368–720, cumbre en 797) */}
      <svg style={{position: "absolute", left: 0, top: 0}} width={MESA.w} height={MESA.h}>
        <path id="qb-cmr40-arco" d={`M ${544 - 640} ${815 + DY + 640} A 640 640 0 0 1 ${544 + 640} ${815 + DY + 640}`} fill="none" />
        <text fill="#fff" fontFamily="Raleway" fontWeight={600} fontSize={40} textAnchor="middle">
          <textPath href="#qb-cmr40-arco" startOffset={(Math.PI * 640) / 2}>{QB_CMR40_DATA.etiqueta}</textPath>
        </text>
      </svg>
      <Cifra top={850 + DY} left={292} cuerpo={286} tracking="-0.05em">40</Cifra>
      <Cifra top={855 + DY} left={640} cuerpo={188}>%</Cifra>
      <Cifra top={1010 + DY} left={641} cuerpo={56}>dcto.</Cifra>
      {/* franja: 30 % + «dcto.» bajo el % + tres líneas en Bold */}
      <Cifra top={1100 + DY} left={316} cuerpo={111} tracking="-0.04em">30</Cifra>
      <Cifra top={1102 + DY} left={453} cuerpo={75}>%</Cifra>
      <Cifra top={1162 + DY} left={456} cuerpo={24} peso={700}>dcto.</Cifra>
      <div style={{position: "absolute", left: 537, top: 1100 + DY - 7, color: "#fff", fontFamily: "Raleway",
        fontWeight: 700, fontSize: 28.5, lineHeight: "30px", letterSpacing: "0.005em"}}>
        {QB_CMR40_DATA.debito.map((l) => <div key={l}>{l}</div>)}
      </div>
      <Img src={staticFile("assets/hilton/qb/oct/tarjetas-cmr-4.png")}
        style={{position: "absolute", left: TARJETAS.x, top: TARJETAS.y, width: TARJETAS.w, height: TARJETAS.w * 295 / 791}} />
      <Linea top={1426} cuerpo={37} peso={400} interlinea={1.12} ancho={900}>
        Tu panorama de sábado ahora<br />tiene un nuevo beneficio
      </Linea>
      <Legal top={1512} cuerpo={20}>{QB_CMR40_DATA.legal}</Legal>
    </AbsoluteFill>
  );
};
