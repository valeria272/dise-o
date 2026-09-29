/**
 * QB · FEED 05-10 · 15:00 · ESTÁTICO — CUMPLEAÑOS EN QB
 *
 * BRIEF (grilla octubre, FEED col. D, OK PARA DISEÑAR desde el 28-09):
 *   El rótulo dice «ST ESTÁTICA» y el tipo «CARRUSEL», pero el comentario del
 *   cliente manda: «Aquí dejemos un estático de cumpleaños» → POST estático de
 *   feed, 4:5 (1080×1350, entrega 2250×2813).
 *   Visual: una escena real de celebración en QB, la torta con velas llegando o
 *   el cumpleañero/a con su grupo; nocturna, cálida, flash o luz ambiente; mesa
 *   compartida, amigos, torta y ambiente QB.
 *   Texto: TU CUMPLEAÑOS SE CELEBRA EN QB · Bajada: Convierte tu cumpleaños en
 *   una noche inolvidable · Complementario: 5 tragos de cortesía para el
 *   cumpleañero/a · Shots de regalo · Postre · Cuenta separadas · Puedes traer
 *   tu propia torta.
 *
 * REFERENCIA: Pinterest 1107392995886954044 («Yes! Friday», Gatsby Bar) — un
 * collage de polaroids con flash que llena la pieza, y al centro una tarjeta de
 * lino con el título en pincel y el texto chico en caja alta.
 *
 * DIRECCIÓN DE ARTE
 *   · Las POLAROIDS son el recurso de la ref: marco blanco, giro leve, sombra.
 *     Siete fotos: seis reales del shooting «QB 13 oct» (107 grupo, 101 brindis
 *     con espumante, 108 brindis con tinto, 104 la invitada con el celular, 92 y 93 parejas; sólo invitados, la
 *     108 encuadrada para dejar fuera a la persona de camisa blanca del fondo) y
 *     UNA generada, la torta con bengalas llegando a la mesa, porque no hay
 *     cumpleaños en las sesiones → «Imagen referencial».
 *   · La TARJETA de lino al centro, derecha como en la ref. Título con las voces
 *     de QB: «Tu cumpleaños» en Brushwell (el pincel de la ref) y «SE CELEBRA EN
 *     QB» en Raleway ExtraBold, en el verde de QB. Sin punto final (regla Hilton).
 *   · Textos literales del brief. ⚠️ «Cuenta separadas» va como viene: la
 *     concordancia (¿«Cuentas separadas»?) se consulta a contenido.
 *   · Zona segura de feed: 12 % abajo sin texto (la tarjeta cierra en 890).
 *
 * ⭐⭐ RONDA 19 — PASA A CARRUSEL (Scarlette, hilo en FEED!C14, 29-09): «hicieron
 *   ajustes en los beneficios de cumpleaños, entonces vamos a hacer un carrusel.
 *   S.1: Tu cumpleaños / SE CELEBRA EN QB / Convierte tu cumpleaños en una noche
 *   inolvidable. S.2/3/4: seguir el brief». En Drive: C1 S1 CUMPLEAÑOS N°1–N°4.
 *   · N°1 = el post aprobado SIN la lista de beneficios (salió del brief): la
 *     tarjeta se achica y queda sólo título + bajada.
 *   · N°2–N°4 = el mismo sistema (polaroids con flash arriba, tarjeta de lino con la
 *     información). Jerarquía: pregunta en Raleway ExtraBold verde → «El
 *     cumpleañero recibe:» en itálica → beneficios con ícono de línea verde; lo que
 *     se ELIGE va en dos recuadros lado a lado unidos por «o» (en la N°3, que suma
 *     todo, por «+»). Textos literales del brief («Cuentas divididas» reemplaza a
 *     «Cuenta separadas»).
 *   · Sólo la N°1 y la N°4 llevan la torta generada → «*Imagen referencial».
 *
 * ⭐⭐ RONDA 20 (Eli 29-09): «el carrusel se ve muy exagerado. La portada, más limpia, con una
 *   imagen de cumpleaños — como la de la historia, esa imagen que logré que se ve mucho
 *   mejor — y la siguiente slide, con respecto a la referencia; las otras, con imagen
 *   variada».
 *   · N°1: la torta de la ST 07-10 a sangre, velo arriba, «Tu cumpleaños» (Brushwell) +
 *     «SE CELEBRA EN QB» (Raleway) + bajada. Nada más.
 *   · N°2: la REFERENCIA (collage de polaroids con flash + tarjeta de lino), con el texto
 *     de «¿VIENES CON 8 O MÁS?». Es la única lámina con collage.
 *   · N°3 y N°4: una foto real distinta a sangre cada una y la información en el
 *     recuadro oscuro con filete de la historia animada (mismo registro que la ST 07).
 *
 * ⭐⭐ RONDA 21 (Eli 29-09): «el carrusel se ve muy saturado y mal. Quiero que la PORTADA sea
 *   igual a la referencia y las demás slides sean como la de la torta, con mejores fotos;
 *   ya que está en el ojo, utiliza fotos más actuales».
 *   · N°1 = la referencia: collage de polaroids + tarjeta de lino con «Tu cumpleaños / SE
 *     CELEBRA EN QB» y la bajada. Polaroids con fotos de «Fotos 4 agosto» (editadas, ago-2026:
 *     la sesión más reciente de QB) + la torta.
 *   · N°2–N°4 = el registro de la portada de la torta: UNA foto a sangre, velo arriba y el
 *     texto en blanco directo sobre él. Sin recuadros, sin cajas, sin tarjetas. Íconos de
 *     línea finos sólo donde ordenan una lista.
 *     N°2 IMG_4988 (amigos brindando en la mesa) · N°3 IMG_4877 (el grupo grande en la mesa)
 *     · N°4 la torta de la historia (postre y torta propia).
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {QB_ASSETS, QB_LOGO} from "../../../brand/qb";
import {BotonVerde, cargarFuentesQbOct, CIFRAS, Grano, Linea, Velo} from "./QbOctKit";
import {FotoFeed} from "./QbFeedKit";

cargarFuentesQbOct();

const QB_POST05_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "TU CUMPLEAÑOS SE CELEBRA EN QB",
  bajada: "Convierte tu celebración en una noche inolvidable",
  legal: "*Imagen referencial",
  },
  g2: {
  titular: "¿VIENES CON 8 O MÁS?",
  recibe: "El cumpleañero recibe:",
  texto: "4 TRAGOS",
  elige: "+ ELIGE TU FAVORITO:",
  opcion1: "1 bucket de 6 cervezas",
  opcion2: "1 botella de espumante",
  },
  g3: {
  titular: "¿SON 15 O MÁS?",
  bajada: "Hay más para celebrar",
  recibe: "El cumpleañero recibe:",
  texto: "REFILL ILIMITADO DE 1 TRAGO A ELECCIÓN",
  opcion1: "1 bucket de cervezas",
  opcion2: "1 botella de espumante",
  pie: "Combínalos según tu preferencia",
  },
  g4: {
  titular: "TODO LISTO PARA TU CUMPLE",
  item1: "Postre para el cumpleañero",
  item2: "Puedes traer tu propia torta",
  item3: "Cuentas divididas",
  cta: "ARMA EL GRUPO Y RESERVA TU CUMPLE EN QB",
  legal: "*Imagen referencial",
  },
};

const W = 1080;
const VERDE = "#2F4635";

const Polaroid: React.FC<{
  src: string; x: number; y: number; w: number; giro: number; pos?: string; alto?: number;
}> = ({src, x, y, w, giro, pos = "50% 50%", alto = 0.78}) => {
  const b = w * 0.045;
  const hImg = (w - 2 * b) * alto;
  return (
    <div style={{position: "absolute", left: x, top: y, width: w, padding: `${b}px ${b}px ${b * 2.6}px`,
      background: "#FBFAF7", transform: `rotate(${giro}deg)`,
      boxShadow: "0 2px 4px rgba(0,0,0,.35), 0 14px 34px rgba(0,0,0,.5)"}}>
      <Img src={staticFile(`assets/hilton/qb/oct/${src}`)} style={{display: "block", width: "100%",
        height: hImg, objectFit: "cover", objectPosition: pos, filter: "contrast(1.08) saturate(1.05)"}} />
    </div>
  );
};

/** r19: sin la lista de beneficios la tarjeta pierde 120 px y se centra en el hueco. */
const TARJETA = {x: 150, y: 360, w: 780, h: 470};

