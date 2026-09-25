/**
 * QB · ST 08-10 · 18:00 · ESTÁTICA — DESCUENTO CMR FALABELLA
 *
 * BRIEF (STORIES col. F, OK PARA DISEÑAR, sin comentario):
 *   Composición más editorial y atmosférica, la barra o una escena interior de QB
 *   con fondo desenfocado, luces cálidas y ambiente nocturno. Panorama atractivo
 *   y accesible cualquier día. Puede aparecer un cocktail protagonista en primer
 *   plano. Texto: TU MESA TIENE BENEFICIOS / TODOS LOS DÍAS · CMR FALABELLA ·
 *   20% OFF · TODOS LOS DÍAS · legal.
 *
 * REFERENCIA: Pinterest 344877283982097898 (Buenavista) — escena de barra
 * oscura con bokeh, titular grande arriba, datos abajo.
 *
 * ⭐⭐ RONDA DE ELI 25-09: «lo mismo con lo del 8 de octubre, el banco ya está
 * aprobado, solamente hay que de repente hacer cambios de fotografías».
 *
 * DIRECCIÓN DE ARTE
 *   · PLANTILLA APROBADA: «BCO CMR 1080×1920» (PANTALLAS BANCOS QB / BCO CMR):
 *     sellos «Oportunidad única» + QB montados en el filete, marco de vidrio,
 *     «¡Todos los días!» en Bell MT itálica, el 20 % enorme con «dcto.», la franja
 *     verde «Ven y disfruta tu beneficio con Banco Falabella», el bloque blanco
 *     «Pagando con» + chips CMR / Débito, y los logos club de restaurantes |
 *     Banco Falabella. Medidas tomadas del PNG aprobado.
 *   · Elementos originales, no redibujados: «ou-logo.png» (Links del editable de
 *     bancos), chips recortados de la aprobada a resolución completa, logos club
 *     de restaurantes / Banco Falabella rasterizados del .ai de «LOGOS FALABELLA».
 *   · FOTO NUEVA del shooting de la carta de enero 2026 («Cerveza Atenea 26»):
 *     el trago rojo protagonista con las plantas oscuras detrás, como la
 *     aprobada. Sin gradación.
 *   · Titular y legal = los del brief. En la aprobada el titular (206–293) y el
 *     legal (1819) caían fuera de la zona segura: acá todo el TEXTO entra en
 *     250 · 340. PROMO → paid.
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {QB_ASSETS, QB_BOTON_FONDO} from "../../../brand/qb";
import {cargarFuentesQbOct, FotoQB, Legal, Linea, MESA, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST08_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "TU MESA TIENE BENEFICIOS TODOS LOS DÍAS",
  etiqueta: "¡Todos los días!",
  texto: "Ven y disfruta tu beneficio con Banco Falabella",
  legal: "Sujeto a consumo de alimentos. Promoción no acumulable con otras ofertas y beneficios.",
  },
};

/** Medidas de la plantilla aprobada, en mesa 1080×1920. */
const MARCO = {x: 168, y: 643, w: 744, h: 730};
const FRANJA = {y: 1080, h: 132};
const FILETE = "#36493B";
const s = (f: string) => staticFile(`assets/hilton/qb/oct/${f}`);

export const QbSt08Cmr: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/08-cmr.jpg" ratio={2250 / 3375} zoom={1.15} cx={0.42} cy={0.62} />
    <Velo arriba={[560, 0.75]} abajo={[520, 0.8]} />
    <Linea top={262} cuerpo={70} peso={700} interlinea={1.08}>TU MESA TIENE</Linea>
    <Linea top={338} cuerpo={70} peso={700} interlinea={1.08}>BENEFICIOS</Linea>
    <Linea top={414} cuerpo={70} peso={700} interlinea={1.08}>TODOS LOS DÍAS</Linea>
    {/* marco: arriba vidrio, franja verde, bloque blanco */}
    <div style={{position: "absolute", left: MARCO.x, top: MARCO.y, width: MARCO.w, height: MARCO.h,
      border: `6px solid ${FILETE}`, borderRadius: 26, overflow: "hidden", background: "rgba(0,0,0,.28)"}}>
      <div style={{position: "absolute", left: 0, right: 0, top: FRANJA.y - MARCO.y - 6, height: FRANJA.h,
        background: QB_BOTON_FONDO}} />
      <div style={{position: "absolute", left: 0, right: 0, top: FRANJA.y + FRANJA.h - MARCO.y - 6, bottom: 0,
        background: "#fff"}} />
    </div>
    <Img src={s("ou-logo.png")} style={{position: "absolute", left: 374, top: 576, width: 144, height: 142}} />
    <div style={{position: "absolute", left: 562, top: 576, width: 146, height: 139, borderRadius: 28,
      background: QB_BOTON_FONDO, display: "flex", alignItems: "center", justifyContent: "center"}}>
      <Img src={staticFile(QB_ASSETS.logoBlanco)} style={{width: 100}} />
    </div>
    <div style={{position: "absolute", top: 728, left: 0, width: MESA.w, textAlign: "center",
      transform: "rotate(-4deg)", color: "#fff", fontFamily: "BellMT", fontStyle: "italic", fontSize: 54}}>
      {QB_ST08_DATA.pieza.etiqueta}
    </div>
    <div style={{position: "absolute", top: 790, left: 0, width: MESA.w, display: "flex",
      justifyContent: "center", alignItems: "flex-start", color: "#fff", fontFamily: "Raleway",
      fontWeight: 800, textShadow: "0 3px 20px rgba(0,0,0,.35)"}}>
      <span style={{fontSize: 290, lineHeight: 0.86, letterSpacing: "-0.03em"}}>20</span>
      <span style={{display: "flex", flexDirection: "column", alignItems: "flex-end", marginLeft: 4}}>
        <span style={{fontSize: 170, lineHeight: 0.9}}>%</span>
        <span style={{fontSize: 62, lineHeight: 1, marginTop: 8}}>dcto.</span>
      </span>
    </div>
    <Linea top={1106} cuerpo={37} peso={700} interlinea={1.2} ancho={640} sombra={false}>
      Ven y disfruta tu beneficio<br />con Banco Falabella
    </Linea>
    <Linea top={1222} cuerpo={22} peso={700} color="#333" sombra={false}>Pagando con</Linea>
    <Img src={s("chips-cmr-debito.png")} style={{position: "absolute", left: (MESA.w - 300) / 2, top: 1256, width: 300, height: 90}} />
    <Img src={s("logo-club-restaurantes-bf.png")} style={{position: "absolute", left: (MESA.w - 628) / 2, top: 1416, width: 628, height: 80}} />
    <Legal top={1530} cuerpo={22}>{QB_ST08_DATA.pieza.legal}</Legal>
  </AbsoluteFill>
);
