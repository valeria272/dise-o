# EBEMA · LinkedIn octubre 2026 — entrega

Grilla: `GRILLA OCTUBRE 2026 - EBEMA` (Carlos Figueroa), sección 03 LINKEDIN.
Drive: `MATERIAL DISEÑO PAULINA / EBEMA / 4-entregado / 2026-10 linkedin octubre`
(`12rsOt4G__ljKSK5uG3s7tn0K5S7-b0wn`).

| Fecha | Pieza | Archivo | Estado |
|---|---|---|---|
| 05/10 | Reel saludo sucursal Talca (18,1 s, 2160×3840) | `ebema_lk_reel-05.10_talca.mp4` | ronda 1 aplicada |
| 12/10 | Carrusel · El equipo de ventas detrás de cada cotización | `c_ventas/ebema_lk_c_ventas1..4.png` | ronda 1 aplicada · L4 aprobada |
| 15/10 | Post estático · Crecimiento del sector (CChC 15,5 %) | `ebema_lk_post-15.10.png` | ronda 1 aplicada |
| 19/10 | Carrusel · Ebema Click: el equipo detrás de la plataforma | `c_click/ebema_lk_c_click1..4.png` | ronda 1 aplicada · L4 aprobada |
| 22/10 | Carrusel · El conteo que no puede fallar antes de despachar | `c_conteo/ebema_lk_c_conteo1..4.png` | ronda 1 aplicada |
| 26/10 | Capacitaciones | — | **PENDIENTE en la grilla** (tema, proveedor, sucursal) |
| 30/10 | Slot de contingencia | — | libre |

## Cómo se reproduce

- **Carruseles y post:** `clients/ebema/sistema-grilla/ejemplos/octubre-2026/linkedin_carruseles.py`
  (HTML → Chrome a 2250×2813). Fondos versionados en
  `public/assets/ebema/linkedin-oct26/carruseles/fondos/` (los genera `linkedin_fotos.py`
  con Seedream 5 Pro; mapa y ventas3/post con Nano Banana Pro — los prompts están en el
  script y en este archivo). Probado con `cmp`: ventas2 y conteo4 salen idénticas byte a byte.
- **Reel:** composición `EbemaLinkedinReelTalca` (`src/compositions/ebema/`). Planos en
  `public/assets/ebema/linkedin-oct26/talca/` — `clips.sh` dice cómo se hizo cada uno.
  `npx remotion render EbemaLinkedinReelTalca <salida>.mp4 --codec=h264 --crf=16`.
  ⚠️ Cierra el reproductor antes: en Windows el render falla si el mp4 está abierto.

## 15/10 — el post pasa a CARRUSEL (Paulina, 30-09: «este post es carrusel. realizar las demas slides.»)

Brief: grilla, diapositiva `id.g37d1a4a2dbc_0_172` — «CARRUSEL LINKEDIN — Crecimiento del sector,
presencia regional de Ebema». Textos **literales**; sólo se decidieron los cortes de línea y los resaltados.

| Lámina | Texto | Fondo |
|---|---|---|
| `ebema_lk_c_crecimiento1` | el post aprobado, **byte a byte** (mismo fileId `1EcwP17r…`, sólo renombrado) | foto real de Antofagasta |
| `ebema_lk_c_crecimiento2` | T2 «Más proyectos en todo el país significan más necesidad de materiales, en más lugares a la vez.» | obra de un tercero, Seedream 5 Pro (`linkedin_fotos.py crecimiento2`), sin letreros ni logos |
| `ebema_lk_c_crecimiento3` | T3 «Ahí es donde pesa contar con un proveedor presente en múltiples regiones, no solo en un punto del país.» | **satélite real** NASA Blue Marble + las 11 sucursales del manual (`linkedin_mapa_sucursales.py`) |
| `ebema_lk_c_crecimiento4` | T4 «Ebema, cerca de donde el sector está creciendo.» | cierre congelado (ventas4) sobre la bodega real de Talca desenfocada (r1) |

⚠️ **Se apartó del brief en un punto, y hay que confirmarlo:** el brief pide para la L2 un «mapa de Chile
con obras activas» y para la L3 «sucursales a lo largo de Chile». Dos mapas seguidos repetían la lámina,
así que la L2 va con foto de obra y el mapa queda para la L3 y el cierre. Si Paulina quiere el mapa también
en la L2, se arma con el mismo satélite.
⚠️ En el mapa, Quilicura y San Bernardo están a 20 px a escala país: se abrieron ±30 px en horizontal
(≈ 0,4° de longitud, los dos dentro de la cuenca de Santiago) para que se lean como dos pines.

**Ronda 1 (Paulina, 30-09):** ver bitácora; `subir_crecimiento_r1.py`, versiones previas en `_crecimiento_r1_antes/`.

Drive (`4-entregado / 2026-10 linkedin octubre / c_crecimiento`): crecimiento2 `1SlrT_48…`, crecimiento3 `1pAUwbIj…`,
crecimiento4 `1mqfotXo…`; md5 verificado. Script: `subir_crecimiento.py`. Comentario del post resuelto.

## Ronda 1 (Paulina, 25-09) — 17 comentarios, todos aplicados y resueltos en Drive

Lista completa en `comentarios-r1.json`; respuestas con `resolver_r1.py`. Reglas que
dejó y que ya están en el manual (§ LinkedIn): ropa formal en oficina, nada de
estructuras inventadas, iluminación comercial, texto donde la foto está despejada.
