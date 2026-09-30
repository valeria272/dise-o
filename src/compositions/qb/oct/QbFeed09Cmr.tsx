/**
 * QB · FEED 09-10 · CARRUSEL — «HOY INVITA TU TARJETA» · CMR FALABELLA  (C3 S1 N°1–N°3)
 *
 * BRIEF (grilla octubre, FEED col. E, OK PARA DISEÑAR desde el 29-09 noche):
 *   SLIDE 1 — PORTADA · Visual: ambiente QB con mesa servida, cocktails y platos
 *     protagonistas; cálida y nocturna, panorama y no estética bancaria.
 *     Texto: HOY INVITA TU TARJETA. Beneficios especiales para disfrutar en QB.
 *   SLIDE 2 — (rotulado «BANCO DE CHILE», pero el texto es CMR) · Visual: mesa más
 *     premium, plato protagonista y copas; el beneficio como información principal.
 *     Texto: CMR FALABELLA 40% dcto. Sábados pagando con tu tarjeta CMR · 30%
 *     pagando con débito Falabella.
 *   SLIDE 4 — CIERRE / CTA · Visual: ambiente de QB, mesa servida y personas
 *     compartiendo. Texto: YA TIENES EL BENEFICIO. AHORA ARMA EL PLAN. RESERVA AHORA.
 *   Legal: *Válido los sábados de octubre pagando con CMR. *Excluye compras con
 *     factura. *No contempla tope de descuento. *Promoción no acumulable…
 *   (No trae slide 3: van tres láminas.)
 * COMENTARIO DEL CLIENTE: «que sea solo de CMR 40 % junto a débito 30 % como
 *   teníamos en agosto y septiembre, sin mezclar con los otros bancos».
 * SCARLETTE (hilo en FEED!E14, 29-09): «incluir este contenido porfis».
 * ELI (29-09): «guíate de los que ya teníamos en bancos, de la referencia, que se
 *   vea bien la jerarquía y la diagramación, hazlo claro, cuidado con los legales».
 *
 * DIRECCIÓN DE ARTE
 *   · La N°2 es la CMR 40-30OFF APROBADA (R-37): el mismo bloque, trasladado
 *     (`BloqueCmr40`), con su titular de dos pesos. Nada redibujado.
 *   · N°1 y N°3 hablan igual: titular en dos pesos de Raleway (ExtraBold + Light,
 *     mismo cuerpo, como «¡AHORA LOS SÁBADOS / SE DISFRUTAN MÁS!») y una bajada.
 *     Dos voces por pieza: Raleway y nada más (Eli 29-09: «no usar tantas
 *     tipografías»).
 *   · FOTOS reales del shooting de la carta ene-2026 (R-40, sin «Imagen
 *     referencial»): American Baby ribs 4 (schop + spritz + ribs) · Entraña criolla 1
 *     (tinto + entraña, la mesa «más premium») · Cerveza Atenea 2 (el brindis sobre
 *     la mesa servida).
 *   · El legal va SÓLO en la N°2, que es donde está la promo, en dos líneas cortadas
 *     por frase (sin palabras solas). Zona segura de feed: texto ≤ 1188.
 *
 * ⭐⭐ RONDA 24 — ELI 30-09: «en los tres tenemos el logo: solamente en la portada» ·
 *   «coherencia en jerarquía con los títulos en posiciones, para que se vea recto hacia
 *   los siguientes slides y tenga continuidad; puede ser en la portada con la segunda» ·
 *   «un plato o una escena del shooting de platos, puedes utilizar uno; la última puede
 *   variar con otro tipo de imagen» · la referencia (el brindis de la N°3) «bastante bien».
 *   → Logo SÓLO en la N°1. Los tres titulares con la MISMA medida: tope y=200, Raleway 68
 *     (ExtraBold arriba, Light abajo; «CMR FALABELLA» en ExtraBold). 68 porque la línea más
 *     larga («YA TIENES EL BENEFICIO.», 849 px medido) cabe en la columna de 960.
 *   → N°1 + N°2 = UNA foto del shooting de la carta: «American Baby ribs 11» (horizontal:
 *     schop y spritz, dos manos tomando las ribs), partida en panorama 2160 px entre las
 *     dos láminas, con el mismo velo en ambas para que el corte no se note. N°3 sigue con
 *     el brindis.
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {QB_ASSETS} from "../../../brand/qb";
import {BloqueCmr40} from "./QbStAprobadaCmr40";
import {BotonVerde, cargarFuentesQbOct, Legal, Linea, MESA, Velo} from "./QbOctKit";
import {FEED, FotoFeed} from "./QbFeedKit";

cargarFuentesQbOct();

const QB_FEED09_DATA: Record<string, Record<string, string>> = {
  g1: {
  titular1: "HOY INVITA",
  titular2: "TU TARJETA",
  bajada: "Beneficios especiales para disfrutar en QB",
  },
  g2: {
  titular1: "CMR FALABELLA",
  texto: "Sábados pagando con tu tarjeta CMR",
  legal: "*Válido los sábados de octubre pagando con CMR. *Excluye compras con factura.",
  legal2: "*No contempla tope de descuento. *Promoción no acumulable con otras ofertas y beneficios.",
  },
  g3: {
  titular1: "YA TIENES EL BENEFICIO.",
  titular2: "AHORA ARMA EL PLAN",
  cta: "RESERVA AHORA",
  },
};

/** Foto 2:3 del shooting sobre la mesa 4:5 (object-fit, sin scale()). */
const Foto: React.FC<{src: string; cy?: number}> = ({src, cy = 0.5}) => (
  <FotoFeed src={`assets/hilton/qb/oct/${src}`} pos={`50% ${cy * 100}%`} />
);

