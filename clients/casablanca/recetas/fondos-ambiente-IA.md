# Casablanca C1 — fondos de ambiente (HECHOS)

> Rescatado del escritorio el 25-08-2026. La receta sirve para cualquier marca que
> necesite **el mismo ambiente cambiando un solo elemento**: una base + ediciones
> img-to-img, nunca 4 imágenes sueltas.

**Estado: listo.** Los 4 ambientes están generados y montados; las 8 piezas de C1
ya están rendidas con ellos. Este archivo queda como receta para repetirlo.

- **Servicio:** Freepik / Magnific (la API key nueva `claudecw` es de Freepik).
- **Script:** ya vive en el repo como
  [`scripts/casablanca-ambiente-base.py`](../../../scripts/casablanca-ambiente-base.py)
  (antes se llamaba `genera_fondos.py` y estaba en el scratchpad).
- **Salida:** `public/assets/casablanca/amb_*.jpg`, 2048 × 2048.

---

## El método (es lo que hace que funcione)

El brief exige **un mismo ambiente en las 4 tarjetas**, cambiando *solo la tabla del
piso*. Generar 4 imágenes sueltas rompe esa regla. El flujo correcto es:

1. **Una sola imagen base** con Mystic (`/v1/ai/mystic`, 2K, `square_1_1`).
2. **Tres ediciones img-to-img** con Nano Banana
   (`/v1/ai/gemini-2-5-flash-image-preview`), pasando la base como
   `reference_images` y pidiendo explícitamente que no cambie nada más.

---

## Prompt base

```
Interior photograph of a bright airy living-dining room, camera at waist height
angled slightly downward so the engineered wood floor fills the entire bottom 55
percent of the frame and recedes in perspective toward the viewer. Above the
floor, a plain light plaster wall with a section of exposed brick and slim wooden
ceiling beams. Only two or three furniture pieces, placed to the left and set
back: a simple light-wood dining table with chairs and a woven basket with a green
plant. Large window on the right with soft natural daylight, warm neutral white
balance. Very clean and uncluttered, with a wide empty floor area in the
foreground and no objects on it. Engineered oak plank flooring in warm honey tone,
wide long planks laid lengthwise. Architectural digest style, photorealistic,
sharp, no people, no text, no logos, no watermark.
```

## Prefijo de las 3 ediciones

```
Keep the entire scene absolutely identical - same walls, same brick, same beams,
same furniture, same plant, same window, same daylight, same white balance, same
camera angle and framing. Change ONLY the wood floor planks to:
```

| Tarjeta | Producto | Final del prompt |
|---|---|---|
| 1 | Roble Natural UV 14/3 · 190 × 1900 | *(es la base)* |
| 2 | Roble Natural UV 10/1.2 · 167 × 1200 | `the same honey oak tone and finish, but noticeably narrower and shorter planks, more visible seams across the floor.` |
| 3 | Roble Aserrado 14/3 · 190 × 1900 | `rustic sawn-cut oak with pronounced saw marks, open grain, visible knots and strong texture, slightly cooler and more matte than before.` |
| 4 | Cumarú 12/2 · 120 × 2130 | `narrow long cumaru planks in a warm reddish-brown tropical hardwood tone, tight straight grain, satin sheen.` |

---

## Aprendizajes de esta ronda

- **La cámara hay que bajarla a mano.** El primer intento dejó el piso en 28 % del
  cuadro; pedir "waist height angled slightly downward" + "fills the bottom 55
  percent" lo subió a ~32 %, que ya lee bien. Si se quiere más piso, insistir con
  el ángulo, no con el encuadre.
- **Nano Banana devuelve 1024 px**, la base sale en 2048. Hay que subir las tres
  variantes con Lanczos para que empaten.
- **El muro es casi blanco → el texto va en gris carbón, no en blanco.** Es el
  mismo criterio de la pieza de cierre de agosto. Sobre el muro claro, el logo va
  gris directo (sin la tarjeta blanca que sí usa C2 sobre fotos oscuras).
- **Velo:** un `radial-gradient` claro centrado en la zona del texto aclara la
  planta que se cruza sin apagar el ladrillo, la ventana ni el piso.
