// ============================================================================
// SANTA GOTA · TV — previews de revisión: las piezas con alfa montadas a ESCALA
// REAL (1:1) sobre un fotograma del programa de referencia (TVN). Sólo para revisar.
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

/** El virtual 775×1080 ocupa toda la altura del cuadro, a la derecha (posición ILUSTRATIVA: la plantilla del canal está pendiente). */
export const VirtualPreview: React.FC = () => (
  <AbsoluteFill style={{background: "#000"}}>
    <Img src={staticFile("assets/santagota/_tv-frame-set.png")} style={{position: "absolute", left: 0, top: 0, width: 1920, height: 1080}} />
    <div style={{position: "absolute", left: 1920 - 775, top: 0, width: 775, height: 1080}}>
      <VirtualTV />
    </div>
  </AbsoluteFill>
);
