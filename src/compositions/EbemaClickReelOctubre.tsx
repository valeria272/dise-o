import React from "react";
import {AbsoluteFill, Img, OffthreadVideo, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";

// =============================================================================
// EBEMA CLICK — Reel Octubre 2026 · pieza 16 del brief
// 1080×1920 · 30 fps · 444 frames = 14,8 s (el brief pide «máx. 15 s»)
//
// El guion del brief es el de septiembre MENOS la escena de despacho/retiro, así que
// esta composición extiende `EbemaClickReel.tsx` (aprobada) en vez de inventar otra:
//   0,0–2,8 s  contratista revisando materiales desde el celular en obra
//   2,8–5,8 s  pantalla de Ebema Click navegando por categorías
//   5,8–9,4 s  productos agregándose al carrito + íconos de beneficios
//   9,4–11,1 s la plataforma abierta + el claim del brief
//  11,1–14,8 s CIERRE OFICIAL de Paulina, tal cual (manual §7, no se rediseña)
//
// ZONAS SEGURAS DE REEL — más estrictas que las del feed. Se toma la más exigente de
// cada borde entre la hoja del brief (120 arriba / 420 abajo / 180 derecha) y la regla
// global del estudio (250 / 340 / 115): **todo el contenido vive entre y=250 e y=1500**,
// con 180 px de aire a cada lado para que la columna de íconos de la app no tape nada.
//
// Sin voz en off: el brief pide que se entienda sin sonido y el texto en pantalla cuenta
// la historia entera (hoja «Zonas seguras»: «si no hay voz, el texto en pantalla cuenta
// la historia»). El único audio es el del cierre oficial.
// =============================================================================
const RED = "#EC1C23", GREY = "#6D6F72", WHITE = "#FFFFFF", INK = "#111111";
export const OCT_FPS = 30;
export const OCT_DURATION = 444;

// zona segura
const SAFE_TOP = 250, SAFE_BOTTOM = 1500, SAFE_X = 180;

let fontsOk = false;
const ensureFonts = () => {
  if (fontsOk || typeof document === "undefined") return;
  fontsOk = true;
  const f = (w: number, file: string) =>
    `@font-face { font-family:'RalewayEB'; font-weight:${w}; font-display:block; src:url(${staticFile(`assets/ebema/fonts/${file}`)}) format('truetype'); }`;
  const css = [f(400, "Raleway-Regular.ttf"), f(600, "Raleway-SemiBold.ttf"), f(700, "Raleway-Bold.ttf"),
    f(800, "Raleway-ExtraBold.ttf"), f(900, "Raleway-Black.ttf"),
    `@font-face { font-family:'HelvEB'; font-weight:700; font-display:block; src:url(${staticFile("assets/ebema/fonts/Helvetica-Bold.ttf")}) format('truetype'); }`].join("\n");
  const st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  const fs = (document as unknown as {fonts?: {load: (s: string) => void}}).fonts;
  if (fs) ["400", "600", "700", "800", "900"].forEach((w) => fs.load(`${w} 40px RalewayEB`));
};
const RALEWAY = "'RalewayEB', 'Raleway', Arial, sans-serif";
const HELV = "'HelvEB', Helvetica, Arial, sans-serif";

// timeline (30 fps)
const T = {s1: 84, s2: 174, s3: 282, s4: 333, end: 444};
const CIERRE_FRAMES = 111; // 3,70 s medidos con ffprobe sobre el cierre oficial

const useIn = (delay = 0, cfg = {damping: 13, stiffness: 170}) => {
  const frame = useCurrentFrame(); const {fps} = useVideoConfig();
  return spring({fps, frame: frame - delay, config: cfg});
};

const Foto: React.FC<{src: string; zoom?: [number, number]; velo?: number; dur: number; blur?: number; pos?: string}> =
({src, zoom = [1.06, 1.16], velo = 0.4, dur, blur = 0, pos = "center"}) => {
  const frame = useCurrentFrame();
  const z = interpolate(frame, [0, dur], zoom, {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill>
      <Img src={staticFile(src)} style={{width: "100%", height: "100%", objectFit: "cover", objectPosition: pos,
        transform: `scale(${z})`, filter: blur ? `blur(${blur}px)` : undefined}} />
      <AbsoluteFill style={{background: `rgba(0,0,0,${velo})`}} />
    </AbsoluteFill>
  );
};

// El lockup arranca en la zona segura, no en el borde
// sin animación de entrada, por lo mismo que el titular de la escena 1
const Lockup: React.FC = () => {
  return (
    <div style={{position: "absolute", top: SAFE_TOP, left: "50%", transform: "translateX(-50%)", zIndex: 5}}>
      <Img src={staticFile("assets/ebema/logos/logo_click_2_blanco_acento.png")} style={{height: 110}} />
    </div>
  );
};

// una línea del titular — componente propio para no llamar hooks dentro de un map
const Linea: React.FC<{texto: string; delay: number; primera: boolean; fijo?: boolean}> = ({texto, delay, primera, fijo}) => {
  const anim = useIn(delay, {damping: 12, stiffness: 190});
  const s = fijo ? 1 : anim;
  return (
    <span style={{position: "relative", display: "block", whiteSpace: "nowrap", marginTop: primera ? 0 : 2,
      transform: `translateY(${interpolate(s, [0, 1], [40, 0])}px)`, opacity: s}}>{texto}</span>
  );
};

// `fijo` deja el titular puesto desde el frame 0, sin animación de entrada: el brief
// exige que el primer frame se lea solo porque se usa como miniatura del video.
const Titular: React.FC<{lines: string[]; size: number; delay?: number; out?: number; fijo?: boolean}> =
({lines, size, delay = 0, out, fijo}) => {
  const frame = useCurrentFrame();
  const anim = useIn(delay + 2, {damping: 16, stiffness: 140});
  const box = fijo ? 1 : anim;
  const exit = out ? interpolate(frame, [out - 10, out], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"}) : 1;
  return (
    <div style={{opacity: exit, transform: `scale(${interpolate(exit, [0, 1], [1.05, 1])})`}}>
      <div style={{position: "relative", display: "inline-block", padding: "0 26px", lineHeight: 1, fontFamily: RALEWAY,
        fontWeight: 900, fontSize: size, color: WHITE, textTransform: "uppercase", letterSpacing: 0.3,
        textShadow: "0 2px 5px rgba(0,0,0,.22)"}}>
        <div style={{position: "absolute", left: 0, right: 0, top: size * 0.5, bottom: -10, background: RED,
          transformOrigin: "0% 50%", transform: `scaleX(${box})`}} />
        {lines.map((l, i) => <Linea key={i} texto={l} delay={delay + 4 + i * 5} primera={i === 0} fijo={fijo} />)}
      </div>
    </div>
  );
};

const Boton: React.FC<{text: string; delay?: number}> = ({text, delay = 0}) => {
  const s = useIn(delay, {damping: 10, stiffness: 220});
  return <div style={{display: "inline-block", background: RED, color: WHITE, fontFamily: RALEWAY, fontWeight: 700,
    fontSize: 32, padding: "16px 48px", borderRadius: 10, opacity: s,
    transform: `scale(${interpolate(s, [0, 1], [0.6, 1])})`}}>{text}</div>;
};

// ---- teléfono con la pantalla de Ebema Click ----
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
    <div style={{position: "relative", width: w, height: h, margin: "0 auto", borderRadius: 48, background: "#101010",
      padding: 13, boxShadow: "0 30px 80px rgba(0,0,0,.45)",
      transform: `translateY(${interpolate(s, [0, 1], [120, 0])}px)`, opacity: s}}>
      <div style={{width: "100%", height: "100%", borderRadius: 37, background: WHITE, overflow: "hidden", position: "relative"}}>
        <div style={{position: "absolute", top: 11, left: "50%", transform: "translateX(-50%)", width: 110, height: 27,
          borderRadius: 14, background: "#101010", zIndex: 3}} />
        {children}
      </div>
    </div>
  );
};

const Tarjeta: React.FC<{i: number; nombre: string; tile: number; px: (n: number) => number}> = ({i, nombre, tile, px}) => {
  const frame = useCurrentFrame();
  const s = spring({fps: 30, frame: frame - 6 - i * 3, config: {damping: 14, stiffness: 180}});
  return (
    <div style={{width: tile, height: tile + 22, borderRadius: 16, background: "#FAFAFA", border: "1px solid #ECECEC",
      display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 5,
      opacity: s, transform: `scale(${interpolate(s, [0, 1], [0.8, 1])})`}}>
      <div style={{width: tile * 0.5, height: tile * 0.5}}><Icono i={i} /></div>
      <div style={{maxWidth: "94%", textAlign: "center", whiteSpace: "nowrap", overflow: "hidden",
        fontSize: Math.min(px(18), Math.round(tile * 0.155)), fontWeight: 700, color: GREY}}>{nombre}</div>
    </div>
  );
};

const PantallaCategorias: React.FC<{w: number}> = ({w}) => {
  const frame = useCurrentFrame();
  // el scroll cabe en los 90 frames de la escena (antes iba a 110 y quedaba cortado)
  const scroll = interpolate(frame, [15, 85], [0, -230], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const k = w / 532;
  const px = (n: number) => Math.round(n * k);
  const tile = (w - 2 * px(26) - 2 * px(14)) / 3;
  return (
    <div style={{position: "absolute", inset: 0, paddingTop: 54, fontFamily: RALEWAY}}>
      <div style={{padding: `6px ${px(26)}px 13px`, borderBottom: "1px solid #eee", display: "flex",
        alignItems: "center", justifyContent: "space-between"}}>
        <Img src={staticFile("assets/ebema/logos/logo_click_1_gris.png")} style={{height: px(38)}} />
        <div style={{width: px(42), height: px(42), borderRadius: 21, border: `3px solid ${RED}`, display: "flex",
          alignItems: "center", justifyContent: "center"}}>
          <svg viewBox="0 0 100 100" width="60%" height="60%"><path d="M30 40 H70 L64 70 H36 Z M40 78 a4 4 0 1 0 0.1 0 M60 78 a4 4 0 1 0 0.1 0 M22 28 H30" stroke={RED} strokeWidth="7" fill="none" strokeLinecap="round" strokeLinejoin="round" /></svg>
        </div>
      </div>
      <div style={{margin: `14px ${px(26)}px`, height: px(48), borderRadius: 24, background: "#F2F2F2", display: "flex",
        alignItems: "center", padding: `0 ${px(18)}px`, color: GREY, fontSize: px(21), fontWeight: 600}}>Buscar materiales…</div>
      <div style={{padding: `0 ${px(26)}px`, fontSize: px(21), fontWeight: 800, color: GREY, textTransform: "uppercase",
        letterSpacing: 1}}>Categorías</div>
      <div style={{position: "relative", overflow: "hidden", height: 700}}>
        <div style={{display: "flex", flexWrap: "wrap", gap: px(14), padding: `13px ${px(26)}px`,
          transform: `translateY(${scroll}px)`}}>
          {CATS.concat(CATS).map((c, i) => <Tarjeta key={i} i={i} nombre={c} tile={tile} px={px} />)}
        </div>
      </div>
    </div>
  );
};

// El carrito va con los íconos de categoría, NO con packshots: los 3 packshots que usaba
// el reel de septiembre (`pajarito_hi` / `sikaflex_hi` / `antioxido_hi`) viven en el kit
// del cliente, que no está en esta máquina. Categorías genéricas = ni marcas ni precios
// inventados, que es lo que el manual prohíbe. Ver ENTREGA.md.
const CARRO = [{i: 0, n: "Cementos"}, {i: 1, n: "Pinturas"}, {i: 4, n: "Fierros"}];
const FilaCarro: React.FC<{fila: {i: number; n: string}; idx: number; px: (n: number) => number}> = ({fila, idx, px}) => {
  const frame = useCurrentFrame();
  const start = 4 + idx * 20;
  const s = spring({fps: 30, frame: frame - start, config: {damping: 14, stiffness: 170}});
  const ok = frame > start + 14;
  return (
    <div style={{display: "flex", alignItems: "center", gap: px(14), padding: px(13), borderRadius: 16,
      background: "#FAFAFA", border: "1px solid #ECECEC", opacity: s,
      transform: `translateX(${interpolate(s, [0, 1], [60, 0])}px)`}}>
      <div style={{width: px(84), height: px(84), flexShrink: 0, borderRadius: 11, background: WHITE, display: "flex",
        alignItems: "center", justifyContent: "center", padding: px(12)}}>
        <Icono i={fila.i} />
      </div>
      <div style={{flex: 1, minWidth: 0, fontSize: px(22), lineHeight: 1.2, fontWeight: 700, color: GREY}}>{fila.n}</div>
      {/* la píldora se dimensiona por su texto y no se encoge — bug del reel de agosto */}
      <div style={{flexShrink: 0, minWidth: px(112), height: px(42), padding: `0 ${px(15)}px`, borderRadius: px(21),
        background: ok ? RED : "#E5E5E5", color: ok ? WHITE : GREY, fontSize: px(17), fontWeight: 800, lineHeight: 1,
        whiteSpace: "nowrap", display: "flex", alignItems: "center", justifyContent: "center"}}>
        {ok ? "✓ Agregado" : "Agregar"}
      </div>
    </div>
  );
};

const PantallaCarrito: React.FC<{w: number}> = ({w}) => {
  const frame = useCurrentFrame();
  const added = CARRO.filter((_, i) => frame > 4 + i * 20 + 14).length;
  const bump = spring({fps: 30, frame: frame - (18 + Math.max(0, added - 1) * 20), config: {damping: 8, stiffness: 260}});
  const k = w / 492;
  const px = (n: number) => Math.round(n * k);
  return (
    <div style={{position: "absolute", inset: 0, paddingTop: 54, fontFamily: RALEWAY}}>
      <div style={{padding: `6px ${px(26)}px 13px`, borderBottom: "1px solid #eee", display: "flex",
        alignItems: "center", justifyContent: "space-between"}}>
        <Img src={staticFile("assets/ebema/logos/logo_click_1_gris.png")} style={{height: px(38)}} />
        <div style={{position: "relative", width: px(42), height: px(42), borderRadius: 21, border: `3px solid ${RED}`,
          display: "flex", alignItems: "center", justifyContent: "center",
          transform: `scale(${1 + 0.25 * Math.sin(Math.PI * Math.min(1, bump))})`}}>
          <svg viewBox="0 0 100 100" width="60%" height="60%"><path d="M30 40 H70 L64 70 H36 Z M40 78 a4 4 0 1 0 0.1 0 M60 78 a4 4 0 1 0 0.1 0 M22 28 H30" stroke={RED} strokeWidth="7" fill="none" strokeLinecap="round" strokeLinejoin="round" /></svg>
          {added > 0 ? <div style={{position: "absolute", top: -9, right: -9, width: 26, height: 26, borderRadius: 13,
            background: RED, color: WHITE, fontFamily: HELV, fontSize: 17, display: "flex", alignItems: "center",
            justifyContent: "center"}}>{added}</div> : null}
        </div>
      </div>
      <div style={{padding: `16px ${px(26)}px`, display: "flex", flexDirection: "column", gap: px(12)}}>
        {CARRO.map((f, i) => <FilaCarro key={i} fila={f} idx={i} px={px} />)}
      </div>
    </div>
  );
};

const Check: React.FC<{text: string; delay: number}> = ({text, delay}) => {
  const s = useIn(delay, {damping: 11, stiffness: 200});
  return (
    <div style={{display: "flex", alignItems: "center", gap: 20, opacity: s,
      transform: `translateX(${interpolate(s, [0, 1], [-50, 0])}px)`}}>
      <div style={{width: 66, height: 66, borderRadius: 15, background: RED, display: "flex", alignItems: "center",
        justifyContent: "center", flexShrink: 0}}>
        <svg viewBox="0 0 100 100" width="64%" height="64%"><path d="M20 52 L42 72 L80 30" stroke={WHITE} strokeWidth="12" fill="none" strokeLinecap="round" strokeLinejoin="round" /></svg>
      </div>
      <div style={{fontFamily: RALEWAY, fontWeight: 900, fontSize: 42, color: WHITE, textTransform: "uppercase",
        textShadow: "0 2px 6px rgba(0,0,0,.35)"}}>{text}</div>
    </div>
  );
};

// ---- escenas ----
// 0,0–2,8 s · «¿Todavía compras materiales de la forma tradicional?»
const S1: React.FC = () => (
  <AbsoluteFill>
    <Foto src="assets/ebema/click/oct_contratista_obra.png" zoom={[1.2, 1.08]} velo={0.46} dur={T.s1} pos="center 32%" />
    <div style={{position: "absolute", left: SAFE_X, right: SAFE_X, top: 1010, transform: "translateY(-50%)",
      textAlign: "center", zIndex: 4}}>
      <Titular lines={["¿Todavía compras", "materiales de la", "forma tradicional?"]} size={60} out={T.s1} fijo />
    </div>
  </AbsoluteFill>
);

// 2,8–5,8 s · «Compra online cuando lo necesites» + la plataforma navegando categorías
const S2: React.FC = () => {
  const pw = 500, ph = 800;
  return (
    <AbsoluteFill>
      <Foto src="assets/ebema/click/oct_ferreteria_pasillo.png" zoom={[1.1, 1.18]} velo={0.62} blur={6} dur={T.s2 - T.s1} />
      <div style={{position: "absolute", left: SAFE_X, right: SAFE_X, top: 410, textAlign: "center", zIndex: 4}}>
        <Titular lines={["Compra online", "cuando lo necesites"]} size={54} delay={2} />
      </div>
      <div style={{position: "absolute", left: 0, right: 0, top: 640, zIndex: 3}}>
        <Phone w={pw} h={ph} delay={6}><PantallaCategorias w={pw - 26} /></Phone>
      </div>
    </AbsoluteFill>
  );
};

// 5,8–9,4 s · productos al carrito + los tres beneficios del brief
const S3: React.FC = () => {
  const pw = 470, ph = 470;
  return (
    <AbsoluteFill>
      <Foto src="assets/ebema/click/oct_ferreteria_pasillo.png" zoom={[1.18, 1.1]} velo={0.64} blur={6} dur={T.s3 - T.s2} />
      <div style={{position: "absolute", left: 0, right: 0, top: 450, zIndex: 3}}>
        <Phone w={pw} h={ph} delay={0}><PantallaCarrito w={pw - 26} /></Phone>
      </div>
      {/* anclado al borde inferior de la zona segura: el último check termina en y=1500
          por construcción, no por un número puesto a mano */}
      <div style={{position: "absolute", left: SAFE_X, right: SAFE_X, bottom: 1920 - SAFE_BOTTOM, display: "flex",
        flexDirection: "column", gap: 22, zIndex: 4}}>
        <Check text="Precios exclusivos" delay={22} />
        <Check text="Compra 24/7" delay={46} />
        <Check text="Sin mínimo de compra" delay={70} />
      </div>
    </AbsoluteFill>
  );
};

// 9,4–11,1 s · el claim del brief, justo antes del cierre oficial
const S4: React.FC = () => {
  const dur = T.s4 - T.s3;
  const frame = useCurrentFrame();
  const out = interpolate(frame, [dur - 8, dur], [1, 0], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{opacity: out}}>
      <Foto src="assets/ebema/click/oct_ferreteria_pasillo.png" zoom={[1.12, 1.06]} velo={0.66} blur={8} dur={dur} />
      <div style={{position: "absolute", left: SAFE_X, right: SAFE_X, top: 860, transform: "translateY(-50%)",
        textAlign: "center", zIndex: 4}}>
        <Titular lines={["Ebema Click"]} size={78} delay={0} />
        <div style={{marginTop: 24, fontFamily: RALEWAY, fontWeight: 600, fontSize: 34, lineHeight: 1.25, color: WHITE,
          textShadow: "0 1px 6px rgba(0,0,0,.4)"}}>
          la plataforma para abastecer<br />tu obra o ferretería
        </div>
        <div style={{marginTop: 26}}><Boton text="Regístrate Gratis" delay={10} /></div>
      </div>
    </AbsoluteFill>
  );
};

// 11,1–14,8 s · CIERRE OFICIAL de Paulina, tal cual (manual §7)
const Cierre: React.FC = () => {
  const dur = T.end - T.s4;
  return (
    <AbsoluteFill style={{background: WHITE}}>
      <Sequence from={0} durationInFrames={Math.min(CIERRE_FRAMES, dur)} layout="none">
        <OffthreadVideo src={staticFile("assets/ebema/cierres/cierre_ebemaclick_st.mp4")}
          style={{width: "100%", height: "100%", objectFit: "cover"}} />
      </Sequence>
      {dur > CIERRE_FRAMES ? (
        <Sequence from={CIERRE_FRAMES} durationInFrames={dur - CIERRE_FRAMES} layout="none">
          <Img src={staticFile("assets/ebema/cierres/cierre_ebemaclick_st_last.png")}
            style={{width: "100%", height: "100%", objectFit: "cover"}} />
        </Sequence>
      ) : null}
    </AbsoluteFill>
  );
};

export const EbemaClickReelOctubre: React.FC = () => {
  ensureFonts();
  return (
    <AbsoluteFill style={{background: INK}}>
      <Sequence from={0} durationInFrames={T.s1}><S1 /></Sequence>
      <Sequence from={T.s1} durationInFrames={T.s2 - T.s1}><S2 /></Sequence>
      <Sequence from={T.s2} durationInFrames={T.s3 - T.s2}><S3 /></Sequence>
      <Sequence from={T.s3} durationInFrames={T.s4 - T.s3}><S4 /></Sequence>
      <Sequence from={T.s4} durationInFrames={T.end - T.s4}><Cierre /></Sequence>
      {/* el lockup acompaña las 4 escenas propias; el cierre oficial trae el suyo */}
      <Sequence from={0} durationInFrames={T.s4}><Lockup /></Sequence>
    </AbsoluteFill>
  );
};
