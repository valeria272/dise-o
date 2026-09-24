/**
 * DOUBLETREE · STORIES col L · 30-10-2026 11:00 · ESTÁTICA – HILTON HONORS,
 * RECORDATORIO DE BENEFICIOS. Estado de la grilla: OK PARA DISEÑO.
 *
 * ── Dirección de arte ─────────────────────────────────────────────────────
 * Referencia: pin `802977808617521306` («Your trusted travel partner»). De ahí
 * sale la composición: titular grande ALINEADO A LA IZQUIERDA arriba, y debajo
 * una REJILLA ABIERTA de beneficios —ícono de línea arriba, rótulo abajo—, sin
 * caja ni divisores. La foto respira abajo.
 * Tipografía y color DT: Stag a dos pesos y un mismo cuerpo, tinta blanca,
 * velo azul que nace en 0 arriba.
 *
 * ⭐ El alineado a la izquierda es de la REFERENCIA (§ «las reglas de
 * composición de DT las puede levantar la referencia de Eli»): el default de DT
 * es centrado. El logotipo sí queda centrado, en su plantilla.
 *
 * ⚠️⚠️ LOS CUATRO BENEFICIOS NO ESTÁN EN EL TEXTO DEL BRIEF. El brief trae sólo
 * la frase; la ref es una rejilla de beneficios, y el hilo de Scarlette sobre
 * esta celda dice «Sumar los beneficios» (contenido respondió «Corregido!»).
 * Se usan los cuatro que el CLIENTE YA APROBÓ en el estático de Honors de
 * septiembre (`Post n°1 S4 DT`), con sus mismos íconos y sus mismos cortes de
 * línea — no se redacta nada nuevo. ⚠️ Avisado a Eli: si contenido quiere
 * otros, se cambian los rótulos y nada más.
 *
 * Foto: `HDT_67`, la habitación con Santiago por la ventana (viaje + estadía).
 *
 * ⛔ El CTA «Únete gratis» es un sticker de enlace del CM: NO se dibuja. Queda
 * libre la zona segura de abajo.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';

import {DT, cargarFuentesDT} from '../../brand/doubletree';
import {Icono, NombreIcono} from './dtIconosOct';

cargarFuentesDT();

const G = DT.geometria;
const MESA = {ancho: 1080, alto: 1920} as const;
const M = G.margenLateral;

/** «Hilton Honors: súmate y disfruta beneficios exclusivos en tu próxima estadía» */
const TITULO: readonly {t: string; peso: number}[] = [
  {t: 'Hilton Honors:', peso: DT.pesos.medium},
  {t: 'súmate y disfruta', peso: DT.pesos.light},
  {t: 'beneficios exclusivos', peso: DT.pesos.light},
  {t: 'en tu próxima estadía', peso: DT.pesos.light},
];
const CUERPO_TITULO = 86;

const BENEFICIOS: readonly {icono: NombreIcono; l: readonly [string, string]}[] = [
  {icono: 'etiqueta', l: ['Tarifas', 'exclusivas']},
  {icono: 'cama', l: ['Upgrades de', 'habitación']},
  {icono: 'regalo', l: ['Canje de', 'noches gratis']},
  {icono: 'monedas', l: ['Acumula puntos', 'en cada estadía']},
];

const SOMBRA = '0 2px 7px rgba(9,25,78,0.6), 0 0 2px rgba(9,25,78,0.45)';

/** Velo: nace en 0 arriba y sube cóncavo — paradas aprobadas de la ST del Día del Turismo. */
const VELO = [0, 0.11, 0.22, 0.33, 0.42, 0.48, 0.52, 0.55, 0.57, 0.58, 0.58];

export const DtStHonorsOct: React.FC<{guia?: boolean}> = ({guia = false}) => (
  <AbsoluteFill style={{backgroundColor: DT.colores.azul}}>
    <Img src={staticFile('assets/hilton/dt/oct/hh-hab.jpg')} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
    {/* velo de arriba: el titular cae sobre la pared clara, así que se refuerza con
        una segunda rampa que MUERE hacia abajo (no hay codo: nace en su máximo y
        se apaga suave). */}
    <AbsoluteFill
      style={{background: `linear-gradient(to bottom, ${VELO.map((a, i) => `rgba(9,25,78,${a}) ${i * 10}%`).join(', ')})`}}
    />
    <AbsoluteFill
      style={{
        background:
          'linear-gradient(to bottom, rgba(9,25,78,0.34) 0%, rgba(9,25,78,0.32) 25%, rgba(9,25,78,0.20) 42%, rgba(9,25,78,0.07) 55%, rgba(9,25,78,0) 65%)',
      }}
    />

    <Img
      src={staticFile('assets/hilton/dt/logo-dt-blanco.png')}
      style={{
        position: 'absolute',
        top: G.logoYStory,
        left: (MESA.ancho - G.logoAnchoStory) / 2,
        width: G.logoAnchoStory,
        height: G.logoAnchoStory / G.logoProporcion,
      }}
    />

    {/* titular, a la izquierda como la referencia */}
    <div style={{position: 'absolute', top: 500, left: M}}>
      {TITULO.map(({t, peso}) => (
        <div
          key={t}
          style={{
            fontFamily: DT.fuentes.titular,
            fontWeight: peso,
            fontSize: CUERPO_TITULO,
            lineHeight: 1.1,
            color: DT.colores.blanco,
            textShadow: SOMBRA,
            whiteSpace: 'nowrap',
          }}
        >
          {t}
        </div>
      ))}
    </div>

    {/* la rejilla abierta de beneficios: 2 × 2, ícono arriba y rótulo abajo */}
    <div
      style={{
        position: 'absolute',
        top: 1000,
        left: M,
        width: MESA.ancho - 2 * M,
        display: 'grid',
        gridTemplateColumns: '1fr 1fr',
        rowGap: 50,
      }}
    >
      {BENEFICIOS.map((b) => (
        <div key={b.l[0]}>
          <div style={{height: 60, display: 'flex', alignItems: 'flex-end'}}>
            <Icono n={b.icono} alto={b.icono === 'cama' ? 52 : 60} />
          </div>
          <div
            style={{
              marginTop: 18,
              fontFamily: DT.fuentes.titular,
              fontWeight: DT.pesos.regular,
              fontSize: 34,
              lineHeight: 1.2,
              wordSpacing: '0.12em',
              letterSpacing: '0.012em',
              color: DT.colores.blanco,
              textShadow: SOMBRA,
            }}
          >
            {b.l.map((x) => (
              <div key={x}>{x}</div>
            ))}
          </div>
        </div>
      ))}
    </div>

    {/* Hilton Honors, blanco y sin sombra (ronda 4 del estático de septiembre) */}
    <Img
      src={staticFile('assets/hilton/dt/hilton-honors-blanco.png')}
      style={{position: 'absolute', top: 1454, left: M, height: 82, width: 82 * 2.3213}}
    />

    {guia ? (
      <>
        <div style={{position: 'absolute', top: 0, left: 0, width: MESA.ancho, height: DT.seguras.story.arriba, background: 'rgba(255,0,110,0.3)'}} />
        <div style={{position: 'absolute', bottom: 0, left: 0, width: MESA.ancho, height: DT.seguras.story.abajo, background: 'rgba(255,0,110,0.3)'}} />
        <div style={{position: 'absolute', top: 0, left: M, width: 1, height: MESA.alto, background: 'rgba(255,0,110,0.6)'}} />
      </>
    ) : null}
  </AbsoluteFill>
);

export const DtStHonorsOctGuia: React.FC = () => <DtStHonorsOct guia />;
