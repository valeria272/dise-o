/**
 * MÁS CENTER · reel de paid media — v3 (04-09-2026).
 *
 * Gramática del cliente (medida sobre r-performance-agosto.mp4): logo blanco arriba (tinta 211 px, y=118),
 * titular en versales Montserrat Bold ~90 px alineado a x=110 en el tercio inferior, pastilla roja #DC1914
 * (627 px, radio 48) con ícono en círculo blanco montado en su borde superior, cierre en rojo pleno con el
 * logo grande (tinta 405 px) y una línea Montserrat Medium ~50 px, pista musical de ~81 BPM.
 *
 * MONTAJE (feedback de Valeria, 04-09): nada «llega y aparece». Los planos se funden entre sí con un
 * zoom lento continuo; los textos entran palabra a palabra con fundido y desplazamiento suave y salen
 * con fundido; la pastilla entra con un resorte sin rebote duro; el cierre funde a rojo. La v2 copiaba
 * el tipeo letra a letra y el golpe de rojo pleno del reel de agosto y se sentía brusca.
 *
 * TIPOGRAFÍA: Montserrat variable auto-hospedada, sin delayRender (memoria reel-video-gotchas). El manual
 * 2023 dice Poppins; las piezas aprobadas y los reels del cliente están en Montserrat (medido 04-09-2026).
 * Textos VERBATIM del brief de octubre 2026. Se entrega en 1080×1920 y en 1080×1080.
 */
import React from "react";
import {AbsoluteFill, Audio, Easing, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";

export const ROJO = "#DC1914";
const LOGO_TINTA = 0.856; // tinta / ancho del SVG
const LOGO_DX = 0.019;    // el centro de la tinta está 1,9 % a la derecha del centro del SVG

let fontsInjected = false;
const ensureMontserrat = () => {
  if (fontsInjected || typeof document === "undefined") return;
  fontsInjected = true;
  const style = document.createElement("style");
  style.textContent = `@font-face{font-family:'Montserrat';font-weight:100 900;font-display:block;src:url(${staticFile("assets/fonts/Montserrat.ttf")}) format('truetype')}`;
  document.head.appendChild(style);
  const f = (document as any).fonts;
  if (f?.load) [500, 700].forEach((w) => f.load(`${w} 100px Montserrat`).catch(() => undefined));
};
ensureMontserrat();

export type Escena = {clip: string; texto: string; tipo: "titular" | "pastilla"; icono?: "oferta" | "evento" | "comunidad"; desde?: number; dur: number; posCuadrado?: string};
export type ReelProps = {escenas: Escena[]; cierre: string};

// ── ritmo del montaje (frames a 30 fps) ──────────────────────────────────────
export const FUNDIDO = 20;      // fundido cruzado entre planos (0,67 s)
const ENTRA_TEXTO = 8;          // el texto entra cuando el plano ya se asentó
const SALE_TEXTO = 14;          // frames que dura la salida del texto
const suave = Easing.out(Easing.cubic);

// ── métricas por formato (px) ─────────────────────────────────────────────────
const metricas = (w: number, h: number) =>
  h > w
    ? {logoW: 245, logoTop: 107, titSize: 90, titLh: 98, titLeft: 110, titBottom: 314, pillW: 627, pillTop: 470, pillSize: 46, pillLh: 60, pillPadTop: 74, pillPadBottom: 44, pillRadio: 48, icono: 130, cierreLogoW: 405, cierreLogoTop: 840, cierreSize: 57, cierreLh: 59, cierreTop: 1310, cierreMaxW: 690}
    : {logoW: 200, logoTop: 46, titSize: 60, titLh: 66, titLeft: 80, titBottom: 150, pillW: 560, pillTop: 250, pillSize: 38, pillLh: 48, pillPadTop: 60, pillPadBottom: 34, pillRadio: 40, icono: 104, cierreLogoW: 300, cierreLogoTop: 430, cierreSize: 40, cierreLh: 44, cierreTop: 700, cierreMaxW: 640};

const Logo: React.FC<{w: number; top: number; style?: React.CSSProperties}> = ({w, top, style}) => {
  const css = w / LOGO_TINTA;
  return <Img src={staticFile("assets/mascenter/logo-blanco.svg")} style={{position: "absolute", left: `calc(50% - ${css / 2 + css * LOGO_DX}px)`, top: top - css * 0.04, width: css, ...style}} />;
};

/** Texto que entra palabra a palabra (fundido + desplazamiento suave) y sale con un fundido. */
const Palabras: React.FC<{texto: string; frame: number; dur: number; paso?: number; salida?: boolean}> = ({texto, frame, dur, paso = 3, salida = true}) => {
  const palabras = texto.split(" ");
  const out = salida ? interpolate(frame, [dur - SALE_TEXTO, dur], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.in(Easing.quad)}) : 1;
  const outY = salida ? interpolate(frame, [dur - SALE_TEXTO, dur], [0, -18], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.in(Easing.quad)}) : 0;
  return (
    <span style={{display: "inline", opacity: out, transform: `translateY(${outY}px)`, willChange: "opacity, transform"}}>
      {palabras.map((p, i) => {
        const f = frame - i * paso;
        const o = interpolate(f, [0, 14], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: suave});
        const y = interpolate(f, [0, 16], [26, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: suave});
        return (
          <span key={i} style={{display: "inline-block", opacity: o, transform: `translateY(${y}px)`, marginRight: "0.28em"}}>{p}</span>
        );
      })}
    </span>
  );
};