/** r21 · N°1: la REFERENCIA — polaroids con flash alrededor de la tarjeta de lino. */
export const QbFeed05CumpleG1: React.FC = () => (
  <AbsoluteFill style={{background: "#15110E"}}>
    <Polaroid src="cumple-ago-4808.jpg" x={-50} y={-40} w={430} giro={-4} pos="50% 50%" />
    <Polaroid src="cumple-ago-4796.jpg" x={330} y={-70} w={420} giro={3} pos="50% 45%" />
    <Polaroid src="cumple-ago-4820.jpg" x={710} y={-30} w={430} giro={-2.5} pos="50% 40%" />
    <Polaroid src="cumple-ago-4842.jpg" x={-120} y={380} w={330} giro={4} pos="50% 35%" alto={1.1} />
    <Polaroid src="cumple-ago-4812.jpg" x={880} y={420} w={330} giro={-3.5} pos="50% 35%" alto={1.1} />
    <div style={{position: "absolute", left: TARJETA.x, top: TARJETA.y, width: TARJETA.w, height: TARJETA.h,
      background: "#EEE6D8", boxShadow: "0 3px 6px rgba(0,0,0,.3), 0 20px 50px rgba(0,0,0,.55)",
      backgroundImage: "repeating-linear-gradient(0deg, rgba(90,70,40,.05) 0 1px, transparent 1px 4px), repeating-linear-gradient(90deg, rgba(90,70,40,.05) 0 1px, transparent 1px 4px)"}} />
    <Img src={staticFile(QB_ASSETS.logoBlanco)} style={{position: "absolute", top: TARJETA.y + 52,
      left: (W - 110) / 2, width: 110, height: 110 / QB_LOGO.proporcion,
      filter: "brightness(0) saturate(100%) invert(22%) sepia(14%) saturate(900%) hue-rotate(83deg) brightness(92%)"}} />
    <Linea top={TARJETA.y + 128} cuerpo={150} familia="Brushwell" color={VERDE} sombra={false} interlinea={1}>
      Tu cumpleaños
    </Linea>
    <Linea top={TARJETA.y + 290} cuerpo={48} peso={800} tracking="0.08em" color={VERDE} sombra={false}>
      SE CELEBRA EN QB
    </Linea>
    <Linea top={TARJETA.y + 358} cuerpo={27} italica peso={400} color="#3A332C" sombra={false} ancho={740}>
      {QB_POST05_DATA.pieza.bajada}
    </Linea>
    <Linea top={TARJETA.y + 420} cuerpo={14} italica color="#6B6259" sombra={false} ancho={400}>
      {QB_POST05_DATA.pieza.legal}
    </Linea>
    <Polaroid src="05-cumple-torta.jpg" x={-30} y={862} w={560} giro={-3} pos="50% 55%" />
    <Polaroid src="cumple-ago-4985.jpg" x={560} y={880} w={540} giro={3.5} pos="50% 45%" />
    <Grano />
  </AbsoluteFill>
);

