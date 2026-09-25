/**
 * SANTA GOTA · «UNA GOTA. CAMBIA TODO.» — los 10 keyframes (primera entrega).
 *
 * Cada keyframe es UN cuadro del spot, con la dirección de arte del Production Bible V2:
 *   ANTES  (01–02) mediterráneo, cálido, luminoso, predecible.
 *   DESPUÉS (03–10) negro, acero, fuego, aceite dorado, verde ácido, naranja.
 * Las placas (comida, aceite, fuego, set) son generadas; el producto es SOLO el
 * packshot oficial. Copy y marca viven bajo la reserva de la huincha (y ≥ 216).
 *
 * Timecodes del guion técnico:
 *   01 00.0–02.5 EL CLICHÉ        06 08.0–09.5 FOOD 2 · carne
 *   02 02.5–04.0 LA GOTA          07 09.5–10.5 FOOD 3 · pasta
 *   03 04.0–05.0 CAMBIA TODO      08 10.5–12.5 EL ORIGEN · reveal
 *   04 05.0–06.5 NUEVO UNIVERSO   09 12.5–15.0 HERO
 *   05 06.5–08.0 FOOD 1 · pizza   10 15.0–20.0 FIRMA
 */
import React from "react";
import {Img, staticFile} from "remotion";
import {C, Copy, Fondo, HUINCHA_Y, Lima, LogoOficial, PLATES, PROD, Placa, Producto, RATIO, SAFE_X, Vineta, useSpot} from "./comun";
import {santagota as SG} from "../../../brand/santagota";

// ── Ajustes de placa (se calibran mirando la placa generada) ───────────────
export const CAL = {
  cliche: "01_gota_sola_v2.png",   // una sola gota suspendida (la v1 y el lote anterior dibujaban chorro)
  gota: "02_gota_sola_v2.png",     // la gota a 2 cm de la burrata, sola
  impacto: "03_impacto_v1.png",
  universo: "04_universo.png",
  pizza: "05_pizza_b_v2.png",      // ⚠ trae un cuello de botella arriba a la derecha: se recorta en KF05
  carne: "06_carne.png",
  pasta: "07_pasta.png",
  origenFondo: "08_origen_fondo_flip.png", // espejado: la sartén queda a la izquierda
  chorroPlaca: "08_chorro_negro.png", // original: el chorro va de arriba-der a abajo-izq
  estudio: "09_estudio_v1.png",
  pisoY: 760,          // fila donde la superficie reflectante recibe el producto (placa estudio)
  tip: {x: 1000, y: 560},       // punta de la boquilla
  botellaH: 780,
  botellaRot: -135,             // cuerpo hacia arriba-derecha, boquilla hacia la sartén (abajo-izq)
  chorro: {w: 845, ox: 845, oy: 88, rot: -7}, // el chorro nace en el borde derecho de la placa (y=18,6 %) y cae a 160°; −7° apunta al centro de la sartén
};

// 01 · EL CLICHÉ — todo quieto, la gota suspendida, sin marca, sin texto.
export const KF01: React.FC = () => {
  useSpot();
  return (
    <Fondo color="#2a1d10">
      <Placa src={CAL.cliche} />
    </Fondo>
  );
};

// 02 · LA GOTA — cae en slow motion. «UNA GOTA.» grande, jerarquía absoluta, muy poco tiempo.
export const KF02: React.FC = () => {
  useSpot();
  return (
    <Fondo color="#2a1d10">
      <Placa src={CAL.gota} />
      <Vineta op={0.45} lado="abajo" />
      <Copy x={SAFE_X} y={700} size={190} lh={0.9}>UNA GOTA.</Copy>
    </Fondo>
  );
};

// 03 · CAMBIA TODO — el impacto: corona líquida sobre negro; la luz ya cambió de universo.
export const KF03: React.FC = () => {
  useSpot();
  return (
    <Fondo>
      <Placa src={CAL.impacto} />
      <Vineta op={0.35} lado="abajo" />
      <Copy x={SAFE_X} y={700} size={190} lh={0.9}>CAMBIA <Lima>TODO.</Lima></Copy>
    </Fondo>
  );
};

// 04 · NUEVO UNIVERSO — sartén negra, verduras en el aire, flare de fuego real. Sin texto.
export const KF04: React.FC = () => {
  useSpot();
  return (
    <Fondo>
      <Placa src={CAL.universo} />
    </Fondo>
  );
};

// 05 · FOOD 1 — chorro sobre pizza. La boquilla queda fuera de cuadro. Sin texto.
export const KF05: React.FC = () => {
  useSpot();
  return (
    <Fondo>
      <Placa src={CAL.pizza} style={{transform: "scale(1.3)", transformOrigin: "0% 100%"}} />
    </Fondo>
  );
};

