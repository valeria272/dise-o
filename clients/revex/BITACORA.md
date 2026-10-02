## 2026-10-02 — Paulina Bustamante (con Claude)

**Qué se hizo:** Paulina revisó la pauta de octubre con su criterio de diseñadora y la corrigió en **tres
rondas el mismo día** (5, 6 y 7), sobre la ronda 4 que Serena había subido el 01-10. Ronda 5: cuadro rojo del
logo de story más corto (sólo un poco de aire bajo el logo) y la muestra como zoom del producto. Ronda 6:
fuera las sombras localizadas (la sombra sale del borde de abajo, suave, y parte donde empieza el texto
blanco), botón del CTA rojo, pie pegado al botón, bloque de story más abajo en SPC y alfombras, logo de app
borrado de la foto de Keraz Marmo Grey y juntas de baldosa fuera del borde de la muestra. Ronda 7: zoom
moderado (se reconoce el modelo de la baldosa) y pie de story un 15 % más grande. Paulina resolvió ella misma
los comentarios de sombra, botón, pie y bloque, y marcó `REVEX_P03C_Feed` como su referencia aprobada.

**Dónde quedó:** Las 32 piezas vigentes están en Drive, en la subcarpeta
`RONDA 7 — comentarios de Paulina 02-10 (vigente)` (`12YUrm6RKkX_w-RUonjZlaFZsushAOVnW`) dentro de «ADS Revex
octubre», con MD5 verificado. **Los archivos sueltos de los carruseles siguen siendo la ronda 4 de Serena**:
el token del estudio no puede reemplazarlos ni responder sus comentarios (`appNotAuthorizedToFile`). Script:
`scripts/revex-oct2026-piezas.py` (rondas 5–7 documentadas arriba del código) y `scripts/revex_sistema.py`
(`bloque_logo` acepta alto). Muestras nuevas en `public/assets/revex/oct/productos/` y la foto sin logo de app
en `public/assets/revex/oct/cliente/2x/`. Local: `out/revex/oct2026/`.

**Qué sigue:** Paulina mandó la ronda 7 a **Sebastián y Serena** para su OK. Si vuelven correcciones, se
aplican sobre la ronda 7 con el mismo script. Con el OK, Serena reemplaza los originales con su token (o la
pauta toma la subcarpeta) y se le muestra a Jenny.

**Abierto:** Jenny no ha visto las rondas 5–7 (la ronda 4 era su lista). Quedan 4 comentarios de Paulina
respondidos y sin resolver en la subcarpeta, y sus 2 primeros sin responder en el archivo de Serena. El cuadro
corto del logo de story contradice la medida 214,1 × 275 del manual y de `marca.json`: se aplicó sólo a este
lote. Urban no se amplió (son fichas de color). En Keraz Marmo Grey story el pie pisa los objetos del mesón.
QA: 4 bloqueantes que son falsos positivos de las fotos de la clienta (P01E, P05B y P07C story; P02A feed).
Siguen en espera las cerámicas blancas P01A/P01B (Jenny), los nombres de color del Urban (Jenny) y el copy
del anuncio de 02 (Sebastián).

## 2026-10-01 — Serena Abarca (con Claude) · entrada reconstruida el 02-10 desde los commits y el manual

**Qué se hizo:** Ronda 3: Jenny rechazó todos los ambientes con IA («las fotos ambientadas están todas
malas») y mandó 18 fotos propias; se rehízo con sus fotos y la lista bajó a 16 tarjetas (fuera las cerámicas
blancas 01A/01B en espera, Keraz Rombo y Calacatta, y las alfombras muro a muro). Ronda 4: sólo la lista de la
clienta (logo del feed centrado, story centrada con muestra-trozo, «EN OFERTA» + frase en SPC y caucho,
alfombras personalizadas) y un QA interno que reemplazó 6 stories con la muestra demasiado ampliada.

**Dónde quedó:** 32 piezas en «ADS Revex octubre» (`1puZ1PWbgaqJo53agyQHVdJSKFjUGAIvx`); las 16 descartadas
en `_fuera de la lista 30-09`. Commits `57291556`, `62ba0a62`, `5fefad62`.

**Qué sigue / Abierto:** ver la entrada del 02-10.

## 2026-09-29/30 — Serena Abarca (con Claude)