const Icono: React.FC<{tipo: Escena["icono"]; size: number}> = ({tipo, size}) => {
  const g = ROJO; const s = size * 0.5;
  const glifo =
    tipo === "oferta" ? <svg width={s} height={s} viewBox="0 0 24 24"><path fill={g} d="M21.4 11.6 12.4 2.6A2 2 0 0 0 11 2H4a2 2 0 0 0-2 2v7c0 .5.2 1 .6 1.4l9 9a2 2 0 0 0 2.8 0l7-7a2 2 0 0 0 0-2.8ZM7 9a2 2 0 1 1 0-4 2 2 0 0 1 0 4Z"/></svg>
    : tipo === "evento" ? <svg width={s} height={s} viewBox="0 0 24 24"><path fill={g} d="M7 2h2v2h6V2h2v2h3a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3V2Zm-2 8v10h14V10H5Zm7 1.2 1.3 2.6 2.9.4-2.1 2 .5 2.8-2.6-1.4-2.6 1.4.5-2.8-2.1-2 2.9-.4L12 11.2Z"/></svg>
    : <svg width={s} height={s} viewBox="0 0 24 24"><path fill={g} d="M12 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6Zm-6 1a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Zm12 0a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5ZM12 13c-2.7 0-6 1.3-6 3.5V19h12v-2.5c0-2.2-3.3-3.5-6-3.5Zm-7.5 1C2.6 14 1 15 1 16.5V19h3.5v-2.5c0-1 .4-1.9 1.2-2.6L4.5 14Zm15 0-1.2-.1c.8.7 1.2 1.6 1.2 2.6V19H23v-2.5C23 15 21.4 14 19.5 14Z"/></svg>;
  return <div style={{width: size, height: size, borderRadius: "50%", background: "#fff", display: "flex", alignItems: "center", justifyContent: "center", boxShadow: "0 2px 6px rgba(0,0,0,.15)"}}>{glifo}</div>;
};

