/**
 * SANTA GOTA · «UNA GOTA. CAMBIA TODO.» — ANIMATIC (15-09-2026, noche).
 *
 * V3 aprobada → storyboard cerrado. Este es el montaje real: duración exacta de cada plano, cortes, copy en
 * tiempo, y el audio se mezcla aparte (scripts/santagota-animatic-mezcla.py) sobre el render.
 *
 * 1920×1080 · 29,97 · 599 cuadros = 19,987 s. Sin huincha: el copy y el logo viven bajo y=216 por si el canal
 * monta la del auspiciador.
 *
 * Reglas que se cumplen por construcción:
 *  - El packaging sólo entra como packshot oficial 2D (nunca pasa por un modelo de video). Las placas en
 *    movimiento son cocina/gota/fuego/pasta: sin producto.
 *  - Sin zoom digital gratuito, sin wipes, sin glitch, sin texto volando: cortes secos, un solo movimiento de
 *    cámara continuo en el reveal y un micro push-in óptico en el hero.
 *
 * Montaje (cuadros @ 29,97):
 *   01 CLICHÉ        0–60      07 PASTA           249–306
 *   02 LA GOTA      60–96      08 REVEAL (1 plano) 306–381   hilo → boquilla → mano → botella · CLICK ≈ 352
 *   03 PLOP         96–114     09 HERO            381–465   «SOMOS LA / REVOLUCIÓN»
 *   04 BIG BANG    114–150     10 HERO            465–546   + «DEL ACEITE DE OLIVA.»
 *   05 PIZZA       150–195     11 FIRMA           546–599   logo · gota cae · PLOP · negro
 *   06 SARTÉN      195–249
 */
import React from "react";
import {AbsoluteFill, Easing, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame} from "remotion";
import {C, Copy, Fondo, H, HUINCHA_Y, Lima, PLATES, PROD, Placa, RATIO, SAFE_X, Vineta, W, useSpot} from "./comun";
import {CAL2} from "./KeyframesV2";
import {CAL3} from "./KeyframesV3";
import {santagota as SG} from "../../../brand/santagota";

const CLIPS = "assets/santagota/spot/clips";

// ── El montaje ─────────────────────────────────────────────────────────────
export const T = {cliche: 0, gota: 60, plop: 96, bigbang: 114, pizza: 150, sarten: 195, pasta: 249, reveal: 306, hero: 381, hero2: 465, firma: 546, fin: 599};
export const CLICK = 352;          // el instante del apriete en el reveal
export const PLOP_FINAL = 584;     // la gota de la firma toca (el clip se suelta a ~3,95 s; entra en 3,1 s)

/** Placa en movimiento (clip generado, sin producto). `from` = segundo del clip donde empieza el plano. */
export const CAL_A: Record<string, {clip: string | null; from: number; rate?: number; placa: string; style?: React.CSSProperties}> = {
  cliche:  {clip: "cliche.mp4",  from: 0.2, placa: CAL2.cliche},    // la gotita baja lentísima y no pasa nada más
  gota:    {clip: "gota.mp4",    from: 1.2, placa: CAL2.gota},      // descenso escultórico
  plop:    {clip: "plop.mp4",    from: 2.45, placa: CAL2.plop},     // la corona del impacto se forma en 2,5–3,2 s
  bigbang: {clip: "bigbang.mp4", from: 0.5, placa: CAL2.bigbang},   // el anillo y el fuego viven; la cámara no se mueve
  pizza:   {clip: "pizza.mp4",   from: 0.6, placa: CAL2.pizza, style: {transform: "scale(1.3)", transformOrigin: "0% 100%"}},
  sarten:  {clip: "sarten.mp4",  from: 2.4, placa: CAL3.sarten},   // el flare está alto en 2,4 s y muere solo hacia 4,2 s
  pasta:   {clip: "pasta.mp4",   from: 0.5, placa: CAL3.pasta, style: {transform: "scale(1.16)", transformOrigin: "0% 100%"}},
};

const Movimiento: React.FC<{id: keyof typeof CAL_A}> = ({id}) => {
  const c = CAL_A[id];
  const base: React.CSSProperties = {position: "absolute", inset: 0, width: W, height: H, objectFit: "cover", ...c.style};
  if (!c.clip) return <Placa src={c.placa} style={c.style} />;
  return <OffthreadVideo src={staticFile(`${CLIPS}/${c.clip}`)} startFrom={Math.round(c.from * 29.97)} playbackRate={c.rate ?? 1} muted style={base} />;
};