**Qué se hizo:** Se produjo el lote de **pauta de octubre** del brief de Sebastián Córdova
(`1rnAxEwixHZ5MLybEcg7SkI36FiljlBLa`): 7 carruseles, 24 tarjetas, **48 piezas** (1:1 a 2250 + story
2250×4000). Las muestras son fotos oficiales de gruporevex.cl (API WooCommerce, 22 de 26 SKU) y los
ambientes son IA (Seedream edit: misma sala, cambia el producto). Hubo QA interno (el velo cambiaba el
color del producto) y **ronda 2 con los 8 comentarios de Paulina**, todos aplicados.

**Dónde quedó:** La ronda 2 está **reemplazada en el mismo archivo** en Drive «ADS Revex octubre»
(`1puZ1PWbgaqJo53agyQHVdJSKFjUGAIvx`), con MD5 verificado, más su `ENTREGA.md`. Local:
`out/revex/oct2026/` y `~/Desktop/REVEX-octubre-2026/`. Scripts: `scripts/revex-oct2026-ambientes.py`
y `scripts/revex-oct2026-piezas.py`; material en `public/assets/revex/oct/` (versionado).

**Qué sigue:** Esperar la revisión de Paulina sobre la ronda 2. Responder y resolver sus 8
comentarios en Drive (o que los cierre ella: lo decide Serena). Cuando lleguen las fotos reales,
reemplazar el archivo en `public/assets/revex/oct/productos/` y volver a correr `revex-oct2026-piezas.py`.

**Abierto:** Faltan fotos reales de **adoquines de caucho** (P06 lleva una muestra PROVISORIA hecha
con IA), **Blanco Brillo 15×15**, **Urban 30×60** y **Brick Blanco mate** → Jenny. Confirmar los
nombres de color del Urban (Pearl / Light Grey / Anthracite) → Jenny. El copy del anuncio de 02 dice
«look del mármol» e incluye el Antique Grey, que es hidráulico → Sebastián. El QA marca un falso
positivo en P02C feed (cortina y ventana blancas al borde).

## 2026-09-09 — Valeria Traverso (con Claude)

**Qué se hizo:** No se diseñó nada; se **reparó el material de referencia** durante el arranque
del estudio. El verificador encontró 25 archivos que decían ser imágenes y eran la página de
login de Google guardada con extensión `.jpg` — el mismo problema que costó las 3 rondas de
septiembre. Se volvieron a bajar del Drive **13**, todos de Revex salvo 3 de Cava.

**Dónde quedó:** `raw/revex/ref-sep2026/` **completa y sana**: las 6 numeradas más `LCD-POST.jpg`
y `LCD-HISTORIA.jpg` — son las que señala el brief de septiembre. En `raw/revex/ref-anteriores/`
se recuperaron `rvx_post-condes.png` (2250×2813, la medida real de entrega), `_op2`, `_wtsp`,
`rvx_post-outlet.png` y `rvx_storie-condes_wtsp.png`. La receta de rescate quedó en la memoria
`compuerta-de-material` (el token local no sirve: hay que sacar los IDs por el conector de Drive).

**Qué sigue:** Antes de producir Revex, correr la compuerta —
`verificar-material.py raw/revex` y mirar la hoja de contacto— y recién ahí diseñar.

**Abierto:** Quedan **9 rotos** en `raw/revex/showroom-2024/` y los `temuco_showroom_*` de
`ref-anteriores/`: se **renombraron al bajarlos** y en Drive se llaman `0 POST VISITA SHOWROOM
TEMUCO 1.png` y parecidos, así que mapearlos sería adivinar. Si se necesitan, hay que
identificarlos a mano en el Drive de Serena. Son referencias históricas de 2024, no del brief
vigente.

# Bitácora — Revex

## 2026-08-27 — Serena Abarca (con Claude)

**Qué se hizo:** Se cerró la grilla de septiembre en 4:5 (2250 × 2812) después de seis
rondas. Se resolvieron los 10 comentarios de Paulina y los 10 de Serena. Correcciones:
los tres cuadros rojos del concurso (CONCURSO, la fecha y la dirección completa), el
interlineado de Temuco, el ícono de WhatsApp en el outlet, la textura del fondo rojo
—el patrón le ponía un velo negro al 17 % de las placas y se leían como bloques sueltos—
y el degradado del concurso, que se apagaba antes del borde y se veía cortado. Se
cambiaron tres fondos por material que mandó Paulina.

