/**
 * DOUBLETREE · STORIES 05-10-2026 11:00 · las TRES historias del feriado.
 * Estado de la grilla (28-09): OK PARA DISEÑO. Venían del comentario del FEED 07-10:
 * «hagamos 3 historias genéricas de feriado, la primera que englobe a ER y FT, otra
 * solo de ER y otra solo de FT».
 *
 * ── 1 · ER + FT (col E) · `DtStFeriadoPlanes` ──────────────────────────────
 * Brief: «Pantalla dividida: pareja brindando / familia en el desayuno buffet».
 * Ref (pin 396809417192630029): foto a sangre, titular centrado arriba, una flecha
 * fina que baja y TARJETAS claras de resultado con miniatura a la izquierda. La
 * «pantalla dividida» del brief se resuelve con esas dos tarjetas, una por programa,
 * cada una con su foto: la pantalla se divide en dos planes.
 * Del buscador de la ref sólo se toma la tarjeta: la barra de búsqueda pediría un
 * texto que el brief no trae (R-01, no se escribe copy).
 * ⛔ «(confirmar tarifa vigente)» es una nota a contenido, no texto de la pieza.
 * ⛔ El countdown al 10-10 es sticker del CM: se deja el aire, no se dibuja.
 *
 * ── 2 y 3 · ER sola (col F) y FT sola (col G) · `DtStFeriadoPrograma` ──────
 * Las dos llevan la MISMA ref (pin 826832812880256665): panel vertical translúcido
 * a la izquierda sobre la foto de la habitación, titular arriba, la lista en
 * píldoras de contorno, un botón lleno y un pie con filete. Se traduce a DT: panel
 * azul DT macizo (α 0,84, como Family Time, E-08), titular Stag a dos pesos y mismo
 * cuerpo (R-04), versales y cifras en Trade, botón blanco con el correo.
 * ER: «Copas con espumante junto a la cama» → `HDT_65`, la habitación REAL con el
 *     montaje de Escapada (cubeta, copa y batas). Sin gente, como pide el brief.
 * FT: «Familia en la habitación o compartiendo el desayuno» → el desayuno del banco
 *     de la familia aprobado el 25-09 (R-68/R-69).
 *
 * Textos literales de la grilla; sin punto en títulos ni bajadas (R-60); el legal
 * conserva su punto. Precios del carrusel vigente (R-28).
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';

import {DT, cargarFuentesDT} from '../../brand/doubletree';
import {Foto, Logo, SOMBRA, Stag, TRADE_CN, Velo} from './dtOct2';

cargarFuentesDT();

const AZUL = DT.colores.azul;
const BLANCO = DT.colores.blanco;

const Guia: React.FC = () => (
  <>
    <div style={{position: 'absolute', top: 0, left: 0, width: 1080, height: DT.seguras.story.arriba, background: 'rgba(255,0,110,0.3)'}} />
    <div style={{position: 'absolute', bottom: 0, left: 0, width: 1080, height: DT.seguras.story.abajo, background: 'rgba(255,0,110,0.3)'}} />
  </>
);

// ═══════════════════════════════════════════════════════════════════════════
// 1 · ¿Fin de semana largo? — los dos planes
// ═══════════════════════════════════════════════════════════════════════════
const PLANES = [
  {quien: 'En pareja', programa: 'Escapada Romántica', precio: 'desde $99.000', foto: 'assets/hilton/dt/oct2/card-pareja.jpg'},
  {quien: 'En familia', programa: 'Family Time', precio: '$125.000', foto: 'assets/hilton/dt/oct2/card-familia.jpg'},
] as const;

const TARJETA = {x: 110, ancho: 860, alto: 250, radio: 34, foto: 206, y0: 930, paso: 290} as const;

const Flechita: React.FC = () => (
  <svg width={34} height={14} viewBox="0 0 34 14" style={{margin: '0 12px', transform: 'translateY(-2px)'}}>
    <line x1="0" y1="7" x2="30" y2="7" stroke={AZUL} strokeWidth="1.8" />
    <path d="M24 1.5 L33 7 L24 12.5" fill="none" stroke={AZUL} strokeWidth="1.8" strokeLinejoin="round" />
  </svg>
);

export const DtStFeriadoPlanes: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: AZUL}}>
    <Foto src="assets/hilton/dt/oct2/feriado-fondo-story.jpg" />
    {/* velo sólo arriba, para el titular blanco; abajo la ciudad queda limpia */}
    <Velo desde={0.4} pie={0.85} lado="arriba" />
    <Velo desde={0.62} pie={0.6} />

    <Logo formato="story" />

    <div style={{position: 'absolute', top: 480, left: 0, width: 1080, textAlign: 'center'}}>
      {[
        {t: '¿Fin de semana largo?', w: DT.pesos.medium},
        {t: 'Tenemos un plan', w: DT.pesos.light},
        {t: 'para cada uno', w: DT.pesos.light},
      ].map((l) => (
        <div
          key={l.t}
          style={{
            fontFamily: DT.fuentes.titular,
            fontWeight: l.w,
            fontSize: 70,
            lineHeight: 1.14,
            color: BLANCO,
            textShadow: SOMBRA,
            whiteSpace: 'nowrap',
          }}
        >
          <Stag t={l.t} />
        </div>
      ))}
      {/* la flecha fina de la ref, que baja a los planes */}
      <svg width={24} height={96} viewBox="0 0 24 96" style={{marginTop: 34, filter: 'drop-shadow(0 1px 3px rgba(9,25,78,0.5))'}}>
        <line x1="12" y1="0" x2="12" y2="92" stroke={BLANCO} strokeWidth="2" />
        <path d="M4 82 L12 94 L20 82" fill="none" stroke={BLANCO} strokeWidth="2" strokeLinejoin="round" />
      </svg>
    </div>

    {PLANES.map((p, i) => (
      <div
        key={p.programa}
        style={{
          position: 'absolute',
          left: TARJETA.x,
          top: TARJETA.y0 + i * TARJETA.paso,
          width: TARJETA.ancho,
          height: TARJETA.alto,
          borderRadius: TARJETA.radio,
          background: 'rgba(250,250,250,0.94)',
          boxShadow: '0 8px 28px rgba(9,25,78,0.22)',
          display: 'flex',
          alignItems: 'center',
          padding: `0 ${(TARJETA.alto - TARJETA.foto) / 2}px`,
          boxSizing: 'border-box',
        }}
      >
        <Img
          src={staticFile(p.foto)}
          style={{width: TARJETA.foto, height: TARJETA.foto, objectFit: 'cover', borderRadius: 22, flexShrink: 0}}
        />
        <div style={{marginLeft: 38, color: AZUL}}>
          <div style={{display: 'flex', alignItems: 'center'}}>
            <span style={{fontFamily: DT.fuentes.texto, fontSize: 24, letterSpacing: '0.16em', textTransform: 'uppercase'}}>
              {p.quien}
            </span>
            <Flechita />
          </div>
          <div style={{fontFamily: DT.fuentes.titular, fontWeight: DT.pesos.medium, fontSize: 50, lineHeight: 1.1, marginTop: 10, whiteSpace: 'nowrap'}}>
            {p.programa}
          </div>
          <div style={{fontFamily: TRADE_CN, fontWeight: 700, fontSize: 46, lineHeight: 1, marginTop: 12, letterSpacing: '0.01em'}}>
            {p.precio}
          </div>
        </div>
      </div>
    ))}

    <div
      style={{
        position: 'absolute',
        top: 1512,
        left: 0,
        width: 1080,
        textAlign: 'center',
        fontFamily: DT.fuentes.texto,
        fontSize: 25,
        letterSpacing: '0.02em',
        wordSpacing: '0.12em',
        color: BLANCO,
        textShadow: SOMBRA,
      }}
    >
      IVA incluido. Válido jueves a domingo y festivos.
    </div>

    {guia ? <Guia /> : null}
  </AbsoluteFill>
);

