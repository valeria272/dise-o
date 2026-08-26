import React from "react";
import {AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";

// =============================================================================
// EBEMA CLICK — Reel Septiembre (guion de la grilla, 5 escenas · "mismo formato de agosto")
// 1080×1920 (story) · 1080×1350 (feed) · 30 fps · 21 s (630 frames)
// Esc.1 contratista con celular en obra · Esc.2 pantalla Ebema Click navegando categorías
// Esc.3 productos al carrito + íconos · Esc.4 despacho / retiro · Esc.5 logo Ebema Click
// Logo 2 sobre imagen · logo 1 gris sobre blanco (pantalla) · logo 3 solo sobre rojo (cierre)
// =============================================================================
const RED = "#EC1C23", GREY = "#6D6F72", WHITE = "#FFFFFF", INK = "#111111";
export const EBEMA_CLICK_FPS = 30;
export const EBEMA_CLICK_DURATION = 630;
type Fmt = "story" | "feed";
export type EbemaClickReelProps = {format: Fmt};

let fontsOk = false;
const ensureFonts = () => {
  if (fontsOk || typeof document === "undefined") return;
  fontsOk = true;
  const f = (w: number, file: string) =>
    `@font-face { font-family:'RalewayEB'; font-weight:${w}; font-display:block; src:url(${staticFile(`assets/ebema/fonts/${file}`)}) format('truetype'); }`;
  const css = [f(400, "Raleway-Regular.ttf"), f(600, "Raleway-SemiBold.ttf"), f(700, "Raleway-Bold.ttf"), f(800, "Raleway-ExtraBold.ttf"), f(900, "Raleway-Black.ttf"),
    `@font-face { font-family:'HelvEB'; font-weight:700; font-display:block; src:url(${staticFile("assets/ebema/fonts/Helvetica-Bold.ttf")}) format('truetype'); }`].join("\n");
  const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  const fs = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (fs) ["400", "600", "700", "800", "900"].forEach((w) => fs.load(`${w} 40px RalewayEB`));
};
const RALEWAY = "'RalewayEB', 'Raleway', Arial, sans-serif";
const HELV = "'HelvEB', Helvetica, Arial, sans-serif";

// timeline
const T = {s1: 105, s2: 216, s3: 402, s4: 462, end: 630};
const VO = {a: 6, b: 108, c: 220, d: 405, e: 466};

const useIn = (delay = 0, cfg = {damping: 13, stiffness: 170}) => {
  const frame = useCurrentFrame(); const {fps} = useVideoConfig();
  return spring({fps, frame: frame - delay, config: cfg});
};

const Foto: React.FC<{src: string; zoom?: [number, number]; velo?: number; dur: number; blur?: number; pos?: string}> = ({src, zoom = [1.06, 1.16], velo = 0.4, dur, blur = 0, pos = "center"}) => {
  const frame = useCurrentFrame();
  const z = interpolate(frame, [0, dur], zoom, {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill>
      <Img src={staticFile(src)} style={{width: "100%", height: "100%", objectFit: "cover", objectPosition: pos, transform: `scale(${z})`, filter: blur ? `blur(${blur}px)` : undefined}} />
      <AbsoluteFill style={{background: `rgba(0,0,0,${velo})`}} />
    </AbsoluteFill>
  );
};

const Lockup: React.FC<{fmt: Fmt}> = ({fmt}) => {
  const s = useIn(2);
  return (
    <div style={{position: "absolute", top: fmt === "story" ? 110 : 56, left: "50%", transform: `translateX(-50%) translateY(${interpolate(s, [0, 1], [-40, 0])}px)`, opacity: s, zIndex: 5}}>
      <Img src={staticFile("assets/ebema/logos/logo_click_2_blanco_acento.png")} style={{height: 132}} />
    </div>
  );
};

const Titular: React.FC<{lines: string[]; size: number; delay?: number; out?: number; kicker?: string}> = ({lines, size, delay = 0, out, kicker}) => {
  const frame = useCurrentFrame();
  const box = useIn(delay + 2, {damping: 16, stiffness: 140});
  const exit = out ? interpolate(frame, [out - 10, out], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 1;
  const k = useIn(delay);
  return (
    <div style={{opacity: exit, transform: `scale(${interpolate(exit, [0, 1], [1.05, 1])})`}}>
      {kicker ? <div style={{fontFamily: RALEWAY, fontWeight: 600, fontSize: size * 0.5, color: WHITE, marginBottom: 10, opacity: k, textShadow: "0 1px 6px rgba(0,0,0,.35)"}}>{kicker}</div> : null}
      <div style={{position: "relative", display: "inline-block", padding: "0 26px", lineHeight: 1, fontFamily: RALEWAY, fontWeight: 900, fontSize: size, color: WHITE, textTransform: "uppercase", letterSpacing: 0.3, textShadow: "0 2px 5px rgba(0,0,0,.22)"}}>
        <div style={{position: "absolute", left: 0, right: 0, top: size * 0.5, bottom: -10, background: RED, transformOrigin: "0% 50%", transform: `scaleX(${box})`}} />
        {lines.map((l, i) => {
          const s = useIn(delay + 4 + i * 5, {damping: 12, stiffness: 190});
          return <span key={i} style={{position: "relative", display: "block", whiteSpace: "nowrap", marginTop: i ? 2 : 0, transform: `translateY(${interpolate(s, [0, 1], [40, 0])}px)`, opacity: s}}>{l}</span>;
        })}
      </div>
    </div>
  );
};

export const Boton: React.FC<{text: string; delay?: number; outline?: boolean}> = ({text, delay = 0, outline}) => {
  const s = useIn(delay, {damping: 10, stiffness: 220});
  return <div style={{display: "inline-block", background: RED, color: WHITE, fontFamily: RALEWAY, fontWeight: 700, fontSize: 32, padding: "16px 48px", borderRadius: 10, border: outline ? `3px solid ${WHITE}` : undefined, opacity: s, transform: `scale(${interpolate(s, [0, 1], [0.6, 1])})`}}>{text}</div>;
};

const Centro: React.FC<{top: string; children: React.ReactNode}> = ({top, children}) => (
  <div style={{position: "absolute", left: 0, right: 0, top, transform: "translateY(-50%)", textAlign: "center", padding: "0 70px", zIndex: 4}}>{children}</div>
);

// ---- teléfono con la pantalla de Ebema Click (mock: logo 1 gris sobre blanco) ----
const CATS = ["Cementos", "Pinturas", "Pisos", "Maderas", "Fierros", "PVC", "Techumbre", "Adhesivos"];
const Icono: React.FC<{i: number}> = ({i}) => {
  const st = {stroke: RED, strokeWidth: 5, fill: "none", strokeLinecap: "round" as const, strokeLinejoin: "round" as const};
  const shapes = [
    <path d="M20 70 L50 20 L80 70 Z M35 70 V85 H65 V70" {...st} />,
    <><rect x="30" y="25" width="40" height="50" rx="6" {...st} /><path d="M30 40 H70" {...st} /></>,
    <><rect x="15" y="30" width="70" height="14" rx="3" {...st} /><rect x="15" y="56" width="70" height="14" rx="3" {...st} /></>,
    <><rect x="20" y="20" width="60" height="60" rx="4" {...st} /><path d="M20 40 H80 M20 60 H80" {...st} /></>,
    <path d="M25 75 L75 25 M20 30 L35 45 M55 65 L70 80 M30 20 L45 35 M65 55 L80 70" {...st} />,
    <><circle cx="50" cy="50" r="24" {...st} /><circle cx="50" cy="50" r="12" {...st} /></>,
    <path d="M10 40 L50 15 L90 40 M20 40 V80 H80 V40" {...st} />,
    <><rect x="30" y="20" width="40" height="60" rx="8" {...st} /><path d="M40 80 V90 H60 V80" {...st} /></>,
  ];
  return <svg viewBox="0 0 100 100" width="100%" height="100%">{shapes[i % shapes.length]}</svg>;
};

const Phone: React.FC<{w: number; h: number; children: React.ReactNode; delay?: number}> = ({w, h, children, delay = 0}) => {
  const s = useIn(delay, {damping: 14, stiffness: 120});
  return (
    <div style={{position: "relative", width: w, height: h, margin: "0 auto", borderRadius: 54, background: "#101010", padding: 14, boxShadow: "0 30px 80px rgba(0,0,0,.45)", transform: `translateY(${interpolate(s, [0, 1], [120, 0])}px)`, opacity: s}}>
      <div style={{width: "100%", height: "100%", borderRadius: 42, background: WHITE, overflow: "hidden", position: "relative"}}>
        <div style={{position: "absolute", top: 12, left: "50%", transform: "translateX(-50%)", width: 120, height: 30, borderRadius: 16, background: "#101010", zIndex: 3}} />
        {children}
      </div>
    </div>
  );
};

const PantallaCategorias: React.FC<{w: number}> = ({w}) => {
  const frame = useCurrentFrame();
  const scroll = interpolate(frame, [20, 110], [0, -260], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  // Igual que el carrito: la pantalla del feed es más angosta, así que las medidas
  // escalan con ella y el nombre de la categoría nunca se sale de su tarjeta.
  const k = w / 532;
  const px = (n: number) => Math.round(n * k);
  const tile = (w - 2 * px(28) - 2 * px(16)) / 3;
  return (
    <div style={{position: "absolute", inset: 0, paddingTop: 58, fontFamily: RALEWAY}}>
      <div style={{padding: `6px ${px(28)}px 14px`, borderBottom: "1px solid #eee", display: "flex", alignItems: "center", justifyContent: "space-between"}}>
        <Img src={staticFile("assets/ebema/logos/logo_click_1_gris.png")} style={{height: px(40)}} />
        <div style={{width: px(44), height: px(44), borderRadius: 22, border: `3px solid ${RED}`, display: "flex", alignItems: "center", justifyContent: "center"}}>
          <svg viewBox="0 0 100 100" width="60%" height="60%"><path d="M30 40 H70 L64 70 H36 Z M40 78 a4 4 0 1 0 0.1 0 M60 78 a4 4 0 1 0 0.1 0 M22 28 H30" stroke={RED} strokeWidth="7" fill="none" strokeLinecap="round" strokeLinejoin="round" /></svg>
        </div>
      </div>
      <div style={{margin: `16px ${px(28)}px`, height: px(52), borderRadius: 26, background: "#F2F2F2", display: "flex", alignItems: "center", padding: `0 ${px(20)}px`, color: GREY, fontSize: px(22), fontWeight: 600}}>Buscar materiales…</div>
      <div style={{padding: `0 ${px(28)}px`, fontSize: px(22), fontWeight: 800, color: GREY, textTransform: "uppercase", letterSpacing: 1}}>Categorías</div>
      <div style={{position: "relative", overflow: "hidden", height: 900}}>
        <div style={{display: "flex", flexWrap: "wrap", gap: px(16), padding: `14px ${px(28)}px`, transform: `translateY(${scroll}px)`}}>
          {CATS.concat(CATS).map((c, i) => {
            const s = spring({fps: 30, frame: frame - 6 - i * 3, config: {damping: 14, stiffness: 180}});
            return (
              <div key={i} style={{width: tile, height: tile + 24, borderRadius: 18, background: "#FAFAFA", border: "1px solid #ECECEC", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 6, opacity: s, transform: `scale(${interpolate(s, [0, 1], [0.8, 1])})`}}>
                <div style={{width: tile * 0.5, height: tile * 0.5}}><Icono i={i} /></div>
                <div style={{maxWidth: "94%", textAlign: "center", whiteSpace: "nowrap", overflow: "hidden", textOverflow: "clip", fontSize: Math.min(px(19), Math.round(tile * 0.155)), fontWeight: 700, color: GREY}}>{c}</div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};

const PRODS = [
  {img: "assets/ebema/click/pajarito_hi.png", n: "Látex Pajarito"},
  {img: "assets/ebema/click/sikaflex_hi.png", n: "Sikaflex 11 FC+"},
  {img: "assets/ebema/click/antioxido_hi.png", n: "Antióxido Maestranza"},
];
const PantallaCarrito: React.FC<{w: number}> = ({w}) => {
  const frame = useCurrentFrame();
  const added = PRODS.filter((_, i) => frame > 30 + i * 38).length;
  const bump = spring({fps: 30, frame: frame - (30 + Math.max(0, added - 1) * 38), config: {damping: 8, stiffness: 260}});
  // La pantalla del feed es más angosta que la del story: todo escala con ella para
  // que el nombre del producto nunca choque con la píldora "Agregado" (bug 24-08-2026).
  const k = w / 492;
  const px = (n: number) => Math.round(n * k);
  return (
    <div style={{position: "absolute", inset: 0, paddingTop: 58, fontFamily: RALEWAY}}>
      <div style={{padding: `6px ${px(28)}px 14px`, borderBottom: "1px solid #eee", display: "flex", alignItems: "center", justifyContent: "space-between"}}>
        <Img src={staticFile("assets/ebema/logos/logo_click_1_gris.png")} style={{height: px(40)}} />
        <div style={{position: "relative", width: px(44), height: px(44), borderRadius: 22, border: `3px solid ${RED}`, display: "flex", alignItems: "center", justifyContent: "center", transform: `scale(${1 + 0.25 * Math.sin(Math.PI * Math.min(1, bump))})`}}>
          <svg viewBox="0 0 100 100" width="60%" height="60%"><path d="M30 40 H70 L64 70 H36 Z M40 78 a4 4 0 1 0 0.1 0 M60 78 a4 4 0 1 0 0.1 0 M22 28 H30" stroke={RED} strokeWidth="7" fill="none" strokeLinecap="round" strokeLinejoin="round" /></svg>
          {added > 0 ? <div style={{position: "absolute", top: -10, right: -10, width: 28, height: 28, borderRadius: 14, background: RED, color: WHITE, fontFamily: HELV, fontSize: 18, display: "flex", alignItems: "center", justifyContent: "center"}}>{added}</div> : null}
        </div>
      </div>
      <div style={{padding: `18px ${px(28)}px`, display: "flex", flexDirection: "column", gap: px(14)}}>
        {PRODS.map((p, i) => {
          const start = 10 + i * 38;
          const s = spring({fps: 30, frame: frame - start, config: {damping: 14, stiffness: 170}});
          const ok = frame > 30 + i * 38;
          return (
            <div key={i} style={{display: "flex", alignItems: "center", gap: px(16), padding: px(14), borderRadius: 18, background: "#FAFAFA", border: "1px solid #ECECEC", opacity: s, transform: `translateX(${interpolate(s, [0, 1], [60, 0])}px)`}}>
              <div style={{width: px(92), height: px(92), flexShrink: 0, borderRadius: 12, background: WHITE, display: "flex", alignItems: "center", justifyContent: "center"}}>
                <Img src={staticFile(p.img)} style={{maxWidth: "86%", maxHeight: "86%"}} />
              </div>
              <div style={{flex: 1, minWidth: 0, fontSize: px(22), lineHeight: 1.2, overflowWrap: "anywhere", fontWeight: 700, color: GREY}}>{p.n}</div>
              <div style={{flexShrink: 0, minWidth: px(120), height: px(44), padding: `0 ${px(16)}px`, borderRadius: px(22), background: ok ? RED : "#E5E5E5", color: ok ? WHITE : GREY, fontSize: px(18), fontWeight: 800, lineHeight: 1, whiteSpace: "nowrap", display: "flex", alignItems: "center", justifyContent: "center"}}>{ok ? "\u2713 Agregado" : "Agregar"}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

const Check: React.FC<{text: string; delay: number}> = ({text, delay}) => {
  const s = useIn(delay, {damping: 11, stiffness: 200});
  return (
    <div style={{display: "flex", alignItems: "center", gap: 22, opacity: s, transform: `translateX(${interpolate(s, [0, 1], [-50, 0])}px)`}}>
      <div style={{width: 74, height: 74, borderRadius: 16, background: RED, display: "flex", alignItems: "center", justifyContent: "center", flexShrink: 0}}>
        <svg viewBox="0 0 100 100" width="64%" height="64%"><path d="M20 52 L42 72 L80 30" stroke={WHITE} strokeWidth="12" fill="none" strokeLinecap="round" strokeLinejoin="round" /></svg>
      </div>
      <div style={{fontFamily: RALEWAY, fontWeight: 900, fontSize: 46, color: WHITE, textTransform: "uppercase", textShadow: "0 2px 6px rgba(0,0,0,.35)"}}>{text}</div>
    </div>
  );
};

// ---- escenas ----
const S1: React.FC<{fmt: Fmt}> = ({fmt}) => (
  <AbsoluteFill>
    <Foto src="assets/ebema/click/ap_contratista_obra.png" zoom={[1.2, 1.08]} velo={0.42} dur={T.s1} pos="center 30%" />
    <Centro top={fmt === "story" ? "56%" : "62%"}>
      <Titular lines={["¿Todavía compras", "materiales de la", "forma tradicional?"]} size={fmt === "story" ? 70 : 62} delay={8} out={T.s1} />
    </Centro>
  </AbsoluteFill>
);
const S2: React.FC<{fmt: Fmt}> = ({fmt}) => {
  const story = fmt === "story";
  const pw = story ? 560 : 470, ph = story ? 1000 : 840;
  return (
    <AbsoluteFill>
      <Foto src="assets/ebema/click/v6_click_contratista_tienda.png" zoom={[1.1, 1.18]} velo={0.6} blur={6} dur={T.s2 - T.s1} />
      <div style={{position: "absolute", left: 0, right: 0, top: story ? 250 : 200, textAlign: "center", zIndex: 4}}>
        <Titular lines={["Compra online", "cuando lo necesites"]} size={story ? 64 : 56} delay={2} />
        <div style={{marginTop: 14, fontFamily: RALEWAY, fontWeight: 600, fontSize: 30, color: WHITE}}>este septiembre.</div>
      </div>
      <div style={{position: "absolute", left: 0, right: 0, top: story ? 560 : 470, zIndex: 3}}>
        <Phone w={pw} h={ph} delay={6}><PantallaCategorias w={pw - 28} /></Phone>
      </div>
    </AbsoluteFill>
  );
};
const S3: React.FC<{fmt: Fmt}> = ({fmt}) => {
  const story = fmt === "story";
  // El teléfono arranca bajo el lockup: antes le comía la bajada "Materiales y
  // beneficios" (QA 24-08-2026). Alto ajustado al contenido real de la pantalla.
  const pw = story ? 520 : 440, ph = story ? 700 : 590;
  return (
    <AbsoluteFill>
      <Foto src="assets/ebema/click/v6_click_contratista_tienda.png" zoom={[1.18, 1.1]} velo={0.62} blur={6} dur={T.s3 - T.s2} />
      <div style={{position: "absolute", left: 0, right: 0, top: story ? 290 : 215, zIndex: 3}}>
        <Phone w={pw} h={ph} delay={0}><PantallaCarrito w={pw - 28} /></Phone>
      </div>
      <div style={{position: "absolute", left: 0, right: 0, top: story ? 1090 : 900, padding: "0 110px", display: "flex", flexDirection: "column", gap: 26, zIndex: 4}}>
        <Check text="Precios exclusivos" delay={40} />
        <Check text="Compra 24/7" delay={80} />
        <Check text="Sin mínimo de compra" delay={120} />
      </div>
    </AbsoluteFill>
  );
};
const S4: React.FC<{fmt: Fmt}> = ({fmt}) => {
  // Paulina (21-08): bodega a la izquierda (retiro en sucursal) · contratista en obra a la derecha (despacho)
  const s = useIn(0, {damping: 16, stiffness: 120});
  const split = interpolate(s, [0, 1], [100, 50]);
  const frame = useCurrentFrame();
  const z = interpolate(frame, [0, T.s4 - T.s3], [1.08, 1.16], {extrapolateRight: "clamp"});
  const Mitad: React.FC<{lado: "izq" | "der"; src: string; pos: string}> = ({lado, src, pos}) => (
    <div style={{position: "absolute", top: 0, bottom: 0, left: lado === "izq" ? 0 : "50%", width: "50%", overflow: "hidden"}}>
      <Img src={staticFile(src)} style={{width: "100%", height: "100%", objectFit: "cover", objectPosition: pos, transform: `scale(${z})`}} />
      <AbsoluteFill style={{background: "rgba(0,0,0,.42)"}} />
    </div>
  );
  return (
    <AbsoluteFill>
      <AbsoluteFill style={{clipPath: `inset(0 ${100 - split}% 0 0)`}}>
        <Mitad lado="izq" src="assets/ebema/click/ap_bodega_pasillo.png" pos="50% 50%" />
      </AbsoluteFill>
      <AbsoluteFill style={{clipPath: `inset(0 0 0 ${split}%)`}}>
        <Mitad lado="der" src="assets/ebema/click/ap_contratista_obra.png" pos="22% 35%" />
      </AbsoluteFill>
      <div style={{position: "absolute", left: "50%", top: 0, bottom: 0, width: 6, background: WHITE, transform: "translateX(-50%)", zIndex: 3}} />
      <div style={{position: "absolute", top: fmt === "story" ? "28%" : "24%", left: 0, width: "50%", textAlign: "center", zIndex: 4, fontFamily: RALEWAY, fontWeight: 800, fontSize: 34, color: WHITE, textTransform: "uppercase", letterSpacing: 2, textShadow: "0 2px 6px rgba(0,0,0,.4)"}}>Retiro en sucursal</div>
      <div style={{position: "absolute", top: fmt === "story" ? "28%" : "24%", right: 0, width: "50%", textAlign: "center", zIndex: 4, fontFamily: RALEWAY, fontWeight: 800, fontSize: 34, color: WHITE, textTransform: "uppercase", letterSpacing: 2, textShadow: "0 2px 6px rgba(0,0,0,.4)"}}>Despacho</div>
      <Centro top={fmt === "story" ? "56%" : "58%"}>
        <Titular lines={["Tú eliges."]} size={96} delay={10} />
      </Centro>
    </AbsoluteFill>
  );
};
const S5: React.FC<{fmt: Fmt}> = ({fmt}) => {
  const frame = useCurrentFrame();
  const dur = T.end - T.s4;
  const vid = fmt === "story" ? "cierre_ebemaclick_st" : "cierre_ebemaclick_post";
  const vidFrames = fmt === "story" ? 111 : 94; // 3,71 s / 3,13 s
  return (
    <AbsoluteFill style={{background: WHITE}}>
      {/* cierre oficial Ebema Click (Paulina, 21-08): lockup + "Regístrate Gratis y accede a precios exclusivos" */}
      <Sequence from={0} durationInFrames={vidFrames} layout="none">
        <OffthreadVideo src={staticFile(`assets/ebema/cierres/${vid}_mute.mp4`)} style={{width: "100%", height: "100%", objectFit: "cover"}} muted />
      </Sequence>
      <Sequence from={vidFrames} durationInFrames={dur - vidFrames} layout="none">
        <Img src={staticFile(`assets/ebema/cierres/${vid}_last.png`)} style={{width: "100%", height: "100%", objectFit: "cover"}} />
      </Sequence>
      <AbsoluteFill style={{background: INK, opacity: interpolate(frame, [dur - 12, dur], [0, 1], {extrapolateLeft: "clamp"})}} />
    </AbsoluteFill>
  );
};

const Musica: React.FC = () => {
  const frame = useCurrentFrame();
  const tramos: [number, number][] = [[VO.a, VO.a + 96], [VO.b, VO.b + 102], [VO.c, VO.c + 177], [VO.d, VO.d + 54], [VO.e, VO.e + 144]];
  const enVoz = tramos.some(([a, b]) => frame >= a - 6 && frame <= b + 6);
  const base = enVoz ? 0.12 : 0.26;
  const fi = interpolate(frame, [0, 20], [0, 1], {extrapolateRight: "clamp"});
  const fo = interpolate(frame, [T.end - 40, T.end], [1, 0], {extrapolateLeft: "clamp"});
  return <Audio src={staticFile("assets/ebema/musica_reel.mp3")} volume={base * fi * fo} />;
};

export const EbemaClickReel: React.FC<EbemaClickReelProps> = ({format}) => {
  ensureFonts();
  const fmt = format;
  return (
    <AbsoluteFill style={{background: INK}}>
      <Sequence from={0} durationInFrames={T.s1}><S1 fmt={fmt} /></Sequence>
      <Sequence from={T.s1} durationInFrames={T.s2 - T.s1}><S2 fmt={fmt} /></Sequence>
      <Sequence from={T.s2} durationInFrames={T.s3 - T.s2}><S3 fmt={fmt} /></Sequence>
      <Sequence from={T.s3} durationInFrames={T.s4 - T.s3}><S4 fmt={fmt} /></Sequence>
      <Sequence from={T.s4} durationInFrames={T.end - T.s4}><S5 fmt={fmt} /></Sequence>
      <Sequence from={0} durationInFrames={T.s4}><Lockup fmt={fmt} /></Sequence>
      <Sequence from={VO.a}><Audio src={staticFile("assets/ebema/vo/ck_01.mp3")} /></Sequence>
      <Sequence from={VO.b}><Audio src={staticFile("assets/ebema/vo/ck_02.mp3")} /></Sequence>
      <Sequence from={VO.c}><Audio src={staticFile("assets/ebema/vo/ck_03.mp3")} /></Sequence>
      <Sequence from={VO.d}><Audio src={staticFile("assets/ebema/vo/ck_04.mp3")} /></Sequence>
      <Sequence from={VO.e}><Audio src={staticFile("assets/ebema/vo/ck_05.mp3")} /></Sequence>
      <Musica />
    </AbsoluteFill>
  );
};
