# EBEMA / EBEMA CLICK — bitácora

> Una entrada por jornada, la más nueva arriba. Lo de hoy se escribe hoy: el
> relevo de mañana lee esto antes de abrir cualquier archivo.

## 2026-09-14 — Paulina Bustamante

**Qué se hizo:** Se produjo la **story 19** de la grilla de septiembre (Ebema Click,
sticker de enlace) como prueba del pipeline — y esa prueba destapó el problema real
del mes: **todo lo que este manual llamaba «el sistema» era el sistema de PAID**.
`sistema/base.css` lo decía en su primera línea desde siempre («EBEMA PAID —
Septiembre 2026») y las referencias que sostenían §4 salen de
`EBEMA/PERFORMANCE/2026/8. Agosto/`. La story se calcó de anuncios y **queda
descartada como entrega**. A partir de ahí, y con las referencias de grilla que dejó
Paulina (5 carruseles, 3 stories, 6 posts, 5 reels), se **midió la gramática de
grilla completa** y se escribió el **sistema de producción que no existía**.

Tres correcciones de Paulina quedaron codificadas el mismo día:
- **Grilla y paid son sistemas distintos**, y no se organizan por el mismo eje:
  grilla por **familia de contenido** (producto en stock · información de servicio ·
  invitación a plataformas) y paid por **submarca**. **SPC no existe en grilla**: son
  ofertas puntuales que pide el cliente, y van a paid.
- **Acá sólo se diseña** (§0-bis): el brief lo arma contenido y trae decidido el
  proveedor, el formato, el pilar, los textos y el ángulo. Una discrepancia **se
  informa, no se resuelve**.
- **Lo que el brief pide generar va por Magnific**: `text-to-image/nano-banana-pro`
  para imagen, `image-to-video/kling-v2-5-pro` para video.

**Dónde quedó:**
- `clients/ebema/CLAUDE.md` — §0 la matriz y cómo se pide una pieza · §0-bis sólo se
  diseña · §4 el esquema Click de paid corregido · **§4-bis la gramática de grilla
  medida** (ancla de marca, las 3 familias, el arco de carrusel, la story y el reel).
- `clients/ebema/sistema-grilla/` — **nuevo**: `base-grilla.css`, `build_carrusel.py`,
  `render.sh` (diseña a 1080, entrega a 2250). Calibrado contra `ebema_c_cedral5`:
  el botón de WhatsApp sale idéntico al píxel y el anillo con menos de 1 px.
- `raw/ebema/1-referencias/` — partido en `grilla/` y `paid/`, y dentro por formato.
- `out/ebema/20260914_st19_click/` — la story descartada, con el aviso en su
  `ENTREGA.md`. **No se subió al Drive.**
- `scripts/_chrome.sh` — los 5 `render.sh` del estudio tenían quemada la ruta de
  Chrome del Mac y no corrían en Windows. Arreglados y probados.

**Qué sigue:** **aparear la grilla de septiembre con sus piezas** — emparejar cada
diapositiva del deck con la pieza que salió, para aprender la traducción brief →
pieza, que es lo que va a hacer falta en octubre. Lo hace Claude solo; Paulina sólo
revisa el apareo y corrige.

**Abierto:**
- 🔴 **Kling 3.0 no está disponible por API.** Sondeado hoy: no aparece en el
  catálogo de nuestra clave ni como fuera de plan; el tope que responde es Kling 2.5
  Pro. Si Paulina genera con Kling 3.0 lo hace en la **web** de Magnific → hay piezas
  que ella puede hacer a mano y que no se reproducen por código. **Decisión pendiente:
  subir el plan de Magnific, o que ella genere los videos y acá se monte.**
- Faltan los **logos de los proveedores** (Cedral, Cintac, Novoplast, Surpol, Toro,
  Polpaico, CMPC, VH) y el **PNG de la flecha** del pie de portada. Sin ellos la
  cápsula de co-marca queda coja. Van en `raw/ebema/3-logos-y-packshots/`.
- Faltan **rondas con corrección** (piezas rechazadas + su versión corregida). Es lo
  que más enseña y lo único que no se puede deducir midiendo.
- **EBEMA sigue sin `clients/ebema/reglas.yaml`**, así que `qa/motor.py --marca ebema`
  se niega a correr y el QA se hace a mano. Viene pendiente desde el 01-09.
- Sin generador para las familias **B** y **C** (sus medidas ya están en el CSS) y sin
  pipeline de reel en Remotion.

## 2026-09-02 — Valeria Traverso

**Qué se hizo:** Valeria pidió **otro diseño** para el carrusel de Cedral de la
grilla de septiembre (slide 6 del deck `1wHJf4hxDgait…`). Se produjeron **dos
rutas completas de 5 láminas cada una**, con los textos verbatim del brief:
**Ruta A «Método»** conserva la gramática de Paulina (marco, caja de logo saliendo
del borde, caja roja detrás de la 2ª línea completa y de la mitad de la 1ª, botón
sin sombra) y le suma portada partida antes/después con corte rojo de 12 px, caja
roja del número **espejo exacto de la caja del logo** (152×186, `top:0`, radio
inferior 14), barra de avance de 5 tramos en el lugar de los puntitos, y cierre en
rojo plano con las planchas en panel. **Ruta B «Zócalo»** rompe el centrado: la
foto limpia hasta 970 px y el texto en un zócalo blanco de 380 px alineado a la
izquierda, con el número de paso en Helvetica Bold al 13 % de ancla.
Los 6 fondos se generaron con **Nano Banana Pro** siguiendo las reglas de imagen
de Paulina (plano amplio, ropa de trabajo, obra ordenada, sin marcas legibles).
El par antes/después de la portada se sacó **usando el «después» como referencia**,
para que la casa, el ángulo y el encuadre sean los mismos.