**Dónde quedó:** Las 8 piezas subidas al Drive en `DISEÑO PAID / GRÁFICAS SEPTIEMBRE`,
ordenadas en CONCURSO, TEMUCO, LAS CONDES y OUTLET. `scripts/revex-sep2026-piezas.py`
con el arreglo del outlet; `scripts/revex-sep-subir.py` nuevo (sube a una carpeta por
nombre, generaliza al de v2); `scripts/revex-outlet-textura.py` quedó obsoleto al mover
el arreglo al render. Tres fondos nuevos en `public/assets/revex/sep/`.

**Qué sigue:** Nada urgente. Si vuelve feedback, el render corre desde el repo limpio:
Valeria versionó los scripts y los 18 fondos en el commit `4351ce3`.

**Abierto:** La foto de Temuco es un frame de video cuya sucursal **no está verificada**
— el cliente compartió su carpeta TEMUCO con la fachada real del Ebema, identificada por
señalética. Regla nueva: una pieza de sucursal no se entrega sin que alguien con acceso
al original confirme la sucursal. Ver el manual, § ronda 4.

## 2026-09-02 — Serena Abarca (con Claude)

**Qué se hizo:** La clienta pidió cambiar SOLO el fondo de la portada del carrusel
«Tus muros también merecen un upgrade» por el render limpio del muro de mármol que
mandó (1000 × 1000, `public/assets/revex/sep/muros_marmol_limpia.jpg`). La pieza no
existía en el repo, así que se midió píxel a píxel la publicada
(`public/assets/revex/sep/muros_upgrade_original.png`) y se reconstruyó la capa
gráfica completa en `scripts/revex-muros-upgrade-foto-limpia.py`. Todo calza:
bloque de logo 356 × 356 a top 0 y barra 250–1797 / 944–1124 idénticos al píxel;
titular con IoU 78 % y tinta 99 % (la referencia de admisión de la marca es 71 %);
cápsula y flecha en la misma caja de 878 × 91.

**Tipografía:** el titular de esta portada es **Montserrat wght 720**, no 775. Se
identificó comparando glifos con la máscara exacta de la línea 2 —que va sobre rojo
macizo, así que su matte se extrae sin error—: 720 da IoU 83,4 % y tinta +0,9 %;
700 → 82,6 %, 750 → 79,8 %. El CTA es Montserrat 400, cap 43, tracking +0,015 em.

**Encuadre:** la foto limpia trae UNA lámpara y a cuadro pleno cae justo debajo del
bloque de logo (lámpara x 653–1022 vs. bloque x 846–1201). Se recortan 174 px por la
izquierda y 25 por arriba para que la lámpara despeje el bloque por 40 px. La variante
sin recortar queda en `--variante plena`.

**Velo:** es lo único que no se copia. El fondo viejo era un render oscuro; el limpio
es de día, con el mármol en 233 de luma, y sobre eso el titular blanco no se lee. Se
puso un degradado que arranca en y 500 —arriba el mármol, que es el producto, queda
intacto— y deja el fondo del titular en 167,7, exactamente la luma que tenía la pieza
aprobada (167,7). Segunda caída suave hasta y 1340 para que el CTA no quede flojo.

**✅ APROBADA por la clienta el 02-09-2026** sin ajustes, en la primera vuelta.

**Dónde quedó:** `out/revex/sep2026/rvx_muros-upgrade_panea_2048.png` (2048 × 2048,
mismo tamaño que la publicada, entra como reemplazo directo) + comparativa
antes/después. Copias en el Escritorio. **No se subió al Drive: no hay token de Google
en esta máquina.** Pasa el QA de marca (7 reglas).

**Qué sigue:** Subirla al Drive reemplazando la portada del carrusel en la carpeta de
entrega (`1uMPBBoOpspRKBEqtiZOElJuMEDuaisl2`) — hay que hacerlo desde una máquina con
token de Google o con el conector de Drive — y pedirle a la clienta el render del muro
en tamaño grande.

**Abierto:** La foto del cliente es de 1000 px y hay que subirla 2,48×. En el detalle
fino (el mueble de madera) la energía de borde queda en 441 contra 719 de la publicada
— se nota sólo al 100 %, no en feed. Si la clienta tiene el render en grande, se
reemplaza el archivo en la misma ruta y se vuelve a correr el script sin tocar nada más.