/** Capa sobre negro en «screen» (brillo y clip EN la misma capa). */
const Screen: React.FC<{src: string; x: number; y: number; w: number; rot?: number; op?: number; blur?: number; bright?: number; z?: number; clip?: string; origen?: string; sx?: number}> = ({src, x, y, w, rot = 0, op = 1, blur = 0, bright = 1, z = 8, clip, origen = "50% 50%", sx = 1}) => (
  <Img src={staticFile(`${PLATES}/${src}`)} style={{
    position: "absolute", left: x, top: y, width: w, height: w * 9 / 16, mixBlendMode: "screen", opacity: op, zIndex: z,
    transform: `rotate(${rot}deg) scaleX(${sx})`, transformOrigin: origen, clipPath: clip,
    filter: `${blur ? `blur(${blur}px) ` : ""}${bright !== 1 ? `brightness(${bright}) contrast(1.15)` : ""}` || undefined,
  }} />
);

/** Entrada editorial del copy: aparece en 3 cuadros, sin volar. */
const Beat: React.FC<{desde: number; children: React.ReactNode}> = ({desde, children}) => {
  const f = useCurrentFrame();
  const op = interpolate(f, [desde, desde + 3], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return <div style={{opacity: op}}>{children}</div>;
};

// ── 01–04 · NORMALIDAD → GOTA → PLOP → BIG BANG ────────────────────────────
const Apertura: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <Fondo color="#000">
      <Sequence from={T.cliche} durationInFrames={T.gota - T.cliche}><Fondo color="#2a1d10"><Movimiento id="cliche" /></Fondo></Sequence>
      <Sequence from={T.gota} durationInFrames={T.plop - T.gota}><Fondo color="#2a1d10"><Movimiento id="gota" /></Fondo></Sequence>
      <Sequence from={T.plop} durationInFrames={T.bigbang - T.plop}><Fondo color="#2a1d10"><Movimiento id="plop" /><Vineta op={0.4} lado="abajo" /></Fondo></Sequence>
      <Sequence from={T.bigbang} durationInFrames={T.pizza - T.bigbang}><Fondo><Movimiento id="bigbang" /><Vineta op={0.3} lado="abajo" /></Fondo></Sequence>
      {/* el copy vive sobre los dos planos: «UNA GOTA.» cae con el PLOP, «CAMBIA TODO.» con el big bang */}
      {f >= T.plop && f < T.pizza && (
        <Copy x={SAFE_X} y={600} size={180} lh={0.9}>
          <Beat desde={T.plop}>UNA GOTA.</Beat>
          <Beat desde={T.bigbang + 4}>CAMBIA <Lima>TODO.</Lima></Beat>
        </Copy>
      )}
    </Fondo>
  );
};

// ── 05–07 · CAOS GASTRONÓMICO CONTROLADO ──────────────────────────────────
const Pizza: React.FC = () => {
  const f = useCurrentFrame();
  // el clip trae el hilo cayendo vertical (x ≈ 0,50 del clip → 1248 px con la escala 1,3): la silueta de la boquilla OFICIAL se cuelga de ahí
  const b = {tipX: 1250, tipY: 200, h: 900, rot: -168, blur: 6, op: 0.9}; const w = b.h * (746 / 791);
  const drift = interpolate(f, [0, 45], [0, -14]);   // la silueta apenas se desliza: está pasando, no posando
  return (
    <Fondo>
      <Movimiento id="pizza" />
      <Img src={staticFile(`${PROD}/boquilla-750-macro.png`)} style={{
        position: "absolute", left: b.tipX - w / 2 + drift, top: b.tipY, width: w, height: b.h, zIndex: 9, opacity: b.op,
        transform: `rotate(${b.rot}deg)`, transformOrigin: "50% 0%", filter: `blur(${b.blur}px) brightness(0.8) saturate(0.85)`,
      }} />
    </Fondo>
  );
};
const Sarten: React.FC = () => <Fondo><Movimiento id="sarten" /></Fondo>;
const Pasta: React.FC = () => <Fondo><Movimiento id="pasta" /><Vineta op={0.25} lado="izq" /></Fondo>;