**Dónde quedó:** entrega en `out/ebema/20260902_carrusel_cedral/` (`ENTREGA.md`,
`editables/build.py`, `editables/carrusel.css`, 10 PNG en `feed/`); la capa nueva
también quedó en el sistema, en `clients/ebema/sistema/carrusel.css`, para reusarla
en los otros carruseles de la grilla; los fondos versionados en
`public/assets/ebema/cedral/` (JPEG 93, excepción de `.gitignore`); el generador en
`scripts/ebema-cedral-fondos.py`. Página comparativa publicada para Paulina y
Carlos: `claude.ai/code/artifact/8c6ca8ad-23f7-4a0e-97a7-7214e52b32a6`.
**QA hecho:** las 10 piezas a 1080×1350 y rojo `#EC1C23` exacto verificado píxel a
píxel — el primer cierre iba en duotono rojo sobre la foto y daba **91 tonos de
rojo**, así que se rehízo en rojo plano con la foto en panel.

**Qué sigue:** que Valeria y Paulina elijan ruta. Elegida una, subir las 5 láminas
a `PERFORMANCE/2026/9. Septiembre/graficas septiembre 26/` con la nomenclatura del
portal, y extender la ruta al resto de los carruseles de septiembre (Novoplast,
Toro, Metalcon, Surpol), que tienen la misma estructura de 5 láminas.

**Abierto:**
1. **⛔ Falta el logo de Cedral** — no está en el kit oficial ni en el banco. Acá
   va como kicker tipográfico. Hay que pedírselo a Paulina o al proveedor y armar
   el lockup EBEMA + CEDRAL.
2. **Las fotos son IA.** Si Pizarreño/Romeral tiene material propio de Cedral,
   ese manda y hay que rehacer los fondos.
3. **El `18` del titular en Helvetica Bold.** La regla dice que *toda* cifra va en
   Helvetica Bold y acá se aplicó también dentro del titular; en la pieza que está
   hoy en la grilla se ve en Raleway. Lo decide Paulina.
4. Los kickers `01 · INSTALACIÓN` / `02 · DURABILIDAD` / `03 · TERMINACIÓN` son
   míos, no del brief. Si el cliente los quiere fuera, se borran sin tocar nada más.

## 2026-09-01 — Serena Abarca

**Qué se hizo:** Paulina pidió por Slack generar las 12 campañas ARIEL de WhatsApp
de septiembre desde una pieza madre suya (`ebema_wtsp_piazza.png`, 2500×4510,
armada con la info de A1), cambiando enunciado ferretero/contratista, precios y
dirección. Se produjeron **6 de 12**: el bloque completo de **LÍNEA PORTEZUELO
(A1–A6)**, por parcheo sobre el píxel de la diseñadora — 0 píxeles modificados
fuera de las zonas de precio, enunciado y dirección. Las tipografías se
identificaron midiendo, no suponiendo: enunciado Raleway SemiBold, dirección
Raleway en peso 450 (que no existe como archivo estático, hubo que traer la
Raleway variable de Google Fonts).

**Dónde quedó:** entrega en `out/ebema/20260901_wsp_A1-A12_piazza/` (`BRIEF.md`
con el brief verbatim del Sheet, `ENTREGA.md` con el QA, `madre/`, `piezas/`,
`qa/`); generador en `scripts/ebema-wsp-piazza-variantes.py`; Raleway variable en
`clients/ebema/sistema/fonts/`. Copia para revisión en el Escritorio de Serena
(`EBEMA Click - WhatsApp Septiembre 2026/`) con `LEEME.txt` y hoja de contacto.
Las 6 piezas de Portezuelo están **rendidas y revisadas**; no hay nada a medias.

**Qué sigue:** cuando Paulina mande **la pieza madre de LÍNEA AZTECA Y CALYX**,
medir su geometría con el mismo método y extender el generador con el bloque
A7–A12 (envío 04/09). La receta de parcheo ya está resuelta, es rápido.

**Abierto:**
- **A7–A12 no son variantes de la madre de Portezuelo** — otro título, otros
  packshots y 3 productos en vez de 4. Esperan su propia madre. Diseñarlas por
  cuenta propia es el error nº1 de §9 de este manual.
- La planilla marca la **Llave Individual Azteca (529779)** como «PRECIO
  PENDIENTE, no incluir hasta recibirlo» → se le pide a Ariel antes del 04/09.
- El brief pide **añadir el logo Piazza** en el bloque Azteca y Calyx.
- **EBEMA no tiene `clients/ebema/reglas.yaml`**, así que `qa/motor.py --marca
  ebema` se niega a correr y el QA de hoy se hizo a mano contra el checklist de
  §8. Queda por escribirlas y firmarlas con Paulina.
