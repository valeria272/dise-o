import React from "react";
import {AbsoluteFill, Easing, Img, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig} from "remotion";
import {Audio, Video} from "@remotion/media";
import {ensureRentasFonts, rentas} from "../../brand/rentas";

/**
 * REEL VALLE ALTIPLÁNICO · NOVIEMBRE 2026 — «Recorrido de amenidades» (mar 3-nov)
 *
 * Guion VERBATIM del brief (RENTAS_NUEVA_URBE_GRILLA_NOVIEMBRE_2026.pptx): los seis
 * bloques `VOZ: […]` son a la vez la locución y los subtítulos que pide el brief.
 * Mismo sistema que RentasReelOctubre.tsx (medido sobre `reel_valle_sept.mp4`):
 * caja de logo arriba, subtítulo en caja azul, cifra grande en itálica con unidad en
 * caja lima, placa azul con curvas de nivel, y cierre canónico en fondo blanco (R-21).
 * Sólo material verificado de Valle (dron de `videos-dron` + fotos del proyecto): el
 * rodaje de «CALAMA» es de Travesía (R-05). No hay foto de living que llene el 9:16
 * (sólo una panorámica de 2000×715), así que los interiores son cocina, dormitorio y
 * clóset/baño — sin franjas (R-18). ⚠️ `dormitorio.jpg` de public/ TRAE franjas desenfocadas (la versión que Valeria rechazó en octubre): no usarlo.
 */

const AZUL = rentas.colors.blue;
const LIMA = rentas.colors.lime;
const FUENTE = rentas.fonts.display;

const P = (s: number, fps: number) => Math.round(s * fps);

const useEntrada = (desde: number, dur = 12) => {
  const frame = useCurrentFrame();
  // 02-10 · Constanza: «se genera una difuminación que se repite, quita ese efecto» (placa
  // azul, 0:19). La entrada llevaba blur 14→0 sobre un spring con `durationInFrames`: el bloque
  // llegaba nítido, volvía a difuminarse 7 fotogramas y recién ahí se asentaba. Ahora entra
  // sin blur, con una curva acotada: aparece y sube, una sola vez.
  const p = interpolate(frame, [desde, desde + dur], [0, 1],
    {extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic)});
  return {opacity: p, transform: `translateY(${interpolate(p, [0, 1], [42, 0])}px)`};
};

const CajaLogo: React.FC = () => (
  <div style={{position: "absolute", top: 0, left: "50%", transform: "translateX(-50%)",
               width: 140, height: 106, background: "#fff",
               borderRadius: "0 0 25px 25px", display: "flex",
               alignItems: "flex-start", justifyContent: "center", paddingTop: 19}}>
    <Img src={staticFile("assets/rentas/logo_rentas.png")} style={{width: 76}} />
  </div>
);

const Subtitulo: React.FC<{desde: number; children: React.ReactNode}> = ({desde, children}) => {
  const e = useEntrada(desde);
  return (
    <div style={{position: "absolute", bottom: 300, left: 0, right: 0, textAlign: "center", ...e}}>
      <span style={{display: "inline-block", background: AZUL, color: "#fff", fontFamily: FUENTE,
                    fontWeight: 700, fontSize: 46, lineHeight: 1.18, padding: "14px 26px",
                    maxWidth: 940, letterSpacing: "-0.005em"}}>
        {children}
      </span>
    </div>
  );
};

const Curvas: React.FC = () => (
  <svg viewBox="0 0 1080 1920" style={{position: "absolute", inset: 0, width: "100%", height: "100%"}}>
    {Array.from({length: 11}).map((_, i) => (
      <path key={i} fill="none" stroke="#fff" strokeOpacity={0.13} strokeWidth={3}
            d={`M -120 ${170 * i + 90} C 200 ${170 * i - 20}, 520 ${170 * i + 210}, 760 ${170 * i + 60}
                S 1080 ${170 * i - 40}, 1220 ${170 * i + 120}`} />
    ))}
  </svg>
);

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

