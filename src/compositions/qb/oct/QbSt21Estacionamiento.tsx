/**
 * QB · ST 21-10 · 18:00 · ESTÁTICA — DESCUENTO ESTACIONAMIENTO
 *
 * BRIEF (STORIES col. R, OK PARA DISEÑAR, sin comentario):
 *   Un ticket de estacionamiento en primer plano sostenido por una mano,
 *   inspirado en la referencia. El texto principal del beneficio va DENTRO del
 *   ticket. Arriba, una pregunta corta que conecte con el usuario.
 *   Texto superior: ¿VIENES EN AUTO? / Tenemos un beneficio para disfrutar más tu
 *   visita. · Dentro del ticket: 50% OFF / EN TU TICKET DE / ESTACIONAMIENTO /
 *   Ingreso por Encomenderos 275 · Legal: Solicita tu ticket a nuestro personal.
 *
 * REFERENCIA: Pinterest 679480662574801544 (tarjeta naranja sostenida en mano).
 *
 * DIRECCIÓN DE ARTE
 *   · Escena GENERADA (Seedream 5 Pro): mano con un ticket en blanco sobre el bar
 *     desenfocado → lleva «Imagen referencial».
 *   · ⛔ El texto del ticket NO lo escribe la IA (manual §4c): se imprime acá con
 *     las fuentes reales, montado sobre el ticket medido por color
 *     (centro 521,990 · 350×678 · −9,8°) y en «multiply», como tinta.
 *   · El ticket lleva el logo de QB impreso arriba y un troquel punteado: se lee
 *     como un ticket y no como una tarjeta.
 *   · PROMO → zona segura de paid.
  *
 * ⭐ RONDA 4 DE ELI 28-09: parecerse a la ref (Autcomm, las cartas del zodiaco).
 *   · FONDO de plantas tropicales con sol, como la ref: la misma mano y el mismo
 *     ticket de la foto anterior, fondo cambiado con Seedream (edición).
 *   · El TICKET se imprime como la carta de la ref: filete interior, dos reglas
 *     que encierran el texto, serif (Bell MT) con la línea clave en itálica, y la
 *     tinta en el verde de QB. El bloque de texto baja para no quedar bajo el
 *     pulgar, que tapa el tercio derecho a media altura.
 *   · El STICKER de estrella de la ref, en crema, montado en la esquina.
 *   Ticket medido en la foto nueva: centro (529, 987), 294×677, −9,2°.
 *
 * ⭐⭐ RONDA 5 DE ELI 28-09: mandó cómo tiene que ser («te adjunto cómo es acá el
 *   ticket», `raw/hilton/qb/ref-oct/R-21-ticket-eli-28sep.png`): la mesa real de
 *   QB con el plato y el trago, y DOS tickets de estacionamiento sobre la mesa,
 *   abajo a la derecha. Se reemplaza la versión de la mano y las plantas.
 *   · FOTO: «Muhammara siria 1» de la sesión de platos de la carta (la misma de
 *     su imagen), extendida hacia arriba con Seedream para el 9:16 y con mesa
 *     libre abajo → «Imagen referencial».
 *   · TICKETS dibujados acá, como los de su imagen: flechas, código de barras,
 *     la «P» en recuadro, TICKET / ESTACIONAMIENTO y el 50 % grande con el OFF
 *     apilado; tinta gris verdosa. Abajo, «Ingreso por Encomenderos 275».
 *   · Todo el texto dentro de la zona segura (≤ 1580).
 *
 * ⭐⭐ RONDA 6 DE ELI 28-09 (la r5 NO se aprobó): «usa el ticket de la imagen que
 *   te mostré… y la imagen de la referencia del fondo: una mano con el ticket en
 *   mano… no con el mismo plato de fondo… el fondo de lo que describe el brief
 *   respecto a cómo es QB realmente». O sea: MANO sosteniendo el ticket (brief y
 *   ref), el DISEÑO del ticket de su imagen, y el fondo de QB real.
 *   · FOTO: mano sosteniendo un ticket en blanco 3:4 sobre la terraza de QB de
 *     noche, generada con Seedream tomando de referencia la foto real «QB oct-15»
 *     (sesión terraza 10-10: lámparas de mimbre, plantas) → «Imagen referencial».
 *   · TICKET medido en la foto: centro (533, 944) en mesa, 455 × 607, +5,5°. Su
 *     diseño se imprime encima en «multiplicar», así toma la luz del papel.
 *
 * ⭐ RONDA 7 DE ELI 28-09: «está demasiado grande, achica un poco el ticket» y «la
 *   línea de puntitos sobresale de la uña, se solapa». 
 *   · Mano + ticket al 85 %, anclados a la esquina de abajo a la derecha (la mano
 *     sigue entrando desde el borde). Detrás, la misma foto desenfocada, y el canto
 *     de arriba y de la izquierda de la foto chica se funden en ella.
 *   · La tinta va dentro de una MÁSCARA DEL PAPEL medida en la foto
 *     (`21-mascara-papel.png`): donde está el pulgar no hay papel, así que no hay
 *     tinta. Con «multiplicar» solo, la línea se imprimía sobre la uña.
 *
 * ⭐ RONDA 8 DE ELI 28-09: «el ticket se ve muy gigante todavía», «el OFF está muy
 *   cerca del cero, se solapan, y el porcentaje también: que se vea más armónico»,
 *   «en vez de un ticket sean dos, que ella los tenga en la mano, que uno
 *   destaque» y el legal en dos líneas, alineado a la izquierda.
 *   · FOTO nueva: la mano sostiene DOS tickets en abanico sobre la misma terraza;
 *     el de adelante (574×923 en la foto, +2,5°) y el de atrás (−14°, asoma a la
 *     izquierda, más en sombra). Cada uno tiene su máscara de papel medida.
 *   · Conjunto al 80 % (el ticket de adelante queda en ~326 px de ancho).
 *   · El ticket se rediseñó a la proporción de estos papeles (300 × 482): el 50 a
 *     140 y el %/OFF con 14 px de aire, sin tocarse.
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {cargarFuentesQbOct, CIFRAS, Linea, LogoQB, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST21_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "¿VIENES EN AUTO?",
  bajada: "Tenemos un beneficio para disfrutar más tu visita",
  etiqueta: "50% OFF",
  texto: "EN TU TICKET DE ESTACIONAMIENTO",
  pie: "Ingreso por Encomenderos 275",
  legal: "*Imagen referencial. Solicita tu ticket a nuestro personal.",
  },
};

const TINTA = "#3D4640";

/** Código de barras: anchos fijos, no aleatorios, para que el render sea estable. */
const BARRAS = [3, 1, 2, 1, 4, 1, 1, 3, 2, 1, 1, 2, 4, 1, 2, 1, 3, 1, 1, 2, 1, 4, 2, 1, 1, 3, 1, 2, 2, 1, 3, 1, 1, 2, 4, 1];
const Barras: React.FC<{ancho: number; alto: number}> = ({ancho, alto}) => {
  const total = BARRAS.reduce((a, b) => a + b * 2, 0);
  const k = ancho / total;
  let x = 0;
  return (
    <svg width={ancho} height={alto}>
      {BARRAS.map((b, i) => {
        const r = <rect key={i} x={x} y={0} width={b * k} height={alto} fill={TINTA} />;
        x += b * 2 * k;
        return r;
      })}
    </svg>
  );
};

