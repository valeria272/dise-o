import React from "react";
import {
  AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig,
} from "remotion";

// =============================================================================
// EBEMA · GRILLA OCTUBRE 2026 · los 4 REELS de Instagram
//   01/10 Ebema Click · 03/10 catálogo Ebema.cl · 15/10 Perfiles Aza · 17/10 OSB LP TechShield
//   (27/10 San Bernardo NO: la grilla lo tiene PENDIENTE y pide metraje real de la Zona Ofertas)
//
// Calcado de los 5 reels de grilla de septiembre (raw/ebema/1-referencias/grilla/video),
// medidos al píxel el 28-09-2026 sobre los cuadros 4K. Todo va en coordenadas de 2160×3840.
//
//  · MARCO de familia A (EBEMA): banda roja arriba-izquierda 0–1012 × 0–396 con esquina r100,
//    filete de 9 px a 36–46 px de ella (r96); cápsula blanca del logo x 1432–1876 hasta y 452
//    (r60 abajo) con el anillo EBEMA x 1518–1797 · y 101–387; banda abajo-derecha
//    1104–2160 × 3442–3840 (r100) con su filete (r80). En el CIERRE queda el mismo marco sin cápsula.
//  · Familia C (Click): SIN bandas en el cuerpo; lockup «EBEMA CLICK · Materiales y
//    beneficios» x 544–1616 · y 732–972. El cierre sí lleva bandas (reel_click_sept).
//  · TIPOGRAFÍA: el cuerpo de los reels es MONTSERRAT (identificada por glifo: la M de patas
//    rectas y la V que baja a la línea base), no Raleway. El cierre oficial sí es Raleway.
//    Las cápsulas en versal roja y la 2.ª línea de Click van en Helvetica Bold.
//  · ARCO: T1 contexto + titular del proveedor → T2/T3 bloques de una caja roja → CIERRE con
//    un solo corte duro (cortina roja en diagonal) sobre BLANCO. En el cuerpo sólo fundidos.
//  · VOZ: los 5 de septiembre leen el brief palabra por palabra (transcritos con Whisper).
//    Lorenzo es-CL con el ajuste que Paulina aprobó el 24-09 (voz/generar.py).
//  · MÚSICA: audio_fondo3 (pista original de Paulina) desde el segundo 8, bajo la voz.
// =============================================================================

export const REELS_OCT_FPS = 30;
const RED = "#EC1C23", GREY = "#6D6F72", WHITE = "#FFFFFF";
const A = (f: string) => staticFile(`assets/ebema/grilla-oct26/reels/${f}`);

// ---------------------------------------------------------------------------- fuentes
let fontsOk = false;
const ensureFonts = () => {
  if (fontsOk || typeof document === "undefined") return;
  fontsOk = true;
  const rw = (w: number, f: string) =>
    `@font-face{font-family:'RalewayEB';font-weight:${w};font-display:block;src:url(${staticFile(`assets/ebema/fonts/${f}`)}) format('truetype');}`;
  const css = [
    `@font-face{font-family:'MontEB';font-weight:100 900;font-display:block;src:url(${staticFile("assets/fonts/Montserrat.ttf")}) format('truetype');}`,
    rw(400, "Raleway-Regular.ttf"), rw(500, "Raleway-Medium.ttf"), rw(600, "Raleway-SemiBold.ttf"), rw(700, "Raleway-Bold.ttf"),
    `@font-face{font-family:'HelvEB';font-weight:700;font-display:block;src:url(${staticFile("assets/ebema/fonts/Helvetica-Bold.ttf")}) format('truetype');}`,
  ].join("\n");
  const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  const fs = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (fs) {
    ["300", "400", "500", "700", "800"].forEach((w) => fs.load(`${w} 80px MontEB`));
    ["400", "500", "700"].forEach((w) => fs.load(`${w} 80px RalewayEB`));
    fs.load("700 80px HelvEB");
  }
};
const MONT = "'MontEB', Montserrat, Arial, sans-serif";
const RALE = "'RalewayEB', Raleway, Arial, sans-serif";
const HELV = "'HelvEB', Helvetica, Arial, sans-serif";

// ---------------------------------------------------------------------------- animación
const clamp = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;
/** Opacidad de un bloque que vive entre [a, b) con fundidos de entrada y salida. */
const vive = (f: number, a: number, b: number, fin = 10, fout = 8) =>
  Math.min(interpolate(f, [a, a + fin], [0, 1], clamp), interpolate(f, [b - fout, b], [1, 0], clamp));
const sube = (f: number, a: number, fps: number) =>
  interpolate(spring({fps, frame: f - a, config: {damping: 16, stiffness: 140}}), [0, 1], [40, 0]);

// ---------------------------------------------------------------------------- marco
const Marco: React.FC<{cierre?: boolean}> = ({cierre}) => (
  <AbsoluteFill style={{pointerEvents: "none"}}>
    <svg width={2160} height={3840} style={{position: "absolute", inset: 0}}>
      <path d="M0 0H1012V296A100 100 0 0 1 912 396H0Z" fill={RED} />
      <path d="M1051.5 0V350A96 96 0 0 1 955.5 446H0" fill="none" stroke={RED} strokeWidth={9} />
      <path d="M2160 3840H1104V3542A100 100 0 0 1 1204 3442H2160Z" fill={RED} />
      <path d="M1063.5 3840V3470A80 80 0 0 1 1143.5 3390H2160" fill="none" stroke={RED} strokeWidth={8} />
    </svg>
    {!cierre && (
      <div style={{position: "absolute", left: 1432, top: -60, width: 444, height: 512, background: WHITE,
        borderRadius: "0 0 60px 60px"}}>
        <Img src={A("logos/logo_ebema_anillo_claro.png")}
          style={{position: "absolute", left: 1513 - 1432, top: 161, width: 284}} />
      </div>
    )}
  </AbsoluteFill>
);

const LockupClick: React.FC = () => (
  <Img src={A("logos/ebemaclick_Logo_blanco.png")}
    style={{position: "absolute", left: 544 - 62 * (1072 / 2376), top: 732 - 140 * (1072 / 2376), width: 2500 * (1072 / 2376)}} />
);

// ---------------------------------------------------------------------------- planos
const Plano: React.FC<{src: string; velo?: number; zoom?: [number, number]; dur: number}> =
  ({src, velo = 0.3, zoom = [1, 1.04], dur}) => {
    const f = useCurrentFrame();
    const z = interpolate(f, [0, dur], zoom, clamp);
    return (
      <AbsoluteFill style={{background: "#000"}}>
        <AbsoluteFill style={{transform: `scale(${z})`}}>
          {src.endsWith(".mp4")
            ? <OffthreadVideo src={A(src)} muted style={{width: "100%", height: "100%", objectFit: "cover"}} />
            : <Img src={A(src)} style={{width: "100%", height: "100%", objectFit: "cover"}} />}
        </AbsoluteFill>
        <AbsoluteFill style={{background: `rgba(0,0,0,${velo})`}} />
      </AbsoluteFill>
    );
  };

