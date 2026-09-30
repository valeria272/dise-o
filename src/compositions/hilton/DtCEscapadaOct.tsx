/**
 * DOUBLETREE · FEED 07-10-2026 12:00 · CARRUSEL – ESCAPADA ROMÁNTICA (atemporal).
 * Estado de la grilla (28-09 20:08Z, Carlos): OK PARA DISEÑO. Los dos comentarios de
 * diseño («No lo dejaría taan romántico…» y «…que sea atemporal») ya los resolvió
 * contenido en el brief: el titular pasó a «Un break de fin de semana sin salir de
 * la ciudad» y el post no nombra el feriado. De ahí R-74: ESCAPARSE, no noche de bodas.
 *
 * ── La referencia (pin 932315560378216027) ────────────────────────────────
 * REF 1 (el pin): pareja brindando junto al ventanal, relajada, nada nupcial. Antetítulo
 * chico en versales espaciadas (~25 % del alto), titular GRANDE centrado debajo, la
 * escena limpia al medio y abajo una PÍLDORA de contorno con una línea de texto.
 * REF 2 (la otra lámina de la misma cuenta, en el mismo pin): foto oscurecida pareja,
 * antetítulo arriba, titular grande centrado y una TABLA de filas separadas por
 * filetes finos a lo ancho, en columnas. Es la lámina «Personaliza tu experiencia».
 * Tipografía y color siguen siendo DT (R-15): Stag a dos pesos y mismo cuerpo en el
 * titular (R-04), versales y cifras en Trade, blanco sobre velo azul DT (R-13).
 *
 * Firma una vez (R-11): logo sólo en la portada, que es programa (R-10). Portada y
 * lámina 2 se contestan con el mismo antetítulo (R-77). Sin punto en títulos ni
 * bajadas (R-60); el legal conserva el suyo. Precio vigente (R-28).
 */
import React from 'react';
import {AbsoluteFill} from 'remotion';

import {DT, cargarFuentesDT} from '../../brand/doubletree';
import {Foto, Logo, SOMBRA, Stag, TRADE_CN, Velo} from './dtOct2';

cargarFuentesDT();

const BLANCO = DT.colores.blanco;
const AZUL = DT.colores.azul;
const M = DT.geometria.margenLateral;

const Antetitulo: React.FC<{top: number}> = ({top}) => (
  <div
    style={{
      position: 'absolute',
      top,
      left: 0,
      width: 1080,
      textAlign: 'center',
      fontFamily: DT.fuentes.texto,
      // RONDA 5 (Constanza, 29-09): «que cada tipografía esté más junta, ese recurso no lo usas en DT»
      fontSize: 30,
      letterSpacing: '0.03em',
      color: BLANCO,
      textShadow: SOMBRA,
    }}
  >
    ESCAPADA ROMÁNTICA
  </div>
);

