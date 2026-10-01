// ============================================================================
// COPYWRITERS — Mockups
// ----------------------------------------------------------------------------
// Cuando una pieza muestra un anuncio o un correo, ese anuncio y ese correo
// tienen que PARECER reales. Un rectángulo blanco con una foto y un botón no
// es un anuncio: es un rectángulo. Lo que lo vuelve creíble es el cromo — el
// encabezado con el avatar y el «Publicidad», la barra de estado del teléfono,
// el «‹ Todos», la hora, la señal y la batería.
//
// Todo se compone con la tipografía del sistema. Nada de esto lo escribe la IA.
// ============================================================================
import React from "react";
import {VOZ2, granoSVG} from "./sistemaV2";

const SANS = VOZ2.cuerpo;

// ---------------------------------------------------------------------------
// Anuncio de Instagram
// ---------------------------------------------------------------------------

/** Avatar circular con iniciales. */
const Avatar: React.FC<{k: number; texto: string; fondo?: string}> = ({
  k, texto, fondo = "#1C1C1C",
}) => (
  <div style={{
    width: 30 * k, height: 30 * k, borderRadius: "50%", background: fondo,
    display: "flex", alignItems: "center", justifyContent: "center",
    fontFamily: SANS, fontWeight: 600, fontSize: 12 * k, color: "#FFF",
    letterSpacing: 0.2, flexShrink: 0,
  }}>{texto}</div>
);

/**
 * Anuncio de Instagram tal como se ve en el feed.
 *
 * Lleva el encabezado con avatar, el rótulo «Publicidad», el menú de tres
 * puntos, la imagen del producto, el titular y el botón de acción. Sin eso se
 * ve un rectángulo; con eso se ve un anuncio.
 */
export const AnuncioIG: React.FC<{
  x: number; y: number; w: number; giro: number;
  marca: string; iniciales: string;
  imagen: React.ReactNode; copy: string; boton: string;
  atenuado?: boolean;
}> = ({x, y, w, giro, marca, iniciales, imagen, copy, boton, atenuado = false}) => {
  const k = w / 420;
  return (
    <div style={{
      position: "absolute", left: x, top: y, width: w,
      // Se apoya en la mesa: perspectiva corta + sombra de contacto dura y
      // sombra larga blanda. Una sola sombra genérica lo deja flotando.
      transform: `rotate(${giro}deg) perspective(1700px) rotateX(7deg)`,
      transformOrigin: "center center",
      background: "#FCFBF9",
      boxShadow: `${6 * k}px ${8 * k}px ${10 * k}px rgba(0,0,0,0.5),
                  ${24 * k}px ${32 * k}px ${54 * k}px rgba(0,0,0,0.52)`,
      overflow: "hidden",
      filter: atenuado ? "brightness(0.66) saturate(0.72) contrast(0.96)" : undefined,
    }}>
      {/* Encabezado */}
      <div style={{
        display: "flex", alignItems: "center", gap: 9 * k,
        padding: `${11 * k}px ${13 * k}px`,
      }}>
        <Avatar k={k} texto={iniciales} />
        <div style={{flex: 1, lineHeight: 1.15}}>
          <div style={{fontFamily: SANS, fontWeight: 600, fontSize: 13 * k, color: "#161616"}}>
            {marca}
          </div>
          <div style={{fontFamily: SANS, fontWeight: 400, fontSize: 11 * k, color: "#8E8E8E"}}>
            Publicidad
          </div>
        </div>
        <div style={{
          fontFamily: SANS, fontSize: 17 * k, color: "#5A5A5A",
          letterSpacing: 1.6, marginTop: -6 * k,
        }}>•••</div>
      </div>

      {/* Imagen del anuncio */}
      <div style={{position: "relative", width: "100%", height: 300 * k, overflow: "hidden"}}>
        {imagen}
      </div>

      {/* Copy y llamada a la acción */}
      <div style={{padding: `${16 * k}px ${16 * k}px ${17 * k}px`}}>
        <div style={{
          fontFamily: SANS, fontWeight: 400, fontSize: 25 * k, lineHeight: 1.22,
          color: "#131313", letterSpacing: -0.2,
        }}>{copy}</div>
        <div style={{
          marginTop: 15 * k, padding: `${11 * k}px 0`, background: "#141414",
          textAlign: "center", fontFamily: SANS, fontWeight: 500,
          fontSize: 15 * k, color: "#FFF", letterSpacing: 0.2,
        }}>{boton}</div>
      </div>

      {/* Grano de papel y caída de luz de la escena. */}
      <div style={{
        position: "absolute", inset: 0, pointerEvents: "none",
        backgroundImage: granoSVG(0.06, 4), backgroundSize: `${180 * k}px ${180 * k}px`,
        mixBlendMode: "multiply",
      }} />
      <div style={{
        position: "absolute", inset: 0, pointerEvents: "none",
        background: "linear-gradient(126deg, rgba(255,255,255,0.14) 0%, rgba(0,0,0,0) 44%, rgba(0,0,0,0.2) 100%)",
      }} />
    </div>
  );
};