/** Fotograma con celular: la pantalla real (captura o video) se compone dentro del
 *  hueco blanco del teléfono, medido sobre el keyframe (1520×2736 → cover a 2160×3840). */
const Celular: React.FC<{
  foto: string; pantalla: React.ReactNode; hueco: {x: number; y: number; w: number; h: number; rot?: number; r?: number};
  dur: number; velo?: number;
}> = ({foto, pantalla, hueco, dur, velo = 0.18}) => {
  const f = useCurrentFrame();
  const z = interpolate(f, [0, dur], [1, 1.035], clamp);
  const k = 2160 / 1520, oy = (2736 * k - 3840) / 2;
  return (
    <AbsoluteFill style={{background: "#000", overflow: "hidden"}}>
      <AbsoluteFill style={{transform: `scale(${z})`, transformOrigin: "50% 45%"}}>
        <Img src={A(foto)} style={{position: "absolute", left: 0, top: -oy, width: 2160, height: 2736 * k}} />
        <div style={{position: "absolute", left: hueco.x * k, top: hueco.y * k - oy, width: hueco.w * k, height: hueco.h * k,
          overflow: "hidden", borderRadius: (hueco.r ?? 34) * k, transform: `rotate(${hueco.rot ?? 0}deg)`, background: WHITE}}>
          {pantalla}
        </div>
        <AbsoluteFill style={{background: `rgba(0,0,0,${velo})`}} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/** Fundido entre planos del cuerpo (el sistema no tiene cortes secos salvo el del cierre). */
const Fundido: React.FC<{from: number; dur: number; children: React.ReactNode; fin?: number}> = ({from, dur, children, fin = 12}) => {
  const f = useCurrentFrame();
  const o = from === 0 ? 1 : interpolate(f, [from, from + fin], [0, 1], clamp);
  return (
    <Sequence from={from} durationInFrames={dur}>
      <AbsoluteFill style={{opacity: o}}>{children}</AbsoluteFill>
    </Sequence>
  );
};

// ---------------------------------------------------------------------------- bloques de texto
/** T1 · titular del proveedor: logo arriba, pre-enunciado, titular y cápsula blanca con versal roja.
 *  Septiembre lo llevaba girado −2° y con la caja roja envolviendo las dos líneas.
 *  ⭐ RONDA 1 de Paulina (28-09, portadas de Aza y LP, «aplican al reel también»):
 *   · «dejemos el enunciado derecho, sin rotación»
 *   · «el cuadro rojo debe llegar a la mitad de la primera línea» — la misma regla de la
 *     portada del carrusel (R-29): el rojo muerde la mitad de las mayúsculas de la 1.ª línea
 *   · la cápsula «debe ser mucho más grande» (56 → 96) */
const Titular: React.FC<{
  a: number; b: number; logo?: {src: string; w: number; top: number}; pre?: string | string[]; lineas: string[]; capsula?: string; top?: number;
  cuerpo: number; // la línea más larga llena ~1.600 px (medido: VH 160, catálogo sept 208)
}> = ({a, b, logo, pre, lineas, capsula, top = 2260, cuerpo}) => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const oLogo = vive(f, a + 12, b), oTit = vive(f, a, b), oCap = vive(f, a + 18, b);
  const sombra = "0 6px 22px rgba(0,0,0,.45)";
  const lh = Math.round(cuerpo * 0.98);
  // mitad de las mayúsculas de la 1.ª línea: el ojo de Montserrat deja ~0,16 em arriba de la versal
  const cortaRojo = Math.round(cuerpo * 0.16 + cuerpo * 0.7 / 2);
  return (
    <AbsoluteFill>
      {logo && (
        <Img src={A(logo.src)} style={{position: "absolute", left: 1080 - logo.w / 2, top: logo.top, width: logo.w,
          opacity: oLogo, transform: `scale(${interpolate(oLogo, [0, 1], [0.92, 1])})`, filter: "drop-shadow(0 12px 30px rgba(0,0,0,.35))"}} />
      )}
      <div style={{position: "absolute", left: 0, right: 0, top, display: "flex", flexDirection: "column", alignItems: "center",
        transform: `translateY(${sube(f, a, fps)}px)`}}>
        {pre && (Array.isArray(pre) ? pre : [pre]).map((t, i, arr) => (
          <div key={t} style={{opacity: oTit, fontFamily: MONT, fontWeight: 700, fontSize: 64, lineHeight: 1.15, color: WHITE, letterSpacing: 0.5,
            textTransform: "uppercase", marginBottom: i === arr.length - 1 ? 14 : 0, textShadow: sombra, textAlign: "center"}}>{t}</div>
        ))}
        <div style={{opacity: oTit, position: "relative", padding: "0 44px 26px"}}>
          <div style={{position: "absolute", left: 0, right: 0, top: cortaRojo, bottom: 0, background: RED,
            boxShadow: "0 18px 40px rgba(0,0,0,.25)"}} />
          {lineas.map((l) => (
            <div key={l} style={{position: "relative", fontFamily: MONT, fontWeight: 800, fontSize: cuerpo, lineHeight: `${lh}px`,
              color: WHITE, textAlign: "center", textTransform: "uppercase", whiteSpace: "nowrap", letterSpacing: -1, textShadow: sombra}}>{l}</div>
          ))}
        </div>
        {capsula && (
          <div style={{opacity: oCap, marginTop: -18, position: "relative", background: WHITE, padding: "12px 34px 10px",
            fontFamily: HELV, fontWeight: 700, fontSize: 96, color: RED, textTransform: "uppercase", whiteSpace: "nowrap"}}>{capsula}</div>
        )}
      </div>
    </AbsoluteFill>
  );
};

/** T2 · bloque de producto (VH_8): línea fina en versal + caja roja en versal + frase en bold. */
// ⭐ Ronda 2 (Paulina, 28-09): «los textos secundarios dejémoslo en 2 filas, pero nunca dejar una
// palabra sola como segunda fila; aplica para todos. Los textos no deben llegar nunca tan al borde
// del video» → toda línea secundaria deja ≥ 300 px de aire a cada lado (medido con PIL).
const BloqueProducto: React.FC<{a: number; b: number; fina: string | string[]; caja: string; bold?: {t: string[]; a: number; b: number}[]; top?: number}> =
  ({a, b, fina, caja, bold = [], top = 1950}) => {
    const f = useCurrentFrame(); const {fps} = useVideoConfig();
    const o = vive(f, a, b);
    return (
      <div style={{position: "absolute", left: 0, right: 0, top, display: "flex", flexDirection: "column", alignItems: "center",
        opacity: o, transform: `translateY(${sube(f, a, fps)}px)`}}>
        {(Array.isArray(fina) ? fina : [fina]).map((t) => (
          <div key={t} style={{fontFamily: MONT, fontWeight: 300, fontSize: 92, lineHeight: 1.05, color: WHITE, textTransform: "uppercase",
            letterSpacing: 1, textShadow: "0 4px 18px rgba(0,0,0,.45)", textAlign: "center"}}>{t}</div>
        ))}
        <div style={{background: RED, padding: "6px 170px 10px", fontFamily: MONT, fontWeight: 700, fontSize: 96, lineHeight: 1.1,
          color: WHITE, textTransform: "uppercase", letterSpacing: 1}}>{caja}</div>
        <div style={{position: "relative", height: 230, width: 2160}}>
          {bold.map((x) => (
            <div key={x.t.join(" ")} style={{position: "absolute", left: 0, right: 0, top: 44, textAlign: "center", fontFamily: MONT,
              fontWeight: 700, fontSize: 80, lineHeight: 1.18, color: WHITE, opacity: vive(f, x.a, x.b), textShadow: "0 4px 18px rgba(0,0,0,.5)"}}>
              {x.t.map((l) => <div key={l}>{l}</div>)}
            </div>
          ))}
        </div>
      </div>
    );
  };

/** T3 · dato de uso (VH_12): una línea liviana + una en bold con un filete rojo debajo. */
/** izquierda: sólo cuando la zona libre está a un costado del sujeto (R-20 manda sobre el centrado). */
const BloqueUso: React.FC<{a: number; b: number; liviana: string; bold: string | string[]; top?: number; izquierda?: number; filete?: number; cuerpoBold?: number}> =
({a, b, liviana, bold, top = 1880, izquierda, filete = 1400, cuerpoBold = 78}) => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const o = vive(f, a, b);
  const linea = interpolate(f, [a + 6, a + 26], [0, 1], clamp);
  return (
    <div style={{position: "absolute", left: izquierda ?? 0, right: izquierda === undefined ? 0 : undefined, top, display: "flex",
      flexDirection: "column", alignItems: izquierda === undefined ? "center" : "flex-start",
      opacity: o, transform: `translateY(${sube(f, a, fps)}px)`, textShadow: "0 4px 18px rgba(0,0,0,.5)"}}>
      <div style={{fontFamily: MONT, fontWeight: 400, fontSize: 70, color: WHITE, lineHeight: 1.1}}>{liviana}</div>
      {(Array.isArray(bold) ? bold : [bold]).map((t) => (
        <div key={t} style={{fontFamily: MONT, fontWeight: 700, fontSize: cuerpoBold, color: WHITE, lineHeight: 1.15}}>{t}</div>
      ))}
      <div style={{marginTop: 22, height: 9, width: filete * linea, background: RED}} />
    </div>
  );
};