export const RentasReelNoviembre: React.FC = () => {
  ensureRentasFonts();
  const {fps, durationInFrames} = useVideoConfig();
  const frame = useCurrentFrame();

  // Música: la misma pista medida para octubre (clara y liviana, como sus reels).
  const musica = interpolate(
    frame,
    [0, P(1.2, fps), durationInFrames - P(2.2, fps), durationInFrames],
    [0, 1.5, 1.5, 0],
    {extrapolateLeft: "clamp", extrapolateRight: "clamp"},
  );

  /**
   * LOCUCIÓN — Benjamín Soto (ElevenLabs vía Magnific, id 864, eleven_v3, estab. 0,45).
   * Texto LITERAL de los bloques VOZ del brief (R-24). Las cifras se le escriben a la
   * voz en palabras («setecientos quince mil», «rentas punto i ene u punto ce ele»)
   * para que las lea como se dicen; lo que se oye es exactamente el texto del brief.
   * A diferencia de octubre, el cierre dura 6,8 s: la URL hablada (5,5 s) cabe entera.
   */
  const LOCUCION = [
    {t: 0.3,  archivo: "01_lugar",        dur: 2.51},
    {t: 3.6,  archivo: "02_areas",        dur: 3.87},
    {t: 9.6,  archivo: "03_interiores",   dur: 3.08},
    {t: 13.8, archivo: "04_sin_comision", dur: 2.27},
    {t: 16.4, archivo: "05_precio",       dur: 5.56},
    {t: 22.5, archivo: "06_cierre",       dur: 5.49},
  ];
  // Ducking por tabla de tiempos (nunca por envolvente): 1,5 → 0,5 con rampas de 0,25 s.
  const RAMPA = 0.25;
  const hablando = LOCUCION.reduce((m, l) => Math.max(m, interpolate(
    frame,
    [P(l.t - RAMPA, fps), P(l.t, fps), P(l.t + l.dur, fps), P(l.t + l.dur + RAMPA, fps)],
    [0, 1, 1, 0],
    {extrapolateLeft: "clamp", extrapolateRight: "clamp"},
  )), 0);
  const musicaConVoz = musica * (1 - 0.667 * hablando);

  return (
    <AbsoluteFill style={{backgroundColor: "#000", fontFamily: FUENTE}}>
      <Audio src={staticFile("assets/rentas/musica_reel.mp3")} volume={musicaConVoz} />
      {LOCUCION.map((l) => (
        <Sequence key={l.archivo} from={P(l.t, fps)} durationInFrames={P(l.dur + 0.1, fps)}>
          <Audio src={staticFile(`assets/rentas/vo-nov/${l.archivo}.mp3`)} />
        </Sequence>
      ))}

      {/* 1 · Logo Valle Altiplánico en pantalla, sobre el dron */}
      <Sequence durationInFrames={P(3.4, fps)}>
        <ClipConLogo src="dron_orbita.mp4" />
        <div style={{position: "absolute", inset: 0, background:
          "linear-gradient(to bottom, rgba(0,0,0,.30) 0%, rgba(0,0,0,.18) 40%, rgba(0,0,0,.18) 60%, rgba(0,0,0,.5) 100%)"}} />
        <div style={{position: "absolute", top: 700, left: 0, right: 0, textAlign: "center",
                     ...useEntrada(P(0.2, fps), 18)}}>
          <Img src={staticFile("assets/rentas/logo_valle_blanco.png")} style={{width: 640}} />
        </div>
        <Subtitulo desde={P(0.4, fps)}>Hay un lugar en Calama<br />que deberías conocer.</Subtitulo>
      </Sequence>

      {/* 2 · Fachada + áreas comunes */}
      <Sequence from={P(3.4, fps)} durationInFrames={P(2.0, fps)}>
        <ClipConLogo src="dron_areas.mp4" />
      </Sequence>
      <Sequence from={P(5.4, fps)} durationInFrames={P(2.0, fps)}>
        <FotoConLogo src="quincho.jpg" zoom={0.10} dx={1.2} />
      </Sequence>
      <Sequence from={P(7.4, fps)} durationInFrames={P(2.0, fps)}>
        <FotoConLogo src="cancha.jpg" zoom={0.10} dx={-1.2} />
      </Sequence>
      <Sequence from={P(3.4, fps)} durationInFrames={P(6.0, fps)}>
        <Subtitulo desde={P(0.2, fps)}>Quincho, cancha y áreas verdes:<br />para disfrutar cada día.</Subtitulo>
      </Sequence>

      {/* 3 · Interiores */}
      <Sequence from={P(9.4, fps)} durationInFrames={P(1.4, fps)}>
        <FotoConLogo src="cocina.jpg" zoom={0.08} dx={-1.0} />
      </Sequence>
      <Sequence from={P(10.8, fps)} durationInFrames={P(1.4, fps)}>
        <FotoConLogo src="bano.jpg" zoom={0.08} dx={1.0} />
      </Sequence>
      <Sequence from={P(12.2, fps)} durationInFrames={P(1.4, fps)}>
        <FotoConLogo src="closet.jpg" zoom={0.08} dy={-1.0} />
      </Sequence>
      <Sequence from={P(9.4, fps)} durationInFrames={P(4.2, fps)}>
        <Subtitulo desde={P(0.2, fps)}>Interiores amplios y luminosos,<br />listos para ti.</Subtitulo>
      </Sequence>

      {/* 4 · Gráfica dinámica: sin comisión + garantía (cada línea entra con su frase) */}
      <Sequence from={P(13.6, fps)} durationInFrames={P(8.6, fps)}>
        <AbsoluteFill style={{background: AZUL}}>
          <Curvas />
          <CajaLogo />
          <div style={{position: "absolute", top: 430, left: 0, right: 0, textAlign: "center", // entradas en frame ABSOLUTO: el hook corre en el padre
                       ...useEntrada(P(13.8, fps), 14)}}>
            <div style={{position: "relative", display: "inline-block"}}>
              <div style={{width: 210, height: 210, borderRadius: "50%", background: LIMA,
                           display: "flex", alignItems: "center", justifyContent: "center",
                           color: AZUL, fontWeight: 900, fontSize: 116, lineHeight: 1}}>$</div>
              <div style={{position: "absolute", right: -46, bottom: -6, width: 92, height: 92,
                           background: "#fff",
                           clipPath: "polygon(0 0, 0 76%, 22% 58%, 37% 94%, 56% 85%, 41% 51%, 69% 49%)"}} />
            </div>
          </div>
          <div style={{position: "absolute", top: 710, left: 0, right: 0, textAlign: "center",
                       ...useEntrada(P(14.1, fps), 14)}}>
            <div style={{color: "#fff", fontWeight: 300, fontStyle: "italic", fontSize: 54}}>
              Aprovecha ahora y arrienda
            </div>
            <span style={{display: "inline-block", background: LIMA, color: AZUL, fontWeight: 700,
                          fontStyle: "italic", fontSize: 66, padding: "10px 26px", marginTop: 10}}>
              SIN COMISIÓN
            </span>
          </div>
          <div style={{position: "absolute", top: 1000, left: 0, right: 0, textAlign: "center",
                       ...useEntrada(P(16.5, fps), 14)}}>
            <div style={{color: "#fff", fontWeight: 300, fontStyle: "italic", fontSize: 46}}>Desde</div>
            <div style={{color: "#fff", fontWeight: 900, fontStyle: "italic", fontSize: 128, lineHeight: 1.02}}>
              $715.000
            </div>
            <span style={{display: "inline-block", background: LIMA, color: AZUL, fontWeight: 700,
                          fontStyle: "italic", fontSize: 40, padding: "8px 20px", marginTop: 4}}>
              mensuales
            </span>
          </div>
          <div style={{position: "absolute", top: 1330, left: 0, right: 0, textAlign: "center",
                       ...useEntrada(P(18.6, fps), 14)}}>
            <div style={{color: "#fff", fontWeight: 300, fontStyle: "italic", fontSize: 46}}>
              1 mes y medio de garantía
            </div>
            <span style={{display: "inline-block", background: LIMA, color: AZUL, fontWeight: 700,
                          fontStyle: "italic", fontSize: 52, padding: "8px 22px", marginTop: 10}}>
              hasta en 6 cuotas
            </span>
          </div>
        </AbsoluteFill>
      </Sequence>

      {/* 5 · CIERRE CANÓNICO — fondo blanco (R-21) */}
      <Sequence from={P(22.2, fps)} durationInFrames={P(6.8, fps)}>
        <AbsoluteFill style={{background: "#fff", alignItems: "center", justifyContent: "center"}}>
          <div style={{textAlign: "center", ...useEntrada(P(22.35, fps), 16)}}>
            <Img src={staticFile("assets/rentas/logo_rentas.png")} style={{width: 420}} />
            <div style={{color: AZUL, fontWeight: 700, fontSize: 46, lineHeight: 1.3, marginTop: 54}}>
              Agenda tu visita<br />en rentas.inu.cl
            </div>
            <div style={{marginTop: 34, opacity: interpolate(frame - P(22.2, fps), [P(3.4, fps), P(3.8, fps)], [0, 1],
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
