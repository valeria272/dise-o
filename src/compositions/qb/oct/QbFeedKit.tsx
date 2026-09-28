/**
 * QB · FEED OCTUBRE 2026 — lo único que el feed necesita aparte del kit de
 * historias: la mesa 4:5 y la foto a sangre en esa mesa.
 *
 * Mesa 1080×1350 (el `.ai` de feed de QB es 1:1 a 1080) → entrega 2250×2812
 * con `--scale=2.0833`. Zona segura de feed: 12 % de abajo sin texto (≤ 1188).
 *
 * ⛔ La foto se dibuja a su tamaño con `object-fit`, nunca con `transform:
 * scale()` (manual §4e).
 */
import React from "react";
import {Img, staticFile} from "remotion";

export const FEED = {w: 1080, h: 1350} as const;
export const FEED_SEGURA = {top: 90, bottom: 1188} as const;

export const FotoFeed: React.FC<{src: string; pos?: string; filtro?: string}> = ({
  src, pos = "50% 50%", filtro,
}) => (
  <Img src={staticFile(src)} style={{position: "absolute", left: 0, top: 0, width: FEED.w,
    height: FEED.h, objectFit: "cover", objectPosition: pos, filter: filtro}} />
);
