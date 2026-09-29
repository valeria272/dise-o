/**
 * QB · ST 09-10 · 15:00 · ESTÁTICA — SUNSET QB
 *
 * BRIEF (STORIES col. G, OK PARA DISEÑAR, sin comentario):
 *   Un cocktail protagonista en primer plano, muy bien iluminado por la luz del
 *   atardecer, atmósfera cálida y sofisticada. En segundo plano personas
 *   compartiendo desenfocadas. Golden hour, look más lifestyle que promocional.
 *   Texto: EL VIERNES CAMBIA DE MOOD. DE 16:00 A 21:00, · SUNSET QB · Cocktails
 *   seleccionados al mejor precio. · Bajada: Tu after office, a otro nivel.
 *
 * REFERENCIA: Pinterest 1025976358870898225 (Moksi) — trago sobre mesa de
 * madera con luz de tarde.
 *
 * ⭐⭐ RONDA DE ELI 25-09: «usa tal cual la pieza gráfica seleccionada, sólo
 * cambia los textos que agrega el brief, pero el logo de Sunset QB déjalo tal
 * cual» · «no se parece a nada a la ya aprobada».
 * ⇒ La base es la ST aprobada de agosto (Drive «POST + ST SUNSET PROMO QB /
 *   St n° 1 QB SUNSET.png»):
 *   · FOTO: la del KV, sin texto, sacada del PDF de «Promo Sunset QB digital»
 *     (imagen 1728×2304) con el MISMO encuadre de la ST aprobada.
 *   · LOGO «Sunset QB»: el vectorial de ese PDF, exportado tal cual
 *     (`sunset-qb-logo.png`), en el lugar y tamaño de la ST aprobada.
 *   · TEXTOS: donde la aprobada decía «TUS FAVORITOS / AL MEJOR PRECIO» va el
 *     titular del brief, en la misma Raleway Regular y el mismo cuerpo; la
 *     pastilla verde en el mismo lugar con el horario; debajo, las dos líneas
 *     que el brief agrega. Sólo Raleway.
 *   · El legal sube a la zona segura de Instagram (en la aprobada estaba a 74 px
 *     del borde).
 *   · PROMO → zona segura de paid. Títulos sin punto (regla Hilton §F).
 *
 * ⭐ RONDA DE ELI 28-09: «Tu after office a otro nivel lo encuentro extraño: aumenta
 *   un poco el tamaño, y las dos F de office sepáralas, se ven muy juntas» · «el
 *   viernes cambia de mood: que se vea más similar a la de referencia». La bajada
 *   pasa de 32 a 38 sin ligadura; el titular va en Raleway LIGHT (300) como
 *   «TUS FAVORITOS / AL MEJOR PRECIO» de la aprobada, no Regular.
 *
 * ⭐ RONDA 4 DE ELI 28-09: «modificar ciertas cosas para que se vea como lo que
 *   ellos solicitan y la referencia, manteniendo Sunset QB como título, que eso sí
 *   tiene que quedar tal cual». Lo que se toma de la ref (Moksh):
 *   · FOTO de hora dorada sobre mesa de madera: el trago protagonista a
 *     contraluz, un plato para compartir abajo y, detrás, gente compartiendo
 *     DESENFOCADA (lo que pedía el brief y quedó pendiente por créditos el 24-09).
 *     Generada → «Imagen referencial».
 *   · RÓTULO A MANO con flecha que señala el trago (en la ref, «Margarita»): acá
 *     dice lo que el brief ya trae, «Cocktails seleccionados al mejor precio», en
 *     Brushwell.
 *   · TITULAR serif en caja alta + una palabra caligráfica, como «READY TO BECOME
 *     your FAVORITE!»: «EL VIERNES» y «MOOD» en Bell MT, «cambia de» en Brushwell.
 *   · El logo «Sunset QB» no se toca: mismo archivo, lugar y tamaño.
 *
 * ⭐ RONDA 6 DE ELI 28-09: «el legal no se ve nada, auméntalo un poco… cuidando los
 *   márgenes de Instagram y paid» y «oscurece un poco hacia arriba para leer
 *   Sunset QB». Legal de 14 a 19 (el bloque de abajo sube 30 px para que cierre
 *   en 1580); velo de arriba de 560 px al 45 % a 820 px al 80 %.
 *
 * ⭐ RONDA DE CONSTANZA (jefa de diseño, grilla 29-09): «aquí en la letra chica se
 *   ve raro con la palabra beneficios solita abajo, porfis no debemos palabras
 *   solitas» → el legal se corta por frase en dos líneas parejas:
 *   «*Imagen referencial. *Sujeto a consumo de alimentos.» /
 *   «*Promoción no acumulable con otras ofertas y beneficios.» Mismo cuerpo y lugar.
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {BotonVerde, cargarFuentesQbOct, FotoQB, Legal, Linea, MESA, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const QB_ST09_DATA: Record<string, Record<string, string>> = {
  pieza: {
  titular: "EL VIERNES CAMBIA DE MOOD",
  medida: "DE 16:00 A 21:00 HRS",
  texto: "Cocktails seleccionados al mejor precio",
  bajada: "Tu after office, a otro nivel",
  legal: "*Imagen referencial. *Sujeto a consumo de alimentos.",
  legal2: "*Promoción no acumulable con otras ofertas y beneficios.",
  },
};

/** Logo «Sunset QB» de la pieza aprobada: 767 px de ancho y tope en 346 (mesa). */
const LOGO_W = 767;
const LOGO_H = LOGO_W * 576 / 2556;