// ═══════════════════════════════════════════════════════════════════════════
// 2 y 3 · el programa solo, en panel vertical
// ═══════════════════════════════════════════════════════════════════════════
type Programa = {
  foto: string;
  focoX: string;
  titulo: {t: string; w: number}[];
  desde?: string;
  precio: string;
  incluye: string[];
};

const ER: Programa = {
  foto: 'assets/hilton/dt/oct2/er-hab-story.jpg',
  focoX: '62%',
  titulo: [
    {t: 'Este fin de', w: DT.pesos.medium},
    {t: 'semana largo,', w: DT.pesos.medium},
    {t: 'escápate', w: DT.pesos.light},
    {t: 'en pareja', w: DT.pesos.light},
  ],
  desde: 'Desde',
  precio: '$99.000',
  incluye: ['Habitación para 2 personas', 'Desayuno buffet', 'Espumante de bienvenida'],
};

const FT: Programa = {
  foto: 'assets/hilton/dt/oct2/ft-hab-story.jpg',
  focoX: '50%',
  titulo: [
    {t: 'Fin de semana', w: DT.pesos.medium},
    {t: 'largo en familia,', w: DT.pesos.medium},
    {t: 'sin salir', w: DT.pesos.light},
    {t: 'de Santiago', w: DT.pesos.light},
  ],
  precio: '$125.000',
  incluye: ['Habitación doble', '2 adultos + 2 niños hasta 12 años', 'Desayuno buffet'],
};

