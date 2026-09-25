/**
 * SANTA GOTA · «UNA GOTA. CAMBIA TODO.» — keyframes V2 (segunda dirección creativa, 15-09-2026).
 *
 * Lo que cambió respecto a la V1 (feedback de Valeria):
 *   NORMALIDAD → GOTA → IMPACTO IMPOSIBLE → EL MUNDO CAMBIA → CAOS GASTRONÓMICO CONTROLADO
 *   → descubrimos que Santa Gota lo provocó todo.
 *   - El big bang (04) es EL PLANO: funciona congelado como KV.
 *   - Food con tres acciones distintas y conectadas: diagonal (pizza) · flash (sartén) · giro (pasta).
 *   - Códigos de marca sembrados antes del reveal: silueta de la boquilla oficial (05), naranja del
 *     fuego (06), verde ácido en la luz (07).
 *   - Reveal como respuesta a una pregunta: hilo → boquilla (08a) → CLICK → botella entera (08b).
 *   - Hero carísimo: negro absoluto, halos por color, aceite desenfocado en primer plano; copy en dos beats.
 *   - La gota como gesto propietario: abre (02) y cierra (11) — el PLOP es el punto de Santa Gota.
 *
 * Montaje aprobado (timecodes de Valeria):
 *   01 00.00–02.00 CLICHÉ           07 08.30–10.20 PASTA · giro + hilo
 *   02 02.00–03.20 LA GOTA          08a 10.20–12.70 REVEAL · la boquilla
 *   03 03.20       PLOP             08b            REVEAL · CLICK · SANTA GOTA
 *   04 03.20–05.00 BIG BANG (KV)    09 12.70–15.50 HERO · SOMOS LA REVOLUCIÓN
 *   05 05.00–06.50 PIZZA · diagonal 10 15.50–18.20 HERO · DEL ACEITE DE OLIVA.
 *   06 06.50–08.30 SARTÉN · flash   11 18.20–20.00 FIRMA · gota · PLOP · negro
 *
 * Producto: SOLO packshot oficial (escala uniforme). Copy y logo bajo la reserva de huincha (y ≥ 216).
 */
import React from "react";
import {Img, staticFile} from "remotion";
import {C, Copy, Fondo, HUINCHA_Y, Lima, LogoOficial, PLATES, PROD, Placa, Producto, RATIO, SAFE_X, Vineta, useSpot} from "./comun";
import {santagota as SG} from "../../../brand/santagota";

// ── Calibración (se ajusta mirando cada placa generada) ────────────────────
export const CAL2 = {
  cliche: "01_gota_sola_v2.png",
  gota: "v2_gota_descenso_v2.png",     // v1 volvió a dibujar una botella en el fondo
  gotaFirma: "v2_gota_firma_v1_limpio.png",     // la gota sola sobre negro (screen) — gesto propietario
  plop: "v2_plop_v1.png",
  bigbang: "v2_bigbang_b_v1.png",      // EL KV: columna + anillo con fuego + el mundo mediterráneo vivo en los bordes (v2_bigbang_v2 = plato ardiendo, alternativo)
  pizza: "v2_pizza_limpia_v2.png",     // sin chorro (el hilito que igual dibujó arriba se recorta): la diagonal se compone
  chorroDiag: "08_chorro_negro_limpio.png",    // arriba-der → abajo-izq, sobre negro (screen)
  sarten: "v2_sarten_flash_v1.png",
  pasta: "v2_pasta_giro_v2.png",       // el tenedor gira; el hilo que envuelve el giro se compone encima
  revealVacio: "v2_reveal_vacio.png",
  hilo: "v2_hilo_negro_limpio.png",              // hilo vertical sobre negro (screen)
  heroSet: "v2_hero_set_v1.png",       // naranja izq / verde der, como el orden de las botellas
  heroFg: "v2_hero_fg_aceite_limpio.png",        // aceite desenfocado en primer plano (screen)
  pisoY: 960,                             // el horizonte de luz del set está en y=813: el piso queda delante, el halo detrás
  // 05: silueta fugaz de la boquilla oficial cruzando en diagonal, muy desenfocada, en primer plano
  boquilla05: {tipX: 1300, tipY: 250, h: 900, rot: -140, blur: 6, op: 0.9},   // SILUETA fugaz: enorme, entra por la esquina, a contraluz
  chorro05: {w: 700, rot: -21},                                                // el chorro grueso (placa arriba-der → abajo-izq) nace en la punta y cae al queso (~1000, 520)
  // 08a: la boquilla oficial en macro, el hilo sube desde la punta
  boquilla08: {cx: 520, tipY: 540, h: 1400, rot: -100}, // horizontal: la tapa entra desde la derecha y SALE por el borde (no se ve el corte), la punta a la izquierda
  // 08b: la botella entera entra a cuadro, inclinada, enorme
  botella08: {tipX: 470, tipY: 600, h: 1480, rot: -100}, // squeeze horizontal como se usa de verdad, enorme, cruza el cuadro (dir = (−sin θ, cos θ))
};