/** Un plano: clip con zoom lento continuo, que entra fundiéndose sobre el anterior. */
const Plano: React.FC<{e: Escena; w: number; h: number; dur: number; fundeEntrada: boolean}> = ({e, w, h, dur, fundeEntrada}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const m = metricas(w, h);
  const opacidad = fundeEntrada ? interpolate(frame, [0, FUNDIDO], [0, 1], {extrapolateRight: "clamp", easing: Easing.inOut(Easing.quad)}) : 1;
  const zoom = interpolate(frame, [0, dur], [1.0, 1.07], {extrapolateRight: "clamp"});
  // El primer plano abre con el mensaje YA puesto (el brief usa el primer frame como miniatura); los demás lo
  // reciben cuando el fundido terminó.
  const t0 = fundeEntrada ? FUNDIDO + ENTRA_TEXTO : -60;
  const ft = frame - t0;
  const durTexto = dur - t0 - Math.round(FUNDIDO * 0.5);   // el texto se va antes de que el plano se funda
  const pop = spring({fps, frame: ft, config: {damping: 200, stiffness: 90, mass: 1}});   // sin rebote
  return (
    <AbsoluteFill style={{opacity: opacidad}}>
      <AbsoluteFill style={{transform: `scale(${zoom})`, transformOrigin: "50% 55%"}}>
        <OffthreadVideo src={staticFile(`assets/mascenter/clips/${e.clip}`)} startFrom={Math.round((e.desde ?? 0) * fps)} muted style={{width: "100%", height: "100%", objectFit: "cover", objectPosition: h > w ? "50% 50%" : e.posCuadrado ?? "50% 68%"}} />
      </AbsoluteFill>
      {/* velo suave abajo para que el titular blanco lea sobre cualquier plano */}
      {e.tipo === "titular" && <AbsoluteFill style={{background: "linear-gradient(180deg, rgba(0,0,0,0) 55%, rgba(0,0,0,.28) 100%)"}} />}
      {ft >= 0 && (e.tipo === "titular" ? (
        <div style={{position: "absolute", left: m.titLeft, right: 60, bottom: m.titBottom, color: "#fff", fontFamily: "Montserrat", fontWeight: 700, textTransform: "uppercase", fontSize: m.titSize, lineHeight: `${m.titLh}px`, textShadow: "0 2px 16px rgba(0,0,0,.35)"}}>
          <Palabras texto={e.texto} frame={ft} dur={durTexto} paso={3} />
        </div>
      ) : (
        <div style={{position: "absolute", left: (w - m.pillW) / 2, top: m.pillTop, width: m.pillW, opacity: interpolate(ft, [0, 10], [0, 1], {extrapolateRight: "clamp"}) * interpolate(ft, [durTexto - SALE_TEXTO, durTexto], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}), transform: `translateY(${(1 - pop) * 40}px) scale(${0.94 + pop * 0.06})`, transformOrigin: "50% 0%"}}>
          <div style={{position: "absolute", left: (m.pillW - m.icono) / 2, top: -m.icono * 0.5, opacity: interpolate(ft, [6, 18], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}), transform: `scale(${interpolate(ft, [6, 22], [0.7, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: suave})})`}}><Icono tipo={e.icono ?? "comunidad"} size={m.icono} /></div>
          <div style={{background: ROJO, borderRadius: m.pillRadio, padding: `${m.pillPadTop}px 40px ${m.pillPadBottom}px`, color: "#fff", fontFamily: "Montserrat", fontWeight: 500, fontSize: m.pillSize, lineHeight: `${m.pillLh}px`, textAlign: "center", minHeight: m.pillPadTop + m.pillPadBottom + m.pillLh * 2}}>
            <Palabras texto={e.texto} frame={ft - 8} dur={durTexto - 8} paso={2} salida={false} />
          </div>
        </div>
      ))}
    </AbsoluteFill>
  );
};

/** CIERRE — réplica del cierre del reel de agosto del cliente (editables de paid), medido a 60 fps:
 *  panel rojo que entra desde la izquierda en 0,25 s · el logo baja desde arriba y se asienta en 0,23 s
 *  (tinta 405 px, borde superior en y=840) · 0,1 s después el texto se escribe a ~80 caracteres/s en
 *  Montserrat Regular ~57 px, centrado en una caja de 665 px · se queda hasta el final, sin fundido. */
