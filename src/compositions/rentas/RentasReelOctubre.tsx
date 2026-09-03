import React from "react";
import {AbsoluteFill, Img, Sequence, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig} from "remotion";
import {Video} from "@remotion/media";
import {ensureRentasFonts, rentas} from "../../brand/rentas";

/**
 * REEL VALLE ALTIPLÁNICO · OCTUBRE 2026 — «Nuevas condiciones»
 *
 * Guion VERBATIM del brief (RENTAS_NUEVA_URBE_GRILLA_OCTUBRE_2026_1.pptx).
 * La estructura y el CIERRE salen de medir `reel_valle_sept.mp4` fotograma a
 * fotograma: caja de logo arriba todo el reel, subtítulo en caja azul, la cifra
 * grande en itálica con la unidad en caja lima, la placa azul con el ícono $ en
 * disco lima y cursor, y el cierre en fondo BLANCO con el logo centrado.
 * Ver clients/nueva-urbe/CLAUDE.md §«El reel — la estructura y el cierre».
 */

const AZUL = rentas.colors.blue;
const LIMA = rentas.colors.lime;
const FUENTE = rentas.fonts.display;

const P = (s: number, fps: number) => Math.round(s * fps);

/** Entra desde abajo con desenfoque, como los subtítulos de sus reels. */
const useEntrada = (desde: number, dur = 12) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const p = spring({fps, frame: frame - desde, config: {damping: 18, stiffness: 130}, durationInFrames: dur});
  return {opacity: p, transform: `translateY(${interpolate(p, [0, 1], [42, 0])}px)`,
          filter: `blur(${interpolate(p, [0, 1], [14, 0])}px)`};
};

/** La caja blanca del logo, colgada del borde superior. En reel va al 13 % del ancho. */
const CajaLogo: React.FC = () => (
  <div style={{position: "absolute", top: 0, left: "50%", transform: "translateX(-50%)",
               width: 140, height: 106, background: "#fff",
               borderRadius: "0 0 25px 25px", display: "flex",
               alignItems: "flex-start", justifyContent: "center", paddingTop: 19}}>
    <Img src={staticFile("assets/rentas/logo_rentas.png")} style={{width: 76}} />
  </div>
);

/** Subtítulo en caja azul, centrado abajo — el patrón de sus reels. */
const Subtitulo: React.FC<{desde: number; children: React.ReactNode}> = ({desde, children}) => {
  const e = useEntrada(desde);
  return (
    <div style={{position: "absolute", bottom: 300, left: 0, right: 0, textAlign: "center", ...e}}>
      <span style={{display: "inline-block", background: AZUL, color: "#fff", fontFamily: FUENTE,
                    fontWeight: 700, fontSize: 46, lineHeight: 1.18, padding: "14px 26px",
                    maxWidth: 900, letterSpacing: "-0.005em"}}>
        {children}
      </span>
    </div>
  );
};

/** Textura de curvas de nivel de la placa de marca, dibujada, no importada. */
const Curvas: React.FC = () => (
  <svg viewBox="0 0 1080 1920" style={{position: "absolute", inset: 0, width: "100%", height: "100%"}}>
    {Array.from({length: 11}).map((_, i) => (
      <path key={i} fill="none" stroke="#fff" strokeOpacity={0.13} strokeWidth={3}
            d={`M -120 ${170 * i + 90} C 200 ${170 * i - 20}, 520 ${170 * i + 210}, 760 ${170 * i + 60}
                S 1080 ${170 * i - 40}, 1220 ${170 * i + 120}`} />
    ))}
  </svg>
);

/**
 * Foto fija con Ken Burns. SIEMPRE a cuadro completo: la panorámica del
 * dormitorio se probó como banda nítida sobre fondo desenfocado y Valeria la
 * rechazó — «no pueden existir esas franjas arriba y abajo, se ve muy amateur».
 * Si una foto no llena el 9:16, no entra al reel.
 *
 * Los interiores van en FOTO y no en video porque el
 * rodaje de «CALAMA» que hay en Drive NO es de Valle Altiplánico: se cotejó
 * contra las fotos verificadas del proyecto y el baño lleva otra cortina y otra
 * cerámica, y la cocina otra cubierta. Ese material es de Travesía del Desierto II.
 */
const FotoKB: React.FC<{src: string; zoom?: number; dx?: number; dy?: number}> =
  ({src, zoom = 0.09, dx = 0, dy = 0}) => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  const p = interpolate(frame, [0, durationInFrames], [0, 1], {extrapolateRight: "clamp"});
  return (
    <AbsoluteFill style={{overflow: "hidden"}}>
      <Img src={staticFile(`assets/rentas/fotos/${src}`)}
           style={{width: "100%", height: "100%", objectFit: "cover",
                   transform: `scale(${1 + zoom * p}) translate(${dx * p}%, ${dy * p}%)`}} />
    </AbsoluteFill>
  );
};

