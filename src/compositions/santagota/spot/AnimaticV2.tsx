/**
 * SANTA GOTA · «UNA GOTA. CAMBIA TODO.» — ANIMATIC V2 (feedback consolidado, 15-09-2026 noche).
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
import {Copy, Fondo, H, HUINCHA_Y, Lima, PLATES, PROD, Placa, RATIO, SAFE_X, Vineta, W, useSpot} from "./comun";
import {CAL2} from "./KeyframesV2";
import {CAL3} from "./KeyframesV3";
import {santagota as SG} from "../../../brand/santagota";

const CLIPS = "assets/santagota/spot/clips";
const FPS = 29.97;

export const T2 = {cliche: 0, gota: 60, plop: 96, cambia: 118, pizza: 150, sarten: 195, pasta: 249, reveal: 306, hero: 375,
  claim1: 449, claim2: 480, gotaFin: 509, plopFin: 528, fin: 599};
export const SQUEEZE_FIN = 340;   // último apriete en el reveal
export const GOTA_SUELTA = 354;   // la gota se desprende de la boquilla

/** Placas en movimiento (clips sin producto). `from` en segundos del clip. */
export const CAL_B: Record<string, {clip: string; from: number; placa: string; style?: React.CSSProperties}> = {
  cliche:   {clip: "cliche.mp4",   from: 0.2, placa: CAL2.cliche},
  gota:     {clip: "gota4.mp4",    from: 0.8, placa: "v4_gota_v1.png"},
  plop:     {clip: "plop4.mp4",    from: 0.0, placa: "v4_plop_v3.png"},   // la columna chica y el primer anillo; la corona grande queda fuera
  universo: {clip: "universo4.mp4", from: 0.3, placa: "v4_universo_v2.png", style: {transform: "scale(1.2)", transformOrigin: "50% 100%", filter: "brightness(0.85)"}},  // recorta la columna de luz de arriba: menos fuego
  pizza:    {clip: "pizza4.mp4",   from: 0.0, placa: "v4_pizza_v1.png", style: {transform: "scale(1.25)", transformOrigin: "0% 100%"}},   // 0–1,5 s: el hilo fino; después el modelo empoza el queso
  sarten:   {clip: "sarten.mp4",   from: 3.0, placa: CAL3.sarten},   // el flare ya va muriendo: dura unos cuadros y se apaga
  pasta:    {clip: "pasta.mp4",    from: 0.2, placa: CAL3.pasta, style: {transform: "scale(1.16)", transformOrigin: "0% 100%"}},  // antes del splash grande
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

// ── 01–04 · NORMALIDAD → GOTA → PLOP → CAMBIA TODO ──────────────────────────
const Apertura: React.FC = () => {
  const f = useCurrentFrame();
  // la onda del cambio: desde el punto de impacto, el universo nuevo se abre en círculo (14 cuadros, ease-out)
  const r = interpolate(f, [T2.cambia, T2.cambia + 14], [0, 2300], {easing: Easing.out(Easing.cubic), extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const borde = interpolate(f, [T2.cambia, T2.cambia + 3, T2.cambia + 14], [0, 0.9, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <Fondo color="#000">
      <Sequence from={T2.cliche} durationInFrames={T2.gota - T2.cliche}><Fondo color="#2a1d10"><Movimiento id="cliche" /></Fondo></Sequence>
      <Sequence from={T2.gota} durationInFrames={T2.plop - T2.gota}><Fondo color="#2a1d10"><Movimiento id="gota" /></Fondo></Sequence>
      {/* el plop sigue debajo mientras el universo nuevo se abre encima desde el impacto */}
      <Sequence from={T2.plop} durationInFrames={T2.pizza - T2.plop}><Fondo color="#2a1d10"><Movimiento id="plop" /><Vineta op={0.35} lado="abajo" /></Fondo></Sequence>
      <Sequence from={T2.cambia} durationInFrames={T2.pizza - T2.cambia}>
        <Fondo color="transparent">
          <div style={{position: "absolute", inset: 0, clipPath: `circle(${r}px at ${IMPACTO.x}px ${IMPACTO.y}px)`}}>
            <Movimiento id="universo" /><Vineta op={0.3} lado="abajo" />
          </div>
          {/* el borde de la onda: una línea de luz dorada que viaja con el círculo */}
          <div style={{position: "absolute", left: IMPACTO.x - r, top: IMPACTO.y - r, width: 2 * r, height: 2 * r, borderRadius: "50%", opacity: borde,
            boxShadow: "0 0 30px 14px rgba(255,190,90,0.55), inset 0 0 40px 12px rgba(255,160,60,0.35)", mixBlendMode: "screen", zIndex: 6}} />
        </Fondo>
      </Sequence>
      {f >= T2.plop && f < T2.pizza && (
        <Copy x={SAFE_X} y={600} size={180} lh={0.9}>
          <Beat desde={T2.plop}>UNA GOTA.</Beat>
          <Beat desde={T2.cambia}>CAMBIA <Lima>TODO.</Lima></Beat>
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
const BOT = {tipX: 470, tipY: 600, h: 1480, rot: -100};   // la botella cruza el cuadro entero: la mano queda fuera
const Reveal: React.FC = () => {
  const f = useCurrentFrame();            // 0..69
  const fS = SQUEEZE_FIN - T2.reveal, fG = GOTA_SUELTA - T2.reveal;
  const w = BOT.h / RATIO.s750;
  // cámara 1: de macro del hilo a plano (44 cuadros, curva óptica)
  const k = interpolate(f, [0, 44], [0, 1], {easing: Easing.bezier(0.33, 0, 0.2, 1), extrapolateRight: "clamp"});
  const z = interpolate(k, [0, 1], [2.2, 1]);
  const px = interpolate(k, [0, 1], [BOT.tipX + 6, W / 2]);
  const py0 = interpolate(k, [0, 1], [BOT.tipY + 300, H / 2]);
  // la gota: se desprende en fG y cae con gravedad; la cámara 2 la acompaña (tilt hacia abajo)
  const t = Math.max(0, f - fG);
  const caida = 3.6 * t * t;
  const py = py0 + caida * 0.9;
  const tx = W / 2 - z * px, ty = H / 2 - z * py;
  // vida: la botella respira (rotación rígida mínima, como sostenida por una mano fuera de cuadro)
  const vida = interpolate(f, [0, 30, 60], [-0.5, 0.2, -0.1], {extrapolateRight: "clamp"});
  const apriete = interpolate(f, [fS - 6, fS, fS + 10], [0, 0.8, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  // el hilo: FINO (sx 0,5), fluye, y después del último squeeze se adelgaza hasta cortarse
  const flujo = (f * 3.2) % 42;
  const grosor = interpolate(f, [fS, fS + 12], [0.5, 0.12], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const hiloOp = interpolate(f, [fS + 4, fG], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const gotaOp = interpolate(f, [fG - 4, fG], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const negro = interpolate(f, [fG + 10, fG + 19], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const hiloW = 1800; const hx = BOT.tipX - 0.516 * hiloW;
  const gW = 420;   // la gota (≈ 63 px), en screen, con la punta pegada a la boquilla
  return (
    <Fondo>
      <div style={{position: "absolute", inset: 0, transform: `translate(${tx}px, ${ty}px) scale(${z})`, transformOrigin: "0 0"}}>
        <div style={{position: "absolute", inset: 0, transform: `rotate(${vida + apriete}deg)`, transformOrigin: `${W}px ${BOT.tipY}px`}}>
          <Img src={staticFile(`${PROD}/hero4-750.png`)} style={{position: "absolute", left: BOT.tipX - w / 2, top: BOT.tipY, width: w, height: BOT.h, zIndex: 10,
            transform: `rotate(${BOT.rot}deg)`, transformOrigin: "50% 0%", filter: "drop-shadow(0 24px 60px rgba(0,0,0,0.7))"}} />
          <Screen src={CAL3.hilo} x={hx} y={BOT.tipY - 6 + flujo} w={hiloW} bright={1.1} z={7} sx={grosor} op={hiloOp} origen={`${0.516 * hiloW}px 0px`} clip={`inset(${flujo}px 0 10% 0)`} />
        </div>
        {/* la gota que se desprende (fuera del grupo que respira: ya no pertenece a la botella) */}
        <Screen src={CAL2.gotaFirma} x={BOT.tipX - gW * 0.5} y={BOT.tipY - gW * 9 / 16 * 0.145 + caida} w={gW} op={gotaOp} bright={1.3} z={12} clip="inset(0 0 52% 0)" />
      </div>
      <Vineta op={interpolate(f, [0, 40], [0.5, 0.2], {extrapolateRight: "clamp"})} lado="centro" />
      <AbsoluteFill style={{backgroundColor: "#000", opacity: negro, zIndex: 40}} />
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

const Hero: React.FC = () => {
  const f = useCurrentFrame();              // 0..224 (375→599)
  const piso = CAL3.pisoY;
  const fC1 = T2.claim1 - T2.hero, fC2 = T2.claim2 - T2.hero, fG = T2.gotaFin - T2.hero, fP = T2.plopFin - T2.hero;
  // cámara: micro travelling lateral + micro push-in, continuos, lineales (nada perceptible cuadro a cuadro)
  const push = interpolate(f, [0, 224], [1.0, 1.04]);
  const trav = interpolate(f, [0, 224], [18, -22]);
  // foco: 1) delante · 2) durante el 2º beat pasa a la de atrás · 3) la gota se lleva el foco · 4) vuelve delante
  const focoAtras = interpolate(f, [fC2 - 10, fC2 + 10, fG - 6, fG + 6, fP, fP + 12], [1.4, 0.3, 0.3, 1.6, 1.6, 1.2], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const focoDelante = interpolate(f, [fC2 - 10, fC2 + 10, fG - 6, fG + 6, fP, fP + 12], [0, 0.9, 0.9, 1.4, 1.4, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  // recorridos de luz: uno al llegar al hero, otro al final sobre la familia
  const barrido1 = interpolate(f, [12, 60], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const barrido2 = interpolate(f, [fP + 40, fP + 66], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const b1 = f < 62 ? barrido1 : -1, b2 = f >= fP + 40 ? barrido2 : -1;
  // la gota final: cae en primer plano (derecha, entre el producto y el claim), el foco la acompaña
  const tg = Math.max(0, f - fG);
  const gY = interpolate(tg, [0, fP - fG], [-260, piso - 40], {easing: Easing.in(Easing.quad), extrapolateRight: "clamp"});
  const gBlur = interpolate(tg, [0, (fP - fG) * 0.6, fP - fG], [7, 1, 0], {extrapolateRight: "clamp"});
  const gOp = f >= fG && f < fP + 2 ? 1 : 0;
  const GX = 1330;
  // la onda: anillo elíptico en el piso desde el impacto + la luz que recorre el set y descubre la familia
  const to = Math.max(0, f - fP);
  const R = interpolate(to, [0, 34], [0, 1500], {easing: Easing.out(Easing.cubic), extrapolateRight: "clamp"});
  const anilloOp = interpolate(to, [0, 3, 34], [0, 0.5, 0], {extrapolateRight: "clamp"});
  const luzOp = interpolate(to, [0, 6, 40, 70], [0, 0.22, 0.12, 0.09], {extrapolateRight: "clamp"});
  const descubre = (dist: number) => interpolate(R - dist, [-60, 180], [0.02, 0.85], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const dCoc = Math.hypot(GX - 360, piso - 40 - (piso - 300)), dAde = Math.hypot(GX - 1150, piso - 40 - (piso - 300));
  const logoOp = interpolate(f, [fP + 16, fP + 22], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <Fondo>
      <div style={{position: "absolute", inset: 0, transform: `translateX(${trav}px) scale(${push})`, transformOrigin: "700px 760px"}}>
        <Placa src={CAL3.heroNegro} style={{filter: `brightness(${0.5 + luzOp * 0.6}) contrast(1.1)`}} />
        {/* la familia ya está en el set, a oscuras: la luz de la onda la descubre (nada entra, nada aparece) */}
        <Botella src="hero4-lata-cocinar.png" ratio={RATIO.lCoc} cx={360} pisoY={piso - 70} h={520} z={7} blur={2.2} dim={descubre(dCoc)} refl={0.14} barrido={b2} />
        <Botella src="hero4-lata-aderezar.png" ratio={RATIO.lAde} cx={1150} pisoY={piso - 64} h={505} z={7} blur={2.2} dim={descubre(dAde)} refl={0.14} barrido={b2} />
        <Botella src="hero4-500.png" ratio={RATIO.s500} cx={900} pisoY={piso - 58} h={720} z={10} blur={focoAtras} dim={0.82 + luzOp * 0.3} barrido={b1 >= 0 ? Math.min(1, b1 * 1.2) : b2} />
        <Botella src="hero4-750.png" ratio={RATIO.s750} cx={610} pisoY={piso} h={930} z={12} blur={focoDelante} dim={1 + luzOp * 0.15} barrido={b1 >= 0 ? b1 : b2} />
        {/* la onda en el piso: elipse en perspectiva, luz dorada, se apaga sola */}
        <div style={{position: "absolute", left: GX - R, top: piso - 40 - R * 0.22, width: 2 * R, height: 2 * R * 0.22, borderRadius: "50%", zIndex: 9, opacity: anilloOp, mixBlendMode: "screen",
          boxShadow: "0 0 12px 3px rgba(255,215,140,0.7), inset 0 0 14px 3px rgba(255,190,100,0.35)"}} />
        {/* la luz que recorre el set desde el impacto */}
        <div style={{position: "absolute", left: GX - R * 1.3, top: piso - 40 - R * 0.9, width: R * 2.6, height: R * 1.8, borderRadius: "50%", zIndex: 8, opacity: luzOp, mixBlendMode: "screen",
          background: "radial-gradient(ellipse at 50% 50%, rgba(255,240,215,0.9) 0%, rgba(255,225,190,0.3) 35%, transparent 70%)"}} />
        <Screen src={CAL3.heroFg} x={-1500} y={860} w={2800} rot={-26} op={0.18} blur={46} z={15} />
      </div>
      {/* la gota final, en primer plano, fuera del grupo de cámara (está delante de todo) */}
      <Screen src={CAL2.gotaFirma} x={GX - 190 * 0.5} y={gY} w={190} op={gOp} blur={gBlur} bright={1.05} z={30} clip="inset(0 0 52% 0)" />
      {/* logo + claim: fijos, editoriales; el logo llega con la luz de la onda */}
      <Img src={staticFile(SG.logo)} style={{position: "absolute", right: SAFE_X + 40, top: Math.max(HUINCHA_Y + 70, 300), width: 360, height: 360 / SG.logoRatio, zIndex: 20, opacity: logoOp,
        filter: "drop-shadow(0 8px 28px rgba(0,0,0,0.55))"}} />
      <Copy x={SAFE_X + 40} y={560} size={64} weight={800} align="right" lh={1.06} style={{letterSpacing: "0.02em", textShadow: "none"}}>
        <Beat desde={fC1}>SOMOS LA<br /><Lima>REVOLUCIÓN</Lima></Beat>
        <Beat desde={fC2}><span style={{fontWeight: 300, letterSpacing: "0.06em"}}>DEL ACEITE DE OLIVA.</span></Beat>
      </Copy>
    </Fondo>
  );
};

export const AnimaticV2: React.FC = () => {
  useSpot();
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      <Sequence from={0} durationInFrames={T2.pizza}><Apertura /></Sequence>
      <Sequence from={T2.pizza} durationInFrames={T2.sarten - T2.pizza}><Pizza /></Sequence>
      <Sequence from={T2.sarten} durationInFrames={T2.pasta - T2.sarten}><Sarten /></Sequence>
      <Sequence from={T2.pasta} durationInFrames={T2.reveal - T2.pasta}><Pasta /></Sequence>
      <Sequence from={T2.reveal} durationInFrames={T2.hero - T2.reveal}><Reveal /></Sequence>
      <Sequence from={T2.hero} durationInFrames={T2.fin - T2.hero}><Hero /></Sequence>
    </AbsoluteFill>
  );
};