// ───────────────────────────────────────────────────────────────────────────
// r19 · N°2–N°4: dos polaroids arriba y la tarjeta de lino con la información
// ───────────────────────────────────────────────────────────────────────────
const TINTA = "#3A332C";
const LINO = {x: 100, y: 360, w: 880, h: 760};

const T = {fill: "none", stroke: VERDE, strokeWidth: 2.2, strokeLinecap: "round" as const, strokeLinejoin: "round" as const};
const ICONOS: Record<string, React.ReactNode> = {
  copa: <><path d="M9 8 H35 L22 23 Z" {...T} /><path d="M22 23 V37 M15 37 H29" {...T} /><path d="M29 8 L34 3" {...T} /></>,
  balde: <><path d="M8 17 H36 L32 38 H12 Z" {...T} /><path d="M15 17 V7 M22 17 V4 M29 17 V7" {...T} /><path d="M6 17 H38" {...T} /></>,
  botella: <><path d="M19 4 H25 V12 C25 15 30 17 30 22 V38 H14 V22 C14 17 19 15 19 12 Z" {...T} /><path d="M14 26 H30" {...T} /></>,
  refill: <><path d="M9 8 H27 L24 37 H12 Z" {...T} /><path d="M38 15 A8 8 0 1 0 38 27" {...T} /><path d="M38 10 V15 H33" {...T} /></>,
  postre: <><path d="M10 21 H34 L30 37 H14 Z" {...T} /><path d="M10 21 C10 10 34 10 34 21" {...T} /><circle cx="22" cy="8" r="2.6" {...T} /></>,
  torta: <><path d="M8 24 H36 V38 H8 Z" {...T} /><path d="M8 30 C12 33 16 27 22 30 C28 33 32 27 36 30" {...T} /><path d="M15 24 V17 M22 24 V15 M29 24 V17" {...T} /><path d="M15 12.5 V13 M22 10.5 V11 M29 12.5 V13" {...T} strokeWidth={3.4} /></>,
  cuenta: <><path d="M12 5 H32 V38 L28.7 35.5 L25.3 38 L22 35.5 L18.7 38 L15.3 35.5 L12 38 Z" {...T} /><path d="M17 13 H27 M17 19 H27 M17 25 H24" {...T} /></>,
};
const Icono: React.FC<{n: string; t?: number}> = ({n, t = 46}) => (
  <svg width={t} height={t} viewBox="0 0 44 44" style={{flex: "none"}}>{ICONOS[n]}</svg>
);

