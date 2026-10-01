# MyZoo · 20/10 Post Parque Pet — imagen limpia

> ⭐ **VIGENTE (Paulina, 01-10-2026): sólo queda la de los perros de pie.**
> `myzoo_post_parquepet_perros-de-pie_2250x2813.png` (feed) y `..._ALTA_3536x4421.png`.
> Todo lo demás está en `_descartadas/` y lo que sigue abajo es el historial de las rondas.
>
> **Última ronda — fondo:** Paulina vio a la gente y a los perros del fondo con malformaciones.
> Se rehízo el fondo por zonas (tres recortes cerrados, Nano Banana Pro, dos pasadas: primero
> «rehaz a la gente y los perros bien formados», después «saca lo que siga borroso») y
> `scripts/myzoo-parquepet-depie-fondo.py` devuelve cada zona sólo donde cambió, sin tocar a
> los dos perros principales, el cielo ni el letrero con el logo oficial.
>
> **Repaso final (mismo día):** Paulina pidió **sacar el logo de MyZoo del stand** (el letrero de la
> carpa queda en blanco) y repasar qué se veía «muy IA». Se corrigió: pecho y patas del beagle
> (lisos y gruesos → pelo corto y dedos definidos, `v4/bg_a.png`) y se borraron las cabinas del
> teleférico con forma de tambor, una mancha blanca y un pilar rosado en el cerro, y una rama
> cortada en el borde izquierdo. Todo está en el mismo script del fondo.
> Orden para reproducir: `myzoo-parquepet-depie.py` → `myzoo-parquepet-depie-fondo.py`.
> En Drive: `5-en-revision/2026-10_octubre/20_post-parquepet_imagen-limpia_01-10`.

**Pedido del cliente (grilla, 20/10):** «el post se ve muy falso (muuuy IA)». Que parezca
el Parque Pet: algo que se asemeje al puesto de MyZoo, actividades, gente paseando y
tutores con sus mascotas de fondo. Referencia: puesto de «Pet Store Collective» (Pinterest).

| Archivo | Qué es |
|---|---|
| `myzoo_post_parquepet_imagen-limpia_2250x2813.png` | **La recomendada.** Tamaño de feed de la marca |
| `myzoo_post_parquepet_imagen-limpia_ALTA_3536x4421.png` | La misma en alta |
| `myzoo_post_parquepet_imagen-limpia_opcionB_2250x2813.png` | Alternativa: más evento a la vista, perros algo más chicos |

Son imágenes **generadas** (Seedream 5 Pro), sin texto ni logos. La recomendada pasó por el
escalador de precisión 2×; la opción B no (el escalador falló dos veces) y está
ampliada con Lanczos desde 1770 px.

**Composición:** todo el evento queda bajo el 46 % de la altura, que es hasta donde
llega hoy el bloque de texto de la pieza (logos + titular + píldoras). El cielo de arriba
está libre.

**El puesto** va en coral con una forma amarilla y **letrero en blanco**: el logo de
MyZoo no se genera con IA; si se quiere, se monta el PNG oficial sobre el letrero.

**Cómo se hizo:** `scripts/magnific.py seedream "<prompt>" --aspecto carrusel`, **sin**
imágenes de referencia. Fuentes y descartes en `raw/myzoo/2026-10_parquepet/gen/`
(`f_seedream_sol.png` = recomendada, `g_seedream_sol.png` = opción B).

**Ojo al revisar con zoom:** junto al golden del puesto hay un perro peludo poco
definido, y el pie del niño (derecha) está algo borroso. A tamaño de pieza no se notan.

## v2 — stand corregido (Paulina, 01-10-2026)

Paulina aprobó la imagen y pidió rehacer el puesto: **sin la curva**, pancarta recta
blanca con el logo de MyZoo, logo también en el panel rosado y productos MyZoo sobre el mesón.

| Archivo | Qué es |
|---|---|
| `myzoo_post_parquepet_imagen-limpia_v2_2250x2813.png` | **La vigente**, tamaño de feed |
| `myzoo_post_parquepet_imagen-limpia_v2_ALTA_3536x4421.png` | La misma en alta |

**Cómo se hizo:** Nano Banana Pro editó sólo el recorte del puesto
(`raw/myzoo/2026-10_parquepet/stand/recorte.png` → `ed_7.png`) con los packshots reales de
referencia, dejando pancarta y panel **en blanco**. El **logo es el PNG oficial**, montado en
perspectiva por `scripts/myzoo-parquepet-stand.py`, que además devuelve el recorte a la imagen
completa. Los productos sí son generados (a ese tamaño la etiqueta no se lee): shampoo y
acondicionador de avena, espuma repelente, shampoo en seco y Odor Eliminator.

## v3 — productos y panel (Paulina, 01-10-2026)

Paulina: los cinco productos de la v2 «se ven montados muy falsamente». Pidió **sólo Odor
Eliminator perro y gato**, con luz y sombra de la escena, y **sin logo en el panel rosado**.

| Archivo | Qué es |
|---|---|
| `myzoo_post_parquepet_imagen-limpia_v3_2250x2813.png` | **La vigente**, tamaño de feed |
| `myzoo_post_parquepet_imagen-limpia_v3_ALTA_3536x4421.png` | La misma en alta |

**Cómo se hizo:** se regeneró sólo el mesón, en un recorte más cerrado
(`stand/meson.png` → `stand/me_b.png`, Nano Banana Pro con los dos packshots de referencia),
pidiendo «la misma foto, con los envases realmente ahí»: transparencia, brillo del sol y
reflejo de color sobre la madera. El logo de la pancarta sigue siendo el PNG oficial.
La letra chica de las etiquetas es generada y tiene errores («Perras», «Gotas»): a tamaño
de pieza no se lee; si la imagen se usa más grande, hay que calzar la etiqueta real.

## Opción 2 — perros de pie, sin stand protagonista (Paulina, 01-10-2026)

Paulina pidió una versión distinta: los **mismos perros, de pie, al centro y mirando a
cámara**, sin el stand de MyZoo en primer plano (cree que al cliente no le va a gustar que
se note tanto); sólo las carpas alrededor, con MyZoo como **un stand más**.

| Archivo | Qué es |
|---|---|
| `myzoo_post_parquepet_imagen-limpia_opcion2-depie_2250x2813.png` | Tamaño de feed |
| `myzoo_post_parquepet_imagen-limpia_opcion2-depie_ALTA_3536x4421.png` | En alta |

**Cómo se hizo:** Seedream 5 Pro con la imagen v1 como referencia (para conservar a los
perros) → `raw/myzoo/2026-10_parquepet/v4/s_b.png` → escalador de precisión 2× →
`scripts/myzoo-parquepet-depie.py`, que recorta a 4:5 y monta el logo oficial, chico, en el
letrero blanco de la carpa de la izquierda (la del mantel coral).

**Ojo:** las orejas del border collie llegan al 47,5 % de la altura; el bloque de texto actual
termina en el 46 %. Cabe, pero justo.
