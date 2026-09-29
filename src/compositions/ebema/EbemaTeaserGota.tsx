// =============================================================================
// EBEMA · TEASER «LA GOTA DE COLOR» — reel 9:16 (29-09-2026)
// Brief: Carlos Figueroa (raw/ebema/teaser-gota-de-color/brief_carlos_teaser.docx).
// Centro de pinturas de Concepción y Temuco con Codelpa: generar expectativa SIN decir
// que son pinturas. Sin voz ni música: sólo diseño sonoro (scripts/ebema-teaser-gota-sfx.py).
//
// Decisiones de Paulina (29-09):
//  · Final = frame «opción C» (Seedream 5 Pro con el KV del cliente como referencia).
//  · Tipografía = la del key visual del cliente: DejaVu Sans (medida glifo a glifo).
//    Rojo = el de EBEMA #EC1C23 (el KV trae #DF221E; R-01, un solo rojo).
//  · Cierre = pantalla negra con el logo EBEMA en blanco apareciendo lento al centro
//    (NO el cierre oficial de reel: este teaser vive en el universo del KV).
//
// Imagen (ronda 1): caída COMPUESTA — la gota recortada de `fin_e` cae sola sobre `piso_e`
// (el mismo piso, vacío y a oscuras) y justo antes de tocar se abre la luz del KV
// (`fin_e_sin_gota`, máscara radial). Empalma sin corte con Kling 2.5 Pro desde `fin_e`
// (`color_e_30`, gota flotando). La caída de Kling (`c1_caida`) se descartó: hacía corona
// de chapoteo y gotas múltiples.
// Textos: los del KV, verbatim, en su jerarquía (MUY PRONTO · titular · filete ·
// SUCURSALES… · Próximamente). Nada de texto dentro de la IA.
// =============================================================================
import React from "react";
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame, Easing} from "remotion";

export const TEASER_FPS = 30;
const A = (f: string) => staticFile(`assets/ebema/teaser-gota/${f}`);
const RED = "#EC1C23", WHITE = "#FFFFFF", FILETE = "rgba(150,156,168,.85)";
const clamp = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;
const s = (x: number) => Math.round(x * TEASER_FPS);

let fontsOk = false;
const ensureFonts = () => {
  if (fontsOk || typeof document === "undefined") return;
  fontsOk = true;
  const css = [
    `@font-face{font-family:'DejaVuKV';font-weight:700;font-display:block;src:url(${A("fonts/DejaVuSans-Bold.ttf")}) format('truetype');}`,
    `@font-face{font-family:'DejaVuKV';font-weight:400;font-display:block;src:url(${A("fonts/DejaVuSans.ttf")}) format('truetype');}`,
  ].join("\n");
  const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  const fs = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (fs) { fs.load("700 70px DejaVuKV"); fs.load("400 70px DejaVuKV"); }
};
const DV = "'DejaVuKV', 'DejaVu Sans', Verdana, sans-serif";

// ---------------------------------------------------------------- tiempos
const T = {
  // RONDA 3 (Paulina, 29-09): «la caída es muy lenta y el video no se ve llamativo; puede ser
  // de ocho segundos» → 8 s.
  impacto: s(1.75),  // la gota se asienta sobre el piso en `caida_fluida_30` (medido cuadro a cuadro)
  color: 79,         // fin de `caida_fluida_30` (2,63 s) = primer cuadro de `color_g_30`: sin corte
  textos: s(3.0),
  negro: s(5.9),     // fundido a blanco
  logo: s(6.2),
  fin: s(8),
};
export const TEASER_DUR = T.fin;
// ⭐ RONDA 1 (Paulina, 29-09, comentarios en Drive):
//   1,7 s «la gota debe caer desde arriba, no debe verse un chorro de agua. La base suelo debe
//         ser plana como una pared o piso plano. La gota debe aparecer desde arriba y justo antes
//         de topar con el piso iluminarse con los colores del KV»
//   5,7 s «la gota no debe estar atada a algo arriba, debe aparecer sola como en el KV»
// → Nuevo final `fin_e` (gota suelta sobre piso plano). La caída compuesta con la gota recortada
//   de la ronda 1 se reemplazó en la ronda 2 por movimiento real de Kling (ver `Caida`).
// Geometría: `fin_e` es 1520×2736 → cover en 1080×1920 = escala 0,7105 y 12 px recortados
// arriba; contacto de la gota con el piso en y 1579.
const K = 1080 / 1520, OFF_Y = (2736 * K - 1920) / 2;
const ORIGEN = {x: 540, y: Math.round(1579 * K - OFF_Y)};

