import React from "react";
import {AbsoluteFill, Easing, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";

// =============================================================================
// EBEMA · GRILLA · STORY ANIMADA de Ebema Click — 07/10/2026
// 1080×1920 · 30 fps · 558 frames = 18,6 s
//
// Brief (grilla de octubre, bloque 02 · INSTAGRAM / STORIES), verbatim:
//   STORY ANIMADA · Sticker de enlace
//   (Dejar espacio para el sticker desde el inicio, sin tapar la gráfica.)
//   T1: ¿Cuánto tiempo pierdes abasteciéndote?
//   T2: Con Ebema Click compras online, 24/7 y sin filas.
//   T3: Para ferreteros y contratistas de Santiago, Rancagua, Chillán, Concepción,
//       Temuco y Puerto Montt.
//   T4: Y cada mes sorteamos una gift card entre quienes compran.
//   T5: Toca el enlace.
//
// ⭐ LA REFERENCIA QUE MANDA: `storie_click.mp4` de la grilla de JULIO 2026 (Paulina,
// raw/ebema/1-referencias/grilla/video/stories/). Es el mismo guion, texto por texto,
// y dura 18,65 s. Todo lo de abajo está MEDIDO sobre sus fotogramas (2160×3840 → /2):
//   · (los arcos rojos de las esquinas de julio se QUITARON en la ronda 1, ver abajo)
//   · lockup Click blanco: tinta x 272,5–806,5 · y 369–479
//   · textos en Raleway REGULAR (no bold): 1 línea blanca + 1 línea en caja roja,
//     cuerpo ≈ 48, bloque entre y 1150 y 1420
//   · T3: las ciudades entran UNA POR UNA, cada una en su cajita roja
//   · cierre en BLANCO: bloques rojos redondeados en las esquinas con filete,
//     anillo EBEMA 404 × 415 en (344, 586), caja «Toca el enlace» 521 × 71 en y 1261
//
// Lo que NO se copia de julio: el cierre decía además «Entra a Ebema Click / y haz
// crecer tu negocio hoy mismo». Octubre no lo trae: sólo T5 «Toca el enlace».
//
// ⛔ RONDA 1 · 24-09-2026 — Paulina, comentarios en Drive sobre ebema_st-07.10.mp4:
//   0:01 «elimina los círculos que salen de las esquinas para todo el video» → sin arcos
//   0:05 T2 en 2 líneas: «Con Ebema Click compras online» / «24/7 y sin filas.»,
//        la segunda en caja roja y en bold
//   0:10 «el video se queda pegado y con glitches; debe ser muy fluido y realista».
//        Causa: los clips de Kling son de 24 fps y el s3 iba con playbackRate .95 →
//        OffthreadVideo repetía cuadros (≈ 5 fps efectivos). Ahora los 4 clips se
//        pasan ANTES a 30 fps con interpolación de movimiento (`*_30.mp4`, minterpolate
//        mci) y se reproducen a velocidad 1, cuadro a cuadro.
//   0:14 la gift card lleva el logo de Ebema Click (pegado en el fotograma clave y
//        re-animado con Kling: s4_logo; la plaquita que Kling inventa en el chaleco se borra con limpiar_s4.py → s4_limpio_30) · la caja «una gift card» del ANCHO de las otras
//        líneas, agrandando caja y texto juntos
//   0:17 «el cuadro de toca el enlace está muy alejado del logo, déjalo más arriba»
//
// ⛔ RONDA 2 · 24-09-2026 (tarde):
//   0:09 «la frase de ferreteros y contratistas déjémosla en bold, se pierde la letra
//        en el fondo» → T3 en Raleway 700
//   0:14 «el logo de ebema click está chueco» → la tarjeta está inclinada ~2° y Kling
//        redibujaba el logo: pegar_logo.py sigue la banda roja cuadro a cuadro y pega
//        el PNG oficial rotado con ella → s4_final_30
//   0:17 «los cuadros de las esquinas deben entrar pero no rebotar, lentamente, y que
//        no se vea una línea blanca en los bordes» → sin spring (ease-out de 28 cuadros)
//        y los bloques SANGRAN 40 px fuera del lienzo: el de abajo terminaba en 1919
//
// Espacio del sticker: se deja libre la franja y 1450–1600 en todas las escenas (T3
// sube su bloque para no entrar ahí). No se dibuja nada: Paulina pidió el 24-09
// «eliminemos esta caja indicadora de todas las stories».
// =============================================================================
const RED = "#EC1C23", WHITE = "#FFFFFF";
export const STORY_OCT_FPS = 30;

const DIR = "assets/ebema/grilla-oct26/story-animada";
// timeline (frames)
// ⛔ RONDA 3 · 24-09-2026 — lleva LOCUCIÓN y música: ver mezcla.py.
//   · 1er intento (voz «Andre» de ElevenLabs + audio de la story de julio) RECHAZADO:
//     «la música de fondo es en realidad el audio completo del video anterior con voz
//     incluida; la voz es malísima, como una persona de habla inglesa hablando
//     español». Ahora: voz es-CL-LorenzoNeural (la eligió Paulina) y la pista
//     ORIGINAL de julio, que pasa ella.
// Las escenas se miden a la voz (no se acelera la voz): arranque (8) + lo que mide su
// mp3 + ~0,5 s de aire. ⚠️ Si cambia una línea, cambian estos números Y LINEAS en mezcla.py.
const ESC = [
  {clip: "s1_30.mp4", from: 0, dur: 108},             // T1 · voz 1,90 s
  {clip: "s2_30.mp4", from: 108, dur: 128},           // T2 · voz 3,38 s · clip 151
  {clip: "s3_lento135_30.mp4", from: 236, dur: 188},  // T3 · voz 5,50 s · clip ×1,35 = 201
  // s4: la frente quedaba bajo el lockup. Se amplía 1,22 desde ARRIBA.
  {clip: "s4_final_30.mp4", from: 424, dur: 110, escala: 1.22},   // T4 · voz 2,78 s · clip 149
];
const CIERRE = {from: 534, dur: 90};         // T5 · voz en el cuadro 22 del cierre
export const STORY_OCT_DURATION = CIERRE.from + CIERRE.dur;   // 624 = 20,8 s

let fontsOk = false;
const ensureFonts = () => {
  if (fontsOk || typeof document === "undefined") return;
  fontsOk = true;
  const f = (w: number, file: string) =>
    `@font-face { font-family:'RalewayEB'; font-weight:${w}; font-display:block; src:url(${staticFile(`assets/ebema/fonts/${file}`)}) format('truetype'); }`;
  const css = [f(400, "Raleway-Regular.ttf"), f(600, "Raleway-SemiBold.ttf"), f(700, "Raleway-Bold.ttf"),
    `@font-face { font-family:'HelvEB'; font-weight:700; font-display:block; src:url(${staticFile("assets/ebema/fonts/Helvetica-Bold.ttf")}) format('truetype'); }`].join("\n");
  const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  const fs = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (fs) ["400", "600", "700"].forEach((w) => fs.load(`${w} 40px RalewayEB`));
};
const RALEWAY = "'RalewayEB', 'Raleway', Arial, sans-serif";
const HELV = "'HelvEB', Helvetica, Arial, sans-serif";

// toda cifra en Helvetica Bold (§3 del manual)
const Num: React.FC<{t: string}> = ({t}) => (
  <>{t.split(/(\d[\d:/]*)/).map((p, i) => (/\d/.test(p) ? <span key={i} style={{fontFamily: HELV}}>{p}</span> : p))}</>
);

const useSpring = (delay: number) => {
  const frame = useCurrentFrame(); const {fps} = useVideoConfig();
  return spring({fps, frame: frame - delay, config: {damping: 16, stiffness: 150}});
};

// salida común de cada bloque de texto: 8 frames antes de cortar
const useSalida = (dur: number) => {
  const frame = useCurrentFrame();
  return interpolate(frame, [dur - 10, dur - 2], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
};

const Linea: React.FC<{delay: number; children: React.ReactNode; size?: number; caps?: boolean; weight?: number}> =
({delay, children, size = 48, caps = true, weight = 400}) => {
  const p = useSpring(delay);
  return (
    <div style={{opacity: p, transform: `translateY(${interpolate(p, [0, 1], [26, 0])}px)`,
      color: WHITE, fontFamily: RALEWAY, fontWeight: weight, fontSize: size, lineHeight: 1.16,
      textTransform: caps ? "uppercase" : "none", whiteSpace: "nowrap", textShadow: "0 2px 14px rgba(0,0,0,.35)"}}>
      {children}
    </div>
  );
};

// la caja roja entra BARRIENDO de izquierda a derecha y el texto aparece encima
const Caja: React.FC<{delay: number; children: React.ReactNode; size?: number; caps?: boolean; ancho?: number; alto?: number; weight?: number; pad?: number}> =
({delay, children, size = 48, caps = true, ancho, alto = 60, weight = 400, pad = 18}) => {
  const p = useSpring(delay);
  const t = useSpring(delay + 5);
  return (
    <div style={{position: "relative", display: "inline-block", height: alto, width: ancho,
      margin: "6px 0", padding: ancho ? 0 : `0 ${pad}px`}}>
      <div style={{position: "absolute", inset: 0, background: RED, transformOrigin: "left center",
        transform: `scaleX(${p})`}} />
      <div style={{position: "relative", opacity: t, color: WHITE, fontFamily: RALEWAY, fontWeight: weight,
        fontSize: size, lineHeight: `${alto}px`, textTransform: caps ? "uppercase" : "none",
        whiteSpace: "nowrap", textAlign: "center"}}>{children}</div>
    </div>
  );
};

const Bloque: React.FC<{top: number; dur: number; children: React.ReactNode}> = ({top, dur, children}) => {
  const o = useSalida(dur);
  return (
    <div style={{position: "absolute", left: 0, right: 0, top, display: "flex", flexDirection: "column",
      alignItems: "center", textAlign: "center", opacity: o}}>{children}</div>
  );
};

const Clip: React.FC<{src: string; dur: number; escala?: number}> = ({src, dur, escala = 1}) => {
  const frame = useCurrentFrame();
  const entra = interpolate(frame, [0, 8], [0, 1], {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{opacity: entra}}>
      <OffthreadVideo src={staticFile(`${DIR}/${src}`)} muted 
        style={{width: "100%", height: "100%", objectFit: "cover", transform: `scale(${escala})`,
          transformOrigin: "center top"}} />
      {/* velo: parejo y más cargado abajo, donde van el texto y el sticker */}
      <AbsoluteFill style={{background: "linear-gradient(to bottom, rgba(0,0,0,.22) 0%, rgba(0,0,0,.12) 30%, rgba(0,0,0,.20) 50%, rgba(0,0,0,.42) 62%, rgba(0,0,0,.55) 78%, rgba(0,0,0,.58) 100%)"}} />
    </AbsoluteFill>
  );
};

const CIUDADES = ["Santiago", "Rancagua", "Chillán", "Concepción", "Temuco", "Puerto Montt"];
// cuadro (dentro de T3) en que la voz nombra cada ciudad: 8 + inicio medido × 30
// (2,39 · 3,11 · 3,74 · 4,52 · 5,04 · 5,24 s dentro de voz/t3.mp3, voz Lorenzo)
const CIUDAD_EN = [80, 101, 120, 144, 159, 165];

const Cierre: React.FC = () => {
  const frame = useCurrentFrame();
  // entran lento y sin rebote (ronda 2: el spring pasaba de largo y volvía)
  const p = interpolate(frame, [2, 30], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic)});
  const anillo = useSpring(10);
  const boton = interpolate(frame, [22, 36], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  // SANGRE: cada bloque se extiende 40 px FUERA del lienzo por sus dos bordes, para
  // que nunca quede una línea blanca entre el rojo y el borde del video
  const S = 40;
  const bloque = (lado: "sup" | "inf") => {
    const sup = lado === "sup";
    const dx = interpolate(p, [0, 1], [sup ? -600 : 600, 0]);
    return (
      <div style={{position: "absolute", transform: `translateX(${dx}px)`, left: 0, top: 0, width: 1080, height: 1920}}>
        {/* filete */}
        <div style={{position: "absolute", border: `3.5px solid ${RED}`,
          ...(sup ? {left: -20 - S, top: -20 - S, width: 547 + S, height: 246 + S, borderRadius: "0 0 52px 0"}
                  : {left: 530, top: 1693, width: 570 + S, height: 247 + S, borderRadius: "52px 0 0 0"})}} />
        {/* bloque macizo */}
        <div style={{position: "absolute", background: RED,
          ...(sup ? {left: -S, top: -S, width: 505 + S, height: 198 + S, borderRadius: "0 0 46px 0"}
                  : {left: 552, top: 1721, width: 528 + S, height: 199 + S, borderRadius: "46px 0 0 0"})}} />
      </div>
    );
  };
  return (
    <AbsoluteFill style={{background: WHITE}}>
      {bloque("sup")}
      {bloque("inf")}
      <Img src={staticFile(`${DIR}/logo_ebema_circulo.png`)} style={{position: "absolute", left: 344 - 30 * 1.649,
        top: 586 - 25 * 1.649, width: 310 * 1.649, opacity: anillo, transform: `scale(${interpolate(anillo, [0, 1], [0.86, 1])})`}} />
      {/* ronda 1: sube de 1261 a 1075 — queda a ~60 del anillo (que termina en 1015) */}
      <div style={{position: "absolute", left: 279.5, top: 1075, width: 521, height: 71, background: RED,
        color: WHITE, fontFamily: RALEWAY, fontWeight: 400, fontSize: 44, lineHeight: "71px", textAlign: "center",
        opacity: boton, filter: `blur(${interpolate(boton, [0, 1], [10, 0])}px)`}}>
        Toca el enlace
      </div>
    </AbsoluteFill>
  );
};

export const EbemaGrillaStoryClickOct: React.FC = () => {
  ensureFonts();
  return (
    <AbsoluteFill style={{background: "#111"}}>
      {ESC.map((e) => (
        <Sequence key={e.clip} from={e.from} durationInFrames={e.dur + 8}>
          <Clip src={e.clip} dur={e.dur} escala={(e as {escala?: number}).escala} />
        </Sequence>
      ))}

      {/* marco de las escenas: el lockup (no va en el cierre) */}
      <Sequence from={0} durationInFrames={CIERRE.from}>
        {/* ⚠️ En julio la tinta del lockup iba en y 369–479. Acá sube 115 (tinta 254–364):
            Kling acerca la cámara durante el plano y a 369 el lockup le caía en la frente
            al ferretero. */}
        <Img src={staticFile(`${DIR}/logo_click_2_blanco_acento.png`)}
          style={{position: "absolute", left: 247, top: 213.8, width: 585}} />
      </Sequence>

      {/* T1 */}
      <Sequence from={ESC[0].from} durationInFrames={ESC[0].dur}>
        <Bloque top={1150} dur={ESC[0].dur}>
          <Linea delay={10}>¿Cuánto tiempo</Linea>
          <Caja delay={18}>pierdes abasteciéndote?</Caja>
        </Bloque>
      </Sequence>

      {/* T2 */}
      <Sequence from={ESC[1].from} durationInFrames={ESC[1].dur}>
        <Bloque top={1150} dur={ESC[1].dur}>
          <Linea delay={8} caps={false}>Con Ebema Click compras online</Linea>
          <Caja delay={62} caps={false} weight={700}><Num t="24/7 y sin filas." /></Caja>
        </Bloque>
      </Sequence>

      {/* T3 — las ciudades de a una. El bloque sube a 930 para no invadir la franja
          del sticker (1450–1600). */}
      <Sequence from={ESC[2].from} durationInFrames={ESC[2].dur}>
        <Bloque top={930} dur={ESC[2].dur}>
          <Linea delay={8} weight={700}>Para ferreteros y</Linea>
          <Linea delay={13} weight={700}>contratistas de</Linea>
          <div style={{height: 14}} />
          {CIUDADES.map((c, i) => (
            <Caja key={c} delay={CIUDAD_EN[i]} caps={false} size={40} ancho={380} alto={56}>{c}</Caja>
          ))}
        </Bloque>
      </Sequence>

      {/* T4 */}
      <Sequence from={ESC[3].from} durationInFrames={ESC[3].dur}>
        <Bloque top={1150} dur={ESC[3].dur}>
          <Linea delay={8} caps={false}>Y cada mes sorteamos</Linea>
          {/* del ancho de «entre quienes compran.» (526): caja y texto crecen juntos, ×1,675 */}
          <Caja delay={57} caps={false} size={80.4} alto={100} pad={30}>una gift card</Caja>
          <Linea delay={74} caps={false}>entre quienes compran.</Linea>
        </Bloque>
      </Sequence>

      {/* T5 — cierre en blanco */}
      <Sequence from={CIERRE.from} durationInFrames={CIERRE.dur}>
        <Cierre />
      </Sequence>
    </AbsoluteFill>
  );
};