/** La foto sube para que el trago quede entre el logo y el bloque de abajo. */
const SUBE = -300;

export const QbSt09Sunset: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/09-sunset-r4.jpg" ratio={1520 / 2736} libre bajar={SUBE} />
    {/* el canto de abajo de la foto (sube 300 px) se funde a negro */}
    <div style={{position: "absolute", left: 0, right: 0, top: 1380, height: 1920 - 1380,
      background: "linear-gradient(180deg, rgba(0,0,0,0) 0%, #000 45%, #000 100%)"}} />
    {/* r6 (Eli): más oscuro arriba para leer «Sunset QB» */}
    <Velo arriba={[820, 0.8]} abajo={[900, 0.85]} />
    <Img src={staticFile("assets/hilton/qb/oct/sunset-qb-logo.png")}
      style={{position: "absolute", top: 346, left: (MESA.w - LOGO_W) / 2, width: LOGO_W, height: LOGO_H}} />
    {/* rótulo a mano con flecha hacia el trago, como «Margarita» en la ref */}
    <div style={{position: "absolute", left: 70, top: 742, width: 440, textAlign: "center", color: "#fff",
      fontFamily: "Brushwell", fontSize: 62, lineHeight: 0.98, textShadow: "0 2px 16px rgba(0,0,0,.5)"}}>
      Cocktails seleccionados<br />al mejor precio
    </div>
    <svg style={{position: "absolute", left: 0, top: 0}} width={MESA.w} height={MESA.h}>
      <path d="M 300 880 C 320 960, 420 990, 525 962" fill="none" stroke="#fff" strokeWidth={4.5} strokeLinecap="round" />
      <path d="M 498 940 L 528 961 L 500 986" fill="none" stroke="#fff" strokeWidth={4.5} strokeLinecap="round" strokeLinejoin="round" />
    </svg>
    {/* titular como la ref: serif en caja alta + una palabra caligráfica */}
    <Linea top={1176} cuerpo={66} familia="BellMT" tracking="0.04em">EL VIERNES</Linea>
    <Linea top={1222} cuerpo={104} familia="Brushwell" interlinea={1}>cambia de</Linea>
    <Linea top={1304} cuerpo={112} familia="BellMT" tracking="0.03em" interlinea={1}>MOOD</Linea>
    <BotonVerde top={1420} ancho={520} alto={54} cuerpo={30} peso={700}>{QB_ST09_DATA.pieza.medida}</BotonVerde>
    <Linea top={1480} cuerpo={34} peso={400} italica>
      {/* sin la ligadura «ff» y con aire entre las dos f (Eli 28-09: «se ve muy junto») */}
      <span style={{fontVariantLigatures: "none"}}>Tu af<span style={{marginLeft: "0.06em"}}>ter</span> of<span style={{marginLeft: "0.07em"}}>f</span>ice, a otro nivel</span>
    </Linea>
    {/* r6 (Eli): «aumenta un poco el tamaño de los legales… no se ve nada». De 14 a 19,
        en dos líneas que cierran en y≈1578, al borde de la zona segura de paid (1580) */}
    <Legal top={1526} cuerpo={19}>{QB_ST09_DATA.pieza.legal}<br />{QB_ST09_DATA.pieza.legal2}</Legal>
  </AbsoluteFill>
);