const Cubre: React.FC<{src: string; video?: boolean}> = ({src, video}) => video
  ? <OffthreadVideo src={A(src)} muted style={{width: "100%", height: "100%", objectFit: "cover"}} />
  : <Img src={A(src)} style={{width: "100%", height: "100%", objectFit: "cover"}} />;

/** RONDA 2 (Paulina, 29-09): «la transición de la gota que cae debe ser mucho más realista,
 *  como una gota de agua; se ve tosca y poco profesional». La gota recortada que se deslizaba
 *  se reemplaza por movimiento REAL: Kling 2.5 Pro anima, desde `fin_e`, la gota que sube y la
 *  luz que se apaga (`r1_sube`), y acá se reproduce AL REVÉS (`llegada_30`): una gota esférica
 *  que baja en cámara lenta y se alarga en lágrima al llegar, terminando exacto en `fin_e`.
 *  Antes va la ENTRADA desde el borde superior (`r3_sale`, 0–3,2 s, también al revés; desde
 *  3,5 s Kling pegaba la gota a una superficie de agua arriba y se descartó). Un solo plano
 *  continuo `caida_real_30`: entrada y primer tramo de la llegada a 2×, los últimos 2,5 s
 *  antes del piso a velocidad real (cámara lenta).
 *  El piso se mantiene a oscuras (velo) y se enciende recién cuando la gota llega.
 *  RONDA 3: el mismo movimiento a 3× (entrada y primer tramo) y 2× (llegada) = `caida_rapida_30`
 *  (3,1 s), y en el contacto funde a la gota de punta más larga (`fin_g2` / `color_g_30`):
 *  «necesito que la gota sea más alargada en la punta superior».
 *  RONDA 4: «al tocar el piso se corta, necesito que sea muy fluido: que la gota cuando va
 *  cayendo se transforme en la gota alargada». Un solo clip de Kling desde `fin_g2` (`m2_sube`):
 *  la punta se recoge de a poco hasta ser esfera mientras sube y la luz se apaga; al revés
 *  (`caida_fluida_30`, 2,5× arriba y 1,5× en la transformación) cae redonda y se alarga sin
 *  corte hasta el cuadro exacto de `color_g_30`. Se descartó `m1_sube` (hacía chorro). */
const Caida: React.FC = () => {
  const f = useCurrentFrame();
  const o = interpolate(f, [0, s(0.3)], [0, 1], clamp);
  const apagado = interpolate(f, [T.impacto - s(0.45), T.impacto + s(0.25)], [0.93, 0], {...clamp, easing: Easing.in(Easing.quad)});
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <AbsoluteFill style={{opacity: o}}><Cubre src="clips/caida_fluida_30.mp4" video /></AbsoluteFill>
      <AbsoluteFill style={{opacity: apagado, background: `linear-gradient(180deg, rgba(0,0,0,0) ${ORIGEN.y - 170}px, #000 ${ORIGEN.y + 30}px, #000 100%)`}} />
    </AbsoluteFill>
  );
};

/** Desde el contacto: Kling desde `fin_g2` (gota de punta larga flotando, luz que late). Entra
 *  fundiendo en 6 cuadros, tapado por el destello: el cambio de forma de la punta no se lee como corte. */
const Color: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{opacity: interpolate(f, [0, 1], [1, 1], clamp)}}>
      <Cubre src="clips/color_g_30.mp4" video />
    </AbsoluteFill>
  );
};

/** Destello blanco-dorado en el punto de contacto, corto. */
const Destello: React.FC = () => {
  const f = useCurrentFrame();
  const o = interpolate(f, [0, 4, 16], [0, 0.7, 0], clamp);
  const r = interpolate(f, [0, 16], [60, 650], clamp);
  return (
    <AbsoluteFill style={{opacity: o, background: `radial-gradient(circle at ${ORIGEN.x}px ${ORIGEN.y}px, rgba(255,246,220,1) 0px, rgba(255,214,140,.5) ${r * 0.35}px, rgba(0,0,0,0) ${r}px)`}} />
  );
};

const Linea: React.FC<{a: number; children: React.ReactNode; style: React.CSSProperties}> = ({a, children, style}) => {
  const f = useCurrentFrame();
  const p = interpolate(f, [a, a + 16], [0, 1], {...clamp, easing: Easing.out(Easing.cubic)});
  return <div style={{...style, opacity: p, transform: `translateY(${(1 - p) * 24}px)`}}>{children}</div>;
};

