/**
 * SANTA GOTA · full screen que el cliente mandó a TVN (la versión con la monja, 18 s) + cierre de Instagram.
 *
 * 21-09-2026 · Valeria: «tómalo y agrega el ícono de Instagram al final con un Síguenos y el perfil santagota.cl».
 * La fuente es el MP4 que ella compartió (copia de WhatsApp, 1920×1080 · 29,97 · 540 cuadros): el proyecto original
 * de esa versión no está en el repo, así que se trabaja ENCIMA del video, sin tocar nada antes del cierre.
 *
 * El cierre ya tenía dos estados (logo → «COMPRA EN TODO CHILE / EN SANTAGOTA.CL») y el segundo queda quieto casi
 * 6 s. Se agrega un TERCER estado con la misma mecánica, sin alargar la pieza:
 *   440–448  el texto de «COMPRA EN…» se apaga (parche del color exacto del panel, medido: rgb 5,37,44)
 *   450→     «SÍGUENOS EN» / «INSTAGRAM» / [ícono] @SANTAGOTA.CL entran subiendo por máscara, como las líneas originales
 * Medidas calcadas del cuadro (columna centrada en x = 1319; altos de mayúscula 41 / 72 / 45 px; lima 190,212,1;
 * el subrayado naranja original en y 680–687 se conserva).
 */
import React from "react";
import {AbsoluteFill, Easing, OffthreadVideo, interpolate, staticFile, useCurrentFrame} from "remotion";
import {santagota as SG, ensureSantaGotaFonts} from "../../../brand/santagota";

export const DUR_FULL_CLIENTE = 540;
const SRC = "assets/santagota/tv-cliente/full_cliente_whatsapp.mp4";
const PANEL = "rgb(5,37,44)";
const LIMA = "rgb(190,212,1)";
const CX = 1319;
const SALE = 440;      // 14,68 s: se apaga «COMPRA EN TODO CHILE»
const ENTRA = 450;     // 15,02 s: entra el estado de Instagram

/** Línea que sube por máscara (igual que las del cierre original). */
const Linea: React.FC<{desde: number; top: number; alto: number; children: React.ReactNode}> = ({desde, top, alto, children}) => {
  const f = useCurrentFrame();
  const k = interpolate(f, [desde, desde + 9], [0, 1], {easing: Easing.out(Easing.cubic), extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  return (
    <div style={{position: "absolute", left: CX - 520, width: 1040, top, height: alto, overflow: "hidden"}}>
      <div style={{position: "absolute", inset: 0, display: "flex", alignItems: "center", justifyContent: "center", transform: `translateY(${(1 - k) * 105}%)`, opacity: k > 0 ? 1 : 0}}>
        {children}
      </div>
    </div>
  );
};

/** Glifo de Instagram en línea (monocromo, como pide el uso de marca de Instagram). */
const Instagram: React.FC<{size: number; color: string}> = ({size, color}) => (
  <svg width={size} height={size} viewBox="0 0 64 64" fill="none" style={{display: "block"}}>
    <rect x="5" y="5" width="54" height="54" rx="15" stroke={color} strokeWidth="6" />
    <circle cx="32" cy="32" r="12.5" stroke={color} strokeWidth="6" />
    <circle cx="47.5" cy="16.5" r="4" fill={color} />
  </svg>
);

export const FullClienteIG: React.FC<{soloCapa?: boolean}> = ({soloCapa = false}) => {
  ensureSantaGotaFonts();
  const f = useCurrentFrame();
  const parche = interpolate(f, [SALE, SALE + 8], [0, 1], {extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const base: React.CSSProperties = {fontFamily: SG.fonts.display, textTransform: "uppercase", whiteSpace: "nowrap", lineHeight: 1};
  return (
    <AbsoluteFill style={{backgroundColor: soloCapa ? "transparent" : "#000"}}>
      {/* soloCapa: sólo la gráfica con alfa; el montaje final lo hace ffmpeg sobre los cuadros ORIGINALES (Remotion
          decodifica el MP4 de WhatsApp un cuadro atrasado: los cuadros vienen duplicados de a pares) */}
      {!soloCapa && <OffthreadVideo src={staticFile(SRC)} muted style={{position: "absolute", inset: 0, width: 1920, height: 1080}} />}
      {/* parche del color del panel sobre el texto anterior (el subrayado naranja de y 680 queda) */}
      <div style={{position: "absolute", left: 950, top: 236, width: 760, height: 420, background: PANEL, opacity: parche, boxShadow: `0 0 14px 10px ${PANEL}`}} />
      {f >= ENTRA - 1 && (
        <>
          <Linea desde={ENTRA} top={250} alto={68}>
            <span style={{...base, fontWeight: 700, fontSize: 58, color: "#FFFFFF", letterSpacing: "0.01em"}}>Síguenos en</span>
          </Linea>
          <Linea desde={ENTRA + 5} top={346} alto={112}>
            <span style={{...base, fontWeight: 800, fontSize: 102, color: "#FFFFFF", letterSpacing: "-0.01em"}}>Instagram</span>
          </Linea>
          <Linea desde={ENTRA + 11} top={562} alto={80}>
            <div style={{display: "flex", alignItems: "center", gap: 20}}>
              <Instagram size={62} color={LIMA} />
              <span style={{...base, fontWeight: 800, fontSize: 56, color: LIMA, letterSpacing: "0.01em"}}>@santagota.cl</span>
            </div>
          </Linea>
        </>
      )}
    </AbsoluteFill>
  );
};

/** Sólo la capa gráfica, con alfa (para montar con ffmpeg sobre el video original). */
export const FullClienteIGCapa: React.FC = () => <FullClienteIG soloCapa />;
