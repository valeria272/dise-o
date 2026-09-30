/**
 * QB · ST 09-10 · SUNSET — VERSIÓN 2 (alternativa a la r28 aprobada, 30-09-2026)
 *
 * PEDIDO DE ELI (30-09): «lo más similar [a la imagen de Magnific] pero con un solo
 * cóctel, el del centro, que destaque» · «una copia del anterior para ver el antes y
 * el después» · para mostrársela a contenido. La r28 (`QbSt09Sunset`) NO se toca.
 *
 * FOTO: «AA — v7 Post 3:4» del Space de Magnific de Eli (Drive 19oeR1nnv77…),
 *   1728×2304 → `raw/hilton/qb/sunset-v2/`.
 *   1. Nano Banana Pro: fuera la flauta de espumante y el mojito (con sombras y
 *      charcos); el spritz, la mesa y la terraza, iguales.
 *   2. Se «aleja la cámara»: la foto al 85 % en un lienzo 9:16 y outpainting de
 *      pérgola + lámparas arriba y la MISMA mesa vacía abajo.
 *   3. Sobre la extensión se vuelve a pegar el paso 1 (borde difuminado 180 px),
 *      para que el spritz sea el de Magnific y no el re-renderizado.
 *   ⇒ «Imagen referencial» en el legal, como en la r28.
 *
 * TEXTOS, logo, botón y legal: los de la r28, mismas voces (Raleway + «mood» en
 * Brushwell). Cambia sólo la geometría que manda la foto nueva:
 *   · el trago está al CENTRO (x≈410–665, y≈643–1373) → el rótulo «Cocktails… DESDE
 *     $3.990» va a la izquierda, a la altura de la copa, y la flecha llega a su borde;
 *   · el pie de la copa termina en y≈1373 → el bloque de texto baja 20 px más que en
 *     la r28 (título a 1410). Legal al pie de historia (1748).
 *
 * ⭐ RONDA 1 DE ELI (30-09): «Cocktails seleccionados al mejor precio no se ve: deja una
 *   cajita oscurecida o una transparencia detrás, que sea sutil» → caja negra al 38 % con
 *   un desenfoque leve del fondo, sólo detrás del rótulo. «De 16 a 21 hrs tiene demasiado
 *   sobrante de caja: que llegue hasta donde corta "Tu after office, a otro nivel"…
 *   eso es regla para todos» → el botón mide lo que mide la bajada (392 px, medido
 *   sobre el render), no 520.
 */
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";

import {BotonVerde, cargarFuentesQbOct, CIFRAS, FotoQB, Legal, Linea, MESA, Velo} from "./QbOctKit";

cargarFuentesQbOct();

const DATA = {
  medida: "DE 16:00 A 21:00 HRS",
  precio: "DESDE $3.990",
  legal: "*Imagen referencial. *Sujeto a consumo de alimentos.",
  legal2: "*Promoción no acumulable con otras ofertas y beneficios.",
};

const LOGO_W = 767;
const LOGO_H = LOGO_W * 576 / 2556;
const BAJA_TEXTO = 214;
/** r1 (Eli, regla para todas): el botón llega hasta donde corta la bajada de abajo. */
const BAJADA_W = 392;

export const QbSt09SunsetV2: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <FotoQB src="assets/hilton/qb/oct/09-sunset-v2.jpg" ratio={3072 / 5504} libre bajar={0} />
    <Velo arriba={[900, 0.7]} abajo={[1000, 0.55]} />

    <Img src={staticFile("assets/hilton/qb/oct/sunset-qb-logo.png")}
      style={{position: "absolute", top: 346, left: (MESA.w - LOGO_W) / 2, width: LOGO_W, height: LOGO_H}} />
    {/* r1 (Eli): cajita translúcida sutil detrás del rótulo, para que se lea sobre las luces */}
    <div style={{position: "absolute", left: 24, top: 690, width: 372, padding: "16px 0 18px", textAlign: "center",
      color: "#fff", fontFamily: "Raleway", background: "rgba(10,7,5,0.38)",
      backdropFilter: "blur(6px)", textShadow: "0 2px 10px rgba(0,0,0,.4)"}}>
      <div style={{fontSize: 32, fontWeight: 400, fontStyle: "italic", lineHeight: 1.15}}>Cocktails seleccionados<br />al mejor precio</div>
      <div style={{fontSize: 50, fontWeight: 800, letterSpacing: "0.02em", lineHeight: 1, marginTop: 12, ...CIFRAS}}>{DATA.precio}</div>
    </div>
    <svg style={{position: "absolute", left: 0, top: 0}} width={MESA.w} height={MESA.h}>
      <path d="M 230 892 C 240 955, 300 988, 395 975" fill="none" stroke="#fff" strokeWidth={4.5} strokeLinecap="round" />
      <path d="M 368 955 L 397 975 L 370 997" fill="none" stroke="#fff" strokeWidth={4.5} strokeLinecap="round" strokeLinejoin="round" />
    </svg>
    <Linea top={1196 + BAJA_TEXTO} cuerpo={56} peso={300} tracking="0.06em">EL VIERNES CAMBIA</Linea>
    <Linea top={1246 + BAJA_TEXTO} cuerpo={140} familia="Brushwell" interlinea={1}>de mood</Linea>
    <BotonVerde top={1420 + BAJA_TEXTO} ancho={BAJADA_W} alto={54} cuerpo={30} peso={700}>{DATA.medida}</BotonVerde>
    <Linea top={1480 + BAJA_TEXTO} cuerpo={34} peso={400} italica>
      <span style={{fontVariantLigatures: "none"}}>Tu af<span style={{marginLeft: "0.06em"}}>ter</span> of<span style={{marginLeft: "0.07em"}}>f</span>ice, a otro nivel</span>
    </Linea>
    <Legal top={1748} cuerpo={19}>{DATA.legal}<br />{DATA.legal2}</Legal>
  </AbsoluteFill>
);