/** El bloque del KV, en su jerarquía y con sus textos tal cual (izquierda, abajo). */
const BloqueKV: React.FC = () => {
  const f = useCurrentFrame();
  const velo = interpolate(f, [0, 20], [0, 1], clamp);
  const filete = interpolate(f, [s(0.5), s(0.5) + 18], [0, 1], {...clamp, easing: Easing.out(Easing.cubic)});
  return (
    <AbsoluteFill>
      {/* velo en rampa suave sólo en la zona del texto (R-38) */}
      <AbsoluteFill style={{opacity: velo, background: "linear-gradient(180deg, rgba(0,0,0,0) 50%, rgba(0,0,0,.45) 60%, rgba(0,0,0,.8) 68%, rgba(0,0,0,.9) 100%)"}} />
      <div style={{position: "absolute", left: 84, top: 1300, fontFamily: DV}}>
        <Linea a={0} style={{color: RED, fontWeight: 700, fontSize: 32, letterSpacing: 1.2}}>MUY PRONTO</Linea>
        <div style={{height: 26}} />
        <Linea a={4} style={{color: WHITE, fontWeight: 700, fontSize: 70, lineHeight: 1.14}}>Algo nuevo<br />está tomando color.</Linea>
        <div style={{height: 34}} />
        <div style={{width: 780 * filete, height: 3, background: FILETE}} />
        <div style={{height: 30}} />
        {/* RONDA 1 (7,3 s): «dejemos en una línea la frase "sucursales concepción y temuco"
            y eliminemos el próximamente» */}
        <Linea a={s(0.7)} style={{color: RED, fontWeight: 700, fontSize: 30, letterSpacing: 1, whiteSpace: "nowrap"}}>SUCURSALES CONCEPCIÓN Y TEMUCO</Linea>
      </div>
    </AbsoluteFill>
  );
};

/** Cierre de Paulina: el logo EBEMA apareciendo lento al centro (ronda 4: sobre blanco, logo oficial). */
const CierreLogo: React.FC = () => {
  const f = useCurrentFrame();
  const o = interpolate(f, [0, s(1.2)], [0, 1], {...clamp, easing: Easing.inOut(Easing.cubic)});
  const z = interpolate(f, [0, T.fin - T.logo], [0.96, 1.0], clamp);
  const W = 380;
  return (
    // RONDA 4 (Paulina, 29-09): «dejémoslo en blanco con el logo de Ebema normal, el que tiene
    // rojo con gris, porque siento que se ve muy oscuro» → fondo blanco + logo oficial.
    <AbsoluteFill style={{background: "#FFFFFF", justifyContent: "center", alignItems: "center"}}>
      <Img src={A("logo_ebema_color.png")} style={{width: W, opacity: o, transform: `scale(${z})`}} />
    </AbsoluteFill>
  );
};

const Negro: React.FC<{dur: number}> = ({dur}) => {
  const f = useCurrentFrame();
  return <AbsoluteFill style={{background: "#FFFFFF", opacity: interpolate(f, [0, dur], [0, 1], clamp)}} />;
};

// ---------------------------------------------------------------- sonido (guion de Carlos)
const Sonido: React.FC = () => (
  <>
    {/* zumbido grave desde el arranque; se corta justo antes del contacto: un instante de silencio */}
    <Audio src={A("sfx/zumbido.mp3")} volume={(f) => interpolate(f, [0, 8, T.impacto - s(0.6), T.impacto - s(0.45)], [0, 0.9, 0.9, 0], clamp)} />
    {/* RONDA 3 (Paulina): la gota suena «como cuando una gota toca el agua» (agua_a: un golpe,
        tono de burbuja que sube 473→656 Hz) y el remate que iba con el logo pasa al momento en
        que se ilumina la gota. El logo entra SIN sonido. */}
    <Sequence from={T.impacto - 2}><Audio src={A("sfx/agua_a.mp3")} volume={1} /></Sequence>
    <Sequence from={T.impacto}><Audio src={A("sfx/remate.mp3")} volume={0.55} /></Sequence>
  </>
);

// ---------------------------------------------------------------- la pieza
export const EbemaTeaserGota: React.FC = () => {
  ensureFonts();
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <Sequence from={0} durationInFrames={T.color}><Caida /></Sequence>
      <Sequence from={T.color} durationInFrames={T.logo - T.color}><Color /></Sequence>
      <Sequence from={T.impacto - 2} durationInFrames={20}><Destello /></Sequence>
      <Sequence from={T.textos} durationInFrames={T.logo - T.textos}><BloqueKV /></Sequence>
      <Sequence from={T.negro} durationInFrames={T.logo - T.negro}><Negro dur={T.logo - T.negro} /></Sequence>
      <Sequence from={T.logo}><CierreLogo /></Sequence>
      <Sonido />
    </AbsoluteFill>
  );
};