const PANEL = {x: 88, y: 470, ancho: 600, alto: 1090, radio: 44, pad: 54} as const;

export const DtStFeriadoPrograma: React.FC<{cual: 'er' | 'ft'; guia?: boolean}> = ({cual, guia = false}) => {
  const p = cual === 'er' ? ER : FT;
  const dentro = PANEL.ancho - PANEL.pad * 2;
  return (
    <AbsoluteFill style={{backgroundColor: AZUL}}>
      <Foto src={p.foto} style={{objectPosition: `${p.focoX} 50%`}} />
      <Velo desde={0.6} pie={0.4} lado="arriba" />

      <Logo formato="story" />

      <div
        style={{
          position: 'absolute',
          left: PANEL.x,
          top: PANEL.y,
          width: PANEL.ancho,
          height: PANEL.alto,
          borderRadius: PANEL.radio,
          background: 'rgba(9,25,78,0.84)',
          backdropFilter: 'blur(3.5px)',
          WebkitBackdropFilter: 'blur(3.5px)',
          padding: `${PANEL.pad + 6}px ${PANEL.pad}px ${PANEL.pad}px`,
          boxSizing: 'border-box',
          color: BLANCO,
          display: 'flex',
          flexDirection: 'column',
        }}
      >
        <div>
          {p.titulo.map((l) => (
            <div
              key={l.t}
              style={{fontFamily: DT.fuentes.titular, fontWeight: l.w, fontSize: 64, lineHeight: 1.12, whiteSpace: 'nowrap'}}
            >
              <Stag t={l.t} />
            </div>
          ))}
        </div>

        <div style={{marginTop: 44, display: 'flex', alignItems: 'flex-end'}}>
          {p.desde ? (
            <span style={{fontFamily: DT.fuentes.texto, fontSize: 30, letterSpacing: '0.04em', marginRight: 14, marginBottom: 8}}>
              {p.desde}
            </span>
          ) : null}
          <span style={{fontFamily: TRADE_CN, fontWeight: 700, fontSize: 92, lineHeight: 0.9}}>{p.precio}</span>
        </div>
        <div style={{marginTop: 12, fontFamily: DT.fuentes.texto, fontSize: 24, letterSpacing: '0.16em'}}>IVA INCLUIDO</div>

        <div style={{marginTop: 42, display: 'flex', flexDirection: 'column', gap: 16}}>
          {p.incluye.map((x) => (
            <div
              key={x}
              style={{
                width: dentro,
                boxSizing: 'border-box',
                border: `1.6px solid rgba(250,250,250,0.85)`,
                borderRadius: 999,
                padding: '15px 18px 12px',
                textAlign: 'center',
                fontFamily: DT.fuentes.texto,
                fontSize: 21,
                letterSpacing: '0.1em',
                textTransform: 'uppercase',
                whiteSpace: 'nowrap',
              }}
            >
              {x}
            </div>
          ))}
        </div>

        <div style={{flex: 1}} />

        <div
          style={{
            alignSelf: 'center',
            background: BLANCO,
            color: AZUL,
            borderRadius: 999,
            padding: '16px 34px 12px',
            fontFamily: DT.fuentes.texto,
            fontSize: 31,
            letterSpacing: '0.02em',
            whiteSpace: 'nowrap',
          }}
        >
          reservas.dtv@hilton.com
        </div>
        <div style={{marginTop: 22, alignSelf: 'center', fontFamily: DT.fuentes.texto, fontSize: 23, letterSpacing: '0.02em'}}>
          Sujeto a disponibilidad.
        </div>
      </div>

      {guia ? <Guia /> : null}
    </AbsoluteFill>
  );
};

