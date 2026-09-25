/**
 * SANTA GOTA · «UNA GOTA. CAMBIA TODO.» — ANIMATIC V4 (feedback de voz de Valeria, 15-09-2026 noche).
 *
 * V4 sobre la V3:
 *   04  «CAMBIA TODO» ya no es lava: es el MISMO plato bajo la luz nueva (negro, luz dura dorada, anillo en el aceite).
 *   08  REVEAL con gente: una persona le echa Santa Gota a una ensalada en una mesa con amigos (golden hour). La escena
 *       la generó Nano Banana con el packshot de referencia y la animó Kling; el packshot OFICIAL se pega cuadro a cuadro
 *       (santagota-spot-mano-video.py --lifestyle). Después, inserto macro: la última gota sale de la boquilla → la
 *       cámara la sigue → aterriza en el hero → PLOP → onda.
 *   12  Placement final más grande: latas más presentes, la luz las descubre igual.
 *   Tono común: velo cálido en soft-light sobre toda la parte de comida para que la pieza conecte de punta a punta.
 *
 * (Cabecera de la V3:)
 *
 * V3 sobre la V2 (regla final: no agregar efectos; menos aceite, cero deformación, movimiento por cámara/luz/foco/
 * montaje/sonido):
 *   00–03  gota real → desprendimiento → impacto (placa de gota LIBRE, sin hilo).
 *   06     sartén con comida real (ajo, tomate, camarón) + aceite + reacción + flare breve.
 *   07     pasta: sólo un hilo fino acompañando el giro; ninguna gota flotando.
 *   08     reveal SIN mano y SIN botella entera: macro boquilla → retroceso PARCIAL hasta reconocer el packaging →
 *          última gota sale de la boquilla → la cámara la sigue → PLOP → la onda/luz revela el hero vertical.
 *   09–10  claim con jerarquía: REVOLUCIÓN protagonista (112 px), «SOMOS LA» chico, «DEL ACEITE DE OLIVA.» Light.
 *   11–12  family shot: nadie se mueve; la onda de luz descubre botellas + latas + logo; último highlight; HOLD.
 *
 * (Cabecera original de la V2:)
 *
 * La ruta y el storytelling están aprobados. La V2 refina la ejecución:
 *   MENOS ACEITE, MÁS IMPACTO — hilos finos, translúcidos, físicos. El WOW sale de cámara + montaje + luz + audio.
 *   03/04  «UNA GOTA.» · microbeat · «CAMBIA TODO.»: en CAMBIA TODO ocurre el cambio: onda → luz → color → espacio.
 *   08     REVEAL sin mano visible: la botella (packshot oficial, RÍGIDO) cruza el cuadro sostenida fuera de él;
 *          hilo → boquilla → último squeeze → una gota se desprende → la cámara la acompaña → negro → PLOP → HERO.
 *          (La mano generada se descartó: «si no es 100 % creíble, mejor sin mano». En el rodaje va mano real +
 *          proxy + tracking; el packaging nunca lo anima un modelo.)
 *   09–12  HERO en un solo set continuo: micro travelling + push-in + recorrido de luz + cambio de foco;
 *          claim en dos beats; una gota cae en primer plano → PLOP → onda → la luz recorre el set y DESCUBRE la
 *          familia completa (latas ya están ahí, a oscuras) → logo + claim → HOLD.
 *   Packaging: sólo packshots oficiales, escala uniforme, nunca deformados. Si una transición lo exigiera,
 *   se cambia la transición.
 *
 * Montaje (cuadros @ 29,97):
 *   01 CLICHÉ 0–60 · 02 GOTA 60–96 · 03 PLOP 96–118 «UNA GOTA.» · 04 CAMBIA TODO 118–150 · 05 PIZZA 150–195 ·
 *   06 SARTÉN 195–249 · 07 PASTA 249–306 · 08 REVEAL 306–375 (último squeeze 340, gota se suelta 354, PLOP 375) ·
 *   09 HERO 375–449 · 10 CLAIM 449 / 480 · 11 GOTA FINAL 509–528 PLOP · 12 ONDA + FAMILIA 528–599 HOLD.
 */
