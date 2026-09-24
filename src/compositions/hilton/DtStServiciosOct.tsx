/**
 * DOUBLETREE · STORIES col G · 13-10-2026 11:00 · ESTÁTICA – SERVICIOS DEL HOTEL.
 * Estado de la grilla: OK PARA DISEÑO.
 *
 * ── Dirección de arte ─────────────────────────────────────────────────────
 * Referencia: pin `682647256073727716` («Campus Hotel»). De ahí sale la
 * COMPOSICIÓN, entera y en su orden:
 *   marco fino de esquinas redondeadas que encierra la pieza · logotipo arriba ·
 *   titular grande centrado · filete · panel de cristal con los servicios ·
 *   tres fotos en tarjetas redondeadas · (abajo, libre).
 * La tipografía y el color son DT: Stag a dos pesos y un mismo cuerpo, tinta
 * blanca, cristal teñido de azul #09194E.
 *
 * ⭐ Diferencia con la referencia, a propósito: allá los servicios son cinco
 * íconos con UNA palabra; acá el brief trae CUATRO servicios con nombre y
 * bajada, así que el panel es de 2 × 2 (la gramática de cuadrante del Honors
 * de septiembre) y no una fila.
 *
 * Fotos: banco profesional del hotel. Fondo = lobby lounge (`HDT_36`),
 * difuminado como en la ref. Tarjetas = bar del lobby (`HDT_39`), el lounge
 * con la barra (`HDT_53`) y el gimnasio (`HDT_82`): una por servicio con
 * espacio propio; Hilton Honors no es un lugar y no lleva foto.
 *
 * Textos literales del brief (§G), sin punto final (§F). La interacción es
 * «informativa, sin interacción (o sticker de encuesta opcional)»: no se dibuja
 * nada y queda libre la zona segura de abajo.
 */
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';

import {DT, cargarFuentesDT} from '../../brand/doubletree';
import {ConTrade, Icono, NombreIcono} from './dtIconosOct';

cargarFuentesDT();

const G = DT.geometria;
const MESA = {ancho: 1080, alto: 1920} as const;

const TITULO = ['Mucho más que solo', 'un lugar para descansar'] as const;
const SERVICIOS: readonly {icono: NombreIcono; nombre: string; bajada: readonly [string, string]}[] = [
  {icono: 'copa', nombre: 'Restaurante & Bar', bajada: ['Gastronomía y', 'coctelería de autor']},
  {icono: 'taza', nombre: 'Coffee & Work Lounge', bajada: ['Ambientes pensados', 'para conectar']},
  {icono: 'etiqueta', nombre: 'Exclusividad Hilton Honors', bajada: ['Upgrades y tarifas', 'especiales']},
  {icono: 'mancuerna', nombre: 'Wellness & Fitness', bajada: ['Mantén tu rutina', 'durante la visita']},
];
const FOTOS = ['sv-bar', 'sv-cowork', 'sv-gym'] as const;
const CTA = 'Descubre todo lo que tenemos para ti';

const SOMBRA = '0 2px 7px rgba(9,25,78,0.55), 0 0 2px rgba(9,25,78,0.4)';

const MARCO = {x: 34, y: 176, ancho: 1012, alto: 1560, radio: 40} as const;
const PANEL = {x: 88, y: 760, ancho: 904, alto: 400, radio: 28} as const;
const TARJETAS = {y: 1196, alto: 300, gap: 20, radio: 22} as const;