export const CIERRE_F = 93;         // 3,1 s, como el del cliente
const WIPE_F = 7;                   // 0,25 s
const Cierre: React.FC<{texto: string; w: number; h: number}> = ({texto, w, h}) => {
  const frame = useCurrentFrame();
  const m = metricas(w, h);
  const wipe = interpolate(frame, [0, WIPE_F], [-100, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.quad)});
  const logoY = interpolate(frame - 3, [0, 8], [-220 * (h / 1920), 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  const chars = Math.max(0, Math.round((frame - 14) * 2.7));   // 80 caracteres por segundo a 30 fps
  return (
    <AbsoluteFill style={{background: ROJO, transform: `translateX(${wipe}%)`}}>
      <Logo w={m.cierreLogoW} top={m.cierreLogoTop} style={{transform: `translateY(${logoY}px)`}} />
      <div style={{position: "absolute", left: (w - m.cierreMaxW) / 2, width: m.cierreMaxW, top: m.cierreTop, color: "#fff", fontFamily: "Montserrat", fontWeight: 400, fontSize: m.cierreSize, lineHeight: `${m.cierreLh}px`, textAlign: "center"}}>
        {texto.slice(0, chars)}
      </div>
    </AbsoluteFill>
  );
};

const Musica: React.FC<{total: number}> = ({total}) => {
  const frame = useCurrentFrame();
  const vol = interpolate(frame, [0, 10, total - 45, total], [0, 1, 1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return <Audio src={staticFile("assets/mascenter/pista-mascenter.m4a")} volume={vol} />;
};

/** Duración total: la suma de los planos menos los solapes de los fundidos, más el cierre. */
export const duracionReel = (p: ReelProps, fps: number) => p.escenas.reduce((a, e) => a + Math.round(e.dur * fps), 0) - (p.escenas.length - 1) * FUNDIDO + CIERRE_F;

export const MasCenterReel: React.FC<ReelProps> = ({escenas, cierre}) => {
  ensureMontserrat();
  const {fps, width: w, height: h} = useVideoConfig();
  const frame = useCurrentFrame();
  const seqs: React.ReactNode[] = [];
  let t = 0;
  escenas.forEach((e, i) => {
    const d = Math.round(e.dur * fps);
    const from = i === 0 ? 0 : t - FUNDIDO;                // cada plano entra FUNDIDO frames antes de que termine el anterior
    // el último plano sigue vivo mientras el panel rojo del cierre lo tapa (si no, queda un hueco negro)
    const extra = i === escenas.length - 1 ? WIPE_F : 0;
    seqs.push(<Sequence key={`e${i}`} from={from} durationInFrames={d + extra}><Plano e={e} w={w} h={h} dur={d} fundeEntrada={i > 0} /></Sequence>);
    t = from + d;
  });
  const inicioCierre = t;   // el panel rojo del cierre tapa el último plano: barrido, como el cliente
  seqs.push(<Sequence key="cierre" from={inicioCierre} durationInFrames={CIERRE_F}><Cierre texto={cierre} w={w} h={h} /></Sequence>);
  const total = inicioCierre + CIERRE_F;
  const m = metricas(w, h);
  // presente desde el frame 0 (miniatura) y se apaga cuando pasa el barrido del cierre
  const logoOp = interpolate(frame, [inicioCierre, inicioCierre + WIPE_F], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{background: "#000"}}>
      {seqs}
      <Logo w={m.logoW} top={m.logoTop} style={{opacity: logoOp}} />
      <Musica total={total} />
    </AbsoluteFill>
  );
};

// ── contenido de octubre 2026 — VERBATIM del brief ────────────────────────────
export const REEL_02: ReelProps = {
  escenas: [
    {clip: "chamisero.mp4", texto: "¿Sabías que en Más Center siempre hay algo nuevo?", tipo: "titular", dur: 4.2},
    {clip: "padrehurtado.mp4", texto: "Ofertas, estrenos y eventos de tus locales favoritos", tipo: "pastilla", icono: "oferta", dur: 4.8},
    {clip: "copiapo.mp4", texto: "Todo cerca, todo en comunidad", tipo: "titular", dur: 4.2},
  ],
  cierre: "Síguenos y no te pierdas nada",
};
export const REEL_03: ReelProps = {
  escenas: [
    // coyhaique.mp4 se descartó: la IA hace vibrar las letras del local (2º orden 8,4 en la franja quieta de arriba; los demás clips ≤ 2). Valeria lo vio: «tintinea».
    {clip: "padrehurtado.mp4", texto: "Aquí pasan cosas todos los días", tipo: "titular", desde: 0.4, dur: 4.2},
    {clip: "osorno.mp4", texto: "Desde promociones hasta eventos únicos de nuestros locatarios", tipo: "pastilla", icono: "evento", dur: 4.8},
    {clip: "chamisero.mp4", texto: "La comunidad que se arma en tu Más Center", tipo: "titular", desde: 0.8, dur: 4.2},
  ],
  cierre: "Sé parte, síguenos en Instagram",
};