import React from "react";
import {AbsoluteFill, Easing, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from "remotion";
import {C, Copy, Fondo, H, Lima, PLATES, PROD, Placa, RATIO, SAFE_X, Vineta, W, useSpot} from "./comun";
import {CAL2} from "./KeyframesV2";
import {CAL3} from "./KeyframesV3";
import {santagota as SG} from "../../../brand/santagota";

const CLIPS = "assets/santagota/spot/clips";
const FPS = 29.97;

export const T3 = {cliche: 0, gota: 60, plop: 96, cambia: 118, pizza: 150, sarten: 195, pasta: 249, amigos: 306, reveal: 351, hero: 375,
  claim1: 449, claim2: 480, gotaFin: 509, plopFin: 528, fin: 599};
export const SQUEEZE_FIN = 340;   // último apriete en el reveal
export const GOTA_SUELTA = 354;   // la gota se desprende de la boquilla

/** Placas en movimiento (clips sin producto). `from` en segundos del clip. */
export const CAL_B: Record<string, {clip: string; from: number; placa: string; style?: React.CSSProperties}> = {
  cliche:   {clip: "cliche.mp4",   from: 0.2, placa: CAL2.cliche, style: {transform: "scale(1.15)", transformOrigin: "50% 100%"}},   // recorta el hilo del borde superior
  gota:     {clip: "gota5.mp4",    from: 0.6, placa: "v4_gota_libre_v1.png"},   // gota LIBRE: sin hilo, cae sola
  plop:     {clip: "plop4.mp4",    from: 0.0, placa: "v4_plop_v3.png"},   // la columna chica y el primer anillo; la corona grande queda fuera
  universo: {clip: "universo_comida.mp4", from: 0.3, placa: "v4_universo_comida_v1.png"},   // el mismo plato bajo la luz nueva: comida, no lava
  pizza:    {clip: "pizza4.mp4",   from: 0.0, placa: "v4_pizza_v1.png", style: {transform: "scale(1.25)", transformOrigin: "0% 100%"}},   // 0–1,5 s: el hilo fino; después el modelo empoza el queso
  sarten:   {clip: "sarten5.mp4",  from: 2.4, placa: "v4_sarten_food_v1.png"},   // comida real; el flare dura ~15 cuadros y muere solo
  pasta:    {clip: "pasta5.mp4",   from: 0.3, placa: CAL3.pasta, style: {transform: "scale(1.16)", transformOrigin: "0% 100%"}},  // sólo el hilo, ninguna gota en el aire
};
export const IMPACTO = {x: 1018, y: 626};  // punto del impacto en v4_plop_v3 (la columna de la gota)

const Movimiento: React.FC<{id: keyof typeof CAL_B; style?: React.CSSProperties}> = ({id, style}) => {
  const c = CAL_B[id];
  return <OffthreadVideo src={staticFile(`${CLIPS}/${c.clip}`)} startFrom={Math.round(c.from * FPS)} muted
    style={{position: "absolute", inset: 0, width: W, height: H, objectFit: "cover", ...c.style, ...style}} />;
};

const Screen: React.FC<{src: string; x: number; y: number; w: number; rot?: number; op?: number; blur?: number; bright?: number; z?: number; clip?: string; origen?: string; sx?: number; sy?: number}> = ({src, x, y, w, rot = 0, op = 1, blur = 0, bright = 1, z = 8, clip, origen = "50% 50%", sx = 1, sy = 1}) => (
  <Img src={staticFile(`${PLATES}/${src}`)} style={{
    position: "absolute", left: x, top: y, width: w, height: w * 9 / 16, mixBlendMode: "screen", opacity: op, zIndex: z,
    transform: `rotate(${rot}deg) scale(${sx}, ${sy})`, transformOrigin: origen, clipPath: clip,
    filter: `${blur ? `blur(${blur}px) ` : ""}${bright !== 1 ? `brightness(${bright}) contrast(1.15)` : ""}` || undefined,
  }} />
);

const Beat: React.FC<{desde: number; children: React.ReactNode}> = ({desde, children}) => {
  const f = useCurrentFrame();
  return <div style={{opacity: interpolate(f, [desde, desde + 3], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"})}}>{children}</div>;
};


/** 02 · LA GOTA — gota real ya desprendida, sin hilo: la placa fija (bokeh) + la gota recortada cayendo con gravedad. Ni Kling ni Mystic
 *  fueron capaces de dar una gota sin hilo (tres intentos): se corta la gota de la placa y se rellena el hueco con el propio bokeh. */
const GotaLibre: React.FC = () => {
  const f = useCurrentFrame();            // 0..36
  const k = 1920 / 2752;                  // la placa se ajusta al cuadro
  const box = {x: 1230 * k, y: 320 * k, w: 310 * k, h: 500 * k};
  const caida = interpolate(f, [0, 36], [0, 181], {easing: Easing.in(Easing.quad), extrapolateRight: "clamp"});   // llega al borde de la burrata en el corte
  const push = interpolate(f, [0, 36], [1.0, 1.05]);
  return (
    <Fondo color="#2a1d10">
      <div style={{position: "absolute", inset: 0, transform: `scale(${push})`, transformOrigin: "52% 55%"}}>
        <Placa src="v5_gota_libre_fondo.png" />
        <Img src={staticFile(`${PLATES}/v5_gota_libre_gota.png`)} style={{position: "absolute", left: box.x, top: box.y + caida, width: box.w, height: box.h, zIndex: 5}} />
      </div>
    </Fondo>
  );
};

// ── 01–04 · NORMALIDAD → GOTA → PLOP → CAMBIA TODO ──────────────────────────
const Apertura: React.FC = () => {
  const f = useCurrentFrame();
  // la onda del cambio: desde el punto de impacto, el universo nuevo se abre en círculo (14 cuadros, ease-out)
  const r = interpolate(f, [T3.cambia, T3.cambia + 14], [0, 2300], {easing: Easing.out(Easing.cubic), extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const borde = interpolate(f, [T3.cambia, T3.cambia + 3, T3.cambia + 14], [0, 0.9, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <Fondo color="#000">
      <Sequence from={T3.cliche} durationInFrames={T3.gota - T3.cliche}><Fondo color="#2a1d10"><Movimiento id="cliche" /></Fondo></Sequence>
      <Sequence from={T3.gota} durationInFrames={T3.plop - T3.gota}><GotaLibre /></Sequence>
      {/* el plop sigue debajo mientras el universo nuevo se abre encima desde el impacto */}
      <Sequence from={T3.plop} durationInFrames={T3.pizza - T3.plop}><Fondo color="#2a1d10"><Movimiento id="plop" /><Vineta op={0.35} lado="abajo" /></Fondo></Sequence>
      <Sequence from={T3.cambia} durationInFrames={T3.pizza - T3.cambia}>
        <Fondo color="transparent">
          <div style={{position: "absolute", inset: 0, clipPath: `circle(${r}px at ${IMPACTO.x}px ${IMPACTO.y}px)`}}>
            <Movimiento id="universo" /><Vineta op={0.3} lado="abajo" />
          </div>
          {/* el borde de la onda: una línea de luz dorada que viaja con el círculo */}
          <div style={{position: "absolute", left: IMPACTO.x - r, top: IMPACTO.y - r, width: 2 * r, height: 2 * r, borderRadius: "50%", opacity: borde,
            boxShadow: "0 0 30px 14px rgba(255,190,90,0.55), inset 0 0 40px 12px rgba(255,160,60,0.35)", mixBlendMode: "screen", zIndex: 6}} />
        </Fondo>
      </Sequence>
      {f >= T3.plop && f < T3.pizza && (
        <Copy x={SAFE_X} y={600} size={180} lh={0.9}>
          <Beat desde={T3.plop}>UNA GOTA.</Beat>
          <Beat desde={T3.cambia}>CAMBIA <Lima>TODO.</Lima></Beat>
        </Copy>
      )}
    </Fondo>
  );
};

// ── 05–07 · CAOS GASTRONÓMICO CONTROLADO (menos aceite) ─────────────────────
const Pizza: React.FC = () => {
  const f = useCurrentFrame();
  const b = {tipX: 1035, tipY: 200, h: 900, rot: -168, blur: 7, op: 0.75}; const w = b.h * (746 / 791);   // el hilo del clip cae en x ≈ 0,43 → 1032 con la escala 1,25
  const drift = interpolate(f, [0, 45], [0, -14]);
  return (
    <Fondo>
      <Movimiento id="pizza" />
      {/* código de marca: la silueta de la boquilla OFICIAL, desenfocada, insinuada. Todavía no es el reveal. */}
      <Img src={staticFile(`${PROD}/boquilla-750-macro.png`)} style={{position: "absolute", left: b.tipX - w / 2 + drift, top: b.tipY, width: w, height: b.h, zIndex: 9, opacity: b.op,
        transform: `rotate(${b.rot}deg)`, transformOrigin: "50% 0%", filter: `blur(${b.blur}px) brightness(0.75) saturate(0.8)`}} />
    </Fondo>
  );
};
const Sarten: React.FC = () => <Fondo><Movimiento id="sarten" /></Fondo>;
const Pasta: React.FC = () => <Fondo><Movimiento id="pasta" /><Vineta op={0.25} lado="izq" /></Fondo>;

// ── 08 · REVEAL — sin mano visible. Hilo → boquilla → botella (rígida, sostenida fuera de cuadro) → último squeeze
//         → la gota se desprende → la cámara la acompaña → negro → PLOP (corte al hero)
const AMIGOS = "assets/santagota/spot/amigos";         // secuencia PNG (Kling + packshot oficial cuadro a cuadro), si la hay
const AMIGOS_STILL = "assets/santagota/spot/amigos_still/0001.png";   // la foto compuesta (packshot oficial pegado con puntos manuales)
const AMIGOS_MODO = "still" as "still" | "seq";
const AMIGOS_TIP = {x: 1105, y: 525};                   // punta de la boquilla oficial en la foto (medida)
const Amigos: React.FC = () => {
  const f = useCurrentFrame();            // 0..45
  const idx = Math.min(120, Math.max(1, 1 + Math.round((f / 29.97) * 24)));
  const push = interpolate(f, [0, 45], [1.0, 1.04]);
  const trav = interpolate(f, [0, 45], [0, -10]);
  const flujo = (f * 3.4) % 42;
  const hiloW = 900; const hx = AMIGOS_TIP.x - 0.516 * hiloW;
  return (
    <Fondo>
      <div style={{position: "absolute", inset: 0, transform: `translateX(${trav}px) scale(${push})`, transformOrigin: "58% 45%"}}>
        {AMIGOS_MODO === "seq"
          ? <Img src={staticFile(`${AMIGOS}/${String(idx).padStart(4, "0")}.png`)} style={{position: "absolute", inset: 0, width: W, height: H}} />
          : <Img src={staticFile(AMIGOS_STILL)} style={{position: "absolute", inset: 0, width: W, height: H}} />}
        {/* el hilo VIVE: fluye desde la boquilla oficial hasta la ensalada (fino, en screen sobre el hilo dibujado) */}
        {AMIGOS_MODO === "still" && (
          <Screen src={CAL3.hilo} x={hx} y={AMIGOS_TIP.y - 4 + flujo} w={hiloW} bright={0.9} op={0.7} z={7} sx={0.45} origen={`${0.516 * hiloW}px 0px`} clip={`inset(${flujo}px 0 38% 0)`} />
        )}
      </div>
      <Vineta op={0.22} lado="abajo" />
    </Fondo>
  );
};

const BOT = {tipX: 470, tipY: 600, h: 1480, rot: -100};   // macro: boquilla + hombro; la botella nunca se ve entera
const Reveal: React.FC = () => {
  const f = useCurrentFrame();            // 0..24 — inserto: la última gota
  const fS = 2, fG = 7;
  const w = BOT.h / RATIO.s750;
  const z = 1.35; const px = BOT.tipX + 330;
  const t = Math.max(0, f - fG);
  const caida = 3.6 * t * t;
  const py = BOT.tipY - 40 + caida * 0.9;
  const tx = W / 2 - z * px, ty = H / 2 - z * py;
  const vida = interpolate(f, [0, 24], [-0.3, 0.1]);
  const apriete = interpolate(f, [fS - 2, fS, fS + 8], [0, 0.8, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const flujo = (f * 3.2) % 42;
  const grosor = interpolate(f, [fS, fS + 6], [0.45, 0.12], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const hiloOp = interpolate(f, [fS + 2, fG], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const gotaOp = interpolate(f, [fG - 3, fG], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const hiloW = 1800; const hx = BOT.tipX - 0.516 * hiloW; const gW = 420;
  return (
    <Fondo>
      <div style={{position: "absolute", inset: 0, transform: `translate(${tx}px, ${ty}px) scale(${z})`, transformOrigin: "0 0"}}>
        <div style={{position: "absolute", inset: 0, transform: `rotate(${vida + apriete}deg)`, transformOrigin: `${W}px ${BOT.tipY}px`}}>
          <Img src={staticFile(`${PROD}/hero4-750.png`)} style={{position: "absolute", left: BOT.tipX - w / 2, top: BOT.tipY, width: w, height: BOT.h, zIndex: 10,
            transform: `rotate(${BOT.rot}deg)`, transformOrigin: "50% 0%", filter: "drop-shadow(0 24px 60px rgba(0,0,0,0.7))"}} />
          <Screen src={CAL3.hilo} x={hx} y={BOT.tipY - 6 + flujo} w={hiloW} bright={1.1} z={7} sx={grosor} op={hiloOp} origen={`${0.516 * hiloW}px 0px`} clip={`inset(${flujo}px 0 10% 0)`} />
        </div>
        <Screen src={CAL2.gotaFirma} x={BOT.tipX - gW * 0.5} y={BOT.tipY - gW * 9 / 16 * 0.145 + caida} w={gW} op={gotaOp} bright={1.3} z={12} clip="inset(0 0 52% 0)" />
      </div>
      <Vineta op={0.3} lado="centro" />
    </Fondo>
  );
};

// ── 09–12 · HERO → CLAIM → GOTA FINAL → ONDA → FAMILIA (un solo set, la cámara vive, el producto no se mueve)
const Botella: React.FC<{src: string; ratio: number; cx: number; pisoY: number; h: number; z: number; blur?: number; dim?: number; barrido?: number; refl?: number}> = ({src, ratio, cx, pisoY, h, z, blur = 0, dim = 1, barrido = -1, refl = 0.22}) => {
  const w = h / ratio; const x = cx - w / 2; const img = staticFile(`${PROD}/${src}`);
  const filtro = `${blur ? `blur(${blur}px) ` : ""}brightness(${dim})`;
  const mask = {WebkitMaskImage: `url(${img})`, maskImage: `url(${img})`, WebkitMaskSize: "100% 100%", maskSize: "100% 100%"} as React.CSSProperties;
  return (
    <>
      <div style={{position: "absolute", left: cx - w * 0.9, top: pisoY - 14, width: w * 1.8, height: 70, zIndex: z - 3, opacity: 0.55 * dim,
        background: "radial-gradient(ellipse at 50% 40%, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 65%)", filter: "blur(6px)"}} />
      <div style={{position: "absolute", left: cx - w * 0.55, top: pisoY - 7, width: w * 1.1, height: 16, zIndex: z - 2, opacity: 0.95 * dim,
        background: "radial-gradient(ellipse at 50% 50%, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 70%)"}} />
      <Img src={img} style={{position: "absolute", left: x, top: pisoY, width: w, height: h, zIndex: z - 1, opacity: refl * dim,
        transform: "scaleY(-1)", transformOrigin: "50% 0%", filter: `blur(2.2px) ${filtro}`,
        WebkitMaskImage: "linear-gradient(180deg, rgba(0,0,0,1) 0%, rgba(0,0,0,0.35) 22%, rgba(0,0,0,0) 62%)",
        maskImage: "linear-gradient(180deg, rgba(0,0,0,1) 0%, rgba(0,0,0,0.35) 22%, rgba(0,0,0,0) 62%)"}} />
      <Img src={img} style={{position: "absolute", left: x, top: pisoY - h, width: w, height: h, zIndex: z, filter: filtro}} />
      {/* recorrido de luz sobre el packaging: una banda suave que cruza, recortada con la silueta del propio packshot */}
      {barrido >= 0 && barrido <= 1 && (
        <div style={{position: "absolute", left: x, top: pisoY - h, width: w, height: h, zIndex: z + 1, mixBlendMode: "screen", opacity: 0.55, ...mask,
          background: `linear-gradient(100deg, transparent ${barrido * 160 - 60}%, rgba(255,240,205,0.9) ${barrido * 160 - 30}%, transparent ${barrido * 160}%)`}} />
      )}
    </>
  );
};

export const PLOP_HERO = 6;   // cuadros después del corte: la gota del reveal toca el piso del set
const Hero: React.FC = () => {
  const f = useCurrentFrame();              // 0..224 (375→599)
  const piso = CAL3.pisoY;
  const fC1 = T3.claim1 - T3.hero, fC2 = T3.claim2 - T3.hero, fG = T3.gotaFin - T3.hero, fP = T3.plopFin - T3.hero;
  // cámara: travelling lateral + push-in continuos que se frenan suavemente hasta el HOLD final
  const push = interpolate(f, [0, fP + 30], [1.0, 1.04], {easing: Easing.out(Easing.quad), extrapolateRight: "clamp"});
  const trav = interpolate(f, [0, fP + 30], [18, -20], {easing: Easing.out(Easing.quad), extrapolateRight: "clamp"});
  // foco: delante · 2º beat pasa atrás · la gota final se lo lleva · vuelve delante tras el PLOP
  const focoAtras = interpolate(f, [fC2 - 10, fC2 + 10, fG - 6, fG + 6, fP, fP + 12], [1.4, 0.3, 0.3, 1.6, 1.6, 1.2], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const focoDelante = interpolate(f, [fC2 - 10, fC2 + 10, fG - 6, fG + 6, fP, fP + 12], [0, 0.9, 0.9, 1.4, 1.4, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const barrido1 = interpolate(f, [PLOP_HERO + 14, PLOP_HERO + 60], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const barrido2 = interpolate(f, [fP + 40, fP + 66], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const b1 = f >= PLOP_HERO + 14 && f < PLOP_HERO + 62 ? barrido1 : -1, b2 = f >= fP + 40 ? barrido2 : -1;
  // ONDA 1 (llegada): la gota del reveal cae en (514, piso−40), PLOP, la luz descubre las botellas
  const G1 = {x: 514, y: piso - 40};
  const g1Y = interpolate(f, [0, PLOP_HERO], [700, G1.y - 118], {extrapolateRight: "clamp"});
  const g1Op = f < PLOP_HERO + 1 ? 1 : 0;
  const t1 = Math.max(0, f - PLOP_HERO);
  const R1 = interpolate(t1, [0, 30], [0, 1300], {easing: Easing.out(Easing.cubic), extrapolateRight: "clamp"});
  const anillo1 = interpolate(t1, [0, 3, 30], [0, 0.45, 0], {extrapolateRight: "clamp"});
  const luz1 = interpolate(t1, [0, 6, 40, 80], [0, 0.2, 0.1, 0.06], {extrapolateRight: "clamp"});
  const rev1 = (dist: number) => interpolate(R1 - dist, [-40, 220], [0.02, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const d750 = Math.hypot(G1.x - 570, G1.y - (piso - 450)), d500 = Math.hypot(G1.x - 845, G1.y - (piso - 400));
  // GOTA FINAL (cierre): cae en primer plano a la derecha, el foco la acompaña
  const tg = Math.max(0, f - fG);
  const gY = interpolate(tg, [0, fP - fG], [-260, piso - 40], {easing: Easing.in(Easing.quad), extrapolateRight: "clamp"});
  const gBlur = interpolate(tg, [0, (fP - fG) * 0.6, fP - fG], [7, 1, 0], {extrapolateRight: "clamp"});
  const gOp = f >= fG && f < fP + 2 ? 1 : 0;
  const GX = 1330;
  // ONDA 2 (cierre): la luz recorre el set y descubre la familia completa; nadie se mueve
  const to = Math.max(0, f - fP);
  const R = interpolate(to, [0, 34], [0, 1500], {easing: Easing.out(Easing.cubic), extrapolateRight: "clamp"});
  const anilloOp = interpolate(to, [0, 3, 34], [0, 0.5, 0], {extrapolateRight: "clamp"});
  const luzOp = interpolate(to, [0, 6, 40, 70], [0, 0.22, 0.12, 0.09], {extrapolateRight: "clamp"});
  const descubre = (dist: number) => interpolate(R - dist, [-60, 180], [0.02, 0.96], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const dCoc = Math.hypot(GX - 315, piso - 40 - (piso - 300)), dAde = Math.hypot(GX - 1000, piso - 40 - (piso - 300));
  const logoOp = interpolate(f, [fP + 16, fP + 22], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const luz = luz1 + luzOp;
  return (
    <Fondo>
      <div style={{position: "absolute", inset: 0, transform: `translateX(${trav}px) scale(${push})`, transformOrigin: "660px 760px"}}>
        <Placa src={CAL3.heroNegro} style={{filter: `brightness(${0.35 + luz * 0.8}) contrast(1.1)`}} />
        {/* la familia ya está en el set, a oscuras: la onda final la descubre (nada entra, nada se mueve) */}
        <Botella src="hero4-lata-cocinar.png" ratio={RATIO.lCoc} cx={315} pisoY={piso - 62} h={610} z={7} blur={1.6} dim={descubre(dCoc)} refl={0.16} barrido={b2} />
        <Botella src="hero4-lata-aderezar.png" ratio={RATIO.lAde} cx={1000} pisoY={piso - 58} h={595} z={7} blur={1.6} dim={descubre(dAde)} refl={0.16} barrido={b2} />
        {/* las botellas: a oscuras hasta que la onda 1 las descubre */}
        <Botella src="hero4-500.png" ratio={RATIO.s500} cx={845} pisoY={piso - 58} h={720} z={10} blur={focoAtras} dim={rev1(d500) * (0.82 + luzOp * 0.3)} barrido={b1 >= 0 ? Math.min(1, b1 * 1.2) : b2} />
        <Botella src="hero4-750.png" ratio={RATIO.s750} cx={570} pisoY={piso} h={930} z={12} blur={focoDelante} dim={rev1(d750) * (1 + luzOp * 0.15)} barrido={b1 >= 0 ? b1 : b2} />
        {/* onda 1: anillo + luz desde el pie de la botella naranja */}
        <div style={{position: "absolute", left: G1.x - R1, top: G1.y - R1 * 0.22, width: 2 * R1, height: 2 * R1 * 0.22, borderRadius: "50%", zIndex: 9, opacity: anillo1, mixBlendMode: "screen",
          boxShadow: "0 0 12px 3px rgba(255,215,140,0.7), inset 0 0 14px 3px rgba(255,190,100,0.35)"}} />
        <div style={{position: "absolute", left: G1.x - R1 * 1.3, top: G1.y - R1 * 0.9, width: R1 * 2.6, height: R1 * 1.8, borderRadius: "50%", zIndex: 8, opacity: luz1, mixBlendMode: "screen",
          background: "radial-gradient(ellipse at 50% 50%, rgba(255,240,215,0.9) 0%, rgba(255,225,190,0.3) 35%, transparent 70%)"}} />
        {/* onda 2: la del cierre */}
        <div style={{position: "absolute", left: GX - R, top: piso - 40 - R * 0.22, width: 2 * R, height: 2 * R * 0.22, borderRadius: "50%", zIndex: 9, opacity: anilloOp, mixBlendMode: "screen",
          boxShadow: "0 0 12px 3px rgba(255,215,140,0.7), inset 0 0 14px 3px rgba(255,190,100,0.35)"}} />
        <div style={{position: "absolute", left: GX - R * 1.3, top: piso - 40 - R * 0.9, width: R * 2.6, height: R * 1.8, borderRadius: "50%", zIndex: 8, opacity: luzOp, mixBlendMode: "screen",
          background: "radial-gradient(ellipse at 50% 50%, rgba(255,240,215,0.9) 0%, rgba(255,225,190,0.3) 35%, transparent 70%)"}} />
        <Screen src={CAL3.heroFg} x={-1500} y={860} w={2800} rot={-26} op={0.18 * Math.min(1, luz * 4)} blur={46} z={15} />
      </div>
      {/* la gota que viene del reveal: aterriza al pie de la botella (delante de todo) */}
      <Screen src={CAL2.gotaFirma} x={G1.x - 420 * 0.5} y={g1Y} w={420} op={g1Op} bright={1.3} z={30} clip="inset(0 0 52% 0)" />
      {/* la gota final del cierre */}
      <Screen src={CAL2.gotaFirma} x={GX - 190 * 0.5} y={gY} w={190} op={gOp} blur={gBlur} bright={1.05} z={30} clip="inset(0 0 52% 0)" />
      {/* logo: llega con la luz de la onda final */}
      <Img src={staticFile(SG.logo)} style={{position: "absolute", right: SAFE_X, top: 330, width: 320, height: 320 / SG.logoRatio, zIndex: 20, opacity: logoOp,
        filter: "drop-shadow(0 8px 28px rgba(0,0,0,0.55))"}} />
      {/* claim: jerarquía editorial — REVOLUCIÓN manda; dos beats; nada vuela */}
      <div style={{position: "absolute", right: SAFE_X, top: 548, zIndex: 20, textAlign: "right", fontFamily: SG.fonts.display, textTransform: "uppercase", color: "#FFFFFF", whiteSpace: "nowrap"}}>
        <Beat desde={fC1}>
          <div style={{fontSize: 44, fontWeight: 700, letterSpacing: "0.2em", lineHeight: 1}}>SOMOS LA</div>
          <div style={{fontSize: 100, fontWeight: 900, letterSpacing: "-0.02em", lineHeight: 0.95, color: C.lima, marginTop: 4}}>REVOLUCIÓN</div>
        </Beat>
        <Beat desde={fC2}>
          <div style={{fontSize: 46, fontWeight: 300, letterSpacing: "0.08em", lineHeight: 1.1, marginTop: 14}}>DEL ACEITE DE OLIVA.</div>
        </Beat>
      </div>
    </Fondo>
  );
};

export const AnimaticV4: React.FC = () => {
  useSpot();
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      <Sequence from={0} durationInFrames={T3.pizza}><Apertura /></Sequence>
      <Sequence from={T3.pizza} durationInFrames={T3.sarten - T3.pizza}><Pizza /></Sequence>
      <Sequence from={T3.sarten} durationInFrames={T3.pasta - T3.sarten}><Sarten /></Sequence>
      <Sequence from={T3.pasta} durationInFrames={T3.amigos - T3.pasta}><Pasta /></Sequence>
      <Sequence from={T3.amigos} durationInFrames={T3.reveal - T3.amigos}><Amigos /></Sequence>
      {/* tono común de la parte de comida: velo cálido en soft-light + viñeta suave (no toca el estudio negro) */}
      <Sequence from={0} durationInFrames={T3.reveal}>
        <AbsoluteFill style={{background: "radial-gradient(ellipse at 50% 45%, rgba(255,186,90,0.16) 0%, rgba(255,150,60,0.10) 55%, rgba(60,20,0,0.22) 100%)", mixBlendMode: "soft-light", pointerEvents: "none", zIndex: 35}} />
      </Sequence>
      <Sequence from={T3.reveal} durationInFrames={T3.hero - T3.reveal}><Reveal /></Sequence>
      <Sequence from={T3.hero} durationInFrames={T3.fin - T3.hero}><Hero /></Sequence>
    </AbsoluteFill>
  );
};
