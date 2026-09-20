/**
 * Guiones de los tres reels de octubre 2026 · Colegio San Esteban
 *
 * Los textos en pantalla salen VERBATIM de la columna «TEXTO SOBRE LA IMAGEN»
 * del brief (`San Esteban - Brief Performance - Octubre 2026.xlsx`), con una sola
 * excepción registrada: donde el brief escribió «más de 100 años» va «110 años»
 * — decidido el 07-09-2026 para no contradecir las piezas aprobadas de
 * septiembre ni el sello de aniversario.
 *
 * Las fotos son de la sesión publicitaria propia del colegio, publicada en
 * hssanesteban.cl (sitio del cliente).
 */
import type {Escena} from "./SanEstebanReel";

/** Pieza 02 · Reel 15 s · Tráfico web */
export const REEL_TRAFICO: Escena[] = [
  {foto: "SE-frontis", encuadre: 42, texto: "110 años de trayectoria en Antofagasta"},
  {foto: "SE-58", encuadre: 60, encuadreY: 5, texto: "Entre los mejores puntajes PAES de la región"},
  {foto: "SE-93", encuadre: 40, texto: "Una comunidad que trasciende el aula"},
  {foto: "SE-abril55", encuadre: 46, encuadreY: 12, cierre: true,
   texto: "Conoce más en nuestro sitio web", cta: "Infórmate en nuestro sitio web"},
];

/** Pieza 05 · Reel 15 s · WhatsApp Antofagasta — Admisión 2027 */
export const REEL_WSP_ANTOFAGASTA: Escena[] = [
  {foto: "SE-54", encuadre: 40, texto: "Admisiones 2027 ya están abiertas"},
  {foto: "SE-58", encuadre: 60, encuadreY: 5, texto: "Entre los mejores puntajes PAES de la región"},
  {foto: "SE-abril55", encuadre: 46, texto: "110 años formando líderes"},
  {
    foto: "SE-93",
    encuadre: 40,
    encuadreY: 18,
    cierre: true,
    texto: "Conversemos por WhatsApp",
    cta: "Escríbenos por WhatsApp",
  },
];

/**
 * Pieza 08 · Reel 15 s · WhatsApp Santiago/Iquique/Calama/La Serena
 *
 * ⚠️ La escena 1 del brief pide «familia haciendo mudanza, cajas» y ese material
 * NO existe: se usa la foto de familia de la sesión del colegio y queda anotado
 * como pendiente en ENTREGA.md.
 */
export const REEL_MUDANZA: Escena[] = [
  {foto: "SE-14", encuadre: 46, texto: "¿Te mudas a Antofagasta el 2027?"},
  {foto: "SE-frontis", encuadre: 42, texto: "San Esteban te espera"},
  {foto: "SE-58", encuadre: 60, encuadreY: 5, texto: "110 años de excelencia académica"},
  {
    foto: "SE-09",
    encuadre: 20,
    cierre: true,
    texto: "Asegura el cupo de tu hijo antes de mudarte",
    cta: "Escríbenos por WhatsApp",
  },
];
