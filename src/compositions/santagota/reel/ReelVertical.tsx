/**
 * SANTA GOTA · «UNA SOLA GOTA LO CAMBIA TODO» — versión VERTICAL para Reels (1080×1920 · 24 fps · 477 cuadros).
 *
 * 28-09-2026 · Diego. Fuente de verdad: el spot horizontal de Diego en D:\DIEGO 2023\COPYWRITERS\SANTA GOTA\
 *   base-santagota.prproj → base-santagota.mp4     montaje limpio (Seedream 5 Pro → Wan 3.0, space de Magnific)
 *   FINAL SANTA GOTA.aep  → final-santagota v2.mp4  el mismo montaje + textos, logo, transiciones y mezcla final
 *
 * v2 (pedido de Diego sobre la v1):
 *  · Los planos que en 9:16 cortaban la botella o la escena se REGENERARON verticales, desde la misma imagen del space:
 *    recorte que contiene toda la acción → franjas arriba/abajo completadas con Seedream 5 Pro (y los píxeles originales
 *    vueltos a pegar al centro) → Wan 3.0 9:16 con el MISMO prompt del nodo. Monja con cuadro inicial y final (escena
 *    completa: cocina, wok, fuego y la botella en la mano), wok y filete con cuadro inicial.
 *  · El split usa los dos clips fuente enteros (sartén | ensalada) apilados, con las botellas completas.
 *  · Transiciones calcadas cuadro a cuadro del v2: destello de luz 28–35, salida del titular con estela 94–99, giro con
 *    desenfoque rotacional 131–139, zoom a través de la O del logo 202–207, giro de salida 377–384.
 *  · Cierre sin choques: logo arriba (sale desde detrás de los productos), productos al medio, CTA abajo, con aire.
 * Zonas seguras de Reels: nada de texto sobre y < 250 ni bajo y > 1580.
 */