/** r24: una foto partida entre N°1 y N°2 (panorama 2160 px), sin scale(). */
const PANO = {w: FEED.w * 2, h: FEED.w * 2 * 2 / 3};
const Panorama: React.FC<{lado: 0 | 1}> = ({lado}) => (
  <Img src={staticFile("assets/hilton/qb/oct/feed09-pano-ribs11.jpg")}
    style={{position: "absolute", left: -lado * FEED.w, top: (FEED.h - PANO.h) / 2, width: PANO.w, height: PANO.h}} />
);
/** r24: el mismo velo en N°1 y N°2, para que la unión del panorama no salte. */
const VeloPano: React.FC = () => <Velo arriba={[560, 0.88]} abajo={[560, 0.85]} plano={0.15} />;

/** r24 (Eli 30-09): los tres titulares a la misma altura y el mismo cuerpo. */
const TIT = {top: 200, cuerpo: 68, paso: 76};

const Logo: React.FC<{top: number}> = ({top}) => (
  <Img src={staticFile(QB_ASSETS.logoBlanco)} style={{position: "absolute", top, left: (FEED.w - 150) / 2, width: 150}} />
);

export const QbFeed09CmrG1: React.FC = () => {
  const d = QB_FEED09_DATA.g1;
  return (
    <AbsoluteFill style={{background: "#000", width: FEED.w, height: FEED.h}}>
      <Panorama lado={0} />
      <VeloPano />
      <Logo top={58} />
      <Linea top={TIT.top} cuerpo={TIT.cuerpo} peso={800} tracking="0.01em" interlinea={1}>{d.titular1}</Linea>
      <Linea top={TIT.top + TIT.paso} cuerpo={TIT.cuerpo} peso={300} tracking="0.01em" interlinea={1}>{d.titular2}</Linea>
      <Linea top={TIT.top + TIT.paso * 2 + 16} cuerpo={34} italica peso={400}>{d.bajada}</Linea>
    </AbsoluteFill>
  );
};

/** El bloque de la aprobada va 380 px más arriba que en la historia. */
const SUBE_BLOQUE = -350; // r24: baja 30 para dejar aire bajo el titular (y=200)

export const QbFeed09CmrG2: React.FC = () => {
  const d = QB_FEED09_DATA.g2;
  return (
    <AbsoluteFill style={{background: "#000", width: FEED.w, height: FEED.h}}>
      <Panorama lado={1} />
      <VeloPano />
      {/* r24: la mano de la ribs asomaba dentro del marco → sombra detrás del bloque, que se
          apaga antes del borde izquierdo para no cortar la unión con la N°1 */}
      <div style={{position: "absolute", left: 0, top: 0, width: FEED.w, height: FEED.h,
        background: "radial-gradient(ellipse 520px 560px at 540px 640px, rgba(0,0,0,.72) 0%, rgba(0,0,0,.55) 55%, rgba(0,0,0,0) 100%)"}} />
      <Linea top={TIT.top} cuerpo={TIT.cuerpo} peso={800} tracking="0.01em" interlinea={1}>{d.titular1}</Linea>
      <div style={{position: "absolute", left: 0, top: 0, width: MESA.w, height: FEED.h, overflow: "hidden"}}>
        <BloqueCmr40 dy={SUBE_BLOQUE} />
      </div>
      <Linea top={1070} cuerpo={34} peso={600}>{d.texto}</Linea>
      <Legal top={1128} cuerpo={19}>{d.legal}<br />{d.legal2}</Legal>
    </AbsoluteFill>
  );
};

export const QbFeed09CmrG3: React.FC = () => {
  const d = QB_FEED09_DATA.g3;
  return (
    <AbsoluteFill style={{background: "#000", width: FEED.w, height: FEED.h}}>
      <Foto src="ap-cmr25.jpg" cy={0.55} />
      <Velo arriba={[600, 0.88]} abajo={[420, 0.7]} />
      <Linea top={TIT.top} cuerpo={TIT.cuerpo} peso={800} tracking="0.01em" interlinea={1}>{d.titular1}</Linea>
      <Linea top={TIT.top + TIT.paso} cuerpo={TIT.cuerpo} peso={300} tracking="0.01em" interlinea={1}>{d.titular2}</Linea>
      <BotonVerde top={1040} ancho={520} alto={92} cuerpo={40}>{d.cta}</BotonVerde>
    </AbsoluteFill>
  );
};