/** Capa sobre negro mezclada en «screen» (chorros, gota, halos): lo negro desaparece. */
const Screen: React.FC<{src: string; x: number; y: number; w: number; rot?: number; op?: number; blur?: number; bright?: number; z?: number; origen?: string; flip?: boolean; clip?: string}> = ({src, x, y, w, rot = 0, op = 1, blur = 0, bright = 1, z = 8, origen = "50% 50%", flip = false, clip}) => (
  <Img src={staticFile(`${PLATES}/${src}`)} style={{
    position: "absolute", left: x, top: y, width: w, height: w * 9 / 16, mixBlendMode: "screen", opacity: op, zIndex: z,
    transform: `rotate(${rot}deg) scaleX(${flip ? -1 : 1})`, transformOrigin: origen, clipPath: clip, // clip-path en la misma capa no rompe el blend
    filter: `${blur ? `blur(${blur}px) ` : ""}${bright !== 1 ? `brightness(${bright}) contrast(1.15)` : ""}` || undefined,
  }} />
);

// 01 · CLICHÉ — belleza mediterránea casi exageradamente clásica. Quieto. Sin marca.
export const V2_01: React.FC = () => { useSpot(); return <Fondo color="#2a1d10"><Placa src={CAL2.cliche} /></Fondo>; };

// 02 · LA GOTA — macro imposible: la gota escultórica desciende, el tiempo casi se detiene. Sin copy todavía.
export const V2_02: React.FC = () => { useSpot(); return <Fondo color="#2a1d10"><Placa src={CAL2.gota} /></Fondo>; };

// 03 · PLOP — el instante del impacto. Silencio. «UNA GOTA.»
export const V2_03: React.FC = () => {
  useSpot();
  return (
    <Fondo color="#2a1d10">
      <Placa src={CAL2.plop} />
      <Vineta op={0.4} lado="abajo" />
      <Copy x={SAFE_X} y={720} size={180} lh={0.9}>UNA GOTA.</Copy>
    </Fondo>
  );
};

// 04 · BIG BANG — EL PLANO. La onda avanza y por donde pasa el mundo cambia. «CAMBIA TODO.»
export const V2_04: React.FC = () => {
  useSpot();
  return (
    <Fondo>
      <Placa src={CAL2.bigbang} />
      <Vineta op={0.3} lado="abajo" />
      <Copy x={SAFE_X} y={720} size={180} lh={0.9}>CAMBIA <Lima>TODO.</Lima></Copy>
    </Fondo>
  );
};