// ---------------------------------------------------------------------------
// Pantalla de Mail en iOS
// ---------------------------------------------------------------------------

/** Iconos de la barra de estado, dibujados — no son emojis ni una fuente. */
const BarraEstado: React.FC<{k: number; hora: string}> = ({k, hora}) => (
  <div style={{
    display: "flex", alignItems: "center", justifyContent: "space-between",
    padding: `${13 * k}px ${22 * k}px ${5 * k}px`,
  }}>
    <div style={{fontFamily: SANS, fontWeight: 600, fontSize: 15 * k, color: "#0B0B0B"}}>
      {hora}
    </div>
    <div style={{display: "flex", alignItems: "flex-end", gap: 5 * k}}>
      {/* Señal */}
      <div style={{display: "flex", alignItems: "flex-end", gap: 1.6 * k}}>
        {[4, 6.5, 9, 11.5].map((h, i) => (
          <div key={i} style={{
            width: 3 * k, height: h * k, borderRadius: 1 * k,
            background: i === 3 ? "#C4C4C4" : "#0B0B0B",
          }} />
        ))}
      </div>
      {/* Wifi */}
      <svg width={15 * k} height={11 * k} viewBox="0 0 15 11" style={{marginBottom: 0.5 * k}}>
        <path d="M7.5 9.6 5.6 7.6a2.7 2.7 0 0 1 3.8 0z" fill="#0B0B0B" />
        <path d="M3.5 5.5a5.7 5.7 0 0 1 8 0" stroke="#0B0B0B" strokeWidth="1.5" fill="none" strokeLinecap="round" />
        <path d="M1.2 3.1a9 9 0 0 1 12.6 0" stroke="#0B0B0B" strokeWidth="1.5" fill="none" strokeLinecap="round" />
      </svg>
      {/* Batería */}
      <div style={{
        width: 24 * k, height: 11.5 * k, borderRadius: 3 * k,
        border: `${1.3 * k}px solid rgba(11,11,11,0.38)`, padding: 1.6 * k,
        display: "flex", alignItems: "center", position: "relative",
      }}>
        <div style={{width: "74%", height: "100%", borderRadius: 1.4 * k, background: "#0B0B0B"}} />
        <div style={{
          position: "absolute", right: -3 * k, top: "34%", width: 1.8 * k,
          height: "32%", borderRadius: 1 * k, background: "rgba(11,11,11,0.38)",
        }} />
      </div>
    </div>
  </div>
);

/**
 * Un correo abierto en Mail de iOS.
 *
 * El cromo es lo que lo vuelve creíble: la barra de estado con hora, señal,
 * wifi y batería; la vuelta a «Todos»; el remitente con su avatar, el «Para:»
 * y la fecha. Después viene el correo de la marca, que es lo que la pieza
 * quiere mostrar.
 */