// ── 08 · REVEAL — UN solo plano: pegados al hilo, la cámara retrocede; aparece la boquilla, la mano, la botella
const REVEAL_SEQ = "assets/santagota/spot/reveal";   // salida de scripts/santagota-spot-mano-video.py (24 fps, 121 cuadros)
const TIP0 = {x: 778, y: 523};                          // punta de la boquilla en el cuadro 1 (lo imprime el script)
const Reveal: React.FC = () => {
  const f = useCurrentFrame();            // 0..75
  const idx = Math.min(121, Math.max(1, 1 + Math.round((f / 29.97) * 24)));
  // cámara: de macro del hilo (z 2,4 centrada bajo la punta) a plano entero (z 1). Un solo movimiento, easing óptico.
  const k = interpolate(f, [0, 62], [0, 1], {easing: Easing.bezier(0.33, 0.0, 0.2, 1), extrapolateRight: "clamp"});
  const z = interpolate(k, [0, 1], [2.4, 1]);
  const px = interpolate(k, [0, 1], [TIP0.x + 4, W / 2]);
  const py = interpolate(k, [0, 1], [TIP0.y + 300, H / 2]);
  const tx = W / 2 - z * px, ty = H / 2 - z * py;
  // la mano ya se mueve sola (muñeca, dedos, hilo). Al CLICK se suma un cabeceo mínimo: el apriete.
  const apriete = interpolate(f, [CLICK - T.reveal, CLICK - T.reveal + 4, CLICK - T.reveal + 16], [0, 0.9, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <Fondo>
      <div style={{position: "absolute", inset: 0, transform: `translate(${tx}px, ${ty}px) scale(${z})`, transformOrigin: "0 0"}}>
        <div style={{position: "absolute", inset: 0, transform: `rotate(${apriete}deg)`, transformOrigin: `${W}px 600px`}}>
          <Img src={staticFile(`${REVEAL_SEQ}/${String(idx).padStart(4, "0")}.png`)} style={{position: "absolute", inset: 0, width: W, height: H}} />
        </div>
      </div>
      <Vineta op={interpolate(f, [0, 40], [0.5, 0.15], {extrapolateRight: "clamp"})} lado="centro" />
    </Fondo>
  );
};

// ── 09–10 · HERO — negro profundo, botellas asentadas (sombra + reflejo + contacto), rim mínimo, micro push-in
const Botella: React.FC<{src: string; ratio: number; cx: number; pisoY: number; h: number; z: number; blur?: number; dim?: number}> = ({src, ratio, cx, pisoY, h, z, blur = 0, dim = 1}) => {
  const w = h / ratio; const x = cx - w / 2; const img = staticFile(`${PROD}/${src}`);
  const filtro = `${blur ? `blur(${blur}px) ` : ""}brightness(${dim})`;
  return (
    <>
      {/* sombra de asiento: ancha y suave + el contacto apretado bajo el pie */}
      <div style={{position: "absolute", left: cx - w * 0.9, top: pisoY - 14, width: w * 1.8, height: 70, zIndex: z - 3, opacity: 0.55,
        background: "radial-gradient(ellipse at 50% 40%, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 65%)", filter: "blur(6px)"}} />
      <div style={{position: "absolute", left: cx - w * 0.55, top: pisoY - 7, width: w * 1.1, height: 16, zIndex: z - 2, opacity: 0.95,
        background: "radial-gradient(ellipse at 50% 50%, rgba(0,0,0,1) 0%, rgba(0,0,0,0) 70%)"}} />
      {/* reflejo en el piso húmedo: más largo que el de e-commerce, se apaga rápido */}
      <Img src={img} style={{position: "absolute", left: x, top: pisoY, width: w, height: h, zIndex: z - 1, opacity: 0.22,
        transform: "scaleY(-1)", transformOrigin: "50% 0%", filter: `blur(2.2px) ${filtro}`,
        WebkitMaskImage: "linear-gradient(180deg, rgba(0,0,0,1) 0%, rgba(0,0,0,0.35) 22%, rgba(0,0,0,0) 62%)",
        maskImage: "linear-gradient(180deg, rgba(0,0,0,1) 0%, rgba(0,0,0,0.35) 22%, rgba(0,0,0,0) 62%)"}} />
      <Img src={img} style={{position: "absolute", left: x, top: pisoY - h, width: w, height: h, zIndex: z, filter: filtro}} />
    </>
  );
};

const Hero: React.FC = () => {
  const f = useCurrentFrame();              // 0..165 (09 + 10)
  const piso = CAL3.pisoY;
  const push = interpolate(f, [0, 165], [1, 1.045]);   // micro push-in óptico, lineal, imperceptible cuadro a cuadro
  const l3 = T.hero2 - T.hero;
  return (
    <Fondo>
      <div style={{position: "absolute", inset: 0, transform: `scale(${push})`, transformOrigin: "640px 760px"}}>
        {/* el set, más hundido: negro casi absoluto, el horizonte húmedo apenas se adivina */}
        <Placa src={CAL3.heroNegro} style={{filter: "brightness(0.55) contrast(1.1)"}} />
        <Botella src="hero4-500.png" ratio={RATIO.s500} cx={900} pisoY={piso - 58} h={720} z={10} blur={1.4} dim={0.8} />
        <Botella src="hero4-750.png" ratio={RATIO.s750} cx={610} pisoY={piso} h={930} z={12} />
        <Screen src={CAL3.heroFg} x={-1500} y={860} w={2800} rot={-26} op={0.2} blur={46} z={15} />
      </div>
      <Copy x={SAFE_X + 40} y={560} size={64} weight={800} align="right" lh={1.06} style={{letterSpacing: "0.02em", textShadow: "none"}}>
        <Beat desde={18}>SOMOS LA<br /><Lima>REVOLUCIÓN</Lima></Beat>
        <Beat desde={l3}><span style={{fontWeight: 300, letterSpacing: "0.06em"}}>DEL ACEITE DE OLIVA.</span></Beat>
      </Copy>
    </Fondo>
  );
};

// ── 11 · FIRMA — logo, familia, la gota cae, PLOP, negro
const Firma: React.FC = () => {
  const f = useCurrentFrame();              // 0..53
  const piso = 900;
  const negro = interpolate(f, [PLOP_FINAL - T.firma + 4, PLOP_FINAL - T.firma + 10], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <Fondo>
      <Placa src={CAL3.heroNegro} style={{filter: "brightness(0.45)"}} />
      <Botella src="hero4-750.png" ratio={RATIO.s750} cx={470} pisoY={piso} h={520} z={12} />
      <Botella src="hero4-500.png" ratio={RATIO.s500} cx={690} pisoY={piso + 4} h={455} z={11} dim={0.9} />
      <Img src={staticFile(SG.logo)} style={{position: "absolute", left: 1080, top: Math.max(HUINCHA_Y + 60, 300), width: 600, height: 600 / SG.logoRatio, zIndex: 20,
        filter: "drop-shadow(0 8px 28px rgba(0,0,0,0.55))"}} />
      <div style={{position: "absolute", left: 1080, top: 700, zIndex: 20, fontFamily: SG.fonts.display, fontWeight: 800, fontSize: 46, letterSpacing: "0.04em", color: C.lima}}>{SG.url}</div>
      <OffthreadVideo src={staticFile(`${CLIPS}/gota_firma.mp4`)} startFrom={Math.round(3.1 * 29.97)} muted style={{
        position: "absolute", left: 1180, top: 330, width: 1000, height: 1000 * 9 / 16, mixBlendMode: "screen", zIndex: 30, filter: "contrast(1.15)"}} />
      <AbsoluteFill style={{backgroundColor: "#000", opacity: negro, zIndex: 40}} />
    </Fondo>
  );
};

export const Animatic: React.FC = () => {
  useSpot();
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      <Sequence from={0} durationInFrames={T.pizza}><Apertura /></Sequence>
      <Sequence from={T.pizza} durationInFrames={T.sarten - T.pizza}><Pizza /></Sequence>
      <Sequence from={T.sarten} durationInFrames={T.pasta - T.sarten}><Sarten /></Sequence>
      <Sequence from={T.pasta} durationInFrames={T.reveal - T.pasta}><Pasta /></Sequence>
      <Sequence from={T.reveal} durationInFrames={T.hero - T.reveal}><Reveal /></Sequence>
      <Sequence from={T.hero} durationInFrames={T.firma - T.hero}><Hero /></Sequence>
      <Sequence from={T.firma} durationInFrames={T.fin - T.firma}><Firma /></Sequence>
    </AbsoluteFill>
  );
};