const FotoConLogo: React.FC<{src: string; zoom?: number; dx?: number; dy?: number}> = (props) => (
  <>
    <FotoKB {...props} />
    <CajaLogo />
  </>
);

const ClipConLogo: React.FC<{src: string}> = ({src}) => (
  <>
    <Video src={staticFile(`assets/rentas/clips/${src}`)} muted
           style={{width: "100%", height: "100%", objectFit: "cover"}} />
    <CajaLogo />
  </>
);

export const RentasReelOctubre: React.FC = () => {
  ensureRentasFonts();
  const {fps} = useVideoConfig();
  const frame = useCurrentFrame();

  /**
   * Locución. La voz es `es-CL-LorenzoNeural` con pitch +26 Hz: el reel de
   * septiembre del cliente mide f0 mediana 138 Hz y Lorenzo neutro cae en 105,
   * así que se sube hasta 123 — misma familia, un punto más grave, que es el
   * «similar pero con el tono algo cambiado» que pidió Valeria.
   * Se genera con `scripts/rentas-voz.py`.
   */
  /**
   * SIN LOCUCIÓN. La versión con TTS (`scripts/rentas-voz.py`) se descartó:
   * «es muy robótica, es falsa». Sus cinco reels llevan locución humana real
   * —medido: modulación silábica 35-41 % en los de mayo a septiembre— y
   * clonarla no se pudo (Higgsfield quedó en 0,43 créditos y no hay clave de
   * ElevenLabs). El guion del brief queda en los subtítulos.
   */
  return (
    <AbsoluteFill style={{backgroundColor: "#000", fontFamily: FUENTE}}>

      {/* 1 · Dron + gancho ─────────────────────────────────────────── */}
      <Sequence durationInFrames={P(3.6, fps)}>
        <ClipConLogo src="dron_orbita.mp4" />
        <div style={{position: "absolute", inset: 0, background:
          "linear-gradient(to bottom, rgba(0,0,0,.34) 0%, transparent 30%, transparent 62%, rgba(0,0,0,.5) 100%)"}} />
        <Subtitulo desde={P(0.35, fps)}>¿BUSCANDO DEPTO EN CALAMA?</Subtitulo>
        <div style={{position: "absolute", top: 210, left: 0, right: 0, textAlign: "center",
                     ...useEntrada(P(1.1, fps), 16)}}>
          <Img src={staticFile("assets/rentas/logo_valle_blanco.png")} style={{width: 470}} />
        </div>
      </Sequence>

      {/* 2 · Áreas comunes ─────────────────────────────────────────── */}
      <Sequence from={P(3.6, fps)} durationInFrames={P(3.4, fps)}>
        <ClipConLogo src="dron_areas.mp4" />
        <Subtitulo desde={P(0.2, fps)}>Octubre llegó con<br />mejores condiciones</Subtitulo>
      </Sequence>
      <Sequence from={P(7.0, fps)} durationInFrames={P(3.0, fps)}>
        <FotoConLogo src="quincho.jpg" zoom={0.10} dx={1.2} />
        <Subtitulo desde={P(0.2, fps)}>Espacios para disfrutar<br />todo el año</Subtitulo>
      </Sequence>
      <Sequence from={P(10.0, fps)} durationInFrames={P(3.2, fps)}>
        <ClipConLogo src="dron_piscina.mp4" />
        <Subtitulo desde={P(0.2, fps)}>Dos piscinas, quincho,<br />cancha y áreas verdes</Subtitulo>
      </Sequence>

      {/* 3 · Interiores + la cifra ─────────────────────────────────── */}
      <Sequence from={P(13.2, fps)} durationInFrames={P(3.4, fps)}>
        <FotoConLogo src="cocina.jpg" zoom={0.10} dx={-1.2} />
        <div style={{position: "absolute", inset: 0, background:
          "linear-gradient(to bottom, transparent 45%, rgba(0,0,0,.52) 100%)"}} />
        <div style={{position: "absolute", bottom: 330, left: 0, right: 0, textAlign: "center",
                     ...useEntrada(P(0.25, fps))}}>
          <div style={{color: "#fff", fontWeight: 300, fontSize: 44, letterSpacing: ".01em"}}>
            Arrienda hoy desde
          </div>
          <div style={{color: "#fff", fontWeight: 900, fontStyle: "italic", fontSize: 132,
                       lineHeight: 1.02, textShadow: "0 8px 30px rgba(0,0,0,.4)"}}>
            $715.000
          </div>
          <span style={{display: "inline-block", background: LIMA, color: AZUL, fontWeight: 700,
                        fontStyle: "italic", fontSize: 40, padding: "8px 20px", marginTop: 6}}>
            mensuales
          </span>
        </div>
      </Sequence>
      <Sequence from={P(16.6, fps)} durationInFrames={P(2.8, fps)}>
        <FotoConLogo src="closet.jpg" zoom={0.11} dy={-1.0} />
        <Subtitulo desde={P(0.2, fps)}>2 y 3 dormitorios<br />con clósets empotrados</Subtitulo>
      </Sequence>
      <Sequence from={P(19.4, fps)} durationInFrames={P(2.8, fps)}>
        <FotoConLogo src="bano.jpg" zoom={0.10} dy={1.0} />
        <Subtitulo desde={P(0.2, fps)}>Entrega inmediata<br />en Calama</Subtitulo>
      </Sequence>

      {/* 4 · La placa de marca ─────────────────────────────────────── */}
      <Sequence from={P(22.2, fps)} durationInFrames={P(4.0, fps)}>
        <AbsoluteFill style={{background: AZUL}}>
          <Curvas />
          <CajaLogo />
          <div style={{position: "absolute", top: 620, left: 0, right: 0, textAlign: "center",
                       ...useEntrada(P(0.2, fps), 14)}}>
            <div style={{position: "relative", display: "inline-block"}}>
              <div style={{width: 210, height: 210, borderRadius: "50%", background: LIMA,
                           display: "flex", alignItems: "center", justifyContent: "center",
                           color: AZUL, fontWeight: 900, fontSize: 116, lineHeight: 1}}>$</div>
              <div style={{position: "absolute", right: -46, bottom: -6, width: 92, height: 92,
                           background: "#fff",
                           clipPath: "polygon(0 0, 0 76%, 22% 58%, 37% 94%, 56% 85%, 41% 51%, 69% 49%)"}} />
            </div>
          </div>
          <div style={{position: "absolute", top: 900, left: 0, right: 0, textAlign: "center",
                       ...useEntrada(P(0.8, fps), 14)}}>
            <div style={{color: "#fff", fontWeight: 300, fontStyle: "italic", fontSize: 56}}>Arrienda</div>
            <span style={{display: "inline-block", background: LIMA, color: AZUL, fontWeight: 700,
                          fontStyle: "italic", fontSize: 62, padding: "10px 26px", marginTop: 10}}>
              SIN COMISIÓN
            </span>
          </div>
          <div style={{position: "absolute", top: 1180, left: 0, right: 0, textAlign: "center",
                       ...useEntrada(P(1.6, fps), 14)}}>
            <div style={{color: "#fff", fontWeight: 300, fontStyle: "italic", fontSize: 46}}>
              Garantía de 1,5 meses
            </div>
            <span style={{display: "inline-block", background: LIMA, color: AZUL, fontWeight: 700,
                          fontStyle: "italic", fontSize: 52, padding: "8px 22px", marginTop: 10}}>
              hasta en 6 cuotas
            </span>
          </div>
        </AbsoluteFill>
      </Sequence>

      {/* 5 · CIERRE CANÓNICO — fondo blanco ────────────────────────── */}
      <Sequence from={P(26.2, fps)} durationInFrames={P(3.8, fps)}>
        <AbsoluteFill style={{background: "#fff", alignItems: "center", justifyContent: "center"}}>
          <div style={{textAlign: "center", ...useEntrada(P(0.15, fps), 16)}}>
            <Img src={staticFile("assets/rentas/logo_rentas.png")} style={{width: 420}} />
            <div style={{color: AZUL, fontWeight: 700, fontSize: 46, lineHeight: 1.3, marginTop: 54}}>
              Agenda tu visita<br />en rentas.inu.cl
            </div>
            <div style={{marginTop: 34, opacity: interpolate(frame - P(26.2, fps), [P(0.9, fps), P(1.3, fps)], [0, 1],
                          {extrapolateLeft: "clamp", extrapolateRight: "clamp"})}}>
              <span style={{display: "inline-block", background: AZUL, color: "#fff", fontWeight: 700,
                            fontSize: 38, padding: "14px 30px"}}>
                ¡Escríbenos por WhatsApp!
              </span>
            </div>
          </div>
        </AbsoluteFill>
      </Sequence>
    </AbsoluteFill>
  );
};
