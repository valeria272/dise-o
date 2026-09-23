/**
 * Prueba de emoji — utilidad, no una pieza.
 *
 * El manual dice que «los emojis del sistema NO sirven en Windows: Chrome
 * resuelve `Segoe UI Emoji` y el ☕ sale LILA». Eso se cazó con el ☕, y de ahí
 * salió la regla de recortar los cuatro emojis de la lámina aprobada del
 * cliente. Pero **es una regla por glifo, no por fuente**: hay que comprobar
 * cada emoji nuevo antes de darlo por perdido.
 *
 * Rinde los candidatos grandes y sobre transparente para poder medirles el color.
 *   npx remotion still src/index.ts BW-Prueba-Emoji out/... --image-format=png
 */
import React from 'react';
import {AbsoluteFill} from 'remotion';

/**
 * ⭐ COMPROBADO el 09-09-2026 rindiendo los cuatro juntos: el 🌸 (U+1F338) sale
 * EN COLOR y correcto —flor de cerezo rosada—, mientras el ☘ y el 🏵 salen
 * NEGROS. O sea que la regla del manual («los emojis del sistema no sirven en
 * Windows, el ☕ sale lila») es **por GLIFO, no por fuente**: hay que probar
 * cada emoji nuevo antes de darlo por perdido.
 *
 * Queda sólo el 🌸, grande, para recortarlo por alfa y guardarlo en el kit.
 */
const CANDIDATOS = ['\u{1F338}'];

export const PruebaEmoji: React.FC = () => (
  <AbsoluteFill style={{flexDirection: 'row', alignItems: 'center', justifyContent: 'space-around'}}>
    {CANDIDATOS.map((e) => (
      <span key={e} style={{fontSize: 520, lineHeight: 1}}>{e}</span>
    ))}
  </AbsoluteFill>
);
