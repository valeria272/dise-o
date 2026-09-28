# EBEMA · Grilla octubre 2026 · REELS de Instagram — v1 (28-09-2026)

Producido por Claude con Paulina Bustamante. Destino: **grilla orgánica** (familia A
proveedor/catálogo · familia C Click). Nada de acá es paid.

## Qué se entrega

| Archivo | Fecha grilla | Duración | Familia |
|---|---|---|---|
| `entrega/ebema_reel-01.10_click.mp4` | 01/10 | 18,7 s | C · Ebema Click (sin bandas, lockup) |
| `entrega/ebema_reel-03.10_catalogo.mp4` | 03/10 | 26,4 s | A · catálogo Ebema.cl |
| `entrega/ebema_reel-15.10_aza.mp4` | 15/10 | 23,4 s | A · proveedor Aza |
| `entrega/ebema_reel-17.10_lp.mp4` | 17/10 | 20,3 s | A · proveedor LP |

Todos a **2160×3840, 30 fps, H.264 + AAC**, como los 5 de septiembre.

| `entrega/ebema_reel-27.10_sanbernardo.mp4` | 27/10 | 28,2 s | sucursal · Zona Ofertas Constructor — **metraje real, sin IA** |

GIFs de todos (320 px, 10 fps, 256 colores) en `out/ebema/gifs_octubre_2026/` y en Drive
`4-entregado / gifs`. **Sin portadas** (Paulina, ronda 2).

## De dónde sale cada cosa

- **Gramática**: medida al píxel sobre `reel_VH · reel_cmpc · reel_polpaico · reel_cat_sept ·
  reel_click_sept` (raw/ebema/1-referencias/grilla/video). Marco, cápsula del logo, cierres y
  tipografía: ver la cabecera de `src/compositions/ebema/EbemaGrillaReelsOct.tsx`.
- **Tipografía**: el cuerpo es **Montserrat** (identificado por glifo, no Raleway); el cierre
  es Raleway; cápsulas y 2.ª línea de Click en Helvetica Bold. El cuerpo del titular se
  ajusta para que la línea más larga llene ~1.600 px (VH 160, catálogo sept 208).
- **Voz**: los 5 de septiembre leen el brief palabra por palabra (transcritos con Whisper).
  Lorenzo es-CL, ajuste aprobado el 24-09 → `public/assets/ebema/grilla-oct26/reels/voz/generar.py`.
- **Música**: `audio_fondo3` (pista original de Paulina) desde el segundo 8, a 0,32 bajo la voz.
  Las otras dos pistas (`audio_fondo`, `audio_fondo2`) no están en este PC.
- **Imagen**: 12 fotogramas clave con **Seedream 5 Pro** (`reels/keyframes/prompts.py`), 10
  animados con **Kling 2.5 Pro** (`reels/clips/animar.py`; el 2.1 Pro falló 10 de 10 el 28-09),
  pasados a 30 fps con interpolación (`reels/clips/a30.py`).
- **Productos reales** (bajados de Prodalam, `raw/ebema/4-productos-proveedores/`): ángulo Aza
  (acero negro laminado, **punta pintada verde**) y LP TechShield (aluminio perforado, **canto
  naranjo**). Los logos van por código; la IA no dibuja ninguno.
- **Pantallas reales**: app Click = video de Paulina (`raw/ebema/app-click/`, se salta el login
  que muestra un teléfono); catálogo = **ebema.cl/catalogos** capturado a 390×844 @3x, con el
  botón y el chat de WhatsApp reales del sitio (`reels/ui/`).
- **Mapa Click**: el de LinkedIn alejado hacia el norte con Nano Banana Pro (Santiago caía al
  4 % del alto, bajo la interfaz de IG). Pines de Paulina trasladados por registro SIFT
  (120 puntos, error mediano 3,5 px).

## Decisiones tomadas que Paulina tiene que confirmar

1. **Logo Aza en negativo** (blanco + hoja verde) sobre la foto: el original azul y gris no se
   lee sobre fondo oscurecido. Así se usó CMPC en septiembre.
2. **Aza, atado de ángulos**: se usan sólo los primeros 5 s del clip (después Kling lo vuelve
   plateado/galvanizado) estirados ×1,95 para cubrir la frase de 9,5 s.
3. **Catálogo dura 26 s** (septiembre 18–21 s): el brief de octubre trae más locución.
4. **Click T4**: el cierre dice «Regístrate gratis / y participa en el sorteo de una / gift
   card cada mes.» (el brief), en la gramática del cierre de Click de septiembre. La flecha al
   sticker del brief no aplica a un reel (no hay sticker): septiembre tampoco la llevó.
5. **LP**: «trabajan» sube al pre-enunciado para que el titular «POR BAJAR / LA TEMPERATURA»
   tenga el cuerpo de septiembre.

## Reproducir

```bash
python public/assets/ebema/grilla-oct26/reels/voz/generar.py
python public/assets/ebema/grilla-oct26/reels/keyframes/prompts.py   # gasta créditos
python public/assets/ebema/grilla-oct26/reels/clips/animar.py        # gasta créditos
python public/assets/ebema/grilla-oct26/reels/clips/a30.py
./node_modules/.bin/remotion render EbemaReelClickOct out/.../ebema_reel-01.10_click.mp4 --codec=h264 --crf=16
# ídem EbemaReelCatalogoOct · EbemaReelAzaOct · EbemaReelLpOct
```

## Rondas (28-09-2026, comentarios de Paulina en Drive)

- **Ronda 1 (10 comentarios):** titular derecho sin rotación · caja roja desde la mitad de
  la 1.ª línea · cápsula 56→96 · Aza «UNA DECISIÓN / MÁS CONSCIENTE» · Click: lockup todo el
  video hasta el cierre y T1 más arriba (zona libre) · catálogo: el T1 de 7 s se partió en dos
  escenas (nuevo `cat_k1b`) con texto normal de reel.
- **Ronda 2 (2 comentarios):** textos secundarios en ≤ 2 filas, sin palabra sola, ≥ 300 px
  del borde (había líneas a 76 px) · catálogo en 3 líneas · **sin portadas** (se borraron).
- Paulina: «ok todo bien» → los 4 reels aprobados tras 2 rondas.

## 27/10 San Bernardo — cómo se hizo

Material de Paulina en `raw/ebema/san-bernardo-zona-ofertas/` (AMBIENTE MULTIUSO = San
Bernardo; `reel_3.mp4` = el reel de junio, REF ANTERIOR; `ref_construmart.mp4`, Día del
Maestro). Cortes en `public/assets/ebema/grilla-oct26/reels/sanbernardo/cortar.py`. Seba
sólo cuando muestra el producto. Gramática del reel_3 + etiqueta por categoría (Construmart).
No se reutilizó el letrero de la entrada del reel_3 (siempre trae texto quemado).