// 06 · FOOD 2 — aceite sobre carne a la parrilla, sizzle y fuego. Sin texto.
export const KF06: React.FC = () => {
  useSpot();
  return (
    <Fondo>
      <Placa src={CAL.carne} />
    </Fondo>
  );
};

// 07 · FOOD 3 — el aceite recorre la pasta a contraluz. Sin texto.
export const KF07: React.FC = () => {
  useSpot();
  return (
    <Fondo>
      <Placa src={CAL.pasta} />
    </Fondo>
  );
};

// 08 · EL ORIGEN — seguimos el chorro hasta la boquilla y por primera vez se ve SANTA GOTA.
//      Fondo generado + chorro generado sobre negro (mezcla screen) + packshot OFICIAL del 750.
//      La botella gira alrededor de la PUNTA de la boquilla (rotar no altera la proporción):
//      cuerpo hacia arriba-izquierda, boquilla apuntando a la sartén. Sin texto: el reveal es el producto.
export const KF08: React.FC = () => {
  useSpot();
  const tip = CAL.tip;            // punta de la boquilla en el cuadro
  const h = CAL.botellaH;         // alto de la botella (el ancho sale de la proporción real)
  const w = h / RATIO.s750;
  const ch = CAL.chorro;          // caja del chorro: nace en la punta y gira `rot` grados
  return (
    <Fondo>
      <Placa src={CAL.origenFondo} />
      <Vineta op={0.35} lado="der" />
      <Img src={staticFile(`${PLATES}/${CAL.chorroPlaca}`)} style={{
        position: "absolute", left: tip.x - ch.ox, top: tip.y - ch.oy, width: ch.w, height: ch.w * 9 / 16,
        mixBlendMode: "screen", transform: `rotate(${ch.rot}deg)`, transformOrigin: `${ch.ox}px ${ch.oy}px`, zIndex: 8,
      }} />
      <Img src={staticFile(`${PROD}/hero-750.png`)} style={{
        position: "absolute", left: tip.x - w / 2, top: tip.y, width: w, height: h, zIndex: 10,
        transform: `rotate(${CAL.botellaRot}deg)`, transformOrigin: "50% 0%",
        filter: "drop-shadow(0 18px 40px rgba(0,0,0,0.6))",
      }} />
    </Fondo>
  );
};

// 09 · HERO — las dos botellas oficiales sobre black studio reflectante. «SOMOS LA REVOLUCIÓN».
export const KF09: React.FC = () => {
  useSpot();
  const piso = CAL.pisoY;
  return (
    <Fondo>
      <Placa src={CAL.estudio} />
      <Producto src="hero-750.png" ratio={RATIO.s750} cx={640} pisoY={piso} h={760} z={12} />
      <Producto src="hero-500.png" ratio={RATIO.s500} cx={935} pisoY={piso + 6} h={660} z={11} />
      <Copy x={SAFE_X} y={470} size={118} align="right" lh={0.94}>SOMOS LA<br /><Lima>REVOLUCIÓN</Lima></Copy>
    </Fondo>
  );
};

// 10 · FIRMA — family shot + logo oficial + claim completo + URL. Latas sólo si el cliente aprueba.
export const KF10: React.FC<{latas?: boolean}> = ({latas = false}) => {
  useSpot();
  const piso = CAL.pisoY + 40;
  return (
    <Fondo>
      <Placa src={CAL.estudio} />
      {latas && <Producto src="hero-lata-cocinar.png" ratio={RATIO.lCoc} cx={330} pisoY={piso - 4} h={330} z={9} reflejo={0.2} />}
      {latas && <Producto src="hero-lata-aderezar.png" ratio={RATIO.lAde} cx={905} pisoY={piso - 4} h={330} z={9} reflejo={0.2} />}
      <Producto src="hero-750.png" ratio={RATIO.s750} cx={520} pisoY={piso} h={640} z={12} />
      <Producto src="hero-500.png" ratio={RATIO.s500} cx={775} pisoY={piso + 6} h={560} z={11} />
      <LogoOficial x={1130} y={Math.max(HUINCHA_Y + 40, 300)} w={620} />
      <Copy x={1130} y={720} size={62} lh={1.02}>SOMOS LA <Lima>REVOLUCIÓN</Lima><br />DEL ACEITE DE OLIVA.</Copy>
      <div style={{
        position: "absolute", left: 1130, top: 880, zIndex: 20, fontFamily: SG.fonts.display, fontWeight: 800, fontSize: 46,
        letterSpacing: "0.04em", color: C.lima, textShadow: "0 2px 16px rgba(0,0,0,0.6)",
      }}>{SG.url}</div>
    </Fondo>
  );
};

export const KF10Latas: React.FC = () => <KF10 latas />;
