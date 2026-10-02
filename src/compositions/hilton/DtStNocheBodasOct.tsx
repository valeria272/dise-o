/**
 * DOUBLETREE · STORIES octubre 2026 · ESTÁTICA NOCHE DE BODAS (col H, sin fecha).
 * ST adicional que pidió el cliente (hilo de Carlos Figueroa a Eli, STORIES!H10, 02-10).
 * Estado de la grilla: OK PARA DISEÑO.
 *
 * Brief: «Imagen de flores y pétalos (dividida en 2 ref aquí, foto 1 y foto 2)».
 * REF de la imagen (pin 974114594422136859): la pieza PARTIDA en dos fotos apiladas, corte
 * seco, el texto centrado sobre cada mitad.
 * REF de la celda LINK (pin 826832812880256665): la misma del feriado ER/FT — panel
 * translúcido con la lista en píldoras de contorno y un botón lleno.
 * Las dos se juntan: arriba las rosas con el titular, abajo la tina con pétalos y el panel.
 *
 * Fotos: las dos que dejó contenido enlazadas en el brief (`scripts/dt-oct6-fotos.py`).
 * El programa se escribe como Eli lo arma en su carrusel de septiembre (`raw/hilton/dt/nb-sep`):
 * «Noche de Bodas» como logotipo de texto en Stag itálica a dos pesos (R-108).
 *
 * Textos literales de la grilla; titular sin punto (R-60), sin tracking (R-132), incluye en
 * Stag caja baja (R-133), versal del titular en y = 440 (R-134).
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';

import {DT, cargarFuentesDT} from '../../brand/doubletree';
import {Logo, SOMBRA, Stag, TITULO_STORY, TRADE_CN, Velo, topTitulo} from './dtOct2';

cargarFuentesDT();

const AZUL = DT.colores.azul;
const BLANCO = DT.colores.blanco;

/** Donde se parte la pieza. Bajo la mitad: arriba tienen que caber logo, titular y las rosas. */
const CORTE = 1100;

const TITULO = [
  {t: 'Lujo, romance', w: DT.pesos.medium},
  {t: 'y el brindis perfecto', w: DT.pesos.light},
];
const CUERPO_TIT = 70;

const INCLUYE = ['Suite', 'Espumante + macarons', 'Desayuno buffet', 'Late check-out hasta las 16:00 hrs'];

const PANEL = {x: 88, y: 1128, ancho: 904, alto: 430, radio: 44, pad: 54} as const;

const Pildora: React.FC<{t: string}> = ({t}) => (
  <div
    style={{
      boxSizing: 'border-box',
      border: '1.6px solid rgba(250,250,250,0.85)',
      borderRadius: 999,
      padding: '10px 14px 8px',
      textAlign: 'center',
      fontFamily: DT.fuentes.titular,
      fontWeight: DT.pesos.regular,
      fontSize: 24,
      lineHeight: 1.2,
      whiteSpace: 'nowrap',
    }}
  >
    <Stag t={t} />
  </div>
);

