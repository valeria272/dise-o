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
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {QB_ASSETS, QB_LOGO} from "../../../brand/qb";
import {cargarFuentesQbOct, CIFRAS, Grano, Linea} from "./QbOctKit";

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

export const QbFeed05CumpleG1: React.FC = () => (
  <AbsoluteFill style={{background: "#15110E"}}>
    {/* fila de arriba */}
    <Polaroid src="05-cumple-107.jpg" x={-50} y={-40} w={430} giro={-4} pos="50% 55%" />
    <Polaroid src="05-cumple-101.jpg" x={330} y={-70} w={420} giro={3} pos="55% 40%" />
    <Polaroid src="05-cumple-108.jpg" x={710} y={-30} w={430} giro={-2.5} pos="30% 45%" />
    {/* costados, medio escondidas tras la tarjeta */}
    <Polaroid src="05-cumple-92.jpg" x={-120} y={380} w={330} giro={4} pos="30% 40%" alto={1.1} />
    <Polaroid src="05-cumple-93.jpg" x={880} y={420} w={330} giro={-3.5} pos="45% 35%" alto={1.1} />
    {/* la tarjeta de lino */}
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
    {/* fila de abajo: la torta (generada) y un brindis */}
    <Polaroid src="05-cumple-torta.jpg" x={-30} y={862} w={560} giro={-3} pos="50% 55%" />
    <Polaroid src="05-cumple-104.jpg" x={560} y={880} w={540} giro={3.5} pos="50% 40%" />
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
const Opciones: React.FC<{top: number; a: string; b: string; iconoA: string; iconoB: string; union?: string}> = ({
  top, a, b, iconoA, iconoB, union = "o",
}) => {
  const caja = (txt: string, ic: string) => (
    <div style={{width: 360, height: 180, boxSizing: "border-box", border: `2px solid ${VERDE}`, borderRadius: 10,
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

export const QbFeed05CumpleG2: React.FC = () => {
  const d = QB_POST05_DATA.g2;
  const y = LINO.y;
  return (
    <AbsoluteFill style={{background: "#15110E"}}>
      <Fondo a="05-cumple-101.jpg" b="15-amigos-72.jpg" c="15-amigos-98.jpg" e="05-cumple-93.jpg"
        posA="55% 40%" posB="50% 45%" posC="50% 40%" posE="45% 35%" />
      <Titulo top={y + 86}>{d.titular}</Titulo>
      <Recibe top={y + 180}>{d.recibe}</Recibe>
      <Filete top={y + 246} />
      <Fila top={y + 280} icono="copa" fuerte cuerpo={56}>{d.texto}</Fila>
      <Linea top={y + 382} cuerpo={28} peso={700} tracking="0.12em" color={VERDE} sombra={false}>{d.elige}</Linea>
      <Opciones top={y + 446} a={d.opcion1} b={d.opcion2} iconoA="balde" iconoB="botella" />
      <Grano />
    </AbsoluteFill>
  );
};

export const QbFeed05CumpleG3: React.FC = () => {
  const d = QB_POST05_DATA.g3;
  const y = LINO.y;
  return (
    <AbsoluteFill style={{background: "#15110E"}}>
      <Fondo a="05-cumple-107.jpg" b="05-cumple-108.jpg" c="05-cumple-92.jpg" e="15-amigos-101.jpg"
        posA="50% 55%" posB="30% 45%" posC="30% 40%" posE="50% 40%" />
      <Titulo top={y + 62}>{d.titular}</Titulo>
      <Linea top={y + 150} cuerpo={88} familia="Brushwell" color={VERDE} sombra={false} interlinea={1}>{d.bajada}</Linea>
      <Recibe top={y + 272}>{d.recibe}</Recibe>
      <Filete top={y + 334} />
      <Fila top={y + 362} icono="refill" fuerte cuerpo={33}>{d.texto}</Fila>
      <Opciones top={y + 446} a={d.opcion1} b={d.opcion2} iconoA="balde" iconoB="botella" union="+" />
      <Linea top={y + 658} cuerpo={28} italica color={TINTA} sombra={false}>{d.pie}</Linea>
      <Grano />
    </AbsoluteFill>
  );
};

export const QbFeed05CumpleG4: React.FC = () => {
  const d = QB_POST05_DATA.g4;
  const y = LINO.y;
  return (
    <AbsoluteFill style={{background: "#15110E"}}>
      <Fondo a="05-cumple-torta.jpg" b="05-cumple-104.jpg" c="12-pulpo.jpg" e="feed16-autor.jpg"
        posA="50% 55%" posB="50% 40%" posC="50% 50%" posE="50% 45%" />
      <Titulo top={y + 90} cuerpo={50}>{d.titular}</Titulo>
      <Filete top={y + 176} />
      <Fila top={y + 216} icono="postre">{d.item1}</Fila>
      <Fila top={y + 300} icono="torta">{d.item2}</Fila>
      <Fila top={y + 384} icono="cuenta">{d.item3}</Fila>
      {/* CTA del brief en el botón verde de QB (esquinas vivas) */}
      <div style={{position: "absolute", top: y + 500, left: (W - 720) / 2, width: 720, height: 112,
        background: VERDE, display: "flex", alignItems: "center", justifyContent: "center", textAlign: "center",
        color: "#fff", fontFamily: "Raleway", fontWeight: 700, fontSize: 30, letterSpacing: "0.06em", lineHeight: 1.3}}>
        ARMA EL GRUPO Y RESERVA<br />TU CUMPLE EN QB
      </div>
      <Linea top={y + 690} cuerpo={16} italica color="#6B6259" sombra={false} ancho={400}>{d.legal}</Linea>
      <Grano />
    </AbsoluteFill>
  );
};