export const DtStFeriadoEr: React.FC = () => <DtStFeriadoPrograma cual="er" />;

/**
 * FT sola. Misma gramática de la ref (panel azul, píldoras de contorno, botón lleno),
 * pero el panel va ABAJO y a lo ancho: en todas las escenas del banco la familia
 * ocupa el centro del cuadro y un panel vertical a la izquierda la tapaba (ronda
 * interna 1). La foto 4:5 va arriba, a sangre, y se funde en azul DT.
 */
const PANEL_FT = {x: 88, y: 1010, ancho: 904, alto: 560, radio: 44, pad: 50} as const;

export const DtStFeriadoFt: React.FC<{guia?: boolean}> = ({guia = false}) => {
  const p = FT;
  const col = (PANEL_FT.ancho - PANEL_FT.pad * 2 - 44) / 2;
  return (
    <AbsoluteFill style={{backgroundColor: AZUL}}>
      <Img src={staticFile(p.foto)} style={{position: 'absolute', top: 0, left: 0, width: 1080, height: 1350, objectFit: 'cover'}} />
      <div style={{position: 'absolute', left: 0, top: 0, width: 1080, height: 1350}}>
        <Velo desde={0.55} pie={1} />
      </div>
      <Velo desde={0.72} pie={0.35} lado="arriba" />
      <Logo formato="story" />

      <div
        style={{
          position: 'absolute',
          left: PANEL_FT.x,
          top: PANEL_FT.y,
          width: PANEL_FT.ancho,
          height: PANEL_FT.alto,
          borderRadius: PANEL_FT.radio,
          background: 'rgba(9,25,78,0.84)',
          backdropFilter: 'blur(3.5px)',
          WebkitBackdropFilter: 'blur(3.5px)',
          border: '1.5px solid rgba(250,250,250,0.35)',
          padding: `${PANEL_FT.pad + 4}px ${PANEL_FT.pad}px ${PANEL_FT.pad - 6}px`,
          boxSizing: 'border-box',
          color: BLANCO,
          display: 'flex',
          flexDirection: 'column',
        }}
      >
        <div style={{display: 'flex', justifyContent: 'space-between'}}>
          <div style={{width: col}}>
            {p.titulo.map((l) => (
              <div key={l.t} style={{fontFamily: DT.fuentes.titular, fontWeight: l.w, fontSize: 52, lineHeight: 1.12, whiteSpace: 'nowrap'}}>
                <Stag t={l.t} />
              </div>
            ))}
          </div>
          <div style={{width: col + 20, display: 'flex', flexDirection: 'column', gap: 14, paddingTop: 6}}>
            <div style={{fontFamily: TRADE_CN, fontWeight: 700, fontSize: 84, lineHeight: 0.9}}>{p.precio}</div>
            <div style={{fontFamily: DT.fuentes.texto, fontSize: 22, letterSpacing: '0.16em', marginBottom: 8}}>IVA INCLUIDO</div>
            {p.incluye.map((x) => (
              <div
                key={x}
                style={{
                  boxSizing: 'border-box',
                  border: '1.6px solid rgba(250,250,250,0.85)',
                  borderRadius: 999,
                  padding: '13px 12px 10px',
                  textAlign: 'center',
                  fontFamily: DT.fuentes.texto,
                  fontSize: 19,
                  letterSpacing: '0.035em',
                  textTransform: 'uppercase',
                  whiteSpace: 'nowrap',
                }}
              >
                <span style={{fontFamily: DT.fuentes.texto}}>{x}</span>
              </div>
            ))}
          </div>
        </div>
        <div style={{flex: 1}} />
        <div style={{display: 'flex', alignItems: 'center', justifyContent: 'space-between'}}>
          <span style={{fontFamily: DT.fuentes.texto, fontSize: 22, letterSpacing: '0.02em'}}>Sujeto a disponibilidad.</span>
          <span
            style={{
              background: BLANCO,
              color: AZUL,
              borderRadius: 999,
              padding: '15px 32px 11px',
              fontFamily: DT.fuentes.texto,
              fontSize: 30,
              letterSpacing: '0.02em',
              whiteSpace: 'nowrap',
            }}
          >
            reservas.dtv@hilton.com
          </span>
        </div>
      </div>

      {guia ? <Guia /> : null}
    </AbsoluteFill>
  );
};
export const DtStFeriadoPlanesGuia: React.FC = () => <DtStFeriadoPlanes guia />;