export const DtStNocheBodasOct: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: AZUL}}>
    {/* ── arriba · foto 1: las rosas con el espumante ─────────────────────── */}
    <div style={{position: 'absolute', top: 0, left: 0, width: 1080, height: CORTE, overflow: 'hidden'}}>
      {/* RONDA 2 (Eli, 02-10): «las copitas, llénalas de un poco de espumante y utiliza esa toma… donde están
          las flores, la botella de champán con las copitas». La foto 1 a lo ancho de la historia no deja caber el
          conjunto bajo el titular (mide 745 px de alto), así que la toma es la misma escena con las copas
          servidas y más pared arriba (`scripts/dt-oct6-nb-brindis.py`): el conjunto queda entero entre el
          titular y el corte (y 601–1088). Va corrido a la derecha (left −30) para que la cortina quede
          fuera del titular: empieza en x = 890 y «perfecto» termina en 840. La ronda 1 (sólo las rosas) usaba `nb-rosas.jpg`. */}
      <Img src={staticFile('assets/hilton/dt/oct6/nb-brindis.jpg')} style={{position: 'absolute', top: -40, left: -30, width: 1180, height: 1180}} />
      {/* mismo velo de las otras historias del feriado (pie 0,72), para que la secuencia se vea pareja */}
      <Velo desde={0.1} pie={0.72} lado="arriba" />
    </div>

    {/* ── abajo · foto 2: la tina con pétalos ─────────────────────────────── */}
    <div style={{position: 'absolute', top: CORTE, left: 0, width: 1080, height: 1920 - CORTE, overflow: 'hidden'}}>
      {/* la ventana esmerilada queda detrás del panel y los pétalos, debajo de él */}
      <Img src={staticFile('assets/hilton/dt/oct6/nb-tina.jpg')} style={{position: 'absolute', top: -58, left: -330, width: 1573, height: 1050}} />
    </div>

    {/* RONDA 3 (Eli, 02-10): «deja el texto y logo en blanco». La pared es clara, así que el blanco se sostiene
        con el velo azul que nace en cero sobre el ramo y sube hasta arriba (R-13) y con la sombra de los
        titulares de historia. La ronda 2 los llevaba en azul DT y sin velo. Todo sobre el eje, como la referencia. */}
    <Logo formato="story" />

    <div style={{position: 'absolute', top: topTitulo(CUERPO_TIT), left: 0, width: 1080, textAlign: 'center', color: BLANCO}}>
      {TITULO.map((l) => (
        <div
          key={l.t}
          style={{fontFamily: DT.fuentes.titular, fontWeight: l.w, fontSize: CUERPO_TIT, lineHeight: TITULO_STORY.interlinea, textShadow: SOMBRA, whiteSpace: 'nowrap'}}
        >
          <Stag t={l.t} />
        </div>
      ))}
    </div>

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
        border: '1.5px solid rgba(250,250,250,0.35)',
        padding: `${PANEL.pad - 14}px ${PANEL.pad}px ${PANEL.pad - 22}px`,
        boxSizing: 'border-box',
        color: BLANCO,
        display: 'flex',
        flexDirection: 'column',
      }}
    >
      <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
        <div>
          {/* R-108: el nombre del programa como logotipo de texto, Stag itálica a dos pesos */}
          <div style={{fontFamily: DT.fuentes.titular, fontStyle: 'italic', fontSize: 50, lineHeight: 1, whiteSpace: 'nowrap'}}>
            <span style={{fontWeight: DT.pesos.semibold}}>Noche</span>
            <span style={{fontWeight: DT.pesos.light}}> de Bodas</span>
          </div>
          <div style={{marginTop: 20, fontFamily: TRADE_CN, fontWeight: 700, fontSize: 100, lineHeight: 0.9}}>$189.000</div>
          <div style={{marginTop: 12, fontFamily: DT.fuentes.texto, fontSize: 25, letterSpacing: '0.03em'}}>IVA INCLUIDO</div>
        </div>
        <div style={{width: 400, display: 'flex', flexDirection: 'column', gap: 10}}>
          {INCLUYE.map((x) => (
            <Pildora key={x} t={x} />
          ))}
        </div>
      </div>

      <div style={{flex: 1}} />

      <div
        style={{
          alignSelf: 'center',
          background: BLANCO,
          color: AZUL,
          borderRadius: 999,
          padding: '15px 36px 11px',
          fontFamily: DT.fuentes.texto,
          fontSize: 30,
          letterSpacing: '0.02em',
          whiteSpace: 'nowrap',
        }}
      >
        Reserva tu escapada de invierno
      </div>
      <div style={{marginTop: 16, alignSelf: 'center', fontFamily: DT.fuentes.texto, fontSize: 22, letterSpacing: '0.02em', wordSpacing: '0.05em'}}>
        Válido de jueves a domingo y festivos.
      </div>
    </div>

    {guia ? (
      <>
        <div style={{position: 'absolute', top: 0, left: 0, width: 1080, height: DT.seguras.story.arriba, background: 'rgba(255,0,110,0.3)'}} />
        <div style={{position: 'absolute', bottom: 0, left: 0, width: 1080, height: DT.seguras.story.abajo, background: 'rgba(255,0,110,0.3)'}} />
      </>
    ) : null}
  </AbsoluteFill>
);

export const DtStNocheBodasOctGuia: React.FC = () => <DtStNocheBodasOct guia />;