export const MailIOS: React.FC<{
  // El rectángulo de la pantalla, MEDIDO sobre la fotografía del teléfono.
  x: number; y: number; w: number; h: number;
  giro?: number; inclinacion?: number;
  hora: string; remitente: string; iniciales: string; fecha: string;
  asunto: string; bajada: string;
  logo: string; imagen: React.ReactNode;
  copy: string; boton: string; cuerpo: string;
}> = ({
  x, y, w, h, giro = 0, inclinacion = 0, hora, remitente, iniciales, fecha,
  asunto, bajada, logo, imagen, copy, boton, cuerpo,
}) => {
  const k = w / 420;
  return (
    <div style={{
      position: "absolute", left: x, top: y, width: w, height: h,
      transform: `rotate(${giro}deg)` +
        (inclinacion ? ` perspective(1500px) rotateX(${inclinacion}deg)` : ""),
      transformOrigin: "center center",
      background: "#FFFFFF", overflow: "hidden",
    }}>
      <BarraEstado k={k} hora={hora} />

      {/* Volver a la bandeja */}
      <div style={{
        display: "flex", alignItems: "center", gap: 3 * k,
        padding: `${4 * k}px ${16 * k}px ${9 * k}px`,
        fontFamily: SANS, fontWeight: 400, fontSize: 16 * k, color: "#1E7BF0",
      }}>
        <span style={{fontSize: 20 * k, lineHeight: 1, marginTop: -2 * k}}>‹</span> Todos
      </div>
      <div style={{height: 1, background: "#E6E6E6"}} />

      {/* Remitente */}
      <div style={{
        display: "flex", alignItems: "center", gap: 10 * k,
        padding: `${12 * k}px ${16 * k}px`,
      }}>
        <Avatar k={k * 1.25} texto={iniciales} fondo="#6E2634" />
        <div style={{flex: 1, lineHeight: 1.3}}>
          <div style={{fontFamily: SANS, fontWeight: 600, fontSize: 15 * k, color: "#111"}}>
            {remitente}
          </div>
          <div style={{fontFamily: SANS, fontWeight: 400, fontSize: 13 * k, color: "#8A8A8A"}}>
            Para: Ti
          </div>
        </div>
        <div style={{fontFamily: SANS, fontSize: 13 * k, color: "#9A9A9A"}}>{fecha}</div>
      </div>

      {/* Asunto */}
      <div style={{padding: `${2 * k}px ${16 * k}px ${10 * k}px`}}>
        <div style={{
          fontFamily: SANS, fontWeight: 600, fontSize: 22 * k, lineHeight: 1.22,
          color: "#101010", letterSpacing: -0.3,
        }}>{asunto}</div>
        <div style={{
          marginTop: 5 * k, fontFamily: SANS, fontWeight: 400,
          fontSize: 14 * k, color: "#8A8A8A",
        }}>{bajada}</div>
      </div>
      <div style={{height: 1, background: "#EDEDED"}} />

      {/* El correo de la marca */}
      <div style={{padding: `${18 * k}px ${16 * k}px 0`, textAlign: "center"}}>
        <div style={{
          fontFamily: VOZ2.titular, fontWeight: 700, fontSize: 17 * k,
          letterSpacing: 3.4 * k, color: "#1A1A1A", textTransform: "uppercase",
        }}>{logo}</div>
      </div>

      <div style={{
        position: "relative", margin: `${14 * k}px ${16 * k}px 0`,
        height: 176 * k, overflow: "hidden",
      }}>{imagen}</div>

      <div style={{padding: `${16 * k}px ${24 * k}px 0`, textAlign: "center"}}>
        <div style={{
          fontFamily: SANS, fontWeight: 400, fontSize: 21 * k, lineHeight: 1.26,
          color: "#141414",
        }}>{copy}</div>
        <div style={{
          margin: `${15 * k}px auto 0`, padding: `${11 * k}px ${18 * k}px`,
          background: "#141414", display: "inline-block",
          fontFamily: SANS, fontWeight: 500, fontSize: 14 * k, color: "#FFF",
        }}>{boton} →</div>
      </div>

      <div style={{
        padding: `${18 * k}px ${24 * k}px`, fontFamily: SANS, fontWeight: 400,
        fontSize: 14 * k, lineHeight: 1.45, color: "#5C5C5C",
      }}>{cuerpo}</div>
    </div>
  );
};