/** Texto de Click (reel_click_sept_7): caja roja Raleway · versal Helvetica · caja roja Raleway. */
type LineaClick = {t: string; tipo: "caja" | "versal" | "blanca" | "bold"};
const BloqueClick: React.FC<{a: number; b: number; lineas: LineaClick[]; top?: number}> = ({a, b, lineas, top = 2160}) => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  return (
    <div style={{position: "absolute", left: 0, right: 0, top, display: "flex", flexDirection: "column", alignItems: "center", gap: 8}}>
      {lineas.map((l, i) => {
        const ai = a + i * 7;
        const st: React.CSSProperties = {opacity: vive(f, ai, b), transform: `translateY(${sube(f, ai, fps) * 0.6}px)`, whiteSpace: "nowrap"};
        if (l.tipo === "caja") return <div key={l.t} style={{...st, background: RED, padding: "2px 40px 12px", fontFamily: RALE, fontWeight: 400, fontSize: 90, color: WHITE}}>{l.t}</div>;
        if (l.tipo === "versal") return <div key={l.t} style={{...st, fontFamily: HELV, fontWeight: 700, fontSize: 88, color: WHITE, textTransform: "uppercase", textShadow: "0 4px 18px rgba(0,0,0,.5)"}}>{l.t}</div>;
        return <div key={l.t} style={{...st, fontFamily: RALE, fontWeight: l.tipo === "bold" ? 700 : 400, fontSize: 90, color: WHITE, textShadow: "0 4px 18px rgba(0,0,0,.5)"}}>{l.t}</div>;
      })}
    </div>
  );
};

// ---------------------------------------------------------------------------- cierre
/** Cortina roja en diagonal (reel_VH 14,9 s) y después el cierre sobre blanco puro. */
const Cortina: React.FC = () => {
  const f = useCurrentFrame();
  const p = interpolate(f, [0, 12], [0, 1], clamp);
  const x = interpolate(p, [0, 1], [-2600, 2600]);
  const o = interpolate(f, [10, 16], [1, 0], clamp);
  return (
    <AbsoluteFill style={{pointerEvents: "none", opacity: o}}>
      <svg width={2160} height={3840} style={{position: "absolute", inset: 0}}>
        <polygon points={`${x},3840 ${x + 2600},3840 ${x + 5200},0 ${x + 2600},0`} fill={RED} />
      </svg>
    </AbsoluteFill>
  );
};