import React from "react";
import {AbsoluteFill, Audio, Easing, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";

export const DUR_REEL_V = 477;
const DIR = "assets/santagota/reel-v2";
const V = (f: string) => staticFile(`${DIR}/${f}`);
const LIMA = "rgb(193,212,0)";
const S = 1920 / 1080;

let fuentes = false;
const cargarFuentes = () => {
  if (fuentes || typeof document === "undefined") return;
  fuentes = true;
  const st = document.createElement("style");
  st.textContent = `
    @font-face{font-family:'Dimbo';src:url(${V("Dimbo Regular.ttf")}) format('truetype');font-display:block}
    @font-face{font-family:'Queen Marker';src:url(${V("The Queen Marker.ttf")}) format('truetype');font-display:block}`;
  document.head.appendChild(st);
  const f = (document as unknown as {fonts?: {load: (s: string) => Promise<unknown>}}).fonts;
  if (f) ["100px Dimbo", "100px 'Queen Marker'"].forEach((s) => f.load(s).catch(() => {}));
};
cargarFuentes();

const cl = {extrapolateLeft: "clamp", extrapolateRight: "clamp"} as const;
/** Interpolación por cuadros clave medidos en el v2. */
const kf = (f: number, fr: number[], v: number[]) => interpolate(f, fr, v, cl);

/* ───────────────────────── imagen ───────────────────────── */

/** Placa del montaje base, a toda la altura, recortada alrededor de `cx` (px de la placa 1920). */
const Base: React.FC<{cx: number}> = ({cx}) => (
  <OffthreadVideo src={V("base.mp4")} muted style={{position: "absolute", top: 0, height: 1920, width: 1920 * S, left: 540 - cx * S}} />
);

/** Clip vertical regenerado (1080×1920), desde el cuadro `desde` de la composición, saltando `salto` cuadros. */
const Vertical: React.FC<{src: string; desde: number; hasta: number; salto?: number}> = ({src, desde, hasta, salto = 0}) => (
  <Sequence from={desde} durationInFrames={hasta - desde} layout="none">
    <OffthreadVideo src={V(src)} muted startFrom={salto} style={{position: "absolute", inset: 0, width: 1080, height: 1920, objectFit: "cover"}} />
  </Sequence>
);

/** Mitad del split: zona 1215×1080 del clip fuente (desde x0) llevada a 1080×960. */
const Mitad: React.FC<{src: string; x0: number; top: number}> = ({src, x0, top}) => {
  const k = 1080 / 1215;
  return (
    <div style={{position: "absolute", left: 0, top, width: 1080, height: 960, overflow: "hidden"}}>
      <OffthreadVideo src={V(src)} muted startFrom={8} style={{position: "absolute", width: 1920 * k, height: 1080 * k, left: -x0 * k, top: 0}} />
    </div>
  );
};

/** Cierre: productos a 1,05× con la tapa más alta en y≈660, sobre el verde del set extendido. */
const K_CIERRE = 1.05;
const TOP_CIERRE = 660 - 268 * K_CIERRE; // 268 = tapa más alta en la placa
const Cierre: React.FC = () => (
  <AbsoluteFill style={{background: "linear-gradient(180deg, rgb(108,118,75) 0%, rgb(111,121,77) 30%, rgb(128,139,82) 72%, rgb(134,144,90) 100%)"}}>
    <Sequence from={384} layout="none">
      <OffthreadVideo
        src={V("base.mp4")}
        muted
        startFrom={384}
        style={{
          position: "absolute",
          width: 1920 * K_CIERRE,
          height: 1080 * K_CIERRE,
          left: 540 - 990 * K_CIERRE,
          top: TOP_CIERRE,
          WebkitMaskImage: "linear-gradient(180deg, transparent 0%, #000 12%, #000 90%, transparent 100%)",
          maskImage: "linear-gradient(180deg, transparent 0%, #000 12%, #000 90%, transparent 100%)",
        }}
      />
    </Sequence>
  </AbsoluteFill>
);

/** Lo que se ve en el cuadro f. Todo lo que gira con la imagen (logo del plato, «SOMOS…») va acá. */
const Imagen: React.FC<{f: number}> = ({f}) => {
  let capa: React.ReactNode = null;
  if (f < 33) capa = <Base cx={960} />;
  else if (f < 65) capa = <Vertical src="wok_v.mp4" desde={33} hasta={65} salto={16} />;
  else if (f < 136) capa = <Vertical src="monja_a.mp4" desde={65} hasta={136} />;
  else if (f < 170) capa = <Base cx={1000} />;
  else if (f < 202) capa = <Base cx={960} />;
  else if (f < 241) capa = <Base cx={850} />;
  else if (f < 271) capa = <Base cx={990} />;
  else if (f < 302) capa = <Vertical src="filete_v.mp4" desde={271} hasta={302} salto={10} />;
  else if (f < 336)
    capa = (
      <Sequence from={302} durationInFrames={34} layout="none">
        <Mitad src="split_sarten.mp4" x0={150} top={0} />
        <Mitad src="split_ensalada.mp4" x0={185} top={960} />
      </Sequence>
    );
  else if (f < 348) capa = <Base cx={930} />;
  else if (f < 372) capa = <Base cx={1080} />;
  else if (f < 384) capa = <Base cx={1100} />;
  else capa = <Cierre />;
  return (
    <AbsoluteFill style={{backgroundColor: "#000", overflow: "hidden"}}>
      {capa}
      {f >= 136 && f < 202 && <LogoPlato f={f} />}
      {f >= 300 && f < 384 && <Somos f={f} />}
    </AbsoluteFill>
  );
};

/* ───────────────────────── transiciones (medidas en el v2) ───────────────────────── */

/** Escala para cubrir el cuadro vertical girado θ grados sin esquinas negras. */
const cubre = (deg: number) => {
  const r = (Math.abs(deg) * Math.PI) / 180;
  return Math.abs(Math.cos(r)) + (1920 / 1080) * Math.abs(Math.sin(r));
};

/** Muestras de obturador: N copias de la imagen con la transformación repartida, promediadas (opacidad 1/(i+1)). */
const Obturador: React.FC<{f: number; n: number; blur?: number; tr: (t: number) => string}> = ({f, n, blur = 0, tr}) => (
  <AbsoluteFill style={{backgroundColor: "#000", filter: blur > 0.3 ? `blur(${blur}px)` : undefined}}>
    {Array.from({length: n}, (_, i) => {
      const t = n === 1 ? 0.5 : i / (n - 1);
      return (
        <AbsoluteFill key={i} style={{transform: tr(t), opacity: 1 / (i + 1)}}>
          <Imagen f={f} />
        </AbsoluteFill>
      );
    })}
  </AbsoluteFill>
);

/** Giro monja → tomates (131–139): horario, cruza el corte en 136. Ángulo y barrido por cuadro, leídos del v2. */
const GIRO_A = {fr: [131, 132, 133, 134, 135, 136, 137, 138, 139], ang: [0, 4, 18, 55, 110, -70, -20, -4, 0], ancho: [0, 3, 10, 26, 40, 34, 14, 4, 0]};
/** Giro de salida ceviche → cierre (377–384): antihorario con zoom. */
const GIRO_B = {fr: [377, 378, 379, 380, 381, 382, 383], ang: [0, -3, -8, -16, -28, -45, -65], ancho: [0, 1, 3, 5, 8, 12, 16], zoom: [1, 1.03, 1.08, 1.16, 1.3, 1.5, 1.8]};

const Escena: React.FC = () => {
  const f = useCurrentFrame();
  if (f > 131 && f < 139) {
    const i = GIRO_A.fr.indexOf(f);
    const a = GIRO_A.ang[i];
    const w = GIRO_A.ancho[i];
    return <Obturador f={f} n={10} blur={w / 8} tr={(t) => { const d = a + (t - 0.5) * w; return `rotate(${d}deg) scale(${cubre(d) * 1.02})`; }} />;
  }
  if (f >= 202 && f < 207) {
    // la mesa entra con zoom radial mientras la cámara atraviesa la O del logo
    const z = kf(f, [202, 203, 204, 205, 206, 207], [1.35, 1.25, 1.15, 1.08, 1.03, 1]);
    const w = kf(f, [202, 203, 204, 205, 206, 207], [0.25, 0.3, 0.35, 0.3, 0.15, 0]);
    return <Obturador f={f} n={8} blur={w * 6} tr={(t) => `scale(${z * (1 + t * w)})`} />;
  }
  if (f > 377 && f < 384) {
    const i = GIRO_B.fr.indexOf(f);
    const a = GIRO_B.ang[i];
    const w = GIRO_B.ancho[i];
    const z = GIRO_B.zoom[i];
    return <Obturador f={f} n={10} blur={w / 8} tr={(t) => { const d = a + (t - 0.5) * w; return `rotate(${d}deg) scale(${Math.max(z, cubre(d) * 1.02)})`; }} />;
  }
  return <Imagen f={f} />;
};

/** Destello de luz gota → wok (28–34): color y opacidad por cuadro, leídos del v2. */
const DESTELLO: Record<number, {bg: string; op: number; blend: React.CSSProperties["mixBlendMode"]}> = {
  28: {bg: "radial-gradient(ellipse 70% 60% at 100% 55%, rgba(255,130,30,1), rgba(255,90,20,0) 70%)", op: 0.85, blend: "screen"},
  29: {bg: "linear-gradient(100deg, rgba(0,0,0,0) 0%, rgba(210,70,30,1) 45%, rgba(255,150,40,1) 100%)", op: 0.8, blend: "screen"},
  30: {bg: "linear-gradient(120deg, #7B2FD0 0%, #B43BD8 50%, #E86BC8 100%)", op: 0.82, blend: "normal"},
  31: {bg: "linear-gradient(135deg, #F2A294 0%, #F4B8A0 45%, #F8DDB2 100%)", op: 0.8, blend: "normal"},
  32: {bg: "linear-gradient(135deg, #F09E92 0%, #F4B8A0 40%, #F9E3B8 100%)", op: 1, blend: "normal"},
  33: {bg: "linear-gradient(135deg, #F09E92 0%, #F4B8A0 40%, #F9E3B8 100%)", op: 0.42, blend: "screen"},
  34: {bg: "radial-gradient(ellipse 45% 70% at 0% 45%, rgba(230,110,50,1), rgba(230,110,50,0) 75%)", op: 0.35, blend: "screen"},
};
const Destello: React.FC = () => {
  const c = DESTELLO[useCurrentFrame()];
  if (!c) return null;
  return <AbsoluteFill style={{background: c.bg, opacity: c.op, mixBlendMode: c.blend}} />;
};

/* ───────────────────────── gráfica ───────────────────────── */

const dimbo: React.CSSProperties = {fontFamily: "Dimbo", color: "#fff", lineHeight: 0.92, whiteSpace: "nowrap", textTransform: "uppercase", textShadow: "0 6px 24px rgba(0,0,0,0.45)"};
const marker: React.CSSProperties = {fontFamily: "'Queen Marker'", color: LIMA, lineHeight: 1, whiteSpace: "nowrap", textTransform: "uppercase", textShadow: "0 6px 24px rgba(0,0,0,0.35)"};

/** Letra a letra con fundido y desenfoque («una sola gota»). */
const Suave: React.FC<{f: number; texto: string; desde: number; paso: number; style: React.CSSProperties}> = ({f, texto, desde, paso, style}) => (
  <span style={style}>
    {texto.split("").map((c, i) => {
      const k = kf(f, [desde + i * paso, desde + i * paso + 3], [0, 1]);
      return <span key={i} style={{opacity: k, filter: `blur(${(1 - k) * 8}px)`, display: "inline-block", whiteSpace: "pre"}}>{c}</span>;
    })}
  </span>
);

/** Letra a letra que cae girando desde arriba a la derecha, grande y desenfocada (LO CAMBIA / SOMOS / DEL ACEITE…). */
const Vuelo: React.FC<{f: number; texto: string; desde: number; paso: number; style: React.CSSProperties}> = ({f, texto, desde, paso, style}) => (
  <span style={{...style, display: "inline-block"}}>
    {texto.split("").map((c, i) => {
      const k = interpolate(f, [desde + i * paso, desde + i * paso + 5], [0, 1], {...cl, easing: Easing.out(Easing.cubic)});
      return (
        <span
          key={i}
          style={{
            display: "inline-block",
            whiteSpace: "pre",
            opacity: k > 0 ? Math.min(1, k * 2) : 0,
            transform: `translate(${(1 - k) * 150}px, ${(1 - k) * -170}px) rotate(${(1 - k) * -65}deg) scale(${1 + (1 - k) * 0.9})`,
            filter: `blur(${(1 - k) * 9}px)`,
          }}
        >
          {c}
        </span>
      );
    })}
  </span>
);

/** Trazo de plumón: se descubre de izquierda a derecha. */
const Trazo: React.FC<{f: number; desde: number; dur: number; children: React.ReactNode; style?: React.CSSProperties}> = ({f, desde, dur, children, style}) => {
  const p = interpolate(f, [desde, desde + dur], [0, 100], {...cl, easing: Easing.out(Easing.quad)});
  return <div style={{...style, clipPath: `inset(-20% ${100 - p}% -20% -5%)`}}>{children}</div>;
};

const UnaSolaGota: React.FC = () => {
  const f = useCurrentFrame();
  if (f >= 33) return null;
  return (
    <AbsoluteFill style={{alignItems: "center", justifyContent: "center"}}>
      <div style={{marginTop: 40}}>
        <Suave f={f} texto="una sola gota" desde={1} paso={0.72} style={{...marker, color: "#fff", fontSize: 150, textTransform: "none"}} />
      </div>
    </AbsoluteFill>
  );
};

/** «LO CAMBIA / TODO» en la zona oscura de la cocina, bajo la sartén (arriba tapa la cara de la monja); sale a la izquierda con estela 94–99. */
const LoCambiaTodo: React.FC = () => {
  const f = useCurrentFrame();
  if (f < 34 || f > 99) return null;
  const dx = kf(f, [94, 95, 96, 97, 98, 99], [0, -10, -120, -420, -800, -1300]);
  const est = kf(f, [94, 95, 96, 97, 98, 99], [0, 20, 60, 160, 260, 300]);
  const bloque = (
    <div style={{position: "absolute", left: 0, right: 0, top: 1240, display: "flex", flexDirection: "column", alignItems: "center"}}>
      <div>
        <Vuelo f={f} texto="LO " desde={35} paso={1} style={{...dimbo, fontSize: 176}} />
        <Vuelo f={f} texto="CAMBIA" desde={37} paso={1} style={{...dimbo, fontSize: 176}} />
      </div>
      <Trazo f={f} desde={42} dur={7} style={{marginTop: -34}}>
        <span style={{...marker, fontSize: 300, display: "inline-block", transform: "rotate(-3deg)"}}>todo</span>
      </Trazo>
    </div>
  );
  const n = est > 0 ? 6 : 1;
  return (
    <AbsoluteFill>
      {Array.from({length: n}, (_, i) => (
        <AbsoluteFill key={i} style={{transform: `translateX(${dx + (n === 1 ? 0 : (i / (n - 1) - 0.5) * est)}px)`, opacity: 1 / (i + 1)}}>
          {bloque}
        </AbsoluteFill>
      ))}
    </AbsoluteFill>
  );
};

/** Logo sobre tomate (lima) y pizza (naranja), vectores del manual «BM SANTA GOTA.pdf» (págs. 4 y 5). Entra con la imagen en el giro; en 202–205 la cámara lo atraviesa por la O. */
const O_X = 0.423; // centro del hueco de la O en logo-bm-*.png (medido)
const O_Y = 0.704;
const LOGO_R = 1519 / 2474; // alto/ancho del logo del manual
const LOGO_W = 900;
const LogoPlato: React.FC<{f: number}> = ({f}) => {
  const src = f < 170 ? "logo-bm-lima.png" : "logo-bm-naranja.png";
  const esc = kf(f, [201, 202, 203, 204, 205], [1, 1.05, 1.9, 5.5, 18]);
  const op = kf(f, [204, 205], [1, 0]);
  const h = LOGO_W * LOGO_R;
  return (
    <img
      src={V(src)}
      style={{
        position: "absolute",
        width: LOGO_W,
        left: 540 - LOGO_W / 2,
        top: 960 - h / 2,
        opacity: op,
        transformOrigin: `${O_X * 100}% ${O_Y * 100}%`,
        transform: `scale(${esc})`,
        filter: `drop-shadow(0 12px 30px rgba(0,0,0,0.35)) blur(${kf(f, [202, 203, 204], [0, 3, 8])}px)`,
      }}
    />
  );
};

/** 202–205: el logo naranja sigue sobre la mesa y la cámara lo atraviesa por la O (capa propia, con estela radial). */
const LogoZoom: React.FC = () => {
  const f = useCurrentFrame();
  if (f < 202 || f > 204) return null;
  const w = kf(f, [202, 203, 204], [0.1, 0.35, 0.8]);
  return (
    <AbsoluteFill>
      {Array.from({length: 6}, (_, i) => (
        <AbsoluteFill key={i} style={{opacity: 1 / (i + 1), transform: `scale(${1 + (i / 5) * w})`, transformOrigin: `${540 - LOGO_W / 2 + O_X * LOGO_W}px ${960 - (LOGO_W * LOGO_R) / 2 + O_Y * LOGO_W * LOGO_R}px`}}>
          <LogoPlato f={f} />
        </AbsoluteFill>
      ))}
    </AbsoluteFill>
  );
};

/** «SOMOS / LA REVOLUCIÓN / DEL ACEITE DE OLIVA» — gira con la imagen en la salida. */
const Somos: React.FC<{f: number}> = ({f}) => (
  <div style={{position: "absolute", left: 60, right: 60, top: 790, height: 400}}>
    <div style={{position: "absolute", left: 20, top: 0}}>
      <Vuelo f={f} texto="SOMOS" desde={307} paso={1.3} style={{...dimbo, fontSize: 150}} />
    </div>
    <Trazo f={f} desde={314} dur={8} style={{position: "absolute", left: -10, top: 112}}>
      <span style={{...marker, fontSize: 150, display: "inline-block", transform: "rotate(-3deg)"}}>la revolución</span>
    </Trazo>
    <div style={{position: "absolute", right: 0, top: 262}}>
      <Vuelo f={f} texto="DEL ACEITE DE OLIVA" desde={306} paso={0.55} style={{...dimbo, fontSize: 108}} />
    </div>
  </div>
);

/** Cierre: el logo sube desde detrás de los productos; CTA entra desde la derecha con estela; barra lima barre; URL se teclea. */
const LOGO_C_W = 560;
const LOGO_C_TOP = 262;
const LINEA_TAPAS = 648; // justo sobre la tapa más alta: el logo se recorta ahí y parece salir desde detrás
const CierreGrafica: React.FC = () => {
  const f = useCurrentFrame();
  const {fps} = useVideoConfig();
  if (f < 400) return null;
  const sube = spring({frame: f - 404, fps, config: {damping: 14, stiffness: 110}});
  const dy = (1 - sube) * (LINEA_TAPAS - LOGO_C_TOP + 20);
  const entra = (desde: number): React.CSSProperties => {
    const k = interpolate(f, [desde, desde + 3], [0, 1], {...cl, easing: Easing.out(Easing.cubic)});
    return {transform: `translateX(${(1 - k) * 700}px)`, opacity: k > 0 ? 1 : 0, filter: `blur(${(1 - k) * 10}px)`, display: "inline-block"};
  };
  const barra = kf(f, [419, 425], [0, 1]);
  const url = "SANTAGOTA.CL";
  const n = Math.max(0, Math.floor(f - 427));
  return (
    <AbsoluteFill>
      <div style={{position: "absolute", left: 0, right: 0, top: 0, height: LINEA_TAPAS, overflow: "hidden"}}>
        <img src={V("logo-cierre.png")} style={{position: "absolute", width: LOGO_C_W, left: 540 - LOGO_C_W / 2, top: LOGO_C_TOP, transform: `translateY(${dy}px)`, filter: "drop-shadow(0 10px 24px rgba(0,0,0,0.25))"}} />
      </div>
      <div style={{position: "absolute", left: 0, right: 0, top: 1420, display: "flex", flexDirection: "column", alignItems: "center"}}>
        <div style={{...dimbo, fontSize: 70, textShadow: "none", display: "flex", gap: 18}}>
          <span style={entra(416)}>CÓMPRALO</span>
          <span style={entra(418)}>EN TODO</span>
          <span style={entra(421)}>CHILE</span>
        </div>
        <div style={{marginTop: 12, height: 78, background: LIMA, padding: "0 28px", display: "flex", alignItems: "center", clipPath: `inset(0 0 0 ${(1 - barra) * 100}%)`}}>
          <span style={{...marker, color: "#0E1C03", fontSize: 64, textShadow: "none"}}>
            {url.split("").map((c, i) => <span key={i} style={{opacity: i < n ? 1 : 0}}>{c}</span>)}
          </span>
        </div>
      </div>
    </AbsoluteFill>
  );
};

export const ReelVertical: React.FC = () => {
  cargarFuentes();
  return (
    <AbsoluteFill style={{backgroundColor: "#000"}}>
      <Escena />
      <UnaSolaGota />
      <Destello />
      <LogoZoom />
      <LoCambiaTodo />
      <CierreGrafica />
      <Audio src={V("audio-v2.wav")} />
    </AbsoluteFill>
  );
};
