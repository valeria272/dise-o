import React from "react";
import {AbsoluteFill, OffthreadVideo, staticFile} from "remotion";

/**
 * VideoSquare01 — 1080×1080 square version of VIDEO1CONLOGO.mp4 (originally 1080×1920, 60fps)
 *
 * Technique: blurred-background fill + contained portrait video centered.
 * The full portrait frame (607×1080) is visible inside the 1080×1080 canvas
 * so no face or logo is cropped. Side columns (~236px each) show the
 * blurred/darkened video fill.
 */
export const VideoSquare01: React.FC = () => {
  const SRC = staticFile("assets/video1.mp4");

  return (
    <AbsoluteFill style={{backgroundColor: "#000000"}}>

      {/* Layer 1 — blurred background fill ────────────────────────────────
          objectFit "cover" scales the 1080×1920 source to fill 1080×1080
          by width, then centers vertically.
          scale(1.14) hides the soft edges that blur creates at the borders. */}
      <AbsoluteFill style={{overflow: "hidden"}}>
        <OffthreadVideo
          src={SRC}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
            filter: "blur(28px) brightness(0.45) saturate(1.3)",
            transform: "scale(1.14)",
          }}
          volume={() => 0}
        />
      </AbsoluteFill>

      {/* Layer 2 — contained portrait video, centered ──────────────────────
          height 100% → 1080px tall → width auto = 607px (aspect 1080:1920).
          Full portrait frame is visible — face and logo stay intact. */}
      <AbsoluteFill style={{justifyContent: "center", alignItems: "center"}}>
        <OffthreadVideo
          src={SRC}
          style={{
            height: "100%",
            width: "auto",
            maxWidth: "100%",
            display: "block",
          }}
          volume={() => 1}
        />
      </AbsoluteFill>

    </AbsoluteFill>
  );
};