/** Los dos papeles, medidos en la FOTO dibujada a 1080 × 1944. */
const FRENTE = {cx: 566, cy: 962, w: 408, giro: 2.5} as const;
const ATRAS = {cx: 489, cy: 1004, w: 408, giro: -14} as const;
/** Diseño del ticket: 300 × 482 (la proporción de los papeles de la foto). */
const DW = 300;
const DH = 482;
/** Escala del conjunto mano + tickets (r8: «se ve muy gigante todavía»). */
const S = 0.8;
const FOTO = {w: 1080, h: 1944} as const;
const MESA_W = 1080;
const m = (n: string) => staticFile(`assets/hilton/qb/oct/21-mascara-${n}.png`);

/** El ticket de la imagen de Eli, sólo la tinta, para imprimirlo sobre el papel de la foto. */
const Tinta: React.FC<{t: {cx: number; cy: number; w: number; giro: number}; opacidad?: number}> = ({t, opacidad = 0.94}) => {
  const k = t.w / DW;
  return (
    /* `zoom` y no `transform: scale()`: Chrome maqueta al tamaño final y el texto sale nítido */
    <div style={{position: "absolute", left: (t.cx - t.w / 2) / k, top: (t.cy - (DH * k) / 2) / k,
      width: DW, height: DH, zoom: k, transform: `rotate(${t.giro}deg)`, mixBlendMode: "multiply",
      filter: "blur(0.25px)", opacity: opacidad, color: TINTA, fontFamily: "Raleway", ...CIFRAS}}>
      <div style={{position: "absolute", left: 26, top: 22, fontSize: 22, fontWeight: 800, letterSpacing: 6}}>↑↑</div>
      <div style={{position: "absolute", left: 24, top: 56}}><Barras ancho={252} alto={32} /></div>
      <div style={{position: "absolute", left: 24, top: 116, width: 72, height: 56, borderRadius: 10, background: TINTA,
        color: "#fff", fontSize: 46, fontWeight: 800, lineHeight: "56px", textAlign: "center"}}>P</div>
      <div style={{position: "absolute", left: 108, top: 112, fontSize: 44, fontWeight: 800, lineHeight: 1}}>TICKET</div>
      <div style={{position: "absolute", left: 109, top: 158, fontSize: 15, fontWeight: 800, letterSpacing: "0.02em"}}>
        ESTACIONAMIENTO</div>
      {/* 50 · % · OFF — con aire: el 50 cierra en ~182 y el bloque %/OFF parte en 196 */}
      <div style={{position: "absolute", left: 20, top: 214, fontSize: 140, fontWeight: 800, lineHeight: 1,
        letterSpacing: "-0.02em"}}>50</div>
      <div style={{position: "absolute", left: 198, top: 226, fontSize: 60, fontWeight: 800, lineHeight: 1}}>%</div>
      <div style={{position: "absolute", left: 197, top: 296, fontSize: 36, fontWeight: 800, lineHeight: 1,
        letterSpacing: "0.02em"}}>OFF</div>
      <div style={{position: "absolute", left: 24, right: 24, top: 396, borderTop: `2px dashed ${TINTA}`, opacity: 0.7}} />
      <div style={{position: "absolute", left: 24, top: 412, fontSize: 16, fontWeight: 600, lineHeight: 1.25}}>
        Ingreso por<br />Encomenderos 275</div>
    </div>
  );
};