export const DtStServiciosOct: React.FC<{guia?: boolean}> = ({guia = false}) => {
  const anchoTarjeta = (PANEL.ancho - 2 * TARJETAS.gap) / 3;
  return (
    <AbsoluteFill style={{backgroundColor: DT.colores.azul}}>
      {/* 1 · el lobby, difuminado como en la referencia */}
      <Img
        src={staticFile('assets/hilton/dt/oct/sv-fondo.jpg')}
        style={{width: '100%', height: '100%', objectFit: 'cover', filter: 'blur(5px)', transform: 'scale(1.03)'}}
      />
      {/* 2 · el velo azul: nace en 0 arriba y sube cóncavo (paradas aprobadas del Día del Turismo) */}
      <AbsoluteFill
        style={{
          background: `linear-gradient(to bottom, ${[0, 0.2, 0.3, 0.38, 0.44, 0.48, 0.52, 0.55, 0.57, 0.58, 0.58]
            .map((a, i) => `rgba(9,25,78,${Math.max(a, 0.18)}) ${i * 10}%`)
            .join(', ')})`,
        }}
      />

      {/* 3 · el marco fino de la referencia */}
      <div
        style={{
          position: 'absolute',
          left: MARCO.x,
          top: MARCO.y,
          width: MARCO.ancho,
          height: MARCO.alto,
          borderRadius: MARCO.radio,
          border: '1.5px solid rgba(250,250,250,0.7)',
          boxSizing: 'border-box',
        }}
      />

      {/* 4 · logotipo, plantilla `logo-ST.png` */}
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

      {/* 5 · titular a dos pesos y un mismo cuerpo */}
      <div style={{position: 'absolute', top: 470, left: 0, width: MESA.ancho, textAlign: 'center'}}>
        {TITULO.map((t, i) => (
          <div
            key={t}
            style={{
              fontFamily: DT.fuentes.titular,
              fontWeight: i === 0 ? DT.pesos.medium : DT.pesos.light,
              fontSize: 78,
              lineHeight: 1.14,
              color: DT.colores.blanco,
              textShadow: SOMBRA,
              whiteSpace: 'nowrap',
            }}
          >
            {t}
          </div>
        ))}
        <div style={{width: 160, height: 1.5, margin: '40px auto 0', background: 'rgba(250,250,250,0.8)'}} />
      </div>

      {/* 6 · el panel de cristal con los cuatro servicios */}
      <div
        style={{
          position: 'absolute',
          left: PANEL.x,
          top: PANEL.y,
          width: PANEL.ancho,
          height: PANEL.alto,
          borderRadius: PANEL.radio,
          background: 'rgba(9,25,78,0.34)',
          backdropFilter: 'blur(14px)',
          WebkitBackdropFilter: 'blur(14px)',
          border: '1.5px solid rgba(250,250,250,0.85)',
          boxSizing: 'border-box',
          display: 'flex',
          flexWrap: 'wrap',
        }}
      >
        {SERVICIOS.map((s, i) => (
          <div
            key={s.nombre}
            style={{
              width: '50%',
              height: '50%',
              boxSizing: 'border-box',
              padding: '0 20px 0 30px',
              display: 'flex',
              alignItems: 'center',
              gap: 22,
              borderRight: i % 2 === 0 ? '1.5px solid rgba(250,250,250,0.4)' : undefined,
              borderBottom: i < 2 ? '1.5px solid rgba(250,250,250,0.4)' : undefined,
            }}
          >
            <div style={{width: 72, display: 'flex', justifyContent: 'center'}}>
              <Icono n={s.icono} alto={56} />
            </div>
            <div style={{color: DT.colores.blanco, textShadow: SOMBRA, whiteSpace: 'nowrap'}}>
              <div
                style={{
                  fontFamily: DT.fuentes.titular,
                  fontWeight: DT.pesos.medium,
                  fontSize: s.nombre.length > 22 ? 25 : 28,
                  lineHeight: 1.15,
                  marginBottom: 8,
                }}
              >
                <ConTrade t={s.nombre} />
              </div>
              {s.bajada.map((l) => (
                <div
                  key={l}
                  style={{
                    fontFamily: DT.fuentes.titular,
                    fontWeight: DT.pesos.light,
                    fontSize: 26,
                    lineHeight: 1.22,
                    wordSpacing: '0.1em',
                  }}
                >
                  {l}
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>

      {/* 7 · las tres tarjetas de foto */}
      {FOTOS.map((f, i) => (
        <div
          key={f}
          style={{
            position: 'absolute',
            left: PANEL.x + i * (anchoTarjeta + TARJETAS.gap),
            top: TARJETAS.y,
            width: anchoTarjeta,
            height: TARJETAS.alto,
            borderRadius: TARJETAS.radio,
            overflow: 'hidden',
            border: '1.5px solid rgba(250,250,250,0.85)',
            boxSizing: 'border-box',
          }}
        >
          <Img src={staticFile(`assets/hilton/dt/oct/${f}.jpg`)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
        </div>
      ))}

      {/* 8 · el subtexto / CTA, literal y sin punto */}
      <div
        style={{
          position: 'absolute',
          top: 1534,
          left: 0,
          width: MESA.ancho,
          textAlign: 'center',
          fontFamily: DT.fuentes.titular,
          fontWeight: DT.pesos.regular,
          fontSize: 34,
          wordSpacing: '0.12em',
          color: DT.colores.blanco,
          textShadow: SOMBRA,
        }}
      >
        {CTA}
      </div>

      {guia ? (
        <>
          <div style={{position: 'absolute', top: 0, left: 0, width: MESA.ancho, height: DT.seguras.story.arriba, background: 'rgba(255,0,110,0.3)'}} />
          <div style={{position: 'absolute', bottom: 0, left: 0, width: MESA.ancho, height: DT.seguras.story.abajo, background: 'rgba(255,0,110,0.3)'}} />
          <div style={{position: 'absolute', top: 0, left: MESA.ancho / 2, width: 1, height: MESA.alto, background: 'rgba(255,0,110,0.6)'}} />
        </>
      ) : null}
    </AbsoluteFill>
  );
};

export const DtStServiciosOctGuia: React.FC = () => <DtStServiciosOct guia />;