// 05 · PIZZA — el squeeze cruza en DIAGONAL, el aceite golpea y el queso reacciona.
//      Código de marca: la silueta fugaz de la boquilla OFICIAL (packshot ampliado), desenfocada, en primer plano.
export const V2_05: React.FC = () => {
  useSpot();
  const b = CAL2.boquilla05; const w = b.h * (746 / 791); const ch = CAL2.chorro05;
  return (
    <Fondo>
      <Placa src={CAL2.pizza} style={{transform: "scale(1.3)", transformOrigin: "0% 100%"}} />
      {/* el hilo cruza en DIAGONAL desde la punta de la boquilla hasta el queso (hilo vertical girado alrededor de su nacimiento) */}
      <Screen src={CAL2.chorroDiag} x={b.tipX - ch.w} y={b.tipY - 0.186 * ch.w * 9 / 16} w={ch.w} rot={ch.rot} origen={`${ch.w}px ${0.186 * ch.w * 9 / 16}px`} bright={1.3} z={8} />
      {/* código de marca: la silueta de la boquilla OFICIAL, desenfocada, a contraluz, cruzando la esquina */}
      <Img src={staticFile(`${PROD}/boquilla-750-macro.png`)} style={{
        position: "absolute", left: b.tipX - w / 2, top: b.tipY, width: w, height: b.h, zIndex: 9, opacity: b.op,
        transform: `rotate(${b.rot}deg)`, transformOrigin: "50% 0%", filter: `blur(${b.blur}px) brightness(0.8) saturate(0.85)`,
      }} />
    </Fondo>
  );
};

// 06 · SARTÉN — el aceite entra, WHOOF: flash de fuego. El naranja de la marca, en el fuego.
export const V2_06: React.FC = () => { useSpot(); return <Fondo><Placa src={CAL2.sarten} /></Fondo>; };

// 07 · PASTA — el tenedor gira, el hilo de aceite envuelve el giro y sale de cuadro. Verde ácido en la luz.
export const V2_07: React.FC = () => {
  useSpot();
  return (
    <Fondo>
      <Placa src={CAL2.pasta} />
      {/* el hilo de aceite nace en el giro del tenedor y sale del cuadro por arriba a la derecha → nos lleva al reveal */}
      <Screen src={CAL2.chorroDiag} x={760 - 0.479 * 2200} y={640 - 0.628 * 2200 * 9 / 16} w={2200} bright={1.3} z={8} />
      <Vineta op={0.3} lado="izq" />
    </Fondo>
  );
};

// 08a · REVEAL · LA BOQUILLA — pegados al hilo, la cámara retrocede; aparece la boquilla. Todavía no sabemos.
export const V2_08a: React.FC = () => {
  useSpot();
  const b = CAL2.boquilla08; const w = b.h * (746 / 791);
  return (
    <Fondo>
      <Placa src={CAL2.revealVacio} op={0.25} style={{filter: "blur(26px)"}} />
      {/* el hilo sube desde el borde inferior hasta la punta de la boquilla */}
      <Screen src={CAL2.hilo} x={b.cx - 0.497 * 2600} y={b.tipY - 8} w={2600} bright={1.5} z={7} />
      <Img src={staticFile(`${PROD}/boquilla-750-macro.png`)} style={{
        position: "absolute", left: b.cx - w / 2, top: b.tipY, width: w, height: b.h, zIndex: 10,
        transform: `rotate(${b.rot}deg)`, transformOrigin: "50% 0%",   // gira alrededor de la PUNTA (arriba del PNG)
        filter: "drop-shadow(0 0 40px rgba(0,0,0,0.9))",
      }} />
      <Vineta op={0.5} lado="centro" />
    </Fondo>
  );
};

// 08b · REVEAL · CLICK · SANTA GOTA — la botella entra completa. Es la respuesta a la pregunta.
export const V2_08b: React.FC = () => {
  useSpot();
  const b = CAL2.botella08; const w = b.h / RATIO.s750;
  return (
    <Fondo>
      <Placa src={CAL2.revealVacio} op={0.25} style={{filter: "blur(26px)"}} />
      <Screen src={CAL2.hilo} x={b.tipX - 0.497 * 2600} y={b.tipY - 8} w={2600} bright={1.5} z={7} />
      <Img src={staticFile(`${PROD}/hero-750.png`)} style={{
        position: "absolute", left: b.tipX - w / 2, top: b.tipY, width: w, height: b.h, zIndex: 10,
        transform: `rotate(${b.rot}deg)`, transformOrigin: "50% 0%",
        filter: "drop-shadow(0 24px 60px rgba(0,0,0,0.7))",
      }} />
    </Fondo>
  );
};

