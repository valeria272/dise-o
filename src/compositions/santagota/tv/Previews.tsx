// ============================================================================
// SANTA GOTA · TV — previews de revisión: las piezas con alfa montadas sobre
// un fotograma real del programa de referencia (TVN). Sólo para revisar.
// ============================================================================
import React from "react";
import {AbsoluteFill, Img, staticFile} from "remotion";
import {HuinchaTV} from "./HuinchaTV";
import {VirtualTV} from "./VirtualTV";

export const HuinchaPreview: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <Img src={staticFile("assets/santagota/_tv-frame-set.png")} style={{position: "absolute", left: 0, top: 0, width: 1920, height: 1080}} />
    <div style={{position: "absolute", left: 0, top: 1080 - 216, width: 1920, height: 216}}>
      <HuinchaTV />
    </div>
  </AbsoluteFill>
);

/** Posición ILUSTRATIVA del panel (la plantilla del canal está pendiente). */
export const VirtualPreview: React.FC = () => {
  const s = 0.72;
  return (
    <AbsoluteFill style={{background: "#000"}}>
      <Img src={staticFile("assets/santagota/_tv-frame-set.png")} style={{position: "absolute", left: 0, top: 0, width: 1920, height: 1080}} />
      <div style={{position: "absolute", left: 1920 - 775 * s - 70, top: 1080 - 1080 * s - 60, width: 775, height: 1080, transform: `scale(${s})`, transformOrigin: "0 0"}}>
        <VirtualTV />
      </div>
    </AbsoluteFill>
  );
};