const Fondo: React.FC<{a: string; b: string; c: string; e: string; posA?: string; posB?: string; posC?: string; posE?: string}> = ({
  a, b, c, e, posA, posB, posC, posE,
}) => (
  <>
    <Polaroid src={a} x={-40} y={-70} w={600} giro={-3.5} pos={posA} alto={0.66} />
    <Polaroid src={b} x={500} y={-40} w={610} giro={3} pos={posB} alto={0.66} />
    <Polaroid src={c} x={-30} y={1060} w={560} giro={3} pos={posC} alto={0.7} />
    <Polaroid src={e} x={540} y={1075} w={570} giro={-2.5} pos={posE} alto={0.7} />
    <div style={{position: "absolute", left: LINO.x, top: LINO.y, width: LINO.w, height: LINO.h,
      background: "#EEE6D8", boxShadow: "0 3px 6px rgba(0,0,0,.3), 0 20px 50px rgba(0,0,0,.55)",
      backgroundImage: "repeating-linear-gradient(0deg, rgba(90,70,40,.05) 0 1px, transparent 1px 4px), repeating-linear-gradient(90deg, rgba(90,70,40,.05) 0 1px, transparent 1px 4px)"}} />
  </>
);

const Titulo: React.FC<{top: number; children: React.ReactNode; cuerpo?: number}> = ({top, children, cuerpo = 62}) => (
  <Linea top={top} cuerpo={cuerpo} peso={800} tracking="0.05em" color={VERDE} sombra={false} ancho={860}>{children}</Linea>
);
const Recibe: React.FC<{top: number; children: React.ReactNode}> = ({top, children}) => (
  <Linea top={top} cuerpo={32} italica peso={400} color={TINTA} sombra={false} ancho={760}>{children}</Linea>
);
const Filete: React.FC<{top: number}> = ({top}) => (
  <div style={{position: "absolute", top, left: (W - 160) / 2, width: 160, borderTop: `2px solid ${VERDE}`, opacity: 0.6}} />
);

