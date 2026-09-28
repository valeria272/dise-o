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
 *
 * ⭐ RONDA DE ELI 28-09: «el texto de todos los días tiene que quedar igual de
 *   curvo, con esa curvatura que estaba… el 20 % de descuento déjalo como estaba
 *   el original». Antes iba girado −4° en recta y el 20 medía 170 px (cifras de
 *   estilo antiguo, sin QB_CIFRAS). Ahora la curva y el 20 % salen MEDIDOS de la
 *   aprobada: arco de radio 384, 20 de 201 px, % pegado al 0, «dcto.» en la base.
  *
 * ⭐ RONDA 5 DE ELI 28-09: «quiero que sea una foto real de barra que tengamos» →
 *   la barra iluminada del shooting «QB oct» (sesión terraza 10-10, foto 31), el
 *   cóctel naranjo con romero asomando arriba a la izquierda como en la aprobada.
 *   Y «el ¡Todos los días! solapa el 2 del 20» → la curva sube 14 px.
 * ⭐ RONDA 4 DE ELI 28-09: «revisando bien las referencias no se asemeja… lo mismo
 *   para todas las historias». De la ref (Buenavista) se toma el fondo —la barra
 *   de noche con las botellas encendidas y el trago sobre la madera— y el titular:
 *   una línea chica, una palabra en caja alta muy pesada y una caligráfica que la
 *   cruza. Con las voces de QB: Raleway ExtraBold 800 (el
 *   más pesado del paquete) + Brushwell. El marco, la curva, el 20 % y los logos
 *   de la aprobada no se tocan. (La foto de la r4 era Seedream: la r5 la cambió
 *   por la barra real.)
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {QB_ASSETS, QB_BOTON_FONDO, QB_CIFRAS} from "../../../brand/qb";
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
const ARCO_R = 384;
/** Cumbre del arco. r5 (Eli 28-09): «que no toque el 2 del 20» → sube 14 px (era 769). */
const CUMBRE = 755;
const ETQ_CUERPO = 54;
const ETQ_TRACK = -1.2;
/** Posición del bloque del descuento: `y` y `x` son el tope y el borde del GLIFO
 *  (la caja se corrige con MET, la métrica medida de Raleway ExtraBold). */
const DCTO = {
  veinte: {x: 306, y: 810, c: 280},
  pct: {x: 636, y: 817, c: 190},
  dcto: {x: 644, y: 969, c: 57},
};
/** Con lineHeight 1 la base cae a 0,853 em (asc 940, desc 234) y la cifra de caja
 *  alta mide 0,718 em: su tope queda a 0,135 em de la caja. Lado = sangría del 2. */
const MET = {tope: 0.135, lado: 0.037};
const Cifra: React.FC<{top: number; left: number; cuerpo: number; tracking?: string; children: React.ReactNode}> = ({
  top, left, cuerpo, tracking = "0", children,
}) => (
  <div style={{position: "absolute", top: top - MET.tope * cuerpo, left: left - MET.lado * cuerpo,
    whiteSpace: "nowrap", color: "#fff", fontFamily: "Raleway", fontWeight: 800, fontSize: cuerpo,
    lineHeight: 1, letterSpacing: tracking, textShadow: "0 3px 20px rgba(0,0,0,.35)", ...QB_CIFRAS}}>
    {children}
  </div>
);
const s = (f: string) => staticFile(`assets/hilton/qb/oct/${f}`);

export const QbSt08Cmr: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/08-cmr-barra.jpg" ratio={3000 / 2000} zoom={0.75} cx={0.491} cy={0.993} libre />
    {/* la foto sube para que el cóctel asome arriba a la izquierda: su canto se funde */}
    <div style={{position: "absolute", left: 0, right: 0, top: 760, height: 1160,
      background: "linear-gradient(180deg, rgba(0,0,0,0) 0%, #000 18%, #000 100%)"}} />
    <Velo arriba={[560, 0.75]} abajo={[520, 0.8]} />
    {/* r4: titular como la ref — línea chica + palabra pesada + caligráfica que la cruza */}
    <Linea top={258} cuerpo={44} peso={700} tracking="0.06em">TU MESA TIENE</Linea>
    <Linea top={302} cuerpo={124} peso={800} tracking="-0.02em" interlinea={1}>BENEFICIOS</Linea>
    <Linea top={404} cuerpo={96} familia="Brushwell" interlinea={1}>todos los días</Linea>
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
    {/* «¡Todos los días!» en CURVA, calcada de la aprobada: la línea base es un
        arco de radio 384 con la cumbre en (545, CUMBRE); el texto se centra en x 554 */}
    <svg style={{position: "absolute", left: 0, top: 0}} width={MESA.w} height={MESA.h}>
      <path id="qb-st08-arco" d={`M ${545 - ARCO_R} ${CUMBRE + ARCO_R} A ${ARCO_R} ${ARCO_R} 0 0 1 ${545 + ARCO_R} ${CUMBRE + ARCO_R}`} fill="none" />
      <text fill="#fff" fontFamily="BellMT" fontStyle="italic" fontSize={ETQ_CUERPO} letterSpacing={ETQ_TRACK}
        textAnchor="middle" style={{fontVariantLigatures: "none"}}>
        <textPath href="#qb-st08-arco" startOffset={(Math.PI * ARCO_R) / 2 - 3}>{QB_ST08_DATA.pieza.etiqueta}</textPath>
      </text>
    </svg>
    {/* el 20 % de la aprobada: cifras de caja alta, 20 de 201 px de alto (tope 810),
        % pegado al 0 (tope 817) y «dcto.» bajo el % sobre la línea base del 20 */}
    <Cifra top={DCTO.veinte.y} left={DCTO.veinte.x} cuerpo={DCTO.veinte.c} tracking="-0.069em">20</Cifra>
    <Cifra top={DCTO.pct.y} left={DCTO.pct.x} cuerpo={DCTO.pct.c}>%</Cifra>
    <Cifra top={DCTO.dcto.y} left={DCTO.dcto.x} cuerpo={DCTO.dcto.c}>dcto.</Cifra>
    <Linea top={1106} cuerpo={37} peso={700} interlinea={1.2} ancho={640} sombra={false}>
      Ven y disfruta tu beneficio<br />con Banco Falabella
    </Linea>
    <Linea top={1222} cuerpo={22} peso={700} color="#333" sombra={false}>Pagando con</Linea>
    <Img src={s("chips-cmr-debito.png")} style={{position: "absolute", left: (MESA.w - 300) / 2, top: 1256, width: 300, height: 90}} />
    <Img src={s("logo-club-restaurantes-bf.png")} style={{position: "absolute", left: (MESA.w - 628) / 2, top: 1416, width: 628, height: 80}} />
    <Legal top={1530} cuerpo={22}>{QB_ST08_DATA.pieza.legal}</Legal>
  </AbsoluteFill>
);