// 09 · HERO — negro absoluto, superficie húmeda, halo naranja detrás de la naranja, halo verde detrás de la
//      verde, aceite dorado desenfocado en primer plano. Botellas enormes. «SOMOS LA REVOLUCIÓN».
const Halo: React.FC<{cx: number; cy: number; w: number; h: number; color: string; op?: number; z?: number}> = ({cx, cy, w, h, color, op = 0.55, z = 9}) => (
  <div style={{position: "absolute", left: cx - w / 2, top: cy - h / 2, width: w, height: h, zIndex: z, opacity: op, pointerEvents: "none",
    background: `radial-gradient(ellipse at 50% 50%, ${color} 0%, ${color}66 28%, transparent 68%)`, filter: "blur(18px)"}} />
);

const Hero: React.FC<{segundo?: boolean}> = ({segundo = false}) => {
  useSpot();
  const piso = CAL2.pisoY;
  return (
    <Fondo>
      <Placa src={CAL2.heroSet} />
      {/* halos de luz DETRÁS de cada botella: naranja tras la naranja, verde tras la verde (luz, no producto) */}
      <Halo cx={560} cy={piso - 380} w={760} h={900} color={C.naranja} />
      <Halo cx={1010} cy={piso - 330} w={700} h={820} color={C.lima} op={0.45} />
      <Producto src="hero-750.png" ratio={RATIO.s750} cx={560} pisoY={piso} h={900} z={12} reflejo={0.26} />
      <Producto src="hero-500.png" ratio={RATIO.s500} cx={1010} pisoY={piso + 4} h={790} z={11} reflejo={0.26} />
      {/* aceite dorado cruzando el primer plano, muy desenfocado */}
      <Screen src={CAL2.heroFg} x={-500} y={640} w={2500} op={0.5} blur={30} z={15} rot={-6} />
      <Copy x={SAFE_X} y={segundo ? 380 : 470} size={112} align="right" lh={0.94}>
        SOMOS LA<br /><Lima>REVOLUCIÓN</Lima>{segundo ? <><br />DEL ACEITE<br />DE OLIVA.</> : null}
      </Copy>
    </Fondo>
  );
};
export const V2_09: React.FC = () => <Hero />;
export const V2_10: React.FC = () => <Hero segundo />;

// 11 · FIRMA — logo oficial + familia chica; una gota cae delante de cámara: PLOP = el punto de Santa Gota. Negro.
export const V2_11: React.FC<{latas?: boolean}> = ({latas = false}) => {
  useSpot();
  const piso = 900;
  return (
    <Fondo>
      <Placa src={CAL2.heroSet} op={0.5} />
      {latas && <Producto src="hero-lata-cocinar.png" ratio={RATIO.lCoc} cx={330} pisoY={piso - 4} h={300} z={9} reflejo={0.15} />}
      {latas && <Producto src="hero-lata-aderezar.png" ratio={RATIO.lAde} cx={830} pisoY={piso - 4} h={300} z={9} reflejo={0.15} />}
      <Producto src="hero-750.png" ratio={RATIO.s750} cx={470} pisoY={piso} h={520} z={12} reflejo={0.18} />
      <Producto src="hero-500.png" ratio={RATIO.s500} cx={690} pisoY={piso + 4} h={455} z={11} reflejo={0.18} />
      <LogoOficial x={1080} y={Math.max(HUINCHA_Y + 60, 300)} w={600} />
      <div style={{position: "absolute", left: 1080, top: 700, zIndex: 20, fontFamily: SG.fonts.display, fontWeight: 800, fontSize: 46, letterSpacing: "0.04em", color: C.lima, textShadow: "0 2px 16px rgba(0,0,0,0.6)"}}>{SG.url}</div>
      {/* la gota, grande, delante de todo: a punto de caer — el PLOP cierra */}
      <Screen src={CAL2.gotaFirma} x={1180} y={330} w={1000} z={30} />
    </Fondo>
  );
};
export const V2_11Latas: React.FC = () => <V2_11 latas />;
