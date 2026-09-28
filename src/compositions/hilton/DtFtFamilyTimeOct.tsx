/**
 * DOUBLETREE · FEED 28-10-2026 12:00 · ESTÁTICO – FAMILY TIME (PRIMAVERA).
 * Estado de la grilla (28-09): OK PARA DISEÑO.
 * Comentario para diseño: «Cambiemos título por Los mejores momentos en familia
 * están más cerca de lo que imaginas» (ya aplicado en la celda del brief).
 *
 * ── La referencia (pin 1114781714025373211) ──────────────────────────────
 * Foto de habitación a sangre, con techo libre arriba; el titular va ARRIBA A LA
 * DERECHA, alineado a la derecha, a dos pesos (la línea de arriba gruesa, la de
 * abajo liviana) y a cuerpo moderado. El resto de la foto queda limpia.
 * Se toma eso tal cual. El logotipo NO va abajo como en la ref: va en su posición
 * de plantilla (`logo-post.png`, tope 111) porque abajo vive el bloque del programa.
 *
 * ── La foto ───────────────────────────────────────────────────────────────
 * Familia fija del banco aprobado el 25-09 (R-68/R-69): la guerra de almohadas en
 * la habitación de dos camas, fondo real de DT. Es la escena con más techo libre.
 *
 * ── El bloque del programa ────────────────────────────────────────────────
 * El de `C1 FT N2` (aprobado, sept): «Family Time» en Stag itálica a dos pesos,
 * precio en píldora blanca + «IVA INCLUIDO», los tres íconos de Eli con filete,
 * el correo en píldora de contorno y el legal. Precio del carrusel vigente (R-28).
 * Titular sin punto (R-60); el legal conserva el suyo.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';

import {DT, cargarFuentesDT} from '../../brand/doubletree';
import {ConTrade} from './dtIconosOct';
import {Foto, Logo, SOMBRA, TRADE_CN, Velo} from './dtOct2';

cargarFuentesDT();

const BLANCO = DT.colores.blanco;
const AZUL = DT.colores.azul;

const INCLUIDOS = [
  {icono: 'assets/hilton/dt/icono-cama-eli.png', prop: 147 / 120, l: ['Habitación', 'doble']},
  {icono: 'assets/hilton/dt/oct/icono-familia-eli.png', prop: 124 / 114, l: ['2 adultos + 2 niños', 'hasta 12 años']},
  {icono: 'assets/hilton/dt/oct/icono-buffet-eli.png', prop: 130 / 120, l: ['Desayuno', 'buffet']},
] as const;

export const DtFtFamilyTimeOct: React.FC<{tinta?: 'blanco' | 'azul'}> = ({tinta = 'blanco'}) => {
  const colorTit = tinta === 'blanco' ? BLANCO : AZUL;
  return (
    <AbsoluteFill style={{backgroundColor: AZUL}}>
      <Foto src="assets/hilton/dt/oct2/ft-feed.jpg" />
      <Velo desde={0.32} pie={0.34} lado="arriba" />
      <Velo desde={0.5} pie={0.92} />

      <Logo formato="feed" />

      {/* titular arriba a la derecha, alineado a la derecha como la ref */}
      <div style={{position: 'absolute', top: 290, right: DT.geometria.margenLateral, textAlign: 'right'}}>
        {[
          {t: 'Los mejores momentos en familia', w: DT.pesos.semibold},
          {t: 'están más cerca de lo que imaginas', w: DT.pesos.light},
        ].map((l) => (
          <div
            key={l.t}
            style={{
              fontFamily: DT.fuentes.titular,
              fontWeight: l.w,
              fontSize: 47,
              lineHeight: 1.2,
              color: colorTit,
              textShadow: tinta === 'blanco' ? SOMBRA : undefined,
              whiteSpace: 'nowrap',
            }}
          >
            {l.t}
          </div>
        ))}
      </div>

      {/* el bloque del programa, el de `C1 FT N2` */}
      <div style={{position: 'absolute', top: 872, left: 0, width: 1080, textAlign: 'center', color: BLANCO}}>
        <div style={{display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 30}}>
          <div style={{fontFamily: DT.fuentes.titular, fontStyle: 'italic', fontSize: 78, lineHeight: 1, textShadow: SOMBRA, whiteSpace: 'nowrap'}}>
            <span style={{fontWeight: DT.pesos.semibold}}>Family</span>
            <span style={{fontWeight: DT.pesos.light}}> Time</span>
          </div>
          <div style={{textAlign: 'center'}}>
            <div
              style={{
                background: BLANCO,
                color: AZUL,
                borderRadius: 60,
                padding: '8px 30px 4px',
                fontFamily: TRADE_CN,
                fontWeight: 700,
                fontSize: 60,
                lineHeight: 1,
              }}
            >
              $125.000
            </div>
            <div style={{marginTop: 8, fontFamily: DT.fuentes.texto, fontSize: 19, letterSpacing: '0.16em', textIndent: '0.16em', textShadow: SOMBRA}}>
              IVA INCLUIDO
            </div>
          </div>
        </div>

        <div style={{margin: '34px auto 0', width: 860, display: 'flex', justifyContent: 'space-between'}}>
          {INCLUIDOS.map((c, i) => (
            <React.Fragment key={c.icono}>
              {i > 0 ? <div style={{width: 1.5, alignSelf: 'stretch', background: 'rgba(250,250,250,0.55)'}} /> : null}
              <div style={{flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 16}}>
                <Img src={staticFile(c.icono)} style={{height: 54, width: 54 * c.prop}} />
                <div
                  style={{
                    textAlign: 'left',
                    fontFamily: DT.fuentes.titular,
                    fontWeight: DT.pesos.regular,
                    fontSize: 24,
                    lineHeight: 1.18,
                    wordSpacing: '0.08em',
                    textShadow: SOMBRA,
                    whiteSpace: 'nowrap',
                  }}
                >
                  {c.l.map((x) => (
                    <div key={x}>
                      <ConTrade t={x} />
                    </div>
                  ))}
                </div>
              </div>
            </React.Fragment>
          ))}
        </div>

        <div style={{marginTop: 38}}>
          <div
            style={{
              display: 'inline-block',
              border: `2px solid ${BLANCO}`,
              borderRadius: 60,
              padding: '11px 36px 8px',
              fontFamily: DT.fuentes.texto,
              fontSize: 34,
              lineHeight: 1,
              letterSpacing: '0.02em',
              textShadow: SOMBRA,
            }}
          >
            reservas.dtv@hilton.com
          </div>
        </div>
        <div style={{marginTop: 18, fontFamily: DT.fuentes.texto, fontSize: 21, letterSpacing: '0.01em', textShadow: SOMBRA}}>
          Válido jueves a domingo y festivos. Cupos limitados.
        </div>
      </div>
    </AbsoluteFill>
  );
};

