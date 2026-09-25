/**
 * SANTA GOTA · «UNA GOTA. CAMBIA TODO.» — V3: sólo los 4 cuadros críticos (15-09-2026, noche).
 *
 * V2 aprobada en concepto. Regla global: MENOS EFECTOS = MÁS PREMIUM; nada debe parecer generado por IA.
 *   06 SARTÉN  flare breve y elegante (fuego −60 %), casi todo negro.
 *   07 PASTA   giro + hilo como transición, pero aceite fotográficamente REAL (translúcido, irregular).
 *   08 REVEAL  prohibido producto flotando: una mano real sostiene el squeeze horizontal desde fuera de
 *              cuadro. La mano y el envase se generan; el PACKSHOT OFICIAL va encima del envase generado y los
 *              dedos vuelven delante por máscara de piel (scripts/santagota-spot-mano.py). Nada redibujado.
 *   09/10 HERO beauty advertising: negro casi absoluto, botellas 30–40 % más grandes con profundidad entre
 *              ambas, superficie húmeda apenas visible, rim naranja/verde FINO en el packshot (no nubes de
 *              color), aceite desenfocado en primerísimo plano, copy editorial chico. El producto manda.
 * El resto de los cuadros sigue siendo la V2.
 */
import React from "react";
import {Img, staticFile} from "remotion";
import {C, Copy, Fondo, Lima, Placa, Producto, RATIO, SAFE_X, Vineta, useSpot} from "./comun";

const PL = "assets/santagota/spot/plates";

export const CAL3 = {
  sarten: "v3_sarten_flare_v1.png",
  pasta: "v3_pasta_real_v3.png",       // giro + hilo real; asoma una punta de dedo arriba-der → se recorta
  reveal: "v3_reveal_compuesto.png",   // salida de scripts/santagota-spot-mano.py (mano + packshot oficial + dedos)
  heroNegro: "v3_hero_negro_v2.png",   // piso húmedo con horizonte apenas visible
  heroFg: "v2_hero_fg_aceite_limpio.png",
  pisoY: 990,
  hilo: "v2_hilo_negro_limpio.png",
  tip: {x: 753, y: 510},               // punta de la boquilla oficial en el compuesto (lo imprime santagota-spot-mano.py)
};

/** Capa sobre negro en «screen» (brillo y clip EN la misma capa: un div envolvente rompe el blend). */
const Screen: React.FC<{src: string; x: number; y: number; w: number; rot?: number; op?: number; blur?: number; bright?: number; z?: number; clip?: string}> = ({src, x, y, w, rot = 0, op = 1, blur = 0, bright = 1, z = 8, clip}) => (
  <Img src={staticFile(`${PL}/${src}`)} style={{
    position: "absolute", left: x, top: y, width: w, height: w * 9 / 16, mixBlendMode: "screen", opacity: op, zIndex: z,
    transform: `rotate(${rot}deg)`, transformOrigin: "50% 50%", clipPath: clip,
    filter: `${blur ? `blur(${blur}px) ` : ""}${bright !== 1 ? `brightness(${bright})` : ""}` || undefined,
  }} />
);

// 06 · SARTÉN — flare corto y hermoso. Menos fuego = más caro.
export const V3_06: React.FC = () => { useSpot(); return <Fondo><Placa src={CAL3.sarten} /></Fondo>; };

// 07 · PASTA — el giro y el hilo real. El movimiento extraordinario viene de cámara y montaje, no de CGI.
export const V3_07: React.FC = () => { useSpot(); return <Fondo><Placa src={CAL3.pasta} style={{transform: "scale(1.16)", transformOrigin: "0% 100%"}} /><Vineta op={0.25} lado="izq" /></Fondo>; };

// 08 · REVEAL — la mano entra desde fuera de cuadro sosteniendo el squeeze. El producto existe físicamente.
export const V3_08: React.FC = () => {
  useSpot();
  const tp = CAL3.tip;
  return (
    <Fondo>
      <Placa src={CAL3.reveal} />
      {/* el hilo REAL (placa sobre negro) nace en la punta de la boquilla y cae */}
      <Screen src={CAL3.hilo} x={tp.x - 0.516 * 2000} y={tp.y - 6} w={2000} bright={1.4} z={7} clip="inset(0 0 12% 0)" />
    </Fondo>
  );
};

// 09/10 · HERO — beauty shot. Negro, producto enorme con profundidad, rim fino, aceite en foreground, mucho aire.
const Hero3: React.FC<{segundo?: boolean}> = ({segundo = false}) => {
  useSpot();
  const piso = CAL3.pisoY;
  return (
    <Fondo>
      <Placa src={CAL3.heroNegro} op={0.9} />
      {/* la de atrás (500, verde): un poco más chica y un pelo fuera de foco = profundidad real */}
      <div style={{position: "absolute", inset: 0, zIndex: 10, filter: "blur(1.4px) brightness(0.86)"}}>
        <Producto src="hero3-500.png" ratio={RATIO.s500} cx={900} pisoY={piso - 58} h={720} z={10} reflejo={0.14} />
      </div>
      {/* la de adelante (750, naranja): manda */}
      <Producto src="hero3-750.png" ratio={RATIO.s750} cx={610} pisoY={piso} h={930} z={12} reflejo={0.16} />
      {/* hilo de aceite dorado desenfocado en primerísimo plano */}
      <Screen src={CAL3.heroFg} x={-1500} y={860} w={2800} rot={-26} op={0.24} blur={46} z={15} />
      {/* copy editorial: chico, con aire, a la derecha, bajo la reserva de huincha */}
      <Copy x={SAFE_X + 40} y={segundo ? 560 : 640} size={64} weight={800} align="right" lh={1.06}
            style={{letterSpacing: "0.02em", textShadow: "none"}}>
        SOMOS LA<br /><Lima>REVOLUCIÓN</Lima>
        {segundo ? <><br /><span style={{fontWeight: 300, letterSpacing: "0.06em"}}>DEL ACEITE DE OLIVA.</span></> : null}
      </Copy>
    </Fondo>
  );
};
export const V3_09: React.FC = () => <Hero3 />;
export const V3_10: React.FC = () => <Hero3 segundo />;
export {C};