const Papel: React.FC<{mascara: string; children: React.ReactNode}> = ({mascara, children}) => (
  <div style={{position: "absolute", left: 0, top: 0, width: FOTO.w, height: FOTO.h,
    WebkitMaskImage: `url(${m(mascara)})`, WebkitMaskSize: "100% 100%", maskImage: `url(${m(mascara)})`,
    maskSize: "100% 100%"}}>{children}</div>
);

const FOTO_SRC = staticFile("assets/hilton/qb/oct/21-mano-dos.jpg");
const FUNDE = "linear-gradient(to right, transparent 0, #000 160px), linear-gradient(to bottom, transparent 0, #000 160px)";

export const QbSt21Estacionamiento: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    {/* fondo: la misma foto, desenfocada, a sangre */}
    <Img src={FOTO_SRC} style={{position: "absolute", left: -60, top: -80, width: FOTO.w + 120, height: FOTO.h + 120,
      filter: "blur(22px) brightness(0.85)"}} />
    {/* mano + ticket al 85 %, anclados abajo a la derecha; `zoom` para que el texto no se ablande */}
    <div style={{position: "absolute", width: FOTO.w, height: FOTO.h, zoom: S,
      left: (MESA_W - FOTO.w * S) / S, top: (1932 - FOTO.h * S) / S}}>
      <Img src={FOTO_SRC} style={{position: "absolute", left: 0, top: 0, width: FOTO.w, height: FOTO.h,
        WebkitMaskImage: FUNDE, WebkitMaskComposite: "source-in", maskImage: FUNDE, maskComposite: "intersect"}} />
      {/* la tinta sólo donde hay papel: el pulgar y el ticket de adelante quedan encima */}
      <Papel mascara="atras"><Tinta t={ATRAS} opacidad={0.88} /></Papel>
      <Papel mascara="frente"><Tinta t={FRENTE} /></Papel>
    </div>
    <Velo arriba={[640, 0.7]} abajo={[440, 0.75]} />
    <LogoQB top={252} ancho={130} />
    <Linea top={356} cuerpo={70} peso={800} tracking="0.01em">{QB_ST21_DATA.pieza.titular}</Linea>
    <Linea top={448} cuerpo={34} peso={400} ancho={880}>{QB_ST21_DATA.pieza.bajada}</Linea>
    {/* r8: el legal en dos líneas, alineado a la izquierda */}
    <div style={{position: "absolute", left: 72, top: 1506, color: "rgba(255,255,255,.85)", fontFamily: "Raleway",
      fontStyle: "italic", fontSize: 20, lineHeight: 1.35, textAlign: "left"}}>
      *Imagen referencial.<br />Solicita tu ticket a nuestro personal.
    </div>
  </AbsoluteFill>
);