/** Beneficio en su renglón: ícono verde + texto, centrado. */
const Fila: React.FC<{top: number; icono: string; children: React.ReactNode; fuerte?: boolean; cuerpo?: number}> = ({
  top, icono, children, fuerte = false, cuerpo = 36,
}) => (
  <div style={{position: "absolute", top, left: 0, right: 0, display: "flex", justifyContent: "center"}}>
    <div style={{display: "flex", alignItems: "center", gap: 18, color: fuerte ? VERDE : TINTA,
      fontFamily: "Raleway", fontWeight: fuerte ? 800 : 600, fontSize: cuerpo,
      letterSpacing: fuerte ? "0.04em" : "0.01em", ...CIFRAS}}>
      <Icono n={icono} t={cuerpo * 1.45} />
      <span>{children}</span>
    </div>
  </div>
);

/** Lo que se ELIGE: dos recuadros lado a lado unidos por «o» (o «+»). */
const Opciones: React.FC<{top: number; a: string; b: string; iconoA: string; iconoB: string; union?: string; w?: number}> = ({
  top, a, b, iconoA, iconoB, union = "o", w = 360,
}) => {
  const caja = (txt: string, ic: string) => (
    <div style={{width: w, height: 180, boxSizing: "border-box", border: `2px solid ${VERDE}`, borderRadius: 10,
      display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 10,
      color: TINTA, fontFamily: "Raleway", fontWeight: 600, fontSize: 30, textAlign: "center", ...CIFRAS}}>
      <Icono n={ic} t={58} />
      <span style={{padding: "0 14px"}}>{txt}</span>
    </div>
  );
  return (
    <div style={{position: "absolute", top, left: 0, right: 0, display: "flex", justifyContent: "center",
      alignItems: "center", gap: 22}}>
      {caja(a, iconoA)}
      <span style={{fontFamily: union === "o" ? "Brushwell" : "Raleway", fontWeight: 300,
        fontSize: union === "o" ? 64 : 56, color: VERDE, lineHeight: 1}}>{union}</span>
      {caja(b, iconoB)}
    </div>
  );
};

/** r21 · N°2–N°4: una foto a sangre y el texto blanco directo sobre el velo (el registro de
 *  la portada de la torta de la r20). */
const TB = {fill: "none", stroke: "#fff", strokeWidth: 2.2, strokeLinecap: "round" as const, strokeLinejoin: "round" as const};
const ICONOS_B: Record<string, React.ReactNode> = {
  postre: <><path d="M10 21 H34 L30 37 H14 Z" {...TB} /><path d="M10 21 C10 10 34 10 34 21" {...TB} /><circle cx="22" cy="8" r="2.6" {...TB} /></>,
  torta: <><path d="M8 24 H36 V38 H8 Z" {...TB} /><path d="M8 30 C12 33 16 27 22 30 C28 33 32 27 36 30" {...TB} /><path d="M15 24 V17 M22 24 V15 M29 24 V17" {...TB} /></>,
  cuenta: <><path d="M12 5 H32 V38 L28.7 35.5 L25.3 38 L22 35.5 L18.7 38 L15.3 35.5 L12 38 Z" {...TB} /><path d="M17 13 H27 M17 19 H27 M17 25 H24" {...TB} /></>,
};
const Blanco: React.FC<{top: number; cuerpo: number; peso?: number; italica?: boolean; tracking?: string; children: React.ReactNode}> = ({
  top, cuerpo, peso = 400, italica = false, tracking, children,
}) => <Linea top={top} cuerpo={cuerpo} peso={peso} italica={italica} tracking={tracking} ancho={960}>{children}</Linea>;