/** El ✔ del brief, dibujado (Stag y Trade no lo traen). */
const Check: React.FC = () => (
  <svg width={26} height={20} viewBox="0 0 26 20" style={{flexShrink: 0, filter: 'drop-shadow(0 1px 2px rgba(9,25,78,0.5))'}}>
    <path d="M2 10.5 L9.5 17.5 L24 2.5" fill="none" stroke={BLANCO} strokeWidth="2.6" strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

const INCLUYE = ['Habitación para 2 personas', 'Desayuno buffet', 'Espumante de bienvenida'];

// ═══════════════════════════════════════════════════════════════════════════
// 1 · PORTADA
// ═══════════════════════════════════════════════════════════════════════════
const Portada: React.FC<{foto: string}> = ({foto}) => (
  <>
    <Foto src={foto} />
    <Velo desde={0.5} pie={0.72} lado="arriba" />
    <Velo desde={0.5} pie={0.9} />

    <Logo formato="feed" />

    {/* RONDA 3 (Eli, 29-09): «están muy juntos los textos… cuando se trata de stack»: interlínea 1,3.
        RONDA 5 (Constanza, 29-09): «el interlineado entre un break… y sin salir… que sea menos, se ve muy
        separado» → 1,16, a medio camino: no vuelve al 1,10 que Eli encontró apretado. */}
    <Antetitulo top={290} />
    <div style={{position: 'absolute', top: 342, left: 0, width: 1080, textAlign: 'center', color: BLANCO}}>
      {[
        {t: 'Un break de fin de semana', w: DT.pesos.semibold},
        {t: 'sin salir de la ciudad', w: DT.pesos.light},
      ].map((l) => (
        <div
          key={l.t}
          style={{fontFamily: DT.fuentes.titular, fontWeight: l.w, fontSize: 64, lineHeight: 1.16, textShadow: SOMBRA, whiteSpace: 'nowrap'}}
        >
          <Stag t={l.t} />
        </div>
      ))}
    </div>

    {/* el programa, abajo y centrado (R-79): precio, lo que incluye y la píldora de la ref con la dirección */}
    <div style={{position: 'absolute', bottom: 36, left: 0, width: 1080, textAlign: 'center', color: BLANCO}}>
      {/* RONDA 2 (Eli, 29-09): «el desde que quede arriba, para que eso quede centrado» */}
      <div style={{fontFamily: DT.fuentes.texto, fontSize: 24, letterSpacing: '0.04em', marginBottom: 4, textShadow: SOMBRA}}>Desde</div>
      <span
        style={{
          display: 'inline-block',
          background: BLANCO,
          color: AZUL,
          borderRadius: 60,
          padding: '8px 30px 4px',
          fontFamily: TRADE_CN,
          fontWeight: 700,
          fontSize: 56,
          lineHeight: 1,
        }}
      >
        $99.000
      </span>
      <div style={{marginTop: 8, fontFamily: DT.fuentes.texto, fontSize: 21, letterSpacing: '0.03em', textShadow: SOMBRA}}>
        IVA INCLUIDO
      </div>

      <div style={{marginTop: 16, display: 'flex', justifyContent: 'center', gap: 30}}>
        {INCLUYE.map((x) => (
          <div key={x} style={{display: 'flex', alignItems: 'center', gap: 11}}>
            <Check />
            <span
              style={{
                fontFamily: DT.fuentes.titular,
                fontWeight: DT.pesos.regular,
                fontSize: 23,
                wordSpacing: '0.06em',
                textShadow: SOMBRA,
                whiteSpace: 'nowrap',
              }}
            >
              {x}
            </span>
          </div>
        ))}
      </div>

      <div
        style={{
          display: 'inline-block',
          marginTop: 18,
          border: `2px solid ${BLANCO}`,
          borderRadius: 999,
          padding: '11px 40px 8px',
          fontFamily: DT.fuentes.texto,
          fontSize: 28,
          letterSpacing: '0.03em',
          wordSpacing: '0.1em',
          textShadow: SOMBRA,
        }}
      >
        Av. Vitacura 2727, Las Condes
      </div>
    </div>
  </>
);

// ═══════════════════════════════════════════════════════════════════════════
// 2 · PERSONALIZA TU EXPERIENCIA
// ═══════════════════════════════════════════════════════════════════════════
const FILAS = [
  // RONDA 3 (Eli, 29-09): los beneficios son un PUNTEO y llevan punto final («cuando son textos extensos, que son
  // punteos de los beneficios, esos sí van con puntos»; R-60 es para titulares y bajadas). Y «+$100.000», como «+$21.000».
  {que: ['Agrega', 'sunset'], precio: '+$21.000', det: [['Una entrada (fría o caliente,', 'a elección) en QB Restaurant.'], ['Dos tragos seleccionados.']]},
  {que: ['Agrega', 'masajes'], precio: '+$100.000', det: [['Dos masajes de 60 minutos.'], ['Valor preferencial con tu reserva.']]},
] as const;

const COL = {que: 250, precio: 230} as const;
const FILETE = '1.5px solid rgba(250,250,250,0.7)';

const Personaliza: React.FC<{foto: string}> = ({foto}) => (
  <>
    <Foto src={foto} />
    <AbsoluteFill style={{background: 'rgba(9,25,78,0.5)'}} />
    <Velo desde={0.0} pie={0.25} lado="arriba" />

    {/* RONDA 2 (Eli, 29-09): en la lámina 2 va el NOMBRE DEL PROGRAMA con su forma de siempre, como
        Family Time: Stag itálica a dos pesos (la del FEED 28-10 aprobado), no el antetítulo en versales. */}
    <div
      style={{
        position: 'absolute',
        top: 118,
        left: 0,
        width: 1080,
        textAlign: 'center',
        color: BLANCO,
        fontFamily: DT.fuentes.titular,
        fontStyle: 'italic',
        fontSize: 92,
        lineHeight: 1,
        textShadow: SOMBRA,
        whiteSpace: 'nowrap',
      }}
    >
      <span style={{fontWeight: DT.pesos.semibold}}>Escapada</span>
      <span style={{fontWeight: DT.pesos.light}}> Romántica</span>
    </div>
    <div
      style={{
        position: 'absolute',
        top: 262,
        left: 0,
        width: 1080,
        textAlign: 'center',
        color: BLANCO,
        fontFamily: DT.fuentes.titular,
        fontSize: 58,
        lineHeight: 1.28,
        textShadow: SOMBRA,
      }}
    >
      <div style={{fontWeight: DT.pesos.semibold}}>Personaliza</div>
      <div style={{fontWeight: DT.pesos.light}}>tu experiencia</div>
    </div>

    <div style={{position: 'absolute', top: 460, left: M, right: M, color: BLANCO, borderTop: FILETE}}>
      {FILAS.map((f) => (
        <div key={f.precio} style={{display: 'flex', alignItems: 'center', padding: '40px 0 36px', borderBottom: FILETE}}>
          <div
            style={{
              width: COL.que,
              textAlign: 'center',
              fontFamily: DT.fuentes.titular,
              fontSize: 44,
              lineHeight: 1.28,
              fontWeight: DT.pesos.medium,
              textShadow: SOMBRA,
            }}
          >
            {/* RONDA 3 (Eli, 29-09): «agregar sunset y agregar masaje, tengan el mismo peso» */}
            <div>{f.que[0]}</div>
            <div>{f.que[1]}</div>
          </div>
          <div
            style={{
              width: COL.precio,
              textAlign: 'center',
              fontFamily: TRADE_CN,
              fontWeight: 700,
              fontSize: 56,
              lineHeight: 1,
              textShadow: SOMBRA,
            }}
          >
            {f.precio}
          </div>
          <div style={{flex: 1, paddingLeft: 10}}>
            {f.det.map((d, i) => (
              <div
                key={d[0]}
                style={{
                  marginTop: i ? 14 : 0,
                  display: 'flex',
                  fontFamily: DT.fuentes.titular,
                  fontWeight: DT.pesos.regular,
                  fontSize: 25,
                  lineHeight: 1.36,
                  wordSpacing: '0.08em',
                  textShadow: SOMBRA,
                }}
              >
                <span style={{width: 22, flexShrink: 0}}>•</span>
                <div>
                  {d.map((x) => (
                    <div key={x}>{x}</div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>

    <div
      style={{
        position: 'absolute',
        bottom: 96,
        left: 0,
        width: 1080,
        textAlign: 'center',
        fontFamily: DT.fuentes.texto,
        fontSize: 24,
        lineHeight: 1.4,
        // R-132 (Constanza, 29-09: «tipografías separadas en cada palabra»): menos aire entre palabras
        wordSpacing: '0.03em',
        color: BLANCO,
        textShadow: SOMBRA,
      }}
    >
      Disponible noches de jueves a domingo y festivos.
      <br />
      Sujeto a disponibilidad.
    </div>
  </>
);

/** `lamina` 1 portada · 2 personaliza. `foto` permite probar variantes de la generación. */
export const DtCEscapadaOct: React.FC<{lamina: number; foto?: string}> = ({lamina, foto}) => (
  <AbsoluteFill style={{backgroundColor: AZUL}}>
    {lamina === 1 ? (
      <Portada foto={foto ?? 'assets/hilton/dt/oct3/er-portada.jpg'} />
    ) : (
      // RONDA 6 (Scarlette, hilo FEED!C14, 30-09): «la 2da slide es la más débil por las copas (no tenemos con
      // mango rosado) y el plato (pongamos imagen de algún producto de QB, esos panes no se encuentran en la carta)»
      // → sale la foto generada; entra la foto REAL de la carta de QB (sesión que pasó Eli el 25-09, «Ostiones
      // parmesanos a la batayaki 20»: brindis con las copas de la casa sobre los ostiones y la trucha).
      <Personaliza foto={foto ?? 'assets/hilton/dt/oct3/er-sunset-qb-real.jpg'} />
    )}
  </AbsoluteFill>
);