type Cierre = {
  arriba?: {t: string; bold?: boolean}[];   // líneas grises sobre el botón o el anillo
  boton?: string;                            // caja roja
  bajoBoton?: string;                        // línea gris bajo el botón (catálogo)
  anilloTop?: number; anilloW?: number;
  orden?: "texto-anillo" | "anillo-texto" | "texto-anillo-boton";
  textoTop?: number;
};
const CierreBlanco: React.FC<{c: Cierre}> = ({c}) => {
  const f = useCurrentFrame();
  const o = interpolate(f, [4, 40], [0, 1], clamp);
  const aw = c.anilloW ?? 662;
  const lineas = (c.arriba ?? []).map((l) => (
    <div key={l.t} style={{fontFamily: RALE, fontWeight: l.bold ? 700 : 400, fontSize: 118, color: GREY, lineHeight: 1.12,
      whiteSpace: "nowrap", textAlign: "center"}}>{l.t}</div>
  ));
  const boton = c.boton && (
    <div style={{background: RED, color: WHITE, fontFamily: RALE, fontWeight: 400, fontSize: 104, padding: "6px 30px 16px",
      borderRadius: 14, whiteSpace: "nowrap", marginTop: 26}}>{c.boton}</div>
  );
  return (
    <AbsoluteFill style={{background: WHITE}}>
      <Marco cierre />
      <AbsoluteFill style={{opacity: o}}>
        <div style={{position: "absolute", left: 0, right: 0, top: c.textoTop ?? 1250, display: "flex", flexDirection: "column", alignItems: "center"}}>
          {lineas}
          {c.orden !== "texto-anillo-boton" && boton}
        </div>
        <Img src={A("logos/logo_ebema_anillo_claro.png")}
          style={{position: "absolute", left: 1090 - aw / 2, top: c.anilloTop ?? 1938, width: aw * (952 / 935)}} />
        {c.orden === "texto-anillo-boton" && (
          <div style={{position: "absolute", left: 0, right: 0, top: (c.anilloTop ?? 1554) + 900, display: "flex", flexDirection: "column", alignItems: "center"}}>
            <div style={{background: RED, color: WHITE, fontFamily: RALE, fontWeight: 400, fontSize: 104, padding: "6px 34px 16px", borderRadius: 14, whiteSpace: "nowrap"}}>{c.boton}</div>
            {c.bajoBoton && <div style={{fontFamily: RALE, fontWeight: 400, fontSize: 88, color: GREY, marginTop: 14}}>{c.bajoBoton}</div>}
          </div>
        )}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------------------- audio
type Voz = {src: string; at: number};
const Sonido: React.FC<{voces: Voz[]; total: number}> = ({voces, total}) => (
  <>
    {voces.map((v) => (
      <Sequence key={v.src} from={v.at}><Audio src={A(`voz/${v.src}`)} volume={1} /></Sequence>
    ))}
    <Audio src={A("musica/audio_fondo3.mp3")} startFrom={8 * 30}
      volume={(f) => interpolate(f, [0, 20, total - 30, total], [0, 0.32, 0.32, 0], clamp)} />
  </>
);

// ---------------------------------------------------------------------------- pantallas reales
/** Catálogo real de ebema.cl/catalogos (capturado el 28-09 a 390×844 @3x): baja la página. */
const PantallaCatalogo: React.FC<{dur: number}> = ({dur}) => {
  const f = useCurrentFrame();
  // 1170 px de ancho de captura → ancho del hueco; se recorre de la tarjeta 1 a la de Madera
  const y = interpolate(f, [8, dur - 6], [0, 11800], {...clamp, easing: (t) => t * t * (3 - 2 * t)});
  return (
    <div style={{position: "absolute", inset: 0, overflow: "hidden", background: WHITE}}>
      <Img src={A("ui/catalogos.jpg")} style={{position: "absolute", left: 0, top: 0, width: "100%",
        transform: `translateY(${-(y / 16386) * 100}%)`}} />
      <Img src={A("ui/wsp_boton.png")} style={{position: "absolute", left: 0, bottom: "1.2%", width: "76.9%"}} />
    </div>
  );
};
/** T3 del catálogo: se toca el botón de WhatsApp y se abre el chat real con las sucursales. */
const PantallaChat: React.FC = () => {
  const f = useCurrentFrame();
  const abierto = interpolate(f, [26, 34], [0, 1], clamp);
  const toque = interpolate(f, [14, 22, 30], [0, 1, 0], clamp);
  return (
    <div style={{position: "absolute", inset: 0, overflow: "hidden"}}>
      <Img src={A("ui/cat_antes_chat.png")} style={{position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover"}} />
      <Img src={A("ui/cat_chat_abierto.png")} style={{position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover", opacity: abierto}} />
      <div style={{position: "absolute", left: "7.2%", top: "90.9%", width: "14.4%", aspectRatio: "1", borderRadius: "50%",
        background: "rgba(255,255,255,.55)", transform: `scale(${0.6 + toque * 0.9})`, opacity: toque}} />
    </div>
  );
};
/** App real de Ebema Click (video de Paulina): `app_click_30.mp4` = el original desde el segundo 1,9
 *  (se salta el inicio de sesión, que muestra un teléfono) a 30 fps constantes — el original
 *  hacía fallar el compositor de forma intermitente («No frame found», 28-09). */
const PantallaApp: React.FC = () => (
  <OffthreadVideo src={A("ui/app_click_30.mp4")} muted
    style={{width: "100%", height: "100%", objectFit: "cover"}} />
);

// ---------------------------------------------------------------------------- mapa (Click T3)
// El mapa de LinkedIn (click3_mapa, Nano Banana Pro 25-09) empieza EN Santiago: puesto en
// 9:16, Santiago y Rancagua caían al 4 % del alto, bajo la interfaz de Instagram. Se alejó
// la cámara hacia el norte con Nano Banana Pro (ui/mapa_click_norte.jpg, 1536×2752) y los
// pines de Paulina se trasladaron registrando los dos mapas con SIFT + afín (120 puntos,
// error mediano 3,5 px). Coordenadas en píxeles del mapa nuevo.
const CIUDADES: [number, number, string][] = [
  [868.5, 832.2, "Santiago"], [834.0, 944.3, "Rancagua"], [714.7, 1160.7, "Chillán"],
  [613.7, 1266.9, "Concepción"], [634.8, 1456.2, "Temuco"], [515.4, 1667.5, "Puerto Montt"]];
const Mapa: React.FC<{dur: number}> = ({dur}) => {
  const f = useCurrentFrame();
  // Ronda 1: el lockup de Click ahora sigue sobre el mapa → se acerca el mapa anclado arriba
  // (×1,2) para que Santiago baje de y≈1160 a ≈1390 y no quede pegado al lockup (R-21).
  const z = interpolate(f, [0, dur], [1.2, 1.25], clamp);
  const s = 2160 / 1536, oy = (2752 * s - 3840) / 2;
  const px = (x: number) => x * s, py = (y: number) => y * s - oy;
  return (
    <AbsoluteFill style={{background: "#000", overflow: "hidden"}}>
      <AbsoluteFill style={{transform: `scale(${z})`, transformOrigin: "50% 0%"}}>
        <Img src={A("ui/mapa_click_norte.jpg")} style={{position: "absolute", left: 0, top: -oy, width: 2160, height: 2752 * s}} />
        <AbsoluteFill style={{background: "rgba(0,0,0,.12)"}} />
        {CIUDADES.map(([x, y, n], i) => {
          const a = 8 + i * 9;
          const p = spring({fps: 30, frame: f - a, config: {damping: 11, stiffness: 160}});
          return (
            <div key={n} style={{position: "absolute", left: px(x) - 42, top: py(y) - 110, opacity: Math.min(1, p * 1.4)}}>
              <svg width={84} height={110} viewBox="0 0 60 78" style={{transform: `translateY(${(1 - p) * -60}px)`}}>
                <path d="M30 0C13.4 0 0 13.4 0 30c0 21 30 48 30 48s30-27 30-48C60 13.4 46.6 0 30 0z" fill={RED} />
                <circle cx="30" cy="29" r="11" fill={WHITE} />
              </svg>
              <div style={{position: "absolute", left: 104, top: 12, fontFamily: RALE, fontWeight: 600, fontSize: 66, color: WHITE,
                whiteSpace: "nowrap", textShadow: "0 3px 14px rgba(0,0,0,.75)"}}>{n}</div>
            </div>
          );
        })}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

// =============================================================================
// LOS 4 GUIONES — textos VERBATIM de la grilla (R-03). Tiempos en cuadros a 30 fps:
// cada tramo dura lo que habla su mp3 (pausa final medida con silencedetect) + ~0,35 s.
// =============================================================================
const s = (x: number) => Math.round(x * 30);

// ---------------------------------------------------------------- 01/10 · EBEMA CLICK
const CK = {t1: 0, t2: s(3.15), camion: s(3.15 + 2.9), t3: s(3.15 + 4.7), cierre: s(3.15 + 4.7 + 5.45)};
export const CK_DUR = CK.cierre + s(4.15 + 1.2);
export const EbemaReelClickOct: React.FC = () => {
  ensureFonts();
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <Fundido from={CK.t1} dur={CK.t2 + 12}><Plano src="clips/click_k1_30.mp4" dur={CK.t2 + 12} velo={0.32} /></Fundido>
      <Fundido from={CK.t2} dur={CK.camion - CK.t2 + 12}>
        <Celular foto="keyframes/click_k2.jpg" dur={CK.camion - CK.t2 + 12} pantalla={<PantallaApp />}
          hueco={{x: 321, y: 1016, w: 386, h: 892, rot: 0.94, r: 30}} velo={0.2} />
      </Fundido>
      <Fundido from={CK.camion} dur={CK.t3 - CK.camion + 12}><Plano src="clips/click_k3_30.mp4" dur={CK.t3 - CK.camion + 12} velo={0.3} /></Fundido>
      <Fundido from={CK.t3} dur={CK.cierre - CK.t3}><Mapa dur={CK.cierre - CK.t3} /></Fundido>
      {/* bajo el lockup, un velo que asienta el blanco (Click no lleva bandas).
          Ronda 1 (Paulina, 28-09): «mantener el logo de ebema en todo el video hasta que llegue
          al cierre» → el lockup sigue también sobre el mapa. */}
      <Sequence from={0} durationInFrames={CK.cierre}>
        <AbsoluteFill style={{background: "linear-gradient(180deg, rgba(0,0,0,.35) 0%, rgba(0,0,0,0) 32%, rgba(0,0,0,0) 50%, rgba(0,0,0,.45) 80%)"}} />
        <LockupClick />
      </Sequence>
      <Sequence from={0} durationInFrames={CK.t3}>
        {/* Ronda 1: «el bloque de texto debe ir más arriba, en la zona donde no hay objetos
            sobre la persona» → entre el lockup (termina en y 972) y el casco (~y 1650). */}
        <BloqueClick top={1130} a={s(0.4)} b={CK.t2 - 2} lineas={[
          {t: "¿Sigues perdiendo horas", tipo: "caja"}, {t: "pidiendo materiales", tipo: "blanca"}, {t: "por teléfono?", tipo: "bold"}]} />
        <BloqueClick a={CK.t2 + 6} b={CK.t3 - 2} lineas={[
          {t: "Con Ebema Click compras online", tipo: "caja"}, {t: "24/7, sin filas", tipo: "versal"}, {t: "y con despacho directo.", tipo: "caja"}]} />
      </Sequence>
      <Sequence from={CK.cierre}>
        <CierreBlanco c={{orden: "anillo-texto", anilloTop: 1172, anilloW: 809, textoTop: 2200,
          arriba: [{t: "Regístrate gratis"}, {t: "y participa en el sorteo"}, {t: "de una gift card cada mes.", bold: true}]}} />
        <Cortina />
      </Sequence>
      <Sonido total={CK_DUR} voces={[{src: "click_t1.mp3", at: CK.t1}, {src: "click_t2.mp3", at: CK.t2},
        {src: "click_t3.mp3", at: CK.t3}, {src: "click_t4.mp3", at: CK.cierre}]} />
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------- 03/10 · CATÁLOGO EBEMA.CL
const CT = {t1: 0, t1b: s(3.65), t2: s(7.25), t3: s(7.25 + 6.45), t4: s(7.25 + 6.45 + 4.8), cierre: s(7.25 + 6.45 + 4.8 + 2.95)};
export const CT_DUR = CT.cierre + s(3.6 + 1.3);
export const EbemaReelCatalogoOct: React.FC = () => {
  ensureFonts();
  const cel = {x: 580, y: 750, w: 438, h: 1033, r: 40};
  return (
    <AbsoluteFill style={{background: "#000"}}>
      {/* Ronda 1 (Paulina, 28-09): «el video principal dura mucho tiempo, añadir más escenas;
          añadamos más texto normal que se usa en reel» → el T1 se parte en la pausa de la voz
          (3,54 s): el maestro con el plano y después sus manos marcando la lista. */}
      <Fundido from={CT.t1} dur={CT.t1b + 12}><Plano src="clips/cat_k1_30.mp4" dur={CT.t1b + 12} /></Fundido>
      <Fundido from={CT.t1b} dur={CT.t2 - CT.t1b + 12}><Plano src="clips/cat_k1b_30.mp4" dur={CT.t2 - CT.t1b + 12} velo={0.26} /></Fundido>
      <Fundido from={CT.t2} dur={CT.t3 - CT.t2 + 12}>
        <Celular foto="keyframes/cat_k2.jpg" dur={CT.t3 - CT.t2 + 12} hueco={cel} pantalla={<PantallaCatalogo dur={CT.t3 - CT.t2} />} />
      </Fundido>
      <Sequence from={CT.t3} durationInFrames={CT.t4 - CT.t3 + 12}>
        <Celular foto="keyframes/cat_k2.jpg" dur={CT.t4 - CT.t3 + 12} hueco={cel} pantalla={<PantallaChat />} />
      </Sequence>
      <Fundido from={CT.t4} dur={CT.cierre - CT.t4}><Plano src="clips/cat_k4_30.mp4" dur={CT.cierre - CT.t4} /></Fundido>
      <Sequence from={0} durationInFrames={CT.cierre}>
        <Marco />
        <Titular a={s(0.6)} b={CT.t1b + 4} lineas={["¿Vas a cotizar", "materiales"]} capsula="para tu obra?" top={2150} cuerpo={179} />
        {/* texto «normal» de reel en la zona libre: el muro desenfocado a la IZQUIERDA del
            maestro, alineado a la izquierda (R-20 manda: nunca sobre la persona ni sobre la
            tabla). En el clip animado el chaleco empieza en x≈1160 a esa altura. */}
        <BloqueUso a={CT.t1b + 8} b={CT.t2} liviana="Lo último que necesitas es" bold={["perder tiempo buscando", "uno por uno."]} top={1180} izquierda={200} filete={900} cuerpoBold={72} />
        <BloqueProducto a={CT.t2 + 10} b={CT.t3} fina="Revisa el catálogo" caja="por categoría" top={2780} />
        <BloqueProducto a={CT.t3 + 6} b={CT.t4} fina={["Cotiza de forma", "personalizada"]} caja="por WhatsApp" top={2780} />
        <BloqueUso a={CT.t4 + 6} b={CT.cierre} liviana="Los materiales que necesitas" bold="para tu obra, en Ebema." top={2050} />
      </Sequence>
      <Sequence from={CT.cierre}>
        <CierreBlanco c={{orden: "texto-anillo-boton", textoTop: 1080, anilloTop: 1554, anilloW: 662,
          arriba: [{t: "Revisa el catálogo", bold: true}, {t: "en Ebema.cl"}], boton: "Cotiza por WhatsApp",
          bajoBoton: "desde el link en nuestra bio."}} />
        <Cortina />
      </Sequence>
      <Sonido total={CT_DUR} voces={[{src: "catalogo_t1.mp3", at: CT.t1}, {src: "catalogo_t2.mp3", at: CT.t2},
        {src: "catalogo_t3.mp3", at: CT.t3}, {src: "catalogo_t4.mp3", at: CT.t4}]} />
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------- 15/10 · PERFILES AZA
const AZ = {t1: 0, t2: s(4.45), t3: s(4.45 + 8.95), cierre: s(4.45 + 8.95 + 5.65)};
export const AZ_DUR = AZ.cierre + s(4.3);
export const EbemaReelAzaOct: React.FC = () => {
  ensureFonts();
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <Fundido from={AZ.t1} dur={AZ.t2 + 12}><Plano src="clips/aza_k1_30.mp4" dur={AZ.t2 + 12} /></Fundido>
      <Fundido from={AZ.t2} dur={AZ.t3 - AZ.t2 + 12}><Plano src="clips/aza_k2_30.mp4" dur={AZ.t3 - AZ.t2 + 12} velo={0.34} /></Fundido>
      <Fundido from={AZ.t3} dur={AZ.cierre - AZ.t3}><Plano src="clips/aza_k3_30.mp4" dur={AZ.cierre - AZ.t3} /></Fundido>
      <Sequence from={0} durationInFrames={AZ.cierre}>
        <Marco />
        <Titular a={s(0.9)} b={AZ.t2 - 2} logo={{src: "logos/logo_aza_negativo.png", w: 900, top: 1330}}
          pre={["Reforzar una estructura", "también puede ser"]} lineas={["una decisión", "más consciente"]} capsula="con el planeta" cuerpo={167} />
        <BloqueProducto a={AZ.t2 + 10} b={AZ.t3} fina="Perfiles Aza" caja="Acero Verde"
          bold={[{t: ["Acero reciclado, con menor", "huella de carbono."], a: AZ.t2 + 22, b: AZ.t2 + s(4.9)},
            {t: ["El mismo desempeño de un", "perfil convencional."], a: AZ.t2 + s(4.9), b: AZ.t3}]} />
        <BloqueUso a={AZ.t3 + 6} b={AZ.cierre} liviana="Se sueldan y atornillan" bold="igual que un perfil convencional." />
      </Sequence>
      <Sequence from={AZ.cierre}>
        <CierreBlanco c={{textoTop: 1120, arriba: [{t: "Perfiles Aza,"}, {t: "disponibles en Ebema.", bold: true}], boton: "Cotiza directo por WhatsApp"}} />
        <Cortina />
      </Sequence>
      <Sonido total={AZ_DUR} voces={[{src: "aza_t1.mp3", at: AZ.t1}, {src: "aza_t2.mp3", at: AZ.t2},
        {src: "aza_t3.mp3", at: AZ.t3}, {src: "aza_t4.mp3", at: AZ.cierre}]} />
    </AbsoluteFill>
  );
};

// ---------------------------------------------------------------- 17/10 · OSB LP TECHSHIELD
const LP = {t1: 0, t2: s(3.25), t3: s(3.25 + 6.75), cierre: s(3.25 + 6.75 + 5.7)};
export const LP_DUR = LP.cierre + s(4.6);
export const EbemaReelLpOct: React.FC = () => {
  ensureFonts();
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <Fundido from={LP.t1} dur={LP.t2 + 12}><Plano src="clips/lp_k1_30.mp4" dur={LP.t2 + 12} /></Fundido>
      <Fundido from={LP.t2} dur={LP.t3 - LP.t2 + 12}><Plano src="clips/lp_k2_30.mp4" dur={LP.t3 - LP.t2 + 12} /></Fundido>
      <Fundido from={LP.t3} dur={LP.cierre - LP.t3}><Plano src="clips/lp_k3_30.mp4" dur={LP.cierre - LP.t3} /></Fundido>
      <Sequence from={0} durationInFrames={LP.cierre}>
        <Marco />
        <Titular a={s(0.6)} b={LP.t2 - 2} logo={{src: "logos/logo_lp.png", w: 560, top: 1300}}
          pre="Hay tableros que también trabajan" lineas={["por bajar", "la temperatura"]} capsula="Tablero OSB LP TechShield" cuerpo={162} />
        <BloqueProducto a={LP.t2 + 10} b={LP.t3} fina="Tablero OSB LP" caja="TechShield"
          bold={[{t: ["Barrera que refleja", "el calor,"], a: LP.t2 + 22, b: LP.t2 + s(3.9)},
            {t: ["además de la resistencia", "estructural de un OSB."], a: LP.t2 + s(3.9), b: LP.t3}]} />
        <BloqueUso a={LP.t3 + 6} b={LP.cierre} liviana="Se corta e instala" bold="igual que un tablero OSB estructural." />
      </Sequence>
      <Sequence from={LP.cierre}>
        <CierreBlanco c={{textoTop: 1120, arriba: [{t: "Tablero OSB LP TechShield,"}, {t: "disponible en Ebema.", bold: true}], boton: "Cotiza directo por WhatsApp"}} />
        <Cortina />
      </Sequence>
      <Sonido total={LP_DUR} voces={[{src: "lp_t1.mp3", at: LP.t1}, {src: "lp_t2.mp3", at: LP.t2},
        {src: "lp_t3.mp3", at: LP.t3}, {src: "lp_t4.mp3", at: LP.cierre}]} />
    </AbsoluteFill>
  );
};

// =============================================================================
// 27/10 · EBEMA SAN BERNARDO — ZONA OFERTAS CONSTRUCTOR
// ⛔ METRAJE REAL, SIN IA (Paulina, 28-09): «este tipo de reel es más promocional, hay que
//    conectar con el cliente». Cortes en `sanbernardo/cortar.py`; Seba sólo cuando MUESTRA.
// Gramática: la del reel anterior de la misma zona (`reel_3.mp4`, junio, la «REF ANTERIOR»
// de la grilla): cápsula del logo arriba a la IZQUIERDA, subtítulos Montserrat con la 2.ª
// línea en caja roja, cierre blanco con la dirección en caja roja y los horarios con reloj.
// Ritmo: el de la referencia de Construmart (un corte y una ETIQUETA por categoría).
// Reglas de Paulina de hoy que también rigen acá: titular derecho con el rojo desde la mitad
// de la 1.ª línea; secundarios en ≤ 2 filas sin palabra sola y ≥ 300 px de aire; texto
// nunca sobre la persona; sin portada.
// =============================================================================
const SB = (f: string) => `sanbernardo/cortes/${f}.mp4`;
const TITULO_SB = 190; // «ZONA OFERTAS» llena ~1.600 px (regla de ancho del titular)

/** Cápsula del logo arriba a la izquierda (reel_3: x 0–468 · y 380–700). */
const CapsulaIzq: React.FC = () => (
  <div style={{position: "absolute", left: -60, top: 380, width: 528, height: 320, background: WHITE, borderRadius: 44,
    boxShadow: "0 10px 30px rgba(0,0,0,.18)"}}>
    <Img src={A("logos/logo_ebema_anillo_claro.png")} style={{position: "absolute", left: 60 + 95, top: 22, width: 276}} />
  </div>
);

/** Subtítulo del reel_3: línea blanca Montserrat 700 + línea en caja roja. */
const Subtitulo: React.FC<{a: number; b: number; blanca?: string; roja?: string; top?: number}> = ({a, b, blanca, roja, top = 2700}) => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const o = vive(f, a, b, 6, 5);
  return (
    <div style={{position: "absolute", left: 0, right: 0, top, display: "flex", flexDirection: "column", alignItems: "center",
      opacity: o, transform: `translateY(${sube(f, a, fps) * 0.5}px)`}}>
      {blanca && <div style={{fontFamily: MONT, fontWeight: 700, fontSize: 84, color: WHITE, lineHeight: 1.18, whiteSpace: "nowrap",
        textShadow: "0 4px 18px rgba(0,0,0,.55)"}}>{blanca}</div>}
      {roja && <div style={{background: RED, padding: "0 26px 6px", fontFamily: MONT, fontWeight: 700, fontSize: 84, color: WHITE,
        lineHeight: 1.18, whiteSpace: "nowrap"}}>{roja}</div>}
    </div>
  );
};

/** Etiqueta de categoría (ritmo Construmart): versal grande en caja roja, en la zona libre. */
const Etiqueta: React.FC<{t: string; dur: number; top?: number}> = ({t, dur, top = 820}) => {
  const f = useCurrentFrame();
  const p = spring({fps: 30, frame: f, config: {damping: 14, stiffness: 220}});
  const o = interpolate(f, [dur - 3, dur], [1, 0], clamp);
  return (
    <div style={{position: "absolute", left: 0, right: 0, top, display: "flex", justifyContent: "center", opacity: o}}>
      <div style={{background: RED, padding: "6px 44px 14px", fontFamily: MONT, fontWeight: 800, fontSize: 132, color: WHITE,
        textTransform: "uppercase", letterSpacing: 1, transform: `scale(${interpolate(p, [0, 1], [0.85, 1])})`,
        opacity: Math.min(1, p * 1.5), boxShadow: "0 16px 40px rgba(0,0,0,.25)"}}>{t}</div>
    </div>
  );
};

const Icono: React.FC<{tipo: "pin" | "reloj"; c: string; s: number}> = ({tipo, c, s}) => tipo === "pin" ? (
  <svg width={s} height={s} viewBox="0 0 24 24" style={{marginRight: 18, flexShrink: 0}}>
    <path d="M12 2C8.1 2 5 5.1 5 9c0 5.3 7 13 7 13s7-7.7 7-13c0-3.9-3.1-7-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z" fill={c} />
  </svg>
) : (
  <svg width={s} height={s} viewBox="0 0 24 24" style={{marginRight: 16, flexShrink: 0}}>
    <circle cx="12" cy="12" r="9.5" fill="none" stroke={c} strokeWidth="2.2" />
    <path d="M12 6.5V12l3.6 2.2" fill="none" stroke={c} strokeWidth="2.2" strokeLinecap="round" />
  </svg>
);

/** Cierre del reel_3 medido: anillo x 746–1397 · y 1166–1835; dirección en caja roja desde
 *  y 2000; horarios en gris con reloj. Todas las cifras en Helvetica Bold (R-02). */
const CierreSB: React.FC = () => {
  const f = useCurrentFrame();
  const o = interpolate(f, [4, 36], [0, 1], clamp);
  return (
    <AbsoluteFill style={{background: WHITE}}>
      <Marco cierre />
      <AbsoluteFill style={{opacity: o}}>
        <Img src={A("logos/logo_ebema_anillo_claro.png")} style={{position: "absolute", left: 1071 - 651 / 2, top: 1166, width: 651 * (952 / 935)}} />
        <div style={{position: "absolute", left: 0, right: 0, top: 2000, display: "flex", flexDirection: "column", alignItems: "center"}}>
          {/* RONDA 1 · 29-09 (Paulina, 24,7 s): «dejemos el texto del cuadro rojo en una sola línea
              bajando un poco el pt para que no llegue tan a los bordes el cuadro» (80 → 60, una línea) */}
          <div style={{display: "flex", alignItems: "center", background: RED, padding: "14px 40px 16px", color: WHITE, fontFamily: HELV,
            fontWeight: 700, fontSize: 60, lineHeight: 1.15, whiteSpace: "nowrap"}}>
            <Icono tipo="pin" c={WHITE} s={66} />
            <div>Av. General Velásquez 10985, San Bernardo</div>
          </div>
          {["Lunes y martes 8:30 a 18:00 hrs", "Miércoles a viernes 8:30 a 17:00 hrs"].map((t, i) => (
            <div key={t} style={{display: "flex", alignItems: "center", marginTop: i === 0 ? 44 : 14, fontFamily: HELV, fontWeight: 700,
              fontSize: 76, color: GREY}}>
              <Icono tipo="reloj" c={GREY} s={70} />{t}
            </div>
          ))}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/** Corte seco entre planos reales (ritmo Construmart; el reel_3 también corta en seco). */
const Corte: React.FC<{from: number; dur: number; src: string; velo?: number; zoom?: [number, number]; children?: React.ReactNode}> =
  ({from, dur, src, velo = 0.18, zoom = [1, 1.03], children}) => (
    <Sequence from={from} durationInFrames={dur}>
      <Plano src={src} dur={dur} velo={velo} zoom={zoom} />
      {children}
    </Sequence>
  );

// Tiempos medidos con Whisper sobre los mp3 (voz/generar.py → sb_t1..t4)
const SBT = {t1: 0, t1b: s(2.1), t2: s(5.2)};
const T2 = SBT.t2;
const SBC = {cer: T2 + s(3.6), pis: T2 + s(4.5), adi: T2 + s(5.1), pin: T2 + s(5.9), adh: T2 + s(6.6), mas: T2 + s(7.05)};
const T3 = T2 + s(8.2), T3b = T3 + s(2.3), T4 = T3 + s(4.8), T4b = T4 + s(1.3), CIE = T4 + s(3.45);
export const SB_DUR = CIE + s(5.3 + 1.2);
export const EbemaReelSanBernardoOct: React.FC = () => {
  ensureFonts();
  const f = useCurrentFrame();
  const zFachada = interpolate(f, [T4b, CIE], [1.02, 1.1], clamp);
  return (
    <AbsoluteFill style={{background: "#000"}}>
      {/* T1 · llegada (se ve el letrero OFERTAS CONSTRUCTOR en la fachada) + el container */}
      <Corte from={SBT.t1} dur={SBT.t1b} src={SB("t1_llegada")} />
      <Corte from={SBT.t1b} dur={T2 - SBT.t1b} src={SB("t1_container")} velo={0.28} />
      {/* T2 · variedad + una etiqueta por categoría */}
      <Corte from={T2} dur={SBC.cer - T2} src={SB("t2_ceramicas_oferta")} />
      <Corte from={SBC.cer} dur={SBC.pis - SBC.cer} src={SB("t2_ceramicas")}><Etiqueta t="Cerámicas" dur={SBC.pis - SBC.cer} /></Corte>
      <Corte from={SBC.pis} dur={SBC.adi - SBC.pis} src={SB("t2_pisos")}><Etiqueta t="Pisos" dur={SBC.adi - SBC.pis} top={1500} /></Corte>
      <Corte from={SBC.adi} dur={SBC.pin - SBC.adi} src={SB("t2_aditivos")}><Etiqueta t="Aditivos" dur={SBC.pin - SBC.adi} /></Corte>
      <Corte from={SBC.pin} dur={SBC.adh - SBC.pin} src={SB("t2_pinturas")}><Etiqueta t="Pinturas" dur={SBC.adh - SBC.pin} /></Corte>
      <Corte from={SBC.adh} dur={SBC.mas - SBC.adh} src={SB("t2_adhesivos")}><Etiqueta t="Adhesivos" dur={SBC.mas - SBC.adh} top={1500} /></Corte>
      <Corte from={SBC.mas} dur={T3 - SBC.mas} src={SB("t2_mas")}><Etiqueta t="¡Y mucho más!" dur={T3 - SBC.mas} /></Corte>
      {/* T3 · stock + carteles de precio */}
      <Corte from={T3} dur={T3b - T3} src={SB("t3_stock")} />
      <Corte from={T3b} dur={T4 - T3b} src={SB("t3_precios")} />
      {/* T4 · Seba invita + la fachada real */}
      <Corte from={T4} dur={T4b - T4} src={SB("t4_seba")} />
      <Sequence from={T4b} durationInFrames={CIE - T4b}>
        <AbsoluteFill style={{overflow: "hidden", background: "#000"}}>
          <Img src={A("sanbernardo/fachada.png")} style={{width: "100%", height: "100%", objectFit: "cover", transform: `scale(${zFachada})`}} />
          <AbsoluteFill style={{background: "rgba(0,0,0,.18)"}} />
        </AbsoluteFill>
      </Sequence>

      {/* capa gráfica del cuerpo */}
      <Sequence from={0} durationInFrames={CIE}>
        <AbsoluteFill style={{background: "linear-gradient(180deg, rgba(0,0,0,0) 58%, rgba(0,0,0,.42) 86%)"}} />
        <CapsulaIzq />
        <Subtitulo a={s(0.1)} b={SBT.t1b} blanca="Si estás con una" roja="obra en marcha," />
        {/* la cápsula «te puede ahorrar más de un peso» medía 1.923 px a cuerpo 96 (regla de ≥ 300 px
            de aire): baja al subtítulo en dos filas */}
        {/* RONDA 1 · 29-09 (Paulina, 3,4 s): «elimina la línea de texto de arriba "esta zona de ebema..."» */}
        <Titular a={SBT.t1b + 2} b={T2} lineas={["Zona Ofertas", "Constructor"]}
          top={1900} cuerpo={TITULO_SB} />
        <Subtitulo a={SBT.t1b + 16} b={T2} blanca="te puede ahorrar" roja="más de un peso." />
        <Subtitulo a={T2 + 3} b={SBC.cer} blanca="Variedad de productos" roja="a precios de oferta." />
        <Subtitulo a={T3 + 3} b={T3b} blanca="Stock disponible" roja="para llevar de inmediato." />
        <Subtitulo a={T3b + 3} b={T4} blanca="Nuevas oportunidades que" roja="se renuevan cada semana." />
        {/* sin texto sobre Seba (R-20): el subtítulo entra con la fachada */}
        <Subtitulo a={T4b + 3} b={CIE} blanca="Ven a descubrir la" roja="Zona Ofertas Constructor" />
      </Sequence>
      <Sequence from={CIE}>
        <CierreSB />
        <Cortina />
      </Sequence>
      <Sonido total={SB_DUR} voces={[{src: "sb_t1.mp3", at: SBT.t1}, {src: "sb_t2.mp3", at: T2}, {src: "sb_t3.mp3", at: T3}, {src: "sb_t4.mp3", at: T4}]} />
    </AbsoluteFill>
  );
};