export const QbFeed05CumpleG2: React.FC = () => {
  const d = QB_POST05_DATA.g2;
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <FotoFeed src="assets/hilton/qb/oct/cumple-ago-4988.jpg" pos="50% 50%" />
      <Velo arriba={[760, 0.92]} abajo={[240, 0.4]} />
      <Blanco top={96} cuerpo={60} peso={800} tracking="0.04em">{d.titular}</Blanco>
      <Blanco top={180} cuerpo={30} italica peso={300}>{d.recibe}</Blanco>
      <Blanco top={232} cuerpo={74} peso={800} tracking="0.03em">{d.texto}</Blanco>
      <Blanco top={330} cuerpo={30} peso={400}>+ Elige tu favorito: 1 bucket de 6 cervezas</Blanco>
      <Blanco top={372} cuerpo={30} peso={400}>o 1 botella de espumante</Blanco>
    </AbsoluteFill>
  );
};

export const QbFeed05CumpleG3: React.FC = () => {
  const d = QB_POST05_DATA.g3;
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <FotoFeed src="assets/hilton/qb/oct/cumple-ago-4877.jpg" pos="50% 50%" />
      <Velo arriba={[800, 0.92]} abajo={[240, 0.4]} />
      <Blanco top={86} cuerpo={60} peso={800} tracking="0.04em">{d.titular}</Blanco>
      <Linea top={160} cuerpo={92} familia="Brushwell" interlinea={1}>{d.bajada}</Linea>
      <Blanco top={288} cuerpo={30} italica peso={300}>{d.recibe}</Blanco>
      <Blanco top={336} cuerpo={40} peso={800}>Refill ilimitado de 1 trago a elección</Blanco>
      <Blanco top={396} cuerpo={30} peso={400}>+ 1 bucket de cervezas + 1 botella de espumante</Blanco>
      <Blanco top={444} cuerpo={26} italica peso={300}>{d.pie}</Blanco>
    </AbsoluteFill>
  );
};

export const QbFeed05CumpleG4: React.FC = () => {
  const d = QB_POST05_DATA.g4;
  const items = [["postre", d.item1], ["torta", d.item2], ["cuenta", d.item3]] as const;
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <FotoFeed src="assets/hilton/qb/oct/07-cumple-torta-verde.jpg" pos="50% 75%" />
      <Velo arriba={[760, 0.92]} abajo={[300, 0.5]} />
      <Blanco top={96} cuerpo={58} peso={800} tracking="0.04em">{d.titular}</Blanco>
      <div style={{position: "absolute", top: 190, left: 0, right: 0, display: "flex", justifyContent: "center"}}>
        <div style={{display: "flex", flexDirection: "column", gap: 14, color: "#fff", fontFamily: "Raleway",
          fontSize: 32, fontWeight: 500, textShadow: "0 2px 12px rgba(0,0,0,.5)"}}>
          {items.map(([ic, t]) => (
            <div key={ic} style={{display: "flex", alignItems: "center", gap: 16}}>
              <svg width={40} height={40} viewBox="0 0 44 44" style={{flex: "none"}}>{ICONOS_B[ic]}</svg>
              <span>{t}</span>
            </div>
          ))}
        </div>
      </div>
      <BotonVerde top={410} ancho={720} alto={96} cuerpo={28}>
        <span style={{textAlign: "center", lineHeight: 1.25, letterSpacing: "0.05em"}}>ARMA EL GRUPO Y RESERVA<br />TU CUMPLE EN QB</span>
      </BotonVerde>
      <Linea top={1150} cuerpo={16} italica ancho={400} color="rgba(255,255,255,.8)">{d.legal}</Linea>
    </AbsoluteFill>
  );
};
