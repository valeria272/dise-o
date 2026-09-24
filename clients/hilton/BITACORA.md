## 2026-09-24 (noche) — Eli (Windows) · DT: /abrir + /al-dia — SIN PIEZAS

**Qué se hizo:** sólo apertura de DT. Pull (trajo EBEMA y Tierra Calma, nada de Hilton),
siembra de memoria y diff por conjunto de cadenas de las dos grillas de DT contra sus
instantáneas. **Septiembre:** «Tu día en DoubleTree» (FEED!O15) pasó a **APROBADO**
(cierra la ronda 10); Día del Turismo (M15) sigue CORREGIDA sin comentario nuevo; el
reel orgánico del 25-09 (F16) pasó de POR GRABAR a EN REVISIÓN con «VIDEO EDITADO»
(no lo editó este estudio); Honors 23-09 PROGRAMADO. Cero hilos de comentario nuevos
después del 23-09 19:33Z. **Octubre:** sin cambios desde la mañana (última edición 23-09
18:51Z).
**Dónde quedó:** instantánea nueva `clients/hilton/grillas/api/dt-sept-20260924.json`
(base del próximo diff) y `clients/_estado-sync.json` → `dt`. En Drive, Eli creó hoy
`S1…S5 HILTON OCT 2026` (`1KDBVTVib5O-sm__EfNadZibN9gnB2lcE`), pero sólo tienen
subcarpeta BW: todavía no hay carpeta DT.
**Qué sigue:** partir octubre por la ST animada Family Time del 1-oct (la más próxima);
después Opinión Expedia (FEED 10-oct), Servicios (ST 13-oct), Reel Honors POV (FEED
14-oct) y Honors beneficios (ST 30-oct). Confirmar con Eli cuál toma y avisar el tiempo
estimado antes de partir.
**⚠️ Corrección al cierre:** mientras se escribía esta entrada, **otra sesión en el mismo
árbol ya estaba produciendo octubre de DT**: `DtStFamilyTimeOct.tsx`, `DtStServiciosOct.tsx`,
`DtStHonorsOct.tsx`, `dtIconosOct.tsx`, `src/DtOctEntry.tsx`, `scripts/dt-oct-fotos.py` y
`dt-oct-20260924b.json`. El `git add -A` de este cierre los subió **a medio hacer** dentro
del commit 1d0b5d4, que no es de esa sesión. No son piezas terminadas ni aprobadas: la
bitácora de ese trabajo la escribe su propio `/cierre`.
**Abierto:** el estado real de las 3 stories de octubre que ya están en código. El Reel Honors POV necesita
**grabar** entrada y recepción (producción). Cinco piezas siguen en REVISAR CONTENIDO y
dos reels orgánicos POR GRABAR. El carrusel del 21-oct tiene comentario del cliente
(«que sean 5…») pero no tiene estado. La portada definitiva de «Tu día» ya no urge:
el carrusel quedó aprobado con la del lobby.

## 2026-09-24 (tarde) — Eli (Windows) · BETWEEN: grilla de OCTUBRE, las 11 piezas OK PARA DISEÑAR — APROBADAS, sin subir

**Qué se hizo:** se diseñó todo lo OK PARA DISEÑAR de la S1 a la S5 de la grilla de octubre
(leída en vivo): 9 historias (01-10 ganador concurso · 02-10 To Go POV animada 8 s ·
05-10 collage «Paso por un café y…» · 07-10 cumpleaños · 08-10 trivia · 19-10 cowork ·
20-10 lo dicen ustedes · 27-10 espacio para tu evento · 28-10 Bonjour) y 2 feed (05-10
reunión · 14-10 espacios). Cuatro rondas con Eli en el día; **todas aprobadas**. No se hizo
el 26-10 «WTF…» (dice GRABAR ORGÁNICO) ni lo que está en revisión/pendiente.
**Regla nueva de Eli:** ⛔ sin rostros de modelos, sólo del cuello hacia abajo → manual § OCTUBRE 2026.
**Dónde quedó:** entrega final en `out/hilton/between/entrega-oct/` (10 PNG a 2250 + MP4
1080×1920 + portada, y 6 guías en `GUIAS CM/`). Página de revisión en
`out/hilton/between/oct-revision/index.html`. Código `src/compositions/hilton/BetweenOctubre.tsx`
+ `src/BetweenOctEntry.tsx`; escenas `scripts/between-oct-generar.py` (Nano Banana Pro);
el video salió de Seedance 2.5 en el Space de Magnific «Between octubre». Fondos usados,
versionados en `public/assets/hilton/between/oct/`.
**✅ SUBIDO (24-09, 14:05):** con `scripts/between-oct-subir-drive.py` a
`10. OCTUBRE / S<n> HILTON OCT 2026 / BW / {STS, FEED}`, en orden y con la semana de la
grilla (feed 05-10 → S1, feed 14-10 → S4). 12 archivos verificados por el conector en su
carpeta. Las GUIAS CM NO se subieron (quedan en `entrega-oct/GUIAS CM/`).
**Qué sigue:** entregarle las GUIAS CM al CM si las pide; el 26-10 «WTF…» cuando esté grabado.
**Abierto:** (1) 20-10 «Lo dicen ustedes» lleva los EJEMPLOS del brief: faltan reseñas reales.
(2) 02-10 va «$2.990» (el brief dice «$2,990»). (3) 05-10 dice «UNA BUENA CONVERSA» (brief:
«CONVERSACIÓN»). (4) 01-10: falta el @ del ganador (sticker de mención). (5) 19-10 lleva
«Between Coffee & Bar» con pin, calcado del «Semusin Cafe» de la ref — no está en el brief.
Eli lo vio todo bien, pero no se le preguntó explícito por (1)–(3) y (5).

## 2026-09-24 — Eli (Windows) · Arranque de máquina + qué está OK PARA DISEÑAR en octubre — SIN PIEZAS

**Qué se hizo:** `/arranque` en la máquina Windows: todo en verde (Node, Chrome,
Python, llavero abierto, Magnific válido, token de Drive responde, TS compila). Después
se leyeron las 4 grillas de octubre **en vivo** (DT/QB/P18 por API de Sheets; Between
por export CSV con gid, porque la de octubre sí lo acepta) y se listó sólo lo marcado
`OK PARA DISEÑAR`/`OK PARA DISEÑO`: **28 piezas** — DT 5 (Family Time animada 1-oct,
Opinión Expedia 10-oct, Servicios 13-oct, Reel Hilton Honors POV 14-oct, Honors
beneficios 30-oct) · QB 11 stories (1 al 26-oct) · Between 10 stories + 2 feed
(1 al 28-oct) · **Piso18 0**.
**Dónde quedó:** instantáneas nuevas `clients/hilton/grillas/api/{dt,qb,p18}-oct-20260924.json`
(base del diff de mañana). Between quedó sólo en el scratchpad (CSV); no se versionó.
**Qué sigue:** Eli elige por dónde partir; lo más próximo es 1-oct (DT Family Time
animada, QB Banco de Chile, BW Anuncio ganador concurso) y 2-oct (BW Promos To Go).
**Abierto:** QB 14-oct «Adivina el trago» trae comentario del cliente («Ok, pero con
alternativas, siento que cuadro de respuesta no responden»). QB 22-oct: anclar a la
recomendación del chef + leyenda «Imagen referencial» en todo material no real (ya
anotado en `clients/qb/CLAUDE.md` §5). La vista mensual de QB sigue diciendo «AGOSTO»
(pestaña vieja), pero las STORIES sí son de octubre. BW 26-oct «WTF…» es orgánico **por
grabar**. No se sabe cuáles de las 28 ya tiene empezadas Eli.

## 2026-09-23 (noche) — Eli (Windows) · DT «Tu día»: ronda 10, rótulo del cierre — SUBIDO

**Qué se hizo:** Javier Mesa (chat): «cambiemos este último texto por "CERRANDO EL
DÍA"». La lámina n°7 pasa de «20:00 — CIERRE EN LA HABITACIÓN» a «20:00 — CERRANDO
EL DÍA»; la hora se mantiene. Misma «C» inicial, así que la sangría del sello no
cambia. QA en verde (sello 11,39:1, tinta en x=89).
**Dónde quedó:** `C1 S5 DT n°7.mp4` y `n°7.gif` **reemplazados en Drive** (mismo
enlace) en `C2-28SEP` y `C1 S5 DT - GIF`; los 14 verificados por md5. La versión
anterior quedó respaldada en `out/hilton/dt/c1-s5/entrega-r9/`.
**Qué sigue:** nada: con eso el cliente da el OK.

## 2026-09-23 (tarde) — Eli (Windows) · BW: reel orgánico «Sea la razón que sea» (ORGÁNICOS, S4 24-09), rondas 1–4 — SUBIDO

**Qué se hizo:** reel de repetición calcado de la referencia de IG (la misma entrega
×8, 1 texto literal del brief por repetición, Raleway ExtraBold blanca), armado como
**proyecto EDITABLE de After Effects** por script (`scripts/bw-reel-razon-ae.jsx`).
R1–R2 con la toma real IMG_4389 → Eli: «muy quemado», «que la toma sea bonita» →
**no aprobado**. R3: toma hecha con IA en Magnific (Space «BW Reel S4 · Sea la razón
que sea»): IMG_4406 extendida a 9:16 → mesa vacía con Nano Banana → Seedance 2.5 con
primer fotograma = mesa vacía y último = foto real. Eli: «el resultado del Space muy
excelente», pero el color gradado «se ve mal» → R4: color de Magnific + 8 % de
saturación, sin contraste ni viñeta; el texto lleva halo difuso (sombra 80 %,
suavidad 34) para leerse sobre el fondo claro.
**Dónde quedó:** `S4 HILTON SEP 2026 › BW › REEL S4 SEA LA RAZÓN QUE SEA`
(`1kMjU0i2pZZ4hQN8s44cifW3ZxZqad2AA`): `BW REEL 24-09 Sea la razon que sea.mp4`
(12,5 s), `- PORTADA.jpg` y `- EDITABLE AE.zip` (.aep + toma en ProRes). Local en
`out/hilton-between/reel-sea-la-razon/` con `_ronda1..3` aparte. Material crudo e IA
en `raw/hilton/between/reel-sea-la-razon/` (+ `ia/`).
**Qué sigue:** esperar la revisión de Eli de la R4. Si pide otro ajuste de texto o
ritmo: editar variables al inicio del `.jsx` y relanzarlo (con AE YA abierto y desde
una ruta sin espacios — ver memoria `after-effects-desde-script`).
**Abierto:** (1) en la grilla, COMENTARIOS CLIENTE de esta pieza dice «Cambiémos este
para QB para variarr» — se siguió en BW porque Eli lo pidió así; no se verificó si
está tachado. (2) La carpeta del material (`14jkKd…`) tiene dos copias de clips de
Ámbar (IMG_2084/2079) a nombre de constanza.olivares@ que ya no se usan: borrar si
Eli dice. (3) Sin música: la pone CM con el audio en tendencia.

## 2026-09-23 (tarde) — Eli (Windows) · DT «Tu día»: la portada pasa al LOBBY (provisoria) — SUBIDA

**Qué se hizo:** Eli pasó dos enlaces nuevos para la portada («utilízalas por ahora,
después la reemplazamos»): `14L5gK…` (jarrón con ramas frente al espejo) y `1IU97W…`
(paneo por las lámparas doradas del lobby). Montaje de 2 cortes con fundido de 0,3 s
(`MONTAJE_PORTADA` en `dt-c1-s5-clips.py`). Son SDR bt709, no HLG: no se tonemapean.
⛔ Con `-filter_complex` el mp4 HEREDABA la matriz −90° del iPhone y salía acostado;
se arregla con `-display_rotation 0` en la entrada + `transpose=1`. QA en verde
(peor: «Tu día» 5,84:1 sobre 3,0).
**Dónde quedó:** `C1 S5 DT n°1.mp4` y `n°1.gif` **reemplazados en Drive** (mismo
enlace), los 14 verificados por md5. La portada de la entrada quedó respaldada en
`out/hilton/dt/c1-s5/entrega-r8/C1 S5 DT n°1-entrada-r9.mp4`.
**Qué sigue:** reemplazar la portada cuando llegue el material definitivo.
**Abierto:** la toma definitiva de la portada.

## 2026-09-23 — Eli (Windows) · DT: carrusel «Tu día en DoubleTree» (FEED 28-09), rondas 8 y 9 — SUBIDO

**Qué se hizo:** ronda del cliente (grilla FEED celda O14) + dos correcciones de Eli.
Videos cambiados por los que el cliente enlazó en el brief: desayuno «Syrup», salón
vacío, Winter Garden con notebook, plato de QB. Gym = **montaje de 4 cortes** de la
carpeta «VIDEOS DADOS POR CLIENTE» (IMG_2662–2665). Habitación = IMG_4122, la de la
tarjetita del reel «Habitación lista» (pedido de Javier Mesa por chat). Portada =
**la entrada** (puertas de vidrio de IMG_1640, recorte que deja fuera el logo), sin
«Desliza». Las interiores quedan sólo con el sello: hora Trade Gothic Regular +
rótulo Trade Gothic Bold Cn, **mismo cuerpo 50**. **Entra QB 19:00** y la habitación
pasa a 20:00: el carrusel tiene **7 láminas**. QA en verde (lo más justo:
«Santiago–Vitacura» 4,52:1 sobre 4,5).
**Dónde quedó:** 7 MP4 (2160×2700, 5 s) + 7 GIF (720 px, 12,5 fps, sin dither)
**subidos y verificados por md5** en `S5 HILTON SEP 2026 › DT › C2-28SEP`
(`1WXTx7b62fI5-heMZ0PDu85zCJWBxq1y3`) y su subcarpeta `C1 S5 DT - GIF`. El cierre se
**renombró** n°6 → n°7 (mismo enlace, contenido nuevo) y QB entró como n°6 nuevo.
Revisión: `out/hilton/dt/c1-s5/revision-r9.html`. Rondas anteriores respaldadas en
`out/hilton/dt/c1-s5/entrega-r7/` y `entrega-r8/`. Clips fuente en
`raw/hilton/dt/s5-sept/clips-r8/` (no viajan; ids en `dt-c1-s5-clips.py`).
**Qué sigue:** esperar la validación del cliente; si objeta la portada, las 6 tomas de
`EXTERIOR HOTEL` 2024 (ambar, `1wT-h-O08xoaNIkCG7s2uQuwMUtpbpZ1N`) están sólo al
dominio: hay que pedir que las bajen y las pasen por enlace abierto.
**Abierto:** que el cliente apruebe la portada de la entrada (en la toma entra una
huésped de espaldas y el vidrio refleja la calle).

## 2026-09-23 — Eli (Windows) · DT: carrusel DÍA DEL TURISMO, ronda 2 (sin punto)

**Qué se hizo:** el cliente aprobó el carrusel con un solo ajuste: «ojo con los puntos en
títulos y subtítulos». El único punto del carrusel era la bajada de la portada («Hoy
celebramos las ganas de descubrir.»), y se quitó. Se volvieron a rendir **solo** la
portada `C1 S5 DT n°1.mp4` y su GIF, y se subieron a Drive reemplazando los archivos, así
que el enlace no cambia. Las láminas 2 a 6 no se tocaron.
**Regla nueva:** recordatorio del cliente para las grillas de octubre: **ni títulos ni
bajadas llevan punto**, en las cuatro cuentas. Queda en `CLAUDE.md` §F (se corrigió la
redacción que dejaba pasar la bajada) y en los manuales de QB y Piso18.
**Dónde quedó:** `src/compositions/hilton/DtC1Turismo.tsx` (bajada sin punto), render en
`out/hilton/dt/c1-turismo/entrega/C1 S5 DT n°1.mp4` y `entrega-gif/C1 S5 DT n°1.gif`,
los dos subidos y reemplazados en `C1 N°1 S5 TURISMO` (el MP4) y en `C1 S5 DT - GIF` (el GIF).
**Qué sigue:** nada. El carrusel queda entregado. Para octubre: antes de rendir cualquier
pieza del complejo, revisar a ojo que ni títulos ni bajadas lleven punto
(`qa/motor.py` todavía no lo comprueba).
**Abierto:** logo solo en la portada (así se entregó) o en todas las láminas: el cliente
aprobó sin pedirlo, así que queda como está salvo que Eli diga otra cosa.

## 2026-09-23 — Eli (Windows) · DT: carrusel video DÍA DEL TURISMO (FEED col M, 27-09), ronda 1

**Qué se hizo:** se diseñó el carrusel de 6 láminas del brief (G1 portada foto + MUT,
Parque Bicentenario, Sky Costanera, Cerro San Cristóbal y Barrio El Golf en video),
según la referencia de Eli (`REF C1 S5 TURISMO`, dos láminas Bronnuti: todo centrado,
logo arriba, filete + nombre al tercio inferior). Portada = `HDT_42` (frontis con plaza,
distinta a la `HDT_43` de la story). MUT y El Golf salen del Drive; **Bicentenario, Sky y
San Cristóbal salen del stock de Magnific** (290160, 6133095, 5625808) porque las
carpetas de Bicentenario y Sky son sólo-dominio y la de San Cristóbal traía un clip
inservible. Se sacaron del cuadro tres marcas ajenas: Bci (El Golf), Mastercard (Sky) y
el pendón «MUT» que duplicaba el titular. QA de contraste limpio en f0 y f149.
**Dónde quedó:** 6 MP4 (2160×2700, 5 s) **subidos** a `S5 HILTON SEP 2026 › DT ›
C1 N°1 S5 TURISMO` (`1hRg3QUZ3KWAEhBFr4ZcYYR6MYDbWdds5`) como `C1 S5 DT n°1…6.mp4`,
verificados por peso contra el local. Revisión para Eli:
https://claude.ai/artifact/Fi2LkYypYQCQ1uY41ZJaZ2. Aparato: `scripts/dt-c1-turismo-{clips,qa,rendir,revision}.py`
+ `src/compositions/hilton/DtC1Turismo.tsx` (carpeta `DT-Carrusel-Turismo` en `DtEntry`).
**GIF (mismo día, pedido de Eli «dejes en gif ahora»):** 6 GIF 720×900, 12,5 fps, sin difuminado (`scripts/dt-c1-turismo-gif.py`) en `C1 N°1 S5 TURISMO › C1 S5 DT - GIF` (`1cr-rQfv2RFsv5yeBi66JWGZyAcgJs7Fg`), verificados por peso. 14–29 MB: para WhatsApp hay que rehacerlos con `--ancho 540`.
**Qué sigue:** la pieza está ENTREGADA completa (MP4 + GIF). Sólo se vuelve a tocar si
llega ronda de Eli o del cliente: `dt-c1-turismo-rendir.py` → `dt-c1-turismo-gif.py` →
`drive-subir.py` (reemplaza por nombre en la misma carpeta y conserva el enlace).
Si pide logo en las interiores: `--con-logo` y correr el encuadre de Sky (el logo cae
sobre la punta de la torre).
**Abierto:** decisión de Eli: ¿logo sólo en portada (entregado) o en todas (como la ref)?
El brief numera dos «G4» (informado, no se tocó). La carpeta `C2-28SEP` recibe el carrusel
«Tu día», cuyos archivos siguen llamándose `C1 S5 DT n°…` — que Eli diga si se renombran.

## 2026-09-22 · Eli (Windows) — DT: el carrusel S5, ronda 7 (el bloque de la portada, final)

**Qué pidió Eli**, seguido sobre el render de la ronda 6: (1) «quiero que el
Santiago - Vitacura esté más pequeño como antes, y listo»; (2) «y el texto de:
by Hilton en el mismo peso del "En DoubleTree"».

**Cómo quedó el bloque, y es la forma final:**

| nivel | texto | tipografía | tinta |
|---|---|---|---|
| 1 | «Tu día» | Stag LightItalic 72, circulada | 187,1 |
| 2 | «en DoubleTree» | Stag **Medium 108** | 731,5 |
| 2 | «by Hilton» | Stag **Medium 108** | 460,2 |
| 3 | «Santiago–Vitacura» | Stag Light **42**, +0,02em | 347,4 |

⭐ **El titular quedó a UN peso y UN cuerpo.** La ronda 6 lo tenía a dos pesos
—Medium + Light—, que es la receta escrita de DT; Eli pidió el segundo renglón
también en Medium. El nombre del hotel se lee entero con la misma voz y quien
marca el cambio de nivel es la ciudad. No contradice el manual: la receta da el
recurso, y cuál de sus formas entra en una pieza es composición, que es de ella
(la misma regla con la que sacó el verde en la ronda 2).

⚠️⚠️ **LA SANGRÍA NO SE HEREDA AL CAMBIAR DE PESO** — y es la lección de la
ronda. La «b» de Stag Light vuela hacia afuera 1,404 px y la de la Medium
**2,592**: dejar el valor viejo deja el renglón 1,2 px corrido. Se re-midió, la
tinta nace en x=88 y el QA del canto izquierdo lo confirma.

⚠️ **El aire de la ciudad se mide contra la LÍNEA BASE, no contra la tinta.**
Arriba está «by Hilton», cuya «y» baja 17 px bajo la base; medir el hueco contra
ese descendente engaña. Quedó en **46 px bajo la base** (29 de tinta a tinta),
que es el mismo aire óptico que tenía la bajada de la ronda 5 contra un renglón
sin descendentes.

⭐ Y la ciudad, al volver a cuerpo 42, **vuelve a ser texto chico**: el QA le
devolvió la vara de **4,5:1** (en la ronda 6, como renglón de titular a 108, se
medía contra 3,0). Da 7,30.

**Entregado.** Sólo la portada viajó otra vez: `C1 S5 DT n°1.mp4` y `.gif`
reemplazados en sitio, mismo `fileId` y mismo enlace. Los 12 archivos del Drive
verificados por md5 contra el local.

**Dónde quedó:**
- Página de revisión: `out/hilton/dt/c1-s5/revision-r7.html` —
  `scripts/dt-c1-s5-revision-r7.py`.
- QA **en verde** · el peor sigue siendo «Tu día» con 3,35:1 sobre vara 3,0 ·
  typecheck limpio.

**Qué sigue:** nada abierto. Eli cerró con «y listo».

---

## 2026-09-22 · Eli (Windows) — ⭐ LA COMPUERTA DE QA SE ENCIENDE POR PRIMERA VEZ

**Qué se hizo.** Sesión de eficiencia, no de producción: Eli preguntó cuánto toma
una corrección y cómo bajarlo. Se midió sobre el propio historial (336 commits de
septiembre) y salieron dos cosas, una esperada y una grave.

**1. El hallazgo grave: `clients/hilton/reglas.yaml` no existía.** `qa/motor.py`
aborta si a la marca le falta ese archivo, así que **ninguna pieza de Between ni de
DT pasó la compuerta en todo septiembre** — 92 commits de Between y 41 de DT, las
dos cuentas más pesadas del estudio, entregadas sin pasar ni siquiera por las cinco
reglas de agencia que sí corren en Casablanca, Revex, CAVA, QB y Piso18. No es que
el QA fuera permisivo con estas dos marcas: no corría.

**2. Se escribió el archivo, calibrado contra material real.** 12 piezas aprobadas
de Between y 3 de DT. Topes medidos: `respiro-borde` 0,050 (Between llega a 0,032,
DT a 0,044 — la máscara toma la fotografía a sangre, no sólo el texto) y
`foto-estirada` 0,012. Más una regla de marca: **«Café XL»**, con la cita literal de
la grilla de octubre, acotada a Between con `solo_archivos`.
✅ Verificado en modo control: **10 de 14 aprobadas pasan limpias**.

### ⛔ El resultado que importa: el QA mecánico NO atrapa los rechazos de Eli

Se calibraron las **12 aprobadas contra 10 rondas rechazadas** de Between. Ninguna
de las cinco métricas separa un grupo del otro:

| métrica | aprobadas | rechazadas |
|---|---|---|
| costura | 9,4 – 76,7 | 9,4 – 25,2 |
| desenfoque-parcial | 0,005 – 0,423 | 0,369 – 0,548 ← al revés |
| foto-estirada | 0,000 – 0,011 | 0,000 – 0,000 |
| paleta-cerrada | 0,355 – 1,000 | 0,800 – 1,000 |
| respiro-borde | 0,000 – 0,032 | 0,024 – 0,043 |

**Between no se rechaza por defectos, se rechaza por criterio** — la caja beige que
no destaca sobre papel beige, el milkshake que no era el producto, la torta sobre
mármol cuando sus hermanas van sobre madera. Eso no lo ve un histograma. Queda
escrito para no volver a intentar el atajo.

Los 4 avisos del modo control son todos `desenfoque-parcial` sobre **la banda del
borde**. Se midió si eran gráfica lisa —en cuyo caso bastaba subir el umbral del
guardia— y **no lo son**: desviación 7,9 · 14,4 · 21,0 · 26,3, contra 16,0 · 27,1 ·
40,0 · 40,2 en las que pasaron limpias. Lo que ve es **el velo** con que las dos
marcas apagan el canto de la foto, que es recurso aprobado. Se deja como aviso.

**Dónde quedó.**
- `clients/hilton/reglas.yaml` — nuevo, con PENDIENTE detallado
- `scripts/_revision.py` — nuevo. El molde de la página de revisión: hasta hoy cada
  ronda era un script de ~300 líneas copiado del anterior (21 scripts, 6.356 líneas,
  y entre rondas seguidas sólo cambiaban 160). Con el molde son ~40. Probado
  rehaciendo la ronda 9 del concurso: **65 líneas contra 237**, y rendido en Chrome
  para confirmar que se ve igual. Los 21 viejos NO se migran: ya se entregaron
- `qa/calibrar.py` — arreglado. Reventaba con `UnicodeEncodeError` (cp1252 y la
  flecha «→»), o sea que **en el Windows de Eli nunca se pudo calibrar una marca**.
  Es parte de por qué Between y DT seguían sin topes

**Qué sigue.** Convertir en `qa/checks.py` las lecciones ya medidas —la foto de
carrusel se aprueba montada, el contraste no ve la textura, igualar la luz no iguala
el material—. Eso es lo que atacaría los rechazos de criterio, que es donde está el
tiempo. Calculado: ~1 día, y hace falta corpus de rechazadas para validar que cada
check separe de verdad.

**Abierto — dos preguntas de criterio para Eli, cada una enciende una regla:**
1. **¿En Between el bloque de texto va centrado?** Hoy no se activó: `bloque_centrado`
   es la regla de Paulina para Revex y su propio docstring avisa de no generalizarla.
   En el repo consta «en Between va centrado», pero se dijo del LOGOTIPO y dentro de
   una advertencia sobre haber dado por global una regla ajena.
2. **Las dos reglas de títulos de DT** —sin punto, y sin mezclar cajas— **¿valen
   también para Between y Piso 18, o son sólo de DT?** Además, para automatizarlas
   falta que el JSON de textos diga cuál línea es el TÍTULO; hoy ni `texto_prohibido`
   ni `grafia_fijada` lo saben y aplicarlas a todos marcaría cada párrafo legítimo.

**Abierto — corpus.** DT tiene sólo **3 aprobadas** en disco contra 12 de Between, y
**ninguna rechazada**: los topes están dominados por Between. Falta que Eli diga
dónde están las piezas de DT aprobadas de meses anteriores.

## 2026-09-22 · Eli (Windows) — DT: el carrusel S5, ronda 6 (sólo la portada)

**Qué pidió Eli**, sobre el render de la ronda 5 del mismo día: (1) «te faltó
borrar el texto chico de abajo de DoubleTree by Hilton… ese último de la
portada»; (2) «quiero que el título se lea como En Doubletree (espacio abajo) by
Hilton (abajo) Santiago - Vitacura en la portada, los demás okey».

**1 · El carrusel se queda sin firma en las SEIS.** La ronda 5 había sacado la
versalita de las cinco interiores y la dejó en la portada porque Constanza acotó
su pedido a «el resto de las slides». Eli la sacó también de ahí, así que
`Firma` se **borró del código** en vez de dejarlo apagado. La marca no queda
huérfana: el nombre completo lo dicen los tres renglones del titular y el
logotipo está grabado en el cristal del propio clip.

⛔ Se dejó escrita en su lugar la trampa que enseñó ese componente, porque vale
para cualquier texto con tracking alineado a la derecha: **CSS agrega el espacio
de tracking también después de la última letra**, así que la tinta no llega al
margen (la firma moría en x=984 con el margen en 992). Ficha:
`tracking-no-llega-a-inline-block`.

**2 · El titular en tres renglones, y de vuelta a cuerpo 108.** La ronda 5 había
metido «en DoubleTree by Hilton» en UN renglón y para que cupiera el cuerpo tuvo
que bajar de 108 a 80,6 — que además dejaba muy poca diferencia de tamaño contra
«Tu día» (72). Partirlo arregla las dos cosas: **«en DoubleTree» Medium /
«by Hilton» Light / «Santiago–Vitacura» Light, los tres a 108**, que es la receta
escrita de DT («titular a dos pesos y un mismo cuerpo»). Medido, los tres entran:
731,5 · 445,9 · **879,4** px de tinta, y el más largo muere en **967,4** contra
un margen de 992.

⛔⛔ **Y otra vez NO se justificaron a una medida común**, aunque con tres
renglones parecía el caso de libro del criterio de Honors. Lo revienta el largo:
a la medida del titular aprobado (731,5) los cuerpos saldrían **108 / 177,2 /
89,8** — «by Hilton», nueve caracteres, quedaría un 64 % más grande que el nombre
del hotel y sería lo más grande de la lámina. En Honors el rango entre cuerpos
fue del 25 %; acá sería del **97 %**. **El criterio de justificar a una medida
sólo funciona con líneas de largo parecido.**

⚠️ **Cada renglón lleva su propia sangría**, porque el hueco del primer glifo es
distinto: +1,404 la «e», **−1,404** la «b» (vuela hacia afuera: hay que empujarla
a la DERECHA) y +3,348 la «S». Los tres nacen en x=88.

⚠️ Medido sobre el render: el aire contra el canto del trazo vuelve a los **28
px** de la ronda 3 (el `marginBottom` del círculo vuelve de 15 a 8). Entre
renglones la separación de líneas base es pareja (110,2 px) aunque la tinta dé
huecos de 35 y 18 px, porque «by» baja la «y» y «Santiago–Vitacura» sube la «S»
y la «t». Sin colisión.

**Entregado.** **Sólo la portada viajó.** Las cinco interiores se verificaron
byte a byte contra la ronda 5 —el render da el mismo md5— y el script de subida
las saltó solo. En Drive se reemplazaron en sitio `C1 S5 DT n°1.mp4` y
`C1 S5 DT n°1.gif`; los 12 archivos quedaron verificados por md5 contra el local.

**Dónde quedó:**
- Página de revisión: `out/hilton/dt/c1-s5/revision-r6.html` —
  `scripts/dt-c1-s5-revision-r6.py`.
- QA **en verde** · el peor sigue siendo «Tu día» con 3,35:1 sobre vara 3,0; los
  tres renglones del titular dan 6,12 · 11,17 · 11,06 · typecheck limpio.
- `dt-c1-s5-gif.py` estrenó `--solo`, para no regenerar seis GIF cuando cambia una.

**Qué sigue:** nada abierto en este carrusel. Si Eli quiere ver la versión
justificada a una medida —la del «by Hilton» gigante— está calculada y se rinde.

---

## 2026-09-22 · Eli (Windows) — BETWEEN: la portada To Go, ahora con la dirección al pie

**Lo que pidió Scarlette** (Slack, sobre la portada que Eli le había pasado):
«te pido un favor, le puedes sumar la dirección a esta portada porfiss ❤️ Con eso
mandamos a VB @Nicolás Ávila y se subee».

**⚠️ La portada del pedido NO es la que está publicada.** La lámina del hilo —y la
que Eli me pasó para hacer el ajuste— es la del **16-09, el vaso sobre la mesa de
listones**; verificado píxel a píxel contra `out/hilton/between/entrega-togo-r25/`
(diferencia media 0,00). La que quedó en Drive esta mañana es la de la **entrada**
(IMG_4170), por la reversión de la r29. Se preguntó antes de tocar nada y la
indicación de Eli fue clara: **«debes subirla como independiente, no borrar nada ni
quitarlo»**. Así que la de la entrada **sigue publicada y sin tocar**, y la nueva se
suma al lado.

**Entregado** — `C1 S4` (`1vZZGvxfiGOIrf73znO39V4aASreumkfZ`), archivo **nuevo**:

| | |
|---|---|
| Archivo | `BW FEED 22-09 Promos To Go 1 portada con direccion.png` |
| id | `1jin31p-Be4bW5SDQoHgjEBYl-lr5HWrI` |
| md5 | `716289b7…` — el mismo del local |
| La que ya estaba | `17xDK7PM…`, md5 `8bb07f15…`, `modifiedTime` **12:48 sin cambios** |

⭐ **La dirección se CALCÓ, no se diseñó.** El único antecedente de dirección sobre
una pieza de feed es la lámina `C1 S2 CUMPLE N1.png` que hizo Eli el 07-09, nacida
del mismo pedido del cliente («aprovechemos de poner la dirección en G1 abajo»). Se
midió sobre ese archivo y se reprodujo:

| | Lámina de Eli | La portada nueva |
|---|---|---|
| altura de versal | 43 px | **43 px** |
| ancho de la línea | 879 px | **877 px** |
| línea de base | a 79 px del canto | **a 78 px** |
| centro de la tinta | 1123 (el lienzo en 1125) | **1123** |
| ancho de asta | 5 / 5,4 | **6 / 5,9** |

⭐⭐ **Y ahí está la lección: el peso salió del TRAZO, no del ojo.** Con el cuerpo ya
calzado (versal de 43 px = 29 px en la mesa), el semibold que usa todo el resto del
sistema daba **7 px de asta y un 35 % más de tinta** que la línea de ella. El
regular se quedaba corto (4 px, 14 % menos). Queda **Medium (500)**, y el tracking
salió de la misma medición: 0,024 em deja la línea en 877 contra 879. Una línea de
pie «parecida» se nota al lado de la de la diseñadora; medirla cuesta dos renders.

**Lo medido antes de entregar:**

- contraste de la línea sobre su fondo, **por el peor tramo de 60 px: 5,03:1**
  (la vara del texto chico son 4,5:1); ni el píxel más claro baja de 4,57:1;
- márgenes 685 px por lado, contra los 175 de mínimo;
- **la pieza sólo cambia en la línea del pie**: contra la entregada del 16-09 no hay
  un solo píxel distinto fuera de `y 2691–2743`;
- `between-qa.py` limpia · typecheck limpio.

⚠️ **El aviso de carrusel sigue, y es de la foto:** contra sus tres hermanas la
portada queda 20 puntos más oscura de mediana y 16 más cálida. Ya estaba anotado el
16-09; la dirección no lo mueve.

**Cómo quedó el código.** `ToGo1` pasó a ser una base con props (`ToGo1Base`) y dos
exportaciones, porque **hay dos portadas vivas en Drive**:

- `BW-F-ToGo-1` → la de la entrada, sin dirección — reproduce el archivo publicado;
- `BW-F-ToGo-1-Direccion` → la del vaso sobre la mesa, con la dirección.

La línea es `DireccionAlPie` en `BetweenSistema.tsx`, con las medidas escritas
encima, y la cadena vive en el kit como `BETWEEN.datos.direccionPieza` («AV.» en
versales, que es como la escribió Eli; la otra forma es la del copy del posteo).

**Dónde quedó:**
- Entregado: `out/hilton-between-togo-r30/` (1 pieza + manifiesto con el id de Drive).
- Página de revisión: `out/hilton/between/revision-direccion-22-09.html` —
  `scripts/between-revision-direccion-22-09.py`.

**Qué sigue:** que Scarlette mande a VB. Y las slides 2, 3 y 4 no se tocaron —
siguen esperando el visto del cliente por los precios y el rollo de canela.

---

## 2026-09-22 · Eli (Windows) — DT: el carrusel S5, ronda 5 (Constanza + Eli)

**Qué pidieron.** Comentario de **Constanza Lizana** en la grilla (22-09, 11:49),
dos cosas: (1) «en la slide 1 (portada) el texto no me gusta animado, el video
detrás al tener movimiento hace que el texto con más movimiento maree. Me
gustaría el texto estático pero el globo que encierra "tu día" sea animado»; y
(2) «en el resto de las slides […] en la parte inferior donde dice "DT by hilton
stgo - vitacura" me gustaría que se eliminara, para que no tenga tanto elemento
por slide». Encima, **Eli** el mismo día: «que en el texto de la portada diga
DoubleTree by Hilton en la misma tipografía del título […] la idea es que se vea
muy igual».

**1 · La portada se quedó quieta.** Se fueron las **cuatro** entradas —itálica,
titular, tercer renglón y también la píldora `DESLIZA`, que lleva texto y también
entraba con un fade—. Queda **un solo gesto**: el trazo del globo, que se dibuja
del f8 al f46. Las cinco interiores conservan sus entradas: Constanza dijo que
las ve bien.

**2 · La versalita al pie salió de las cinco interiores.** `<Firma>` quedó sólo
en la portada.

⚠️ **PENDIENTE DE ELI:** la portada es ahora la **única lámina donde el nombre
sale dos veces** —el bloque dice «en DoubleTree by Hilton / Santiago–Vitacura» y
el pie repite lo mismo en versalitas—. Constanza acotó su pedido a «el resto de
las slides», así que **se dejó** y va como opción A. La opción B (sin firma) está
rendida en la página de revisión. **Lo que subió al Drive es la A.**

⚠️ **Lo que NO se tocó, a propósito:** el degradado azul del pie de las
interiores existía para sostener esa versalita y ahora no sostiene nada. Se dejó
porque ella dijo que el resto de las slides las ve bien; está ofrecido en la
página.

**3 · La jerarquía de la portada, en tres niveles.** El nombre venía partido
entre dos voces —«DoubleTree» en el titular a 108 y «by Hilton» en el renglón
Light de 42—, que es exactamente lo que Eli lee como «se ve diferente». Ahora:
«Tu día» (intacta) · **«en DoubleTree by Hilton»** en Stag Medium · **«Santiago–
Vitacura»** en el tercer nivel, con la misma tipografía que tenía la bajada.

⭐⭐ **El cuerpo es la consecuencia de la medida.** «en DoubleTree by Hilton» a
cuerpo 108 mide **1211,2 px** de tinta y la columna son **904**: no cabe.
**80,606** es el cuerpo exacto al que la tinta mide 904,00 y el renglón nace en
88 y muere en 992 — flush contra los dos márgenes, medido glifo a glifo sobre
`Stag-Medium.ttf`.

⛔ **Y NO se justificaron los tres renglones a una medida común**, que es lo que
pide ese criterio: acá la línea larga es la que tiene que pesar. A una medida de
904, «Santiago–Vitacura» saldría a cuerpo **109,3** contra 80,6 del nombre del
hotel — la ciudad más grande que la marca. La propia memoria del criterio deja
escrita la excepción («si la línea larga es la que tiene que pesar, se parte en
dos ANTES de justificar») y acá se aplicó.

⚠️ El costo, y va dicho en la página: el titular baja de 108 a 80,6, así que
contra «Tu día» (72) la diferencia de **tamaño** es chica. Lo que sostiene la
jerarquía es el **peso**. Si Eli lo ve flojo, la salida es partir el nivel 2 en
dos renglones y devolverle el 108.

⭐ El ritmo vertical se devolvió a lo aprobado midiendo sobre el render: el hueco
trazo→titular vuelve a los **28 px** de la ronda 3 (se había cerrado solo a 21 al
bajar el cuerpo) y el hueco contra el tercer nivel queda en **42 px**, 1,5× el de
arriba.

⭐⭐⭐ **Y EL QA CAMBIÓ DE MÉTODO — el fondo ya no se estima, se MIDE.** Al dejar
la portada quieta, la tinta pasó a estar en pantalla desde el f0, y `peor_tercio`
sacaba «el fondo» promediando la banda **con la tinta adentro**: cantó **2,69:1**
sobre un fondo que da **3,52:1**. No se arregló enmascarando por color —en estas
láminas el fondo TIENE blancos legítimos (el cielo entre las vigas, el cielo raso
del salón) y un umbral «>200 es tinta» borra justo el fondo más claro, que es el
que puede hundir el contraste—. Se arregló rindiendo un **fotograma de control
sin ninguna tinta** (`--props='{"soloFondo":true}'`) y midiendo ÉSE. Excepción:
una banda cuyo fondo es PIEZA y no foto —«DESLIZA», que va sobre la píldora— se
mide sobre la lámina, y se marca con `"pieza"`.

⭐ De paso se cerró el pendiente que el propio QA tenía anotado desde la ronda 4:
**tres bandas de las interiores no cubrían su propia tinta por la derecha** (el
desayuno se quedaba 44 px corto en el titular; el lobby, 58; la habitación, 24) y
el salón sobraba 54. Las diez se re-midieron sobre el render.

**Entregado.** Las 6 MP4 (2160×2700, 5,06 s) y las 6 GIF (720 px, 12 fps)
**reemplazadas en sitio** en `S5 HILTON SEP 2026 › DT`
(`1qqPFM2EDVvAzgZLLQIJpxYr6gkFmKNHk`) y su subcarpeta `C1 S5 DT - GIF`
(`13RPiyOpfNxgRJ_EJ1nndqTxgRk5dNnme`): mismo `fileId`, así que **los enlaces que
circulan siguen sirviendo**.

**Dónde quedó:**
- Piezas: `out/hilton/dt/c1-s5/entrega/` y `entrega-gif/`.
- Página de revisión: `out/hilton/dt/c1-s5/revision-r5.html` —
  `scripts/dt-c1-s5-revision-r5.py`.
- QA **31/31 en verde** · el peor del carrusel es «Tu día» con 3,35:1 sobre vara
  3,0 · typecheck limpio.

**Qué sigue:** que Eli diga **A o B** en la firma de la portada, y si quiere que
el degradado del pie de las interiores se vaya con la versalita.

---

## 2026-09-22 · Eli (Windows) — BETWEEN: la portada del To Go vuelve a la foto de la entrada

**Lo que pidió Eli:** «vuelve a la imagen en la portada que yo había puesto
primero […] el cliente quiere volver a esa», con el pantallazo de
`IMG_4170.HEIC`. O sea que se deshace el cambio de foto del 16-09 —que a su vez
vino de que el cliente corrigió el enlace de la grilla— y la portada del carrusel
**PROMOS TO GO** (FEED 22-09) vuelve a la toma de la persona saliendo del local
con el vaso en la mano.

**Ya estaba rendida y ella lo dijo a tiempo:** «para ya lo tenemos», señalando
`out/hilton-between-togo-r25/`. En efecto, `BW-F-ToGo-1.png` de esa carpeta es
byte a byte la portada del 14-09 con esa foto (md5 `8bb07f15…`), así que **la
entrega es ese archivo**, no un render nuevo. Se había rendido uno para verificar
y sólo se diferenciaba en el antialias de los glifos; se botó.

**Entregado:** archivo `17xDK7PMvJyvvXMF3diTm-zswq--XUDpn` de **C1 S4**
(`1vZZGvxfiGOIrf73znO39V4aASreumkfZ`) **reemplazado en su contenido**, así que el
enlace que circula en la grilla sigue sirviendo. Verificado con el conector:
`modifiedTime` 22-09 y `fileSize` 8.175.071, que es el del local.

**El código quedó apuntando a esa foto**, que es la regla del estudio: si la
pieza se re-rinde, sale la que está en Drive. Dos líneas en `ToGo1` —
`togo-portada-r23.jpg` y `degradadoPie` de vuelta a **0,72**.

⭐ **Y ahí está la lección del día, ya en el manual:** el 0,60 se había calibrado
contra la foto del vaso sobre la mesa, que abajo es clara y pareja. Sobre los
pantalones crema de esta otra deja el script en **3,59:1** —pasa, pero al filo— y
con 0,72 sube a **4,49:1**. **Un velo calibrado contra una placa de fondo no
sobrevive al cambio de placa.**

⚠️ **Lo que NO se hizo, a propósito:** volver a la ronda 23 entera. Aquella
llevaba todo el bloque en caja taupe y Eli la sacó en la r24. Retrocede la placa
de fondo y el parámetro que depende de ella, nada más.

⚠️ **La portada se sale del tono del carrusel y no tiene arreglo:** mediana 73 ·
saturación 23 contra 102–104 · 37–47 de sus tres hermanas (el tope del QA son 14).
Es una toma de calle, cromáticamente pobre, y emparejarla obliga a devolver el
«filtro cálido» que el cliente mandó eliminar el 31-08. La portada anterior
tampoco pasaba (mediana 84, calidez 37). Se entrega igual porque la foto la
eligió el cliente.

**Dónde quedó:**
- Entregado: `out/hilton-between-togo-r29/` (1 pieza + manifiesto con el id de Drive).
- Página de revisión: `out/hilton/between/revision-22-09.html` —
  `scripts/between-revision-22-09.py`.
- QA 1/1 limpia · `--carrusel` con las dos advertencias de arriba · typecheck limpio.

**Qué sigue:** las slides 2, 3 y 4 no se tocaron y siguen esperando el visto del
cliente sobre los precios nuevos y el rollo de canela (columna K, `EN CAMBIOS`).

---

## 2026-09-22 — Elisabet Soto «Eli» · BETWEEN, LOS VASOS TO GO SE REHICIERON

**Qué se hizo:** los vasos To Go del 21-09 quedaron **reemplazados**. Eli los
rehizo ella misma en Magnific desde claude.ai y el resultado está mejor logrado
que el recorte fotográfico. Space **«BETWEEN_VASOS TOGO»**
(https://www.magnific.com/app/spaces/a2ce7bd4-9df0-47db-b7b2-d96f5c81079c).

**⚠️ Lo que hay que saber antes de tocar estos archivos:** no son la foto del vaso
recortada — son **generados** con Google Nano Banana 2, y **el logotipo lo redibujó
el modelo**. Contradice la regla dura del estudio («la IA hace ambiente y fondo,
nunca el producto ni el logotipo») y entra porque lo decidió la diseñadora de la
cuenta. No es permiso general: está escrito en el manual como excepción declarada.

**Por qué es mejor, medido:** el logotipo se lee **entero en los tres** —el grande
real salía «ƎTWEEN» en las nueve tomas de las dos sesiones, que era el problema
abierto de ayer—, el canto de la tapa no tiene muescas, los tres vienen a plomo, el
mediano no trae el pliegue del cartón, y el recorte no dejó orla (el canto está a
166–184 del beige del fondo). Lo único que se pierde es resolución: 1221 px de
silueta contra 1947 de ayer.

**Dos cosas había que arreglarles, y se arreglaron:**
1. **No venían a escala común.** Cada vaso se generó en su propio encuadre — en la
   v1 el MEDIANO salía más alto que el GRANDE. Se reescalaron a la proporción real
   del envase (0,712 / 0,861 / 1,000, la medida ayer con dos reglas independientes),
   atando el factor al EXTRA para que todo baje y nada se interpole hacia arriba.
   El trío del Space, generado de una sola vez, la confirma: 0,705 / 0,832 / 1,000.
2. **El kraft no era el mismo** entre los tres (11/255). Una ganancia multiplicativa
   por canal, medida en el cuerpo limpio. Queda en 0,0/255.

**Se eligió la v2 del Space, por medida y no a ojo:** el molde de la tapa entre los
tres dispersa 0,014 en v2 contra 0,077 en v1 (en v1 el del medio trae una tapa
notoriamente más alta, y eso es justo lo que rompe la lectura de familia).

**⭐ Y se cerró el pendiente de las onzas.** El Space los rotula, así que los nombres
cambiaron: ayer «chico / mediano / grande» → hoy **MEDIANO 8 oz / GRANDE 12 oz /
EXTRA 16 oz**. Los archivos se renombraron en consecuencia. Nada de código los
referenciaba todavía, así que no se rompió nada.

**Dónde quedó:** `out/hilton/between/vasos-togo/` (6 PNG + `revision.html` con el
antes, el después y la foto real), banco de marca en
`public/assets/hilton/between/togo-sep2026/togo-vaso-*-nobg.png`, originales del
Space en `raw/hilton/between/vasos-togo-v2/`, y dos scripts nuevos
`between-vasos-togo-v2*.py`. **La entrega de ayer no se borró:** está en
`out/hilton/between/vasos-togo/_reemplazado-21-09/` y en el commit `cc0f0a2`.

**El `/al-dia` de la misma jornada confirmó el renombre y trajo tres cosas más:**
- ⭐ **La grilla de OCTUBRE le da la razón al Space.** El FEED del 5-oct (carrusel
  Café To Go, slide 3 «TAMAÑOS Y PRECIOS») pide «que se entienda la diferencia entre
  **mediano, grande y Extra**». ⚠️ Pero en la línea de precios el mayor es **«Café
  XL»**: `Mediano $1.990 · Grande $2.790 · XL $2.990`. El rótulo en pantalla sale
  literal del brief; el nombre del archivo es cosa nuestra. Y la ST animada del
  25-oct los repite en combo — **al mediano le falta el precio**, dice «CAFÉ
  MEDIANO $» y nada más: preguntar antes de armar.
- ⛔ **Eli ya había subido 5 piezas de la promo To Go el 21-09 a las 20:00**
  (`PROMOS C1 S4 TOGO N°_1..5.png`, carpeta «C1 PROMOS ACTUALIZADAS 2026 TOGO»).
  **Son anteriores a los vasos** —los recortes se cerraron a las 21:28 y los
  generados hoy—, o sea **ninguna de las cinco usa los vasos nuevos**. Si hay que
  actualizarlas es trabajo aparte, y primero hay que mirar si existe un editable
  más nuevo que el render.
- **Octubre no es producible:** las 21 piezas en EN REVISIÓN y cero comentarios de
  cliente. Instantánea nueva en `clients/hilton/grillas/between-octubre-2026.md`.
  Septiembre dio **diff cero**: el movimiento de hoy en Drive es ruido.

**Qué sigue / abierto:**
1. ~~Que Eli confirme los nombres~~ — **confirmado por la grilla de octubre.**
2. **El 8 oz generado no muestra la faja de kraft** del real (el kraft le llega hasta
   la tapa). Se pidió así en el prompt — es decisión, no error. Si hay que mostrarla,
   se regenera cambiando esa línea.
3. **Resolución**, sólo si hace falta: si un vaso tiene que ocupar una pieza entera,
   pasarlo por el escalador de **precisión** (⛔ el creativo redibuja el logotipo).
   Ayer costó 630 créditos por tres.
4. **Subirlos al Drive de Between** si el CM los va a usar este mes — hoy están en el
   repo y en el Space.

---

## 2026-09-21 — Elisabet Soto «Eli» · CIERRE DEL DÍA (BETWEEN)

**Qué se hizo:** los tres vasos To Go recortados sin fondo, a escala común, para
actualizar la promo — cinco PNG con transparencia real (los tres sueltos + el
trío en los dos órdenes). Seis rondas con Eli: se enderezaron (venían inclinados
+4,5° / +3,9° / +3,0°, cada uno distinto), se rehizo el canto de la tapa por tono
porque el modelo de recorte lo dejaba dentado contra el follaje, se reconstruyó
el aro blanco del chico (contra el mármol el modelo no lo ve), se midió la
proporción real con dos reglas independientes y **se terminó sacándole proceso,
no poniéndole**: el veredicto fue «está sobreprocesado».

**Dónde quedó:** `out/hilton/between/vasos-togo/` (5 PNG + `revision.html`),
copia en el banco de marca `public/assets/hilton/between/togo-sep2026/`, y cuatro
scripts `between-vasos-togo-*.py`. Space de Magnific **«BETWEEN · vasos To Go
(producto)»** con los vasos y el prompt de referencia del envase. Todo rendido y
entregado; nada a medias.

**Qué sigue:** subir los cinco PNG al Drive de Between si el CM los va a usar
este mes — hoy sólo están en el repo y en el Space.

**Abierto — dos cosas, y las dos necesitan foto nueva, no retoque:**
1. **El logotipo del vaso GRANDE se lee «ƎTWEEN».** Ese vaso quedó girado así en
   las nueve tomas de las dos sesiones, incluida la que el manual daba como
   «logotipo entero y legible». Pedir una foto del grande con el logotipo al
   frente.
2. **Al MEDIANO le queda una traza del canto de su sombra.** Ese vaso no tiene
   toma buena: en IMG_5715 el cartón está **doblado** (relieve, no sale con
   ningún filtro) y en 5716–5719 tiene sombra dura de la tapa sobre el cuerpo.
   Pedir el mediano solo, con el lado sin dobleces al frente y sin la tapa
   proyectando sombra.

También pendiente de Eli: **de cuántas onzas son los tres vasos**. Con ese dato la
proporción queda clavada sin estimar (hoy la tapa del chico se toma como 80 mm
contra 90 mm, la familia estándar 8/12/16 oz).

---

## 2026-09-21 (cierre 13f) · Eli (Windows) — BETWEEN, VASOS TO GO: EL LOGOTIPO

**Lo que devolvió Eli:** «los logos se ven mal y borrosos». Correcto, y era mío.

Comparando contra la foto cruda a la misma escala se veía claro: el trazo salía
lavado, hueco y con orla clara. Tres causas, todas sobre el mismo punto:

1. La ventana de la mediana que **detecta** el logotipo era del 2 % del ancho —
   comparable al grosor de la letra—, así que se hundía dentro del propio trazo y
   la máscara salía mordida. Ahora va al 5,5 %.
2. La máscara que lo **protege** no estaba dilatada: cubría el centro del trazo
   pero no su canto, y el canto se quedaba con la versión filtrada.
3. El **suavizado del grano** (bilateral) pasaba por encima del logotipo.

Corregido: todo filtro que toque el cuerpo se pondera ahora por una máscara del
logotipo **más ancha que el trazo**.

**Se rehízo el paso de Magnific** sobre la versión corregida (sharpness 10,
ultraDetail 12), otros **630 créditos**. Entrega al mismo tamaño: chico 2399×3162
· mediano 2643×3742 · grande 2712×4285 · trío 7940×4285. Los nuevos quedaron
también en el Space «BETWEEN · vasos To Go (producto)».

---

## 2026-09-21 (cierre 13e) · Eli (Windows) — BETWEEN, VASOS TO GO POR MAGNIFIC

**Lo que pidió Eli:** «utiliza esas referencias pero hazlo en Magnific para que
guardes los vasos como prompt en un space. La idea es mejorarlos, que se vean
producto profesional y usarlos en distintas aplicaciones».

**Space creado: «BETWEEN · vasos To Go (producto)»** —
https://www.magnific.com/app/spaces/a2cd75a6-1446-45e6-9481-3bc94391494a
Tiene los tres recortes, los tres mejorados, y en la descripción el **prompt de
referencia** con las reglas duras del envase (kraft mate, tapa negra mate,
logotipo serigrafiado y no etiqueta, aro blanco sólo en el chico, mediano y
grande comparten tapa, nada de relight sobre el producto).

**Modelo: `ultra-photo` (Precision photo) a 2x**, sharpness 8 · grain 5 ·
ultraDetail 10. ⛔ El creativo no se usó: alucina detalle y sobre el logotipo
cambia el dibujo. Verificado que no redibujó nada — la diferencia media en la
zona del logotipo contra un 2x por Lanczos es **2,87 de 255**. **630 créditos**
los tres (el ilimitado no aplicaba en esta sesión).

**Los dos cuidados del método**, ya en el manual: el entorno se deja plano antes
de subir (si no, el upscaler dibuja un halo en el canto) y el alfa se **rasteriza
de nuevo desde el polígono**, no se escala.

⛔ **Un error propio que el QA cazó:** el polígono se guardaba en coordenadas del
lienzo sin recortar, así que al rearmar cayó corrido. Lo delató el control de la
tapa compartida, que saltó de 0,971 a 1,047. Corregido: vuelve a 0,971.

**Entrega, ahora al doble de resolución:** chico 2399×3162 · mediano 2643×3742 ·
grande 2712×4285 · trío 7940×4285. Mismos nombres, misma carpeta, más la copia
en el banco de marca.

---

## 2026-09-21 (cierre 13d) · Eli (Windows) — BETWEEN, VASOS TO GO · RONDA 4

**Lo que devolvió Eli:** «la del centro se ve una raya extraña, debe verse como
los vasos de al lado pero en su tamaño».

**Era un defecto del envase, no del revelado.** El vaso mediano de `IMG_5715`
tiene un **pliegue en el cartón** y quedó girado hacia la cámara. Probé cuatro
caminos —aplanar la baja frecuencia, separar la banda fina con mediana en vez de
gaussiano, igualar el contraste local del grano, y clonar superficie limpia— y el
último estampó un fantasma del logotipo. Ninguno lo saca, porque no es luz: es
relieve.

⭐ **Se resolvió mirando la sesión entera:** en `IMG_5719` el MISMO vaso está
solo, de frente, con el logotipo completo y el lado bueno hacia la cámara. El
mediano ahora se entrega desde ahí. Mezclar tomas no rompe el set porque el
revelado reemplaza la baja frecuencia por el perfil del cilindro y la iluminación
del origen no sobrevive.

**De paso quedó una mejora que sí vale para los tres:** la banda fina se separa
con mediana, no con gaussiano. Un pasaaltos gaussiano **repica en un escalón** y
dibuja justo la línea que se quería borrar — parte de lo que se veía era
artefacto mío.

**Dos umbrales pasaron a ser adaptativos:** el croma que separa tapa de kraft
(sale de una semilla en el 12 % de arriba del propio vaso) y el balance de
blancos (el 2 % más claro y neutro de cada foto, porque el parche fijo de mármol
cayó en sombra en 5719 y corrió el color).

**Proporción, remedida con la tapa sobre 5715 para los tres:** chico 0,712 ·
mediano 0,861 · grande 1,000, con las dos reglas a ±0,9 % y ±2,1 %. Control de
tapa compartida en la entrega: 0,970.

**Entrega:** los mismos cinco PNG. Revisión en `revision.html`.

---

## 2026-09-21 (cierre 13c) · Eli (Windows) — BETWEEN, VASOS TO GO · RONDA 3

**Lo que devolvió Eli:** «necesito principalmente que mejores el recorte, hay
bordes que parecen mal recortados… sobre todo en las tapas. Y hay unas partes que
se ven unas líneas extrañas: que se vea muy o bastante liso con un poco de
textura de lo que es el kraft. Lo demás perfecto, la perspectiva está súper bien».

**1 · El canto.** La tapa es plástico negro contra follaje oscuro: ahí el modelo
de recorte inventa muescas de ±15 px y a ratos se trae una franja del fondo.
Probé suavizar el contorno, abrir morfológicamente y ajustarle una elipse al
borde medido — los tres fallan, y la elipse se fue 270 px de más. Lo resolvió el
**tono**: núcleo neutro → casco convexo → dilatación condicionada al tono. Y el
alfa ahora se **rasteriza a 4×** desde el polígono suavizado, con el remate de
3 px por la normal.

**2 · Las líneas extrañas.** Eran una sombra proyectada y, en el mediano, un
**pliegue del papel**. Se arregló partiendo el canal en tres bandas: la baja se
reemplaza por el perfil del cilindro, la media se bota y la fina —el grano del
cartón— se conserva. El logotipo va protegido con máscara blanda y el clarity
apagado, porque su radio volvía a dibujar el resto de la sombra.

**3 · Tres errores propios que costaron la ronda**, los tres en el manual: la
tapa no se elige por el componente que empieza más arriba; el casco convexo queda
por dentro del canto real; y la baja frecuencia no se estima con gaussiano porque
la sombra tiene borde.

**Control:** la tapa del mediano contra la del grande —la misma tapa— queda en
0,974 (ideal 1,000) y la del chico en 0,873 (ideal 0,889).

**Entrega:** los mismos cinco PNG en `out/hilton/between/vasos-togo/` + copia en
el banco de marca. Revisión en `revision.html`.

---

## 2026-09-21 (cierre 13b) · Eli (Windows) — BETWEEN, VASOS TO GO · RONDA 2

**Lo que devolvió Eli sobre la ronda 1:** «necesito que se vean más derechos y
sin flash de cámaras o rayas de luz, deben verse mejor proporcionados y mejor
imagen. Está bien que sea sin fondo».

**1 · A plomo.** Venían inclinados +4,49° el grande, +3,86° el mediano y +3,00°
el chico —cada uno distinto, que es lo que hacía que no se leyeran como familia—.
Ahora quedan en ±0,11°. El eje se mide por la bisectriz de los dos flancos y el
mate se vuelve a sacar sobre el vaso ya derecho.

**2 · Sin flashes ni rayas de luz.** Brillos comprimidos con tanh contra una base
desenfocada, en la tapa completo y en el papel sólo los excesos (si no, se aclara
el logotipo). Fuera también la raya blanca de la junta tapa/vaso.

**3 · La proporción estaba mal de verdad, no era percepción.** El mediano y el
grande **comparten tapa** y en la entrega sus tapas medían **4,8 % distinto**.
Ahora se mide con dos reglas —el horizonte sobre IMG_4153 y la tapa compartida
sobre IMG_5715— y se entrega la media geométrica: **chico 0,719 · mediano 0,864 ·
grande 1,000**, con el desacuerdo repartido en ±2,4 % en vez de cargado a una.

⛔ **Dos errores propios que costaron esta ronda, y quedaron en el manual:** las
cajas de medición de IMG_4153 **cortaban** el vaso (el mate tocaba el borde), y
como los tres se **tocan en la silueta** el mate los une, así que los anchos
medidos ahí no servían — el control de «tapa compartida» de la ronda 1 dio un
falso 0,36 % sobre una medición contaminada.

⛔ **Y tres trampas de máscara**, todas en el manual: la tapa no se elige por el
componente que empieza más arriba (una mota de 690 px se la robó al chico y el
vaso salió con **la tapa café**); el casco convexo queda por dentro del canto real
y hay que dilatarlo o deja orla; y el umbral de croma para separar plástico de
papel se pasa con el balance de blancos aplicado.

📏 **Pendiente con el cliente:** de cuántas onzas son los tres vasos. Con ese dato
la proporción queda clavada sin estimar (hoy la tapa del chico se toma como 80 mm
contra 90 mm, la familia estándar 8/12/16 oz).

**Entrega:** los mismos cinco PNG en `out/hilton/between/vasos-togo/`, revisión en
`revision.html`. Scripts: los cuatro `between-vasos-togo-*.py`.

---

## 2026-09-21 (cierre 13) · Eli (Windows) — BETWEEN, LOS TRES VASOS TO GO SIN FONDO

**Qué pidió Eli.** Los tres tamaños de vaso To Go en tres fotos independientes,
cada uno solo, más una imagen con los tres pero **«no tan apegados»**, todo **sin
fondo** («se utilizará sólo el vaso de to go»), para actualizar la promo. Mandó
dos carpetas de Drive como referentes: `1Jx4Z6hvIic0qyypIq6Ob2l3vZm4QiMBA`
(= la sesión `cafes-sep2026`, IMG_5714–5729) y
`1hHcwg-Z-h9OuOhM0rkc-eotuzSMpUuq9` (= `vasos-togo-sep2026`, IMG_4137–4175).
Las dos ya estaban bajadas en el repo. Encargo extra: **«mejora un poco, que se
vea profesional de fotógrafo pro»**.

**La toma elegida: `IMG_5715`.** Es la única con los tres vasos **completos,
separados y con los tres logotipos de frente**, y además en sombra abierta — luz
suave, sin el sol duro de la mesa de listones. Descartadas: `5716`/`5717` (se
tapan entre sí), `5718`–`5720` (falta el grande y hay medio vaso en sombra dura),
`4151`–`4157` (sol duro y se solapan).

**Lo que se entrega** — `out/hilton/between/vasos-togo/`, PNG con transparencia
real y sin sombra:

| Archivo | |
|---|---|
| `BW-ToGo-vaso-chico.png` | 1211 × 1592 |
| `BW-ToGo-vaso-mediano.png` | 1303 × 1830 |
| `BW-ToGo-vaso-grande.png` | 1355 × 2146 |
| `BW-ToGo-tres-tamanos.png` | 3959 × 2146, de chico a grande |
| `BW-ToGo-tres-tamanos-invertido.png` | el mismo, de grande a chico |

Los tres sueltos van **a escala común**: puestos al 100 % quedan proporcionados
entre sí. Copia en el banco de marca,
`public/assets/hilton/between/togo-sep2026/togo-vaso-*-nobg.png`.
Página de revisión: `out/hilton/between/vasos-togo/revision.html`.

⭐⭐⭐ **La proporción se midió, no se estimó: chico 0,716 · mediano 0,838 ·
grande 1,000 (±2 %).** En la foto los tres están a distinta distancia, así que
los altos en píxeles mienten. Sale del horizonte, y el horizonte sale de que los
listones de la mesa están **igualmente espaciados**. El control que la valida:
mediano y grande **comparten tapa** y sus bocas corregidas dan el mismo diámetro
con **0,36 %** de diferencia. Todo el detalle quedó en el manual.

⛔ **Lo que hay que mirar, y no tiene arreglo por acá: el logotipo del vaso
grande se lee «ƎTWEEN».** El vaso quedó girado así en las dos sesiones — se
revisaron las nueve tomas donde aparece, incluida `togo-grande-frontal-b.jpg`,
que el manual daba como «logotipo entero y legible» y tampoco lo tiene. **Pide
una foto nueva del grande con el logotipo al frente.**

⛔ **El aro blanco del chico no se recorta: se mide.** Contra el mármol blanco el
modelo de recorte lo pierde en las tres tomas y con contraste local también. Se
reconstruyó con recta en cada flanco + elipse al fondo, verificado contra el
perfil de saturación de la foto (el aro termina en y=5100, la elipse cayó en 5103).

**El revelado.** Balance de blancos medido sobre el mármol; sombra proyectada
aplanada en luz **y en croma** dejando vivo el degradé del cilindro (ahí se fue
la mancha verde que la muralla de plantas dejaba en el mediano); tapa al 16 % de
croma; los tres igualados al mismo kraft; canto rematado 3 px hacia adentro y
descontaminado; ruido suavizado antes de enfocar.

**Scripts:** `between-vasos-togo-proporcion.py` (la medición),
`between-vasos-togo-recorte.py` (mate, base reparada y revelado),
`between-vasos-togo-entrega.py` (escala común y montaje),
`between-vasos-togo-revision.py` (la página).

⚠️ **QA:** `qa/motor.py --marca hilton` no corre — Hilton todavía no tiene
`clients/hilton/reglas.yaml`. Son recursos sin texto ni zonas seguras, así que
no aplica; la revisión fue a la vista, sobre fondo claro y oscuro.

---

## 2026-09-21 (cierre 12) · Eli (Windows) — BETWEEN, CONCURSO RONDA 13: **el legal completo, y en 3 líneas** ✅ APROBADA

> ✅ **Eli aprobó la ronda 13 el 21-09-2026, mirando la página de antes/después.**
> El carrusel del concurso queda **CERRADO**: las dos láminas están en el Drive
> en su versión final y el enlace no cambió.

**Qué pidió Nicolás** (Slack, con pantallazo de la slide 2). Dos cambios de
texto, los dos en la lámina 2:

1. **El legal completo del concurso**, escrito palabra por palabra:
   «*Concurso válido del 21 al 30 de septiembre. El ganador será anunciado el 1
   de octubre. Premio: un café diario, para disfrutar en local o en formato To
   Go durante todo el mes de octubre de 2026. Premio personal e
   intransferible.» Entra el **premio** y la **intransferibilidad**, que no
   estaban en ninguna de las dos láminas.
2. **La frase de los comentarios, por tercera vez**: «Si yo fuera CEO del café
   **en Between**, mi primera acción sería…». Va de «CEO de Between» (r5) →
   «CEO del café» (r6) → ésta.

⭐⭐ **LA REGLA QUE DEJA LA RONDA: primero se mide cuánto texto cabe, después se
mueve la lámina.** A cuerpo 21 el legal nuevo son **4 líneas, +56,3 px**, en la
lámina que menos sitio tiene: abajo están la polaroid y el vaso con el logotipo
impreso y el manual prohíbe taparlos. El primer intento pagó esas cuatro líneas
**moviendo la pieza** —titular y tarjeta 28 px arriba, los cuatro separadores de
18 a 15, medido y encajado al píxel—. Funcionaba, pero tocaba una lámina cerrada
para acomodar un párrafo.

Eli lo cortó de raíz: **«achica un poco más el texto del legal… al menos en 3
líneas que quede, sin quitar texto»**. Y ahí el problema desaparece:

    legal, 21 → 17 px · de 2 a 3 líneas      +12,1
    la cita, 36 → 34 (obligada, ver abajo)    −5,0
    ───────────────────────────────────────  +7,1

**17 no es un número al azar: es el TECHO.** Es el cuerpo más grande al que el
párrafo entero entra en tres líneas, medido con la propia `.ttf` sobre los 630
px de ancho útil de la tarjeta — a 18 la primera línea mide 626,0 y se pasa por
4 px, así que salta a cuatro; a 16 pierdes tamaño sin ganar ninguna línea.

⭐ **Y porque cabe en tres, la lámina VUELVE a su geometría aprobada**: titular
en `top: 150`, tarjeta en `top: 320`, separadores en 18/14. Lo único distinto de
la pieza publicada son los dos textos. La tarjeta cerraba en **y=975,0** y
cierra en **978,2** —3,2 px— con **25,8 px** de aire hasta el marco blanco del
recorte.

> Lo que no hace falta se devuelve. Mover una lámina cerrada para que quepa un
> párrafo es la solución cara; medir a qué cuerpo el párrafo cabe es la barata.

⚠️ **La cita baja de 36 a 34, y ésa sí es obligada, no estética.** Con «en Between»
adentro la primera línea mide **645,1 px** a cuerpo 36 y el ancho útil de la
tarjeta es **630**: Chrome la parte y la cita se va a TRES líneas, o sea sube de
nivel por encima del titular de la lámina. El otro corte —«…del café / en
Between, mi primera…»— deja la línea larga en 654,1, tampoco entra y encima
separa la marca de su preposición. A 34 mide 608,5 y sigue en las dos líneas
aprobadas.

⛔⛔ **EL HALLAZGO DE LA RONDA, y vale para toda la cuenta: la ITÁLICA de
Raleway no trae `lnum`.** El legal muestra las cifras bajando de la línea base
—el «3» de «30», los «2» de «2026»—, que es exactamente lo que Eli nombró en el
carrusel To Go («los números se ven desordenados… no se ven uno más arriba y
abajo que los otros»). Se le aplicó `CIFRAS_ALTAS` y **el render salió idéntico
píxel a píxel**. Leyendo la GSUB de los .ttf del repo: `Raleway-SemiBoldItalic`
tiene `ccmp dnom frac liga locl numr` y **no** `lnum`; la redonda y la bold sí.

> **La regla: en Between, un texto en itálica con cifras las va a mostrar de
> estilo antiguo y no hay CSS que lo arregle.** Si tienen que ir a caja alta, el
> texto va en redonda. Escrita en `clients/hilton/CLAUDE.md § 9`.

Acá **se dejó la itálica**: es el tratamiento que Eli aprobó, el defecto ya
venía en la lámina publicada y cambiarlo mueve una pieza cerrada. Informado en
la página de revisión; la decisión es de ella.

**✅ ENTREGADO.** Sólo cambió la N2, así que sólo se subió la N2, **reemplazando
el mismo archivo** — el enlace no cambió.

- `C1 S3 CONCURSO N2.png` → <https://drive.google.com/file/d/1l3KDqsLhRFxSx9AJzNVJhHuiFyIOtzTb/view>
  (md5 `288f146c…`, 3 823 576 B, verificado contra el local y con el `parents`
  consultado: sigue dentro de `1HEga0sjGH766I4EnpHKP2ED31prslo0L`).
- `C1 S3 CONCURSO N1.png` **no se tocó**: su md5 sigue siendo `385d6162…`, el
  mismo que subió la ronda 12. La portada no tiene ninguno de los dos cambios.
- La página de antes/después también quedó en esa carpeta como
  `C1 S3 CONCURSO - antes y despues r13.html`
  (<https://drive.google.com/file/d/1kP4tcGOhjlmgeT_ulcjdUkrOkerZghoz/view>).
  ⚠️ **Drive no renderiza `.html`, lo ofrece para descargar**, así que la que se
  abre de una es la publicada: <https://claude.ai/artifact/AZ4JqRYMVY1AwjripK1idc>

**QA.** `between-qa.py` da la slide 2 **limpia**, carrusel en el mismo tono
(197 / 201), `npm run typecheck` limpio.

⚠️ **La slide 1 arrastra un aviso del QA que NO se tocó**: «texto a 74 px del
borde derecho (mínimo 84)». Ya estaba en la versión entregada y aprobada en la
ronda 12; corregirlo mueve una lámina cerrada y no es lo que pidió el cliente.
Se informó en la página de revisión y **Eli aprobó igual**, así que la pieza
queda con ese aviso. Si alguna vez se reabre la portada, ése es el primer sitio
donde mirar.

**Abierto.**
1. ✅ **El asterisco del legal: resuelto, se queda como está.** Se le preguntó a
   Eli —el asterisco abre el legal y no tiene a quién referirse, porque no hay
   otro en el carrusel— y aprobó la lámina con él puesto. **No se le agrega uno
   a «1 MES DE CAFÉ GRATIS» en la portada ni se saca.**
2. Sigue sin resolverse si hay que reemplazar también en `C1 S3 CONCURSO`
   (`1eXZnhj5-2j7o4AuwClf5dngcn6k9oQzC`, dentro de `S3 HILTON SEP 2026 / BW`),
   donde todavía están las láminas de la **ronda 5**. Viene abierto de la r12.

**Dónde está todo.**
- Composición: `src/compositions/hilton/BetweenC1S3Concurso.tsx` (`C1S3Concurso2`).
- Mediciones corribles: `scripts/between-concurso-s3-r13-medir.py`
  (`frase` · `legal` · `encaje`).
- Página de revisión: `scripts/between-concurso-s3-r13-revision.py` →
  `out/hilton/between/concurso-s3-r13/revision-r13.html`.
- Entrega empaquetada a 150 ppp: `scripts/between-concurso-s3-entrega.py`.

---

## 2026-09-21 (cierre 11) · Eli (Windows) — DT, CARRUSEL S5: **ENTRÓ EL GYM**, el carrusel pasa a SEIS

**Qué pidió Eli.** «Toma el diseño del gym que nos faltaba, ahora ya está para
que podamos diseñar esa slide, y sólo cambia el nombre a la otra. Verifica si
cambió algo más.»

**Qué cambió en la grilla, verificado por diff.** Se bajó la instantánea del día
(`clients/hilton/grillas/api/dt-sept-20260921.json`) y se comparó por conjunto de
cadenas contra la del 15-09, hoja por hoja:

| Dónde | Qué cambió |
|---|---|
| **FEED 28-09 · el carrusel** | ⭐ El brief pasa de 4 a **5 slides**: entra `SLIDE 4 - SIGUE CON TU RUTINA DIARIA (GYM)`, visual «mostrar espacio disponible del GYM (Sin personas)», texto «Un espacio para mantenerte en movimiento.» El cierre pasa a ser el slide 5. **Es el único cambio del brief**, lo demás está palabra por palabra idéntico. Estado `REVISAR CONTENIDO` → **`CORREGIDA`** |
| FEED 23-09 · estático Honors | Comentario nuevo: **«Cambiemos foto por habitación de categoría superior y ok!»** · estado `OK PARA DISEÑO` → **`APROBADO`** |
| FEED · columna nueva 27-09 10:00 | **`CARRUSEL EFEMERIDE - DÍA DEL TURISMO`** — sólo el título, **el brief viene vacío** |
| FEED 14-09 → 16-09 | La opinión de Booking se corrió de fecha; estado `YA POSTEADO` |
| STORIES 18-09 | estado → `APROBADO` |
| STORIES 21-09 animada | horario **11:00 → 16:00** · estado → `APROBADO` |
| REELS 10-09 | comentario nuevo: «No tiene el ajuste el video editado verdad?» · estado → `CORREGIDA` |

**Qué se hizo.** La lámina del gym, con su renumeración. El carrusel queda en
**seis** láminas de 2160×2700 y 5,06 s, todas video.

⭐⭐ **Y el hallazgo de la sesión: el gimnasio SÍ estaba filmado.** Este repo
llevaba cuatro días diciendo que no había video del gym en ninguna carpeta y que
la lámina tendría que salir de la foto `HDT_82` —o sea ser la única sin
movimiento real, con la decisión escalada a Eli—. Era falso: `CONTENIDO HOTEL
2026 › GYM` (`1Xl8ECYMSqtfJNlseP9zddRi9gI43Kz6i`) tiene **7 clips**, descartados
en su momento por ser «sólo `.MOV` de iPhone» **cuando los otros cinco clips de
este mismo carrusel son exactamente eso**. Medidos, traen la misma ficha técnica
que la sesión del 16-09 (HEVC Main 10, HLG, 3840×2160 rotado −90, 59,9 fps) y
entran por `dt-c1-s5-clips.py` sin tocar una línea. La regla quedó escrita:
**un material se descarta por lo que se ve en el fotograma, nunca por con qué se
grabó.**

**De los 7 se eligió `IMG_1700`**, y no por contraste —los siete pasan las varas
de sobra—: lo que decide es qué queda detrás del bloque de texto durante los 5 s
y que el brief pide «el espacio». `1699` mete la torre de poleas en el titular,
`1698` es detalle de mancuernas, `1697` abre sobre una pared vacía. `1700`
recorre la sala entera con el techo limpio arriba, y dura **4,99 s**: es el único
clip del carrusel que va a velocidad real, sin ralentizar. `fy=0.50` y no más
abajo — con 0,44 el marco del espejo se mete en la caja del texto.

**El titular va a cuerpo 68 y no 74.** Es la frase más larga del brief: a 74 el
gancho mide 963 px contra 904 de medida útil y Chrome lo parte, dejando el bloque
en TRES líneas cuando sus cinco hermanas son de dos. A 68 entra en una y el
bloque mide **885 px**, que es lo mismo que el del lobby (892) y el del cierre
(884). Es el criterio de DT del 15-09: la medida manda y el cuerpo es la
consecuencia.

**El rótulo va «SIGUE CON TU RUTINA DIARIA», sin el «(GYM)»** — misma regla que
la slide 3 (`TIEMPO PARA TI (COWORK / LOBBY)` → «TIEMPO PARA TI»): el paréntesis
del brief nombra el espacio, que es lo que muestra la imagen. Informado a Eli.

⛔⛔ **LA TRAMPA DE LA ENTREGA: insertar una lámina RENUMERA y el Drive reemplaza
por NOMBRE.** El gym entra en el lugar 4, así que **`C1 S5 DT n°5.mp4` ya no es
el cierre: es el gym**, y el cierre pasa a `n°6`. Subir «reemplazando por nombre»
sin mirar deja el cierre pisado. Orden correcto: **primero subir el `n°6` nuevo,
después reemplazar el `n°5`.** Las cuatro primeras no se tocan.

**Dónde quedó — ⭐ SUBIDO Y VERIFICADO.** Eli pidió subirlo y dejar además una
copia en GIF en carpeta aparte.

`S5 HILTON SEP 2026 › DT` — `1qqPFM2EDVvAzgZLLQIJpxYr6gkFmKNHk`

| | qué es | `fileId` | |
|---|---|---|---|
| `C1 S5 DT n°1.mp4` | portada | `1XOgP7k-vucZaNgBEEB6Ct-i-UpPnHZgx` | sin tocar |
| `C1 S5 DT n°2.mp4` | 8:30 desayuno | `16xH8LsdH_btwNDbaVswO_-1zPR6vN-On` | sin tocar |
| `C1 S5 DT n°3.mp4` | 9:30 salón | `1E3jDFfn_ZN1GuWy-L3y2jXJaSHatLy6x` | sin tocar |
| `C1 S5 DT n°4.mp4` | 12:00 cowork | `10Dn_CbKfyjuyNksckTjH-SdM_Kr2-4rF` | sin tocar |
| `C1 S5 DT n°5.mp4` | **16:00 GYM** | `1rysBShpjQZrsNrxLaDFJoLuAdC9OqUE-` | **archivo NUEVO** |
| `C1 S5 DT n°6.mp4` | cierre | `1KmdGW1R0Nx-23tkd07tNlPPV79xPZyK4` | **renombrado**, mismo id |

⭐⭐ **LA RENUMERACIÓN SE RESOLVIÓ RENOMBRANDO, NO RE-SUBIENDO.** El cierre ya
estaba arriba como `n°5`; se le cambió **sólo el nombre** a `n°6`, así que
conserva su `fileId`, su enlace y su historial, y no volvieron a viajar 22 MB.
El gym entró como archivo nuevo en el `n°5` que quedó libre. Quien tenga el
enlace viejo del `n°5` **sigue viendo el cierre**, que es lo que ese enlace
siempre mostró — lo que cambió es su número, no su contenido.

⚠️ Antes de renombrar, el script **verifica por md5** que el `n°5` de Drive sea
de verdad el cierre, y se planta si no lo es. Está en
`scripts/dt-c1-s5-subir.py`, con `--ensayo` para ver qué haría sin tocar nada.

**Los GIF** — `… › C1 S5 DT - GIF` (`13RPiyOpfNxgRJ_EJ1nndqTxgRk5dNnme`), las
seis láminas a **720×900, 12 fps**, 15-24 MB cada una y 118 MB en total.
`scripts/dt-c1-s5-gif.py`, con la tabla de por qué esos dos números: a 1080 px
pesan el doble y no se ven más nítidas, y a 540 la versalita de la firma empieza
a empastarse. ⚠️ **No entran por WhatsApp** (tope ~16 MB): para chat hay que
correrlo con `--ancho 540`.

✅ **Los 12 archivos verificados por md5 contra el local y con el `parents`
consultado**: todos dentro de su carpeta, ninguno en «Mi unidad».

⭐ **Y la carpeta nueva NO dio el problema de permisos que se temía.** El cierre
del 17-09 dejó escrito que no se creaba subcarpeta porque «la crearía el token
del estudio y no Eli, y en esta cuenta eso ya dio problemas». Medido ahora: la
carpeta y el archivo nuevo heredan **exactamente** los mismos permisos que el
`n°1` del 17-09 —dueña `valeria@copywriters.cl` y compartido con el equipo
completo, incluido el cliente (`doubletreesantiagovitacura@gmail.com` y
`magdalena.cordero@hilton.com`)—. En esta carpeta se pueden crear subcarpetas.

- Entrega local: `out/hilton/dt/c1-s5/entrega/` y `entrega-gif/`.
- Composición: `src/compositions/hilton/DtC1S5Dia.tsx`, lámina `gym`.
- Clip: `scripts/dt-c1-s5-clips.py`, entrada `"gym"`. El `.MOV` no viaja en git
  (34 MB) pero el script documenta id, tramo, recorte y gradación.
- Página de revisión: `out/hilton/dt/c1-s5/revision-r4.html`.
- QA: **pasa entero**. Typecheck limpio.

⚠️ **El gimnasio se gradó un punto más abajo** (brillo −0,04, gamma 0,95) porque
tiene el piso más claro del carrusel y la versalita de la firma caía a 4,35:1,
bajo la vara de 4,5. Sube a **4,54:1** — pasa, pero por poco. Midiendo el fondo
real, enmascarando la tinta, da 5,5:1, así que el margen de verdad es mayor. No
se tocó el velo: esa rampa vale para las seis.

⚠️⚠️ **Y apareció algo del QA que NO se arregló acá, a propósito.**
`peor_tercio` promedia la banda **con la tinta blanca adentro**, así que el
número que canta depende de lo apretada que esté la caja y no sólo del fondo. El
sesgo es conservador —da falsas alarmas, no tapa fallos—, pero significa que hoy
conviven dos varas de medir en el mismo archivo (las bandas de la portada son el
contorno del glifo, las de las interiores llevan 10 px de holgura) y que **tres
bandas de láminas ya entregadas no cubren su tinta por la derecha**: `desayuno`
se queda 35 px corto en el sello y 44 en el titular, `lobby` 58 en el titular,
`habitación` 24. Es el mismo modo de falla que la ronda 3 encontró en la portada.
Arreglarlo re-mide una pieza ya aprobada y puede destapar algo de lo que está en
el Drive: **merece una pasada propia**. Está informado en la página de revisión y
la nota completa está al pie de `scripts/dt-c1-s5-qa.py`.

**Qué sigue.**
1. ✅ Subido y verificado — ver arriba.
2. La **hora del cierre** sigue sin entregarla contenido: la lámina n°6 va sin
   sello de hora. Es lo único que queda abierto de esta pieza.
3. ⭐ **El FEED del 27-09 es una pieza nueva sin brief**: la celda dice
   `CARRUSEL EFEMERIDE - DÍA DEL TURISMO` y el resto está vacío. Hay que pedirlo.
4. El estático de Honors del 23-09 quedó **APROBADO**, pero con un comentario
   nuevo encima: «Cambiemos foto por habitación de categoría superior y ok!».
   Esa pieza se entrega desde el editable `.ai`, no desde Remotion.

**Abierto** (de la ronda 2, sin cambios): portada sin lockup a confirmar por
escrito · los textos con punto final · el `12:00` · la gente al fondo de los
clips del salón y la portada.

---

## 2026-09-21 (cierre 10) · Eli (Windows) — BETWEEN, CONCURSO: **SUBIDO AL DRIVE**

**Qué se hizo.** Eli mandó la carpeta de destino y se subieron las dos láminas
del carrusel del concurso, ya con todos los cambios de las rondas 6 a 12.

**Dónde quedó.**
- Carpeta: `1HEga0sjGH766I4EnpHKP2ED31prslo0L`
  (<https://drive.google.com/drive/folders/1HEga0sjGH766I4EnpHKP2ED31prslo0L>)
- `C1 S3 CONCURSO N1.png` → <https://drive.google.com/file/d/1Jq74oFUQsChTrYkpLiIanG3gKTKAKZ4g/view>
- `C1 S3 CONCURSO N2.png` → <https://drive.google.com/file/d/1l3KDqsLhRFxSx9AJzNVJhHuiFyIOtzTb/view>
- **Verificadas por md5 contra el local** (`385d6162…` y `b005c2f4…`) y con el
  `parents` consultado: las dos están DENTRO de la carpeta pedida, no en «Mi
  unidad» — que es el modo en que falla el token de scope `drive.file`.

⚠️ **Son archivos NUEVOS en una carpeta nueva.** En `C1 S3 CONCURSO`
(`1eXZnhj5-2j7o4AuwClf5dngcn6k9oQzC`, dentro de `S3 HILTON SEP 2026 / BW`)
siguen las láminas de la **ronda 5**, que es lo que ve quien entre por el enlace
viejo de la grilla. Si esa carpeta es la que mira el portal, hay que reemplazar
ahí también — está preguntado.

⭐ **El aparato de medición volvió al repo**: `scripts/between-concurso-s3-medir.py`
junta las cinco mediciones que citan la pieza y el manual (hueco limpio, holgura
contra el recorte, contrastes por tercios, ángulo de la caja de la REF 1 y
ángulo de los garabatos rojos). Las citas de los comentarios ahora apuntan ahí.

⛔ **Y una trampa del propio aparato, anotada donde corresponde:** el contraste
se mide sobre la FOTO, nunca sobre la pieza rendida. En el render la franja ya
contiene la tinta y el «fondo» sale contaminado — el rótulo daba 4,15:1 contra
el papel y 2,26:1 medido sobre sí mismo.

**Qué sigue.** El visto de Scarlette sobre el texto, y decidir si se reemplaza
también en `C1 S3 CONCURSO`.

## 2026-09-21 (cierre 9) · Eli (Windows) — BETWEEN, CONCURSO RONDA 12: la jerarquía de la cabecera

**Qué pidió** (esta vez con el pantallazo rayado): bajar TODO el bloque porque
«se está viendo muy muy junto el concurso al logo», **juntar «SE BUSCA:» con la
cajita** —«así como está en la referencia, para que se entienda que es un texto
junto»— y las cuñas «con esa curvatura, en ese ángulo».

⭐⭐ **El segundo pedido pagó el primero, y eso es lo que hay que recordar.** No
había de dónde sacar aire para despegar el rótulo del logo: la lámina está llena
y todo lo demás ya estaba en su mínimo. Juntar las dos líneas lo resolvió, porque
en la `REF 1` **la caja monta sobre el texto**: un solape de 8 px devuelve 12 px
de alto al bloque, que son exactamente los que faltaban. **El aire lockup→rótulo
pasó de 31 a 46 px sin mover la pila ni achicar ningún cuerpo.** Los cuatro aires
quedaron 46 · 30 · 20 · 18.

⭐⭐ **Y el giro de las cuñas se MIDIÓ sobre el garabato rojo.** En la ronda 11 se
dedujo de la `REF 2` y salió **al revés**. Acá se aisló el rojo del pantallazo y
se le sacó el eje principal a cada marca por PCA (`between-concurso-s3-medir.py rojo`): las tres dan
**22°, 40° y 87°** contra los 67°, 88° y 120° del dibujo sin girar, o sea
**−42°**. El abanico se abre hacia arriba-izquierda, como un destello que sale de
la palabra — no hacia ella.

> **La regla que deja:** cuando la diseñadora DIBUJA la corrección, el ángulo se
> mide en su dibujo. Deducirlo de la referencia original es una segunda fuente y
> puede dar el signo cambiado.

⚠️ **Queda una duda anotada:** marcó con rojo una **estrella sobre la chispa** de
la esquina derecha, pero no la mencionó al hablar. No se tocó, y quedó preguntado
en la página de la ronda.

**Dónde quedó.** `out/hilton/between/concurso-s3-r12/` · entrega reempaquetada ·
página: <https://claude.ai/artifact/4yaocFvnH4kzMNKWgkw9mc> · QA y typecheck
limpios · la CTA sigue cerrando en 827 con 20 px de holgura.

**Qué sigue.** **Nada subido al Drive**; con el OK,
`python scripts/between-concurso-s3-entrega.py --subir`.

## 2026-09-21 (cierre 8) · Eli (Windows) — BETWEEN, CONCURSO RONDA 11: aire bajo el logo y las cuñas

**Qué pidió.** «Baja los textos que dejo encerrado sólo un poco, sin solapar
imágenes, ya que están muy cerca del logo. Y ajusta las 3 líneas de ilustración,
gíralas como te dejo la ref.»

⚠️ **El pantallazo NO llegó** —el mensaje entró sin imagen— y quedó avisado en la
página de la ronda. Los dos cambios se hicieron con lo deducible.

- **Aire lockup→CONCURSO: 21 → 31 px.** El rótulo baja 10 y la bajada 6. Nada se
  solapa: la tinta más alta queda en y=210 y el lockup cierra en 179.
- Los 16 px salieron de donde no cuestan jerarquía: **interlineado de la bajada
  1,30 → 1,25** y 4 px del bloque del titular. El aire cajita→«¿El sueldo?»
  queda en 17, el mismo que tiene la pila entre su primera línea y su caja.
- **Las cuñas giran de −12° a +40°.** No es a ojo: en la `REF 2` las tres
  **convergen abajo a la izquierda y se abren hacia arriba-derecha**, apuntando
  al texto; el dibujo propio irradia hacia arriba, y la diferencia entre las dos
  orientaciones es de 40°. Rotadas ocupan x 103–222: no cruzan el margen de 84
  ni tocan la «C» de CONCURSO, que abre en x≈235.

**Dónde quedó.** `out/hilton/between/concurso-s3-r11/` · entrega reempaquetada en
`out/hilton/between/entrega-c1-s3-concurso/` · página:
<https://claude.ai/artifact/SucVjGKadyzbxTFsfgFhWQ>

**Qué sigue.** Que Eli mande el pantallazo si el giro o la bajada no son los que
marcó. **Nada subido al Drive**; con el OK,
`python scripts/between-concurso-s3-entrega.py --subir`.

## 2026-09-21 (cierre 7) · Eli (Windows) — BETWEEN, CONCURSO RONDA 10: **portada terminada**

**Qué pidió Eli.** «Este invierte el color, el texto café y el fondo beige.
Agranda un poco el texto y caja del CEO. Más deja **puntas rectas** al de caja
del CEO. Y listo.»

| Qué | Antes | Ahora |
|---|---|---|
| Caja «1 MES DE CAFÉ GRATIS» | taupe con tinta beige | **beige con tinta café** |
| Cuerpo del CEO | 54 | **60** |
| Caja del CEO | 78 × 385 | **88 × 456**, y **sin radio** |

⭐ **La inversión ordena la jerarquía, no sólo el color.** Con las dos cajas del
mismo taupe ninguna mandaba sobre la otra —el defecto que la ronda 5 ya había
diagnosticado en el sello— y ahora el bloque macizo es el del titular, que es el
nivel de arriba. La del premio se lee por su tinta (6,31:1 por dentro) y no por
su canto (1,50:1 contra el papel).

⭐ **Y las puntas rectas salen de la REF 1:** su bloque de color no tiene radio.
El radio de la marca (16) se queda en las cajas de dato, que sí lo llevan.
`TitularEnCaja` tiene ahora prop `radio`.

⚠️ **De dónde salieron los 16 px que necesitaba la caja para crecer:** se
apretaron los aires que NO están atados a una proporción —el de arriba del
rótulo (25→21), el de la bajada al bloque (25→20) y el interno del bloque
(30→10, que además es lo que hace la referencia, donde la caja monta sobre el
texto)—. **El aire rótulo→bajada se mantuvo en 32**, que es el único con una
proporción medida detrás (1,5× el aire entre las líneas de la bajada).

⚠️ La inversión de la caja del premio va por `style` sobre `CajaDato` y **no
tocando el componente**: su caja es taupe y la usan piezas ya aprobadas.

**Lo medido.** Caja del CEO 4,19:1 contra el papel · caja del premio 1,50:1 con
6,31:1 por dentro · CONCURSO 4,14:1 · bajada 4,16:1 · CTA cierra en 827 contra
un halo que entra en 847 · 23 px entre la caja del CEO y «¿El sueldo?» con la
rotación descontada · carrusel en el mismo tono (197/201) · typecheck limpio.

**Dónde quedó.**
- **Entrega empaquetada y al día**: `out/hilton/between/entrega-c1-s3-concurso/`
  — `C1 S3 CONCURSO N1.png` y `N2.png`, 2250×2812 a 150 ppp.
- Renders: `out/hilton/between/concurso-s3-r10/`. Props: `jerarquia: 'A'` +
  `titularEstilo: 'cajaSans'`.
- Página: <https://claude.ai/artifact/6CKXTycEkp9i84K8qgoaym>

**Qué sigue.** ⚠️ **NADA SUBIDO AL DRIVE.** Con el OK:
`python scripts/between-concurso-s3-entrega.py --subir` reemplaza el contenido
de los archivos de `C1 S3 CONCURSO` (`1eXZnhj5-2j7o4AuwClf5dngcn6k9oQzC`) y los
enlaces de la grilla no cambian. Siguen abiertos el visto de Scarlette sobre el
texto y el copy de la grilla («Si yo fuera CEO de Between»).

## 2026-09-21 (cierre 6) · Eli (Windows) — BETWEEN, CONCURSO RONDA 9: **CERRADA la portada**

**Qué eligió Eli.** «Quiero la opción 3, pero con lo del CEO ese texto **en
cajita con un leve ángulo como la referencia**, y el se busca **aumenta un poco
el grosor del beige**.» O sea el híbrido de las dos opciones de la ronda 8: la
línea de arriba en Raleway con halo (una sola tipografía, como el referente) y
«CEO DEL CAFÉ» en el bloque de color inclinado, que es el otro recurso de la
`REF 1`.

⭐⭐ **El ángulo se MIDIÓ sobre la referencia.** Aislando el azul de la caja y
ajustando sus bordes por mínimos cuadrados (`between-concurso-s3-medir.py angulo-ref`): borde superior
**−2,20°**, inferior **−3,34°**. Se tomó **−3°**, dentro del rango medido y
coincidente con el registro que la marca ya usa (el sello de la ronda 4 gira −4°).

⛔ **Y una trampa de la rotación:** `transform` no cambia la caja del layout, así
que una caja rotada sobresale `ancho·sen(giro)/2` —10 px acá— por arriba y por
abajo. Sin descontarlo, la cajita quedaba a 10 px de «¿El sueldo?».

⛔ **Otra, del mismo tipo:** el primer cálculo de la caja usó la CAJA ALTA del
texto (43 px a cuerpo 60) y la caja medía 116, no 101 — **un `div` con
`lineHeight: 1` mide el CUERPO entero**. El cuerpo bajó a 54 y el relleno pasó a
0,23 del cuerpo, que es el de `CajaDato`.

⚠️ El halo de «SE BUSCA:» sube de 12 a **16 px**. Y el aire rótulo→bajada se
abrió de 22 a **32**: bajo una palabra de 104 px, 22 se leían pegados. 32 es
1,5× el aire entre las líneas de la propia bajada, que es la proporción del
manual.

**Lo medido.** CONCURSO 4,14:1 · cajita del titular 4,19:1 contra el papel y
6,31:1 por dentro · bajada 4,16:1 · aire cajita→«¿El sueldo?» 26 px con la
rotación descontada · CTA cierra en 827 contra un halo que entra en 847 ·
carrusel en el mismo tono (196/201) · typecheck limpio.

**Dónde quedó.**
- **Entrega empaquetada**: `out/hilton/between/entrega-c1-s3-concurso/` —
  `C1 S3 CONCURSO N1.png` y `N2.png`, 2250×2812 a 150 ppp.
- Renders de la ronda: `out/hilton/between/concurso-s3-r9/`.
- Props de la pieza: `jerarquia: 'A'` + `titularEstilo: 'cajaSans'`.
- Página: `scripts/between-concurso-s3-r9-revision.py` →
  <https://claude.ai/artifact/1gcHHtGYGKgujK75WctWBz>

**Qué sigue.** ⚠️ **NADA SUBIDO AL DRIVE.** Con el OK de Eli se sube con
`python scripts/between-concurso-s3-entrega.py --subir`, que reemplaza el
contenido de los archivos de la carpeta `C1 S3 CONCURSO`
(`1eXZnhj5-2j7o4AuwClf5dngcn6k9oQzC`) — los enlaces de la grilla no cambian.
Siguen abiertos el visto de Scarlette sobre el texto y el desfase del copy de la
grilla («Si yo fuera CEO de Between»).

## 2026-09-21 (cierre 5) · Eli (Windows) — BETWEEN, CONCURSO RONDA 8: el rótulo pierde la caja

**Qué pidió Eli.** «Borra el recuadro beige que tiene, para que destaque mucho
más […] más grueso, más grande, incluso como la referencia», y para el titular
**tres versiones**: como «menos organizar mis archivos» (caja plana rellena),
como «estoy haciendo de todo…» (sticker con contorno) y —en un segundo mensaje—
«otra donde el se busca no sea Brushwell».

**Qué se hizo.**
- **CONCURSO sin caja**: café suelto, **Raleway Black 900, cuerpo 104** (610 px
  de tinta). Contra el papel pasa de **1,50:1 a 4,17:1**.
- **Tres titulares**, los tres rendidos a 2250: `caja` (taupe con tinta beige,
  cuerpo 64), `sticker` (halo de 12 px con Brushwell) y `stickerSans` (el mismo
  halo con «SE BUSCA:» en Raleway ExtraBold, que es como resuelve la REF 1: una
  sola tipografía y sólo cambia el tamaño).
- Props: `titularEstilo: 'caja' | 'sticker' | 'stickerSans'`.

⛔⛔ **El contorno NO se puede hacer con `-webkit-text-stroke`.** Se pintó así en
la ronda 7 y el defecto apareció al ampliar el render: Chrome aplica
`paint-order` **glifo a glifo**, así que el contorno de cada letra cruza por
encima del relleno de la anterior. Ahora es un **halo de 24 copias con
`text-shadow`**, que se pinta entero detrás del texto y queda continuo. Está en
el manual (§ «en un marco» puede ser un contorno).

⛔ **Y el halo se descuenta del aire:** los 9 px de la marca menos 12 de halo
dejaban las dos líneas a −3 y los halos se tocaban. Se abrió a 27.

**Lo medido.** CTA cierra en 827 contra un halo que entra en 847 (20 px) ·
CONCURSO 4,17:1 · bajada 4,16:1 · gaps del titular a «¿El sueldo?» 19 · 24 · 38
según la opción · carrusel en el mismo tono (197/201) · typecheck limpio.

**Dónde quedó.** `out/hilton/between/concurso-s3-r8/` · página:
`scripts/between-concurso-s3-r8-revision.py` →
<https://claude.ai/artifact/74U2JsKP3kRwaisYbjt9o9>

**Qué sigue.** Elegir entre las tres y subir reemplazando los archivos del Drive.
Siguen abiertos el visto de Scarlette y el copy de la grilla («CEO de Between»).

## 2026-09-21 (cierre 4) · Eli (Windows) — BETWEEN, CONCURSO RONDA 7: el titular pasa a sticker

**Qué pasó.** Eli eligió la **opción A** («apilado todo, como centrado») y pidió
tres ajustes sobre ella: CONCURSO «un poco más destacado», la bajada «un
poquitito más grande, porque se lee muy poco», y **«que se busca CEO del café
esté en un marco beige […] que sea como el sticker, igual que la referencia. Así
se achica más»**. La slide 2, «quedó perfecta».

| Qué | Antes | Ahora |
|---|---|---|
| CONCURSO | 52 | **68** (+31 %) · la caja pasa a 515 px de ancho |
| Bajada | 30 | **36** (+20 %) · 654 y 625 px, dentro de la columna |
| Titular | 88 | **64** (−27 %) · 419 px, con contorno |
| Marco del titular | — | **contorno beige de 8 px** |

⭐⭐ **«Marco beige» NO era una caja, y eso se resolvió mirando la referencia.**
En la `REF 1` el titular no está dentro de un rectángulo: lleva un **contorno
claro pegado a las letras** —una calcomanía— y la caja plana rellena está
reservada para el rótulo. Traducido con el beige de la marca, el titular y el
recorte de la figura pasan a leerse como piezas del mismo collage. Si se hubiera
dibujado un rectángulo, la pieza habría tenido tres cajas apiladas.

⭐ **El recurso entró al sistema, no a la pieza:** `TitularBetween` tiene ahora
`contorno` y `contornoColor` (`src/compositions/hilton/BetweenSistema.tsx`),
opt-in como `cajaAlta` y `pesoCaps` para que ninguna pieza aprobada se mueva. Se
pinta con `-webkit-text-stroke` **más `paint-order: stroke fill`** — sin el
`paint-order` el trazo se centra en el canto del glifo y se come la mitad de la
tinta en vez de crecer hacia afuera. El grosor no es a ojo: 8 px a un cuerpo de
64 es la misma proporción que el contorno blanco del recorte de la foto.

⭐⭐ **Y la regla del carrusel no se aplicó a ciegas.** «Un carrusel, un cuerpo de
titular» había bajado la slide 2 a 88 en la ronda 6. Acá la portada baja a 64,
pero su titular dejó de ser *el titular suelto de la lámina* y pasó a ser un
**rótulo enmarcado**: otro objeto, así que la regla no compara. La slide 2 se
congeló en los 88 que Eli aprobó — verificado, **0 píxeles de diferencia** contra
el render que ella miró.

**Lo medido.** CTA cierra en y=827 contra un halo que entra en 847 → 20 px de
holgura · bajada 4,16:1 (el mismo contraste del titular aprobado) · caja beige
1,50:1 y caja taupe **4,15:1** contra el papel · tinta dentro de la caja 6,31:1 ·
aires de cabecera 30 · 20 · 20 · 29 (interno 20, salto al mensaje 29) · carrusel
en el mismo tono (mediana 198/201) · typecheck limpio.

**Dónde quedó.**
- `out/hilton/between/concurso-s3-r7/` — `beige-1.png`, `taupe-1.png`, `slide2.png`
  (2250×2812) y `antes-r6-1.png`.
- Página de la ronda: `scripts/between-concurso-s3-r7-revision.py` →
  <https://claude.ai/artifact/EiDzyJaktckoCqTzxtcUNK>
- Props: `jerarquia: 'A'` + `selloTono: 'beige' | 'taupe'`.

**Qué sigue.** **Elegir el color del sello** (beige o taupe) y recién ahí subir,
reemplazando el contenido de los archivos que ya están en Drive para que los
enlaces de la grilla no cambien. Siguen abiertos el visto de Scarlette sobre el
texto y el desfase del copy de la grilla («CEO de Between»).

## 2026-09-21 (cierre 3) · Eli (Windows) — BETWEEN, CARRUSEL CONCURSO: contenido reordenó la portada

**Qué llegó.** Nicolás Ávila, por Slack y a pedido del cliente, con Scarlette en
copia: cambios de texto en el carrusel del concurso (FEED del **24-09**, S4, hoy
`EN REVISIÓN`) «para darle mayor relevancia a la efeméride». Y en el segundo
mensaje, lo que de verdad manda: **«dejaría como principal CONCURSO […] después,
como segunda jerarquía, las bajadas […] y desde ahí seguiría con SE BUSCA: CEO
DEL CAFÉ»**.

O sea que no es un texto que se agrega: **es el orden de lectura de la portada el
que cambia**, y eso mueve la decisión que tomó Eli en la ronda 5 (la caja beige
grande encabezando la pila de la izquierda). El sello conserva su caja y su
cuerpo —52, el que ella eligió— pero sube a rótulo de la lámina.

| slide | qué cambia |
|---|---|
| 1 · portada | sube CONCURSO a rótulo · entra la bajada «Se acerca el Día Internacional del Café y se abrió la vacante más importante» · el titular pasa a tercer nivel |
| 2 · tarjeta | una línea: «Si yo fuera CEO de **Between**» → «Si yo fuera CEO **del café**» |

⭐ **La portada NO tenía sitio, y eso se midió antes de componer.** El lockup
cierra en y=180; el halo blanco del recorte entra en la columna de la CTA en
**y=847** (medido sobre la foto, x 492–495), así que la última línea no puede
pasar de y≈827. Entre medio hay **662 px** para sello 84 + bajada 78 + titular +
«¿El sueldo?» 44 + caja taupe 66 + CTA 78. Con el titular en los 103 de la ronda
5 quedan **80 px para cuatro aires** — una portada apretada. Por eso van **dos
salidas a revisión, y lo que discuten no es el texto sino qué cede**:

- **A · apilado** — todo en el eje: sello centrado, bajada centrada de dos líneas
  y el **titular baja de 103 a 88**. Obedece la jerarquía completa que pidió
  contenido. Holgura contra el recorte: 20 px.
- **B · banda** — el sello se queda a la izquierda y la bajada se le pone al
  lado, en tres líneas, sobre el papel limpio de la derecha que estaba vacío
  (x 507–996). Cuesta 117 px en vez de 188, y con eso **el titular se queda en
  103**. Lo que cede es el eje. Holgura: 30 px.

⛔ **La primera tirada de A estaba mala y la salvó la medición, no la vista.** Con
la cabecera en 218/324/424/614 la CTA cerraba en y=844 contra un halo que empieza
en 847: **tres píxeles**. Toda la cabecera subió 17 px.

**Dos cosas de criterio que quedan escritas:**
- La bajada va en **caja baja**, no en las versales en que llegó: en esta marca
  las versales son del titular y de la caja taupe. Misma traducción que
  «SE BUSCA:» → «Se busca:», y sin punto final.
- En B el corte de línea **se compone a mano** (424 · 264 · 382 px): corrido
  dejaba «importante» sola en la tercera línea.

**Dónde quedó.**
- Renders 2250×2812 de las dos salidas: `out/hilton/between/concurso-s3-r6/`
  (`A-1/A-2/B-1/B-2`, más `antes-1/antes-2` que son la copia de la ronda 5).
- Código: `src/compositions/hilton/BetweenC1S3Concurso.tsx` — prop `jerarquia`
  (`'A' | 'B' | 'ronda5'`), con el presupuesto vertical escrito en la cabecera.
  La lámina de la ronda 5 sigue viva y reproducible.
- Página de revisión: `scripts/between-concurso-s3-r6-revision.py` →
  `out/hilton/between/concurso-s3-r6/revision-r6.html` y
  <https://claude.ai/artifact/2S7FmiqfVo4BMuGwY6CYkV>
- QA: carrusel en el mismo tono (mediana 197/201) · contraste de la bajada
  **4,17:1**, el mismo del titular aprobado · typecheck limpio.
  ⚠️ `between-qa.py` marca «texto a 74 px del borde derecho» en la portada: es
  **falso positivo conocido** —lo detecta también en la lámina ya aprobada— y es
  el halo del recorte contra el pelo, no texto.

**Qué sigue.**
1. **Que Eli elija A o B.** Recién ahí se rinde la entrega y se reemplaza el
   contenido de los archivos que ya están en Drive, para que los enlaces de la
   grilla no cambien.
2. ⚠️ **El texto no está confirmado por Scarlette**: en el mismo mensaje Nicolás
   le pregunta «confírmame si te gusta ese texto o para ver otro».
3. ⚠️ **El copy de la grilla sigue diciendo «Si yo fuera CEO de Between»**
   (columna del 24-09). Es de contenido; si se publica así, la gráfica y el pie
   no dicen lo mismo.

**Abierto.** Nada subido al Drive todavía.

## 2026-09-21 (cierre 2) · Eli (Windows) — BETWEEN, CARRUSEL PROMOS TO GO: los cambios de contenido de la S4

**Qué se hizo.** Llegaron por Scarlette (21-09, 10:08) los comentarios de
contenido del cliente sobre el carrusel **Promos To Go** (FEED col K · 22-09):
los tres precios nuevos, cambiar la medialuna por **rollo de canela** y
«los productos no se ven proporcionales unos con otros, revisar los tamaños de
los cafés y sus agregados».

| slide | qué quedó |
|---|---|
| 1 · portada | sin cambios |
| 2 · Café + Sándwich | sólo el precio: **$3.490** |
| 3 · Café + Dulce | **rollo de canela**, fotografía real, y **$2.990** |
| 4 · Los tres | sólo el precio: **$4.490** |

⭐ **La slide 3 dejó de ser una generación.** El rollo con el vaso vigente ya
estaba fotografiado: sesión `25 jul 2025`, toma **`25-281`** (vertical, con muro
vegetal). Es la regla madre de la ronda 10 —«antes de generar un producto,
búscalo en la sesión»— y acá se cumplió entera: no hay montaje, ni logotipo
estampado, ni relight. Su vaso pasó de leer 782 px de logotipo a **480**, contra
los 554 de la slide 2.

⛔⛔ **Y la slide 4 costó cuatro intentos y terminó SIN TOCAR.** Está todo en
`clients/hilton/CLAUDE.md § UNA FOTOGRAFÍA APROBADA NO SE RETOCA`: escalar los
tres productos dejó 888.000 px tocados, el logotipo del vaso duplicado y un
trozo del pan borrado («se ve como si estuviera pegoteado»); regenerar la escena
entera salió limpia pero con un sándwich que no es el de la marca; y escalar
sólo el vaso, aun con compuerta, movía el pliegue de la bolsa. Eli: «vuelve a la
foto anterior a esta». **La regla que queda: si la proporción está mal, se pide
otra foto.**

**Dónde quedó.**
- Entrega con el nombre del portal: `out/hilton/between/entrega-togo-r26/` (4 piezas, 2250×2812).
- **Subidas a `C1 S4`** (`1vZZGvxfiGOIrf73znO39V4aASreumkfZ`) **reemplazando el
  contenido del mismo archivo**, así que los enlaces que ya circularon en la
  grilla siguen sirviendo. Verificadas por md5 contra el local.
- Composición: `src/compositions/hilton/BetweenSeptiembre.tsx` (`ToGo2/3/4`).
- Aparato de la slide 3: `scripts/between-togo3-r26.py` — lleva anotado el ID de
  Drive de la toma `25-281` por si hay que rebajarla.
- Los tres intentos de la slide 4 quedan versionados a propósito, porque son de
  donde sale la regla: `between-togo4-r26.py`, `-r27-generar.py` + `-r27-acabado.py`,
  `-r28.py`. La escena generada, en `raw/hilton/between/s4/gen-r27/`.
- Assets: `togo-s3-r26.jpg` y `togo-25jul2025-rol.jpg` entran a git con su
  **excepción documentada en `.gitignore`** (las otras tres del carrusel ya
  estaban versionadas).
- Página de revisión que vio Eli: <https://claude.ai/artifact/XiQzzYWXXhkggEJgDFxtn6>
- QA 3/3 limpias · typecheck limpio.

**Qué sigue.**
1. **Esperar el visto del cliente.** La columna K sigue en `EN CAMBIOS`; se lee
   con `export?format=csv&gid=1537718358`. ⚠️ El comentario de Scarlette es
   NATIVO: no aparece en el CSV, sólo la nota vieja del enlace de la G1.
2. Si el cliente insiste con la proporción de la slide 4, **no se retoca la
   foto**: se le pide al hotel una toma nueva del trío más cerca, o sin la bolsa
   en cuadro.
3. El brief de la grilla sigue con los precios viejos ($4.290 / $3.790 / $5.290).
   No se toca —es de contenido— pero conviene saberlo al releerlo.

**Abierto.**
- ⚠️ **El sándwich de la slide 2 no creció.** Eli lo pidió («lo que es sándwich
  es más grande solo un poco») y se hizo, pero el retoque le dejaba un filo doble
  en el papel: se deshizo y la slide volvió a la foto aprobada. Queda ofrecido
  regenerar esa escena con el método de ella si lo quiere.
- ⚠️ La sesión de vasos que mandó Eli (`raw/hilton/between/cafes-sep2026/`, 15
  fotos de los tres tamaños) quedó bajada y medida. **No está en ningún manual
  todavía como banco**; de ahí salió el patrón del logotipo.

## 2026-09-21 · Eli (Windows) — BETWEEN, ST 30-09 «Plateada al Carmenere»: **ENTREGADA**

**Qué se hizo.** Eli rechazó la pieza que estaba en el Drive: «no se parece a la
ref […] ese recuadro que parece transparente de vidrio». Tenía razón, y el
defecto era de método: **la referencia de la columna U compone todo el texto
dentro de una tarjeta de vidrio y la pieza lo dejaba suelto sobre la foto.** Dos
rondas en el día y quedó aprobada.

**Ronda 33 — el cuadro de vidrio.** Se midió la tarjeta sobre la referencia, no
se estimó: velo **blanco α 0,21** (los tres canales dieron 0,216 · 0,210 · 0,205,
que es lo que prueba que es blanco y no un color de marca), filete de 1,5 px,
radio y aire interior al **9,2 % del ancho**, **sin sombra** (el perfil hacia
afuera del borde es plano) y el fondo **difuminado** por dentro — la nitidez
interior cae al 0,7–38 % de la exterior, el mismo rango del pin de DT, así que se
adoptó su radio de 3,5 px.

**Ronda 34 — el titular sale de la fórmula.** Eli: «que este texto sea en solo la
primera mayúscula la demás no y en raleway pero no tan gruesa, **ya que hay
muchos similares en historias**. más similar el recuadro a la ref». Se le
ofrecieron tres versiones y eligió **«B · sin Brushwell, todo Raleway»**. La
pieza quedó en caja baja, Raleway **SemiBold 600**, tracking 0, una sola familia
y una sola oración en dos líneas.

⭐ **Lo que hay que recordar de esta ronda:** en la 33 el aire del cuadro tuvo que
bajar de 84 a 72 porque no cabía el sticker del enlace. Al sacar la Brushwell
—que sola medía 113 px de tinta— **el cuadro bajó de 640 a 605 de alto y el aire
de la referencia volvió a caber**. La desviación no era un problema de geometría:
era el peso del titular. *Cuando una medida de la referencia «no cabe», mirar
primero qué la está empujando.*

⛔ **Y dos números del archivo estaban mal anotados:** el borde del plato en el
último fotograma está en **y=1127** (no en 1140), y el obstáculo real **no es el
borde del plato sino la comida, que empieza en y=1230**. Entre medio hay 103 px
de ala de loza limpia. La zona del enlace quedó en **340 × 120 en y=1007**, que
termina justo en 1127 y no pisa el plato en ningún fotograma.

**Dónde quedó.**
- Entrega: `out/hilton-between-s5-r34-final/`, con el nombre del portal, más la
  guía del CM y la página de revisión (`revision-final.html`).
- **Subida al Drive el mismo día, reemplazando el archivo**
  (`1ismDXD-Nizxuy24g9YuwvgE8juhHKTea`): **el enlace de la grilla no cambió.**
  Carpeta `STS` de la S5 — `1r_spPoBx-vR63J8GTRVCUkbZGGyNLnJg`.
- Código: `src/compositions/hilton/BetweenStS5.tsx` (rondas 33 y 34, con todas
  las mediciones escritas) y el nuevo prop **`cajaAlta`** de `TitularBetween`
  en `BetweenSistema.tsx` — opt-in, así que ninguna pieza aprobada se movió.
- Manual: dos secciones nuevas en `clients/hilton/CLAUDE.md` — «EL CUADRO DE
  VIDRIO» y «HAY MUCHOS SIMILARES EN HISTORIAS».
- Contraste del beige con el velo puesto: **7,9 a 9,7 : 1**.

**Qué sigue.** Nada pendiente en esta pieza. La otra de la S5 —la del 28-09, el
vaso To Go gigante— sigue como estaba, sin cambios.

**Abierto.**
- ⚠️ **La pastilla taupe quedó siendo lo más pesado de la pieza.** Es ExtraBold
  en caja alta sobre fondo macizo y ahora el titular es más liviano que ella. Se
  le avisó a Eli y no la pidió cambiar; si alguna vez lo dice, baja a SemiBold o
  se le saca el fondo.
- El `cajaAlta={false}` sólo se usó acá. Si Eli lo pide en otra story, el
  registro alterno completo está en el manual.

## 2026-09-21 · Eli (Windows) — DT, CARRUSEL S5: ronda 3 de la portada, **APROBADA**

**Qué se hizo.** Un solo ajuste, pedido por Eli sobre un pantallazo: «ajusta la
línea del Tu día, porque se tapa la i; además baja un poco y junta con el título
ya que se ve extraño. Lo demás está bien.» Aprobado en la primera vuelta.

⛔ **El trazo no tapaba la tilde por estar mal dibujado: la palabra no cabía.**
La tinta de «Tu día» llegaba a x=327,6 y el canto derecho del círculo estaba en
x=319,1 — «día» se salía **8,5 px** por la derecha y la curva pasaba justo por
la tilde y por la «a». Medido glifo a glifo contra el trazo: la «í» en
**−1,9 px** y la «a» en **−2,0 px** (negativo = se tocan).

| | ronda 2 | ronda 3 |
|---|---|---|
| círculo | 258×130 | **306×154** (+19 %) |
| holgura de la «í» | −1,9 px | **+20,8 px** |
| holgura de la «a» | −2,0 px | **+16,3 px** |
| hueco contra «en DoubleTree» | 57,6 px | **24 px** |

Por eso **la palabra no se movió de lado** —sigue de x=140,5 a 327,6, que es lo
aprobado y lo que el QA mide contra el margen—: crece el trazo. Y el bloque baja
30 px **sin mover el titular**: `height` + `marginBottom` sigue sumando **162**,
que es lo que clava «en DoubleTree» en y=492.

⚠⚠ **Y apareció un fallo que se entregó el 17-09 sin que nadie lo viera.** La
banda del QA de «Tu día» arrancaba en x=162 y la tinta arranca en **140,5**: se
saltaba la «T», justo la letra que cae sobre la viga clara del cielo. El QA
cantaba 3,27:1 y la tinta real daba **2,71:1**, bajo la vara de 3. Al bajar el
bloque entra en la parte del velo que ya pesa y sube a **3,35:1**. La banda queda
corregida y ahora **sale del contorno de los glifos** (fontTools + la línea base
de Chrome), no de mirar el render. Memoria: `banda-de-qa-sale-del-glifo`.

**Dónde quedó.**
- Drive: **reemplazada en su sitio** en `S5 HILTON SEP 2026 › DT`, mismo
  `fileId` `1XOgP7k-vucZaNgBEEB6Ct-i-UpPnHZgx`, así que **el enlace que ya
  circuló sigue sirviendo**. Las otras cuatro no se tocaron.
- Entrega local: `out/hilton/dt/c1-s5/entrega/C1 S5 DT n°1.mp4` (2160×2700, 5,06 s).
- Composición: `src/compositions/hilton/DtC1S5Dia.tsx` — cuatro números:
  `height/marginBottom` 154/8, el `<svg>` en `left: -12.87, top: 13.69`,
  `<Circulo ancho={306} alto={154}>` y el texto en `top: 54`.
- QA: pasa entero. Typecheck limpio.
- Página de revisión: `out/hilton/dt/c1-s5/revision-r3.html`, con el antes/después
  al tamaño real y el detalle de la tilde a 2×.

**Qué sigue.** Lo mismo que dejó el 17-09, sin cambios: pedirle a contenido el
**slide del GYM** (y decidir con Eli que sería la única lámina sin video) y la
**hora del cierre**. Al insertar el GYM hay que **RENUMERAR**: el cierre pasa a
ser la n°6.

**Abierto.**
- ✅ **La regla ya está en el manual** — `clients/hilton/CLAUDE.md` § «RONDA 3
  DEL CARRUSEL S5 (21-09): LAS CAJAS DEL QA SE CALCULAN, NO SE MIRAN». Se
  commiteó **sólo esa sección**, armando el índice con `hash-object` +
  `update-index`, porque otra sesión tenía 156 líneas suyas sin commitear en el
  mismo archivo (Between: «EL CUADRO DE VIDRIO» y la ronda del titular). **Su
  trabajo quedó intacto en el árbol y lo tiene que subir ella.**
- Siguen abiertos los puntos del 17-09: portada sin lockup (a confirmar por
  escrito), los textos con punto final, el `12:00`, y la gente al fondo de los
  clips del salón y la portada.
- El estado de la celda en la grilla sigue siendo `REVISAR CONTENIDO`.

---

## 2026-09-17 (cierre 2) · Eli (Windows) — DT, CARRUSEL DE VIDEOS DE LA S5: **APROBADO**

**Qué se hizo.** Se diseñó y se entregó el **carrusel de videos «Tu día en
DoubleTree»** (FEED col M · 28-09 · 12:00), la primera pieza ANIMADA que el
estudio produce para esta cuenta. Cinco láminas de **5,0 s** a **2160×2700**,
aprobadas por Eli en la ronda 2.

Las cinco salen de material filmado del hotel: la **sesión de video del 16-09**
de Scarlette (`SESIÓN VIDEOS`, que hasta hoy no estaba mapeada en ningún manual) y
el único clip de exterior, que vive en la otra carpeta — `CONTENIDO HOTEL 2026 ›
Exterior hotel`.

| | lámina | clip |
|---|---|---|
| n°1 | Portada · «Tu día / en DoubleTree / by Hilton Santiago–Vitacura» + DESLIZA | `Exterior hotel / IMG_1640` |
| n°2 | 8:30 · Desayuno antes de la reunión | `DESAYUNO BUFFET QB / IMG_5700` |
| n°3 | 9:30 · Reunión en salón | `SALÓNES / IMG_5785` |
| n°4 | 12:00 · Tiempo para ti | `COWORK / IMG_5736` |
| n°5 | Cierre en la habitación | `HABITACIONES / IMG_5741` |

**La ronda 2**, que es de donde salen casi todas las reglas nuevas, fueron seis
correcciones de Eli: usar los videos de los dos enlaces · sacar el verde de DT ·
abrir el tracking de los titulares · **alinear bien a la izquierda** · subir la
calidad · y acercar la portada a la referencia. Cada una, con lo que se midió
para resolverla, está en `CLAUDE.md § RONDA 2 DEL CARRUSEL S5`.

**Dónde quedó.**
- Entrega: `out/hilton/dt/c1-s5/entrega/C1 S5 DT n°1..5.mp4` (2160×2700, 5,0 s).
- **Subidas a Drive** en `S5 HILTON SEP 2026 › DT`, sueltas en la carpeta (no se
  creó subcarpeta a propósito: la crearía el token del estudio y no Eli, y en esta
  cuenta eso ya dio problemas de permisos). La ronda 2 **reemplazó los mismos
  archivos**, así que los enlaces de la ronda 1 siguen sirviendo.
- Composición: `src/compositions/hilton/DtC1S5Dia.tsx`, carpeta `DT-Carrusel-S5`.
- El aparato: `dt-c1-s5-fotos.py` · `dt-c1-s5-clips.py` · `dt-c1-s5-qa.py` ·
  `dt-c1-s5-rendir.py` · `dt-c1-s5-revision.py`.
- Página de revisión: `out/hilton/dt/c1-s5/revision-r2.html`.
- QA: pasa entero — contraste de las 16 tintas contra su fondo real medido en el
  primer y el último fotograma, y **las 15 franjas de texto alineadas en x=88**.

⚠️ **Los clips intermedios NO viajan en git** (156 MB, porque en la ronda 2
dejaron de reescalarse para ganar calidad). Es una excepción declarada a «el
render vuelve al repo», y es segura: `dt-c1-s5-clips.py` documenta el ID de Drive
de cada `.MOV`, el tramo, el recorte, la gradación y la velocidad, así que se
reconstruyen con **un comando** y de forma determinista.

**Qué sigue.**
1. **Pedirle a contenido el slide del GYM.** El brief no lo trae y la fila
   COMENTARIOS PARA DISEÑO lo pide («Faltó GYM!»). La lámina está armada y la hora
   la da el propio comentario (16:00). ⚠️ **No hay video de gimnasio en ninguna
   carpeta** —ni en la sesión del 16-09 ni en `CONTENIDO HOTEL 2026`, que sólo
   tiene 7 `.MOV` de iPhone—: hoy quedaría con la foto `HDT_82` y sería la única
   lámina que no es video. Eso hay que decidirlo con Eli.
2. **Pedirle a contenido la hora del cierre.** El comentario da tres horas y la
   cuarta es la del gym; para «cierre en la habitación» no hay. Va sin sello de
   hora; es un prop y entra en un render.
3. Al insertar el GYM hay que **RENUMERAR**: va entre la n°4 y la n°5, así que el
   cierre pasa a ser la n°6. El portal levanta por nombre.

**Abierto.**
- ⚠️ **La portada quedó SIN el lockup** y firma con la versalita al pie, como las
  otras cuatro y como la referencia. Se apoya en §B («en feed el logotipo por
  defecto no va»), pero es una decisión de marca que conviene que Eli confirme por
  escrito; volver a ponerlo es un minuto.
- Los cuatro textos del brief **terminan en punto** y la regla F.1 de DT dice que
  los títulos no llevan. Van literales (§G: el copy no se toca). Informado.
- «12» del comentario se compuso **12:00**, para que la columna de horas sea una
  sola serie. Informado.
- En el clip del salón hay **dos personas al fondo** (~20 px, sin rostro) y en el
  de la portada **gente de espaldas** entrando. Si molestan, `IMG_5783` y
  `IMG_5784` son la misma sala vacía.
- El estado de la celda en la grilla sigue siendo `REVISAR CONTENIDO`.

---

## 2026-09-17 · Eli (Windows) — DT, BANCO DE PRUEBAS: mejorar una edición de Premiere desde código

⚠️ **No es pieza de grilla y no reemplaza nada entregado.** Eli preguntó si se
puede editar en Premiere en conjunto y mejorar las transiciones de texto, y puso
una historia de prueba: `F:/Carpeta de grillas Hilton 2026/SEPTIEMBRE/DT/S5/
ST PRUEBA PARA CLOUDE CODE/ST PRUEBA CLOUDE.prproj` (copia de la ST n°2 de la S2).

### Lo que se hizo

**El `.prproj` se leyó entero desde código** — es XML comprimido con gzip. Salió
la línea de tiempo exacta (mesa 1080×1920, 9,64 s, 8 pistas, **0 keyframes**) y
hasta el TEXTO de los siete gráficos esenciales, decodificando el base64 del
parámetro «Texto de origen». Método en la memoria `prproj-se-lee-desde-codigo`.

**El hallazgo grande: los incluidos caen sobre la foto equivocada.** «+Botella de
espumante.» corre de 0,52 a 3,00 —o sea sobre la CAMA— y la foto del BAR, que es
justo la del espumante, se queda sin texto propio. El orden de fotos de Eli ya
cuenta bien la historia; era la edición la que no lo seguía.

Los otros seis: el corte de los 3,00 s no anuncia nada (el titular cruza dos
fotos), las tres fotos están clavadas, tres de las cuatro transiciones son la
misma máquina de escribir —lineal, misma cadencia para 19 y para 33 caracteres—,
todo pasa en el primer segundo y medio y después nada hasta 5,24, ningún texto
tiene salida, y «Escapada Romántica» aparece sin animación ninguna.

Se armó el antes y el después **con las mismas fotos, textos, tipografía, velo y
diagramación**, para que la comparación aísle sólo la edición.

### Dónde quedó

| Qué | Dónde |
|---|---|
| La composición (las dos versiones + guía) | `src/compositions/hilton/DtStPrueba.tsx` |
| Registro en Remotion | `src/DtEntry.tsx`, carpeta `DT-Prueba-ST` |
| La página que mira Eli | `scripts/dt-st-prueba-revision.py` |
| Renders y página | `out/hilton/dt/prueba-st/` (gitignored) |

### Dos cosas medidas que decide Eli

1. ⚠️ **El logotipo cae en 4,15–5,12:1** sobre las tres fotos, bajo el 6,7–9,3 de
   §B.4. La rampa de DT nace en 0 arriba y ahí no recibe ayuda; para llegar a 6,7
   haría falta α ≈ 0,36–0,46 en esa banda, o sea un velo superior de verdad — que
   es lo que ella marcó como «forzado» en la ronda 4 del Día del Turismo. En azul
   es peor (3,13–3,86:1). Se dejó medido y sin tocar: cambiar la regla del velo
   no lo decide una pieza de prueba.
2. ⛔ **STAG NO TRAE EL SIGNO `+`.** Verificado con `fontTools` sobre los nueve
   cortes: a todos les falta `U+002B`, y no estaba en la lista documentada. O sea
   que «+Botella de espumante.» en Stag-Regular **no dibuja su primer carácter**.
   En Premiere se ve porque el sistema mete una fuente de reemplazo — pero ese
   `+` no es Stag. Se corrigió el guard `stagSirve()` de `src/brand/doubletree.ts`
   para que lo atrape. **Hay que revisar si ese `+` aparece en otras piezas de DT.**

El velo sí quedó resuelto: con la rampa **ya aprobada** del Día del Turismo el
titular da 5,56–8,10:1 y los incluidos 5,05–8,30, sin cargarla más (se probaron
rampas de 0,73 y 0,80 y se descartaron).

### ⭐⭐ RONDA 2 — «SE SOLAPAN»: LO QUE ESTORBA LA TINTA ES EL OBJETO, NO OTRO TEXTO

Eli sobre la primera versión: «se ve una leve deficiencia en los textos. Se
solapan. **Habitación para dos** y **buffet**, ese texto como que queda
interceptado con otros. Trata de ubicarlos de mejor manera. Lo demás lo veo
sumamente bien, como para a futuro hacer algo muy similar.»

**Ningún texto se solapaba con otro** — se revisó fotograma a fotograma. Lo que
los interceptaba era **la FOTO**: la mano con el macarón caía justo en medio de
«Habitación para dos», y el plato con el vaso de jugo cruzaba «Incluye desayuno
buffet para dos.». Nombró esas dos y **no** la del bar, que es exactamente el
orden del daño — o sea que estaba leyendo bien y el problema era real.

#### ⭐⭐⭐ 1. EL CONTRASTE NO VE ESTO. HAY QUE MEDIR EL **DETALLE**

Las tres bandas **pasaban** la vara de luminancia de `la-tinta-la-manda-el-fondo`
(5,05–8,30:1) y aun así el texto se leía mal, **porque lo que estorba no es el
brillo del fondo sino su TEXTURA**. Es un modo de falla que la regla del velo no
cubre, y que no se ve en los números de contraste.

La medición que sí lo ve: **energía de gradiente** (`|∂x| + |∂y|`) bajo la banda,
y con dos detalles que son los que la hacen funcionar:

1. **en el ancho REAL de esa línea**, no en toda la columna de texto;
2. **mirando el peor tramo de 60 px, no el promedio** — un objeto chico en medio
   de la línea la arruina y el promedio de la fila ni lo nota. Con el promedio,
   la foto de la cama daba «bien»; con el peor tramo, saltó al tiro.

#### ⛔⛔ 2. LO QUE SE PROBÓ Y NO SIRVE: REENCUADRAR LA FOTO

Se barrió (escala, deriva) buscando fondo tranquilo bajo el texto. Mejoraba la
medición un **23–46 %**… y **le cortaba la cara a la pareja en las tres fotos**.
El optimizador se va al borde del recorte porque «fondo tranquilo» significa «sin
gente», que es justo lo contrario del encargo. Se compuso, se miró y se descartó.

**La regla que queda: la foto no se toca para acomodar el texto. Se mueve el
texto.** Que además es lo que ella pidió, textual.

#### ⭐ 3. EL AJUSTE: SUBIR EL PAR TITULAR + INCLUIDO

Las tres fotos **coinciden** en que el carril limpio del incluido está en
**y ≈ 1160** y no en 1235, así que no hizo falta moverlo plano por plano.

| banda | antes | ahora | peor foto |
|---|---|---|---|
| incluido | 1235 | **1160** | 22,12 → **18,62** (−16 %) |
| titular | 1084 | **1003** | 24,96 → 27,15 (**+9 %**) |

**El titular PIERDE un 9 % y se aceptó a propósito:** son 106 px en Stag Medium
Italic con sombra y aguanta un fondo movido; el incluido son 44 px en Regular y
es el que ella marcó. Cuando hay que repartir el daño, se le carga a la tinta
grande. El contraste en las posiciones nuevas sigue pasando (titular 5,12–7,92 ·
incluido 5,18–8,10).

#### ⭐ 4. Y EL BLOQUE QUEDÓ EN DOS GRUPOS, NO EN CUATRO LÍNEAS SUELTAS

```
titular ─66─ incluido      ← el mensaje
             ─129─
precio  ─62─ CTA           ← la oferta
```

Antes eran **62 · 54 · 62**: cuatro líneas a distancia pareja, sin grupos. Es la
regla `jerarquia-de-bloque-de-texto` —el salto ENTRE niveles mayor que el salto
DENTRO del nivel— y acá salió gratis al subir el par.

⚠️ **Esto NO se sube a ninguna parte.** Eli: «no es para subirlo a ningún lado ni
en Drive ni nada de eso, es solamente para tenerlo ya guardado, en mente de cómo
podemos volver a mejorar una edición ya hecha.» Queda en el repo y nada más.

### ✅ APROBADO — el método queda como referencia

Eli, después de la ronda 2: **«quedó bien»**. Y antes, sobre la primera versión:
«lo demás lo veo sumamente bien, **como para a futuro hacer algo muy similar**»
y «necesito que sepas más adelante trabajar así los siguientes archivos de videos
de DT».

⇒ **Esto no fue un encargo suelto: es cómo se van a trabajar sus videos de DT.**
El aparato queda en la memoria `dt-video-de-premiere-a-codigo`.

**Qué sigue:** el paso pendiente de la conversación — **probar si Premiere Pro
2026 carga un panel CEP** (la máquina tiene CSXS.12 y ya corren paneles, incluido
el de Magnific en Illustrator) o si exige UXP. Ese panel es lo que permitiría
escribir en su línea de tiempo en vivo, en vez de entregarle piezas rendidas.

**Abierto:**
1. Las dos decisiones medidas que quedaron para ella: **el velo del logotipo**
   (4,15–5,12:1 contra la vara 6,7–9,3 de §B.4) y **el `+` de Stag en otras
   piezas** de DT ya entregadas.
2. ⚠️ **`src/DtEntry.tsx` sigue sin commitear.** Importa `DtC1S5Dia.tsx`, que es
   el carrusel S5 que quedó en vuelo en el mismo árbol sin subir; commitear el
   entry sin ese archivo rompe el repo. Falta agregarle el
   `<Folder name="DT-Prueba-ST">` cuando el árbol esté limpio — es un commit de
   una línea y **la composición ya está subida**, sólo le falta el registro.
3. El `.prproj` de ella **no se tocó**: la versión nueva es un render aparte, no
   una modificación de su proyecto. Y **nada se subió a Drive** — es banco de
   pruebas, queda en el repo y nada más.

---

## 2026-09-16 (cierre 4) · Eli (Windows) — BETWEEN, RONDA 5: el sello del concurso y la CTA

**La primera ronda del CLIENTE sobre este carrusel.** Llegó por Slack, de Nicolás
Ávila con Scarlette, y son dos cambios, los dos de la **portada**:

1. «Darle más protagonismo a la palabra **CONCURSO**. Que sea más grande y quizás
   usar otro tono de café, o algún recurso visual que haga que destaque más y se
   vea llamativo de inmediato.»
2. «Cambiar **POSTULA AQUÍ → DESLIZA** por **¿Quieres el puesto? → Desliza para tu
   entrevista**.»

Eli agregó en la misma vuelta: «haz una opción donde CONCURSO esté en una **caja
beige más grande estilo la ref**».

### Lo que se hizo

**El sello no se agrandó a secas, porque el defecto no era el tamaño.** Medido:
el sello y la caja «1 MES DE CAFÉ GRATIS» eran **la misma caja taupe con tinta
beige**, y dos cajas iguales en una lámina no se jerarquizan entre sí. Se invirtió
—fondo beige `#FFF9EB`, tinta café `#675B49`, que es la caja de color plano de la
`REF 1` al revés— y así la lámina queda beige contra taupe.

⛔ **No se inventó un tercer marrón**, que era la primera vía que sugería el
cliente: la paleta de Between son dos tintas y un marrón nuevo es abrirle un color
a la marca. Queda anotado que `#4C4133` daría 6,13:1 si algún día se decide.

**Se le pusieron a Eli las dos opciones rendidas y al tamaño de publicación**
(`out/hilton/between/concurso-s3-r5/revision-r5.html`) y **eligió la B**:

| | dónde | cuerpo | resultado |
|---|---|---|---|
| A · `tag` | línea del lockup | 36 (+29 %) | mejor compuesta, pero 36 es el TECHO: el lockup arranca en x=408 |
| **B · `caja`** ✅ | encabeza la pila | **52 (+86 %)** | lo que el cliente pidió: se ve de inmediato |

Yo había recomendado la A y me equivoqué de pregunta: el encargo era *tamaño*, y
en esa posición no había tamaño que dar. **La posición que limita el tamaño es la
que se cede, no el tamaño.** Las cuatro reglas de la ronda quedaron escritas en
`clients/hilton/CLAUDE.md § S3 · CONCURSO · RONDA 5`.

**La CTA** va literal y en dos líneas, partida por la flecha —arriba la pregunta,
abajo la acción—: entera mide 700 px y el canal limpio de esa franja termina en
x≈630. El cuerpo no se bajó (sigue en 32); lo que sube es el interlineado, de 1,1
a 1,22. De regalo, el remate enlaza con la N2, que se titula «TU ENTREVISTA
EMPIEZA AHORA».

### ⚠️ Un tropiezo de proceso que conviene no repetir

La página de revisión tomaba el «antes» de la carpeta de **entrega**, que es el
archivo que la propia entrega sobrescribe: al re-rendir, la página pasó a comparar
el después contra sí mismo sin avisar. Ahora la copia de la ronda anterior se
guarda antes de re-rendir (`concurso-s3-r5/r4-N1-respaldo.png`) y el «antes»
apunta ahí.

### Dónde quedó

- Sólo la **N1** cambió y sólo ella se re-subió, **reemplazando el mismo archivo**
  (`1A9KfIwPp_XzEi4prUVHzXmDM5zX-27mB`, carpeta `C1 S3 CONCURSO` de
  `S3 HILTON SEP 2026 / BW`): **el enlace de la grilla no cambió**. Verificado con
  el conector MCP — 5.118.684 bytes, los mismos que el local, `createdTime` intacto
  de la ronda 4 y `modifiedTime` nuevo. La **N2 no se tocó**.
- Código: `src/compositions/hilton/BetweenC1S3Concurso.tsx` — el sello es ahora una
  variante (`taupe` · `tag` · `caja`) y se rinde con
  `--props='{"sello":"caja"}'`; el default del componente ya es `caja`.
- Página de la ronda: `scripts/between-concurso-s3-r5-revision.py` →
  `out/hilton/between/concurso-s3-r5/revision-r5.html`.
- QA de carrusel: mediana 197 vs 201, calidez 37,7 vs 33,1 — mismo tono. El único
  aviso de `between-qa.py` es el falso positivo conocido de la N1.

### Qué sigue

1. **Esperar la respuesta del cliente a esta ronda.** El carrusel ya está en su
   carpeta con el enlace de siempre, así que Nicolás y Scarlette ven la versión
   nueva sin que nadie les mande nada.
2. **Pedirle a contenido la fecha del concurso.** Es lo único que le falta a la
   pieza para estar completa.
3. Si piden más aún sobre el sello, la vía que queda **sin** tocar la paleta es el
   giro y el contorno blanco del sticker; el marrón nuevo `#4C4133` está medido
   pero lo aprueba la marca, no la pieza.

**Abierto.** Sigue pendiente pedirle a contenido la **fecha** del concurso: la
grilla dice `X DEFINIR` y el concurso corre del 21 al 30-09. Y siguen los
pendientes de los cierres anteriores: Between **sin `clients/hilton/reglas.yaml`**,
las **`GUIA CM`** en local sin decidir cómo llegan al CM, **`BETWEEN.logo.cafe`
apuntando a un PNG negro**, y el legal VIEJO en `BetweenCumple.tsx:112` y
`BetweenSeptiembre.tsx:794`.

---

## 2026-09-16 (cierre 3) · Eli (Windows) — BETWEEN, RONDA 4: el fondo es UNA hoja de papel

> «El fondo debe ser el mismo beige papel para ambas slides, que sea plano y
> transicione.»

Es sobre el mismo carrusel del concurso que la ronda 3 había dejado «continuo», y
la corrección enseña algo que el manual no tenía escrito.

### ⭐⭐⭐ Igualar la LUZ no iguala el MATERIAL

La ronda 3 dejó el salto de luminancia en la costura en **0,95** —invisible— y aun
así ella seguía viendo dos fondos. Lo que no coincidía no era el tono: la portada
era una **pared lisa** y la slide 2 un **panel de veta vertical de madera**, más
rosado. Un polinomio de grado 3 corrige el campo de luz; no convierte madera en
yeso.

Así que no se persiguió más la costura: **se cambió la superficie**. Se sintetiza
UNA hoja de papel beige de 4500 × 2813 —las dos láminas juntas— y cada slide se
queda con su mitad. La continuidad deja de corregirse y pasa a existir por
construcción. Medido sobre la pieza rendida: **0,97** de salto, y ahora en las
**2.812 filas**, no sólo en el 45 % de arriba donde había pared en las dos.

⭐ **El retrato y el bodegón no se re-generaron**: están aprobados y regenerarlos
era perderlos. Sólo cambió la superficie de atrás, con el recorte intacto.

### ⛔⛔ La máscara del crecimiento no sirve para REEMPLAZAR

`between-concurso-s3-fondo-continuo.py` crece desde el canto sobre la imagen
reducida a ¼ con `binary_dilation(12)` — saltos de 48 px reales, que **saltan por
encima del borde blanco del recorte**. Para corregir iluminación daba lo mismo;
para reemplazar el fondo pintaba papel encima del escritorio. Medido, la fuga
metía el escritorio entero en el «fondo»: 89,1 % del cuadro en vez de 84,2 %.

Lo que sirve es `scipy.ndimage.label` a resolución completa, quedándose con las
componentes que tocan el **canto SUPERIOR**: la pared lo toca en las dos láminas,
el escritorio nunca. Sin fugas y sin lista de excepciones.

### ⭐⭐ El tono del papel se MIDE

`#DFC9BB`, la mediana de las dos paredes aprobadas: el papel entra en el sitio
exacto que ocupaba la pared y ningún contraste ya aprobado se mueve.

⛔ **No se usó el `papel-beige.png` crema (`#FFF9EB`) de la story del 18-09.** A
sangre gana en el titular (6,31:1 contra 4,17:1) y **pierde en las dos cosas que
sostienen el collage**: el contorno blanco del recorte cae a 1,05:1 —el sticker
deja de existir— y la tarjeta crema de la N2, que no tiene contorno, se funde con
el fondo. El fondo de una pieza no se elige por el contraste del titular solo.

Y «plano» tiene amplitud: la receta de papel se reusa tal cual salvo el
**manchado, que baja de 2,8 a 1,4** — a 2,8 funciona en un cartel de 1700 px, pero
a sangre en 4500 px la hoja se lee como nubes.

### ⭐⭐ Al cambiar el fondo se va también la sombra del sticker

Y sin ella el recorte es un papel pegado. Se rehace desde la silueta y **no a
ojo**: se midió la que traían las láminas aprobadas —cociente contra su propio
campo de luz, por franjas de distancia al filo— y la síntesis se ajustó a ese
perfil (0,948 · 0,977 · 0,998 contra 0,946 · 0,984 · 0,999). Es una sombra corta:
a 25 px ya no existe.

**Dónde quedó.** Las dos láminas **reemplazan el mismo archivo** en
`S3 HILTON SEP 2026 / BW / C1 S3 CONCURSO` (`N1`
`1A9KfIwPp_XzEi4prUVHzXmDM5zX-27mB` · `N2` `1IGWnaOypxzO3jnZVrQ8deZg1cgyWMkMr`),
verificadas por `fileSize` y `modifiedTime` con el conector MCP: **los enlaces de
la grilla no cambiaron**. Los dos fondos se reproducen **byte a byte** (`cmp`).
Script nuevo: `scripts/between-concurso-s3-fondo-papel.py`. Assets nuevos:
`c1-portada-papel.jpg` y `c1-escritorio-papel.jpg` — las escenas aprobadas quedan
intactas como fuente. Revisión actualizada con el antes/después:
`out/hilton/between/revision-16-09.html`.

**La grilla, revisada hoy antes de tocar nada:** ninguna ronda nueva del cliente.
Lo único que se movió en las cuatro pestañas son tres estados que pasaron de
`EN CAMBIOS` a `CORREGIDO` (FEED col 13 y STORIES cols 17 y 18) — o sea, lo que se
entregó hoy. La instantánea de `grillas/between-septiembre-2026-vivo/` sigue
sirviendo de base para el próximo diff.

**Abierto:** lo mismo de los cierres anteriores. Sigue pendiente pedirle a
contenido la **fecha del concurso** (`X DEFINIR` en la grilla).

---

## 2026-09-16 (CIERRE DEL DÍA) — Elisabet Soto · BETWEEN

Resumen para el relevo. El detalle de cada ronda está en las entradas de abajo
(rondas 1 a 4 del mismo día).

> ⚠️ **Actualizado:** después de este cierre entró la **ronda 4** —el fondo del
> carrusel del concurso pasó a ser UNA hoja de papel beige, plana y cortada en
> dos—. Está en la entrada de más arriba, «cierre 3».

**Qué se hizo:** se produjo el **carrusel del CONCURSO «Se busca: CEO del café»**
(FEED col 10, pieza nueva, dos láminas) y se cerraron **tres ajustes de grilla**:
la ST del 21-09 (fuera «Masa» + legal), la ST del 22-09 (legal, reubicado bajo la
copa) y **la portada** del carrusel PROMOS TO GO del 22-09, que cambió de foto
porque el cliente corrigió el enlace. Cuatro rondas de correcciones de Eli en el
mismo día, todas aplicadas y medidas.

**Dónde quedó:** todo entregado y verificado en Drive.
· `C1 S3 CONCURSO N1/N2.png` → carpeta **nueva** `C1 S3 CONCURSO` dentro de
  `S3 HILTON SEP 2026 / BW` (`1eXZnhj5-2j7o4AuwClf5dngcn6k9oQzC`).
· Las dos ST y la portada To Go **reemplazan el MISMO archivo**, así que los
  enlaces que el cliente tiene en la grilla no cambiaron.
· Código: `BetweenC1S3Concurso.tsx`, `BetweenTrazosConcurso.tsx`, y los cambios en
  `BetweenStS4.tsx` y `BetweenSeptiembre.tsx`.
· Scripts: `between-concurso-s3-{generar,fotos,fondo-continuo,entrega}.py`,
  `between-st-s4-entrega.py`, `between-togo1-r25.py`, `between-revision-16-09.py`.
· **Las cinco piezas reproducen byte a byte** desde el repo (`cmp`).
· Revisión para mirar: `out/hilton/between/revision-16-09.html` (imágenes
  embebidas, se abre con doble clic y se puede reenviar tal cual).
· Instantánea nueva de las 4 pestañas de la grilla en
  `grillas/between-septiembre-2026-vivo/` — **ésa es la base del próximo diff**.

**Qué sigue:**
1. **Pedirle la fecha del concurso a contenido.** La grilla dice `X DEFINIR` y el
   concurso corre del 21 al 30-09, con el ganador el 1 de octubre.
2. Esperar la ronda del cliente sobre las cuatro piezas subidas hoy.
3. FEED col 15 sigue `PENDIENTE POR CLIENTE`: pidió cambiar el espacio de «nuevas
   promos de desayuno» por otro tema.
4. El reel orgánico del 15-09 quedó **RECHAZADO** y sin contenido en la grilla.

**Abierto:**
· ⚠️ **El Strudel queda con una discrepancia informada:** el titular dice «CUATRO
  INGREDIENTES» y el mosaico tiene cuatro cuadrantes, pero el listado quedó en
  tres. Eli confirmó que el cambio es sólo eliminar la palabra; si el cliente lo
  nota, bajar a «TRES» es decisión suya.
· ⚠️ La tapa del vaso de la portada To Go **queda cortada por el canto de arriba**.
  Es inevitable con esa foto y está demostrado en `between-togo1-r25.py`.
· ⛔⛔ **El token del estudio ya no LEE el Drive de Hilton** (scope `drive.file`):
  sube y reemplaza bien, pero para listar, verificar o crear carpetas hay que usar
  el conector MCP de Drive. Las cuatro subidas de hoy se verificaron así.
· ⚠️ **Dos sesiones escribieron en este mismo directorio hoy** (los commits
  `fbdb431` de Between y `39dc674` de Piso18, los dos a las 15:46, mientras esta
  sesión trabajaba). No se perdió nada, pero conviene no tener dos ventanas
  abiertas sobre la misma carpeta.
· Siguen de antes: Between **sin `clients/hilton/reglas.yaml`**, las **`GUIA CM`**
  en local sin decidir cómo llegan al CM, **`BETWEEN.logo.cafe` apuntando a un PNG
  negro**, el Strudel como producto GENERADO a la espera de foto real, y los
  falsos positivos de `between-qa.py`.

---

## 2026-09-16 (cierre 2) · Eli (Windows) — BETWEEN, RONDA 3: el fondo continuo, la polaroid y la raya

> «Quiero que la textura beige del fondo hagan transición en ambas slides del
> carrusel del concurso. Además, para el slide 2 añade la polaroid de foto de la
> misma chica de frente, feliz, que es igual a la referencia del slide 2. Muy
> sutil, donde no tape textos. Las ST quedan okey. El último carrusel se ve muy
> oscuro y con una raya, te adjunto un pantallazo: mejora la foto un poco, se ve
> un poco extraña y oscura arriba, baja un poco la transparencia si necesitas.»

### 1. ⭐⭐⭐ LA PARED CONTINUA SIN VOLVER A GENERAR

`scripts/between-concurso-s3-fondo-continuo.py`. En el cumpleaños la continuidad
se resolvió generando UN panorama y cortándolo en dos. **Acá no se podía**: las
dos escenas ya estaban aprobadas —la persona la aprobó ella en esta misma
sesión— y regenerar significaba perder el retrato. Así que la continuidad se
construye sobre lo que ya hay, y sin mover un píxel del sujeto:

1. máscara de fondo por crecimiento desde el canto sobre los píxeles de pared
   (el borde blanco del recorte, que está en 243+, corta el crecimiento solo);
2. el campo de cada lámina y el campo del PAR, los dos como polinomio de grado 3;
3. se aplica `nuevo − actual` **sólo al fondo**: como es baja frecuencia, el
   grano de la pared se conserva exacto;
4. convergencia de costura, que es lo que hace un panorama de verdad.

**Los tres intentos, medidos** (salto de luminancia en la costura; el umbral de
la cuenta es 1,5):

| Método | Salto |
|---|---|
| campo actual por desenfoque gaussiano ancho | **18,66** ⛔ |
| campo actual por polinomio (sin convergencia) | **3,30** ⚠️ |
| + convergencia de costura (500 px de caída) | **0,95** ✅ |

⛔ **Por qué el gaussiano no sirve:** se sesga contra el canto del cuadro —la
normalización por la máscara tira los valores hacia adentro— así que el campo
sale mal justo donde hay que medir. Dos polinomios no tienen ese problema.

⚠️ Y una trampa de scipy: `binary_erosion` erosiona también el BORDE del cuadro,
así que la máscara quedaba vacía en la costura (0 filas comparables). Va
`border_value=1`.

**De regalo, el QA de carrusel pasó de 195/202 a 197/196 de mediana:** el fondo
continuo igualó las dos láminas mejor que cualquier gradación.

### 2. La polaroid — el personaje se fija con la pieza aprobada

El retrato de frente se generó pasándole como referencia **la portada aprobada y
un recorte de su cara**. Es la forma práctica de fijar el personaje (memoria
`generar-personas-nombrar-el-tipo`: «el perfil aprobado se fija como referencia o
cada generación da una cara distinta»), y salió la misma mujer.

Va abajo a la izquierda, 188 px, girada 4°, con el pie del marco MÁS ANCHO que
los lados —sin eso no se lee como polaroid—. Es el único hueco de la lámina sin
texto ni producto: el beige limpio llega hasta x≈270 entre y=1000 y 1250, y el
legal vive dentro de la tarjeta.

### 3. ⭐⭐ LA RAYA DEL CARTÓN: `cv2.inpaint` NO SIRVE SOBRE TEXTURA

La raya es un pliegue claro del cartón (x 508–612, y 424–622 del asset de
2155×2694). El primer intento fue `cv2.inpaint` (Telea) y **dejó un parche
LISO, sin grano**: sobre kraft eso se ve MÁS que la raya. Es la misma familia de
error que el manual ya tiene escrita para los recortes, en versión textura.

Lo que funciona es un **clonado por separación de frecuencias**: se toma el mismo
tramo del vaso 150 px a la derecha —misma altura, misma banda de luz— y se le
trasplanta sólo su ALTA frecuencia, conservando la BAJA del destino. Se va la
raya, se mantiene el sombreado del cilindro y el grano sigue siendo real.

### 4. «Oscura arriba» se arregla en la FOTO, no en la transparencia

El degradado ya estaba en su piso: barrido contra el contraste de la tinta beige
(la marca pide 3:1), **0,60 → 3,27 · 4,79 · 3,95** y **0,55 → 2,91**, o sea que
bajo 0,60 el script se cae. Así que lo que se aclaró fue la foto: un levante de
sombras ponderado por la ALTURA, que se apaga en y=0,45 —justo donde arranca el
bloque de texto— así que la franja de arriba deja de leerse apagada y el
contraste del titular no se mueve ni un punto. Verificado: los tres contrastes
son idénticos antes y después del levante.

**Dónde quedó:** las tres piezas re-subidas reemplazando el mismo archivo y
verificadas por `fileSize`; las tres reproducen byte a byte; la página de
revisión actualizada con esta ronda.

**Abierto:** lo mismo de los cierres anteriores.

---

## 2026-09-16 (cierre) · Eli (Windows) — BETWEEN, RONDA 2: cuatro correcciones suyas

Sobre lo entregado esta misma tarde. Sus palabras, literales:

> «La chica del post de concurso debe verse más blanca chilena, pelo ondulado y
> con gafas lifestyle. Y la segunda slide no se parece mucho a esta referencia 2.
> Solo un poco ambas, añade esas ilustraciones sencillas de la slide 2. Legal de
> la st strudel en beige o con caja, que no se ve nada con el color que tiene. Y
> la última no se ve nada, el carrusel de la portada muy oscura y quemada; no
> edites la foto original, déjala así tal cual el link, pero con textos y diseños
> de arriba y transparencia. Solo reemplaza la foto.»

### 1. La persona de la portada — se pide NOMBRANDO el tipo

Escena regenerada. ⚠️ «Más blanca» **no** se traduce restando color: pedir «menos
morena» empuja el fenotipo al nórdico (memoria `generar-personas-nombrar-el-tipo`).
Va «una mujer CHILENA de piel clara, rasgos latinoamericanos, pelo castaño
ONDULADO y suelto, con anteojos de marco fino y traslúcido». El logotipo del vaso,
revisado al 300 %: **BƎTWEEN / COFFEE & BAR** completo a la primera.

### 2. Las ilustraciones sencillas — segunda excepción a la regla del trazo

`src/compositions/hilton/BetweenTrazosConcurso.tsx`. Es la misma excepción que se
abrió el 08-09 para las banderitas, con las cuatro condiciones del manual: lo pide
la diseñadora para una pieza, el motivo no existe en su `.svg`, va en un solo color
de marca (café `#675B49`) y el trazo es de grosor constante con puntas redondeadas.
Cuatro motivos: las **tres cuñas** que ella recortó de la REF 2, una **chispa** de
cuatro puntas, una **estrella** de contorno y una **flecha** curva.

⚠️ Dos correcciones de posición, las dos por medición: las cuñas de la portada
caían sobre la caja taupe (que va de y=612 a 678 y de x=84 a 620) y partían la
palabra «CAFÉ»; y las de la slide 2 tocaban la «A» de «AHORA» (el titular llega a
x≈928 y cierra en y≈325). **Un trazo se coloca contra el mapa de la pieza, no a ojo.**

### 3. El legal del Strudel — beige DENTRO de caja

Ninguna tinta suelta aguanta esa franja: son los dos cuadrantes claros y miden
159 · 162 · 165 por tercios (beige 1,5:1, café 1,8:1). Con la caja taupe el
contraste deja de depender de la foto: **6,3:1**. Es la salida que el propio
cliente dejó escrita —«cuando no se logra visualizar los textos, puedes dejarlo en
una caja del color café #675B49»— y es la tercera vez que esa frase resuelve algo.

### 4. ⭐⭐ La portada del To Go: la foto NO se grada, y el logotipo se mide ENTERO

- **Fuera toda la gradación.** La pasada anterior igualaba la mediana al set
  (116→102) y enfriaba la calidez (50,9→33,1), y entre eso y el degradado la
  lámina se leía apagada. Ahora entra tal cual el enlace; lo único que queda es
  el recorte 4:5, que no es opcional.
- **El degradado baja de 0,72 a 0,60**, barrido contra el contraste de la tinta
  beige (la marca pide 3:1): 0,72 → 5,41 · 5,54 · 4,77 · 0,65 → 3,92 · 4,98 · 4,05
  · **0,60 → 3,27 · 4,79 · 3,95** · 0,55 → 2,91 (el script se cae).
- ⛔⛔ **Y el error de la pasada anterior, que vale como regla:** el encuadre se
  calculó contra el WORDMARK (fila 2593) y el logotipo impreso son **DOS bandas**
  —wordmark 2239–2513 y «COFFEE & BAR» 2617–2685—, así que el script terminaba
  rozando la segunda. Con el logotipo completo, la ventana no puede pasar de
  2 × (4032 − 2685) = **2694** de alto: queda 2155×2694 desde la fila 1338.
  **Un lockup se mide entero, no por su línea principal.**

**Dónde quedó:** las cuatro piezas re-subidas reemplazando el mismo archivo y
verificadas por `fileSize` con el conector; las cuatro reproducen byte a byte;
`out/hilton/between/revision-16-09.html` actualizada con esta ronda.

**Abierto:** lo mismo del cierre anterior. Se suma que la tapa del vaso de la
portada To Go **queda cortada por el canto de arriba** — es inevitable con esta
foto y está explicado en `scripts/between-togo1-r25.py`.

---

## 2026-09-16 (tarde) · Eli (Windows) — BETWEEN: el CONCURSO de la S3, y tres ajustes de grilla

**Marca: BETWEEN.** Sesión de diseño. Encargo de Eli: «toma los cambios en grilla
que dejó cliente y haz el concurso del carrusel que solicita ahí en la S3, que es
urgente […] súbelo en la carpeta de Drive S3 BW con nombre de C1 S3 CONCURSO,
además necesito los ajustes de grilla S4 y S3».

### Lo que traía la grilla viva (diff contra la instantánea del 10-09)

Se bajó por CSV —el `.xlsx` de Between sigue congelado, el método del 10-09 vale—
y se diffeó por CONJUNTO de cadenas contra `between-septiembre-2026-vivo/`:

| Hoja | Qué cambió |
|---|---|
| FEED col 10 | **PIEZA NUEVA**: «CARRUSEL CONCURSO – SE BUSCA: CEO DEL CAFÉ», `OK PARA DISEÑAR`, fecha `X DEFINIR`, con `REF 1` y `REF2` |
| FEED col 9 | la fecha del «Ella habló» se movió de **16** a **17 de septiembre** |
| FEED col 12 | To Go 22-09 sigue `EN CAMBIOS`; comentario NUEVO arriba: «Perdón, se puso mal el enlace: es esta en la G1 …1ZUClVyKcfy…» |
| FEED col 15 | «Por el momento no tendremos esta info. Cambiar por otro tema por favor» → `PENDIENTE POR CLIENTE` |
| STORIES col 16 | 21-09 Strudel → `EN CAMBIOS` · «Eliminar MASA y agregar legal Imagen referencial» |
| STORIES col 17 | 22-09 Primavera → `EN CAMBIOS` · «Agregar legal Imagen referencial» |
| ORGÁNICOS col 2 | el reel del 15-09 pasó a **RECHAZADO** y su contenido se borró |

⭐ **Las referencias de la grilla SÍ se pueden leer, aunque el CSV no las traiga.**
El CSV pierde los hipervínculos y la API de Sheets rebota el archivo («must not be
an Office file»). La vía que funciona es **`export?format=zip`**, que devuelve el
HTML de cada hoja con sus `<a href>` — y de paso todas las imágenes que el cliente
pegó dentro. Ahí salieron `REF 1` y `REF2`, dos pines de Pinterest, que se bajaron
con el Chrome del sistema en headless a `raw/hilton/between/refs-concurso-s3/`.

### 1 · El carrusel del concurso (pieza nueva, 2 láminas)

`src/compositions/hilton/BetweenC1S3Concurso.tsx` · `BW-F-Concurso-1` y `-2`.

**Las dos referencias comparten UN recurso** y ése era el encargo real: el sujeto
**recortado como sticker con borde blanco**. La REF 1 además pone el titular
grande y el remate dentro de una caja de color plano; la REF 2, una hoja pegada
con la LISTA de ítems. Traducido a Between sin inventarle nada:

- el recorte **se generó ya recortado** (Nano Banana Pro, con la foto real del
  2.º piso y las del vaso To Go vigente como referencia) — no se pegó por código;
- la caja de color plano **es la caja taupe `#675B49`** que la marca ya tiene;
- la hoja con la lista **es la tarjeta crema con filas taupe y casillas ✓** de
  `C1 S2 CUMPLE N2`;
- el sello «CONCURSO» que pide el brief es esa misma caja taupe girada 4°.
- ⛔ NO entraron el papel arrugado, la cinta, las polaroids ni los garabatos de la
  REF 2: el repertorio de línea de Between son los trazos del `.svg` de Eli.

**Entrega:** `C1 S3 CONCURSO N1.png` y `N2.png`, 2250×2812 a 150 ppp, en una
carpeta **`C1 S3 CONCURSO`** creada dentro de `S3 HILTON SEP 2026 / BW`
(`1eXZnhj5-2j7o4AuwClf5dngcn6k9oQzC`). Verificadas por `fileSize` contra el local.

### 2 · S4 · las dos stories (21 y 22-09)

- **Strudel**: fuera «Masa» del listado y entra el legal. ⚠️ El legal va en **café
  y no en beige**, medido: la franja del pie son los dos cuadrantes claros y da
  159–165 por tercios, o sea «sobre L≈150 va café suelto». Con el beige del
  sistema salía lavado. La zona del ícono 🍎 sube a 1345–1495 para no taparlo.
- **Primavera**: entra el legal, y Eli lo corrigió en la misma sesión —«ajusta el
  legal abajo donde indica la flecha porque no se lee bien»—. La posición estándar
  de `LegalAlPie` (bottom 360) lo dejaba **sobre el vidrio de la copa**. Bajó al
  margen de marca (bottom 84): la tinta cae en 1808–1836, 12 px bajo la base de la
  copa (que cierra en 1796) y sobre madera oscura.
- Las dos **reemplazan el MISMO archivo** en `S4 HILTON SEP 2026/BW/STS`, así que
  los enlaces de la grilla no cambiaron.

### 3 · S4 · la portada del carrusel PROMOS TO GO

Eli: «haz el ajuste de la portada, las demás slides están okey según vi
comentarios». El enlace corregido apunta a **IMG_4146** (el vaso sostenido sobre
la mesa), no a IMG_4170 (la entrada) que había usado la r23. Verificado por md5:
es el mismo archivo que `public/assets/hilton/between/togo-sep2026/togo-en-mano-mesa.jpg`,
ya curado en el repo. Bajó como **HEIC con extensión `.jpg`** — no está roto.

**Dónde quedó:**

- `scripts/between-concurso-s3-generar.py` · `-fotos.py` · `-entrega.py`
- `scripts/between-st-s4-entrega.py` (nuevo, reemplaza en el mismo archivo)
- `scripts/between-togo1-r25.py`
- `scripts/between-revision-16-09.py` → `out/hilton/between/revision-16-09.html`
- instantánea nueva de las 4 pestañas en `grillas/between-septiembre-2026-vivo/`
- las 5 piezas **reproducen byte a byte** desde el repo (`cmp`).

**Qué sigue:**

1. ⚠️ **El Strudel queda con una discrepancia INFORMADA:** el titular dice «CUATRO
   INGREDIENTES» y el mosaico tiene cuatro cuadrantes, pero el listado quedó en
   tres. Eli confirmó que el cambio es sólo eliminar la palabra. Si el cliente lo
   nota, la decisión de bajar a «TRES» es suya.
2. El carrusel del concurso no tiene **fecha**: la grilla dice `X DEFINIR` y el
   concurso corre del 21 al 30-09. Hay que pedirle la fecha a contenido.
3. Sigue `PENDIENTE POR CLIENTE` el espacio de «nuevas promos de desayuno»
   (FEED col 15) — el cliente pidió cambiarlo por otro tema.
4. El reel orgánico del 15-09 quedó **RECHAZADO** y sin contenido en la grilla.

**Abierto:**

- ⛔⛔ **El token del estudio ya no llega al Drive de Hilton por `files.get`.** Su
  scope es `drive.file`, así que sólo ve lo que la propia app creó: `files.get`
  sobre cualquier carpeta de Hilton devuelve 404. **Subir SÍ funciona** (crear con
  `parents` y reemplazar por nombre lo que ella misma subió), pero para LISTAR o
  verificar hay que usar el conector MCP de Drive. Las tres subidas de hoy se
  verificaron así.
- Siguen de los cierres anteriores: Between **sin `clients/hilton/reglas.yaml`**,
  las **`GUIA CM`** en local sin decidir cómo llegan al CM, **`BETWEEN.logo.cafe`
  apuntando a un PNG negro**, el Strudel como producto GENERADO a la espera de
  foto real, y los falsos positivos de `between-qa.py` (hoy marcó el borde blanco
  del recorte del concurso como si fuera texto: la tinta que acusa está en
  y 984–1349 y todo el texto de esa lámina vive entre 96 y 760).
- ⛔ Y sigue en pie: **`BetweenCumple.tsx:112` y `BetweenSeptiembre.tsx:794` con el
  legal VIEJO** del cumpleaños.

---

## 2026-09-16 (tarde) — DT · rondas 7 y 8: los dos estáticos de S3 y S4, ENTREGADOS

**Marca: DT.** Sesión de diseño. Dos piezas, tres cambios, **todos pedidos por el
cliente** —no por Eli ni por una superior—, que es la primera vez en esta cuenta.

| Pieza | Dónde | Qué pidió |
|---|---|---|
| **ST 18-09 Fiestas Patrias** (S3) | STORIES col H · `EN CAMBIOS` | Javier Meza, WhatsApp 10:22: «2 ajustes · Quitar punto final · Hacerle más zoom a foto de animadores para que se vean más grandes» · «el resto ok!» |
| **Post n°1 S4 DT · Hilton Honors** (S4) | FEED col K · `EN CAMBIOS` | Grilla, en rojo y **sin tachar**: «Cambiemos foto por habitación de categoría superior y ok!» |

**Lo que NO entró, por decisión de Eli el mismo día:** la **ST animada del 21-09**
(Escapada Romántica, STORIES col J, también `EN CAMBIOS`). Textual: «Para DT no
cambies el video, ese lo hago yo, solo toma los estáticos». Sus cambios quedan
anotados más abajo para cuando ella la tome.

**Lo que se descartó y por qué, para no volver a mirarlo:** FEED col I (16-09,
Opinión Booking) está `APROBADO` **con todos sus comentarios tachados**, y STORIES
col K (27-09, Día del Turismo) sigue en `EN REVISIÓN` **sin un solo comentario**.
Ninguna de las dos se tocó.

### ⭐⭐ RONDA 8 — la historia volvió, y las dos correcciones eran la misma

Eli sobre la ronda 7: **«aumenta más el zoom de los animadores porque no se ve
mucho»** y **«puedes llegar un poco más abajo siguiendo la línea porque se ve un
lado azul extraño. Que debería ser igual a los otros espacios azulitos que se ven.
No tanto como ese.»** · «lo demás cambios okey».

⛔ **La costura era un defecto de verdad y tenía un número.** La junta entre el
cuadro de los animadores y el de la mesa iba en **43,5 px @1080** cuando todas las
demás del mosaico van en **5**. Sale del `+ 38` del polígono de `mesa-azul`, que
baja su borde superior sin que nadie bajara el del cuadro de arriba: 5 + 38 = 43.

Se arregló **bajando el cuadro de arriba** —lo que ella pidió, y además deja
intacto el encuadre ya aprobado de la mesa—, con el borde inferior **paralelo al
techo de `mesa-azul` y 5 px por encima**. Lleva un escalón a propósito en x=425,
donde quien manda pasa a ser `colaborador`; cae justo detrás de la junta vertical,
o sea no se ve. Verificado: 4,8 · 4,8 · 4,8 · 5,3 px a lo largo de la diagonal.

⭐ **Y las dos correcciones se resolvieron con el mismo movimiento:** al bajar la
costura el cuadro **creció de 305 a 343 px de alto**, y eso es lo que permitió
subir el zoom de 1,45× a **2,0×** sin cortar a los animadores más arriba. Quedan en
**736 px, el 52 %** del ancho del cuadro (venían del 26 % en la ronda 6), vistos de
la cabeza a medio muslo, con la manta y la faja enteras.

> ⭐⭐ **Regla para cualquier mosaico:** las costuras se **miden**, no se miran. Un
> filete que se sale del patrón se lee como error de montaje aunque nadie sepa
> decir por qué, y un polígono con desplazamiento propio rompe la promesa de
> `FILETE = 5` en silencio.

**Entregada.** Re-subida al mismo archivo del Drive: el enlace sigue igual.

### ⭐⭐ El hallazgo de la sesión: la foto de una pieza con tinta blanca se ELIGE MIDIENDO

El pedido decía «habitación de categoría superior» y las habitaciones bonitas del
banco **no aguantan la diagramación**. El velo del feed es convexo —casi no pesa
hasta pasada la mitad— y el titular blanco cae justo ahí: `HDT_66` (la cama king,
la más de catálogo) deja el titular en **2,1:1** contra una vara de 3:1, y `HDT_65`
en 2,8:1. Se midieron **once** habitaciones contra el velo real y sólo una sirve.

⭐ Y la que sirve es también la que mejor contesta el pedido: **`HDT_68`, la suite**,
la única toma donde se ven los dos ambientes a la vez. Porque en este hotel lo que
separa una categoría superior de una estándar es **el estar**, no la cama. Las otras
dos que pasaban la medición —`HDT_57` y `HDT_59`— son de **dos camas**, o sea
categoría estándar: justo lo contrario.

⛔ **La salida no fue cargar el velo ni pasar el titular a azul.** Lo primero tapa la
foto, que es el argumento de la pieza; lo segundo cambia un look ya aprobado por un
pedido que sólo hablaba de la foto.

### ⛔⛔ Y se encontró un defecto de medición que llevaba desde la ronda 1

`scripts/dt-ft-honors-foto.py` medía con la rampa **cóncava de historia** (pie 0,58)
y esta pieza usa la **convexa de feed** (pie 0,50) desde la ronda 2. Con la foto
oscura del lobby la diferencia no se notaba; con una habitación clara daba el
titular en **6,3:1 cuando de verdad estaba en 2,8:1** — o sea aprobaba piezas que
`dt-qa.py` rechaza. Corregido.

### Lo que cambió, medido

| Pieza | Elemento | Antes | Después |
|---|---|---|---|
| ST 18-09 | bajada en versales | «DOUBLETREE.» · 340 px | **«DOUBLETREE» · 335 px** |
| ST 18-09 | cuadro del escenario | pareja 368 px = 26 % del cuadro · cuadro 305 de alto | **zoom 2,0× → 736 px = 52 % · cuadro 343** |
| ST 18-09 | costura con el cuadro de abajo | **43,5 px** | **5 px, como el resto del mosaico** |
| Post 23-09 | foto de fondo | `HDT_36` lobby | **`HDT_68` suite, fx 0,80** |
| Post 23-09 | logotipo DT | 2,42:1 *(desviación declarada)* | **4,32:1** |
| Post 23-09 | logotipo Hilton Honors | 6,70:1 | **8,60:1** |
| Post 23-09 | titular · panel · íconos · rótulos · regla · llamado | — | **sin tocar** |

Las dos pasan `dt-qa.py` **limpias**. `npm run typecheck` limpio.

### Qué quedó hecho

1. **`recorta()` del collage acepta `zoom`** — escala uniforme y recorta, no
   deforma. Al subirlo hay que recalcular el `foco`, y queda escrito cómo.
2. **`dt-ft-honors-foto.py` es por variantes**: `suite` (la que va), `estar68` (la
   alternativa medida), `king` · `bienvenida` · `estar` (descartadas, con su
   número) y `lobby` (reconstruye la entrega vieja byte a byte).
3. **La página de la ronda** — `out/hilton/dt/DT S3-S4 - ronda 8.html`, con el
   antes, el después, los animadores **ronda a ronda**, la costura de cerca y las
   alternativas de foto. Un solo archivo, imágenes embebidas.
   ⭐ Eli no podía abrirla desde la terminal, así que se **publicó como página web**:
   https://claude.ai/artifact/4L1rHEMfybm5w6ehMpqsPN — se republica al mismo enlace
   cada ronda. Ojo: **Drive no renderiza `.html`**, los ofrece para descargar.
4. Las rondas anteriores archivadas en `_rondas/` de cada pieza.

### ✅ LAS DOS ENTREGADAS — y el tope del token, medido de verdad

- **ST 18-09** → `S3 HILTON SEP 2026 › DT`, reemplazada **en el mismo archivo**
  (`1SCxxWbpvvUMULbBnDnOYiPOQ0WQx-cic`): **el enlace no cambió**, quien ya lo tenía
  ve la ronda 8. 12 229 310 B en disco y en Drive, idénticos.
- **Post n°1 S4 DT** → `S4 HILTON SEP 2026 › DT`, archivo **nuevo**
  (`1tF4nWGEJTvCr3bwZIXow6kKI30zACYkW`, 10 083 019 B). El de Eli quedó renombrado a
  **`Post n°1 S4 DT - r6 SUPERADA (lobby).png`** y sigue en la carpeta.

#### ⭐⭐ EL TOPE DEL TOKEN NO ES «no puede escribir en la carpeta». ES OTRO, Y MÁS CHICO

Esto corrige lo que se venía diciendo desde Between el 14-09. Sondeado hoy contra
`S4 HILTON SEP 2026 › DT`, que creó Eli:

| Operación | Resultado |
|---|---|
| `files.get` / `files.update` sobre un archivo de Eli | **404** — la app no lo ve |
| **`files.create` con `parents` = su carpeta** | **✅ FUNCIONA** |

O sea: con scope `drive.file` **sí se puede dejar una entrega dentro de la carpeta
de otra persona**; lo único que no se puede es **pisar un archivo que subió ella**.
Toda la ronda anterior se dio por bloqueada de más.

**El procedimiento que queda**, y es el mismo de Between:

1. Renombrar el archivo viejo a `… - rN SUPERADA (qué era).png` — eso **sí** lo
   hace el conector MCP de Drive, que corre como Eli (`update_file`, sólo título y
   carpeta, no contenido).
2. Subir el nuevo con `scripts/drive-subir.py --carpeta <ID>`, con el nombre bueno.

⚠️ **El costo, que hay que decir:** el `fileId` **cambia**, así que quien tuviera
el enlace viejo cae en el archivo SUPERADA. Por eso el renombre no es opcional: sin
él quedan dos archivos con el mismo nombre y se aprueba el corte equivocado. Cuando
la pieza la subió el estudio —como la ST— se reemplaza en sitio y el enlace se
conserva; ésa sigue siendo la vía buena.

> ⚠️ **Y por eso sigue abierta la decisión de fondo:** o las entregas las sube
> SIEMPRE el script del estudio, o el token pasa a scope `drive` completo. Mientras
> no se decida, cada pieza que Eli suba a mano obliga a cambiar el enlace la próxima
> vez que se corrija.

### ⛔⛔ Y hay que decidir qué pasa con el editable

Desde la ronda 5 la entrega del post salía del `.ai` de Eli. **Esta ronda se rindió
desde el repo** —`DtFtHonors.tsx` reproduce la pieza dentro de ±2 px y pasa el mismo
QA—, porque lo que cambia es la foto de fondo. O sea que
`editable/Post n°1 S4 DT - EDITABLE.ai` **sigue con el lobby**. Si la próxima ronda
se trabaja ahí, primero hay que cambiarle la foto: está lista y recortada a
2250×2813 en `public/assets/hilton/dt/ft-honors-habitacion.jpg`.

### Qué sigue

**De estas dos piezas, nada:** las dos están entregadas, con QA limpio y subidas.
Lo siguiente de DT en el FEED es **columna M, 28-09, un CARRUSEL** («Tu día en
DoubleTree by Hilton Santiago-Vitacura», tipo timeline, sin modelos) — pero sigue
en **`REVISAR CONTENIDO`** y **no se diseña hasta que pase a `OK PARA DISEÑO`**.
Antes de tocarlo: correr `/al-dia` y leer la celda viva, no la instantánea.

### Abierto

- **La ST animada del 21-09 la hace Eli.** Lo que pidió el cliente, para que no se
  pierda: sacar **dos fotos** (la del trago en la barra y la de la pareja en la mesa
  del café) y dejar las otras; cambiar el texto de la pantalla 1 a **«Habitación
  para dos / Botella de espumante»**; que la foto de la mujer con la taza caiga
  **cuando se habla del desayuno buffet**; y «que las transiciones no sean con ese
  rebote, busquemos algo más sutil y ahora que hay menos fotos, que no sean tan
  rápidas». El video vive en `ST n°1 S4 DT.mp4` (9,64 s · 1080×1920 · 25 fps),
  hecho en Adobe, **no en este repo**.
  ⭐ Dato útil si alguna vez hay que bajarlo: la copia de `S4 › DT › STS` **no está
  compartida** y devuelve la página de login; la copia **pública** es
  `1xvTkYaRmUmdGX6nS-fm7jOl0C9VQAs0w`. Es otra vez la regla de buscar las copias
  por título antes de dar algo por bloqueado.
- **El editable, con la foto vieja** (arriba).
- Sigue sin respuesta lo del 15-09: **la Opinión Booking del 14-09 quedó en `EN
  REVISIÓN` con la fecha pasada** — hay que preguntarle a Eli si se publicó.

## 2026-09-16 — Arranque de la máquina · hallazgo de MATERIAL (no es sesión de diseño)

**Qué se hizo:** verificación completa del estudio en el Windows de Eli con
`/arranque`. No se diseñó ni se entregó nada. El verificador de material levantó
36 archivos «rotos» en `raw/` y **la mayoría no lo están**.

**Dónde quedó:** las 25 fotos de `raw/hilton/dt/fiestas-patrias-18/` y la
`ref-eli-r27/foto-base.jpg` de Between son **HEIC de iPhone con extensión
`.jpg`** — la foto está buena, miente el nombre. **No se rebajan del Drive: ya
están en disco.** Chrome no lee HEIC, así que antes de usarlas hay que
convertirlas (receta en la memoria `heic-no-es-archivo-roto`; `pillow-heif` ya
está instalado en esta máquina).

Sí están rotos de verdad: `raw/hilton/dt/identidad/DTbH-Brand-Identity-Guidelines-EN.pdf`
y los cuatro `*.DESCARGA-FALLIDA.html` de `ref-s4/` y `sesion-real/banco-maestro/`
— son la página de login de Google guardada con otra extensión.

**Qué sigue:** nada bloqueante. Cuando toque Fiestas Patrias de DT, convertir las
25 fotos primero. Si se necesita el manual de identidad de DoubleTree, rebajarlo.

**Abierto:** nada.

## 2026-09-16 — DT · ronda 6 del estático Honors, y el editable pasó a mandar

**Marca: DT.** Sesión de diseño. Pieza: `Post n°1 S4 DT` (FEED col K, 23-09).

**Qué pidió la grilla**, literal, de una superior:

> «donde dice canje podría ser así porfis — Canje de / noches gratis»
> «y el recuadro en cada item sin tanto aire, se ve como muy pelaitoo»
> «solo eso baby, lo demás lo veo todo oki en grillass»

**Quién lo hizo.** Eli, en su editable, antes de pasar el encargo. El `.ai` del
16-09 a las 09:32 ya traía los dos cambios. Acá se verificó, se exportó la
entrega y se puso el repo al día.

**⛔⛔ LO QUE HAY QUE APRENDER DE ESTE DÍA: la pieza ya no sale de Remotion.**
Desde la ronda 5 (15-09, tarde) la entrega se exporta del
`out/hilton/dt/ft-honors/editable/Post n°1 S4 DT - EDITABLE.ai`. Se rindió la
composición sin mirar eso y **se sobrescribió el PNG entregado**. Se recuperó
byte a byte desde `editable/_verificacion/estado-actual.png` (mismo md5) y no se
perdió nada, pero la regla queda escrita: **antes de rendir una pieza de DT, mirar
si hay editable y si es más nuevo que el último render**. El QA fue lo que lo
delató —tres «SUSTITUCIÓN DE FUENTE» en textos que nadie había tocado—, así que
la compuerta hizo su trabajo.

**Lo que cambió**, medido sobre los dos PNG de entrega, @1080:

| | Ronda 5 | Ronda 6 |
|---|---|---|
| «Canje» | «Canje de noches» / «gratis» | **«Canje de» / «noches gratis»** |
| Caja | 880 × 306 en y 812 | **764 × 260 en y 842** |
| Celda · tinta | 153 · 40,1 % | **130 · 47,4 %** |
| Logo Hilton Honors | 64 de alto, y 1156 | **81,6 de alto, y 1136** |
| Titular | — | mismo cuerpo, **bajó 12 px** en bloque |
| Regla del pie, foto, logo DT, llamado | — | **sin cambio** (diferencia máxima 0) |

**⭐ El hallazgo que vale para la cuenta: el ancho nuevo de la caja es la medida
del titular.** 764 no es un número redondo — es la medida a la que Eli justificó
las tres líneas en la ronda 5. Apretó el cuadro hasta la columna del titular, y
por eso ahora titular y caja cierran en la misma vertical. **La regla del pie NO
la siguió**: se quedó en 880, así que en el código dejó de colgar de la caja.

**⭐⭐ Y «pelaitoo» tenía un número detrás.** Se midió `DT FT S3` —única pieza
aprobada con la misma estructura de ícono · regla vertical · rótulo de dos líneas
en celda cerrada—: su celda mide 110,4 y su tinta 54,7, o sea **49,5 %**. Esta
pieza iba en **40,1 %** y quedó en **47,4 %**. El aire sobraba en la CAJA, no en
el contenido: no se tocó el cuerpo del rótulo (29), ni los íconos, ni los aires de
celda, que son gramática de Eli ya medida.

**Qué quedó hecho.**

1. **La entrega**, exportada del `.ai` con `scripts/ai-puente.py` (COM a
   Illustrator, que estaba arriba y sin documentos). ⚠️ **La escala es 208,37 %,
   no 208,33 %**: con 208,33 salen 2250×**2812** y el máster de la cuenta es 2813.
   Fuentes resueltas (ninguna sustituida) y rasterizado en 300 ppi con suavizado.
2. **QA limpio** — `python scripts/dt-qa.py "out/hilton/dt/ft-honors/Post n°1 S4 DT.png"`.
   Las bandas de `scripts/dt-qa.py` se re-midieron enteras sobre esta entrega.
3. **La composición sincronizada** con el editable: `DtFtHonors.tsx` rinde la
   misma pieza dentro de **±2 px** en todos sus elementos y pasa el mismo QA con
   los mismos números. Incluye el titular justificado de la ronda 5, reconstruido
   con cuerpo y tracking por línea. ⚠️ El tracking que predice el cálculo sobre el
   `.ttf` NO sirve: **Chrome compone esos glifos más angostos que PIL** y la medida
   quedaba hasta 19 px corta. Los valores buenos salen de rendir y medir.
4. **Página de la ronda** — `out/hilton/dt/ft-honors/Post n°1 S4 DT - ronda 6.html`,
   con el antes, el después, el recuadro de cerca y los números. La de la ronda 4
   (`- revision.html`) se dejó intacta.
5. La ronda 5 quedó archivada en `_rondas/`.

**⚠️ Lo único que el código no reproduce como sistema:** en el editable la
**columna izquierda** de la caja va 10,6 px más a la derecha que la derecha —el
grupo entero, con los anchos idénticos a 0,5 px—, o sea Eli lo arrastró a mano. Se
reprodujo como `EMPUJON_COL_IZQ`, **aparte de la gramática**, para que nadie lo
confunda con una regla. Si se le fue la mano, se borra esa constante y listo.

**Entregado.** **Eli subió ella misma el PNG al Drive** el 16-09, reemplazando el
archivo de `S4 › DT`, así que **el enlace no cambió**: quien ya lo tenía ve la
versión nueva. Desde esta sesión no se tocó nada del Drive.

**⭐ Y el editable ahora VIAJA EN EL REPO.** Decisión de Eli del 16-09: se abrió
excepción en `.gitignore` para `out/hilton/dt/ft-honors/editable/*.ai`. Como la
entrega se exporta de ese archivo, sin él quien clonara tenía la composición
sincronizada pero no la fuente de verdad. ⚠️ Son ~34 MB de binario que git no
diferencia: **cada guardado suma otros 34 MB al historial**. Si se vuelve pesado,
la salida es versionar sólo el `.svg` intermedio (5,4 MB y diferenciable) — pero
ése NO trae los ajustes hechos a mano dentro de Illustrator, que es justo lo que
cambió en esta ronda.

**Qué sigue.** De esta pieza, **nada**: entregada, subida y con el enlace
conservado. Lo siguiente de DT en el FEED es **columna M, 28-09, un CARRUSEL**
(«Tu día en DoubleTree by Hilton Santiago-Vitacura», tipo timeline, sin modelos)
— pero está en **`REVISAR CONTENIDO`**, o sea el cliente todavía lo está viendo y
**no se diseña hasta que pase a `OK PARA DISEÑO`**. Antes de tocarlo: correr
`/al-dia` y volver a leer la celda viva, no la instantánea (el 15-09 la celda
cambió de estado entre dos lecturas del mismo día).

**Abierto.**

- **El empujón de 10,6 px de la columna izquierda** — hay que preguntarle a Eli si
  fue a propósito o se le arrastró el grupo. Si fue sin querer, se borra
  `EMPUJON_COL_IZQ` de `DtFtHonors.tsx` y la caja queda pareja.
- **El peso del `.ai` en el historial.** Entró hoy por decisión de Eli. Hay que
  mirarlo en unos meses: cada guardado suma ~34 MB y no se puede diferenciar.
- **Hilton no tiene `reglas.yaml`.** Su compuerta ejecutable es `scripts/dt-qa.py`,
  que sí está al día con esta geometría. Queda anotado porque el resto de las
  marcas del estudio se revisan con `qa/motor.py --marca <marca>` y DT no entra
  por ahí.

## 2026-09-15 (apertura) — DT · el `/al-dia` que destrabó el día, y DOS HILOS OPEN que sobraron

**Marca: DT.** **No es sesión de diseño**: es la apertura (`/abrir doubletree`).
El trabajo del día está en las entradas de más abajo —la ST del 18-09 y el
estático de Honors, las dos aprobadas y subidas—. Esto anota **lo único que el
día no dejó escrito**.

**Qué se hizo.** Diff de la grilla viva (modificada hoy 12:24Z) contra la
instantánea del 10-09. Encontró las dos tareas que después se produjeron, y de
paso que **los dos bloqueantes que venían del 10-09 ya no existían**:

- **La bandera de Panamá** (hilo `AAACGzJtEYc`, `FEED!I14`) quedó **RESUELTA**.
- **La carpeta de referencias de la reseña** (`1Dlki995RRdwueFGlZOkF9rybf7maMJ5u`)
  **ya no está vacía**: 5 PNG, entre ellos `imagen_2026-08-14_112424991.png`, el
  que propuso Carlos. ⚠️ Se ve por `embeddedfolderview`, **no** por `parentId`
  —que sigue devolviendo vacío—, o sea el bloqueo era del método de lectura y no
  del material (memoria `agotar-material-antes-de-bloquear`).
- **STORIES col H (18-09)** pasó a `OK PARA DISEÑO` y Scarlette dejó el material
  ayer 21:18Z: `1_LUmZ26C9FtGl9zLgE_IxRoN7-0so91w`, **179 archivos** del evento
  interno de Fiestas Patrias del lunes en Piso18. ⚠️ Buena parte son **`.HEIC`, que
  Chrome no carga** — el mismo modo de falla silencioso del TIFF del lobby y de
  Brushwell.
- **FEED col K (23-09)** pasó a `APROBADO` con el comentario **sin tachar** «Les
  dejé ajustes en el brief»: cambiaron los rótulos (caja baja, «Canje de noches
  gratis», «Acumula puntos en cada estadía») y se agregó el titular «MÁS
  BENEFICIOS EN CADA ESTADÍA CON HILTON HONORS».

**Dónde quedó.** `clients/hilton/grillas/dt-septiembre-2026.md` (la instantánea
nueva, base del próximo diff) y `clients/_estado-sync.json`. Los dos entraron
dentro de los commits del día — `c87c29e`, `856753d` y `3fe2ac4` —, o sea **están
respaldados**, sólo que no en un commit propio.

**Qué sigue.** Nada de esta sesión: el día ya se cerró en las entradas de abajo.

**Abierto — ⛔ dos hilos nativos que siguen `OPEN` y ya no corresponden.** Nadie
los va a cerrar si no quedan anotados, y un hilo abierto se lee como ronda
pendiente:

- `AAACB_tY1w4` (`FEED!K10`, Scarlette, 13-08) — pedía **grabar el reel** de
  Hilton Honors coordinando con Sebastián Serrano. **Obsoleto**: esa pieza pasó a
  estático y hoy quedó aprobada.
- `AAACFVjwFEY` (`STORIES!H15`, Scarlette, ayer 21:18Z) — es el que entregó el
  material del 18-09. **Ya se usó y la pieza está aprobada y subida**, así que se
  puede cerrar.

⚠️ Y sigue sin respuesta, por si se pierde entre las entradas del día: **la
Opinión Booking del 14-09 (`FEED` col I) quedó en `EN REVISIÓN` con la fecha ya
pasada** — hay que preguntarle a Eli si se publicó.

---

# HILTON — bitácora

> ⚠️ **Este archivo lo comparten las 4 marcas del complejo (DT · QB · Between ·
> Piso18) y lo escriben varias sesiones el mismo día.** Cada entrada dice de qué
> marca es. Si vas a retomar una, busca su marca, no la fecha.

---

## 2026-09-15 (cierre) — PISO18 · **S5 APROBADA**

**Marca: PISO18.** Eli aprobó las **5 piezas** tras tres rondas. Con esto
**septiembre de Piso18 queda completo**: la S4 se aprobó más temprano el mismo día
y la S5 cierra acá.

| Pieza | Archivo en Drive | Tamaño |
|---|---|---|
| Historia 28-09 «Planifica tu evento de fin de año» | `STS › ST N°1 S5.png` | 2250 × 4000 |
| Carrusel 29-09 «Cumpleaños en Piso18» | `C1 S5 PISO18 › C1 S5 N°1..3.png` | 2250 × 2813 |
| Historia 30-09 «Visita guiada virtual» | `STS › ST N°2 S5.png` | 2250 × 4000 |

En `S5 HILTON SEP 2026 › PISO18`. **Los cinco `fileId` no cambiaron en ninguna de
las tres rondas** —`files().update`—, así que cualquier enlace que el cliente ya
tuviera muestra la versión aprobada.

**Las tres rondas, en una línea cada una:**

1. Las 3 piezas de cero. Torta y brindis producidos editando foto real, porque el
   banco no los tiene. Fondo oscuro plano ⇒ bloqueante de QA ⇒ entra `GranoFondo`.
2. Portada del carrusel rehecha (se parecía a la del 15-09 y era muy cerrada) y la
   ST del 30-09 centrada: los teléfonos iban 131 px a la izquierda **y** el
   tracking descentraba las líneas.
3. La torta pasa a cuatro pisos, entran velas y globos porque la escena leía
   matrimonio, y **se borra el logotipo de la portada** por repetitivo.

**Lo reutilizable de toda la jornada está en `clients/hilton/CLAUDE.md` § LA S5**,
y lo que NO es de Piso18 es esto:

- ⭐⭐⭐ **El `letter-spacing` descentra una línea centrada.** CSS lo pone también
  después de la última letra, así que sobra aire a la derecha y `text-align:
  center` lo reparte mal. Se compensa con un `text-indent` del mismo valor. **Vale
  para todas las marcas del estudio.**
- ⭐⭐ **Un fondo oscuro PLANO dispara el bloqueante «foto estirada para llenar el
  formato»** del motor de QA, porque mide rachas de filas idénticas. No es un falso
  positivo que haya que calibrar: se le da grano al fondo y además se ve mejor.
- ⭐ **Una portada de carrusel se mide contra la portada anterior de la misma
  vertical**, no sola.

**QUÉ SIGUE — la próxima tarea concreta, la que haría uno mismo mañana:**

> **Abrir octubre de Piso18.** La grilla ya está bajada en
> `clients/hilton/grillas/p18-octubre-2026.md`. El orden es: correr `/al-dia` para
> ver si cambió, leer la primera columna con estado `OK PARA DISEÑAR`, y **antes de
> producir nada, verificar si pide torta, brindis o fiesta** — si los pide, hay que
> pedirle la sesión a Eli, porque el banco no los tiene (está medido sobre 386
> fotos). El aparato está completo: kit, 3 composiciones, QA y script de subida.

**Pendiente de la cuenta, no de la S5** (para quien retome PISO18 en octubre):

- La **ST del 21-09** sigue sin brief de diseño; hay que pedírselo a contenido.
- Falta **`Edwardian Script ITC`**, la cuarta voz del sistema.
- Sigue sin diagnosticar el **«quedó algo extraño detrás del logo»** del cliente.
- ⛔ **El banco no tiene torta de cumpleaños ni brindis.** Si octubre los vuelve a
  pedir, hay que pedirle la sesión a Eli antes de producir nada.
- La **grilla de octubre** ya está en `clients/hilton/grillas/p18-octubre-2026.md`.

---

## 2026-09-15 (noche) — PISO18 · S5 RONDA 3 · **la S5 queda cerrada**

**Marca: PISO18.** Última ronda. Eli dio por buenas las otras cuatro piezas —*«las
demás de la S5 okey»*— y corrigió sólo **la portada del carrusel**.

**Qué dijo:** *«La portada del carrusel, la torta que se vea más grande y alta, no
se destaca en nada. Y añade detalles de cumpleaños, se ve muy de matrimonio aún.
Y bórrale el logo, muy repetitivo.»*

**Qué se hizo, en la misma escena (`piso_18-154`) y con el mismo archivo de Drive:**

1. **La torta pasó de dos pisos a cuatro.** Medido aislando el glaseado en la
   columna central: el cuerpo pasó de ocupar el **15 % del alto al 52 %**. El
   defecto no era el tamaño absoluto sino que su cima quedaba **por debajo de la
   línea del follaje colgante** y se perdía contra él.
2. **Entraron velas de cumpleaños encendidas y globos.** La escena de esta marca
   —jardín colgante, mantelería, copones dorados— **lee matrimonio por defecto**, y
   un topper de «50 años» no alcanza a desempatarla. Los globos no se inventaron:
   están en el brief del propio carrusel, en la slide 2.
3. **Fuera el logotipo** de la portada, y con él el velo superior que existía sólo
   para sostenerlo.

**Las tres lecciones, que valen más allá de esta pieza:**

- ⭐ **El protagonista de una portada tiene que cortar contra el fondo**, no quedar
  dentro de la masa visual de otro elemento. Se comprueba mirando la silueta, y el
  tamaño se mide, no se estima.
- ⭐⭐ **La escena de Piso18 lee «matrimonio» por defecto.** Para que una pieza diga
  cumpleaños hacen falta elementos que en un matrimonio no existen: velas
  encendidas y globos. Y su color se toma de la foto, no se elige aparte.
- ⛔ **La portada del carrusel no siempre lleva logotipo.** Corrige la gramática
  escrita y la instrucción del 22-09. Es decisión de **ritmo del feed** y se
  consulta; no se generaliza (en `C2 S1 n°1` el logotipo va).

⛔ Y el recordatorio de siempre con los prompts: **no escribir «serpentinas»** —en
Between devolvió serpientes—. Se pidieron «globos» y «velas», y se prohibió
explícitamente confeti y guirnaldas de papel.

**Estado: la S5 de Piso18 está entregada y sin comentarios abiertos.** Los cinco
`fileId` de Drive siguen siendo los mismos desde la ronda 1.

**Lo que sigue pendiente de la CUENTA (no de la S5):** la ST del 21-09 sigue sin
brief de diseño; falta `Edwardian Script ITC`; y sigue sin diagnosticar el «quedó
algo extraño detrás del logo» del cliente.

---

## 2026-09-15 (noche) — PISO18 · S5 RONDA 2, las correcciones de Eli aplicadas

**Marca: PISO18.** Continúa la entrada de más abajo y **reemplaza su entrega**: los
cinco archivos de Drive son los mismos, con el contenido actualizado.

**Qué dijo Eli:** *«La historia okey, pero el carrusel pasa que se ve muy igual al
carrusel portada anterior y es muy cerca, puedes generar otra torta o usar otro
fondo con torta que diga 50 años, pero con mejores colores. Primera ST okey,
segunda necesito que centres el celular y los textos.»*

**Qué se hizo:**

1. **Portada del carrusel, rehecha entera.** Escena nueva —de la mesa oscura con
   arreglo seco (`piso_18-141`) a la mesa larga bajo el jardín colgante
   (`piso_18-154`)—, plano general en vez de detalle, y una torta de dos pisos con
   topper dorado que dice **`50 años`**, en rosa palo con franja frambuesa y las
   mismas flores que ya están en la foto.
2. **ST del 30-09 centrada.** Eran **dos** causas: los teléfonos estaban 131 px
   corridos a la izquierda (dos coordenadas a mano que nadie sumó) y el tracking
   descentraba las líneas con versales espaciadas.
3. **ST del 28-09:** no se tocó, quedó aprobada.

**Las dos lecciones que quedan, y ninguna es sólo de Piso18:**

- ⛔ **Una portada de carrusel se mide contra la portada ANTERIOR de la misma
  vertical, no sola.** La de la ronda 1 era correcta pieza por pieza y estaba mala
  en el conjunto: otra torta en plano cerrado catorce días después. Mismo error
  que la torta de Between sobre mármol.
- ⭐⭐⭐ **El `letter-spacing` descentra una línea centrada**, porque CSS lo pone
  también después de la última letra. Se compensa con un `text-indent` del mismo
  valor. Vale para **todas las marcas** del estudio.

**Y cómo se comprueba un centrado:** midiendo el bbox de tinta por bandas contra
el eje del lienzo, no mirando. En la pieza corregida el desvío máximo es de 5,5 px
sobre 2250 (0,24 %).

**Sigue abierto** lo mismo que la ronda 1: las pestañas del planner son criterio
propio, la bajada del 30-09 lleva la preposición repuesta, la torta y el brindis
son producidos, y falta `Edwardian Script ITC`.

---

## 2026-09-15 (noche) — PISO18 · S5 DE SEPTIEMBRE, ENTREGADA (ronda 1)

**Marca: PISO18.** Sesión aparte de la S4 del mismo día, que ya está aprobada.

**Qué se entregó:** las **3 piezas de la S5**, o sea todo lo que quedaba pendiente
de la cuenta en septiembre.

| Pieza | Archivo | Dónde |
|---|---|---|
| Historia 28-09 «Planifica tu evento de fin de año» | `ST N°1 S5.png` (2250×4000) | `S5 HILTON SEP 2026 › PISO18 › STS` |
| Carrusel 29-09 «Cumpleaños en Piso18», 3 slides | `C1 S5 N°1..3.png` (2250×2813) | `… › C1 S5 PISO18` |
| Historia 30-09 «Visita guiada virtual» | `ST N°2 S5.png` (2250×4000) | `… › STS` |

La carpeta de destino **la creó Eli** el 15-09 a las 19:49Z, el mismo minuto en que
subió las dos referencias a `REF`. Revisión visual en
`out/piso18/s5/revision/index.html` y como artefacto publicado.

**Las dos referencias que dejó** (`REF`, `1Ten76mKoEQWF-dEg4vsLcybk7id96Mg9`) son
una **agenda de anillas** con foto sujeta por clip y pestañas de índice (para el
28-09) y **dos teléfonos escalonados** sobre fondo desaturado (para el 30-09).
Las dos se tradujeron, no se calcaron. Copiadas en `raw/hilton/piso18/ref-s5/`.

**Lo más reutilizable de la jornada, en cuatro líneas:**

1. ⛔ **El banco no tiene torta ni brindis** — medido sobre 386 fotos (110 deco
   2024 + 85 ago 2023 + las **191 de `3-Finales 2026`**, bajadas enteras acá por
   primera vez). Ni siquiera la torta del carrusel publicado el 15-09. Las dos
   ausencias se produjeron **editando foto real** con Nano Banana Pro, como en la
   S4. Si vuelve a hacer falta, **hay que pedirle la sesión a Eli**.
2. ⭐⭐⭐ **Un fondo oscuro PLANO es bloqueante en el QA** («foto estirada para
   llenar el formato»: 18 % de filas idénticas en la del 28-09). No se aflojó el
   tope — se le dio **grano** al fondo, que además se ve mejor. Entra `GranoFondo`
   al kit y **todo fondo oscuro de esta marca lo lleva**.
3. ⭐ **La historia con sticker de enlace NO lleva botón.** Es la excepción que el
   propio cliente dictó el 18-09 para no redundar. Si el sticker es de cotización,
   el botón sí va.
4. ⚠️ **El feed se rinde a `--scale=2.0837`, no a 2.0833:** con 2,0833 el alto da
   2812 y el máster aprobado de la cuenta es **2813**.

**Cómo se rehace:**

```bash
npx remotion still src/P18Entry.tsx P18-ST-Planifica out/piso18/s5/ST-N1-S5.png --scale=2.0833
npx remotion still src/P18Entry.tsx P18-C1-Cumple-S1 out/piso18/s5/C1-S5-N1.png --scale=2.0837
python qa/motor.py --marca piso18 --textos clients/piso18/entregas/textos-s5.json out/piso18/s5/*.png
python scripts/p18-s5-subir.py --dry-run     # y sin --dry-run para subir
```

**Lo que queda abierto — hay que preguntárselo a Eli:**

- **Las pestañas del planner** dicen las cinco verticales (matrimonio, cumpleaños,
  corporativo, bautizo, fin de año). Es criterio propio apoyado en su orden de
  «mostrar más de lo demás» y en que bautizo tiene 0 piezas en todo septiembre.
  Si no le gusta, se cambia en un minuto.
- **La bajada del 30-09.** El cliente la tipeó «recorre cada rincón Piso18 desde
  donde estés» y en la pieza dice «Recorre cada rincón **de** Piso18 desde donde
  estés.» — se le repuso la preposición y el punto. Está declarado en la entrega.
- **La torta y el brindis son PRODUCIDOS** y van marcados como tales en la página
  de revisión. Si prefiere foto real, tiene que subir la sesión del cumpleaños.
- **El solapamiento del 29-09 con el carrusel de cumpleaños del 15-09**: los mismos
  cuatro beneficios. Es de contenido, se informó y no se corrigió.
- Sigue faltando **`Edwardian Script ITC`**, la cuarta voz del sistema. La historia
  del 30-09 la pedía por referencia y va en IvyPresto mientras tanto.
- Sigue sin diagnosticar el **«quedó algo extraño detrás del logo»** del cliente.

---

## 2026-09-15 (tarde) — DT · RONDA 5 DEL ESTÁTICO DE HONORS, HECHA EN ILLUSTRATOR

**Marca: DT.** Continúa el cierre de DT que está más abajo; **reemplaza su entrega**.

**Qué se hizo:** se sacó el **editable** de la pieza para que Eli la trabajara en
su Illustrator, ella **rehizo el titular** y la dio por buena. El criterio nuevo
—*el titular se justifica a una medida común escalando cada línea*— quedó escrito
en `clients/hilton/CLAUDE.md` § **RONDA 5**, que es lo que hay que leer.

Cuerpos 68/68/68 → **92,3 / 87,5 / 73,6**; anchos de tinta **764,2 / 764,1 /
766,6** (2,4 px entre las tres); versal 47,6 → 65,3. El llamado del pie quedó
centrado exacto en 540 con tracking 10 (los rótulos siguen en 12).

**Dónde quedó:** `Post n°1 S4 DT.png` **reemplazado en el MISMO archivo de Drive**
— [`132pCMwB…`](https://drive.google.com/file/d/132pCMwB46c0nDz7DiyECSrLNFyShkFhv/view),
**el enlace no cambió**. Verificado por `fileSize`: 8 440 764 bytes a los dos
lados. La ronda 4 quedó archivada en `out/hilton/dt/ft-honors/_rondas/`.

**Cómo se rehace:**

```bash
python scripts/dt-editable-svg.py --verificar   # el editable, con los valores de la ronda 5
python scripts/ai-puente.py --abrir "out/hilton/dt/ft-honors/editable/Post n°1 S4 DT - EDITABLE.ai"
python scripts/dt-qa.py "out/hilton/dt/ft-honors/*.png"
```

⭐ **Hay puente con Illustrator**: `scripts/ai-puente.py` habla por COM con el
Illustrator abierto y corre ExtendScript adentro (leer el documento vivo,
medirlo, modificarlo, exportar). Así se midieron estos números — no se estimó
ninguno.

**Qué sigue:** de esta pieza, nada — está entregada y aprobada. Lo siguiente de
DT en la grilla sigue siendo lo que ya decía el cierre de la mañana: **FEED col I
(14-09)**, que quedó en `EN REVISIÓN` con la fecha pasada (hay que preguntarle a
Eli si se publicó), y **STORIES col H (18-09)**, que pasó a `EN EDICIÓN` después
de subirse. Antes de tocar cualquiera de las dos, correr `/al-dia`.

⭐ Y hay una decisión de método que conviene tomar con Eli: **ahora se le puede
entregar el editable de cualquier pieza** y trabajar con ella dentro de su
Illustrator. Si eso va a ser lo normal en DT, la pregunta es si las piezas se
siguen armando en Remotion y el `.ai` es sólo la última milla, o si el `.ai` pasa
a ser la fuente. Hoy quedó a medio camino y por eso el `.tsx` está desfasado.

**Abierto / ojo con esto:**

- ⚠️ **`src/compositions/hilton/DtFtHonors.tsx` reproduce la RONDA 4, no la 5.**
  La pieza entregada sale ahora del `.ai`. Quien necesite rehacerla por código
  tiene que trasladarle los cuerpos y las líneas base de la ronda 5 (están en el
  `TITULO` de `dt-editable-svg.py`, leídos del documento de Eli).
- ⛔⛔ **Illustrator cambia los ESPACIOS del nombre por GUIONES al exportar**
  (`Post-n°1-S4-DT.png`). El portal levanta por nombre: hay que renombrar.
- ⚠️ `dt-qa.py` deja **una falsa alarma declarada**: el rótulo «Tarifas» da
  huella 0,586 contra un señuelo de 0,488 —gana la fuente correcta— pero se
  queda a 0,002 del margen de 0,10, porque el rasterizador de Illustrator no es
  el de Chrome. **No se aflojó el margen.** Las fuentes se verificaron por COM.
- Las tres observaciones que se le hicieron a Eli y **ella no aplicó** (están
  medidas, por si vuelven): el aire titular→caja bajó a 38,2 px; el titular queda
  a 56 px de sangrado de la caja (dos márgenes casi iguales); y «CON HILTON
  HONORS» quedó la línea más chica.

---

## 2026-09-15 — PISO18 · S4 **APROBADA** (cierre)

**Marca: PISO18.** Cierra la jornada. Las **8 piezas quedaron aprobadas por Eli**
tras tres rondas. La entrada de más abajo («S4 DE SEPTIEMBRE, ENTREGADA») es la
ronda 1 y **sus fotos ya no son las vigentes** — léela sólo para el historial.

**Qué se entregó, y es lo que está publicado en Drive:**

| Pieza | Archivo | Dónde |
|---|---|---|
| Carrusel 22-09, 4 slides | `C1 S4 N°1..4.png` (2250×2813) | `S4 HILTON SEP 2026 › PISO18 › C1 S4 PISO18` |
| Historia 22-09, atardecer | `ST N°2 S4.png` (2250×4000) | `… › STS` |
| Historia animada 23-09 | `ST N°3 S4.mp4` (1080×1920 · **13,06 s**) | `… › STS` |
| Historia 25-09, encuesta | `ST N°4 S4.png` (2250×4000) | `… › STS` |
| Post de feed 25-09 | `Post S4 PISO18 25-09.png` | raíz de `PISO18` |

Los enlaces de Drive **no cambiaron entre rondas**: se reemplazó el contenido con
`files().update`, así que lo que el cliente ya tenga sigue sirviendo.

**Las tres rondas, en una línea cada una:**

1. Las 8 piezas de cero. Flores recoloreadas con IA porque el banco de entonces
   tenía un solo estilo floral.
2. La animada rehecha con la referencia como plantilla; la historia del atardecer
   pasa a ser dos fotos cosidas por la onda; textura de papel en la encuesta.
3. **Todas las flores pasan a la sesión de decoración real**; la animada se rehace
   entera con el salón vacío y empuje lateral; el titular del atardecer crece,
   sube y pierde la sombra doble.

**⭐⭐⭐ LO MÁS REUTILIZABLE DE LA JORNADA — y no es de Piso18:**

```bash
curl -sL "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t" -o archivo
```

Baja de Drive **cualquier tamaño, en paralelo y sin token**. El conector MCP corta
en 10 MB y se cae con más de 4 llamadas simultáneas; `uc?export=download` devuelve
920 KB de HTML con archivos grandes. Con el endpoint bueno entraron **110 fotos /
1,7 GB en una pasada** más cuatro videos de hasta 115 MB.
⛔ **Las rondas 1 y 2 se entregaron a medias por dar por bloqueante un tope que no
existía.** Está escrito en `clients/hilton/CLAUDE.md` § LAS RONDAS 2 Y 3, punto 0.

**Lo que cualquiera que retome PISO18 tiene que saber:**

- ⛔ **Para flores, la sesión es `Piso 18_28 ago decoración 2024`**
  (`1xS-ly0pKHUzyfhSv7PMrEkuFezymVCUk`, 110 fotos a 3840×5760, ya en
  `raw/hilton/piso18/deco-ago2024/`). Las mesas redondas con mantel blanco de la
  sesión de agosto 2023 **ya no son el montaje actual**.
- ⛔ **`IMG_4177.MOV` es el único video de montaje** de los cuatro de «Llegada de
  la primavera»; los otros tres son una presentadora a cámara. Y **se declara
  horizontal siendo vertical** (rotación por metadato).
- ⛔ **Ninguna foto se amplía**: se divide el ancho de destino por el del recorte y
  tiene que dar menos de 1.
- ⛔ La historia animada de esta marca **abre a sangre, sin zoom, con empuje
  lateral y bajo 15 s**.

**⚠️ Qué queda pendiente de la cuenta (no de la S4):**

- **La S5 de septiembre** ya está en la grilla y sin tocar: FEED col Q (29-09,
  carrusel de cumpleaños, `EN REVISIÓN`) y STORIES cols P y Q (28-09 y 30-09,
  las dos `OK PARA DISEÑAR`).
- **La ST del 21-09** sigue fuera: su celda está en APROBADO pero no trae brief de
  diseño. Hay que pedírselo a contenido.
- **Falta `Edwardian Script ITC`**, la cuarta voz del sistema. La historia del
  22-09 la pedía y va en IvyPresto itálica mientras tanto.
- Sigue sin diagnosticar el **«quedó algo extraño detrás del logo»** del cliente:
  el velo del PNG plantilla ya se descartó como causa el 15-09.

---

## 2026-09-15 — PISO18 · S4 DE SEPTIEMBRE, ENTREGADA

**Marca: PISO18.** Sesión aparte de la de DT que corre el mismo día.

**Qué se hizo:** las **8 piezas de la S4** de cero, y de paso el aparato de la
marca, que no existía. Carrusel del 22-09 (4 slides de arreglos florales, sin
texto, logo sólo en la primera), post de feed del 25-09 («Piso18 de noche») y tres
historias: 22-09 (atardecer), 23-09 (animada de montaje, 17 s) y 25-09 (encuesta
de arreglos A/B/C).

**Dónde quedó:** en `S4 HILTON SEP 2026 › PISO18`
([`1xHin8e7…`](https://drive.google.com/drive/folders/1xHin8e7Iw4gdGR5x-Z_akFCokOzy4wE3)),
con las carpetas que pidió Eli textualmente:

| Carpeta | Archivos |
|---|---|
| `C1 S4 PISO18` | `C1 S4 N°1..4.png` (2250×2813) |
| `STS` | `ST N°2 S4.png` · `ST N°3 S4.mp4` · `ST N°4 S4.png` (2250×4000 / 1080×1920) |
| raíz de `PISO18` | `Post S4 PISO18 25-09.png` — no es historia ni carrusel y no cabía en ninguna |

Revisión visual para Eli: `out/piso18/s4/revision/index.html` (con el antes/después
de cada foto intervenida y las dos referencias que ella dejó).

**Lo que decidió Eli en la sesión** (cuatro preguntas + tres):
1. La ST del **21-09 queda fuera** — está en APROBADO pero su celda no trae brief.
2. El carrusel va **sin texto**, las 4 slides limpias, logo sólo en la primera.
3. La animada es **montaje de fotos**, no timelapse — no hay metraje y su propia
   referencia tampoco era un timelapse.
4. La variedad floral se consigue **cambiando la paleta con Magnific** sobre la foto
   real; el atardecer, **reiluminando** un ventanal real; y la progresión del montaje
   arranca por lo más desnudo que existe, **sin inventar un salón vacío**.

**Lo que quedó montado en el repo** (antes no existía nada de esto):
`src/brand/piso18.ts` · `src/compositions/piso18/` · `src/P18Entry.tsx` ·
`clients/piso18/reglas.yaml` · `scripts/p18-s4-subir.py` · el logotipo ya recortado
sin el velo en `public/assets/piso18/logo-piso18-completo.png`.
**Las 7 capas de la marca pasan de 3½ a 7.**

**QA:** las 8 piezas pasan `python qa/motor.py --marca piso18`. Y el modo control
sobre las 5 piezas aprobadas del cliente queda **en cero falsos positivos**, después
de calibrar tres topes que marcaban la propia pieza que el cliente firmó (detalle y
mediciones en `clients/hilton/CLAUDE.md` § LA S4 PRODUCIDA, punto 7).

**⚠️ Qué sigue / qué está pendiente:**

- **Eli todavía estaba subiendo fotos** cuando se produjo esto («aún no cargan todas
  pero en un rato estarán»). En `SESIÓN PLATOS 23-5` sólo había un `.DS_Store`.
  **Cuando termine de subir, vale la pena volver a mirar**: si aparecen las carpetas
  de decoración (`DECO/SIN LOGO`, `Piso 18_28 ago decoración 2024`), el carrusel y la
  encuesta se pueden rehacer con arreglos reales variados en vez de recoloreados.
- **El conector de Drive corta en 10 MB** y se cae con más de 4 llamadas en paralelo.
  Quedaron **36 de las 121** fotos de la sesión de agosto sin bajar, y la sesión de
  julio 2026 entera es inaccesible por peso. **Destrabarlo es una decisión de Eli**:
  compartir esas carpetas como «cualquiera con el enlace» y baja todo con `curl`.
- **Falta `Edwardian Script ITC`**, la cuarta voz del sistema. La ST del 22-09 la
  pedía (su referencia usa letra manuscrita) y va en IvyPresto itálica mientras tanto.
- Sigue sin diagnosticar el **«quedó algo extraño detrás del logo»** del cliente: el
  velo del PNG plantilla ya se descartó como causa el 15-09, y hay que pedirle a Eli
  la pieza concreta.

---

## 2026-09-15 — Elisabet Soto «Eli» (Windows) · CIERRE DEL DÍA

**Qué se hizo:** el **estático de Hilton Honors** de DT (FEED col K, publica el
23-09 18:00) de cero a **APROBADO en cuatro rondas**. Foto real del lobby
(`HDT_36`), caja de cristal con 4 cuadrantes, íconos de las piezas de Eli, y los
dos logotipos. En paralelo, otra sesión cerró la identidad de **PISO18** (su
entrada está más abajo) y antes se había aprobado la **ST del 18-09 de Fiestas
Patrias**.

**Dónde quedó:** `Post n°1 S4 DT.png` (2250×2813, `md5 82d5c7a4…`) subido a
**S4 › DT** — [`132pCMwB4…`](https://drive.google.com/file/d/132pCMwB46c0nDz7DiyECSrLNFyShkFhv/view).
Verificado que el archivo del Drive es el mismo (10 216 607 bytes a los dos
lados) y que **se reproduce byte a byte** desde el repo (`cmp` limpio).
Composición en `src/compositions/hilton/DtFtHonors.tsx`; los cuatro comandos que
lo rehacen están en la cabecera de la entrada de DT, más abajo.

**Qué sigue:** nada de esta pieza. Lo siguiente de DT en la grilla es **FEED col I
(14-09)**, que sigue en `EN REVISIÓN` **con la fecha ya pasada** — hay que
preguntarle a Eli si se publicó. Y **STORIES col H (18-09)** pasó hoy de
`OK PARA DISEÑO` a **`EN EDICIÓN`** después de que se subiera: quien retome esa
pieza que lo mire.

**Abierto:**
- ⚠️ **6 vs 4 cuadrantes — lo decide el CLIENTE, no diseño (§G).** El brief dice
  «dividida en 6 cuadrantes» y la lista de rótulos trae 4, porque tachó «WiFi
  Premium» y «Check-in Digital» y no actualizó esa línea. Se armó con 4. Si los
  pide de vuelta, la caja pasa a 3×2 y es media hora.
- ⚠️ El **logotipo DT va en 2,42:1**, bajo la vara de 4,5. Es decisión de Eli
  (blanco, limpio, sin sombra ni halo) y el QA la lleva declarada como
  `⚠️ ACEPTADA`, no como «ok». La salida medida, si alguna vez se quiere en
  regla, es el azul de la §B.4: 4,84:1.
- ⛔ **Siguen frenadas las 3 fuentes que sólo tiene el cliente**: Stag LCG, Trade
  Gothic LT Std Bold y Trade Gothic Next LT Pro Bold.
- ⛔ **El banco de DT no tiene toma CENITAL ni PISCINA.** El brief de esta pieza
  pedía las dos y hubo que tomar las alternativas que él mismo ofrece. Si el
  cliente las quiere de verdad, es material que hay que pedirle.

---

## 2026-09-15 · Eli (Windows) — PISO18: la marca pasa de no tener nada a poder diseñarse

Sesión larga y **de sistema, no de piezas**: no se entregó nada al cliente, y fue a
propósito. Se cerró la identidad de una marca que el 09-09 tenía **0 de las 7 capas**.

**Qué se hizo:**

1. **Cayó el bloqueante n°1 que arrastraba desde el 09-09.** Eli subió hoy 14:03–14:22Z
   la carpeta **`GRILLA IA PISO18`** (`1jNeMFcp02zsbk_cEH-wTYMRaMuLwrN1u`) con los
   editables empaquetados, el logo, las piezas aprobadas y los proyectos de motion.
2. **Se midió la identidad** de los cuatro `Informe.txt` (S1, S2, S4, S5): mesa
   **1080 × 1350**, RGB sRGB, y las tipografías **IvyPresto Headline + Display**,
   **Raleway** y **Edwardian Script ITC**.
3. **Eli dictó la marca entera** en dos tandas: la palabra prohibida, las verticales,
   los botones de cotización, el color oficial, el material, los dos tipos de espacio
   y el reemplazo de rostros. Todo está en `clients/hilton/CLAUDE.md` §PISO18.
4. **Se produjeron y aprobaron los dos perfiles de personas**, en dos rondas.

**Dónde quedó:**

| | |
|---|---|
| Manual | `clients/hilton/CLAUDE.md` §PISO18 — creció ~30 KB |
| Grillas | `grillas/p18-septiembre-2026.md` (actualizada, la previa queda como `.PREVIA-10-09.md` para el diff) y **`p18-octubre-2026.md`, nueva** |
| Fuentes | `public/assets/fonts/piso18/` — Against y Raleway Medium **sí viajan**; IvyPresto **no** (`.gitignore`) |
| Script | `scripts/p18-ivypresto-link.py` |
| Material | `raw/hilton/piso18/MATERIAL.md` + `perfiles/APROBADO-*.png` (no viajan) |
| Rondas | `out/hilton/piso18/perfiles/ronda-1.html` y `ronda-2.html` |

**Lo medido que manda (y que corrige suposiciones):**

- ⭐ **Piso18 trabaja a 1080 px, no a 2250 como DT.** Tres formatos vivos: **1080×1350**
  feed, **2250×4000** story y **1080×1080** las promos.
- ⭐ **El color oficial es `#D4145A`**, dado por Eli. Mi medición sobre las promas en
  JPG daba `#D6145B`/`#D5135A`, a 2 de distancia: es el ruido de compresión.
  **Medir sobre JPG sirve para verificar, nunca para fijar.**
- ⭐⭐ **`logo PISO18.png` no es el logotipo: es la plantilla de story** 2250×4000 con un
  **velo negro en degradado** (alfa 150 en `y=0` → 0 en `y≈1667`) que ocupa el 99,4 %
  de su alfa. El logotipo son 566 px de ancho, proporción **2,4825**.
  ⚠️ **Me equivoqué y lo corregí el mismo día:** primero escribí que ese velo era el
  «algo extraño detrás del logo» que reportó el cliente. **No lo es** — la historia
  aprobada `ST N°1 S1.png` lo trae puesto, o sea es intencional y da legibilidad.
  **Ese pendiente del cliente sigue sin diagnosticar.**
- ⛔⛔ **`tabular-nums` NO FUNCIONA EN RALEWAY.** Medido con `fontTools` sobre los tres
  Raleway del estudio (Piso18, EBEMA, Between): **ninguno declara `tnum`**, sólo `lnum`,
  y **Chrome lo ignora en silencio**. El `1` mide 0,450 em y el `0` 0,614 — un 36 % de
  diferencia, que descuadra a la vista `$6.000.000` contra `$4.500.000`. La instrucción
  de Eli sobre los signos se cumple **por código**: caja al **máximo** de la fila, nunca
  al promedio (el defecto que se arregló en Between el 14-09).
- ⚠️ **Against le faltan `¿` y `¡`.** Un titular con pregunta no se puede componer en ella.

**⭐⭐⭐ IvyPresto: resuelta.** Es Adobe Fonts y no se empaqueta, **pero estaba activada
en Creative Cloud en esta máquina**. `scripts/p18-ivypresto-link.py` la busca **por su
nombre interno** (no por el id numérico, que cambia al re-sincronizar) y deja los **20
cortes** en `public/assets/fonts/piso18/ivypresto/`. **Probado en Chrome headless, no
supuesto:** las 20 renderizan bien **pese a ser CFF**, que es donde falló Brushwell.
⛔ La carpeta está en `.gitignore` y nunca sale del equipo.

**Los dos perfiles, aprobados:**

`PISO18-mujer-35` (id `2288933`) y `PISO18-hombre-35` (id `2288934`), fijados como
**referencias de personaje en la librería de Magnific** — se invocan por id o con
`@nombre` y la cara sale igual pieza tras pieza. Space **PISO18 · Perfiles de personas**.
Costo: 10 hojas, **1.000 créditos** (el modo ilimitado no aplicaba en la sesión).

> ⭐⭐ **Lo que costó y queda escrito:** «menos moreno» y «perfil chileno» se empujan
> entre sí — al aclarar, el modelo se va solo al fenotipo **nórdico**. La salida no fue
> aclarar menos sino **nombrar el tipo**: «chileno de ascendencia española o alemana,
> piel clara de subtono cálido, que siga leyéndose latinoamericano y NO nórdico».
> Y **la edad se pide por rasgos, no por número**: «35 años» daba 38–42; funcionó
> «frente lisa, mandíbula firme, sin marcas de expresión marcadas».

**Qué sigue:**

Diseñar. Lo primero que vence de las **7 piezas en `OK PARA DISEÑAR`** es **FEED col M
(22-09, carrusel)** y **STORIES col L (22-09)**.

**Abierto:**

- ⛔ **Tres cosas que las dicta Eli:** el archivo del logo **`PISO18` solo** (no está en
  la carpeta, sólo el completo) y **qué cuenta como «ocasión»** para usarlo; **en qué
  pieza** vio el cliente lo del logo; y las tres del 09-09 que siguen sin respuesta
  (¿vale la §G para P18?, ¿la regla de rostros?, ¿quién hace S2 y S3?).
- **Eli va a separar las carpetas de matrimonio tradicional y lounge**, y a adjuntar una
  sesión nueva. Hace falta apenas se toque una pieza con el salón montado.
- ⚠️ **El material no se puede bajar masivamente.** El token del estudio es `drive.file`
  y devuelve **0 archivos** en las 4 carpetas de fotos; `curl` da la página de login; no
  hay Drive para escritorio. Sólo sirve el conector MCP, **de a un archivo** — alcanza
  para armar una pieza, no para una hoja de contacto del banco. Para eso habría que
  ampliar el token a `drive.readonly` (misma decisión abierta desde Between el 14-09).
- ⚠️ **Los `.HEIC` de la sesión de julio no los carga Chrome** y los `.MOV` de iPhone
  traen rotación por metadato y 60 fps. Convertir antes de rendir.
- ⚠️ La **paleta** sigue sin salir del `.ai` (pesan 1,5 GB y no se abrieron), y no existe
  `clients/piso18/` ni `marca.json` ni kit en `src/brand/` ni reglas en `qa/motor.py`.

**⚠️ Aviso para quien abra mañana — hubo DOS sesiones en paralelo sobre este repo.**
La otra trabajó **DoubleTree** y commiteó `856753d` (el estático de Hilton Honors + el
QA por pieza). **Sigue con trabajo sin commitear**: `src/compositions/hilton/DtFtHonors.tsx`
(ronda 4, el aire de los textos) y `raw/hilton/dt/ref-s4/try.jpg`. **Este cierre NO los
subió a propósito** — no se commitea el trabajo a medias de otra sesión bajo un mensaje
de Piso18. Esa sesión tiene que cerrar lo suyo, o se pierde.

---

## 2026-09-15 · Eli (Windows) — DOUBLETREE: el post de Hilton Honors, ✅ APROBADO

> ## ✅ APROBADA POR ELI EN LA RONDA 4 — 15-09-2026
>
> **`Post n°1 S4 DT.png`** · 2250×2813 · `md5 82d5c7a4fc9cb050d2cb109a0e8639c0`
> Subida a **S4 › DT** (`1sW3paRt7FotnGBe8IZLccTTSNz8rN9TF`) como
> [`132pCMwB46c0nDz7DiyECSrLNFyShkFhv`](https://drive.google.com/file/d/132pCMwB46c0nDz7DiyECSrLNFyShkFhv/view).
> **Verificado que el archivo del Drive es el mismo**: 10 216 607 bytes a los dos
> lados. Cuatro rondas en el día. El enlace nunca cambió — se reemplazó en sitio.
>
> ⚠️ **Lo único que queda abierto NO es de diseño:** el brief dice «6 cuadrantes»
> y la lista de rótulos trae 4, porque el cliente tachó «WiFi Premium» y
> «Check-in Digital» y no actualizó esa línea. **Se armó con 4 y lo decide el
> cliente** (§G). Si los quiere de vuelta, la caja pasa a 3×2.
>
> **Cómo se reproduce, de cero:**
> ```bash
> python scripts/dt-ft-honors-foto.py
> python scripts/dt-rendir.py DT-F-HiltonHonors DT-F-HiltonHonors-Guia >        --salida out/hilton/dt/ft-honors
> python scripts/dt-qa.py "out/hilton/dt/ft-honors/*.png"
> python scripts/dt-ft-honors-revision.py
> ```
>
> ---
>
> ✅ **CORRECCIÓN DE LA PROPIA SESIÓN QUE LA HIZO.** Esta entrada la reconstruyó
> otra sesión desde los archivos, con la pieza a medio camino, y por eso decía
> «rendido y SIN ENTREGAR / no se subió nada». **Ya no es así:** la pieza pasó el
> QA y se subió a **S4 › DT** (`1sW3paRt7FotnGBe8IZLccTTSNz8rN9TF`) como
> `Post n°1 S4 DT.png` —
> [`132pCMwB46c0nDz7DiyECSrLNFyShkFhv`](https://drive.google.com/file/d/132pCMwB46c0nDz7DiyECSrLNFyShkFhv/view) —
> a las 14:24Z. Queda **a la espera del visto de Eli**, no de la entrega.
>
> ⚠️ Como en las otras subidas de la cuenta, el archivo queda a nombre de
> `valeria@copywriters.cl`: lo sube el token del estudio, no Eli.
>
> **La página de revisión NO se subió al Drive a propósito** — trae notas internas
> y esa carpeta la ve el cliente. Vive en
> `out/hilton/dt/ft-honors/Post n°1 S4 DT - revision.html` (1,5 MB, un solo
> archivo, imágenes embebidas) y la arma `scripts/dt-ft-honors-revision.py`.
>
> Lo demás de esta entrada está bien, y sigue abajo. Se agregan al final las dos
> cosas que dejó la compuerta.

**Qué se hizo.** El post estático de **Hilton Honors** (FEED col K, 23-09, 18:00),
armado contra `Ref post s4.jpg` de REFERENCIAS S4 DT. Rendido a las 11:14 en
`out/hilton/dt/ft-honors/Post n°1 S4 DT.png` (2250×2813, 10 MB) con su guía de QA.

**Dónde quedó.**

| | |
|---|---|
| Composición | `src/compositions/hilton/DtFtHonors.tsx` |
| La foto del lobby | `scripts/dt-ft-honors-foto.py` → `public/assets/hilton/dt/ft-honors-lobby.jpg` |
| Render | `out/hilton/dt/ft-honors/Post n°1 S4 DT.png` |

⭐ **Y dejó una medición para la marca: el máster de FEED va a escala 2,0837, no
2,0833.** El 4:5 de esta cuenta es 2250×**2813** —las tres piezas aprobadas y la
plantilla `logo-post.png`— y 2813 no es 4:5 exacto: 4:5 de 2250 da 2812,5 y el
equipo redondeó hacia arriba. Con la escala de historia la mesa sale 2250×2812 y
queda 1 px corta. Ya está puesto en `dt-rendir.py`, que elige la escala por el
prefijo del id (`DT-F-*` → feed).

**Qué sigue.** Mostrárselo a Eli y, si lo aprueba, subirlo a **S4 › DT** con el
nombre `Post n°1 S4 DT.png` — así lo levanta el portal. **No se subió nada.**

**Abierto.**

1. ⚠️⚠️ **Discrepancia del brief, informada y NO resuelta (§G):** el brief pide
   «dividida en **6** cuadrantes» y la lista de rótulos trae **4**. No es un error
   de lectura: el cliente **tachó** los otros dos («WiFi Premium» y «Check-in
   Digital») junto con el titular viejo, y la línea del «6» quedó sin actualizar.
   Se armó con 4 (2×2), que es lo único que el brief permite — poner 6 obligaría a
   inventar dos beneficios. **Decide el cliente si vuelven los tachados.**
2. **Dos cosas que el brief nombra y el banco no tiene**, resueltas con la
   alternativa que el propio brief ofrece en la misma frase: no hay toma
   **cenital** del hotel («o angular elegante») y el complejo no tiene la
   **piscina** fotografiada («instalaciones, lobby o habitación» → se usó el lobby).
3. **El titular va a la izquierda y al 49 % de la altura**, que es donde lo pone la
   referencia; el brief dice «zona superior izquierda». Se siguió la referencia,
   que es lo que Eli mandó hoy para esta pieza, y queda anotado por si lo quiere
   más arriba. No es un conflicto real —en los dos casos va a la izquierda— pero
   se informa.

### ⭐⭐ Lo que dejó la compuerta, y vale para toda pieza de FEED que venga

1. **`dt-qa.py` tenía el máster quemado en 2250×4000.** Es el mismo modo de falla
   que esta misma mañana con las bandas del Día del Turismo, una capa más arriba:
   ahora era el FORMATO el que estaba al nivel del módulo. La primera pieza de
   feed de la cuenta habría rebotado como si estuviera mala. Ahora hay `FORMATOS`
   (máster, alto de mesa, zona segura y geometría del logotipo por formato) y cada
   pieza declara el suyo. ⚠️ Y la zona segura inferior de 340 px **es sólo de
   historia**: exigírsela a un post de feed orgánico acusa al pie por estar donde
   corresponde.
2. ⛔⛔ **La huella de fuente por perfil de columnas NO sirve para un titular corto
   en versales, y acusó a esta pieza estando perfecta.** En «EN CADA ESTADÍA»,
   **georgia le ganó a la Stag correcta** (r=+0,697 contra +0,619). El perfil mide
   dónde caen los astiles, y 15 versales de anchos parecidos normalizadas a 200
   columnas dan un perfil parecido en cualquier serif. Se resolvió comparando
   **glifo a glifo en 2D** —la regla del estudio, `revex-adn-medido`—: Stag-Light
   **0,900** contra constantia 0,630 · Stag-Regular 0,576 · georgia 0,539. El
   elemento elige el método con `"huella": "glifos"`; el perfil sigue siendo bueno
   para una línea larga en caja baja. De paso, `perfil_pil()` ahora compone con el
   mismo `letter-spacing` que declara la pieza.
   ⚠️ Verificado que la ST del Día del Turismo sigue pasando igual.
3. ⭐ **El contenedor de DT tiene dos densidades y las dos son legítimas.** Medido,
   el panel de `DT FT S3` es casi macizo (α 0,84–0,90 sobre `#09194E`); acá va en
   0,30 porque el brief pide «estilo cristal o translúcida». Y su ANCHO son 880
   (la referencia) y no 730 (el panel de DT) — mismo criterio que en el Día del
   Turismo cuando las dos medidas chocaron.
4. **Las carpetas de REFERENCIAS de Eli piden sesión de Google**: no abren por
   `embeddedfolderview` ni por `uc?export=download`, y el token del estudio
   tampoco las ve. Abre el conector MCP de Drive. ⭐ Y hubo atajo: su archivo era
   un pin de Pinterest y **el brief enlazaba ese mismo pin en su celda LINKS**, así
   que la versión grande se bajó de `i.pinimg.com/originals/`. Antes de trabarse
   con una referencia, mirar la celda LINKS.

**Y una de otra pieza, vista al refrescar la grilla (no es de esta sesión):**
STORIES col H (18-09, el saludo de Fiestas Patrias que se subió hoy) pasó de
`OK PARA DISEÑO` a **`EN EDICIÓN`**. Quien retome esa pieza que lo mire.

### ⭐⭐ RONDA 2 (15-09, tarde) — y una corrección de MARCA que no era de esta pieza

Eli: «Te falta añadir el logo de Hilton honors, ya que es de los beneficios.
Trata de utilizar iconos ya utilizados en mis piezas gráficas, busca en los
editables. El título déjalo centrado. Logo blanco y conserva la imagen del fondo,
la transparencia azul más abajo y sutil. Si los textos no se leen usa una sombra
paralela muy sutil en los textos.»

Todo aplicado y re-subido al mismo enlace **menos el logo de Hilton Honors**
(ver abajo). El QA quedó limpio y la ST del Día del Turismo sigue pasando igual.

**⛔⛔ Lo grande: los rótulos del panel de DT van en STAG, no en Trade Gothic.**
Salió por el pedido de los íconos: al ir a buscarlos a `C1 FT N2` se midió el
texto de al lado, glifo a glifo. **Stag Regular 0,701 contra Trade Gothic 0,285**
(14 letras, IoU 2D). La ronda 1 los había puesto en Trade siguiendo la regla
escrita «Trade para el cuerpo», que viene del manual oficial de Hilton — pero lo
que el cliente aprobó es otra cosa. Corregido en la pieza y en el manual.
⚠️ **Y van tres veces que pasa lo mismo: una regla escrita no sustituye una
medición sobre la pieza aprobada.**

**Lo demás que dejó la ronda, todo en el manual:**

1. **La gramática de cuadrante de Eli**, que no estaba escrita: caja de ícono
   70,6×57,1 · trazo 2,4 px · **regla vertical de 1,9** entre ícono y rótulo ·
   rótulo a dos líneas. Y sus íconos son **objetos con estructura interior**, no
   siluetas — por eso la luna se cambió por un regalo (el brief daba a elegir).
   La **cama** se extrajo de `C1 FT N2` y ya vive en
   `public/assets/hilton/dt/icono-cama-eli.png`.
2. **El logotipo blanco es excepción de PIEZA**, no cambio de la §B.4. Medido:
   blanco 3,30:1 contra azul 4,84:1 sobre el cielorraso. Eli pidió blanco y dio
   la salida (la sombra); con ella sube a 3,61:1 y se lee.
   ⛔ **Se probó el halo radial detrás del logo —el recurso del Día del Turismo—
   y NO sirve acá:** allá caía sobre cielo con textura, acá sobre un cielorraso
   plano, y se veía como una mancha. Se botó y se cambió por tres sombras
   apiladas sobre el propio logotipo. **Un recurso aprobado en otra pieza no se
   hereda sin volver a mirarlo.**
3. **«El velo más abajo y sutil» se resuelve CURVANDO la rampa** (cóncava →
   convexa, pie 0,58 → 0,50), nunca dejándola plana y arrancándola más abajo:
   ese codo es la banda que ella misma marcó como «forzado».
4. **`dt-qa.py`: la vara de contraste depende del tamaño de la tinta.** Estaba
   quemada en 4,5 y reportó en rojo un titular a 4,22:1 que está bien — el manual
   ya fijaba **3:1 para titulares** desde el 10-09. Y una desviación decidida por
   la diseñadora se declara en la ficha de la pieza, con su número a la vista.

**⚠️ PENDIENTE, Y ES LO ÚNICO: EL LOGO DE HILTON HONORS.**
Está ubicado (`GRILLA IA DT › Logos › Hilton Honors Logo_White PNG.png`, 14 KB,
ya blanco) y **no se puede traer a disco**: `curl` devuelve login en las tres
rutas, el token es scope `drive.file`, y el conector MCP entrega inline —sin
dejar archivo— todo lo que pese menos de ~40 KB. Se intentó transcribir el base64
dos veces y las dos llegó cortado; se borró en vez de montar un logotipo roto.
**Se le pidió a Eli que lo copie a `raw/hilton/dt/identidad/logos/`.** El hueco ya
está reservado (y 1186, centrado) y la composición lo dibuja con
`conHonors={true}` — es cambiar una línea y volver a rendir.

⛔ **Y la trampa:** `hilton honors.png` (43 KB) de esa misma carpeta **SÍ** baja y
**NO es el Honors**: es el logotipo **Hilton «For The Stay»**, mal rotulado en el
Drive. Guardado como `hilton-FOR-THE-STAY (NO es Honors).png` para que nadie lo
use por error.

### ⭐⭐ RONDA 3 (15-09, tarde) — el cristal, y el pendiente RESUELTO

Eli: «esos iconos se ven achatados, aplastados, déjalos bien puestos. El logo no
le hagas eso del fondo o sombra azul. Te faltó añadir el logo de Hilton Honors
[+ enlace]. Y faltó el detalle de la referencia de ese cuadro: mira, difuminado
dentro del cuadro el fondo.»

Las cuatro aplicadas, re-subida al mismo enlace, QA limpio y la ST del Día del
Turismo sigue pasando igual.

1. ⭐⭐⭐ **EL CUADRO DE CRISTAL LLEVA EL FONDO DIFUMINADO.** Era el detalle que
   hacía que la caja se leyera como un rectángulo pintado. Medido sobre el pin
   cruzando el borde: mediana **3,5** ⇒ `backdrop-filter: blur(3.5px)` @1080.
   ⛔ La primera medición comparó la caja contra franjas de arriba y abajo y dio
   «no hay desenfoque» — estaba mal planteada, porque arriba hay pasto y abajo
   grava. **Para medir un desenfoque hay que cruzar el borde.**
2. ⭐⭐ **Un ícono se dibuja en SU proporción, no llenando la ranura.** Los tres
   dibujados llenaban la caja de 71×57 de Eli, que es ancha porque su contenido
   es una CAMA. Pasaron a un cuadrado de 52×52 centrado.
3. ⛔⛔ **La cama se volvió a extraer: el alfa se saca del HISTOGRAMA.** La
   primera extracción usaba una rampa 60→250 y arrastraba un halo (el panel de
   `C1 FT N2` es translúcido y la foto que se ve a través quedaba con alfa > 0).
   El histograma es bimodal ⇒ rampa **120→235**.
4. **El logotipo DT queda limpio, sin sombra ni halo, y bajo la vara: 2,42:1.**
   De acá sale una regla para la compuerta: **una desviación que decidió la
   diseñadora no se imprime como «ok»**. `dt-qa.py` tiene ahora tres estados
   —ok · ⚠️ ACEPTADA · ⛔— y la aceptada sale con su número y su motivo.
5. ✅ **EL LOGO DE HILTON HONORS, RESUELTO.** Eli abrió el acceso del archivo y
   bajó entero con `uc?export=download`: **13 967 bytes, los que declara Drive**.
   Blanco puro con alfa, 1091×470, proporción 2,3213. Puesto donde ella lo
   dibujó, centrado entre el pie de la caja y la regla del pie.

**Sigue abierto:** la discrepancia de los **6 vs 4 cuadrantes** del brief, que es
del cliente y no se resuelve acá (§G).

### ⭐ RONDA 4 (15-09, tarde) — jerarquía y aire

Eli: «agranda un poco el logo de Hilton Honors, cuida las jerarquías y orden,
sube un poco lo de arriba, y al logo de Hilton Honors quítale esa sombra que
tiene. En los textos (no del título) separa un poco, están muy juntos entre
palabras y no se ve tan legible.»

Las cuatro aplicadas, re-subida al mismo enlace, QA limpio.

1. ⭐⭐ **El espacio ENTRE PALABRAS es un ajuste aparte del tracking.** Ella
   nombró las palabras, así que ahí va el grueso: `wordSpacing: 0,14em` en los
   rótulos y en el llamado; el tracking apenas 0,012em. El titular no se toca.
   Se ve en la medición: el llamado pasa de 444 a **474 px** de ancho.
2. ⭐ **«Sube un poco lo de arriba» es lo que abre el espacio de abajo.** Titular
   +35, caja +30, y con eso el logotipo de Honors puede crecer. Los saltos del
   tercio inferior quedan parejos: caja→Honors 38 · Honors→regla 38.
3. ⭐ **La jerarquía de los dos logotipos.** Honors pasa de 52 a 64 de alto
   (ancho 148,8, proporción real 2,3213) y queda pesando casi como el DT (160):
   es el asunto de la pieza, no una firma secundaria. Y va **sin sombra**, como
   el DT — sobre el piso de madera da 7,19:1.

---

## 2026-09-15 (RONDAS 1–6) · Eli (Windows) — DOUBLETREE: la ST del 18-09, aprobada y subida

**Qué se hizo.** La historia estática de STORIES col H (18-09, 09:00), de cero a
aprobada en seis rondas. **Subida al Drive** (`16JBlbWB0AImxv_7sdS7Yj3btZh2pX2iT`),
`md5` verificado contra el local: `eb0543ba8bf43ff8538a262209f5f35d`.

### ⭐⭐⭐ 1. La ronda 1 estuvo BIEN HECHA y aun así era la pieza equivocada

Se eligió una foto entre las 150 de la carpeta **midiendo**: se barrieron todos los
encuadres 9:16 posibles puntuando la calma de la franja del texto y la presencia de
sujeto abajo. Salió `IMG_1988`, y con el aparato de la ST del Día del Turismo la
pieza pasó el QA a la primera.

Eli mandó una referencia armada y **cambió la pieza entera**: collage, titular en
itálica, bajada en versales, logotipo abajo. Nada de lo medido estaba mal; lo que
faltaba era la dirección, y esa no se deduce del brief.

⚠️ **Lo que SÍ se hizo bien y conviene repetir:** el brief dejaba el collage como
«por confirmar, no resolver sin aprobación del cliente», así que la ronda 1 fue de
una foto y el collage se INFORMÓ en vez de resolverlo (§G). Lo destrabó Eli.

### ⭐⭐ 2. El QA tenía la geometría de UNA pieza al nivel del módulo

`dt-qa.py` guardaba las bandas y los textos del Día del Turismo como constantes
globales, así que la primera historia nueva de DT se midió contra la pieza anterior
y cantó **cuatro fallos que no existían**. Un QA que acusa a una pieza sana se deja
de mirar, que es peor que no tenerlo.

Ahora hay `PIEZAS`: cada una declara sus bandas, sus textos, la tinta de su
logotipo y su geometría, y se elige por el nombre del archivo. Verificado que la
del Turismo sigue pasando.

⚠️ Y la regla que ya va por cuarta vez: **las bandas se re-miden en cada ronda que
mueva el texto, y el QA se corre DESPUÉS de eso, nunca antes.**

### ⭐⭐ 3. Las cuatro correcciones de la ronda 3, y la que arrastraron

«Deja el logo arriba, aprieta los interlineados, el fondo en azul DT.»

| | Antes | Después |
|---|---|---|
| Logotipo | y 1345 · 180 px | y 241 · 167 px (plantilla) |
| Hueco del titular | 47 px · 0,37 em | 32 px · 0,25 em |
| Hueco de la bajada | 31 px · 0,62 em | 19 px · 0,38 em |
| Hilo entre cuadros | `#FAFAFA` | `#09194E` |

⭐ **Apretar los dos huecos internos obligó a mover el que los separa.** Quedaba en
76 px contra 32 dentro del titular —más de 3×— y la regla es ~1,5×. La bajada subió
35 px y quedó en 59 contra 32: 1,8×.

⭐ **El hilo en azul de marca cohesiona el mosaico.** En blanco se leía como diez
fotos sueltas; en azul, como una sola pieza.

### ⭐⭐ 4. El logotipo creció y destapó un defecto de fondo

Ronda 4: de 167 a **225** (15,5 % → 20,8 % del ancho). Con el titular al 75 %, el
logotipo no sostenía el otro extremo de la jerarquía. ⚠️ Es excepción de TAMAÑO y
no se hereda: sigue centrado, en su tope de 241 y a su proporción real.

**Y al crecer, su caja pasó a ir de x=427 a x=652 — y el corte en diagonal del
mosaico la cruzaba entre 564 y 588.** Una línea azul saliendo por detrás del
lockup: el mismo defecto que obligó a re-encuadrar la foto del Día del Turismo. El
corte se movió a (745,0)–(700,455), a 48 px del canto.

> **Regla: cuando un elemento de marca cambia de tamaño, se vuelve a mirar QUÉ HAY
> DETRÁS de su caja nueva.** El QA no lo agarra —mide contraste, no colisiones— y a
> ojo tampoco, porque el defecto aparece recién al 100 %.

### ⭐⭐ 5. «De una esquina» eran DOS banderas

Ronda 4 puso una bandera asomando por la esquina superior izquierda, con la esquina
elegida midiendo las cuatro (sup-izq 11,01:1 · sd 16,0, la más calma). Eli devolvió
la pieza con **dos marcas rojas flanqueando el bloque de texto**.

⭐ Y ya estaba resuelto: es el mismo pedido de la ronda 5 de la S3 de Between, y de
ahí sale el truco del **`espejo` POR FUERA de la rotación** — con el mismo `giro` y
espejo en una de las dos, el par queda simétrico solo.

⭐ **La geometría de la bandera se COPIÓ, no se importó.** Un archivo de Between no
tiene nada que hacer dentro de una pieza de DT, pero la geometría no es criterio de
Between: es la bandera de Chile, con dos defectos de zoom ya corregidos (el escalón
del cantón y la espina de la división). Lo que SÍ cambió: acá el trazo va limpio,
sin la textura de mano de Between.

### ⭐ 6. «Al límite el palito» se calcula, no se busca a ojo

Ronda 6: las banderas suben de 205 a 235 y se corren hasta que la punta del mástil
cae EXACTO en el canto. El mástil termina en (56, 224) del viewBox y todo gira 18°,
así que su punta real cae en **(31,6 · 190,4)** ya rotada; a escala 235/300 son 24,7
px ⇒ `x = −24,7` y `x = 869,7`.

⚠️ **Y el ancho tiene techo, que lo pone el texto:** a 235 la tela llega a x=200 y
la bajada más larga empieza en x=236 — 36 px de aire. A 245 quedarían 27; a 265 se
tocan.

⚠️ **Trampa del QA que dejó esta ronda:** las banderas caen en la misma franja que
«Patrias!», así que el QA medía 991 px de «ancho del titular» —el vuelo de bandera a
bandera— y cantaba descentrado. La ventana de esa línea se cerró a x 280-820.

### ⭐ 7. Cómo se listó una carpeta que el conector no lista

La carpeta que mandó Eli (`1_LUmZ26C9FtGl9zLgE_IxRoN7-0so91w`, 179 archivos) devuelve
`{}` por `search_files`. El índice salió por **`embeddedfolderview`** y la hoja de
contacto con las **miniaturas** (`thumbnail?id=…&sz=w400`, ~30 KB), no bajando 150
archivos. Y cuatro de esos «.jpg» son **HEIC** por dentro: `pillow_heif` los abre.

### ⚠️ Dos cosas que chocan con reglas escritas, y mandó la referencia

- **La línea larga quedó arriba** — el repertorio de DT dice corta arriba, larga
  abajo. Acá el corte lo fija el titular de Eli.
- **Las versales van en Stag y no en Trade Gothic** — el manual oficial le da a
  Trade las versales; la referencia las pone en serif itálica.

Las dos anotadas en la composición para que se lean como decisión, no como descuido.

### ⛔ Los rostros: autorización puntual, NO precedente

§A de DT dice que en imagen no va el rostro de un trabajador. Eli la levantó **para
esta pieza y por el formato**: «acá no pasa nada si se ven los rostros, por formato
de storie». La próxima pieza de DT vuelve a §A salvo que ella diga lo contrario.

### Entrega y dónde quedó todo

| | |
|---|---|
| Drive | `16JBlbWB0AImxv_7sdS7Yj3btZh2pX2iT` · `DT ST 18-09 Felices Fiestas Patrias.png` |
| Verificación | `md5 eb0543ba8bf43ff8538a262209f5f35d`, igual al local · 12 299 570 B |
| Composición | `src/compositions/hilton/DtStFiestasPatrias.tsx` |
| El mosaico | `scripts/dt-st-fiestas-collage.py` (+ los curl para re-bajar los 10 cuadros) |
| La foto de la ronda 1 | `scripts/dt-st-fiestas-foto.py` |
| QA | `scripts/dt-qa.py`, ahora por pieza |
| Revisión | `out/hilton/dt/st-18sep-fiestas/revision.html` |

`npm run typecheck` limpio. `dt-qa.py` 1/1 limpia, y la del Día del Turismo sigue
pasando.

### Abierto

1. **El brief sigue diciendo que el collage es «por confirmar».** Lo destrabó Eli,
   no el cliente. La conversación con el cliente es de ella.
2. `scripts/dt-ft-honors-foto.py` apareció sin commitear (11:04 de hoy) y **no es de
   esta sesión**. Se dejó fuera del commit a propósito.
3. La ronda 1 quedó reproducible por si el cliente prefiere la de una foto.

---

## 2026-09-14 (RONDAS 27–32) · Eli (Windows) — BETWEEN ST 28-09: el montaje se bota y la escena se GENERA

**Qué se hizo.** La historia del 28-09 («HUMOR | CAFÉ TO GO») se rehizo entera y
quedó **APROBADA**. Seis rondas en un día, y las tres primeras fueron por el
camino equivocado.

⛔⛔ **LA LECCIÓN DEL DÍA, Y ESTABA ESCRITA.** Las rondas 27 y 28 recortaron el
vaso de `IMG_4150` y le corrigieron por código el contorno, el campo de luz, la
textura de la fibra, la sombra y la luz envolvente — incluso con un trasplante de
luz de Magnific. Tres rechazos seguidos de Eli: «se ve pegoteado», «parece que
tuviera luz de flash», «no aprobado». La respuesta llevaba desde el 07-09 en la
primera línea de [`PROMPTS-DE-ELI.md`](PROMPTS-DE-ELI.md):

> **«No se compone: se GENERA.»** […] generar un fondo y pegarle encima recortes,
> logotipos vectoriales, sombras de contacto y campos de luz calculados **produjo
> cinco rechazos seguidos**, y el último con estas palabras: «parecen de paint
> pegoteados».

Y su regla: **cuando algo falla varias veces con materiales distintos, lo que hay
que cambiar no es el material ni la posición: es el MÉTODO.** Antes de tocar una
pieza de Between se lee ese archivo. No se leyó, y costó tres rondas.

**Cómo quedó.** Escena generada con Nano Banana Pro (`magnific.py pro --aspecto
story --resolucion 4K`) y tres referencias a 1024 px: el vaso grande de la sesión
del 09-09 (de ahí llega el logotipo impreso), la foto de la persona, y el muro del
Winter Garden. El vaso, las manos, la sombra y el fondo **nacen juntos**: los dos
brazos abrazándolo, la sombra sobre el pantalón, el apoyo en la cadera. Nada de
eso se podía montar.

**Las rondas del cliente, en orden:**

| Ronda | Qué pidió Eli | Cómo se resolvió |
|---|---|---|
| 27 | «le falta naturalidad, un recorte preciso del vaso, se ve pegoteado» + «parece que le falta la cabeza» | contorno por grabCut guiado, sombra dirigida, y el lienzo crecido para que la tapa pase 103 px sobre la línea de coronilla |
| 28 | «parece que tuviera luz de flash» | medido: la fibra estaba 3,7× sobre la del vaso real y el cartón en 232/255 |
| 28b | «hazlo realista en magnific» (×2) | se corrió: 3 relights lo volvieron gris (Δ logo 43–59) y la edición alisó el material. Se entregó un híbrido |
| 29 | «no se ve realista, se está suciando el fondo […] guíate de mis prompts» | **se botó el montaje y se generó la escena** |
| 30 | «prueba con el fondo de winter garden […] se ve una sombra extraña» | Winter Garden + candado contra sombras sueltas |
| 31 | «no tenemos ese color en Between, debe ser el café de bw» | *(se entendió mal: se cambió el fondo entero)* |
| 32 | «me refería al degradado verde de arriba, NO al fondo» | plantas + muro del local en café `#675B49` encima. **APROBADA** |

⭐ **El verde lima de arriba NO se puede repintar por código, y se intentó cuatro
veces**: máscara por detalle (el café se mete entre las hojas), borde por columnas
a σ=90 (recto), borde «sostenido» a σ=14 (un peine de picos verdes) y transición
blanda (no llega a cambiar el color). La razón: **esa franja no tiene borde, es un
degradado**, y buscarle uno es inventarlo. Se le pidió al generador —«las plantas
llenan el fondo y su COPA es irregular; por encima, el muro del local pintado de
#675b49; el borde lo dibujan las hojas»— y salió a la primera.

⛔ **El logotipo hay que mirarlo AL 300 % EN CADA TIRADA.** De seis generaciones,
tres escribieron mal la Ǝ: una con E normal, otra con la Ǝ en la penúltima letra
(«BETWEƎN») y otra con dos Ǝ. Acierta ≈ una de cada dos. También hubo que
re-tirar dos veces por el **anillo blanco en la base** —que es del vaso CHICO— y
ahí quedó otra regla: **volver a tirar sale más barato que parchar el producto**;
tres intentos de taparlo por código dejaron un peinado de rayas y un arco mal
ajustado.

**Dos cosas que se arreglan siempre después del generador** (ya estaban en el
manual de Eli, y se confirmaron): el color de marca no llega exacto —el muro llegó
`#7E6C59` y se llevó a `#675B49` con ganancia multiplicativa sobre el medio tono—
y el encuadre hay que pedirlo franja por franja.

⭐ **Y un truco que ahorró una generación:** el titular caía sobre la tapa. Como el
muro de arriba es plano, se continuó hacia arriba y se bajó la escena 734 px con
`--bajar`. El salto de tono en esa costura mide **0,03** (sobre 1,5 se vería).

**Dónde quedó.**

- Pieza: `out/hilton-between-s5-r32/BW-S5-HumorToGo.png` (2250 × 4000), fondo en
  `public/assets/hilton/between/s5/st-28-09-togo.jpg` (versionado).
- **Subida al Drive reemplazando el archivo**: `1dIH_dM4yBlM2AX5TlCE9tKMgaqlMB1wr`,
  mismo enlace, 11,0 MB, `modifiedTime` del 14-09. Carpeta `STS` de la S5.
- Generación: `scripts/between-st-s5-togo-generar.py` (6 escenas, con los prompts
  textuales) · acabado: `scripts/between-st-s5-togo-acabado.py`.
- Referencias a 1024 px versionadas en `raw/hilton/between/s5/refs-gen/`.
- El montaje descartado queda documentado en `scripts/between-s5-vaso-gigante.py`
  y `scripts/between-s5-vaso-magnific.py` — sirven de registro de por qué no.
- Composición: `src/compositions/hilton/BetweenStS5.tsx`. El titular bajó de
  y=300 a **y=262**: en la escena generada el vaso empieza más arriba.
- Revisión que vio Eli: <https://claude.ai/code/artifact/225d6e23-8761-49ee-90cd-b857724f5a08>

**Medido en la pieza entregada:** contraste del titular 4,9–5,6:1 por tercios
(beige sobre café de marca), 79 px de aire entre el texto y el filo de la tapa,
bloque en 263–538 sobre 1920. `between-qa.py` marca el pliegue del pantalón como
si fuera texto: es el falso positivo de siempre.

**Qué sigue.** La ST del 30-09 (Plateada al Carmenere) sigue en Drive con la
versión del 11-09 y no se tocó hoy.

**Abierto.**

- ⚠️ **El brief dice «una chica» y la pieza es de un hombre.** El titular es de
  primera persona y no tiene género, así que se sostiene; queda informado, no
  resuelto — el brief es del cliente.
- Sigue pendiente de antes: las columnas T y U en `OK PARA DISEÑAR` desde el
  11-09, entregadas y sin visto del cliente.

## 2026-09-14 (RONDA 26) · Eli (Windows) — BETWEEN S5: el vaso del 28-09 deja de ser cartón generado

**El encargo.** «Debemos mejorar el vaso y trata de utilizar una foto como la
sesión nueva de vasos ToGo» — la sesión del 09-09 que entró al banco esta misma
mañana.

**⭐⭐ El diagnóstico es medible, no de gusto.** Puesto el vaso de la pieza al
lado del de la sesión y normalizados al mismo ancho, el generado se delata en
tres cosas:

| | pieza (r3) | vaso real 09-09 | pieza (r26) |
|---|---|---|---|
| saturación del cartón | 0,198 | **0,619** | **0,391** |
| tono del cartón (R/G) | 1,136 | 1,486 | 1,296 |
| motas de pulpa | sí, de 5 a 15 px | ninguna | ninguna |
| **logotipo / ancho del vaso** | **0,42** | **0,91** | A 0,76 · B 0,88 |
| alto del bloque / ancho | 0,140 | 0,377 | A 0,294 · B 0,386 |

⛔ **No se regeneró nada.** `scripts/between-s5-vaso-real.py` (nuevo) le cambia
la **superficie** al vaso ya aprobado, partiendo de la misma base limpia de la
ronda 4. La silueta, el tamaño, la inclinación, la tapa, las manos y la chica
quedan intactos — es lo que Eli cerró en la ronda 3 («el tamaño está ideal del
vaso y también está bien las tipografías y la persona»).

**Cómo:**

- **La luz de la escena se conserva.** El campo de luz sale del propio vaso con
  una mediana de 21 px —que borra las motas, que miden 5 a 15— y un desenfoque
  corto de 9 px que aplana las nubes de 80–150 px del generador. El pliegue del
  cartón y la sombra de contacto de los dedos quedan intactos, que es lo que
  hace que la mano se vea apoyada.
- **La fibra sale de `togo-grande-frontal.jpg`** (IMG_4150, el packshot del vaso
  grande, la toma más nítida de las 39), dividiéndole su propia luz. Va a 0,45
  de escala: a 1:1 la trama se lee como damasco, porque el vaso de la pieza es
  1,4 veces más ancho que el de la foto.
- **El color es el kraft medido bajo el iluminante de ESTA escena.** El tono de
  tres tomas de la sesión, corregido a 0,75 por la luz fría del patio: la tapa
  negra, que es neutra, da B/G 1,16 acá y ≈1,00 en la sesión.

**⭐⭐⭐ Las manos NO se pueden separar por descarte, y me costó tres vueltas.**
Definir «piel = lo que no es cartón» falla porque **el filo desenfocado del vaso
da tono 13,9–16,0° y R/G 1,35–1,44 — exactamente los números de la piel en
sombra**: esa franja se tomaba por mano y quedaba un ribete crema de 60 px
pegado al contorno. Lo que sí funciona: la piel **tiene un núcleo
inconfundible** (tono < 8°, R/G > 1,42) que el filo del vaso no tiene en ninguna
parte, y se deja crecer desde ahí hasta donde el tono sigue siendo de piel, con
la barrera en 13° y un tope de 60 px de recorrido. Con la barrera en 17° el
crecimiento se colaba por la sombra de contacto de los dedos y dejaba un halo
pálido de 40 px alrededor de la mano.

**⛔⛔ Y había un tope mal puesto en `between-s5-logo-vaso.py`.** La envoltura
cilíndrica se rendía si `W/2 >= radio`, o sea a **1 radián (57,3°)** de medio
arco, cuando el tope real es **90°**. Con el logotipo a su proporción —que en el
vaso grande abarca **131° del cilindro**— el guardia devolvía el logotipo **sin
envolver**, y se estampaba plano y más ancho que el vaso. Corregido.

**⚠️ La decisión que queda abierta: el tamaño del logotipo.** A su proporción
real el bloque va a 0,82 del alto del cuerpo, y a esa altura **el brazo ya cruza
el vaso**. En las fotos de la sesión la mano tapa parte del logotipo y se ve
natural; en una historia donde el vaso ES la marca, «COFFEE & BAR» a medias no.
Por eso hay dos versiones rendidas y elige Eli:

| | comando | proporción | costo |
|---|---|---|---|
| **A** (recomendada, es la que quedó en el asset) | `--centro 1704 3798 --ancho 1600 --radio 897` | 0,76 del ancho | 2 px de holgura con la sombra de la tapa; 22 px de tinta rozando la piel |
| **B** | `--centro 1697 3860 --ancho 2025 --radio 887` | 0,88 del ancho | la mano le come 5 149 px de tinta |

**Dónde quedó.**

- Piezas: `out/hilton-between-s5-r26/BW-S5-HumorToGo-A.png` y `-B.png`
  (2250 × 4000). QA `between-qa.py`: 2/2 limpias.
- Fondos: `raw/hilton/between/s5/r5-togo-carton.png` → `r5-togo-logoA.png` /
  `logoB.png` → `st-28-09-togo-r26a.jpg` / `r26b.jpg`.
  **El asset `public/assets/hilton/between/s5/st-28-09-togo.jpg` quedó con la A**
  (verificado por md5 contra `st-28-09-togo-r26a.jpg`).
- Scripts: `between-s5-vaso-real.py` (nuevo, con los valores de la entrega como
  defaults: corriéndolo pelado sale el mismo archivo) y
  `between-s5-revision-r26.py` (la página).
- Revisión que vio Eli:
  <https://claude.ai/code/artifact/7f9539e0-9150-4276-be8d-137b90f3c0a0>

**⛔ NO se subió al Drive.** La pieza del 28-09 está en Drive con id
`1dIH_dM4yBlM2AX5TlCE9tKMgaqlMB1wr`; hay que reemplazar su contenido
(`between-s5-subir-drive.py`) **después** de que Eli elija entre A y B.

**Abierto.**

- ⚠️ **La tapa sigue siendo la generada.** La de la pieza es mate y de plástico
  modelado; la de la sesión es brillante, con un reflejo vivo en el reborde
  enrollado. Cambiarla es rehacer geometría, no retocar superficie, y no entraba
  en «mejorar el vaso» sin volver a tocar algo ya aprobado. Es una ronda aparte.
- ⚠️ **`src/BetweenEntry.tsx` no registra las composiciones de la S5**, así que
  `between-rendir.py` no las ve. Se rinden con `npx remotion still src/index.ts
  BW-S5-HumorToGo … --scale=2.0833`. Vale la pena agregarlas al entry.
- Sigue pendiente de antes: las columnas T y U en `OK PARA DISEÑAR` desde el
  11-09, entregadas y sin visto del cliente.

## 2026-09-14 · Eli (Windows) — BETWEEN: el carrusel To Go deja de ser generado, y aparece la sesión real del vaso

**Qué se hizo.** Tres rondas sobre el **CARRUSEL PROMOS TO GO** (FEED columna L,
**22 de septiembre** — ojo, ya no es el 14: la grilla lo movió con la nota
«Intercambiemos fechas con el de cowork»). Eli las dio por **APROBADAS** y las
cuatro piezas están subidas al Drive.

**⭐⭐⭐ Lo más importante del día: llegó la sesión real del vaso To Go.** Sebastián
subió el 14-09 a las 12:17Z **39 fotos** (iPhone 16 Pro, tomadas el 09-09 16:25),
y Eli las pasó como «vasos TOGO actualizados y **aprobados por cliente**». Entraron
a **MATERIAL DE MARCA** (`1hHcwg-Z-h9OuOhM0rkc-eotuzSMpUuq9`), o sea al banco
permanente y NO a la carpeta del mes — por eso un `/al-dia` que sólo mire las
carpetas del mes no las ve; aparecieron buscando por `owner` + `modifiedTime`.

⭐⭐ **Y el hallazgo que ordena la cuenta: el vaso son TRES tamaños con siluetas
distintas.** El chico es cónico y lleva **anillo blanco en la base**; el mediano y
el grande son kraft hasta abajo, y el grande es alto y casi cilíndrico.
⛔ **`togo-vaso-real-nobg.png` —la referencia que se usó todo septiembre— es el
vaso CHICO.** Y en la ronda 2 de la ST del 28-09 se le pidió al generador «anillo
blanco en la base» como detalle de realismo: para un vaso grande eso es **falso**.
Todo escrito en `clients/hilton/CLAUDE.md § EL VASO TO GO — la sesión del 09-09`.

**Las tres rondas, y las dos primeras las corrigió Eli:**

| Ronda | Qué pidió | Cómo quedó |
|---|---|---|
| 23 | Scarlette (14-09 10:29): «cambiar la portada a alguna de las que saco el seba» + «se ven un poco opacadas las demás slides» | Portada = foto real de la entrada. Slides regradadas. **Titular en caja taupe** |
| 24 | Eli: «los textos de la portada como estaban antes… puedes añadir un degradado» + «casi mejora, necesito más luz y un poco de color» | Fuera la caja, entra `degradadoPie`. Slides con más luz y color |
| 25 | Eli: bajada «crecer un poco y subir», degradado del pie más suave, «los números se solapan» | Bajada 40→44, bloque 171→140, pie del degradado a 0,88, **caja tabular arreglada** |

**⭐⭐⭐ ESTO CIERRA CUATRO RONDAS DE LA PORTADA.** La ronda 12 había dejado escrito
que «la escena del brief NO EXISTE» —75 fotogramas de los 25 clips del cliente, ni
un plano de alguien saliendo con un vaso— y por eso las rondas 12, 15, 16 y 18 la
generaron. El cliente mandó a grabar eso: **ahora la portada es una fotografía
real en la entrada del local**, que es el fondo que venía pidiendo desde la ronda 10.

**⛔⛔ Un defecto de SISTEMA que Eli cazó mirando, y afecta a toda la marca.**
`ANCHO_CIFRA_EM_POR_PESO` estaba en el **promedio** de los diez dígitos (0,600 em
en ExtraBold) y el «0» mide **0,707**: la caja era 18 % más angosta que el glifo
más ancho y los ceros se encaballaban. Una caja tabular sólo alinea si cabe el
dígito más ancho. **Arreglado para cualquier pieza con horario o precio**, no sólo
ésta. No confundirlo con el defecto del 08-09 (el tracking que no llega al
`inline-block`): son dos cosas distintas.

**⭐⭐ Y una lección de método que me costó una ronda.** Diagnostiqué «opacadas»
como «lavadas» y bajé la mediana de 124 a 101 para pegarle al **promedio de lo
aprobado del mes**. Era la métrica equivocada: ese promedio mezcla interiores
oscuros (Cumple está en 70) con bodegones de luz natural. Faltaba **color**, no
densidad. El grupo de comparación se elige por tipo de escena, no por promedio de
la carpeta.

**Dónde quedó.**

- Piezas rendidas: `out/hilton-between-togo-r25/` (4 PNG, 2250×2812). QA 4/4 limpias.
- Scripts: `between-togo-slides-r23.py`, `between-togo-slides-r24.py`,
  `between-togo1-r23.py` — los tres leen de assets versionados.
- Sistema: props nuevos `bloqueEnCaja` (queda, aunque esta pieza ya no lo use),
  `degradadoPie`, `sizeBajada` y `anchoBajada` en `PiezaFeedBodegon`.
- Material: 39 originales en `raw/hilton/between/vasos-togo-sep2026/` (gitignored)
  y **8 tomas canónicas versionadas** en `public/assets/hilton/between/togo-sep2026/`.
- Revisión que vio Eli: <https://claude.ai/code/artifact/27435cbe-1970-405c-8731-d275ba71e4be>
- ⚠️ `out/hilton-between-r24/` **ya estaba ocupada** por el carrusel «Primero la
  foto» del 07-09; por eso los renders de hoy van en `out/hilton-between-togo-r25/`.

**⛔ La subida al Drive tuvo un tope, y va a repetirse.** Las cuatro piezas que
estaban en **C1 S4** (`1vZZGvxfiGOIrf73znO39V4aASreumkfZ`) las había subido Eli a
mano, y el token del estudio tiene scope **`drive.file`**: sólo alcanza lo que él
mismo creó, así que reemplazar su contenido devolvió **404** en las cuatro. El
conector MCP tampoco sirve (cambia el título, no el contenido).
→ Con el visto de Eli: se **renombraron** las cuatro viejas a `v1 SUPERADA - …`
(no se borraron) y se subieron las nuevas con el nombre del portal. Verificadas
byte a byte. De paso la portada dejó de llamarse `BW-F-ToGo-1.png` —el nombre del
render— y el mapa `NOMBRES` de `between-subir-drive.py` se corrigió de 14-09 a
**22-09** y de «trio» a «los tres».

**Qué sigue.**

1. **Mirar si el cliente marca la columna L.** Sigue en `EN CAMBIOS`; se lee con
   `export?format=csv&gid=1537718358` y se diffea contra
   `clients/hilton/grillas/between-septiembre-2026-vivo/gid-1537718358.csv`.
2. **Las columnas T y U de STORIES siguen en `OK PARA DISEÑAR`** desde el 11-09:
   entregadas y sin visto del cliente. No es ronda nueva, es falta de marca.
3. Cuando llegue la grilla de octubre, `/abrir between` y a producir.

**Abierto.**

- ⚠️ **La portada no muestra la cara y no tiene bolsa To Go.** El brief pide «café
  y bolsa To Go en mano» y las 18 tomas de ese bloque tienen la cabeza cortada por
  el encuadre. Eli dijo «la imagen okey», así que va — pero si el cliente lo
  levanta, la portada vuelve a necesitar imagen generada.
- ⚠️ **Los 4 archivos nuevos del Drive quedaron a nombre de `valeria@copywriters.cl`**
  (la cuenta del token), no de Eli. Para borrarlos hace falta esa cuenta.
- ⚠️ **Decisión de fondo pendiente:** o las entregas de Between se suben SIEMPRE
  con el script, o el token del estudio pasa a scope `drive` completo. Si no, este
  404 reaparece cada vez que haya que corregir una pieza subida a mano.
- Sigue pendiente de antes: pedirle al cliente **una foto real de alguien
  trabajando en el cowork**, que es lo único que aún obliga a generar una escena.

## 2026-09-11 (RONDA 3) · Eli (Windows) — BETWEEN S5: la animada aprobada, y el detalle del vaso

**La historia 2 (30-09, animada) quedó APROBADA** y no se tocó. En la 1 (28-09)
Eli pidió dos arreglos de detalle sobre el vaso; el tamaño del vaso, las
tipografías y la persona quedaron como estaban. Se reemplazó el contenido del
**mismo archivo** de Drive: el enlace no cambió.

**Lo que pidió, textual:**

> «Tienes que borrar esa línea que se ve y que el logo se vea más centrado al vaso,
> como un mockup. El logo debe verse realista que está en el vaso, como los
> originales.»

**Los tres hallazgos:**

1. ⛔ **La línea la pedí yo.** El prompt de la ronda 2 decía «una costura vertical
   del cartón» —iba en la lista de detalles físicos que arreglaron el realismo— y
   el generador la puso justo al medio, partiendo el logotipo en «BETW | EEN».
   → **Regla: a un generador, los detalles DIRECCIONALES hay que ubicarlos.**
   Sin un «al costado», van donde más estorban.
2. ⭐⭐ **«Se ve descentrado» podía no ser el logotipo.** Estaba a 50 px del eje
   (2,6 %). Lo que desbalanceaba era la línea, que partía la cara del vaso en dos
   paños desiguales. Antes de mover un elemento, mirar qué más hay en su entorno.
3. ⚠️ **El eje de un objeto ocluido se mide donde NO está ocluido.** El borde
   izquierdo del vaso lo tapa el brazo, así que el detector tomaba el fondo oscuro
   por cartón y daba un centro corrido 200 px. El eje bueno lo da **la tapa**, que
   se ve entera. Llegué a estampar sobre el valor falso antes de cazarlo.

**Lo que se hizo:**

- `scripts/between-s5-vaso-costura.py` — **script nuevo**: borra la costura fila a
  fila interpolando el cartón lateral y devolviéndole el grano. Medido: la caída de
  luminancia en esa columna pasó de −13,2 a −2,8 niveles de gris.
- `scripts/between-s5-logo-vaso.py` — opción **`--radio`**: envoltura cilíndrica
  real (el ancho del logotipo es un arco, lo que se ve es la cuerda). No contradice
  la regla del 31-08: la línea de base queda recta, el radio se mide y la
  compresión es del 8 % en el borde, progresiva.
- QA: margen 99/97, zonas seguras libres, contraste 8,7–11,8:1 — sin cambios.

**Dónde quedó:**

- `public/assets/hilton/between/s5/st-28-09-togo.jpg` — el fondo nuevo.
- `raw/hilton/between/s5/r4-togo-sin-costura.png` — la escena sin costura ni logo.
- Drive: mismo id, 9 926 928 bytes, verificado.
- Revisión (versión 3): <https://claude.ai/code/artifact/7a48f6ca-fded-4a5a-bb00-70c3046a1072>

**Qué sigue:** **septiembre de Between queda cerrado** — las 27 piezas del feed y
las 13 historias están entregadas, y las dos últimas (col T y col U de STORIES) se
subieron hoy. Lo concreto para mañana:

1. **Mirar si el cliente marcó las columnas T y U.** Se leen con
   `docs.google.com/spreadsheets/d/1wNF6qLil9qMFCGgXPlVqHBQcabfmCWWY/export?format=csv&gid=1367300884`
   y se comparan por DIFF contra
   `clients/hilton/grillas/between-septiembre-2026-vivo/gid-1367300884.csv`. La
   del 30 ya está aprobada por Eli; falta el visto del cliente y el de la del 28.
2. **Si vuelve corregida la del 28**, la escena sin costura ni logotipo está en
   `raw/hilton/between/s5/r4-togo-sin-costura.png`: se re-estampa y listo, no hay
   que volver a generar.
3. **Cuando llegue la grilla de octubre**, `/abrir between` y a producir.

**Abierto:** lo mismo de la ronda 2 — el video sin audio, el corte de línea del
titular del 28-09, la chica generada y el falso positivo de `between-qa.py`.
Y sigue pendiente **pedirle al cliente una foto real de alguien trabajando en el
cowork**, que es lo único que aún obliga a generar una escena.

## 2026-09-11 (RONDA 2) · Eli (Windows) — BETWEEN S5: aparece el plato real y el vaso deja de parecer maqueta

Eli mandó **dos sesiones de fotos** y con eso cayeron los dos puntos débiles de la
entrega de la mañana. Las dos piezas se rehicieron y se **reemplazó el contenido
de los mismos archivos de Drive**: el enlace no cambió.

**Lo que pidió, textual:**

> «en esta carpeta puedes encontrar platos de Between […] creo que acá puedes
> encontrar referente del plato o el mismo plato. Para la historia del vaso togo
> estática el vaso se ve muy falso y mal el logo. Hazlo más realista y acerca más
> a la chica y el vaso, para que el fondo pase a 2do plano.»

**Lo que se hizo:**

1. **30-09 · el plato ahora es el de Between.** `Between-131` a `143` de la
   sesión de platos: plato BLANCO, carne braseada en salsa de vino, puré con
   ciboulette, hojas verdes y rábano. Se le pidió al generador cambiar **sólo el
   plato** y dejar idéntica la escena aprobada. La diagramación no se movió.
2. **28-09 · el vaso se rehizo tres veces.** Realismo del cartón (con la foto del
   vaso vigente de cerca), plano cerrado con el fondo desenfocado, y una vuelta
   más para devolverle sitio al titular.
3. **El logotipo pasó de 133 a 274 px** y se movió a la franja entre la tapa y el
   brazo.
4. Página de revisión actualizada **en la misma dirección** (versión 2).

**Los tres hallazgos, y el primero duele:**

1. ⛔⛔ **LA FOTO DE LA PLATEADA EXISTÍA Y SE DIO POR INEXISTENTE.** En la mañana
   se concluyó que Between no la tenía y se usó la de **QB**, que es otro plato
   (loza de borde turquesa, champiñones). La causa: se miraron los **31 archivos
   de la raíz** de `raw/hilton/between/platos-ene/` y no las **202 miniaturas**
   de esa misma carpeta, que son la sesión completa. Los platos de almuerzo
   empiezan en la `76`.
   → **Regla nueva: antes de decir «no hay foto», hoja de contacto de la sesión
   ENTERA, miniaturas incluidas.** `scripts/hoja-contacto.py` tarda un minuto.
2. ⭐ **«Se ve falso» es una lista de piezas que faltan, no un ajuste de
   realismo.** El vaso real tiene seis cosas que el generado no tenía: cartón
   crema (no anaranjado), fibra y motas, borde enrollado, costura vertical,
   anillo blanco en la base y nervaduras en la tapa. Hay que **nombrarlas una por
   una** en el prompt; «cartón kraft realista» no alcanza.
3. ⭐⭐ **Acercar la cámara le quita sitio al titular.** Con el plano cerrado la
   banda limpia se desplomó de y=879 a **y=443** y el texto no cabía. La solución
   no es alejar —eso deshace lo pedido— sino **subir el encuadre**: el vaso baja
   dentro del cuadro y la banda vuelve a y=960. El vaso sigue igual de cerca.
   Corolario: **el logotipo del producto también tiene zona segura** — a su altura
   natural quedaba bajo la barra de Instagram.

**Dónde quedó:**

- `src/compositions/hilton/BetweenStS5.tsx` — cabecera con la ronda 2 escrita.
  **Los componentes no se tocaron:** sólo cambiaron las dos fotografías.
- `public/assets/hilton/between/s5/` — los dos fondos nuevos (`st-28-09-togo.jpg`
  con el logotipo ya estampado, `st-30-09-plateada.mp4`).
- `raw/hilton/between/plateada-real/` — `bw-135`, `bw-138` y `bw-141`, las tres
  fotos reales del plato.
- Drive: mismos ids, bytes nuevos, verificado por `fileSize` y `modifiedTime`.
- Revisión: <https://claude.ai/code/artifact/7a48f6ca-fded-4a5a-bb00-70c3046a1072>

**Abierto:**

- ⚠️ El video sigue **sin audio**: la grilla no lo pide y no hay pista aprobada.
- ⚠️ El corte de línea del titular del 28-09 respeta las dos líneas del brief, lo
  que deja el cuerpo bajo el token de 117. Si Eli lo quiere más grande, se rompe
  en tres líneas.
- ⚠️ La chica del 28-09 sigue siendo **generada**. No se le ve la cara, así que la
  pieza queda fuera del asunto de los rostros; si Eli prefiere una modelo de la
  sesión real, hay que elegir el fotograma.
- ⚠️ `between-qa.py` sigue con el falso positivo — van nueve piezas.

## 2026-09-11 · Eli (Windows) — NO es sesión de diseño: se cerró el hueco de material de DT y Hilton por fin tiene ficha

Verificación del estudio (`/arranque`) en el Windows de Eli. **No se tocó ninguna
pieza de ninguna de las 4 marcas.** Se anota acá porque deja resuelto lo que el
CIERRE 2 de ayer había dejado abierto en DT, y porque aparece un pendiente de
Between que no es de esta sesión.

**Qué se hizo:**

1. **Los 5 archivos de `raw/hilton/dt/` quedaron resueltos, y eran DOS problemas
   distintos, no uno.**
   · **El TIFF del lobby no estaba roto** (ya lo decía el CIERRE 2) pero sí era
     inservible para rendir: **Chrome no carga TIFF**, o sea el mismo modo de falla
     silencioso de Brushwell. Se conservó el original como
     `03-lobby-02.tif` y se generó `03-lobby-02.jpg` (4192x3104, calidad 95,
     6,2 MB) que Chrome sí carga.
   · **Los otros 4 eran HTML de login**, confirmado. Se renombraron a
     `*.DESCARGA-FALLIDA.html` — **no se borraron**: quedan visibles por lo que son
     y la compuerta deja de contarlos como imagen rota.

2. **⭐ El hueco de fotos NO existía, y por eso no hay nada que pedirle al cliente.**
   Antes de declarar material faltante se aplicó la memoria
   `agotar-material-antes-de-bloquear`: hoja de contacto de las 109 fotos de
   `sesion-real/` y se miró.
   · `ref-dia-turismo.jpg` **tenía su `.png` sano al lado**, misma imagen 1080x1350.
   · Los 3 de `banco-maestro/` (`businesscenter`, `exterior2`, `fachada156`) tienen
     nombre de galería web, no de la sesión (que son `_MG_####`). **Lo que prometían
     ya está cubierto por las 96 fotos sanas de `muestra/` y `muestra2/`**: frontis
     (`alta/HDT_43-frontis.jpg`), exterior, y los salones de reuniones completos con
     montaje y proyector, que es el «business center». Se dejó un `LEEME.txt` en
     `banco-maestro/` explicando dónde está cada cosa para que nadie los persiga de
     nuevo.
   · `python scripts/verificar-material.py raw/hilton` → **1858 válidos, 0 rotos.**

3. **⭐⭐ Hilton ya tiene `clients/hilton/marca.json`, y el motivo importa.**
   `scripts/verificar-fuentes.py` recorre `clients/*/marca.json`: al no existir la
   ficha, **se saltaba Hilton entero y su informe decía «todo bien» sin haber mirado
   ni una fuente de DT ni de Between**. Ahora las 4 salen verificadas:
   **Stag · Trade Gothic · Raleway · Brushwell**.
   · La ficha declara **sólo tipografías, a propósito**. Colores, formatos y zonas
     seguras se dejaron FUERA porque no están medidos y escribirlos de memoria sería
     inventarle un sistema a la marca (memoria `no-inventar-sistema-de-marca`).
   · Se anotó en la ficha que **las dos Trade ya tienen su `.woff2`** — eso está
     comprobado. Lo que **NO** está comprobado es que Chrome los cargue: falta correr
     `document.fonts.check` sobre una pieza real. En código se carga el `.woff2` y
     nunca el `.otf` CFF, y la primera pieza de DT que se rinda se mira al 100 %.
   · **Trampa cazada:** al declarar los 3 cortes que sólo tiene el cliente (Stag LCG
     y los dos Trade Bold), el script los leyó como declarados y les puso **✓ verde
     falso**. Un falso ✓ es peor que no tener el dato. Se renombró la clave a
     `_cortes_que_solo_tiene_el_cliente_NO_LEER_COMO_DISPONIBLES` y quedan sólo como
     texto en `pendientes`.

**Dónde quedó.** Nada rendido y nada entregado. Lo único versionable es
`clients/hilton/marca.json`; lo de `raw/` va en `.gitignore` de todas formas.
`doctor.sh` cierra con **2379 archivos válidos, 0 rotos** y TypeScript limpio.

**Qué sigue.** DT ya no tiene excusa de material: la próxima sesión entra directo a
**la ronda nueva del cliente en DT** que sigue abierta desde el `/al-dia` del 10-09.

**Abierto.**
- ⚠️ **`scripts/between-s5-logo-vaso.py` estaba sin commitear** (creado hoy 11:42,
  antes de esta sesión). Es la rotación rígida del logotipo sobre el vaso To Go
  inclinado de la ST del 28-09 (S5). Compila limpio y usa
  `public/assets/hilton/between/logo-negro.png`, que ya está en el repo. **Se
  commitea hoy por la regla `el-render-vuelve-al-repo`, pero esta sesión NO trabajó
  Between: en qué ronda va esa ST y si se entregó lo confirma Eli.**
- Sigue pendiente la **ronda nueva del cliente en DT** (viene del 10-09).
- Faltan por pedir al cliente: **Stag LCG**, **Trade Gothic LT Std Bold de ancho
  normal** (el del bloque de precio) y **Trade Gothic Next LT Pro Bold**.

---

## 2026-09-11 · Eli (Windows) — BETWEEN S5: las dos últimas historias, y septiembre queda cerrado

Sesión de Between. Se produjeron las **columnas T y U** de la hoja STORIES —lo
único que le quedaba a la cuenta— y con eso **la grilla de septiembre de Between
no tiene ninguna columna sin producir**, ni en STORIES ni en FEED.

**Qué se hizo:**

1. **La grilla se leyó VIVA por CSV** (`export?format=csv&gid=1367300884`), no del
   `.xlsx` congelado. Col T: `ST ESTÁTICA – HUMOR | CAFÉ TO GO`. Col U:
   `ST ESTÁTICA – ANIMADA | PLATEADA AL CARMENERE`, con `INTERACCIÓN: LINK CARTA`.
   Las dos en `OK PARA DISEÑAR`.
2. **Se descubrió que las dos YA ESTABAN en Drive**, del lote de 27 del 27-08, y
   que nunca pasaron por ninguna de las 13 rondas posteriores. Estaban congeladas
   en el sistema de agosto: vaso sin logotipo, escenario que no es Between, plato
   inventado, y la col U como PNG cuando la grilla la pide animada. Se rehicieron
   las dos.
3. **Se abrió un espacio de Magnific para la semana** con las 5 referencias reales
   adentro, y ahí quedaron las 8 escenas generadas y el video:
   <https://www.magnific.com/app/spaces/a2b896f3-0597-4ff7-9bcf-2a2d772324de>
4. **Subidas a `S5 · BW · STS`** (`1r_spPoBx-vR63J8GTRVCUkbZGGyNLnJg`), verificadas
   por `fileSize` y `parentId`.
5. **La revisión se publicó como página**, no como archivo local:
   <https://claude.ai/code/artifact/7a48f6ca-fded-4a5a-bb00-70c3046a1072>

**Dónde quedó:**

- `src/compositions/hilton/BetweenStS5.tsx` — las dos piezas, con la medición
  escrita en la cabecera. Registradas en `src/Root.tsx` como `BW-S5-HumorToGo`,
  `BW-S5-Plateada` y sus dos `-Guia`.
- `scripts/between-s5-logo-vaso.py` — **script nuevo**: estampa el logotipo real
  sobre un vaso INCLINADO con rotación rígida. `between-logo-vaso.py` no rota y el
  vaso de esta pieza va tumbado 27°.
- `scripts/between-s5-subir-drive.py` — **script nuevo**: el de siempre sólo mira
  `*.png` y acá una de las dos piezas es un MP4.
- `scripts/between-st-s5-generar.md` — los prompts textuales y las tres vueltas.
- Material versionado: `public/assets/hilton/between/s5/` (la foto del To Go con
  el logotipo ya estampado y el MP4 de fondo) y `raw/hilton/between/s5/` (las 8
  escenas generadas, incluidas las descartadas), más
  `raw/hilton/between/refs-s5/` (lo que dejó contenido) y
  `raw/hilton/between/plateada-real/`.
- `clients/hilton/CLAUDE.md` — sección nueva de la S5 y la tabla de estado al día.

**Los tres hallazgos de la sesión:**

1. ⭐⭐ **El muro de Between es oscuro y el generador lo aclara solo.** Las dos
   primeras vueltas de las DOS piezas se perdieron por eso: el beige daba 1,3–1,9:1
   contra el 8–15:1 de las piezas aprobadas. Se arregla pidiendo la penumbra en el
   tercio superior dentro del prompt, no con multiply.
2. ⭐⭐ **En una historia animada la geometría no es una, son 270.** La zona del
   sticker y el contraste hay que medirlos en el ÚLTIMO fotograma: con el
   acercamiento el corredor libre se encogió de ~300 px a 175 px.
3. ⭐ **El vaso se pide liso siempre.** No hay prompt fiable para la `Ǝ` invertida:
   en dos vueltas Nano Banana escribió un «BETWEEN» inventado en una sans
   cualquiera. Se estampa el archivo oficial.

**Abierto:**

- ⚠️ **Falta una foto real de la Plateada al Carmenere de Between.** No existe en
  ninguna carpeta de la marca. La referencia que se usó es
  `Quotidien-176.jpg res al carmenere`, de la sesión de platos de **QB**. El plato
  llega fiel y la escena se reambientó en la mesa de teca de Between, pero la foto
  no es de Between y **está informado en la página de revisión**. Vale la pena
  pedírsela al cliente.
- ⚠️ **El video va sin audio a propósito**: la grilla no lo pide y no hay pista
  aprobada para Between. Si Eli quiere música, se monta sin cambiar la duración.
- ⚠️ **`between-qa.py` sigue con el falso positivo, van ocho piezas.** Acá contó
  como texto el filo del cuchillo y el brillo de la loza. La medición de esta
  entrega se hizo aislando la gráfica a mano.
- El corte de línea del titular del 28-09 respeta las dos líneas del brief, lo que
  deja el cuerpo bajo el token de 117. Si Eli lo quiere más grande, se rompe en
  tres líneas: es una línea de código.

## 2026-09-10 (CIERRE 3 · noche) · Eli (Windows) — BETWEEN: la ST del Cowork pasa de generada a real, en 4 rondas

Sesión de Between (las dos anteriores del día fueron de DT). Arrancó con
`/abrir between` y cerró con la pieza subida y una página de revisión publicada.

**Qué se hizo:**

1. **`/al-dia` destapó por qué el archivo iba atrás de la realidad** — ver
   «Abierto», es el hallazgo de método de la sesión y **cierra el misterio que
   quedó abierto anoche**.
2. **La ST del Cowork (STORIES col N, 16-09) se rehízo cuatro veces** por pedido
   del cliente y de Eli, hasta quedar aprobada la base y ajustada dos veces más:
   · **ronda 10** — Scarlette Muñoz, comentario nativo de las 12:55 sobre
     `STORIES!N`: «podemos cambiar la imagen a una real de cowork?». La foto que
     salía era una escena **enteramente generada** y no era Between;
   · **ronda 11** — Eli: «el montaje está mal logrado». Se acabó pegar el vaso a
     mano; la escena se produce entera con IA sobre la foto real;
   · **ronda 12** — Eli: el vaso To Go pasa a **taza blanca de cappuccino**;
   · **ronda 13** — Eli: vuelve el **sándwich de jamón y queso** de la versión
     aprobada y la taza se separa del plato «un poco muy sutil».
3. **La revisión se publica como página**, no como archivo local (memoria
   `antes-y-despues-en-html`): <https://claude.ai/code/artifact/0c5e87e2-4a2f-448a-994e-ff7b2453ef92>
   — va por la versión 4 y la dirección no cambia.

**Dónde quedó:**

- `src/compositions/hilton/BetweenStS3.tsx` — las cuatro rondas escritas en la
  cabecera de la pieza. Componente nuevo **`LogoBeigeMarca`** (el lockup café se
  cae a 1,80:1 sobre el cielo gris de la foto real); `LogoCafeMarca` quedó
  huérfano y se removió, `LOGO_CAFE` sigue en uso por la pieza del 18.
- Fondos versionados, **el histórico completo** en
  `public/assets/hilton/between/st-s3/`: `st-16-09-cowork.jpg` (generado) ·
  `-real.jpg` (foto sola) · `-real-vaso.jpg` y `-real-laptop.jpg` (los montajes
  descartados) · **`-escena.jpg`** (el entregado).
- Scripts nuevos: **`between-cowork-escena-ia.py`** (el que produce la escena),
  `between-cowork-laptop-ia.py`, `between-cowork-r10-html.py` y
  `between-cowork-r10-artifact.py`.
- Instantánea **viva** de las cuatro pestañas de la grilla en
  `clients/hilton/grillas/between-septiembre-2026-vivo/` — **ésa es la base del
  próximo diff**, no el `.md` hecho sobre el blob.
- **Subida a `S3 HILTON SEP 2026/BW/STORIES`** reemplazando el **mismo archivo**
  `1lAgqPkkA25L4VRlnIg9UayWPdZxDuqwk`: **el enlace no cambió**. Última versión
  **7 212 471 B**, 2250 × 4000 a 150 ppp, verificada por `fileSize` y `parentId`.
- Las otras dos de la S3 **no se tocaron**: 8 077 154 B y 7 249 755 B.
- Comprobado con `cmp` en cada ronda: **reproduce byte a byte**.
- `clients/hilton/CLAUDE.md` — cuatro secciones nuevas (rondas 10 a 13).

**Qué sigue:**

1. **Producir la col T (28-09, Humor To Go) y la col U (30-09, Plateada al
   Carmenere)**, las dos en `OK PARA DISEÑAR`. Es lo único de Between sin hacer:
   el FEED está entero `YA POSTEADO` / `APROBADO` / `CORREGIDO`.
2. **Arreglar `between-qa.py`.** Van **siete piezas seguidas** con el mismo falso
   positivo: cuenta como texto cualquier blanco de marca con un borde oscuro
   cerca — el foco del cielo, el brillo del muro de listones y ahora la loza del
   plato. Hay que darle una forma de distinguir un brillo de foto de un trazo de
   letra. Eli ya sabe que está pendiente.
3. Confirmar si el cliente marca la N ahora que volvió corregida, y si la O
   (18-09, `EN REVISIÓN`) se cierra.

**Abierto:**

- ⭐⭐⭐ **EL `.xlsx` DE LA GRILLA DE BETWEEN ESTÁ CONGELADO, Y LA GRILLA VIVA SE
  LEE POR CSV.** Es la respuesta al misterio de anoche. `uc?export=download`
  devuelve el **blob subido**, que Google deja de reescribir: hoy bajó con el
  **md5 idéntico** al del 09-09 con el `modifiedTime` movido a las 19:12Z. La capa
  viva se lee con
  `docs.google.com/spreadsheets/d/<id>/export?format=csv&gid=<gid>`, y los `gid`
  salen de `<id>/htmlview` (la página `/edit` no los trae). Los de Between: FEED
  `1537718358`, STORIES `1367300884`, ORGÁNICOS `1543656935`, mensual `688659470`.
  **La prueba de que el blob miente:** su vista mensual dice «AGOSTO» y la viva
  dice «SEPT». ⛔ Queda **invalidada** la nota del 09-09 «si el md5 coincide, no
  hay ronda». ⚠️ Y el comentario **nativo** tampoco sale en el CSV: ése se lee con
  `read_file_content` del conector MCP con `includeComments=true`. Son **tres**
  fuentes, no dos.
- ⭐⭐ **SE CIERRAN LOS DOS PENDIENTES QUE ARRASTRABA LA CUENTA.** STORIES col G
  (**reel Café Bombón**) y col D (**ST café de regalo**) pasaron de `EN CAMBIOS` a
  **`APROBADO`**. El Café Bombón venía anotado como bloqueante desde el 09-09 («no
  existe composición», «nadie anotó cuál de los tres caminos para la leche
  condensada se aceptó») y Eli había dicho «ya lo dejé corregido»: **el cliente lo
  aprobó, así que su corrección existió y no hay que rehacerlo**.
  `PROPUESTA-reel-cafe-bombon.md` deja de estar en pie.
- ⚠️ **Material que sigue faltando: una foto real de alguien trabajando en el
  cowork.** El brief pide «notebook abierto + café Between + libreta» y el cliente
  no tiene ningún notebook fotografiado ahí — los únicos fotogramas con notebook
  son del **lounge del hotel**, con caras reconocibles y en otro espacio. Con esa
  foto la pieza dejaría de necesitar el paso de IA. Vale la pena pedírsela.
- ⚠️ **Hay una variante ofrecida y sin decidir:** la misma escena con el hueco
  entre plato y taza más ancho (754 px contra los 481 de la entregada). Está en la
  página de revisión; si Eli la prefiere, cambiarla es una línea.
- Siguen de los cierres anteriores: Between **sin `clients/hilton/reglas.yaml`**
  (así que `qa/motor.py --marca hilton` no corre), las **`GUIA CM`** en local sin
  decidir cómo llegan al CM, y **`BETWEEN.logo.cafe` apuntando a un PNG negro**.
- ⛔ Y sigue en pie: **`BetweenCumple.tsx:112` y `BetweenSeptiembre.tsx:794` con el
  legal VIEJO** del cumpleaños.

---

## 2026-09-10 (CIERRE 2) · Eli (Windows) — NO es sesión de diseño: 5 archivos de DT no sirven para producir

**Qué se hizo.** Verificación del estudio en el Windows de Eli (`/arranque`). **No
se tocó ninguna pieza de Hilton.** Se anota acá sólo porque la compuerta de
material encontró **5 archivos de `raw/hilton/dt/` que no se pueden usar**, y
quien abra DT mañana se topa con ellos.

**⛔ Cuatro nunca se bajaron — son la pantalla de login de Google.** Pesan ~908 KB
cada uno y empiezan con `<!doctype html>` apuntando a `accounts.google.com/v3/signin`.
Es exactamente el patrón de la memoria `compuerta-de-material`: el enlace de Drive
devolvió el login en vez del archivo y `curl` lo guardó igual, con nombre de foto.

| Archivo | Qué es de verdad |
|---|---|
| `dt/ref-s4/ref-dia-turismo.jpg` | HTML de login |
| `dt/sesion-real/banco-maestro/businesscenter.jpg` | HTML de login |
| `dt/sesion-real/banco-maestro/exterior2.jpg` | HTML de login |
| `dt/sesion-real/banco-maestro/fachada156.jpg` | HTML de login |
| `dt/moodboard-refs/03-lobby/03-lobby-02.jpg` | **TIFF válido** 4192×3104 RGB, mal nombrado |

**⭐ El quinto NO está roto y el diagnóstico se equivocó.** `doctor.sh` lo reportó
como «desconocido, no una imagen»: es un **TIFF RGB de 4192×3104** con extensión
`.jpg`. La foto está entera. Pero **Chrome no carga TIFF**, así que tampoco sirve
para una composición tal cual — hay que convertirlo antes de usarlo, no volver a
bajarlo.

**Dónde quedó.** Nada rendido y nada tocado en `raw/` (va en `.gitignore` de todas
formas). Los tres de `banco-maestro/` son del banco maestro de la sesión real, así
que el hueco es de fotos de producción, no de referencias sueltas.

**Qué sigue.** Antes de la próxima pieza de DT: volver a bajar los cuatro del Drive
con el método que sí funciona (`curl uc?export=download`, memoria
`bajar-grilla-ajena-de-drive`), y convertir el TIFF del lobby a JPG. Después
`python3 scripts/verificar-material.py raw/hilton` tiene que salir limpio.

**Abierto.** Sigue pendiente la **ronda nueva del cliente en DT** que encontró el
`/al-dia` de la mañana (ver CIERRE 1 de hoy) — no se tocó en esta sesión.

---

## 2026-09-10 (CIERRE 1) · Eli (Windows) — DOUBLETREE: la ST del Día del Turismo APROBADA y subida, y el manual pierde la razón de cuerpos

**Qué se hizo.** Se cerró la historia del **Día del Turismo** (STORIES col K,
27-09) en **tres rondas más** sobre la que se había entregado anoche: la 4, la 5
y la 6. **Aprobada y subida** al mismo archivo de Drive, así que el enlace no
cambió. Y de paso el `/al-dia` de la mañana encontró **ronda nueva del cliente**
en DT, que queda para la próxima sesión.

**⭐ La ronda 4 — «la línea de una esquina a la otra».** Eli marcó el PNG en rojo:
la línea de canto a canto como la referencia, el texto más chico más grande, y
todo más arriba. Se volvió a **medir el pin** en vez de ajustar a ojo, y ahí
estaban las tres respuestas:

| | La referencia | Lo entregado | Corregido |
|---|---|---|---|
| Arranque del bloque | 35,6 % de la altura | **48,5 %** | 36,6 % |
| Horizontales del marco | **salen del lienzo** | 800 px centradas | de canto a canto |
| Nivel más chico | ≈30 px de mayúscula | 27 px (cuerpo 38) | 32 px (cuerpo 46) |

· **La causa del «están muy abajo» era de código, no de gusto:** el texto iba
  `justifyContent: center` dentro de un marco de 880 de alto, así que se hundía
  hasta la mitad. Ahora se ancla arriba con el aire medido del pin (razón
  arriba/abajo 0,68 contra su 0,64).
· **El marco de la referencia SANGRA.** Ampliadas las cuatro esquinas al 200 %,
  su borde inferior se va fuera del lienzo por los dos lados. Se rindieron **dos
  lecturas** del pedido y Eli eligió: **A, dos escuadras opuestas**, cada
  horizontal naciendo en una esquina redondeada y muriendo en el canto. La B
  (sólo las dos horizontales) se **retiró del repo y del disco** — dejarla
  registrada es dejar a mano la pieza que no se entrega.
· ⛔ **El titular NO creció**, y es a propósito: ya iba más ancho que el del pin
  (55 % contra 51 %). Lo que estaba mal era su altura.

**⭐⭐ La ronda 5 — el velo, y un defecto que introdujo el propio arreglo.** Subir
el texto lo sacó de la zona velada y lo puso sobre la punta dorada del edificio:
medido por tercios, **«¡Feliz Día» quedaba en 2,14:1 y no se leía**. O sea que
cumplir el pedido sin más rompía la pieza. Se subió la rampa del velo, y Eli
respondió: **«baja la opacidad arriba, se ve muy forzado; la transparencia debe
ser de 0 arriba y ajustar»**. Tenía razón y el defecto era mío: la rampa se
quedaba PLANA en 0 hasta el 21 % y de ahí saltaba a 0,44 — **ese codo es una
banda visible**, el velo «empezaba» en un punto en vez de nacer. Ahora arranca en
**0 en el borde** y sube cóncava con paradas cada ~10 %.

⭐ Y quedó con **menos** velo que antes donde importa: en la banda del titular
bajó de 0,538 a **0,399**, y en el pie de 0,66 a **0,58**. Se ve más foto.

**⚠️⚠️ La ronda 6 — LEÍ MAL EL PEDIDO Y HAY QUE NO REPETIRLO.** Eli pidió que
«¡Feliz Día» tuviera **«el mismo peso»** que «del Turismo», y se leyó como
GROSOR: se le bajó el corte a Light. Ella corrigió: **«me refería al tamaño de la
tipografía, no a cambiar el grosor»**. Corregido en los dos sentidos — cuerpo
80 → **130** (igual al de abajo) y grosor de vuelta a **Medium**, como ella lo
había dejado en la ronda 3. Al mismo cuerpo lo que distingue las dos líneas es el
largo de la frase: «¡Feliz Día» da **514 px** y «del Turismo!» **742**, con 143
px de holgura en los 800 útiles del marco.

**⭐ Y ESO CAMBIÓ EL MANUAL — con un paso en falso que quedó anotado.** El manual
decía que el titular de DT va a **dos pesos** (medido en `C1 FT N1`) y que la
razón de cuerpos es **1,62** (58 / 94). Lo que vale ahora:
· **los dos pesos SIGUEN** (Medium arriba, Light abajo) — ése es el recurso;
· **la razón de cuerpos YA NO RIGE**: las dos líneas miden lo mismo.
En la ronda 5 se había escrito **al revés** (que se iban los pesos y quedaba la
diferencia de cuerpo) y se corrigió en los dos lugares del manual. ⚠️ Con la
advertencia al lado: `C1 FT N1` es una pieza de **Family Time**, así que si
aparece una pieza nueva de esa campaña **hay que preguntarle a Eli** si el
criterio del cuerpo único la alcanza o si es sólo de las historias.

**⚠️ Y una regla técnica nueva, que salió de medir:** el contraste del titular
**subió de 3,61 a 3,76:1 al volver a Medium**, porque el trazo grueso lleva más
tinta. Por eso: **el grosor NO se toca para arreglar legibilidad** — afinarlo
cuesta contraste. Si hace falta, se resuelve con el velo o con el color.

**El techo de esta toma, medido y aceptado.** El titular vive en el 36-46 % de la
altura, o sea sobre lo más claro de la foto, y con el velo naciendo en cero no se
puede cargar esa banda sin volver a forzar arriba. Quedó en **3,76:1**: pasa,
porque a cuerpo 130 es **texto grande** y ahí la vara es **3:1, no 4,5** (se
venía exigiendo la de texto chico). Se agotaron las dos salidas antes de
aceptarlo: con rampa lineal **ni el pie totalmente opaco pasa de 3,43:1**, y
barridos los **25 encuadres 9:16 posibles** de `HDT_43` el mejor deja el titular
en **2,60:1 sin velo** — no hay ventana donde caiga sobre zona oscura, el
edificio no llega tan arriba. ⭐ **La vía del sistema, si algún día se quiere
margen de sobra: el titular en AZUL DT como el logotipo (§B.4), que sobre este
cielo mide 9:1 sin nada de velo.** No se hizo porque nadie lo pidió.

**⚠️ El QA se acusó a sí mismo por TERCERA vez.** Sus bandas de tinta estaban
fijas en las filas de la ronda anterior, así que al subir el texto reportó «sin
tinta» en las cuatro líneas **más una falsa sustitución de fuente**. Era el QA,
no la pieza: reapuntadas, las huellas salen correctas (Stag Light r=+0,84 contra
0,35 del mejor señuelo; Stag Medium r=+0,80 contra 0,53). Quedó escrito en
`scripts/dt-qa.py`: **las bandas se re-miden en cada ronda que mueva el texto, y
el QA se corre DESPUÉS de eso, nunca antes.**

**Dónde quedó.** Subida y **verificada contra Drive**:
[DT ST 27-09 Dia del Turismo.png](https://drive.google.com/file/d/12bBQuWsgPsNu8xZ0C1CL_l-0CScGeyuZ/view)
— `parentId` = `1dB-uwVA2Xdhxl0olsc2SMn6KMZ4J_h8E`, o sea **STS de la S4 de DT** y
no «Mi unidad»; 11 803 167 B, 2250×4000, 150 ppp. Es el **mismo archivo** de
anoche, reemplazado: **el enlace no cambió**. Reproducible desde el repo — el
script, la foto (`public/assets/hilton/dt/st-turismo-frontis.jpg`), las fuentes y
el logotipo están todos versionados, y `cmp` dio idéntico byte a byte.
Commits: `422d5f8` (r4), `b4cebd4` (r5), `507dc96` (r6).

**⭐ Cómo se revisa una ronda desde ahora.** Eli pidió, con «siempre», que el
antes/después se entregue **en HTML** y no como lámina en el chat: ella aprueba
mirando y comparado. La página de esta pieza (cortina antes/después, guías de
altura y canto, la referencia al lado y las mediciones abajo) quedó publicada, y
la preferencia está en la memoria como `antes-y-despues-en-html`.

**Qué sigue — RONDA NUEVA DEL CLIENTE, encontrada hoy por el `/al-dia`.**
Confirmada por **diff de contenido** contra la instantánea de anoche (el
`modifiedTime` se movió y el tamaño del blob bajó de 93 a 66 MB sin significar
nada: la grilla es nativa de Sheets):

1. ⛔ **FEED col I — OPINIÓN BOOKING del 14-09: `OK PARA DISEÑO` → `EN REVISIÓN`**,
   y con ella un **hilo nativo NUEVO y OPEN** (`AAACGzJtEYc`, anclado en
   `FEED!I14`, de Carlos hoy 12:24:19Z): «*@elisabet.soto holaaa, podemos agregar
   la bandera de Panamá a la reseña?*» — **sin responder, y la pieza publica en 4
   días.** El material ya está decidido en la celda («Ok el que sugiere Carlos» →
   `imagen_2026-08-14_112424991.png`). ⚠️ La carpeta de referencias
   (`1Dlki995RRdwueFGlZOkF9rybf7maMJ5u`) **sigue devolviendo vacía**.
2. ⭐ **FEED col K — 23-09: el reel se volvió ESTÁTICO y YA ES DISEÑABLE.** Era
   «REEL - HILTON HONORS formato POV», frenado desde el 13-08 por Scarlette
   (grabar con material propio en la 2da jornada, coordinar con Sebastián
   Serrano), y ahora es **«ESTÁTICO HILTON HONORS, TODOS LOS BENEFICIOS»** con
   brief completo (foto real a sangre, caja translúcida de 6 cuadrantes con
   iconos, footer «Inscríbete gratis en el link de la bio»), copy nuevo entero y
   la referencia cambiada de TikTok a Pinterest. Comentario de la celda: «*este
   que mejor sea un estático, ya hicimos reel hace poco (guardemos la idea de
   todas formas)*». **El bloqueo era de formato y desapareció.** ⚠️ El hilo de
   Scarlette (`AAACB_tY1w4`, `FEED!K10`) sigue marcado OPEN pero quedó
   **obsoleto**: ya no hay reel que grabar.
3. ⚠️ **STORIES col J — ESCAPADA ROMÁNTICA del 21-09: `EN CAMBIOS` → `CORREGIDA`**
   y el hilo de los **AD ONS** (`AAACGx-K8dA`) pasó de OPEN a **RESOLVED — pero
   se cerró SIN CONTESTAR.** Nadie respondió el «no entiendo qué es AD ONS» de
   Eli, el comentario de la celda está **intacto palabra por palabra** y el brief
   **sigue diciendo $109.000** cuando la pieza entregada ya dice $99.000. O sea
   se movió el estado, no el brief. **No se inventa** (§G): hay que preguntarle a
   Carlos si la pieza se cierra tal como está entregada o si los AD ONS entran.

**Abierto.**
- ⛔ **La bandera de Panamá** (punto 1) — es la tarea más urgente por fecha.
- ⛔ **Los AD ONS** (punto 3) — bloqueante de contenido, no de diseño.
- **¿El criterio del cuerpo único alcanza a Family Time?** — preguntarle a Eli.
- Siguen frenadas **las tres fuentes** que sólo tiene el cliente (Stag LCG, Trade
  Gothic LT Std Bold, Trade Gothic Next LT Pro Bold) y **la carpeta de la reseña
  del 14-09**.
- Sin respuesta por **cuarta** vez: ¿`reglas.yaml` entra con la geometría de DT, o
  primero los dos checks nuevos de `qa/checks.py`?
- **PISO18** tuvo ronda menor hoy y **no pide trabajo de diseño**: FEED col F
  (10-09, fotos de novios) pasó a `CORREGIDO`, un comentario quedó tachado y una
  etiqueta de semana cambió. **Cero hilos nativos OPEN** en esa grilla.

---

## 2026-09-09 (CIERRE 6 · noche) · Eli (Windows) — DOUBLETREE: la historia del Día del Turismo, y DT deja de no tener sistema

**Qué se hizo.** Se **diseñó y entregó la última historia de la S4**, `ESTÁTICA ·
DÍA DEL TURISMO` (STORIES col K, 27-09, estado `OK PARA DISEÑO`, sin comentarios
para diseño). Eli pidió guiarse de la referencia que ella misma dejó en
`REFERENCIAS S4 DT` pero con los lineamientos de DT. Salió en **tres rondas**, las
tres con marcas de ella. Y para poder hacerla hubo que **medir la geometría de DT
y escribirle un kit de código**, que era el pendiente que arrastraban los tres
cierres anteriores del día.

**Antes de diseñar, el `/al-dia` encontró ronda del cliente en la grilla** — y esta
vez el blob sí la traía. Ver el detalle en `clients/_estado-sync.json`; en corto:
**STORIES J16 pasó de `REVISAR CONTENIDO` a `EN CAMBIOS`** (la Escapada Romántica
del 21-09, la que estaba frenada por §G), y **desapareció del archivo el GIF de la
pieza ya entregada**. Se rescató del xlsx viejo antes de perderla
(`raw/hilton/dt/recuperado/`) y al abrirla apareció lo importante: **ya decía
`$99.000`**, o sea que la corrección de precio estaba hecha y la que quedó atrás
es la grilla, no la pieza.

**La pieza, y las decisiones que la sostienen:**

- **Foto real del cliente, nada generado.** `HDT_43.jpg` — el **frontis del
  hotel**, 4475×6718, de la sesión profesional. Recortada a 9:16 y **reducida** a
  2250×4000: nunca ampliada ni estirada.
- **El encuadre se midió, no se eligió a ojo.** La ventana centrada dejaba el
  logotipo tocando la cornisa; se midió el «no-cielo» dentro de la caja del
  logotipo para cada offset y se tomó el **174**, que da **0 % de intrusión**.
- **El logotipo va en AZUL DoubleTree, no en blanco.** Es la regla §B.4 aplicada
  con medición: sobre el cielo pálido el blanco daba **1,79:1** y el azul da
  **6,7 a 9,3:1** sin ningún velo encima. Así la mitad de arriba queda limpia.
- **El titular a dos pesos de Stag**, con el orden de la marca (arriba la chica,
  abajo la grande y liviana).
- ⛔ **Stag no puede escribir `¡`** — verificado glifo a glifo: a los nueve cortes
  les falta `U+00A1` y `U+00BF`. Se resolvió con **el truco de Eli**
  (`volteaApertura`), no cambiando el titular de familia.
- **Los textos van LITERALES del brief** y no se agregó dirección, correo, CTA ni
  legal: el brief dice «saludo simple, sin promoción» (§G).

**Las tres rondas de Eli, y qué cambió cada una:**

| Ronda | Qué pidió | Qué se hizo |
|---|---|---|
| 1 | — | Titular 58/94, marco 730, filete 2 px al 55 %, velo fuerte |
| 2 | «título más grande, ajusta el espaciado, la línea como la referencia, baja la transparencia» | Titular a 72/116 (de 50 % a 61 % del ancho); salto titular→subtexto de 30 a 58; **filete a 1 px en blanco pleno** y marco a 766; velo de 0,90 a 0,60 |
| 3 | «agranda todo más y súbelo, la línea como la referencia, el Feliz Día menos grueso, el secundario que crezca» | Marco a **800 de ancho y tope en 680** (subió 425 px); titular a 80/130 (**68,7 %** del ancho); **«¡Feliz Día» de Bold 700 a Medium 500**; subtexto de 30 a **38** |

**⭐ Lo que hay que quedarse de la ronda 2, porque es método:** la línea blanca no
se ajustó «a ojo hasta que se pareciera». Se **midió la de la referencia**: en su
borde superior el píxel es `rgb(255,253,250)` y **mide 1 px**. La nuestra eran 2 px
al 55 %, y por eso se veía blanda. Una referencia se mide igual que una pieza.

**⭐⭐ Y la corrección al diagnóstico del banco de imágenes:** el cierre de la tarde
dejó escrito «⛔ Del FRONTIS casi no hay nada y no baja». **Es falso.** `HDT_42` y
`HDT_43` son el frontis, en alta, y bajan sin token. Lo que no baja es el banco
maestro `Imágenes`, que es otra carpeta. La técnica que lo destrabó vale para
cualquier marca: **la hoja de contacto con las miniaturas de Drive**
(`thumbnail?id=…&sz=w400`, ~30 KB) en vez de bajar 40 archivos de 20-37 MB a
ciegas. Ahí se vio además que hay **habitaciones con la vista de Santiago** y **el
gimnasio en alta**, también dados por faltantes. Lo único que sigue sin estar
fotografiado es **la cookie como producto**.

**⚠️ Dos veces el QA se acusó a sí mismo, y las dos quedaron arregladas en el
código.** Primero la máscara de blanco tomaba el brillo del edificio como si fuera
tinta; después, al subirle el contraste a la foto, la cara oscura de la torre entró
en el rango de `#09194E` y el QA reportó **el logotipo descentrado y de 243 px
cuando estaba perfecto**. La lección: *un umbral de color no distingue un elemento
gráfico de la foto*. Ahora el logotipo se verifica **contra su propia silueta**
(IoU, umbral 0,52 calibrado contra variantes malas a propósito) y la fuente **por
forma** (correlación del perfil de tinta), no por ancho — el ancho daba ±5 % con la
fuente correcta, o sea falsas alarmas.

**Dónde quedó.** La pieza está en Drive, en `S4 HILTON SEP 2026 › DT › STS`:
[DT ST 27-09 Dia del Turismo.png](https://drive.google.com/file/d/12bBQuWsgPsNu8xZ0C1CL_l-0CScGeyuZ/view)
— 2250×4000, 150 ppp, 11 350 675 B, verificado contra el `parentId` (no cayó en «Mi
unidad»). Las tres rondas se subieron **al mismo archivo**, así que el enlace no
cambió. Código nuevo: `src/brand/doubletree.ts`, `src/compositions/hilton/DtStTurismo.tsx`,
`src/DtEntry.tsx` y `scripts/dt-{logo-tintas,st-turismo-foto,rendir,qa,st-turismo-entrega}.py`.
El manual quedó con la geometría medida, el aparato y sus cinco chequeos.
**Reproducible: se regeneró y `cmp` dio idéntico byte a byte.**

**Qué sigue.** **Preguntarle a Carlos qué son los AD ONS** de la Escapada Romántica
(STORIES J, 21-09). Es lo único que falta para cerrarla: la animación existe, el
precio ya está en `$99.000` y la fecha (21-09) ya es post 18. El hilo
`STORIES!J15` está OPEN porque **Eli preguntó y nadie contestó**.

**Abierto.**
- ⛔ **Los AD ONS** — bloqueante de contenido, no de diseño. No se inventan (§G).
- ⚠️ **El logotipo queda 9 px dentro de los 250 px de zona segura superior**
  (arranca en 241). **No es error: es la posición de la plantilla de Eli**, y los
  250 px son la zona segura de *Meta Ads*, no la de una historia orgánica. Si esta
  pieza se pauta, hay que bajarlo.
- **El letrero «DOUBLETREE» de la propia fachada** cae detrás del subtexto. Se
  apagó con una sombra local suave (no subiendo el velo de toda la pieza, que es lo
  que Eli pidió evitar). Si ella prefiere verlo, se saca en un minuto.
- Siguen frenadas **las tres fuentes que faltan** (Stag LCG, Trade Gothic LT Std
  Bold, Trade Gothic Next LT Pro Bold — sólo las tiene el cliente) y **la carpeta de
  la reseña del 14-09**, que sigue devolviendo vacía.
- Sin respuesta desde la mañana: **¿`reglas.yaml` entra con la geometría, o primero
  los dos checks nuevos de `qa/checks.py`?** Con el kit ya escrito, ahora la
  geometría se puede volcar cuando ella diga.

---

## 2026-09-09 (CIERRE 5 · noche) · Eli (Windows) — BETWEEN S3: la primera ronda del CLIENTE, dos correcciones de copy

Quinta sesión del día y segunda de Between (las otras tres fueron de DT y Piso18).
Arrancó con `/abrir between` y cerró con las dos piezas corregidas y subidas.

**Qué se hizo:**

1. **`/al-dia` NO encontró ronda nueva, y se equivocó** — ver «Abierto», es el
   hallazgo de la sesión. La grilla había movido su `modifiedTime` a 18:33Z con el
   md5 intacto, así que se leyó como «alguien sólo la abrió». Eli tenía en pantalla
   dos comentarios en rojo que el archivo de Drive no trae.
2. **Se corrigieron las dos stories de la S3 que el cliente devolvió**, con sus
   comentarios pasados por captura de pantalla. Las dos son de **copy**:
   · col N (16-09 Cowork) — «Saquemos el "Puedes venir", reemplacémoslo por
     Cowork, para dar contexto» → titular «Cowork / ¡TE ESPERAMOS!»;
   · col O (18-09 Saludo) — «Para no redundar, pongamos ¡Feliz 18 de septiembre!
     con eso super ok» → la caja de cierre cambia; el párrafo del brief no se toca.
3. El **14-09 (quiz) no se tocó**: no traía comentario. Verificado que reproduce
   byte a byte los 8 077 154 B que ya estaban en Drive.

**Dónde quedó:**

- `src/compositions/hilton/BetweenStS3.tsx` — los dos cambios, con la ronda escrita
  en las cabeceras de las dos piezas. Renders en `out/hilton/between/st-s3/`
  (gitignored) y entrega en `out/hilton/between/entrega-st-s3/`, 2250×4000 a 150 ppp.
- Fondos ya versionados desde el 08-09 en `public/assets/hilton/between/st-s3/`:
  **nada nuevo que commitear ahí**, sólo cambió texto.
- **Subidas a `S3 HILTON SEP 2026/BW/STORIES`** (`1SNBRIvKLvQSC2bYF3u5_oPL5UumIo-gM`)
  reemplazando el MISMO archivo, así que los enlaces no cambiaron. Verificadas por
  `fileSize` contra el local: 16-09 `1lAgqPkkA25L4VRlnIg9UayWPdZxDuqwk` (6 000 522 B)
  y 18-09 `1NxF_9CEv2GsgDeDns84dCHdW6wuWeM5M` (7 249 755 B).
- `between-qa.py`: 2/2 limpias. Las `GUIA CM` se regeneraron y **no se subieron**.
- Comprobado con `cmp` que el render sale **idéntico byte a byte** al re-rendir.
- `clients/hilton/CLAUDE.md` — sección nueva «S3 · RONDA 9».
  ⚠️ **Ojo con la numeración:** las rondas 6, 7 y 8 de la S3 son del 08-09 y son de
  Eli. Ésta es la 9 y es la primera del cliente. El commit `3a1782f` la llama
  «ronda 7» por error; el manual y la composición dicen 9, que es lo correcto.

**Qué sigue:**

1. **El reel Café Bombón (col G) YA NO ES TAREA DE ESTA CUENTA HOY:** Eli dijo
   «la del café bombón ya lo dejé corregido». ⚠️ Pero la corrección **no aparece
   en ninguna parte** — la grilla no se movió y no hay ningún archivo de Café
   Bombón en Drive buscado por título. Antes de volver a producirlo hay que
   preguntarle **dónde lo dejó**, para no duplicar. La propuesta de los tres
   caminos sigue en `clients/hilton/PROPUESTA-reel-cafe-bombon.md`.
2. **STORIES col D** (ST café de regalo) sigue en `EN CAMBIOS` con «Mismo
   comentario del legal» sin tachar, aunque el legal se entregó el 08-09. Sigue sin
   saberse qué falta.
3. Confirmar si el cliente marca las tres de la S3 ahora que las dos volvieron.

**Abierto:**

- ⭐⭐⭐ **UNA RONDA DEL CLIENTE PUEDE NO ESTAR EN EL `.xlsx`.** Es el hallazgo de
  la sesión y está escrito en el manual (§ S3 · RONDA 9.5). Resumen: `modifiedTime`
  se movió 12:48Z → 18:33Z, el md5 del archivo bajado quedó IGUAL, el conector MCP
  confirmó lo mismo — y aun así el cliente había escrito dos comentarios en rojo y
  movido dos piezas a `EN CAMBIOS`. **«El md5 coincide» NO prueba que no haya
  ronda.** Un `modifiedTime` que se mueve con el blob intacto es SOSPECHA: hay que
  preguntarle a la diseñadora qué ve en pantalla.
- ⚠️ Y su corolario: los rojos de hoy **no los va a ver el próximo que abra la
  grilla por script**, así que el diff de mañana puede mostrarlos como entrada
  nueva cuando son de hoy.
- Siguen de los cierres anteriores: Between **sin `clients/hilton/reglas.yaml`**
  (así que `qa/motor.py --marca hilton` no corre), las **`GUIA CM`** en local sin
  decidir cómo llegan al CM, **`BETWEEN.logo.cafe` apuntando a un PNG negro**, el
  Strudel de la S4 como producto GENERADO a la espera de foto real, y los dos
  falsos positivos de `between-qa.py` en la S4.
- ⛔ Y sigue en pie: **`BetweenCumple.tsx:112` y `BetweenSeptiembre.tsx:794` con el
  legal VIEJO** del cumpleaños.

---

## 2026-09-09 (CIERRE 4 · noche) · Eli (Windows) — BETWEEN S4: las dos stories del 21 y 22-09, APROBADAS en 6 rondas

Sesión de Between (las tres anteriores del día fueron de DT y Piso18). Arrancó con
`/abrir between` y cerró con las dos piezas aprobadas por Eli y subidas.

**Qué se hizo:**

1. **`/al-dia` cazó una ronda nueva del cliente**, entrada hoy a las 12:48:37Z.
   Desapareció `REVISAR CONTENIDO` de TODA la grilla: el FEED del cumpleaños pasó
   a `CORREGIDO` con el comentario del legal **tachado** y su vista previa
   reemplazada por la lámina corregida, y **STORIES D y G pasaron a `EN CAMBIOS`**.
   Contenido pegó además **nuestras tres stories de la S3** en las columnas M, N y
   O (estados sin mover: el cliente aún no marca).
2. **Se produjeron las dos stories estáticas de la S4** —21-09 Strudel y 22-09
   Primavera— por encargo de Eli, guiadas por las dos referencias que dejó
   contenido. **Seis rondas** hasta el OK.
3. Se dibujaron **siete trazos nuevos** para el kit y entró el **quinto emoji**.

### La ronda del cliente, pieza por pieza

| Pieza | Antes | Ahora |
|---|---|---|
| FEED col E · 09-09 Café de cumpleaños | `REVISAR CONTENIDO` | **`CORREGIDO`** — legal cerrado, comentario tachado |
| STORIES col D · ST café de regalo | `REVISAR CONTENIDO` | **`EN CAMBIOS`** |
| STORIES col G · 09-09 **Reel Café Bombón** | `REVISAR CONTENIDO` | **`EN CAMBIOS`** |
| STORIES M · N · O (la S3) | sin cambio | nuestras piezas **pegadas** en la grilla |

⚠️ Salió de la hoja un GIF animado de 104 frames (vaso Between vacío sobre madera)
que calza con la escena 1 del Café Bombón. Respaldado en
`raw/hilton/between/de-grilla/` antes de que se perdiera.

### Las seis rondas de la S4, y qué dejó cada una

| # | Lo que dijo Eli | Lo que cambió |
|---|---|---|
| 1 | (encargo) | las dos piezas, con el sticker en zona reservada |
| 2 | «te dejo la sesión que tenemos de **cómo son**» + «el fondo debe ser mejor realizado» | ⛔ **el milkshake estaba mal**: se había usado `Between-214.jpg`, foto REAL del cliente pero de OTRO producto. Se rehízo con la sesión del producto |
| 3 | «sol y nubes como ilustración, guíate de mis editables» + «títulos en raleway semi bold» | los tres trazos nuevos, `pesoCaps` en el titular y la jerarquía título/párrafo/bajada |
| 4 | «una ilustración como la de esta captura» + «raleway con más grosor» | la capa de línea **sangra** por los bordes y va **repasada**; el titular a Bold 700 |
| 5 | «más irregulares y no tan bien hechas, como textura de pincel» | el canto **aserrado en píxeles absolutos** y la geometría irregular |
| 6 | borrar las rayitas, añadir nube, «usar el beige de BW» | tinta a `#FFF9EB`, tres nubes escalonadas a la izquierda |
| — | «en el título te faltó añadir este emoji 🌸» | el 🌸 entra: la regla de los emojis estaba **mal generalizada** |

**Dónde quedó:**

- `src/compositions/hilton/BetweenStS4.tsx` — las dos piezas y sus dos `GUIA CM`.
- `scripts/between-st-s4-generar.py` · `-fotos.py` — las escenas y el paso a 2250.
- `scripts/between-trazos-sol-nubes.py` — los 7 trazos, con la mano de Eli medida.
- `src/compositions/hilton/BetweenPlanchaTrazos.tsx` y `BetweenPruebaEmoji.tsx` —
  dos utilidades de comprobación (rendir su `.svg` y probar emojis). No son piezas.
- `BetweenSistema.tsx` — la prop **`pesoCaps`**, opt-in. Comprobado: la ST del
  cowork del 16-09 re-rinde con **0 píxeles** de diferencia.
- Kit: `sol`, `solGrande`, `nube`, `nubeChica`, `nubeDoble`, `nubeDobleChica`,
  `rayitas` y el emoji `flor`.
- Entrega: `out/hilton/between/entrega-st-s4-21-22-09/` (+ `GUIAS CM/`), 2250×4000.
- **Subidas a `S4 HILTON SEP 2026/BW/STS`** y verificadas por `fileSize` contra el
  local: Strudel `173nqK9PFefnQpN6Skyi9-vBpVzgYRFjC`, Primavera
  `1PZZS-7L2xL89oNAyqY_yaFysxXKO1CoV` (se reemplazó 6 veces el MISMO archivo, así
  que el enlace nunca cambió).
- **Las dos reproducen byte a byte** desde el repo.
- `clients/hilton/CLAUDE.md` — seis secciones nuevas (§4 bis a §4 sexies + la de
  aprobación) y la instantánea nueva de la grilla.

**Qué sigue:**

1. **El reel Café Bombón.** Pasó a `EN CAMBIOS`, estaba agendado **hoy** y no
   existe composición. Lo único que el cliente pidió por escrito es el legal de
   «imagen referencial»; **nadie anotó cuál de los tres caminos para la leche
   condensada se aceptó** — la propuesta está en
   `clients/hilton/PROPUESTA-reel-cafe-bombon.md` y hay que preguntárselo a Eli.
2. **STORIES col D** (ST café de regalo) también está en `EN CAMBIOS`, aunque la
   corrección del legal se entregó el 08-09. Hay que confirmar qué falta.
3. La S4 la puede seguir el resto del mes con lo que quedó en el kit.

**Abierto:**

- ⚠️ **El Strudel es un producto GENERADO.** Between no tiene ninguna foto del
  Strudel de manzana (buscado en las 202 de la sesión de enero, en los desayunos
  de agosto, en `dulces-tortas` y en la carta). Está rotulado para poder
  reemplazarlo el día que llegue la foto.
- ⚠️ Los ocho trazos recortados de la plancha de Eli conservan su `#fffaee`,
  mientras los siete nuevos van en el `#FFF9EB` de la marca que ella pidió. Son
  2 y 3 puntos de diferencia; si molesta, se re-tiñen los ocho.
- ⚠️ **`between-qa.py` marca las dos piezas y en los dos casos es FALSO POSITIVO**
  (la comida clara y las nubes que sangran). Verificado imprimiendo dónde están
  los píxeles. Convendría darle al script una forma de distinguir ilustración de
  texto.
- Siguen del cierre anterior: Between **sin `clients/hilton/reglas.yaml`** (así que
  `qa/motor.py --marca hilton` no corre), las **`GUIA CM`** en local sin decidir
  cómo llegan al CM (10 días), y **`BETWEEN.logo.cafe` apuntando a un PNG negro**.
- ⛔ Y sigue en pie: **`BetweenCumple.tsx:112` y `BetweenSeptiembre.tsx:794` con el
  legal VIEJO** del cumpleaños.

---

## 2026-09-09 (CIERRE 3 · tarde) — Eli (Windows), DOUBLETREE: el moodboard de la sesión de fotos

**Qué se hizo.** Se armó el **moodboard para la sesión fotográfica del hotel**, de cero
y en seis rondas de pedidos de Eli: frontis, entrada, recepción, check-in, lobby,
pasillos, ascensores, los **cinco tipos de habitación**, cowork (espacio, sillones y
mesas, y trabajo con persona desenfocada), cafetería, las dos terrazas, restaurante,
desayuno buffet, gimnasio, wellness, eventos corporativos, el salón real (entrada,
señalética, pantalla + mesas, montaje sencillo tipo cowork) y mesas redondas. Cada
lámina lleva escrita **la regla de rostros que aplica** y el formato —POST horizontal
/ HISTORIA vertical—. Se entregaron **75 láminas**.

**⭐ El hallazgo de la sesión, y vale más que el entregable.** Se midió el banco real
del hotel y **casi nada de lo que la cuenta necesita está fotografiado**:

- **Todo `CONTENIDO HOTEL 2026` es video de iPhone.** Los cinco tipos de habitación,
  el exterior, el wellness, el gym, el cowork y los salones Astoria/Conrat: **puros
  `.MOV` y `.HEIC`**. La carpeta «Exterior hotel» tiene **un solo archivo, y es video**.
- **La sesión profesional (`FINAL 1`, 370 archivos) sí cubre los salones** y no se
  estaba usando. Pero medido sobre muestras de 48: **~92 % horizontal** (4 verticales
  de 48, o sea **para historias 9:16 no hay material**), **un solo encuadre repetido**
  cuarenta veces, **casi ningún plano de detalle** y **nadie en cuadro**.
- ⛔ **La COOKIE no existe fotografiada como producto**, siendo el ícono de la marca:
  `COOKIE DAY 2026` son fotos del **evento interno** del equipo posando con carteles.
- ⛔ **Del FRONTIS casi no hay nada** y no baja: el banco maestro `Imágenes` no está
  compartido por enlace (401 / página de login), y no hay copias por título.

**Dónde quedó.** El moodboard de 75 láminas en
[Drive](https://docs.google.com/presentation/d/1PC0mqZF2iW78uFSGAzvHJYz7Ok-W9S8VzYrYt2NR-28/edit).
**Eli lo rearmó en su propio documento** —«MoodBoard Hotel sesión», 44 láminas, portada
COPYWRITERS 2026— con su plantilla y su nomenclatura. Se midió esa plantilla y se le
dejaron las **7 láminas que faltaban, calcadas a ella**, en un archivo aparte para
copiar y pegar:
[láminas que faltan](https://docs.google.com/presentation/d/19-XE-aevwu6ZYGgakXNoEhMbYDBwYkG8pq2u8nTegP4/edit).
Código: `scripts/dt-moodboard-{pinterest,definir,armar,subir,laminas-eli}.py` y
`clients/hilton/dt-moodboard-laminas.json`. Diagnóstico completo del material en
`clients/hilton/dt-banco-de-imagenes.md`.

**Qué sigue.** **Medir la geometría de DT** sobre las 3 piezas aprobadas del Family
Time y con eso cerrar `marca.json` + `src/brand/doubletree.ts` + `reglas.yaml` — es lo
que quedó pendiente desde la mañana y no se alcanzó.

**Abierto.**
- ⛔ **Para Eli, antes de escribir `reglas.yaml`:** ¿entra primero la geometría, o los
  dos checks nuevos de `qa/checks.py` (`titulo_sin_punto`, `caja_uniforme`)? Un
  `reglas.yaml` parcial haría que `qa/motor.py --marca hilton` empiece a aprobar con
  cobertura incompleta. **Se preguntó dos veces y sigue sin respuesta.**
- ⛔ **Compartir el banco maestro `Imágenes`** (`1A38ASrVjXdTt1s4nMr2tnfG-15--RmYR`) o
  arrastrar a mano `Fachada` y `Business Center`: hoy no bajan.
- **Tres planos que la sesión tiene que producir sí o sí** porque no existen en ningún
  lado: **la cookie, el frontis y el gimnasio**.
- ⚠️ **Nomenclatura:** Eli rotula los locales **con su marca** (`CAFETERÍA BW`,
  `RESTAURANT QB`, `TERRAZA DE QB`). Lo de «no como marca» que dijo era sobre el
  tratamiento de la foto, no sobre el título. **Su rótulo manda.**
- Siguen frenadas: `STORIES J` del 21-09 (dice «desde $109.000», §G), las tres fuentes
  que faltan y la carpeta de la reseña del 14-09.

---

## 2026-09-09 (CIERRE 3 · tarde) · Eli (Windows) — PISO18: la marca entra al sistema, y entra como marca propia

Primera vez que el estudio abre **Piso18**. Arrancó con `/abrir piso18`.

**Qué se hizo:**

1. **`/al-dia` acotado a P18: la grilla nunca se había abierto.** `PISO18 _GRILLA
   SEPTIEMBRE 2026` (`1kF9OwDflz3mFR_NAodu0Y0YJvQj5wbbmAlN7SdRTFAo`, de Carlos) se
   movió **hoy 13:36:47Z** y venía **sin `viewedByMeTime`**. Se bajó completa (46,9 MB
   de xlsx real) y se leyeron las 4 hojas.
2. **⛔ Hay un hilo ABIERTO y es para Eli.** Comentario de Carlos de **hoy 13:25Z** en
   `FEED!F13` = celda COMENTARIOS CLIENTE del post del **10-09** («Sección fotos novios
   en hotel»), estado `REVISAR CONTENIDO`. **Sale mañana a las 12:00.** El comentario
   sólo dice «me ayudas aquí?»: el encargo está en la celda, no en el hilo. ⚠️ Esa misma
   celda recibió la **misma pregunta cuatro veces** (31-08, 02-09, 07-09 y hoy); las tres
   primeras están resueltas. Es la pieza que rebota.
3. **⭐⭐ Eli dictó la identidad de la marca, y lo primero es un cortafuegos:** *«Todo es
   propio y diferente a DT, recuerda no mezclar las marcas.»* Piso18 es un **centro de
   eventos dentro del hotel, en el piso 18** — relación de dirección física, **no de
   identidad**. El asunto son los **espacios y su decoración**. Cinco verticales:
   matrimonio · cumpleaños · corporativo · bautizo · otros, y **la marca se está
   abriendo**: *«últimamente van por más eventos, no sólo es matrimonio»*.
4. **Se auditó el mes contra ese criterio** (medido, no estimado): **matrimonio 8 ·
   cumpleaños 3 · corporativo 2 (las dos de refilón) · bautizo 0 · genérico 10**. La
   grilla todavía no refleja la apertura. Se dejó escrito **como diagnóstico, no como
   corrección** — la grilla la escriben cliente y contenido.

**Dónde quedó:**

- `clients/hilton/CLAUDE.md` — sección nueva **§PISO18 — MARCA PROPIA** (línea ~273) con
  el cortafuegos, las 5 verticales, la auditoría, el estado de las 7 capas (**tiene 0**)
  y cómo volver a bajar la grilla. Corregida la fila P18 de «Las 4 cuentas», que decía
  «eventos con vista (cumpleaños, novios, corporativo)» y se comía el bautizo.
- `clients/hilton/CHECKLIST-CLIENTE.md` — partido en **dos bloques que no se cruzan**.
  Nuevos bloqueantes **P1–P5** de Piso18 y las decisiones abiertas.
- `clients/hilton/grillas/p18-septiembre-2026.md` — instantánea nueva (1.389 líneas).
  **Es la base del diff de la próxima ronda**, que P18 no tenía.
- `raw/hilton/piso18/` (no viaja en git) — árbol de aterrizaje con `LEEME.md`:
  `ref-eli-sep2026/`, `editables/`, `logo/`, `fotos/`. Las dos fotos que estaban en
  `Downloads` se movieron a `fotos/`.
- **No se produjo ninguna pieza**, y fue a propósito: sin gramática medida, cualquier
  pieza le inventa un sistema a la marca.

**Qué sigue:**

`/adn piso18` en cuanto Eli deje los editables — mide paleta, tipografías y gramática de
una pasada. Y con eso, la pieza del **10-09**, que es la urgente.

**Abierto:**

- ⛔ **El bloqueante n°1: las piezas de referencia no bajan.** Las **10** de la carpeta
  `P18` de la S1 (`1TR-CiAE84ryQ1gTA2PvkEthsWhwSm5yA`) más 4 de julio (`C1 S5 P18 n°1–4`):
  **las 14 devuelven ~908 KB de página de login**. Se aplicó la regla de buscar **copias
  por título** (la que salvó el Family Time): hay copias públicas, **pero son de otras
  marcas** — `CARRUSEL NB 1` es Noche de Bodas de DT y `C1 S2 CUMPLEAÑOS` vive dentro de
  la carpeta `BW`. De Piso18, cero. Se destraba compartiendo la carpeta por enlace o
  copiando los PNG a `raw/hilton/piso18/ref-eli-sep2026/`.
- **Eli va a dejar los editables y el universo completo de Piso18** (comprometido hoy).
- **Faltan además:** logo P18 en PNG con transparencia (hay un pendiente del cliente,
  «quedó algo extraño detrás del logo», que **no se puede ni diagnosticar** sin el
  archivo), las tipografías propias, la galería del fotógrafo y la medida del máster.
- **Tres decisiones que las dicta Eli:** ¿la **§G** vale para Piso18? ¿la regla de
  **rostros de trabajadores** vale acá? (la grilla de P18 pide «sin caras directas» por
  su cuenta, así que converge, pero no está dictada) y **¿quién hace las semanas 2 y 3?**
  — hay **13 piezas en `OK PARA DISEÑAR`** y no existe carpeta `P18` en la S2 ni en la S3,
  mientras Between tiene las tres.
- **1 story bloqueada por cliente:** el menú del 09-09 espera los PDF actualizados.

**⭐ Lo aprendido, que sirve para cualquier marca:**

> Un **Sheet nativo** de Google se baja con `/export?format=xlsx`, **no** con
> `uc?export=download` — ese es para un `.xlsx` ya subido, como la grilla de Between.

> Un comentario de Drive que sólo dice «me ayudas aquí?» **no trae el encargo**: el qué
> vive en la **celda que el comentario ancla**. Leer el ancla, no el hilo.

⚠️ **Aviso para quien abra mañana:** hoy hubo **dos sesiones en paralelo** sobre este
repo. La otra (`479f3b86`) trabajó las **stories S4 de Between** y dejó sin commitear
`scripts/between-st-s4-generar.py` y la instantánea `between-septiembre-2026.md`
actualizada al 09-09. **Este cierre NO las subió a propósito** — no se commitea el
trabajo a medias de otra sesión bajo un mensaje de Piso18. Esa sesión tiene que cerrar
lo suyo, o se pierde.

---

## 2026-09-09 (CIERRE 2 · tarde) · Eli (Windows) — DOUBLETREE: cae el bloqueante del Family Time, y la lección es de método

Sesión corta, de una sola cosa, y esa cosa era el **bloqueante número uno** que dejó
el cierre de esta mañana. Arrancó con `/abrir Doubletree`.

**Qué se hizo:**

1. **`/al-dia` acotado a DT: sin ronda nueva.** El sheet `DOUBLETREE | GRILLA
   SEPTIEMBRE 2026` sigue en **`08-09 20:42:32Z`** — la marca de tiempo *exacta* de la
   instantánea de la mañana. El estado del mes no se movió, y Eli no subió archivos hoy.
2. **⭐⭐ Se bajó el carrusel de Family Time, que ayer se declaró imposible.** Ya está en
   `raw/hilton/dt/aprobadas-sept/`: `C1 FT N1.png` (6 733 610 B), `C1 FT N2.png`
   (3 029 114 B) y de paso `DT FT S3.png` (6 709 065 B) — los tres **2250 × 2813 RGBA**
   y con **bytes idénticos** a los que declara Drive, así que no son re-exportaciones.
   **La regla del Family Time pasó de escrita a ejecutable.**
3. **Se leyó el carrusel y trajo contenido que faltaba en el manual** (ver abajo).
4. **Octubre avanzó fuerte, pero no es nuestra lane.** El doc `TEMAS OCTUBRE | HILTON`
   se movió a las 14:33Z y Scarlette **resolvió 14 hilos** entre 13:46 y 14:12Z. Ya **no
   son 13 comentarios abiertos**: queda **uno solo, y es de QB** (deco de Halloween,
   «confirmar con cliente… anclado a alguna acción comercial»).

**⭐⭐ La lección del día, y es de método — vale más que el archivo:**

> **Un archivo de Drive que no baja NO es un bloqueante hasta haber buscado sus COPIAS
> POR TÍTULO. El permiso vive en la CARPETA, no en el archivo.**

`C1 FT N°1.png` existe en **cuatro** carpetas con bytes idénticos: tres piden login y
**la cuarta es pública**. Ayer se cerró la sesión declarándolo bloqueante después de
probar dos caminos **sobre una sola carpeta**. Era un bloqueante falso, y costó una
sesión. La búsqueda que lo resolvió:

```
search_files: title contains 'FT' and mimeType contains 'image/'
              and owner = 'elisabet.soto@copywriters.cl'
```

⚠️ **Y un aviso sobre las herramientas:** el conector de Drive **no estaba caído**.
`search_files`, `get_file_metadata` y `read_file_content` respondieron bien en esta
misma sesión, mientras `download_file_content` devolvió «session expired» **tres veces
seguidas** con esos dos PNG. **La herramienta que falla no prueba que el archivo no
esté.** Quedó ampliada la memoria `agotar-material-antes-de-bloquear` con este paso.

**Lo que trajo el carrusel, ya escrito en el manual §C:** Family Time es **`$125.000`**
con **`IVA INCLUIDO`** bajo la cifra, y tres incluidos con ícono de línea —
**Habitación doble** · **2 adultos + 2 niños hasta 12 años** · **Desayuno buffet**.
Correo `reservas.dtv@hilton.com` y legal al pie `*Válido de jueves a domingo y
festivos. Sujeto a disponibilidad.` **El precio CALZA con el manual: no hay
discrepancia.** Estos textos van literales, no se parafrasean.

**Y confirma dos reglas ya escritas, medidas sobre la pieza aprobada:** el `$` del
precio y el `@` del correo **son Trade Gothic** (las nueve Stag no traen ninguno de los
dos), y el titular va **a dos pesos en caja baja y sin punto** («Este es su panorama /
Ideal en familia»), que es exactamente lo que dictó Eli esta mañana.

**Dónde quedó.** Archivos tocados: `clients/hilton/CLAUDE.md` (fila del Family Time de
⛔ a ✅ + los incluidos en §C + bloque nuevo con el **comando de recuperación**),
`clients/_estado-sync.json`, y la memoria `agotar-material-antes-de-bloquear` (+ su
línea en `MEMORY.md`). **No se rindió ni se entregó ninguna pieza**, así que no hay
scripts ni fondos que commitear por la regla del render.

⚠️ **Los tres PNG NO viajan en git** (`.gitignore: raw/*`). Por eso el manual quedó con
el **comando exacto** para volver a bajarlos en otra máquina —los tres IDs públicos y
los bytes que tienen que pesar—, justo antes de §D. Si llegan ~900 KB de HTML, es la
página de login y no el PNG.

**Qué sigue.** Lo mismo que dejó el cierre de la mañana, ahora **desbloqueado**:
**medir la geometría de DT** sobre estas tres piezas aprobadas y con eso cerrar
`marca.json` + `src/brand/doubletree.ts` + `reglas.yaml`.

**Abierto.**
- ⛔ **Decisión para Eli, y hay que hacerla antes de escribir `reglas.yaml`:** el
  archivo **no queda completo sin dos checks nuevos** en `qa/checks.py`
  (`titulo_sin_punto` y `caja_uniforme`), porque operan sobre `ctx["textos"]` y no
  sobre el PNG. Un `reglas.yaml` parcial haría que `qa/motor.py --marca hilton`
  **empiece a aprobar piezas con cobertura incompleta**, que es peor que no correr.
  **¿Entra primero la geometría, o los dos checks?** Se le preguntó y no alcanzó a
  responder.
- **`STORIES J` (21-09)** sigue frenada: dice «desde $109.000» y no calza con ningún
  programa. **No se toca hasta que el cliente confirme** (§G).
- **Siguen abiertas las tres decisiones de Eli del 08-09:** ¿el titular con la primera
  línea en verde sigue vigente? ¿entra el rosa `#DC224B` a la paleta? ¿el azul es
  `#09194E` (manual) o `#111C4E` (medido)?
- **Bloqueantes de cliente** (`CHECKLIST-CLIENTE.md`), **sin cambios hoy:** las tres
  fuentes que faltan (Stag LCG, Trade Gothic LT Std Bold, Trade Gothic Next LT Pro
  Bold) y la carpeta de la reseña del 14-09, que **sigue devolviendo vacía**
  (`1Dlki995RRdwueFGlZOkF9rybf7maMJ5u`).
- **¿La regla §G vale también para QB, Between y Piso18?** Se dictó **para DT** y no se
  dio por extendida. Lo tiene que decir Eli.

---

## 2026-09-09 (CIERRE) · Eli (Windows) — DOUBLETREE: Eli dictó la capa de imagen y redacción, y fijó el límite del encargo

Sesión corta y de una sola cosa: **cerrar el sistema de DT con lo que faltaba**, que
era la conversación de Eli sobre uso de foto/video y cómo se deben ver las piezas.
Arrancó con `/abrir DT`.

**Qué se hizo:**

1. **`/al-dia` cazó ronda nueva de DT** — la grilla se movió a las **20:42Z del 08-09**,
   o sea *después* de la pasada de la tarde. Diff limpio: **3 celdas de 195 en FEED**,
   0 en STORIES, 0 en REELSORGÁNICOS, 0 en las otras dos hojas. Esta vez **las columnas
   NO se corrieron** (los titulares de la fila 10 son idénticos).
   - **FEED G (10-09, `POST - NOCHE DE BODAS`): `CORREGIDA` → `APROBADO`.** Es la pieza
     que Eli entregó el 07-09. **Cerrada.**
   - **FEED K (23-09, `REEL - HILTON HONORS formato POV`): `POR GRABAR` → `REVISAR
     CONTENIDO`**, y el comentario cambió de «Podríamos hacer como un video todo en POV»
     a «**Este que mejor sea un estático**, ya hicimos reel hace poco (guardemos la idea
     de todas formas)». ⚠️ La fila `DISEÑOS` sigue diciendo REEL y el brief sigue
     describiendo 5 escenas con rodaje coordinado con Sebastián Serrano.
2. **⭐⭐ Eli dictó LA LEY DE DT** y quedó escrita en `clients/hilton/CLAUDE.md` como
   bloque nuevo (§A–§G): rostros, logo, programas, fotos, tono, títulos y el límite del
   encargo. Detalle abajo.
3. **⛔⛔ Y fijó el límite del encargo, que manda sobre todo:** «Para esta cuenta no
   tienes que tocar nada de brief ni contenido, solamente ayudarme a mí a diseñar. Eso
   lo decide netamente cliente con contenido, por respeto a las grillas y brief que
   ellos dejen. El cliente si solicita ajustes, ahí nosotros lo veremos.» Está como
   aviso al inicio del manual **y** completa en §G, con memoria propia
   (`solo-diseno-el-brief-no-es-mio`).
4. **Se re-midió la cobertura de glifos de las fuentes de DT, peso por peso.**
5. **Se cruzaron los precios del mes entero** contra lo que dictó Eli.

**⭐ Las reglas de Eli, en corto:**

- **Rostros de trabajadores: por defecto NO.** En imagen (post/story), **del torso hacia
  abajo**, y **las manos** en preparaciones de cocina. **En video SÍ**, porque habla la
  propia persona. Excepción en imagen: **fechas del oficio** (ej. día del housekeeping).
  ⚠️ Consecuencia: el Hilton Honors del 23-09, al pasar de reel a estático, **pierde el
  permiso de mostrar rostros**.
- **Logo:** siempre el **principal** (vertical, 4 líneas). El **horizontal sólo si el
  cliente lo pide**. **Blanco por defecto**, y **azul DoubleTree cuando el fondo es
  demasiado blanco** y el logo se pierde. No choca con la regla del 08-09 («en feed por
  defecto no va»): esa decide *si* aparece, ésta *cuál y de qué color*.
- **Programas:** Family Time **$125.000** · Escapada Romántica **$99.000** · Noche de
  Bodas **$189.000** (confirmado hoy). La promo de ER **no es permanente** y la de
  septiembre 2026 fue de **$89.000** (reserva 11–20 de sept, Fiestas Patrias). ⚠️ Al
  terminar el mes hábil, **las piezas se cambian y el precio vuelve a $99.000**: una
  pieza con promo no se reutiliza sin editar.
- **Fotos de los programas: siempre las nuestras**, pero **con el rostro reemplazado por
  uno generado** (uno de hombre y uno de mujer) **y variando** entre piezas, para no
  ensuciar el feed ni las historias.
- **Tono:** elegante, minimalista, sencillo. **No saturado.**
- **Títulos:** ⛔ **sin punto nunca** (el punto es de los párrafos largos o del texto que
  viene después) y ⛔ **sin mezclar cajas** — todo en caja baja o todo en versales.
  ⚠️ Esto **no** prohíbe el titular a dos pesos (Stag Bold + Stag Light): los dos pesos
  se permiten, la mezcla de cajas no.

**Lo medido hoy:** las **nueve** Stag del repo son *el mismo* subconjunto de **354
glifos** y a **todas** les faltan `$ % ¿ ¡ @ € º ª # *` — no es sólo la «Stag normal»,
como decía la nota de ayer. Las dos Trade Gothic (287 glifos) cubren todo el set de
prueba. Corolario práctico nuevo: además del precio, **el `@` de un correo y el `%` de
un descuento también son Trade**.

**⛔ Y las fuentes que Eli subió anoche NO eran nuevas.** Las dos carpetas `Fonts` de
`GRILLA IA DT` (19:54–20:56Z) traen **los mismos archivos** que ya estaban en
`public/assets/hilton/dt/fonts/` — bytes idénticos (Stag Regular 70 116, Medium 70 164,
SemiBold 70 008, Italic 77 424, MediumItalic 77 880, Light 70 680; Trade Regular 28 936
y BoldCn20 29 251). **Siguen faltando Stag LCG, Trade Gothic LT Std Bold y Trade Gothic
Next LT Pro Bold**, y sólo el cliente los tiene.

**El cruce de precios (diagnóstico, NO lista de correcciones):** `FEED C` $99.000 ✓ ·
`FEED D` $89.000 ✓ (era la promo) · `FEED F` $125.000 ✓ · `FEED G` $189.000 ✓ ·
⛔ **`STORIES J` (21-09, `ANIMADA - ESCAPADA ROMÁNTICA`) dice «desde $109.000»**, que no
calza con ninguno. **Decisión de Eli: no se toca hasta que el cliente confirme.**

> 🔴 **El error del día, anotado a propósito:** al encontrar los $109.000 **recomendé
> diseñarla con $99.000 y avisarle al cliente**. Eso era editarle el brief, y de ahí
> salió la regla §G. **Detectar la discrepancia sirve; resolverla no me toca.**

**Dónde quedó.** Capas del sistema DT: **identidad, formatos, copy, imagen y gramática
de redacción LISTAS**. Falta la **geometría medida** (y con ella `marca.json`,
`src/brand/doubletree.ts` y `reglas.yaml`). Archivos tocados hoy:
`clients/hilton/CLAUDE.md` (bloque nuevo + aviso de cabecera + nota de glifos),
`clients/hilton/grillas/dt-septiembre-2026.md` (instantánea del 09-09, base del próximo
diff), `clients/_estado-sync.json`, y `raw/hilton/dt/DT-grilla-septiembre-2026.xlsx`
actualizado (no viaja en git). **No se rindió ni se entregó ninguna pieza**, así que no
hay scripts ni fondos nuevos que commitear.

**Qué sigue.** **Medir la geometría** de las piezas aprobadas y con eso cerrar
`marca.json` + `src/brand/doubletree.ts` + `reglas.yaml`.

⛔ **Pero está bloqueado por un archivo, y es el bloqueante número uno de mañana:** la
regla del Family Time dice que la fuente de verdad es **el último carrusel de Eli**, y
ése **no está en esta máquina**. Son `C1 FT N°1.png` (6,73 MB) y `C1 FT N°2.png`
(3,03 MB), que Eli dejó el 08-09 20:15Z en la carpeta de Drive **`C1 FAMILY TIME`**
(`1eCrtkz0HUAiDT27qlXlKm8xKJxjKvJ-p`). **No se pueden bajar desde acá:** por enlace
llega la página de login (la carpeta no está compartida) y el conector MCP devuelve
**contenido vacío** con los dos. **Hay que copiarlos a mano a
`raw/hilton/dt/aprobadas-sept/` o compartir la carpeta por enlace.**

**Sobre el `reglas.yaml` de DT — se puede, pero no se improvisó hoy.** Los checks que ya
existen cubren parte (`zona_segura` con los 209/369 de Eli, `contraste_texto` para el
33 % del manual, `formato_clp`, `respiro_borde`), **pero las dos reglas de título
necesitan checks nuevos** en `qa/checks.py` (algo como `titulo_sin_punto` y
`caja_uniforme`, que operarían sobre `ctx["textos"]`, no sobre el PNG). Se dejó sin
crear a propósito: un `reglas.yaml` parcial haría que `qa/motor.py --marca hilton`
**empiece a aprobar piezas con cobertura incompleta**, que es peor que no correr.

**Abierto.**
- ⛔ **Los dos PNG del carrusel de Family Time** (arriba). Sin ellos la regla del Family
  Time está escrita pero **no es ejecutable**.
- **`STORIES J` (21-09)** frenada esperando que el cliente confirme el precio.
- **Siguen abiertas las tres decisiones de Eli del 08-09:** ¿sigue vigente el titular con
  la primera línea en verde? ¿el rosa `#DC224B` entra a la paleta? ¿el azul del sistema
  es `#09194E` (manual) o `#111C4E` (medido)?
- **Bloqueantes de cliente** (`CHECKLIST-CLIENTE.md`): las dos fuentes que faltan, y el
  estático de reseña del 14-09 — **la carpeta que el brief nombra devuelve vacía**
  (`1Dlki995RRdwueFGlZOkF9rybf7maMJ5u`). Lo que sí hay es el `REF` de I11
  (`1yoXATM5Kh3v1IfBqyPUVaMW1wzBfPh0-`): dos PNG de Diego Aguilar del 12-08, la misma
  pieza de agosto en español e inglés, con la reseña literal. ⚠️ Son de **Tripadvisor** y
  firman con nombre («Sam»), mientras septiembre pide **Booking con iniciales** y octubre
  **Expedia**. Sirven de **gramática** de la pieza, no de contenido.
- **⭐ Octubre ya está en juego, y NO es nuestra lane:** `TEMAS OCTUBRE | HILTON | 04/09`
  (`1W-1a7axLS3FMif1mZJxIitLRu4H2dfqFz8k7YCe9VP8`) se modificó **hoy 13:18Z** y trae
  **13 comentarios abiertos de Scarlette Muñoz**. DT en octubre: 7 posts (2 reels
  orgánicos) + 6 stories, la reseña pasa a Expedia y el reel del día del chef **sale
  desde DT** en colab con las otras 3 marcas (un solo video para las cuatro). Por §G,
  **se lee y se espera** — lo negocian contenido y el cliente.
- **¿La regla §G vale también para QB, Between y Piso18?** Se dictó **para DT** y no se
  dio por extendida. Lo tiene que decir Eli.

**Otras marcas del complejo (no revisadas a fondo, `/al-dia` fue acotado a DT):** la
grilla de **Between se movió hoy 09-09 12:48Z**, QB el 08-09 20:52Z y Piso18 el 08-09
20:40Z. Eli trabajó anoche en QB (`CARTA QB DIGITAL GENERAL`, `KV FLYER QB GENERAL 2026
SEP`) y en brochures del hotel.

---

## 2026-09-08 (CIERRE 3 · noche) · Eli (Windows) — DOUBLETREE: la identidad queda cerrada y medida

Tercera sesión del día, la primera de **ADN de DT**. Arrancó con `/abrir Doubletree`
y terminó con la capa de identidad completa. Eli fue subiendo material durante la
sesión: la carpeta `GRILLA IA DT`, ocho carpetas de sesiones fotográficas, las
referencias de margen y los dos logos.

**Qué se hizo:**

1. **`/al-dia` cazó ronda nueva en la grilla de DT** (08-09 15:31Z, Carlos Figueroa).
   ⚠️ **La grilla se reestructuró**: se insertaron columnas «SEMANA n» y todas las
   letras corrieron, así que el diff por columna es ruido — hay que comparar por
   contenido. **Un solo comentario nuevo en todo el mes**: FEED 10-09 «Noche de Bodas»
   («el carrusel de agosto tiene un error, debería ser Noche de Bodas… agregar
   dirección»), y **Eli ya lo entregó** el 07-09. Instantánea nueva en
   `clients/hilton/grillas/dt-septiembre-2026.md`.
2. **Se extrajo el manual oficial de Hilton** (dic 2021, 50 mil caracteres) y se
   destiló a reglas en español en **`clients/hilton/dt-manual-oficial.md`**.
3. **Se leyeron los 9 `Informe.txt`** de los editables empaquetados y se midieron
   logos y zonas seguras por canal alfa.
4. **Se mapeó el banco de imágenes** — 8 carpetas con IDs y orden de búsqueda, en
   **`clients/hilton/dt-banco-de-imagenes.md`**.
5. **Se abrió `clients/hilton/CHECKLIST-CLIENTE.md`** con lo que hay que pedirle al
   cliente, con el argumento de a qué piezas afecta cada cosa.

**⭐ Las reglas que dictó Eli, y que MANDAN sobre el manual:**

> **«El manual es un apoyo, pero al final la diseñadora soy yo.»** El manual manda en
> **color, tipografía y su uso**; en **composición y uso del logo manda Eli**.

- **Tipografía:** Stag + Trade es el default de grilla. **Raleway salió en 2026
  porque no está en el manual.** Kallimata tampoco va en grilla — **entra sólo por
  ocasión especial** (San Valentín, Cyber, Año Nuevo, eventos), igual que cualquier
  otra elegante o curva. Es excepción por fecha, no recurso de grilla.
- **Logo:** **en feed, por defecto NO va** («ensucia el feed»). Sólo en programas del
  hotel y piezas importantes. **El horizontal, sólo si el cliente lo pide — casi nunca.**

**Lo medido (todo por canal alfa, no deducido):**

- **Logo, colocación en mesa 1080** — feed: 160,3 × 130,6 px a **111,4 px** del borde
  superior, centrado. Historia: 167,0 × 136,3 px a **241,0 px**, centrado.
- **`logo DT.png`**: tinta 1603 × 1307, **proporción 1,2265**, blanco puro, 4 líneas
  (icono 617 · DoubleTree 193 · by Hilton 154 · SANTIAGO–VITACURA 86).
  ⭐ **Trae su aire incorporado**: 187 px a los lados ≈ la altura de la «D», que es
  justo el aire de §3.2. **Al colocarlo no se suma margen, y recortarlo al borde de
  la tinta rompería la norma sin que se note.**
- **`Hilton Honors Logo_White PNG.png`**: 1091 × 470, proporción 2,3213. **No es logo
  del hotel: es del programa.** Sólo cuando la pieza habla de beneficios.
- **⚠️ Zonas seguras de Eli, y NO son las genéricas de la agencia:** su
  `Zona segura PNG.png` (estaba dentro de los `Links` del editable de stories) marca
  **209 px bloqueados arriba y 369 abajo** en mesa 1080×1920, más una franja de
  precaución entre 1119 y 1549. La regla global del estudio dice 250/340. **En DT
  manda la plantilla de Eli.** El logo a 241 px queda 32 px bajo su banda.
- **Del manual:** primera línea del titular en **verde `#A3CD39`** y el resto en blanco ·
  titular interlínea 100 % y tracking 40 · cuerpo 160 % y tracking 10 · contraste
  logo/fondo mínimo 33 % · sobre fondo verde va el logo **azul** · **SPANISH LA usa
  las mismas fuentes que el inglés** · Cookie con mayúscula cuando es la de la marca.

**⛔ El límite que hay que asumir — confirmado por Eli: el cliente no le facilita las
fuentes.** Tenemos Stag normal (354 glifos) + Trade Gothic LT Std Regular + Bold
Condensed No. 20. **Faltan Stag LCG, Trade Gothic LT Std Bold y Trade Gothic Next LT
Pro Bold.** Tres consecuencias:

1. La regla «precios y preguntas en Trade» **sigue vigente pero por otra razón**: no
   la manda la marca, es que **nuestra Stag no puede escribir `$ % ¿ ¡ @`**. Es apaño
   con fecha de vencimiento.
2. **El bloque de precio no va a quedar idéntico al aprobado** — el sustituto comprime
   la píldora de ~630 px a ~410 px al mismo alto de dígito.
3. **El examen de admisión no puede dar 100 % sobre el Family Time** (lleva `$125.000`).
   El bloque de precio queda como **desviación declarada**, y el QA lo marca como
   revisión humana obligatoria, no aprobado automático.

**Dos correcciones a cosas que yo había escrito mal:**
- Dije que los 241 px del logo eran «la zona segura de Instagram de 250». **No:** la
  plantilla de Eli dice 209. El número sale de su plantilla, no de la regla genérica.
- Pedí el `.ai` del Family Time. **Sobra:** casi seguro está dentro de
  `GRILLA FEED DT S1 SEP.ai`, que Eli ya subió.

**Dónde quedó.** Capas del sistema: **identidad, formatos y copy LISTAS**; imagen
mapeada; **gramática, pipeline y QA pendientes**. Página de estado (artefacto):
`https://claude.ai/code/artifact/62c1cbbf-874c-418f-979d-78dbe75c8e15`.
Material bajado a `raw/hilton/dt/` (no viaja en git): manual en texto, los dos logos,
la zona segura y la grilla nueva.

**Qué sigue.** **Medir la gramática pieza por pieza** sobre Family Time, Escapada
Romántica y Noche de Bodas — es lo único que queda por hacer con el material que hay.
Después `marca-dt.json` + `src/brand/doubletree.ts` + `reglas-dt.yaml`.

**Abierto.**
- **Eli habla mañana de las reglas de uso de foto y video** (qué se puede usar y qué
  no) **y de cómo se deben ver las piezas**. Eso es justo la capa de Imagen y la de
  Gramática/QA: **con esa conversación el sistema queda completo.** Pedirle sobre todo
  los casos en que dijo que NO — un rechazo enseña el límite más rápido que diez aprobadas.
- **Dos decisiones suyas pendientes:** ¿sigue vigente el titular con la primera línea
  en verde? ¿y el rosa `#DC224B` que aparece como tinta plana en el pie de firma y no
  está en la paleta?
- **El azul:** `#09194E` del manual vs `#111C4E` medido. No es error — el editable
  lleva el PANTONE 2766 C en Lab y al exportar a sRGB da otro valor. Falta elegir cuál
  fija el sistema (recomendado: el de Eli, que es el que se publica).
- **Bloqueantes de cliente** (en `CHECKLIST-CLIENTE.md`): las dos fuentes, y el texto
  literal + iniciales + rating de la reseña de Booking, que sigue frenando el estático
  del 14-09.
- **Falta el `Informe.txt`** de `GRILLA FEED DT S1 SEP` — el único de los nueve paquetes
  que llegó sin él.

---

## 2026-09-08 (CIERRE 2 · tarde) · Eli (Windows) — BETWEEN: el legal de los extras

Segunda sesión del mismo día. La de la mañana cerró las tres stories de la S3
(entrada más abajo); ésta arrancó con `/abrir between` y **la grilla se había
movido entre medio**.

**Qué se hizo:**

1. **`/al-dia` cazó una ronda nueva del cliente**, entrada entre las 09:21Z y las
   16:39Z — o sea después de la pasada de la mañana. El tema es **el legal**, y
   toca tres piezas.
2. **Se arregló el legal de la story 2 del cumpleaños** y se entregó al Drive
   reemplazando el mismo archivo.
3. Se escribió en el manual la regla de fondo que explica el error.

### La ronda: «sacaron el legal de los extras 😭, hay que dejarlo»

| Pieza | Antes | Ahora | Comentario nuevo |
|---|---|---|---|
| FEED col E · 09-09 · Café de cumpleaños | `CORREGIDO` | `REVISAR CONTENIDO` | «Pero sacaron el legal de los extras 😭, hay que dejarlo, con eso queda ok» |
| STORIES col D · ST café de regalo | `CORREGIDO` | `REVISAR CONTENIDO` | «Mismo comentario del legal» |
| STORIES col G · 09-09 · **Reel Café Bombón** | `EN REVISIÓN` | `REVISAR CONTENIDO` | «Agreguemos legal imagen referencial y OK» — y **se tachó** la duda de hace 12 días |
| STORIES col I · Emergencia | `CORREGIDO` | **`APROBADO`** | — |
| STORIES col J · 11-09 · Así se hace tu café | `CORREGIDO` | **`APROBADO`** | — |

También: los 3 reels orgánicos sin fecha recibieron 11, 24 y 28-09 con el brief
reescrito (son con colaboradores reales: metraje, no IA), y la Promo To Go se
corrió de 08-09 a 10-09.

⚠️ **Las tres stories de la S3 no se tocaron en la grilla**: la 14 y la 18 siguen
`OK PARA DISEÑAR` y la 16 `CORREGIDO`. El OK de Eli fue **interno**; el cliente
todavía no marca.

### ⭐⭐ De dónde salió el texto del legal: de la PIEZA, no del comentario

El comentario dice *qué* falta; **la pieza viva del Drive dice cómo está
escrito**. Eli ya había corregido el carrusel de feed ella misma —reemplazó
`C1 S2 CUMPLE N2.png` el 08-09 a las **12:31**— así que bastó calcarlo. Y calcarlo
cambió la respuesta: no es una frase de dos oraciones, son **DOS LÍNEAS, cada una
con su propio asterisco**:

```
*Presenta tu cédula de identidad para canjear tu café el día de tu cumpleaños.
*Extras y personalizaciones no incluidas.
```

Si se hubiera deducido del comentario, habría salido una sola línea larga.

### Cómo se perdió el legal, reconstruido

Eli hizo **dos** versiones del carrusel el 07-09, las dos en `raw/hilton/between/de-eli/`:

| | Cédula / «el día» | Extras |
|---|---|---|
| `cumple-s2/` (14:53) | ⛔ «de cumpleaños» | ✅ sí |
| `cumple-s2-v2/` (17:40) | ✅ corregido | ⛔ **se perdió acá** |

La corrección de la fecha **reescribió la frase completa** y en el camino borró la
segunda oración, que el comentario no mencionaba. De ahí la regla nueva del
manual: **el legal es acumulativo — se le agrega, no se redacta de cero.**

### La story 1 NO se tocó, y hay motivo

La lámina N1 del carrusel lleva la **dirección** (`AV. Vitacura 2727, Las Condes`),
no el legal. El legal vive sólo en la lámina 2 → sólo en la story 2. Verificado
leyendo las dos láminas, no supuesto.

### Lo medido antes de dar la pieza por buena

| | Antes (1 línea) | Ahora (2 líneas) |
|---|---|---|
| tinta del legal | y 1646,4 – 1669,9 | y 1646,4 – **1702,1** |
| cierra a | 247 px del borde | **218 px** |
| franja inferior de Meta (340 px) | 90 px | **122 px** |

- El bloque creció **hacia abajo**: la línea 1 **no se movió un píxel** (0 px de
  diferencia sobre y=3497 contra el render anterior), o sea que sigue donde Eli la
  aprobó el 07-09.
- La banda de la línea 2 está **más oscura** que la de la 1 — luminancia 0,071
  contra 0,155 midiendo **por tercios** de la columna, ~8:1 contra el beige
  `#fff9eb`. El pie se lee **mejor** abajo que arriba.
- Subir el bloque para recuperar franja lo devolvería sobre el **plato y las
  cintas**, que es justo lo que Eli mandó corregir.

### Un susto que no era: la ST 1 «no reproducía»

Al re-rendir, la story 1 salía con **21.500 px distintos** contra la entregada, y
las dos líneas del titular se veían más gordas. No era una regresión:

- los anchos de tinta son **idénticos al píxel** (script 1710 px, Raleway 1635 px);
- no hay corrimiento (probado ±2 px: el mínimo está en 0);
- el código de la pieza **no cambió** entre el commit de la entrega y HEAD, y los
  cambios de `BetweenSistema.tsx` de la ronda 8 son todos **opt-in con el valor
  por defecto anterior**;
- a zoom 2× los glifos son los mismos.

Es **rasterización** (~3 % más tinta de antialiasing), no diseño. Igual dejó una
lección: la diferencia bruta de píxeles no sirve de veredicto — hay que medir
extensiones, corrimiento y tinta antes de gritar regresión.

**Dónde quedó:**

- `src/compositions/hilton/BetweenStCumpleCarrusel.tsx` — el legal en dos `<div>`
  (uno por línea; con un `<br/>` suelto JSX deja el salto del código como espacio
  y descentra la línea).
- Entrega: `out/hilton/between/entrega-st-cumple-09-09-r2/` — la story 2 y su
  `GUIA CM`, 2250×4000.
- **Subida a STS** (`1lupGWfILmS9JQ4tznkqqddTKOh6uFtEe`) **reemplazando el mismo
  archivo**: id `1lCkTS4wzhTi3a0CJR3X6r001Ihtx8kxZ`, **el enlace no cambió**.
  Verificado por `md5Checksum` (Drive = local, `6d2db4a702…`), por `parents` y
  comprobando que la story 1 sigue intacta (`b5671a6242…`, fecha 07-09).
- **Reproducible byte a byte**: `cmp` limpio entre el render y el archivo entregado.
- `clients/hilton/CLAUDE.md` — la redacción real, la tabla de medidas y la regla
  del legal acumulativo.
- `clients/hilton/grillas/between-septiembre-2026.md` — instantánea nueva, que es
  la base del diff de mañana.

**Qué sigue:**

1. **El reel Café Bombón** — está agendado el **09-09 (mañana)**, no existe
   composición todavía y el cliente acaba de contestar la pregunta que lo tenía
   frenado desde el 27-08. Hay propuesta escrita en
   `clients/hilton/PROPUESTA-reel-cafe-bombon.md`. ⚠️ **Antes de producir hay que
   preguntarle a Eli** si esa propuesta es la que el cliente aceptó: el estado
   quedó en `REVISAR CONTENIDO`, no en `OK PARA DISEÑAR`, y lo único que pidieron
   por escrito es el legal de «imagen referencial» — que **no es el mismo legal**
   de esta sesión.
2. La lámina de FEED del cumpleaños ya la corrigió Eli; el slot sigue en
   `REVISAR CONTENIDO` esperando que el cliente lo marque.

**Abierto:**

- ⛔ **`BetweenCumple.tsx:112` y `BetweenSeptiembre.tsx:794` siguen con el legal
  VIEJO** («de cumpleaños», y la primera además dice «carnet»). Quien rehaga una
  de esas dos tiene que corregirlo en la misma pasada.
- ⚠️ **El QA marca la story 2 con 122 px** dentro de la franja inferior de Meta,
  contra los 90 de antes y los **104 de la propia plantilla de Eli**. En orgánico
  funciona con la sombra; **si la pieza pasa a pauta hay que rehacer el pie**, no
  sólo subirlo. Es decisión de Eli.
- Siguen en pie del cierre de la mañana: Between **sin `clients/hilton/reglas.yaml`**
  (`qa/motor.py --marca hilton` no corre), las **`GUIA CM`** en local sin decidir
  cómo llegan al CM (9 días), y **`BETWEEN.logo.cafe` apuntando a un PNG negro**.

## 2026-09-08 (CIERRE DEL DÍA) · Eli (Windows) — resumen para el relevo

Jornada completa sobre **BETWEEN, stories de la S3** (14, 16 y 18-09): ocho rondas
con Eli en vivo. Las entradas de cada ronda están más abajo; esto es el estado.

**Qué se hizo:** se rehicieron de cero las tres historias de la S3 —las del set
del 31-08 no se podían editar porque sus fotos de origen ya no existen— y se
entregaron a la carpeta STORIES del Drive. En el camino se cambió el método de
imagen de la marca (las escenas ahora se GENERAN con el hueco del texto adentro,
no se recortan del banco 4:5), se dibujaron tres ilustraciones nuevas para la
pieza del 18 y se arreglaron dos defectos del sistema que afectaban a toda la
marca.

**Dónde quedó:**

| Pieza | Estado |
|---|---|
| `BW ST 14-09 Cuando es hora de cafe.png` | ✅ **APROBADA** |
| `BW ST 16-09 Cowork te esperamos.png` | última corrección entregada (kerning del horario) — **falta el OK de Eli** |
| `BW ST 18-09 Saludo Fiestas Patrias.png` | ✅ **APROBADA** |

Carpeta STORIES: `1SNBRIvKLvQSC2bYF3u5_oPL5UumIo-gM`. Las tres se subieron
**reemplazando el mismo archivo**, así que los enlaces que ya tiene Eli siguen
sirviendo. Verificado por `md5Checksum` y por `parents` en cada subida.

Código: `src/compositions/hilton/BetweenStS3.tsx` y `BetweenIlustraS3.tsx`.
Scripts: `between-st-s3-generar.py` (escenas), `-materiales.py` (logo café +
textura de papel), `-fotos.py` (retoques y recorte), `-entrega.py` (empaque y
subida, con `--solo` para no re-subir una pieza aprobada).
Todo rendido, con QA pasado y commiteado ronda por ronda.

**Qué sigue:** esperar el OK de Eli sobre la **16-09**. Si lo da, la S3 de stories
queda cerrada y lo siguiente de Between es la S4 (21-09 strudel, 22-09 primavera)
y la S5 (28-09 humor to go, 30-09 plateada), que están todas `OK PARA DISEÑAR` en
la grilla y son de las 8 historias que **no se pueden editar: se rehacen**.

**Abierto:**
- ⛔ **`BETWEEN.logo.cafe` apunta a un PNG NEGRO `#000000`**, no al café de marca.
  Se generó el archivo correcto (`logo-cafe-marca.png`) y se usa en la S3, pero el
  token NO se tocó porque lo usan `BetweenCumple`, la G2 de `BetweenSeptiembre` y
  la tarjeta del carrusel del cumpleaños. **Quien rehaga una de esas tres tiene
  que cambiarle el logo en la misma pasada.**
- Las **guías `GUIA CM`** (con la zona del sticker marcada) siguen sólo en local,
  en `out/hilton/between/entrega-st-s3/GUIAS CM/`. Van **ocho días** sin que se
  decida cómo le llegan al community manager: Slack o una subcarpeta del Drive que
  el portal no levante. Es decisión de Eli.
- **Between sigue sin `clients/hilton/reglas.yaml`**, así que
  `qa/motor.py --marca hilton` se niega a correr. Hay que escribirlo con Eli
  porque son sus medidas.
- El comentario de `STORIES!N` («se puede entender que estuvimos cerrados») sigue
  **sin tachar** en la grilla. Se atacó por la foto —mesa servida y en uso— y el
  copy va literal del brief ya corregido; si el cliente quería otra redacción, la
  decide el CM.
- ⚠️ Si la **16-09** pasa a PAUTA hay que revisar el titular: es beige sobre pared
  clara (1,33:1 medido) por pedido expreso de Eli. En orgánico funciona con la
  sombra; comprimido y en pantalla chica se pierde.

**Y una cosa que NO es de Between, del cierre:** quedaba sin commitear una pasada
de **`/al-dia` a DOUBLETREE** (grilla modificada el 08-09 15:31Z por Carlos
Figueroa). Entra en este commit, y trae dos cosas que alguien tiene que mirar:
- **un comentario nuevo** en FEED col G (10-09) — «POST · NOCHE DE BODAS»: el
  carrusel de agosto tiene un error, debería decir *Noche de Bodas*. **Eli ya lo
  entregó** (`C1 S1 N°1/2.png` en `S2 HILTON SEP 2026/DT/NOCHE DE BODAS`);
- **producible hoy en DT: sólo la estática del Día del Turismo (27-09)**. El
  estático de Opinión Booking (14-09) sigue bloqueado desde el 03-09 porque la
  carpeta de reseñas devuelve 0 archivos por el conector y falta el texto literal.
  Y DT sigue **sin ADN**: no hay `marca.json`, ni `reglas.yaml`, ni
  `src/brand/doubletree.ts`.

## 2026-09-08 (ronda 8) · Eli (Windows) — BETWEEN: el tracking no llegaba a las cifras tabulares

**Qué dijo Eli**, sobre el bloque del horario de la ST 2: «recuerda el uso de
kerning y tracking de separación optima ya que se pierde y esta muy junto. Debe
verse armonico y bien visualmente. Separalos un poco en los lados espacio entre
letras no parrafos».

Eran **tres** cosas, y la segunda es un defecto del SISTEMA que afectaba a toda
pieza de Between con horario.

### 1. El tracking del horario ya estaba en el kit y no se estaba usando

La línea iba en 0,02em. La marca ya tiene el valor: el token
`BETWEEN.trackingHorario` es 7 px y `Dato` lo aplica a cuerpo 29–30 (~0,24em), y
`CajaTexto` —el chip de horarios de Eli— usa 3 px a cuerpo 30 (0,10em). La línea
va en ExtraBold, que pide más aire que un semibold, así que se tomó el valor del
chip como piso: **0,10em**. Con eso las dos líneas miden 443 y 467 px dentro de
los 722 útiles del cartel.

### ⛔⛔ 2. EL HALLAZGO: `letter-spacing` no alcanza a un `inline-block`

`cifrasTabulares` mete cada dígito en un `inline-block` de ancho fijo, que es lo
que alinea las cifras. Pero **Chrome no le aplica `letter-spacing` a una caja
atómica**. O sea que en una línea con tracking abierto las LETRAS se separan y las
CIFRAS no. Medido a 0,10em: letras con 5,8–10,6 px de hueco y los dígitos de cada
grupo **pegados, 0,5 y 2,9 px**. Se veía como si la hora estuviera en otra
tipografía.

Corregido en `cifrasTabulares`, que ahora acepta `trackingEm` y lo replica como
`marginRight` en cada dígito — que es lo que hace `letter-spacing` con un carácter
normal. **Por defecto 0, así que ninguna pieza ya aprobada cambia.**

> **Regla:** toda vez que una línea con cifras tabulares lleve tracking, hay que
> pasárselo también a `conCifras`. Vale para horarios, precios y cualquier dato.

### 3. Lo que el tracking parejo destapa en una hora: los dos puntos flotan

Con la línea abierta, el «:» trae sus propios laterales y encima recibe el
tracking por los dos lados: quedaba con 12,0 y 13,0 px alrededor contra 5,3 entre
dígitos. Eso es **kerning**, no tracking: se corrige por PAR. Cada «:» va en un
span que anula el tracking y se mete 2 px por lado (`horarioKerneado`). Medido
después: 5,3–7,7 px, el mismo rango que los dígitos.

⚠️ Los huecos entre dígitos siguen levemente desiguales (2,9 a 7,7) y eso **es
correcto**: la caja tabular iguala los AVANCES, no la tinta, y el «2» es 34
milésimas más angosto que el «0». Igualar la tinta rompería la alineación de
cifras, que es para lo que existe la caja.

### El orden del diagnóstico, que queda escrito

**Primero el largo, después el tracking, después el kerning del par.** Si hay que
achicar una línea más de ~20 % para que quepa, ningún tracking la va a salvar
(ronda 7); con el cuerpo bien, se abre el tracking con el valor del kit; y recién
ahí se miran los pares que quedaron flotando.

### Entrega

Sólo la 16-09, reemplazando el mismo archivo en STORIES y verificada por `md5`. La
14-09 y la 18-09 están aprobadas y no se tocaron. `between-qa.py`: la 16-09 y la
18-09 limpias; los dos avisos que quedan son los del cierre de la 14-09.

## 2026-09-08 (ronda 7) · Eli (Windows) — BETWEEN S3: el horario partido en dos y el titular en beige

**Qué pidió Eli**, recortando la línea del horario: «este texto está muy pegado. y
el otro quiero que sea beige de BW».

### «Muy pegado» no era el tracking: era el LARGO de la línea

El horario iba en UNA línea de **36 caracteres** que a cuerpo 45 mide 826 px
contra los 722 útiles del cartel, así que `CajaDato` la achicaba hasta **~31 px**:
altura de mayúscula 23 contra las 33 de la pieza aprobada. A ese cuerpo y con
tracking cero, las letras se apelmazan. Aflojar el tracking lo empeora, porque
encoge más el cuerpo.

Se partió en dos líneas y entró al cuerpo pleno de la marca: medido con la fuente
real, «LUNES A VIERNES» da 402 px y «08:00 A 22:00 HRS.» 421 px a cuerpo 45 con
+0,02em, las dos con holgura dentro de 722. Y es la estructura del referente, que
también parte el horario en dos.

> **Regla:** cuando una línea de dato hay que achicarla más de ~20 % para que
> quepa, el problema es el LARGO, no el cuerpo ni el tracking. Se parte la línea.

### El titular en beige: decisión de Eli, y está medida

Sobre esta pared el beige da 1,33:1 de contraste contra los 1,90:1 del café — está
medido y quedó escrito en la ronda 5, y Eli lo pidió igual después de eso. Manda
ella. Lo que lo sostiene es la sombra que `TitularBetween` aplica sola en `tono
beige`, que le da un canto oscuro suave y despega la letra de la pared: queda como
tipografía clara sobre fondo claro, que es un registro legítimo y es lo que hace
el referente (ahí la pared es gris media). **Si la pieza pasara a pauta hay que
revisarlo**: en pantalla chica un 1,33:1 se pierde.

### Estado

La 14-09 y la 18-09 **APROBADAS**, no se tocaron. La 16-09 reemplazada sobre el
mismo archivo en STORIES y verificada por `md5`. `between-qa.py`: la 16-09 y la
18-09 limpias; los dos avisos que quedan son los del cierre de la 14-09, ya
aprobados.

**Abierto:** las guías del CM siguen sólo en local (octavo día); el comentario de
`STORIES!N` sin tachar; Between sin `reglas.yaml`; `BETWEEN.logo.cafe` sigue
apuntando al PNG negro para las tres piezas viejas que lo usan.

## 2026-09-08 (ronda 6) · Eli (Windows) — BETWEEN S3: la ST 3 APROBADA; la tipografía de la ST 2, corregida

**Qué dijo Eli:** «La st 3 aprobada, la ST 2 necesito que cuides como están los
textos, se están solapando y no tienen kernig optimo».

**ST 3: APROBADA.** No se toca ni se re-sube.

### Eran TRES defectos, y los tres se midieron sobre el render

1. **El aire script → caja alta daba 12,5 px.** El token
   `BETWEEN.aire.scriptATitulo` vale 9 y está medido sobre una script SIN
   descendentes; «Puedes venir» tiene la «P» de Brushwell con una cola larguísima
   que se come esos 9. Va en 30 con el opt-in `aireScriptATitulo`; medido después:
   35 px. Ojo con la comparación: dentro de la bajada la interlínea de tinta es
   ~13 px, así que con 12,5 el salto ENTRE niveles era igual al salto DENTRO de un
   nivel — la jerarquía al revés.

2. **El «kerning»: −0,024em es correcto para 8 letras, no para 14.**
   `BETWEEN.trackingCaps` está calibrado sobre «PERFECTO»; sobre «¡TE ESPERAMOS!»
   acumula ~36 px de cierre y las letras salen comprimidas. Se agregó
   `trackingCapsEm` a `TitularBetween` como **opt-in** —el token no se toca porque
   lo usan piezas aprobadas— y acá va en −0,006em.
   ⚠️ Aflojar el tracking ensancha la línea y `encoger` baja el cuerpo: quedó en
   altura de mayúscula 75 px, el orden de la pieza aprobada del cumpleaños (72).
   Y hay un TECHO calculado: la pared clara llega a x≈909 y el bloque va centrado
   sobre el eje, así que una línea centrada no pasa de 738 px de tinta — más
   grande no cabe sin salirse al follaje o sin descentrar, y descentrar no es la
   gramática de Between.

3. **El ritmo DENTRO del cartel estaba invertido.** `CajaDato` mide 66 px con el
   texto centrado, así que ya aporta ~16 px de aire; con `marginTop: 2` el salto
   horario → bajada quedaba en ~18 px, menos que los ~40 de interlínea de la
   propia bajada. Corregido a 22 y 26: medido después, horario → bajada 51 px,
   bajada → cierre 44 px, dentro de la bajada ~13 px.

### La regla que deja

Los tres son **el mismo error de método**: usar un token medido en otra línea sin
comprobarlo en ésta. El aire de 9, el tracking de −0,024em y el margen de 2
estaban todos «según el manual», y los tres estaban mal acá — porque la línea
tiene descendentes, porque tiene 14 letras y porque la caja de arriba ya traía
relleno propio.

> **Antes de dar por bueno un bloque de texto: medir sobre el render los saltos de
> tinta a tinta y comprobar que el salto entre niveles es mayor que el salto
> dentro de cada nivel.** Tres minutos, y caza las tres cosas.

### QA y entrega

`between-qa.py`: 3/5 limpias, con los dos avisos ya aprobados del cierre de la
14-09. Sólo se re-subió la 16-09, reemplazando el mismo archivo en STORIES y
verificada por `md5`. La 14-09 y la 18-09 están aprobadas y no se tocaron.

**Abierto:** las guías del CM siguen sólo en local (séptimo día); el comentario de
`STORIES!N` sin tachar; Between sin `reglas.yaml`; `BETWEEN.logo.cafe` sigue
apuntando al PNG negro para las tres piezas viejas que lo usan.

## 2026-09-08 (ronda 5) · Eli (Windows) — BETWEEN S3: subir el texto de la 2, dos banderas en la 3

**Qué pidió Eli**, marcando las piezas con rojo: en la ST 2, «solo subir el texto
según lo que te pido en el ejemplo» —una llave que envuelve el titular, el cartel
y el cierre, con una flecha hacia arriba—; en la ST 3, «pon dos banderas en la
dirección que te dejo el ejemplo 2 y que puedas acomodar más los textos».

### ⛔ La ST 2: «titular beige» y «titular arriba» no pueden ir juntos

Medido: arriba la pared es clara y el beige da **1,33:1** mientras el café da
1,90:1; abajo es exactamente al revés (beige 2,38–2,80, café 1,08). O sea que se
puede tener el titular beige (abajo, como en la ronda 4) o el titular arriba (en
café), **no las dos cosas**. Mandó el pedido nuevo: subió y pasó a café — que
además es lo que hace el referente, tipografía oscura sobre pared plana.

Y aparecieron dos cosas más que quedaron escritas:

- **hay una franja PROHIBIDA, y 610–820**: ahí la foto se parte (izquierda pared
  clara, derecha follaje oscuro) y ninguna de las dos tintas se lee en todo el
  ancho. Ningún titular puede quedar ahí;
- **el titular tiene un TECHO**: buscando el borde del follaje fila por fila, la
  pared se mantiene clara en todo el ancho hasta y≈590 y a 620 se derrumba a
  x=642. El bloque mide 180 px, así que arranca en 405 — 41 px de aire bajo el
  lockup en vez de los 77 del token. Concesión consciente: entre el token y que se
  lea, gana que se lea. El ancho baja a 770 porque con 810 el «!» final se salía
  al follaje.

El cierre entró al cartel (beige, cursiva 38 px) porque la llave de Eli lo
envuelve con el horario y la bajada, y porque suelto a esa altura tendría que ser
beige mientras el titular es café: dos tintas sueltas se leen como descuido. El
cartel cierra en y≈885 y **la mesa servida se queda con toda la mitad de abajo**.

### La ST 3: dos banderas apuntando hacia afuera

`BanderaChile` ganó `espejo`, y está hecho como un `scale(-1 1)` **por fuera** del
`rotate`: así, con el mismo `giro`, la espejada apunta al lado contrario y el par
queda simétrico hacia afuera — las dos flechas en «V» que dibujó Eli.

Van **dentro del bloque del brindis**, en absoluto sobre sus flancos vacíos (el
`viewBox` mide 760 y las tazas ocupan 248–512, así que sobran ~230 px por lado).
No le quitan ancho al motivo principal y el cartel no crece de alto: ese aire es
el que se usó para «acomodar más los textos» (30 px del dibujo al titular, 34 al
párrafo, 34 a la caja del saludo).

⛔ **Y un defecto de dibujo que costó una pasada:** las dos banderas salieron
CORTADAS, leyéndose como cintas sin palo. La bandera se dibuja recta y se inclina
con `rotate` sobre (150,130), y al girarla el pie del mástil —(56,224)— se va a
y≈252, fuera del `viewBox` de 240 de alto. Subió a 270. **Regla: cuando un dibujo
se inclina, hay que evaluar sus puntos extremos girados y comprobar que caben.**

### QA y entrega

`between-qa.py`: **3/5 limpias**, con los dos avisos ya aprobados del cierre de la
14-09. La 14-09 no se tocó ni se re-subió. La 16-09 y la 18-09 reemplazadas sobre
el mismo archivo en STORIES, verificadas por `md5` y por `parents`.

**Abierto:** las guías del CM siguen sólo en local (sexto día); el comentario de
`STORIES!N` sin tachar; Between sin `reglas.yaml`; y `BETWEEN.logo.cafe` sigue
apuntando al PNG negro para las tres piezas viejas que lo usan.

## 2026-09-08 (ronda 4) · Eli (Windows) — BETWEEN S3: cinco correcciones, y una era un defecto del kit

**Qué pidió Eli:** en la ST 2, agrandar el texto de abajo («que sea italic pero un
poco más grande»), sacar el titular «Puedes venir…» del recuadro café, y que el
logo sea «el café de between ese color». En la ST 3, una **ilustración cute de la
bandera de Chile** y que el cuadro beige sea una **textura de papel**.

### ⛔⛔ El hallazgo: `BETWEEN.logo.cafe` no es café, es NEGRO PURO

El token del kit dice `cafe` y apunta a `logo-negro.png`, cuyos píxeles opacos
miden `#000000`. O sea que **toda pieza que pidió «el logo en café» venía saliendo
con el logo negro**, fuera de la paleta de Between. Eli lo cazó a ojo y llevaba dos
rondas insistiendo.

El archivo correcto (`logo-cafe-marca.png`: el café `#675B49` sobre el canal alfa
del logo oficial) lo genera `scripts/between-st-s3-materiales.py`. **El token NO se
tocó**: lo usan piezas ya aprobadas y cambiarlo las re-flujaría. Queda escrito en
el manual que quien rehaga `BetweenCumple`, la G2 de `BetweenSeptiembre` o la
tarjeta del carrusel del cumpleaños tiene que cambiarles el logo en la misma
pasada — y ahí sí corregir el token.

### ST 2 — un titular beige suelto se ubica midiendo POR TERCIOS

Sacar el titular del cartel obligó a decidir a qué altura va, y el promedio de la
franja **no alcanza**. Medido por tercios de la columna, el contraste del beige:

| y | izq | centro | der |
|---|---|---|---|
| 620 | 1,36 | 1,50 | 2,20 |
| 800 | 1,41 | 2,07 | 2,45 |
| **880** | **2,71** | **2,19** | **2,87** |

El tercio izquierdo sigue siendo pared clara hasta y≈860: un titular beige arriba
se leería por la derecha y desaparecería por la izquierda — el defecto que Eli
marcó. La primera altura donde pasa de 2:1 en los TRES tercios es y=880.

**Regla que deja:** para texto suelto sobre foto, el promedio de la franja miente.
Se mide en los tres tercios y manda el peor de los tres.

Con el titular afuera, el cartel se queda sólo con el dato y baja a y=1330 (bajo
la taza, que ocupa 1120–1320), y el sitio del sticker de enlace se mueve a la
**pared**, que con el pie ocupado es la superficie más limpia de la pieza.

El cierre pasó de 28 a **38 px** en cursiva: 28 es la medida del LEGAL de una
story, y cuando el brief manda un cierre con contenido se lee chico. Va en y=1532
porque la cursiva a 38 baja más de lo que uno calcula (en 1540 el QA marcaba 5 px).

### ST 3 — papel sintetizado y bandera en una tinta

**La textura de papel se sintetiza, no se genera con IA:** el tinte tiene que caer
exacto en `#FFF9EB` y con semilla fija se reproduce byte a byte. Grano fino +
fibra horizontal + manchado muy leve, desvío final 2,86 niveles sobre 255. El
primer intento tenía el manchado casi al doble y la hoja se leía como **nubes** —
el papel del referente es parejo con grano, no jaspeado.

**La bandera va en UNA tinta y manda la geometría:** Eli pidió la bandera de Chile
y, en el mismo mensaje, los colores de Between. El rojo y el azul no están en la
paleta, así que se dibuja como se dibuja una bandera en una ilustración de una
tinta — cantón cuadrado, estrella calada en el color del papel, división
horizontal. Ninguna otra bandera tiene esa combinación, así que se lee chilena sin
el tricolor. Ondea, el mástil es corto y va inclinada: una bandera recta se lee
como un ícono de menú de idioma.

⚠️ Dos defectos que sólo aparecieron al zoom y hay que revisar siempre en un
dibujo: el cantón, puesto a ojo, quedaba 14 px más abajo que la división y dejaba
un escalón en la esquina (sus bordes tienen que ir sobre las mismas curvas de la
tela, evaluadas en x=118); y la división sobresalía del borde libre de la tela y
se veía una espina.

### QA y entrega

`between-qa.py`: **3/5 limpias**, con los dos avisos ya aprobados del cierre de la
14-09. **La 14-09 no se re-subió** — está aprobada, y para eso se le agregó
`--solo` al script de entrega. La 16-09 y la 18-09 quedaron reemplazadas sobre el
mismo archivo en STORIES, verificadas por `md5` y por `parents`.

**Abierto:** las guías del CM siguen sólo en local (quinto día); el comentario de
`STORIES!N` sigue sin tachar; Between sigue sin `reglas.yaml`; y queda pendiente
corregir `BETWEEN.logo.cafe` cuando se rehagan las tres piezas que lo usan.

## 2026-09-08 (ronda 3) · Eli (Windows) — BETWEEN S3: la 14-09 APROBADA, y las otras dos rehechas

**Qué dijo Eli:** «La primera ST queda aprobada, para la segunda ST el logo es el
color café de between, y los titulos en beige por favor para que se lea y sea
visible. Para la ST 3 sucede que el contexto es 18 de septiembre de fiestas
patrias de Chile, necesito que sea detalles ilustrados y haz más similar a la
referencia con los colores de between.»

**14-09: APROBADA.** No se tocó. Se le agregó `--solo` a
`scripts/between-st-s3-entrega.py` para poder re-subir las otras dos sin volver a
tocar una pieza aprobada.

### ST 2 — «los títulos en beige para que se lea»: la tinta la manda el fondo

Medido: sobre la pared beige de la foto (L=177) el beige `#FFF9EB` da **1,43:1**
de contraste y el café `#675B49` da 2,0:1. O sea que cambiarle el color al texto
por sí solo lo hace DESAPARECER — y en esta foto el beige no pasa de 1,9:1 hasta
y≈880, que es donde empieza la mesa y queda a 240 px de la taza.

La salida es la que el cliente dejó escrita («cuando no se logra visualizar los
textos, puedes dejarlo en una caja del color café #675B49»): el titular, el
horario y la bajada entran a **un solo cartel taupe con todo el texto en beige**,
y el lockup se queda en **café** arriba, sobre la pared clara. Las dos cosas que
pidió Eli, y con la mesa servida entera a la vista.

> **La regla que deja:** se mide la luminancia de la franja donde cae el texto.
> Bajo L≈120 va beige suelto; sobre L≈150 va café suelto; y si el texto tiene que
> ser beige sobre fondo claro, no se cambia la tinta — se le pone el cartel debajo.

### ST 3 — detalles ilustrados, y la regla del trazo queda acotada

El manual prohíbe dibujar trazos nuevos para Between, y en las rondas 1 y 2 eso se
respetó (el brindis se resolvió fotografiado). Acá Eli pidió lo contrario
explícitamente, así que la regla cede **acotada**: se puede dibujar un motivo
nuevo cuando la diseñadora lo pide, el motivo no existe en su `.svg`, va en UN
solo color de marca, y el trazo es de grosor constante con puntas redondeadas
como el referente — sin imitar el pincel de Brushwell.

Entran dos motivos, en `src/compositions/hilton/BetweenIlustraS3.tsx`:
**guirnalda de banderitas** y **brindis de dos tazas**, los dos en café `#675B49`.
Nada de rojo, azul ni blanco de bandera: el 18 se lee por las banderitas, no por
el tricolor — Eli pidió los colores de Between.

**El brindis costó tres intentos y va sin brazos ni manos, a propósito.** La mano
maciza dejó dos manchas que sobre el beige se leían como borrones; la de contorno
dejó dos aros cruzando la taza y el asa. Una mano mal dibujada es peor que
ninguna, que es la misma lección que ya estaba escrita para las manos de IA. Y la
geometría que sí funciona quedó medida en el manual: bases a 160 px, giro de 10°
sobre la base hacia el centro (ojo con el sentido), bocas a 8 px, asa al lado de
afuera y chispas cortas metidas entre las dos columnas de vapor.

**Y «más similar a la referencia» resultó ser la PROPORCIÓN.** La ronda 2 ya tenía
panel beige y ambiente detrás; lo que no tenía era que el cartel ocupara ~80 % del
alto con la foto como marco. Al invertir eso, la pieza se lee como el referente.
El cartel se ajusta a su contenido: con `minHeight` fijo quedaban 160 px de beige
muerto al pie. Y como el brindis pasó a ser dibujo, la foto del brindis sobraba —
el fondo es ahora el local muy desenfocado, con las ampolletas como manchas de luz.

### QA y entrega

`between-qa.py`: **3/5 limpias**, con los dos avisos conocidos del cierre del
14-09 (55 px en la franja de Meta, ya aprobado). Las tres subidas **reemplazando
el mismo archivo** en STORIES, verificadas por `md5` y por `parents`: los enlaces
no cambiaron.

**Abierto:** las guías del CM siguen sólo en local (cuarto día); el comentario de
`STORIES!N` sigue sin tachar en la grilla; Between sigue sin `reglas.yaml`.

## 2026-09-08 (ronda 2) · Eli (Windows) — BETWEEN S3: las tres stories rehechas con foto PRODUCIDA

**Qué pasó:** Eli devolvió las tres de la mañana — «Hazlos de nuevo las 3 stories
ya que no cumplen, **debes dejar mejores fotografías, mejor imagenes hazlo en
conjunto a magnific**» — y adjuntó tres referentes en Drive
(`12S5bEGzPtZmE82U_ZxrboyZwsvOOQoZ0`, bajados a
`raw/hilton/between/ref-s3-eli/`), con la condición: «deben ser colores y fondos
de Between, pero puedes guiarte de elementos de la referencia para hacerlos
similar. Con la identidad visual de BW». Se rehicieron las tres y quedaron
**reemplazadas en el mismo archivo** de la carpeta STORIES, así que los enlaces
que ya tenía no cambiaron.

### ⭐⭐ La lección, y corrige la de la mañana

La ronda 1 gastó el día resolviendo **cómo recortar** el banco 4:5 a 9:16 —hasta
subir las fotos a 2× con el upscaler para ganar libertad vertical— y funcionaba.
Y aun así las tres estaban mal, porque el problema no era el recorte:

> **Una historia de Between no se recorta: se PRODUCE.** Si la foto no trae el
> hueco que la diagramación necesita, el texto termina apoyado en cajas taupe — y
> con tres piezas resueltas así, las tres se parecen entre sí.

Los tres referentes de Eli hacen lo contrario y **el hueco es su tema**: un torso
de color liso que llena el cuadro, una pared plana en el tercio de arriba, un
plano del local muy desenfocado. En los tres el titular va grande y sin caja.
El `escalar 2x` de la mañana no se deroga: pasa a ser el plan B, para cuando hay
que llevar una foto real del banco a 9:16.

### Las tres, y qué elemento se tomó de cada referente

| Pieza | Referente | Traducido a Between |
|---|---|---|
| **14-09** | torso con camisa azul llenando el cuadro + taza sostenida abajo | **campo de color café `#675B49`** (un sweater liso) + taza blanca con rosetón en el tercio inferior. Los 880 px de campo limpio dejan el quiz de su porte REAL, 660×360 |
| **16-09** | pared plana gris arriba + titular enorme + mesa con notebook | **pared beige** desenfocada arriba → y por eso es la **primera pieza de Between con titular en tinta café**, que es para lo que el kit define ese color |
| **18-09** | panel crema sobre la foto del local + dos manos brindando dibujadas | **panel beige `#FFF9EB`** con tinta café y el lockup café adentro; y el **brindis va con dos tazas de verdad, en la fotografía** |

⭐ El brindis en la FOTO y no dibujado es una decisión de sistema: el repertorio de
línea de Between son los trazos del `.svg` de Eli y ahí no hay un brindis; el
manual prohíbe dibujar o generar trazos nuevos. Pedírselo al generador con las dos
tazas reales como referencia respeta las dos cosas.

### Lo que hubo que arreglar después del generador

1. **El color de marca no llega exacto.** El sweater salió `#564134`. Corregido a
   `#675B49` con ganancia multiplicativa por canal sobre máscara blanda de
   luminancia. ⚠️ Y la ganancia se mide sobre un rectángulo de **medio tono**: el
   primer intento la calculó sobre el promedio de la máscara —que arrastra las
   sombras y da `#412f25`— y pedía ×1,57–1,97, reventando los medios. **El color
   de una prenda es su medio tono, no su promedio con sombras.**
2. **La IA metió una marca de tercero:** el logotipo de un fabricante de
   computadores en la tapa del notebook. Fuera, con la interpolación horizontal.
3. **«Los dos tercios de abajo son MESA de madera» produjo una COSTURA.** El
   generador pegó un plano recto en primer plano con un salto horizontal visible a
   media pieza. Se rehizo pidiendo que la MISMA escena siga hacia abajo y
   prohibiendo la línea. Vale como regla de prompt.
4. **El bloque de dato del 16-09 tapaba la taza.** Puesto al pie como en el
   referente, las dos cajas caían sobre y=1120–1320, que es donde está la taza: la
   pieza que habla del café lo escondía. Subió a bajo el titular. **La estructura
   del referente se respeta hasta que choca con la foto propia; ahí manda la foto.**
5. **Las manos, revisadas al 300 %** una por una — las tres pasan: pulgar y dedos
   con uña, nudillos y pliegues, sin masas lisas.

### QA

`between-qa.py`: **3/5 limpias**, con dos avisos por el cierre del 14-09, que
entra **55 px** en la franja inferior de Meta. Es menos que los 90 px del legal
que Eli aprobó en la ST 2 del cumpleaños, y no se puede subir más: medido, la taza
y la mano llegan hasta y=1600. Vale en orgánico; si pasa a pauta, hay que subirlo.
`qa/motor.py --marca hilton` sigue negándose: Between no tiene `reglas.yaml`.

**Los prompts, textuales, quedaron en `PROMPTS-DE-ELI.md` §4** — «recuerda el
prompt y resultado es importante».

**Abierto:**
- Las **guías del CM** siguen sólo en local (`out/hilton/between/entrega-st-s3/GUIAS CM/`).
  Es el tercer día que queda pendiente cómo se le hacen llegar.
- El comentario de `STORIES!N` sigue sin tachar en la grilla.
- Las tres escenas generadas (48 MB) van forzadas al repo: Nano Banana **no es
  determinista** y sin ellas las piezas no se pueden volver a armar iguales.

## 2026-09-08 · Eli (Windows) — BETWEEN S3: las tres stories que faltaban, entregadas

**Qué se hizo:** Eli pidió la S3 de stories — «lo harás nuevamente con la
información que ya tienes», guiándose del brief y de las referencias de Pinterest
de la grilla, «pero ligado siempre a la marca de Between», y dejando **aire libre**
donde va la interacción en vez de dibujarla. Se rehicieron las tres de cero, se
pasaron por la compuerta y quedaron **subidas al Drive**.

### Lo entregado

`out/hilton/between/entrega-st-s3/` — 2250×4000 · 150 ppp:

    BW ST 14-09 Cuando es hora de cafe.png
    BW ST 16-09 Cowork te esperamos.png
    BW ST 18-09 Saludo Fiestas Patrias.png
    GUIAS CM/ …2 copias con la zona marcada   ← internas, NO van al Drive

Subidas a la carpeta **STORIES** (`1SNBRIvKLvQSC2bYF3u5_oPL5UumIo-gM`), el enlace
que pasó Eli. Verificado por `md5Checksum` contra el archivo local y por
`parents`: las tres están DENTRO de STORIES, no en «Mi unidad» (con scope
`drive.file` eso puede pasar en silencio).

Composición: `src/compositions/hilton/BetweenStS3.tsx`
(`BW-S3-HoraCafe` · `BW-S3-Cowork` · `BW-S3-Dieciocho` + dos `-Guia`).

### Por qué se rehicieron y no se editaron

`StHoraCafe`, `StCowork` y `StDieciocho` del set del 31-08 están entre las **8
historias que ya no se pueden rehacer**: sus fotos de origen no existen en ningún
disco. Y había que rehacerlas igual, porque arrastraban tres defectos que hoy son
reglas escritas:

1. la del 14-09 llevaba una **modelo de la sesión de julio 2023 con la cara
   enfocada**, y el cliente pidió el 08-09 «modificar el aspecto de estas
   modelos, ya no las podemos usar tal cual»;
2. las tres **dibujaban el sticker** de Instagram;
3. la del 16-09 mostraba el local **vacío**, que es justo lo que dispara el
   comentario abierto «se puede entender que estuvimos cerrados».

### El hallazgo de la jornada: el 4:5 del banco contra el 9:16 de la story

Es el problema de fondo de toda historia de Between y hasta hoy no estaba
nombrado. Al recortar 4:5 a 9:16 se conserva **todo el alto** y se corta el
ancho, o sea que el sujeto no se mueve de altura: en las tres fotos caía justo
donde va el sticker. Se resolvió subiendo las fuentes a **2× con el upscaler de
Freepik** y recortando una ventana más chica que el alto total, que es lo único
que da libertad vertical. Las tres salieron **reduciendo** (×0,90 · ×0,98 ·
×1,00): ninguna ampliada, contra el ×1,42 que obligaba el camino anterior.
Receta y tabla de franjas en el manual, § «S3 · LAS TRES STORIES».

### Las decisiones de imagen, una por una

- **14-09** `mesa-cafe-2piso.jpg` — capuchino en la mesa del lounge. Se eligió
  por medición: su franja calma está en y=480–640 (L=45) para el titular, y deja
  **madera limpia de 1360 abajo** para el quiz.
- **16-09** `cowork-terraza.jpg` — mesa de la terraza con notebook, taza,
  libreta y celular, con las ampolletas encendidas. La ventana se cerró a 2300 px
  por dos razones medidas: dejar fuera la **sombrilla blanca** (el lockup beige
  desaparecía encima) y acortar la franja de sillas y adoquín del pie, que se
  comía media pieza cuando el mensaje es «te esperamos».
- **18-09** `desayuno-completo-2.jpg` — desayuno para compartir. **KIMBO borrado**
  con dos cajas de interpolación horizontal, no una: la línea donde la taza se
  apoya en el platillo cruza la punta de la barra gris y con una caja ancha
  salía aplanada. Verificado al 100 % en la pieza final.

Las tres estaban **sin usar** en septiembre: se cruzó contra `BetweenSeptiembre.tsx`
para no repetir foto dentro del mes.

### Las referencias de Pinterest, traducidas

Los tres pines vienen en la grilla y se bajaron por `i.pinimg.com` (la página del
pin no expone `og:image`, pero el HTML sí trae la URL). De cada uno se tomó la
ESTRUCTURA, no el aspecto: la tarjeta con la pregunta arriba y la taza abajo
(14-09) → titular + zona reservada; el antetítulo espaciado con el horario al pie
(16-09) → script Brushwell + caja taupe; el panel de color sobre la foto (18-09)
→ la caja `#675B49`, que es el mecanismo que el cliente autorizó por escrito.

### QA

`scripts/between-qa.py` → **5/5 limpias**, incluidas las dos guías. `qa/motor.py
--marca hilton` **se niega a correr**: Between no tiene `reglas.yaml` y el motor
prefiere negarse antes que dar un visto bueno con reglas de agencia. Queda
pendiente escribírselo con Eli.

**Reproducibilidad:** comprobada con `cmp`, no supuesta — los tres recortes se
regeneran **byte a byte** desde las fuentes a 2×. Esas fuentes (80 MB) van
forzadas al repo por la misma razón que el panorama del cumpleaños: el upscaler
no es determinista y sin ellas un recorte distinto mañana no sería la misma foto.

**Abierto:**
- El comentario de `STORIES!N` sigue **sin tachar** en la grilla. Acá se atacó por
  la foto (mesa servida y en uso) y el copy va literal del brief ya corregido. Si
  el cliente quería además otra redacción, la decide el CM, no diseño.
- No se pudo LISTAR la carpeta STORIES antes de subir (el token es `drive.file`).
  Si el set del 31-08 sigue ahí con estos mismos nombres, el uploader **reemplazó**
  el archivo; si estaba con otro nombre, hay que borrar el viejo a mano.
- Las **guías del CM** otra vez quedan sólo en local. Sigue sin decidirse si se le
  mandan por Slack o si va una subcarpeta al Drive que el portal no levante.

## 2026-09-07 (cierre 3) · Eli (Windows) — BETWEEN: las dos stories del cumpleaños

**Qué se hizo:** Eli rehizo y subió el carrusel de cumpleaños del feed
(`C1 S2 CUMPLE N1/N2.png`, Drive `1P5NSpKHGCRwqCVZYlPU4zKkH09-YcqKk`) y pidió
**dos stories de secuencia** a partir de él, con sticker interactivo. Se armaron,
pasaron dos rondas de correcciones suyas, las **aprobó** y quedaron **subidas al
Drive**. Se corrigió además un defecto de emojis que afectaba a toda la marca.

### Lo entregado

`out/hilton/between/entrega-st-cumple-09-09/` — 2250×4000:

    BW ST 09-09 Cafe de regalo cumpleanos 1.png   ← el vaso
    BW ST 09-09 Cafe de regalo cumpleanos 2.png   ← las condiciones
    …1 GUIA CM.png · …2 GUIA CM.png               ← internas, NO van al Drive

Subidas a **S2 HILTON SEP 2026 / BW / STS** (`1lupGWfILmS9JQ4tznkqqddTKOh6uFtEe`),
pesos verificados contra los locales. Copia también en
`~/COPYLAB-ENTREGAS/BETWEEN-S2-SEP2026/`, con las guías en su subcarpeta.
Composición: `src/compositions/hilton/BetweenStCumpleCarrusel.tsx`.

### Las tres correcciones de Eli, y qué enseñó cada una

1. ⭐⭐ **«Debe ser una transición de la foto el slide 1 y la 2.»** Las dos escenas
   generadas por separado se botaron. Ahora hay **UNA sola fotografía continua**
   de 4096×4096 y los dos fondos son sus mitades
   (`scripts/between-st-cumple-panorama.py`): la mesa, las cintas, el follaje y la
   luz siguen de una historia a la otra. **Es la misma orden que ya había dado el
   04-09 para el carrusel de feed** («que sea una continuidad con la slide dos»),
   o sea que es criterio de marca y no un pedido suelto — vale para el próximo
   carrusel, no hay que esperar a que lo pida.
   La frase que lo destrabó fue la del **encuadre**: hay que decirle al generador
   dónde va el sujeto dentro del cuadro, porque de un cuadrado salen dos 9:16 y
   sobra poco. El primer intento puso el vaso abajo y el sticker chocaba con su
   base.
2. **«No agregues logo en portada por el vaso.»** Fuera el lockup, y de las DOS:
   en la 1 firma el vaso con su logotipo impreso, en la 2 la tarjeta con el avatar
   y el handle — y las dos láminas del carrusel aprobado tampoco lo llevan. Al
   sacarlo el titular sube de y=441 a y=300 (el ancla de 441 está calculada para
   caer bajo el logo) y la tarjeta de la 2, de 430 a 330.
3. **«El legal más abajo donde se lea mejor.»** De y=1524 a **y=1640**: en 1524
   caía sobre el plato y las cintas, en 1640 cae sobre la madera limpia.

### ⛔ Tres reglas nuevas que salen de acá (todas en `PROMPTS-DE-ELI.md` §3)

- **Los emojis del sistema NO sirven en esta máquina.** Windows resuelve
  `Segoe UI Emoji` y el ☕ sale **lila** — el defecto que Eli ya había cazado en
  los renders del estudio. Apple Color Emoji no se puede redistribuir, así que se
  **recortan de la lámina aprobada** con `scripts/between-emoji-extraer.py` y
  entran como PNG con transparencia, desde
  `public/assets/hilton/between/emoji/`. **Vale para TODA pieza de Between con
  emojis**, no solo para ésta.
- **El garabato de línea se apoya en el FONDO, nunca sobre el producto ni sobre
  quien lo sostiene.** A la derecha del vaso se montaba encima del logotipo
  impreso y se leía «BETWEENS», con la cuerda cruzando el wordmark; antes, abajo
  a la izquierda, caía sobre la mano. Romper el logotipo del vaso es el peor error
  posible en una pieza cuyo tema es ese vaso.
- **Las cajas del listado van con `letterSpacing: -0.015em`.** Con el tracking por
  defecto la misma línea medía 361 px contra los **348,5 medidos en la pieza
  aprobada** (3,6 % más suelta), y esos 12 px de más echaban el emoji a una línea
  nueva: las filas crecían de 95 a 132 px.

### Lo interactivo se resolvió como ZONA RESERVADA

660×210 limpios en y=1280. El sticker lo pone el CM al publicar con el sticker
**real** de Instagram (ST1 deslizador 🎂 · ST2 encuesta «¿Ya lo canjeaste?»). Un
sticker dibujado en el PNG se ve interactivo y no lo es. Las copias `GUIA CM`
llevan la zona marcada y son para el CM: **no se suben ni se mandan al cliente.**

### Reproducibilidad, comprobada y no supuesta

Se forzaron al repo los dos fondos, la ventana, los cuatro emojis y **el panorama
de origen** (38 MB). El panorama va aunque pese: sin él, un recorte distinto
mañana obligaría a regenerar y **no sería la misma foto**. Verificado con `cmp`:
los fondos se re-cortan **idénticos byte a byte**, la ST 2 se re-renderiza
idéntica y la ST 1 difiere en **95 píxeles de 9.000.000 con máximo 2/255** en la
zona del titular — antialiasing de Chrome, invisible.

**Dónde quedó:** todo commiteado y subido. `MarcoIGPost` NO se tocó: se quedó
atrás respecto de lo aprobado (fondo blanco en vez de crema, viñetas «•» en vez de
casillas) pero lo usan piezas ya aprobadas y cambiarlo las re-flujaría, así que la
tarjeta nueva se armó aparte con la geometría medida.

**Qué sigue:** el manual quedó con la línea de tiempo de las tres órdenes
contradictorias sobre si la ST de cumpleaños es una o dos (28-08 dos → 01-09 una →
07-09 dos). Lo próximo de la S2 sigue siendo lo que ya estaba: `BW FEED 09-09
Primero la foto` y `BW FEED 11-09 Ella hablo ella escucho`.

**Abierto:**
- ⚠️ **Si alguna de estas dos stories pasa a PAUTA, hay que subir el legal de la
  ST 2**: hoy entra 90 px en la franja inferior de 340 px de Meta y `between-qa.py`
  lo marca. Es decisión de Eli y tiene precedente (su plantilla de story con logo
  abajo entra 104 px), pero en orgánico solamente.
- Las guías `GUIA CM` **todavía no le llegaron al CM**: están sólo en la carpeta
  local de Eli. Hay que decidir si se le mandan por Slack o si se sube una
  subcarpeta al Drive que el portal no levante.
- `MarcoIGPost` quedó desalineado con la marca. Cuando se rehagan `BetweenCumple`
  y la G2 de `BetweenSeptiembre`, hay que subirle el fondo crema y las casillas.

## 2026-09-07 (cierre 2) · Eli (Windows) — BETWEEN: la torta comida del carrusel del 14-09

**Cambio de último minuto de Eli:** la última slide del carrusel del **14-09** debe
ser «una torta casi en totalidad comida, pero que se vea lindo aún». Nos dejó el
video de la torta real y una carpeta de dulces y tortas.

⚠️ Y lo primero fue no confundirse de pieza: **el del 14-09 no es Promos To Go**
(ése se movió a la S4 del 22-09), es **«PRIMERO LA FOTO… ¿O NO?»**, cuyo remate es
«¡NOOO! Se me olvidó la foto». La torta comida es el chiste de la pieza.

### Lo entregado

`out/entrega-r25/S3/` — las 4 slides, 2250×2812, 4/4 limpias en `between-qa.py`:

    BW FEED 14-09 Primero la foto 1 desayuno.png
    BW FEED 14-09 Primero la foto 2 latte.png
    BW FEED 14-09 Primero la foto 3 croissant.png
    BW FEED 14-09 Primero la foto 4 torta comida.png   ← la nueva

### Las dos cosas que enseñó, y están en el manual (ronda 25)

1. **El encargo traía una condición más, y estaba en la grilla.** `FEED!H15` tenía
   sin tachar: «que se vea más vacío el plato […] **que sea desde arriba también
   como los 2 anteriores**». O sea plato vacío **y** cenital.
2. ⭐⭐ **Una foto de carrusel no se aprueba suelta, se aprueba MONTADA.** La r24
   cumplía todo lo pedido y estaba mala: iba sobre mármol blanco mientras sus tres
   hermanas van sobre los listones oscuros. Rompía el mundo del carrusel (mediana
   219 contra ~102) y dejaba el titular blanco casi ilegible. Leído con eso a la
   vista, «como los 2 anteriores» **no hablaba del ángulo: hablaba de la mesa.**
   La r25 es la misma torta con una sola variable cambiada, y salió a la primera.

También quedó corregida una nota de la ronda 19: el factor de calidez de
`iguala_tono()` **no es fijo** (allá era pedir 60 para terminar en 34, acá 22,8
para terminar en 20,8). Se mide sobre la propia foto.

### El banco de dulces y tortas

`raw/hilton/between/dulces-tortas/` con `LEEME.md`: los **9 videos verticales
2160×3840 a 60 fps** indexados, con su póster cada uno y hoja de contacto. **Dos
bajados completos** (los que se necesitaron); los otros siete están sólo como
póster para no bajar 1,9 GB sin motivo. Un fotograma de esos videos es una foto 4K.

### ✅ Drive y repo, cerrados el mismo día

**Eli ordenó la carpeta de Drive y dejó la entrega lista** (07-09): sacó los
archivos viejos «BW FEED 14-09 Promos To Go …», que eran de cuando ese carrusel
todavía era de la S3, y resolvió dónde queda cada uno. **Septiembre de Between
queda entregado.**

En el repo (commit `b50a9e7`) viajan **forzados**, porque `public/assets/` y `raw/`
están en el `.gitignore`: los fondos gradados de los dos carruseles aprobados, las
tres piezas que hizo Eli y todos los scripts de las rondas. Verificado con `cmp`:
re-renderizar la slide 4 desde el repo da el **mismo PNG byte a byte**.

⚠️ Lo único que NO viaja son las generaciones PNG de `ia-sept` (~95 MB). No hacen
falta para rendir —eso sale de los `.jpg` gradados— y los prompts para rehacerlas
están en `clients/hilton/PROMPTS-DE-ELI.md`.

### ⛔ Lo que sigue pendiente, y ya no es de septiembre

1. Los emojis del mock rinden **lila en Windows**: falta empaquetar Noto Color
   Emoji en `public/assets/hilton/between/fonts/` y nombrarla primera en la pila.
2. **`clients/hilton/reglas.yaml` sigue sin existir**, así que Between pasa sólo
   por `between-qa.py` y no por `qa/motor.py`, que es la compuerta del estudio.
3. Del carrusel «Primero la foto» queda el viejo reparo del **vaso KIMBO en la
   G1** («ese kimbo hay que quitarlo»), que Eli no ha vuelto a pedir.

---

# Bitácora — HILTON (DT · QB · Between · Piso18)

> Una entrada por sesión, la más nueva arriba. Sirve para que otro diseñador
> retome la cuenta mañana sin preguntar nada. Se escribe en el `/cierre`.

---

## 2026-09-07 (cierre) · Eli (Windows) — BETWEEN: el carrusel PROMOS TO GO queda APROBADO

**Eli: «aprobados».** Las cuatro piezas del carrusel Promos To Go, que pasó a la
**S4 del 22-09** (antes S3 del 14-09), quedan aprobadas.

| slide | foto | archivo de entrega |
|---|---|---|
| 1 · portada | `togo-portada-r18.jpg` | `BW FEED 22-09 Promos To Go 1 portada.png` |
| 2 · café + sándwich | `togo-s2-r20.jpg` | `…2 sandwich.png` |
| 3 · café + dulce | `togo-s3-r21.jpg` | `…3 dulce.png` |
| 4 · los tres | `togo-s4-r22.jpg` | `…4 los tres.png` |

Están en `out/entrega-r21/S4/`, 2250×2812, y las cuatro limpias en
`between-qa.py`.

### Qué se hizo para llegar acá, en dos frases

La ronda 20 corrigió lo estructural: **la jerarquía del brief estaba invertida en
las tres slides interiores** (la bajada hacía de titular y el titular del brief
iba dentro de la barra del precio), y las fotos se regeneraron con el método de
Eli —prompt propio por slide, con su pieza aprobada y las fotos reales del
producto como referencias— en vez de componer recortes. La ronda 21 arregló sus
dos últimos reparos: la medialuna exagerada de la slide 3 y el plato de cerámica
para el muffin de la slide 4.

### ⛔ Lo que NO se hizo, y es lo único que falta

1. **Nada subido al Drive.** El carrusel cambió de semana, así que **no hay
   carpeta destino todavía**: las piezas viejas viven en `S3 · BW`
   (`1QOreVz6NVYvuri9RAYQRMNiilV_IN8XZ`) y estas van a la S4. Hay que decidir si
   se crea `S4 · BW` o si se reemplazan por id las de la S3 para conservar los
   enlaces del portal. **Decisión de Eli.**
2. **Sin commit.** Y ojo con esto: los fondos y las generaciones viven en
   `public/assets/` y `raw/`, las dos en el `.gitignore`. Sin forzarlas al commit
   **este carrusel no se reproduce en otra máquina** — es exactamente el problema
   que Revex ya tuvo. Son unos 60 MB entre las generaciones de esta jornada y las
   tres piezas de Eli.

### El estado de septiembre, después de esta jornada

| pieza | semana | estado |
|---|---|---|
| Carrusel Promos To Go | S4 · 22-09 | ✅ **aprobado** (4 piezas) |
| ST Emergencia | S2 · 09-09 | ✅ aprobado — **la hizo Eli**, ya subida por ella |
| Carrusel Cumpleaños | S2 · 09-09 | ✅ aprobado — **lo hizo Eli** |

⭐ Y el aprendizaje de la jornada, que vale más que las piezas, está en
`clients/hilton/PROMPTS-DE-ELI.md`: **no se compone, se genera**, con las fotos
reales como referencia y una sola variable por vez.

---
## 2026-09-07 (tarde) · Eli (Windows) — BETWEEN rondas 17-19: ELI REHIZO DOS PIEZAS Y ESO ES LA NOTICIA

**Eli rechazó la ST de Emergencia y el carrusel de Cumpleaños, los rehizo ella
misma y dejó los prompts a la vista.** Esa es la entrada más importante de esta
bitácora en semanas: no es una ronda más de correcciones, es un cambio de método.

### ⛔ Lo que quedó rechazado, y por qué

Cinco rondas seguidas del estudio sobre las mismas piezas, con esta secuencia de
veredictos:

    r11  papelitos de color plano sembrados en la mesa   → «infantil»
    r12  oro metálico dibujado                           → «parece un plátano»
    r14  el vector de Eli sembrado                       → «quemado»
    r17  cinta FOTOGRÁFICA con 15-26 % de especular      → «falsa, quemada»
    r19  fondo generado + recortes + logo estampado       → «parecen de paint pegoteados»

El MATERIAL mejoró en cada vuelta y el veredicto no cambió nunca. Porque el
problema no era el material.

> ⭐⭐⭐ **El método era el error: el estudio COMPONÍA y Eli GENERA.** Ella le pasa
> las fotos reales del producto como referencias (`@img1 @img2 @img3`), describe
> la escena terminada, y el generador entrega el producto, su logotipo impreso, la
> luz, las sombras y **hasta el texto de la señalética** ya integrados. Cada
> elemento que el estudio pegaba encima era una costura más.

Y una conclusión mía que resultó **falsa** y conviene tenerla anotada: después del
«falsa, quemada» de la r17 decidí que el dorado tenía que irse al fondo y fuera de
foco, porque nítido sobre la mesa siempre se leía pegoteado. La pieza de Eli lo
desmiente: su dorado está **sobre la mesa y en foco**, y se ve de lujo.

### ⭐ Dónde está todo lo de Eli

| pieza | archivo |
|---|---|
| ST Emergencia (S2 · 09-09) | `raw/hilton/between/de-eli/emergencia-s2/BW ST 09-09 Emergencia Between.png` |
| Cumpleaños 1 y 2 (S2 · 09-09) | `raw/hilton/between/de-eli/cumple-s2/C1 S2 CUMPLE N{1,2}.png` |
| **sus PROMPTS, textuales** | **`clients/hilton/PROMPTS-DE-ELI.md`** ← leer antes de escribir cualquier prompt de esta marca |

La ST de Emergencia **ya la subió ella al Drive** (`S2 · BW / STS`, 07-09 16:05).
Mis versiones de las tres piezas se borraron de `out/entrega-r18/` y quedó un
LEEME explicando cuál manda, para que nadie entregue el archivo equivocado.

### ✅ Lo que SÍ quedó del estudio: el carrusel PROMOS TO GO

Pasó a la **S4 del 22-09** (antes S3 14-09). Entregado en `out/entrega-r19/S4/`,
4 de 4 limpias en `between-qa.py`, y hecho ya con el método de Eli:

- **portada**: Eli dejó el fondo aprobado; se corrigieron los «textos corridos» —
  y no era el centrado (las cinco líneas caen a ±2 px del eje) sino el AIRE, con
  la jerarquía invertida: 23 px de script→titular contra 63 px entre las dos
  líneas del titular. Con `aireScriptATitulo={44}` queda 96 contra 63;
- **slides 2, 3 y 4**: una generación con prompt propio cada una, pasándole la
  pieza aprobada de Eli como referencia de vaso y de calidad. **El logotipo del
  vaso viene nativo en la imagen, no estampado**, así que no hay costura;
- **slide 4**: la bolsa va **lisa, sin logo** — instrucción literal de Eli, «borra
  los logos, déjala sólo en el vaso de TOGO»;
- se sacó la etiqueta «Croissant» y su flecha: sus coordenadas estaban medidas
  sobre la foto anterior;
- tono igualado a la portada (calidez 29-35 contra 34,2 de ella).

⚠️ Ojo con un detalle no obvio del igualador: `iguala_tono()` corrige la calidez
ANTES de la saturación, y el paso de saturación la vuelve a comprimir. Para
terminar en 34 hay que **pedir 60**. Pidiendo 34 el resultado cae en 19-20, o sea
más frío que la portada.

### ⚠️ Lo que queda abierto

1. **Los emojis del mock rinden distinto según la máquina.** La pieza de Eli tiene
   el ☕ correcto (una taza de café); en Windows la pila cae en Segoe UI Emoji y
   sale una **taza lila**. Se cierra empaquetando Noto Color Emoji en
   `public/assets/hilton/between/fonts/` y nombrándola PRIMERA en la pila.
2. **`clients/hilton/reglas.yaml` sigue sin existir**, así que Between no pasa por
   `qa/motor.py` — la compuerta del estudio — sino sólo por `between-qa.py`.
3. **Nada del carrusel To Go subido al Drive.** Falta el paso de entrega.
4. Siguen los pendientes viejos: `FEED!H16` sin responder, nombres con fechas
   viejas en Drive y el duplicado «…4 trio.png».

### Los scripts de estas rondas

`between-emergencia-r16/r17/r18.py` · `between-cumple-muro-r16/r18.py` ·
`between-cumple-cintas-r17.py` · `between-cintas-recortar.py` ·
`between-croissant-recortar-r17.py` · `between-togo1-r16/r18.py` ·
`between-togo4-r16.py` · `between-togo-slides-r19.py`

⚠️ Los de Emergencia y Cumpleaños quedan como **historial**, no como pipeline: esas
dos piezas ya no se producen así. El que sigue vivo es
`between-togo-slides-r19.py`, que es el único escrito con el método nuevo.

---
## 2026-09-07 · Eli (Windows) — BETWEEN ronda 16: la referencia era de geometría

**Eli mandó tres encargos con una referencia de Pinterest en la mano** —una caja
de «romper el vidrio en caso de emergencia»— y las tres piezas salieron. Cuatro
piezas rendidas, `between-qa.py` limpio en 7 de 7 (incluidas las slides 2 y 3 que
no se tocaron, rendidas sólo para el control de carrusel).

### Lo que se hizo

| pieza | qué pidió | qué se hizo |
|---|---|---|
| **ST Emergencia** (S2, 09-09) | «igual a la referencia, con café TOGO, croissant jamón queso y muffin de chocolate» | **rehecha entera**: caja vertical que manda en el cuadro, titular SOBRE el vidrio, llamado en la BARRA del marco, los 3 productos reales apoyados en una línea de base |
| **Cumpleaños 1 y 2** (S1, 03-09) | «volver a hacer el fondo, genera en magnific, globos de fondo sutil, que se note que es Between» | **sólo el muro**: 3 globos champán generados y compuestos en el muro vegetal REAL de la 257 — el par abre en la slide 1 y uno solo cierra en la 2 |
| **To Go 1 portada** (S3, 14-09) | «arregla el logo» | el logotipo pasó de **0,158 a 0,32** del alto del cuerpo (el vaso real da 0,485), con comba de 8 px y enmascarado por los dedos |
| **To Go 4 los tres** (S3, 14-09) | «vuelve a hacer ese, se ve extraño la foto de fondo y todo» | **escena regenerada** con el muro verde y la mesa miel de sus hermanas, los 2 logotipos re-medidos y el tono igualado a las slides 2 y 3 |

### ⭐ El hallazgo de la sesión, y es de método

**Las cuatro piezas llevaban 3 o 4 rondas de ajustar parámetros dentro de un
planteamiento equivocado.** La regla de la ronda 15 («a la segunda vez que se
repite un comentario, mira el insumo») necesitaba un piso más:

> **A la TERCERA ronda de parámetros sobre la misma pieza, lo que está mal es la
> geometría o la escena.**

- La ST de Emergencia: la caja era **apaisada** (1,20 : 1) y ocupaba el 35 % del
  alto, con 292 px de vacío arriba y 465 abajo. La referencia es vertical y manda
  en el cuadro. Se vio en un segundo poniendo **la pieza al lado de la referencia
  al mismo alto** — el control que el método pide y que esta pieza nunca tuvo.
- El logo de la portada: cuatro rondas tratando de **esquivar la mano**, y la
  ronda 15 terminó peor que la 9 (0,158 contra el 0,32 aceptado). Los dedos
  cruzan el centro del vaso porque **así se toma un vaso**: la salida es que los
  dedos lo TAPEN, no que lo empujen a la tapa.
- La slide 4: tres rondas de revelado peleando contra un **interior de bar** en
  un carrusel de bodegones de luz de día. El problema era la escena.

Todo medido y escrito en `clients/hilton/CLAUDE.md § RONDA 16`, con los 13
aprendizajes y sus cifras.

### ⚠️ Dos decisiones que hay que confirmar

1. **La Cumpleaños 1 ahora tiene globos REALES en el fondo y los globos
   ILUSTRADOS de Eli encima**, los dos en el mismo tercio izquierdo. Es decir dos
   veces lo mismo con dos materiales. Se dejaron los dos porque el criterio con
   que Eli aprobó esa slide fue *«que sean ilustradas, con el trazado que ya se
   sabe y se conoce»* y hoy pidió globos en el fondo generado: **no se resuelve
   en silencio.** Si sobran, se quitan los ilustrados en una línea.
2. **La slide 4 dice «¡LLÉVATE LOS 3!» y el brief que Eli pegó hoy dice «Llévalo
   contigo.»** El «¡Llévate los 3!» salió de una corrección del cliente
   (Scarlette, ronda 4: «en lugar de llévalo contigo, pongamos algo que haga más
   sentido»), está aplicado y tachado en la grilla. Se conservó la corrección del
   cliente por sobre el brief, que nunca se actualizó. **Confirmar cuál manda.**

### ⛔ Lo que NO se hizo

- **Nada se subió al Drive.** Las cuatro piezas están en
  `out/hilton-between-r16/` y falta correr `between-r15-entrega-subir.py`
  adaptado a la r16 para reemplazar por id y conservar los enlaces.
- **Los emojis del mock de la Cumpleaños 2 siguen mal**: el ☕ sale como una taza
  **lila** porque en Windows la pila cae en Segoe UI Emoji. Y peor: en el Mac
  caería en Apple Color Emoji, o sea que **la misma pieza rinde distinto según
  quién la rinda**. Se cierra empaquetando Noto Color Emoji y poniéndola primera
  en la pila. No estaba en el encargo de hoy.
- `clients/hilton/reglas.yaml` **sigue sin existir**, así que Between no pasa por
  `qa/motor.py` (la compuerta del estudio) sino sólo por el `between-qa.py` a
  medida.
- Siguen abiertos los pendientes de la r15: `FEED!H16` sin responder, los nombres
  con fechas viejas en Drive, el duplicado «…4 trio.png» y la ST 03-09 generada.

### Dónde está todo

- Piezas: `out/hilton-between-r16/` (2250×2812 feed · 2250×4000 story)
- Escenarios y generaciones: `public/assets/hilton/between/ia-sept/`
  (`emergencia-fondo-r16.png`, `cumple-globos-r16.png`, `cumple-fondo-r16b.png`,
  `togo-portada-gen-r16.png`, `togo-trio-gen-r16.png`)
- Fotos reveladas: `fotos-gradadas/cumple-r16-{1,2}.jpg`, `togo-portada-r16.jpg`,
  `togo-trio-r16.jpg`
- Base con el muro nuevo: `raw/hilton/between/togo-25jul2025/base-r16-muro.jpg`
- Scripts: `between-emergencia-r16.py` · `between-cumple-muro-r16.py` ·
  `between-togo1-r16.py` · `between-togo4-r16.py`
- Cómo se reproduce la Cumpleaños de punta a punta:

```bash
python scripts/between-cumple-muro-r16.py
BW_CUMPLE_ORIGEN=raw/hilton/between/togo-25jul2025/base-r16-muro.jpg \
  BW_CUMPLE_RONDA=r16pre python scripts/between-cumple-fondo.py
BW_CUMPLE_RONDA=r16pre BW_CUMPLE_RONDA_OUT=r16 \
  python scripts/between-cumple-confeti-r14.py
npx remotion still src/BetweenEntry.tsx BW-F-Cumple-1 \
  out/hilton-between-r16/BW-F-Cumple-1.png --scale=2.0833
```

---
## 2026-09-05 · Eli (Windows) — BETWEEN ronda 15: la reiteración era el diagnóstico

**Eli devolvió la ronda 14 entera**, y con una frase que vale más que las cuatro
correcciones: «**ya que es muy reiterativo los cambios y debes mejorar**».

Tiene razón, y la causa está medida: **las cuatro correcciones de la ronda 14
fueron ajustes de parámetro dentro de un método roto.** Ninguna tocó la causa.

| pieza | su reclamo | la ronda 14 ajustó… | lo que estaba roto de verdad |
|---|---|---|---|
| Cumpleaños | «lo dorado se ve **quemado**» | color, tamaño, sombra | el **alfa**: se filtraba sin premultiplicar y `rotate()` mete negro |
| Emergencia | «el vaso to go **pegoteado**» | escala, piso, sombra, luz | el **recorte**: canto mordido por grabCut |
| To Go 1 | «el logo **sigue igual**» | centro y ancho, 3 rondas | **no cabía**: banda de 25 px para un lockup de 56 |
| To Go 4 | «**sigue oscuro** y logos extraños» | mediana, calidez, saturación | las **sombras**, que nadie miró |

> **La regla de proceso que queda: a la SEGUNDA vez que el cliente repite un
> comentario, se prohíbe tocar el parámetro.** Hay que ir a mirar el insumo —el
> recorte, el alfa, el espacio disponible— con zoom. Un comentario que se repite
> no dice «te pasaste de valor»: dice «estás mirando el sitio equivocado».

### Qué se hizo, pieza por pieza

**Cumpleaños 1 y 2 — el «quemado» era un halo negro.** Se desenfocaba el RGB y el
alfa por separado; `rotate(expand=True)` rellena las esquinas con negro
transparente (medido: el RGB invisible pasa de 239 a 1) y el desenfoque lo
arrastra al contorno. Ahora el filtrado va con **alfa premultiplicado** y la
pieza pasa por `hombro()`. Vale para cualquier recorte que se filtre.

**ST Emergencia — el «pegoteado» era el recorte.** Tres rondas puliendo el
montaje sobre un vaso con el canto mordido. **El vaso bueno ya estaba en el
repo**: `togo-vaso-real-nobg.png`, el mismo con el que se midió el logotipo
oficial. Más la temperatura del hueco llevada al producto al 45 %.
⚠️ `remove-background` de Magnific está **caído** (503 del gateway, también con
cuerpo vacío). El script quedó escrito: `scripts/between-vaso-matte.py`.

**To Go portada — se cambió la FOTO, que es lo que había que hacer hace tres
rondas.** La banda de cartón limpia entre la tapa y los dedos medía 25 px y el
lockup de marca pide 56: no cabía, y por eso sólo se podía elegir por dónde
cortarlo. Se regeneró la escena con **Nano Banana Pro** —misma mujer, mismo
local, misma luz, mismo encuadre— cambiando una sola cosa: que tome el vaso más
abajo. Ahora hay 83 px limpios y el logotipo entra entero a 0,86, centrado, con
17 y 16 px de aire.

**To Go slide 4 — «oscuro» no era la mediana, eran las sombras.** Estaba en 100
contra 99 y 102 de sus hermanas, o sea igualada, pero su percentil 10 y el fondo
negro la hacían leer oscura. `abre_sombras()` levanta los medios bajos sin tocar
el negro puro (p10: 30 → 46). Y los «logos extraños» eran vectores **sin grano ni
desenfoque** sobre una fotografía: ahora el sello se funde a la nitidez local y
recibe el grano del papel; el de la bolsa baja de 0,58 a 0,50 porque cruzaba el
pliegue.

### ✅ SUBIDO AL DRIVE, reemplazando por id (las 5, verificado)

`between-qa.py` limpio en 4 de 5 — el aviso de `BW-F-Cumple-1` sigue siendo el
falso positivo documentado (1 px del canto del plato).

**Herramientas nuevas:** `between-togo1-r15.py` (genera, mide y compone la
portada) · `between-vaso-matte.py` (listo, esperando que Magnific vuelva) ·
`between-r15-entrega-subir.py`.

**Abierto:** lo mismo de la ronda 14 —`FEED!H16` sin responder, los nombres con
fechas viejas, el duplicado «…4 trio.png», avisarle a Scarlette del mock, la ST
03-09 generada y `clients/hilton/reglas.yaml` que no existe.

---

## 2026-09-05 · Eli (Windows) — BETWEEN ronda 14: cuatro correcciones, cuatro mediciones malas

**Lo primero del día, antes de producir:** `/abrir between`. El pull no trajo
nada y la grilla de Between se había movido el 04-09 a las 20:49Z, pero el diff
completo contra la copia de las 18:24Z dio **sólo dos celdas, las dos de estado**:
`FEED!J16` (Ella habló) EN CAMBIOS → **CORREGIDO**, y `STORIES!I16` (Emergencia)
REVISAR CONTENIDO → **EN CAMBIOS** — y ésta última se movió *antes* de que la
ronda 13 subiera la pieza rehecha (20:49Z contra 21:31Z), así que apuntaba al
render viejo. Cero comentarios nativos nuevos y cero comentarios en las 5 piezas
del Drive. **No había ronda 14 en la grilla: la ronda 14 la pidió Eli por chat.**

---

### Qué pidió Eli, y qué se hizo

| Pieza | Su comentario | Qué se hizo |
|---|---|---|
| **S1 Cumpleaños 1 y 2** | «debes quitar esos **plátanos dorados**… puedes añadir alguna de [vector de confeti dorado] **sutiles** en el slide 1 y 2. **Hazlo realista** y mantén el resultado de la foto de togo y medialuna» | Los plátanos estaban **dentro del mock de la slide 2**. Fuera. Entra confeti dorado del vector que ella mandó, sembrado sobre la mesa con la receta de montaje. La foto no se tocó |
| **S2 ST Emergencia** | «vuelve a hacer lo de TOGO, MUFFIN CHOCOLATE + CROISANT QUESO JAMÓN, **para que se vea apetitoso** en caso de romper» | Los tres revelados con `apetitoso()`, 25 % más grandes y **por fin apoyados**: el piso de la vitrina estaba mal medido. Más sombra en la pared del fondo y el recorte del vaso limpio |
| **S3 slide 1** | «el logo del vaso debes **centrarlo según el vaso**. Arréglalo» | 171 px (0,86) centrado en el eje real del cuerpo. La causa de tres rondas era que el cuerpo medía 199 px, no 240 |
| **S3 slide 4** | «se ve extraño, **no tiene coherencia del color** de las demás, tiene que ser la misma foto pero **sin esa edición**» | Fuera la igualación de tono que la dejó lechosa. Rehecha con punto negro antes del gamma |

⛔ **No se tocaron** las slides 2 y 3 del To Go («no las toques», sigue vigente)
ni «Ella hablo Ella escucho».

---

### ⭐⭐⭐ El hilo común, y es incómodo: las cuatro correcciones eran de MEDICIÓN

Ninguna de las cuatro era un problema de criterio. En las cuatro, la ronda
anterior **aplicó la regla correcta sobre un número equivocado** — y por eso Eli
lleva tres rondas repitiendo el mismo comentario sobre el mismo logo.

| pieza | la regla estaba bien | el número estaba mal |
|---|---|---|
| vaso To Go | «0,86 del ancho del vaso, centrado» | el ancho del vaso: 240 supuesto contra **199** real |
| vitrina | «una sola línea de base, medida sobre el contenedor» | el piso: 1230 supuesto contra **1272** real |
| slide 4 | «igualar el tono al de sus hermanas» | el método: gamma sin punto negro |
| confeti | «armonizar el objeto agregado con la escena» | contra la **superficie** en vez del **iluminante** |

**Lo que hay que cambiar en el método: cuando un comentario se repite, no se
corrige la pieza — se vuelve a medir la constante.** Las tres rondas del logo se
gastaron ajustando el centro y el tamaño sobre un ancho de vaso que nadie volvió
a comprobar.

---

### ⭐⭐ Los plátanos estaban donde nadie los buscó

La ronda 13 sacó las cintas doradas de la foto de la slide 1 y dio el asunto por
cerrado. Pero la **ventana del mock de Instagram de la slide 2** seguía apuntando
a `cumple-r12-1.jpg`. Las cintas plátano estuvieron publicadas un día entero
*dentro del post* de la slide 2, con la slide 1 ya limpia — y ahí las vio Eli.

> **Regla nueva, en el manual: al cambiar el fondo de una pieza se hace `grep`
> del nombre viejo en `src/` antes de cerrar la ronda.** Un mock de post enseña
> otra pieza adentro y no se actualiza solo.

### ⭐⭐ El adorno realista sí se podía — el problema era el material, no el registro

La ronda 12 concluyó que el adorno de esta marca tiene que ser ilustración
porque una cinta dorada «parece un plátano». **Era media conclusión.** Lo que no
aguantaba la comparación con la fotografía no era el realismo: era que la cinta
la dibujaba yo con `ImageDraw`. El vector que mandó Eli (Freepik/Magnific
**177837523**, gratuito dentro del plan) trae cintas con vuelta, cara interior y
exterior y especular propia, y sobre eso sí vale la pena aplicar la receta de
montaje. 27 serpentinas recortadas con alfa en `recursos/confeti-oro/`.

Y los doodles de pincel **se quedaron**: la slide 1 se aprobó con ellos.

⛔ En el camino, dos errores propios que quedaron escritos:
- **armonicé el oro contra el color de la MADERA** y salió naranja mandarina;
  contra el muro vegetal, verde. El iluminante de la toma es neutro
  (0,983/1,000/1,030, medido en el anillo blanco del vaso): un objeto agregado
  toma el color de la **luz**, no el de la superficie donde cae;
- y lo dejé **demasiado sutil**. Al 100 % se veía bien; a los 430 px que mide la
  pieza en el feed de un teléfono eran motas y la corrección no se leía. +25 %.

---

### ✅ SUBIDO AL DRIVE, reemplazando por id (las 5, verificado)

- **S1** → `BW FEED 03-09 Cumpleanos 1.png` · `…Cumpleanos 2 detalles.png`
- **S2** → `BW ST 09-09 Emergencia Between.png`
- **S3** → `BW FEED 14-09 Promos To Go 1 portada.png` · `…4 los tres.png`

`between-qa.py` limpio en 4 de 5; el aviso de `BW-F-Cumple-1` es el falso
positivo ya documentado (1 px del canto del plato en x=3, y=1575) y es **idéntico
al del render de la ronda 13**, que Eli aprobó.

⚠️ `qa/motor.py --marca hilton` **no corre**: Hilton no tiene
`clients/hilton/reglas.yaml`. La compuerta de la marca hoy es `between-qa.py`.
Crear las reglas ejecutables es una decisión que necesita la firma de Eli.

**Herramientas:**
- `scripts/between-confeti-recortar.py` — trocea el vector en 27 serpentinas
- `scripts/between-cumple-confeti-r14.py` — la siembra, con DOF, iluminante y sombra
- `scripts/between-recortes-limpiar.py` — le quita al recorte la mesa que arrastró
- `scripts/between-r14-entrega-subir.py` — entrega y reemplazo por id
- modificados: `between-togo1-r12.py`, `between-togo4-r12.py`, `between-emergencia-r13.py`

**Abierto (lo mismo de ayer, nada se cerró hoy):**

1. Las 4 piezas de la ronda 13 que quedaron **sin aprobar y sin comentar** ahora
   están reemplazadas por las de la 14. Falta que Eli se pronuncie.
2. **`FEED!H16` (Primero la foto, 14-09)** sigue en REVISAR CONTENIDO con la
   pregunta de la CM sin responder: «¿Qué plato es el que ya está comido?».
3. Los **nombres de archivo** siguen con las fechas viejas; renombrar va junto con
   borrar la copia vieja (el portal levanta por nombre).
4. El **duplicado «BW FEED 14-09 Promos To Go 4 trio.png»** sigue vivo en la
   carpeta antigua (`1LELTpyvTlOYwf2ULSbPRe2tJDTZ2av28`, subido por nuestro
   token): hay que borrarlo a mano.
5. **Avisarle a Scarlette** que el mock de post volvió.
6. La **ST 03-09 del cumpleaños** (`BW-S-Cumple`) sigue siendo una escena generada
   con una vela mientras el feed de ese día ya es fotografía real.
7. **`clients/hilton/reglas.yaml`** no existe.

---

## 2026-09-04 · Eli (Windows) — BETWEEN, CIERRE DEL DÍA: estado de aprobación

**Eli, al cerrar: «solo te apruebo lo de cumpleaños Slide 1, mañana seguiremos».**

Esta entrada existe para que mañana no haya que deducir nada. Lo que está en el
Drive es la ronda 13; lo que está APROBADO es una sola pieza.

| Pieza | Archivo en Drive | Estado al cierre |
|---|---|---|
| **S1 · Cumpleaños 1** | `BW FEED 03-09 Cumpleanos 1.png` | ✅ **APROBADA** |
| **S1 · Cumpleaños 2** | `BW FEED 03-09 Cumpleanos 2 detalles.png` | ⏳ sin aprobar — pendiente de comentario |
| **S2 · ST Emergencia** | `BW ST 09-09 Emergencia Between.png` | ⏳ sin aprobar — pendiente de comentario |
| **S3 · To Go 1 portada** | `BW FEED 14-09 Promos To Go 1 portada.png` | ⏳ sin aprobar — pendiente de comentario |
| **S3 · To Go 4 los tres** | `BW FEED 14-09 Promos To Go 4 los tres.png` | ⏳ sin aprobar — pendiente de comentario |
| **S2 · Ella habló** | `BW FEED 11-09 Ella hablo Ella escucho.png` | ✅ aprobada en la ronda 12 |
| **S3 · To Go 2 y 3** | `…2 sandwich.png` · `…3 dulce.png` | ✅ no objetadas; Eli pidió no tocarlas |

⚠️ **Ojo con esto mañana: «no aprobada» no es «rechazada».** Eli aprobó una y
dejó las otras cuatro sin comentar, no las devolvió con correcciones. **No hay
que rehacerlas por iniciativa propia** — hay que esperar qué dice de cada una.
El día ya tuvo tres rondas seguidas (11, 12 y 13) y dos de ellas se fueron en
rehacer cosas que nadie había pedido rehacer.

⭐ **Y lo que SÍ conviene mirar antes de tocar nada:** el criterio con el que
aprobó la Cumpleaños 1 es el que mandó para el resto del carrusel —
**«que sean ilustradas, con el trazado que ya se sabe y se conoce»**. Si mañana
devuelve la Cumpleaños 2, lo más probable es que sea por lo mismo (ahí el adorno
también es doodle, pero el mock del post es un elemento gráfico grande que no
había en la slide aprobada).

**Nada más que hacer hoy.** El repo está al día (`c6757c4`), las 5 piezas están
en sus carpetas del Drive con el mismo enlace de siempre, y los pendientes de
proceso siguen siendo los cuatro de la entrada de la ronda 13 (la ST 03-09 del
cumpleaños, los nombres con fechas viejas, el duplicado «…4 trio.png» y la
pregunta sin responder de `FEED!H16`).

---

## 2026-09-04 · Eli (Windows) — BETWEEN ronda 13: el adorno pasa a ilustración

*(Quinta sesión del día. La ronda 12 está en la entrada de más abajo.)*

**Qué devolvió Eli, y qué se hizo:**

| Pieza | Su comentario | Qué se hizo |
|---|---|---|
| **S1 Cumpleaños 1 y 2** | «me gustó mucho la foto. Sin embargo pusiste una serpentina dorada que **parece un plátano**… Por último, que sean **ILUSTRADAS, con el trazado que ya se sabe y se conoce, punto**» · «está superbién editada el vaso, y la segunda slide» | El adorno **sale de la foto** y pasa a los doodles de pincel de Eli (`recursos/confeti.png`, `globos-par.png`). La foto vuelve a ser sólo foto |
| **S2 ST Emergencia** | «se ve muy mal el fondo. Tiene que ser mejor editado, mejor elaborado… con el café To Go, con el **vaso que ya habíamos logrado**, el que está aprobado. El croissant, que es lo salado. Un **muffin de chocolate**» | Vitrina rehecha de cero: se genera VACÍA y los tres productos reales entran con línea de base común, sombra de contacto, campo de luz y el reflejo del vidrio encima |
| **S3 portada** | «quedó muy bien. Sin embargo el **logo se ve poco centrado**» | Re-medido y re-centrado sobre la CARA VISIBLE del cartón |
| **S3 slide 4** | «se ve **quemada**, se ve basura, y tiene que verse **todas las slides similares en cuanto al tono y los colores**» | Tono igualado a las slides 2 y 3 |
| **S3 slides 2 y 3** | «no las toques» | No se tocaron |

**⭐⭐⭐ El aprendizaje del día, y costó TRES pasadas sobre la misma pieza: un
adorno que va sobre una fotografía es ILUSTRACIÓN, no fotografía.**

| intento | qué era | veredicto |
|---|---|---|
| ronda 11 | papelitos de 5 colores planos, tiras cortas | «se ve muy infantil y mal diseñado» |
| ronda 12 | cintas de ORO metálico, arqueadas, con veta especular y sombra | «parece un plátano» |
| ronda 13 | los trazos de pincel de Eli, encima de la foto | ✅ |

Y lo que hay que entender es **por qué el segundo intento falló por ser mejor**:
la cinta de oro tenía todo lo que el manual pide para un elemento agregado
—tamaño por cercanía, desenfoque según la profundidad de campo, sombra de
contacto, acabado metálico— y precisamente por eso perdió. Un objeto que
pretende ser fotografía **se mide contra la fotografía que lo rodea**, y una
forma dibujada de 40 px no aguanta la comparación con un croissant de 900 px
hecho con un 50 mm. Un doodle, en cambio, no compite: no pretende ser parte de
la escena.

> Y el corolario práctico: **el adorno de Between ya existe.** Son los trazos que
> hizo Eli en Illustrator y viven en `public/assets/hilton/between/recursos/`.
> Antes de dibujar un adorno nuevo, mirar si ya está ahí.

`dorados()` y `cinta()` se quedan en `scripts/between-cumple-fondo.py` **sin
llamarse**, para que el intento y sus mediciones queden registrados.

**⭐⭐ La vitrina de Emergencia: el recetario de montaje completo.** Los cinco
defectos de la anterior eran todos de montaje —caja crema sobre crema sin vidrio
reconocible, productos flotando sin línea de base ni sombra, escalas
incoherentes, el vaso cortado por el marco y recortes sin la luz del interior—.
El orden que sí funciona, y sirve para cualquier vitrina o repisa:

1. **el contenedor se genera VACÍO** (así el generador no inventa productos ni
   logotipos);
2. los productos son **fotografía real recortada**, uno por compartimento;
3. **una sola línea de base**, medida sobre el contenedor;
4. **sombra de contacto** por objeto, corta y densa;
5. **campo de luz** de su propio compartimento;
6. **luz envolvente** en el canto;
7. y **el reflejo del vidrio ENCIMA**.

⚠️ Dos mediciones que costaron una pasada cada una: la vitrina tuvo que rehacerse
**ancha y baja** —con tres compartimentos verticales de 300×1.180 los productos
quedaban con dos tercios de aire encima— y el `PISO` es la línea del piso
**visible** (1230), no el canto inferior del interior (1259): entre las dos corre
el riel de latón, y apoyando en 1259 los tres quedaban medio hundidos detrás de
él.

**⭐ «Quemada» puede ser NARANJA, no blanco.** La slide 4 era la más OSCURA de
las cuatro (mediana 87 contra 99 y 102) y aun así se veía quemada: el problema
era el color. Calidez 55,3 contra 23,7 y 34,2; saturación 57,8 contra 40,9 y
43,6. Es un interior de bar con reflejos naranjas y, contra dos bodegones de luz
de día, se leía anaranjada. `iguala_tono()` corrige calidez, saturación y mediana
**en ese orden**, porque cada una desplaza a la siguiente. Las cuatro slides
quedaron en mediana 95-107, calidez 24-34 y saturación 32-44.

> **Regla: un carrusel se mide entre sus propias slides antes de entregar.**

**⭐ Y el logo del vaso, por segunda vez: se centra en la CARA VISIBLE.** Iba a
206 px centrado en x=920 (el 0,86 del ancho de la silueta), o sea 817-1023, pero
la cara visible del cartón va de 840 a 1023: los primeros 23 px caían sobre el
dedo, la máscara se los comía y la tinta visible arrancaba en 840 — descentrada
28 px. Ahora: 175 px centrado en 932, en la banda donde el cartón libre mide 183
(de y=1250 a 1325; más abajo los dedos lo reducen a 90).

**✅ SUBIDO AL DRIVE, reemplazando por id** (las 5, verificado):

- **S1** → `C2 CUMPLEAÑOS BW`: Cumpleanos 1 y 2 detalles
- **S2** → Emergencia Between
- **S3** → Promos To Go 1 portada y 4 los tres

⛔ **No se tocaron** las slides 2 y 3 del To Go (pedido expreso de Eli) ni «Ella
hablo Ella escucho» (aprobada en la ronda 12).

`between-qa.py` limpio en 4 de 5. El aviso de `BW-F-Cumple-1` es el falso
positivo ya documentado (dos píxeles del canto del plato, gris neutro). Y de paso
el QA cazó un defecto real: el doodle de confeti de la G2 dejaba tinta a 79 px
del canto derecho —el trazo de pincel sobresale ~6 px del ancho declarado, como
ya pasó con los globos en las rondas 7 y 8—; se corrió de x=890 a x=876.

**Herramientas:**

- `scripts/between-cumple-fondo.py` (era `between-cumple-r12.py`) — ahora sólo
  hace el FONDO; los adornos los pone la composición
- `scripts/between-emergencia-r13.py` — la vitrina vacía + los tres productos
  reales, con el recetario de montaje completo
- `iguala_tono()` en `scripts/between-togo4-r12.py`
- `scripts/between-r13-entrega-subir.py`

**Abierto:**

1. La **ST 03-09 del cumpleaños** (`BW-S-Cumple`) sigue siendo una escena
   generada con una vela mientras el feed de ese día ya es fotografía real.
2. Los **nombres de archivo** siguen con las fechas viejas; renombrar va junto
   con borrar la copia vieja (el portal levanta por nombre).
3. El **duplicado «BW FEED 14-09 Promos To Go 4 trio.png»** sigue en la carpeta
   antigua: hay que borrarlo a mano.
4. **`FEED!H16` (Primero la foto)** sigue en REVISAR CONTENIDO con la pregunta de
   la CM sin responder: «¿Qué plato es el que ya está comido?».
5. **Avisarle a Scarlette** que el mock de post volvió (lo había pedido fuera en
   la ronda 5; volvió porque lo mandó Eli con su editable).

---

## 2026-09-04 · Eli (Windows) — BETWEEN ronda 12: dorado elegante, y se deja de montar

*(Cuarta sesión del día. La ronda 11 está en la entrada de más abajo.)*

**Qué devolvió Eli de la ronda 11**, y las cuatro correcciones eran mías:

| Pieza | Su comentario | Qué se hizo |
|---|---|---|
| **S1 Cumpleaños 1 y 2** | «eso que agregaste, de serpentinas se ve muy infantil y mal diseñado. Debe ser **dorado muy elegante**… como está en el editable» · «se ve un poco **blanco y filtro extraño** y desenfocado el vaso togo y **él es el protagonista**» | Serpentinas de ORO metálico en vez de cinco colores planos; exposición fijada por el PRODUCTO, no por el cuadro; nitidez local sobre el vaso; y en la G2 el desenfoque de fondo baja de 9 a 4 px |
| **S1 Cumpleaños 2** | «el logo del icono de la segunda slide no es los colores que se utiliza. Es **fondo café between + logo en beige**» | Avatar del mock corregido: disco `#675B49` con el lockup en `#FFF9EB` |
| **S2 ST Emergencia** | «el cambio es *que el salado sea un crosant jamon queso y que el dulce sea un muffin*» | El cambio **ya estaba hecho en la ronda 10 y nunca se subió**. Se rindió y se subió |
| **S3 portada** | «la chica tiene **recortes** se ve muy mal editado… los textos están bien en el diseño, solo la foto de fondo estaba extraño» | Escena **generada completa en una pasada**. Fuera el montaje |
| **S3 slide 4** | «se ve **quemada y mal**. Vuelve a hacer ese diseño: los tres productos juntos **en formato To Go**… una mano tomando la bolsa o el café» | Escena nueva desde un editable de ELI, con muffin, mano y los dos logotipos estampados con el vector real |
| **S2 Ella habló** | «queda **aprobado**» | No se toca |

**⛔⛔ El error de fondo, y es medible: fijé la exposición por la mediana del
CUADRO.** En la toma del cumpleaños la mitad de arriba es muro vegetal casi
negro, así que la mediana global daba **62**; para llevarla a 104 hizo falta un
gamma que abrió el sujeto un tercio. Resultado: el vaso pasó de mediana 127 a
**166** y su calidez de 25,5 a **18,7** — o sea, kraft blanquecino y sin calidez.
Eso es exactamente «un poco blanco y filtro extraño». Ahora el objetivo se mide
sobre el PRODUCTO (vaso + comida): 118 → 126, y el vaso queda en 130 con calidez
27,8. Y la calidez sólo se corrige si pasa de 28 — el perfil `neutro` del mes
está pensado para las fotos que venían en 35-49, no para una que ya viene bien.

**⭐⭐ Y el otro aprendizaje, sobre los adornos: lo infantil era el COLOR PLANO.**
Los papelitos los pidió el cliente, la idea estaba bien; la ejecución no. Cinco
colores planos en tiras cortas se leen como **grageas de torta**. La referencia
de la marca para «cumpleaños elegante» está en el propio editable de Eli: globos
champán y cintas doradas. Lo metálico no es el color, es la variación — degradado
a lo largo de la cinta (una cinta gira y toma la luz desigual) más una veta
especular. Y forma de cinta: arqueada, afinada en las puntas y de 4,5 a 8,5 veces
más larga que ancha.

**⛔⛔ Lo de la portada es de método y ya van tres rondas.** Era un montaje: una
figura recortada sobre un fotograma del local. La ronda 11 le fundió el canto con
un mapa de nitidez y no alcanzó, porque **un recorte y su fondo nunca comparten
la luz**. Se dejó de montar:

1. **primero se agotó el material real** — 75 fotogramas de los 25 clips `.MOV`
   del cliente: todos interiores del hotel y del cowork, ni un plano de alguien
   saliendo con un vaso. La escena del brief no existe;
2. se generó **entera en una pasada** con Nano Banana Pro, con un fotograma del
   muro vegetal real como referencia y pidiendo el vaso **kraft liso**;
3. **upscaler ×2 antes de recortar** (el 4:5 sale de una ventana de 2.880 px);
4. el logotipo real **estampado y enmascarado al cartón**, para que la tinta no
   caiga sobre los dedos;
5. y el encuadre **calculado para el bloque de texto que ya está aprobado**: el
   vaso cierra en y=1483 y la script arranca en y≈1595.

**⭐⭐ Y un hallazgo que vale para toda la cuenta: el generador conserva el
logotipo de la referencia, pero REDIBUJADO.** En la slide 4 la base fue un
editable de Eli que ya traía los logotipos impresos. El modelo los mantuvo en su
sitio y con la silueta correcta —incluso la `Ǝ` invertida— pero el trazo y el
tracking no son los de la marca. Es lo que el cliente reclamó en la ronda 5. Así
que se pidió el envase **sin ninguna letra** y se estampó el vector real en la
bolsa (0,58 del ancho de la cara, centro al 54 % del alto, medido en el editable
de Eli) y en el vaso.

⚠️ Y ahí salió una corrección a la regla del manual: **la proporción del logo se
mide sobre la CARA VISIBLE, no sobre la silueta.** El 0,86 del vaso oficial está
medido de frente; en un vaso cercano y girado la cara visible es más angosta, y
aplicando 0,86 el logotipo se pasaba y la máscara lo cortaba — quedaba «ƎTWEEN /
OFFEE & BAR». A 320 px (la cara visible medida) se lee entero.

**✅ SUBIDO AL DRIVE, reemplazando por id** (las 5, verificado):

- **S1** → `C2 CUMPLEAÑOS BW`: Cumpleanos 1 y 2 detalles
- **S2** → Emergencia Between *(la que llevaba dos rondas sin subir)*
- **S3** → Promos To Go 1 portada y 4 los tres

⛔ **No se re-subieron** «Ella hablo Ella escucho» (aprobada) ni las slides 2 y 3
del To Go (nadie las objetó y la versión de la ronda 11 ya está revelada). Mover
la fecha de una pieza que el cliente no pidió cambiar sólo lo hace dudar.

`between-qa.py` limpio en 4 de 5. El aviso de `BW-F-Cumple-1` («texto a 1 px del
borde izquierdo») es el falso positivo ya documentado: son **dos píxeles** del
canto del plato, en y=1575 y 1596, de color (234,227,225) — gris neutro, no el
beige de marca. El texto de esa pieza está arriba, entre y=312 y 964.

**Herramientas nuevas, versionadas:**

- `scripts/between-cumple-r12.py` — las serpentinas doradas (`cinta()` dibuja una
  tira arqueada con acabado metálico) y `revela_por_sujeto()`
- `scripts/between-togo1-r12.py` — la portada generada entera, con el estampado
  enmascarado al cartón (`solo_sobre_el_carton()`)
- `scripts/between-togo4-r12.py` — la escena To Go con los dos logotipos
  estampados
- `scripts/between-r12-entrega-subir.py` — entrega a 150 ppp y reemplazo por id

**Abierto:**

1. **La ST 03-09 del cumpleaños (`BW-S-Cumple`)** sigue siendo una escena
   generada con una vela, mientras el feed de ese día ya es fotografía real.
   Está en CORREGIDO y el cliente no la reabrió.
2. **Los nombres de archivo siguen con las fechas viejas** (la grilla se re-fechó
   el 04-09). El portal levanta por nombre: renombrar hay que hacerlo junto con
   borrar la copia vieja.
3. **El duplicado «BW FEED 14-09 Promos To Go 4 trio.png»** sigue vivo en la
   carpeta antigua: hay que borrarlo a mano.
4. **`FEED!H16` (Primero la foto, 14-09)** sigue en REVISAR CONTENIDO con la
   pregunta de la CM sin responder: «¿Qué plato es el que ya está comido?».
5. **La mano de la portada tapa el canto de la «B»** del vaso. Con el logo a
   y=1300 se lee «BETWEEN / COFFEE & BAR» completo salvo ese borde; si se quiere
   intacto hay que cambiar el gesto, no el montaje.
6. **Avisarle a Scarlette que el mock de post volvió** (lo había pedido fuera en
   la ronda 5; volvió porque lo mandó Eli con su editable).

---

## 2026-09-04 · Eli (Windows) — BETWEEN ronda 11: las tres EN CAMBIOS, subidas

**Qué pedía la ronda.** Eli: corregir lo que está EN CAMBIOS en la S1, S2 y S3,
guiándose del brief, de los comentarios del cliente **sin tachar** y de los
mensajes de Scarlette; rehacer fondos; que se vea realista y no falso; que el
vaso To Go sea el actual; borrar rayones, imperfecciones y migas de las mesas. Y
dejó en el Drive **el editable de la slide 2 del carrusel de cumpleaños**
(`1kjIL3VuLnKH0ED3h8lx9kQ4GPUI5XHVF`) «para que lo mejores».

**Primero hubo que volver a leer la grilla, y ahí apareció el primer problema.**
La hoja `FEED` se **re-fechó entera** el 04-09: borró la SEMANA 1 y corrió el mes
—el cumpleaños del 3 al **9**, «Primero la foto» del 9 al **14**, «Ella habló»
del 11 al **16**, las Promos To Go del 14 al **22**—. Y el diff contra la copia
de la mañana salió corrido de columna porque
**`scripts/grilla-instantanea.py` tenía quemada la fila del ESTADO** (`FEED 15`,
cuando en Between es la **16**; la 15 es `COMENTARIOS DISEÑO`). Con eso el
encabezado imprimía el comentario en vez del estado y —peor— el filtro se
**saltaba toda columna sin comentario de diseño**: piezas enteras no aparecían.
Ya está arreglado: la fila se busca por su rótulo en la columna A. La instantánea
de hoy trae las 33 columnas de las tres hojas y **el diff de mañana ya sirve**.

**Las tres EN CAMBIOS, y qué se hizo en cada una:**

| Pieza | Estado / celda | Qué se hizo |
|---|---|---|
| **S1 · Cumpleaños** (FEED 09-09, carrusel) | `FEED!E16` EN CAMBIOS | Las dos slides pasan a ser **dos recortes 4:5 REALES** de la toma `25-257` (se cae el panorama espejado); mesa sin rayones; revelado por medios; **papelitos de colores** sembrados en la escena —el pedido de Scarlette que llevaba dos rondas anotado y no se veía—; el bloque de texto **sube** al muro libre (abajo caía sobre el hojaldre); y la G2 se rehace con **el mock de post de Eli**, corregido |
| **S2 · Ella habló** (FEED 16-09) | `FEED!J16` EN CAMBIOS | «Arriba ella hablo y abajo ella escuchó»: la escena se **voltea en vertical** para que la taza LLENA quede arriba, que es la que habló según el brief. Etiquetas re-medidas, logo arriba, mesa limpia |
| **S3 · Promos To Go** (FEED 22-09, carrusel) | `FEED!L16` EN CAMBIOS | **El revelado de las cuatro slides** (era el «filtro medio raro»), mesas sin rayones ni migas, el logotipo impreso del vaso de vuelta en las 4, fuera el segundo vaso del canto de la G4, canto de la figura fundido en la portada y re-encuadre para que el titular no le pase por encima al vaso |

**⭐⭐⭐ El hallazgo de la sesión, y cierra un reclamo de cuatro rondas.** El
cliente lleva desde el 31-08 diciendo «se ven quemadas y con un filtro medio
raro» y Eli «el vaso está erróneo». No era un filtro ni el estampado: **tres de
las cuatro fotos del carrusel To Go estaban SIN GRADAR**. Medido, calidez
(R̄ − B̄): la del sándwich 20,9 (gradada a `neutro`, el perfil del mes) contra
49,4, 40,7 y 35,1 de las otras tres. Por eso el vaso de la slide 2 se leía
impreso y el de las 3 y 4 «descolorido» — **es el mismo vaso de la misma
sesión**. No había que re-estampar nada: había que sacarle el velo cálido.

**Herramientas nuevas, versionadas:**

- `scripts/between-togo-r11.py` — el revelado de las 4 slides To Go, con
  `borra_rayones()` (rayones grandes **por CROMA**, que es lo que los separa de
  la veta), `limpia_mesa()` (migas incluidas: la del módulo compartido sólo
  cazaba marcas oscuras), `realza_impresion()`, `funde_canto_figura()` y
  `revive_el_muffin()`
- `scripts/between-cumple-r11.py` — los dos recortes reales del cumpleaños y los
  `papelitos()` con tamaño por cercanía, desenfoque según la profundidad de campo
  real y sombra de contacto
- `scripts/between-ellahablo-r11.py` — el volteo y la limpieza de la mesa
- `scripts/between-r11-entrega-subir.py` — entrega a 150 ppp y **reemplazo por
  id** en el Drive

**✅ SUBIDO AL DRIVE, y reemplazando en su sitio.** Las 7 piezas se actualizaron
**por su id**, así que conservan el enlace y el portal ve la versión nueva sin
que nadie reenvíe nada. Verificado en las tres carpetas (todas marcan 12:48–12:49):

- **S1** → `C2 CUMPLEAÑOS BW` (`1TfFCqNfQw0ucTwqvJD8iqft7Y__voRUw`): Cumpleanos 1
  y 2 detalles
- **S2** → `1Yh2Puq1ZEmbM2HaoTh-LUydKwtZRmpn1`: Ella hablo Ella escucho
- **S3** → `1QOreVz6NVYvuri9RAYQRMNiilV_IN8XZ`: Promos To Go 1, 2, 3 y 4

`between-qa.py` limpio en las 7 (el aviso de «titular 27 %» en `BW-F-EllaHablo`
es el falso positivo conocido: esa pieza **no lleva titular** porque el brief
pide que el chiste se lea en la imagen).

**⚠️ Los nombres de archivo quedaron con las fechas VIEJAS, y es a propósito.**
El portal levanta las piezas **por nombre**: renombrarlas crearía duplicados y
dejaría la versión anterior publicada. Renombrar hay que hacerlo junto con borrar
la copia vieja, y es decisión de Eli.

**Lo que se aprendió está en el manual** ([`CLAUDE.md`](CLAUDE.md) § RONDA 11):
los 10 puntos, con las mediciones. Los tres que más sirven para otras marcas:

1. **una fila de la grilla nunca se quema en un script** — se busca por rótulo,
   porque el cliente reordena la hoja sin avisar;
2. **si para llenar un encuadre hay que espejar más de un 10 % del ancho, el
   encuadre está mal elegido** — se cambia el recorte, no se teje;
3. **antes de retocar, prueba a mover el encuadre.** Sacó el vaso cortado del
   canto de la G4 y despejó el titular de la portada, las dos con un zoom del
   5–11 % y sin inventar un píxel.

**⛔ Y una corrección mía, antes de que causara daño.** Escribí que el editable
de Eli tenía un typo («ien cualquier horario»). **No lo tenía:** medí los
contornos del `exclamdown` de Raleway y el signo está bien construido — en esa
familia el `¡` tiene la misma silueta que una «i» de asta larga. El problema de
lectura sí es real, y se resolvió moviendo el signo al arranque de la frase
(«¡Disponible de lunes a viernes, en cualquier horario!»).

**Abierto, en orden:**

1. **Falta avisarle a Scarlette que el mock de post volvió.** La ronda 5 lo había
   sacado por pedido suyo («no me gusta como se ve como post, haría un check
   list») y ahora vuelve porque lo mandó Eli con su editable. Manda Eli, pero
   conviene que no llegue como sorpresa.
2. **`FEED!H16` (Primero la foto, 14-09) sigue en REVISAR CONTENIDO** con una
   pregunta NUEVA sin responder de la CM: «¿Qué plato es el que ya está comido?».
   Es la única novedad de la grilla de hoy que no se tocó — es contenido, no
   diseño.
3. **`STORIES!I16` (Emergencia, 09-09) sigue en REVISAR CONTENIDO.** Los dos
   productos ya se cambiaron en la ronda 10 (croissant de jamón queso y muffin)
   pero **esa pieza no se re-subió** y la del Drive es la del 02-09.
4. **El duplicado viejo «BW FEED 14-09 Promos To Go 4 trio.png»** sigue vivo en
   la carpeta antigua: hay que borrarlo a mano.
5. **La ST 03-09 del cumpleaños (`BW-S-Cumple`)** sigue siendo una escena
   generada con una vela, mientras el feed de ese día ya es fotografía real. Está
   en CORREGIDO y el cliente no la reabrió; unificarla es decisión de Eli.
6. **La mano tapa parte del «COFFEE & BAR»** del vaso en la portada To Go. Es lo
   que pasa de verdad al sostener un vaso impreso y la palabra se lee, pero si se
   quiere entero hay que cambiar el gesto, no el montaje.

---

## 2026-09-04 · Eli (Windows) — BETWEEN ronda 10 · 2.ª pasada: el revelado

**Qué pasó.** La primera pasada cambió el MATERIAL (producto real en vez de
generado) y Eli devolvió las cinco piezas igual: «se ve mal diagramadas», «no se
ve un retoque que se vea apetitosa las imágenes de comida», «el color está muy
oscuro», «tiene que ser realista y no pegoteado», «borrar los rayones de la
mesa», «hay un plato que se ve cortado».

**El diagnóstico, y es de método: faltaba el REVELADO.** Estábamos entregando la
foto del banco cruda. La sesión viene subexpuesta, la mesa de listones está llena
de marcas negras y el hojaldre sale plano — el paso que en un estudio hace el
retocador no existía. Ahora vive en [`scripts/between_retoque.py`](../../scripts/between_retoque.py)
(limpiar madera → revelar → apetitoso → nitidez) y lo comparten las cuatro piezas.

**Qué se rehizo, pieza por pieza:**

| Pieza | Cambio |
|---|---|
| Cumpleaños 1 y 2 | **Se dejó de montar.** Ya no se mueve el vaso ni se borra el plato: la slide 1 es la foto tal cual —el café CON las medialunas, como pidió Eli— y la slide 2 la misma mesa siguiendo. Mesa sin rayones, exposición arriba, hojaldre con claridad |
| ST Emergencia | Los tres productos con la luz del nicho aplicada, apoyados en una misma línea de base, con el reflejo del cristal ENCIMA (antes quedaban pegados sobre el vidrio) y el muffin aclarado. El café también pasó a ser el vaso real |
| To Go portada | Fondo de 26 a 13 px de desenfoque + **luz envolvente** en el canto de la figura + revelado. Era el «se ve mal montada» |
| To Go slide 4 | El plato del dulce entra ENTERO, mesa limpia, muffin aclarado y **fuera las etiquetas «Salado»/«Dulce»**: no cabían sin apretar la pieza y la caja de la promo ya nombra los tres |

**Lo que se aprendió está en el manual** ([`CLAUDE.md`](CLAUDE.md) § RONDA 10 ·
SEGUNDA PASADA): el orden del revelado; por qué el **gamma de medios** es lo que
arregla «está muy oscuro» y no subir las luces (que quema el hojaldre); por qué
la mesa aguanta el espejo y el muro no; las tres cosas que delatan un recorte
pegado —la luz del destino, lo que va delante, la línea de base—; y las dos
falsas alarmas del «vaso cortado» en la slide 4.

**⚠️ Un aviso del QA que es FALSO POSITIVO.** `between-qa.py` marca «texto a 0 px
del borde izquierdo» en `BW-F-Cumple-1` y `BW-F-ToGo-4`. No es texto: es el
hojaldre (231,228,207) y el borde del plato (210,222,221) pegados al canto, que
caen dentro del umbral con el que el QA aísla el beige de marca. Verificado
midiendo en qué filas cae. El texto de las dos piezas está centrado y con margen.

**Dónde quedó.** Renders en `out/hilton-between-r10/` y la entrega con nombre de
portal en `out/entrega-r10/`. **Sigue sin subirse nada al Drive**, esperando el
visto bueno de Eli.

**Abierto (viene de la pasada anterior):**

1. El duplicado viejo «BW FEED 14-09 Promos To Go 4 trio.png» hay que borrarlo a
   mano en el Drive: la entrega usa el nombre de la ronda 9 («…4 los tres.png»)
   para reemplazar la pieza viva.
2. La ST 03-09 del cumpleaños (`BW-S-Cumple`) quedó como estaba —está en
   CORREGIDO y el cliente no la reabrió— pero ahora el feed de ese día es
   fotografía real y la historia sigue siendo una escena generada con una vela.
3. **Avisarle a la CM que las medialunas se quedan.** Scarlette pidió «sacar el
   plato de los vigilantes» y Eli pidió lo contrario. Manda Eli, pero conviene
   que no llegue como sorpresa en la ronda siguiente.

---

## 2026-09-04 · Eli (Windows) — BETWEEN ronda 10: la cuenta deja de generar producto

**Qué pedía la ronda.** Un comentario NUEVO de Scarlette del 03-09 22:25 —
comentario nativo de Excel en `FEED!E15`, no en la fila 15, así que **leyendo
sólo la fila se pierde** (ya pasó en la ronda 5) — más dos pendientes sin tachar
que llevaban días en la grilla:

| Dónde | Estado | Qué pedía |
|---|---|---|
| `FEED!E15` · Cumpleaños 3-sep (S1) | EN CAMBIOS | «no les gusta la propuesta :( me piden usemos la imagen que te adjunto acá igual hay que retocarla, **cambiar el vaso al nuevo**, **sacar el plato de los vigilantes**, y poderle algo que haga ref a cumpleaños al rededor (quizas en la mesa poner como esos **papelitos de colores** que se lanzan) y la **imagen de la slide 2 tiene que tener relación** igual con la primera» |
| `FEED!L15` · To Go 14-sep (S3) | EN CAMBIOS | «el **fondo no tiene nada que ver con BT**, tenemos algunos videos que hemos hecho en la entrada de BT, saquemos el fondo de ahí?» |
| `STORIES!I15` · Emergencia 9-sep (S2) | REVISAR CONTENIDO | «Cambiaría que el **salado sea un crosant jamon queso** y que el **dulce sea un muffin**» |

Y encima, de Eli: la imagen de las dos slides del cumpleaños **continua**, con el
café en la primera; y del carrusel To Go, arreglar la portada («el vaso está
erróneo») y la slide 4 («mejora la foto y el vaso»).

**⭐⭐⭐ El hallazgo de la sesión, y cambia el método del mes.** El cliente lleva
**desde la ronda 4** reclamando lo mismo por cuatro caminos distintos —el vaso
con logotipo inventado, la taza con marca ajena, «nada que ver jajajaja», «que
no se vea tan IA»— y lo veníamos tratando como un problema de prompt o de
estampado. **No lo era: el producto está fotografiado y no lo estábamos usando.**
La carpeta `BETWEEN 25 JULIO MODELOS` del propio cliente
(`1gI00XGbBV5YjqcSjG3SmmkMuxr-ev_60`, 60 archivos) trae el vaso vigente solo, con
croissant de jamón queso, con muffin, con rol de canela y con los vigilantes —
todo sobre la misma mesa, el mismo muro y el mismo 50 mm.

Y el remate: **la foto que adjuntó Scarlette y `25-257` son la misma toma con 63
segundos de diferencia** (EXIF: 15:45:11 y 15:46:14, mismo cuerpo, mismo lente,
mismo diafragma). El fotógrafo hizo la mesa con el vaso viejo y con el nuevo, así
que «cambiar el vaso al nuevo» **ya estaba disparado**. Cero IA en el producto.

**Las 5 piezas, todas con QA limpio** (`out/hilton-between-r10/`, entrega armada
en `out/entrega-r10/` con el nombre del portal y 150 ppp):

| Pieza | Qué se hizo |
|---|---|
| `BW-F-Cumple-1` y `-2` (S1) | **Una sola fotografía real partida en dos slides.** Base `25-248`, plato de los vigilantes borrado, escena espejada para que el café quede en la slide 1 con su fondo y su sombra reales, y papelitos de cumpleaños sembrados sobre la mesa. Fuera el doodle de confeti: ya está en la escena |
| `BW-S-Emergencia` (S2) | Los dos productos de la vitrina cambiados por **recortes reales**: muffin de chocolate (dulce) y croissant de jamón queso (salado). Los textos de la encuesta no se tocan |
| `BW-F-ToGo-1` (S3) | Fondo = `HDT_56`, la foto de arquitectura del propio local (barra de mármol, mural dorado y el pasillo hacia el muro vegetal de la entrada), desenfocado. Vaso = el REAL de `25-248`, con los dedos devueltos encima |
| `BW-F-ToGo-4` (S3) | Bodegón **enteramente real**: café + croissant jamón queso (de `25-278`) + muffin en su plato (de `25-266`). Las cuatro coordenadas de etiquetas y flechas re-medidas |

**Herramientas nuevas, todas versionadas:**

- `scripts/between-recortes-reales.py` — recorta productos con grabCut y deja el
  alfa limpio en `public/assets/hilton/between/recortes/`
- `scripts/between-cumple-panorama.py` — el panorama continuo del cumpleaños
- `scripts/between-emergencia-productos.py` — cambia los productos de la vitrina
- `scripts/between-togo4-bodegon.py` — el bodegón real de la promo
- `scripts/between-togo1-real.py` — la portada con fondo del local y vaso real

**⭐ Y una de método que sirve a todas las marcas:** con
`https://drive.google.com/thumbnail?id=<ID>&sz=w4000` Drive devuelve **el archivo
ORIGINAL** aunque el token no tenga permiso, siempre que esté compartido por
enlace. Con `sz=w640` se arman hojas de contacto baratas. Así se eligieron las
fotos sin bajar 700 MB.

Todo el detalle técnico —los cuatro intentos fallidos de borrar el plato, por qué
espejar en vez de recortar, la proporción como prueba objetiva de que un vaso es
generado, y las dos trampas de grabCut— quedó en el manual,
[`clients/hilton/CLAUDE.md § RONDA 10`](CLAUDE.md).

**⛔ Lo que NO se hizo, y hay que decidir:**

1. **Nada se subió al Drive todavía.** Las 5 piezas están en `out/entrega-r10/`
   listas. Ojo con un detalle: la slide 4 del To Go está **DUPLICADA en el
   Drive** con dos nombres —«…4 trio.png» (ronda 7, carpeta vieja) y «…4 los
   tres.png» (ronda 9, en `S3 · BW`, que es la carpeta viva)—. El script de
   entrega ya usa el nombre de la ronda 9 para que la corrección REEMPLACE en vez
   de dejar una tercera copia, pero **el duplicado viejo hay que borrarlo a mano**.
2. **La ST 03-09 del cumpleaños (`BW-S-Cumple`) quedó como estaba.** Está en
   CORREGIDO y el cliente no la reabrió, pero ahora el feed del mismo día es
   fotografía real y la historia sigue siendo una escena generada con una vela.
   Es decisión de Eli si se unifica.
3. **El metraje de la entrada que menciona el cliente no está en el repo.** Se
   usó la foto de arquitectura, que es del mismo lugar. Si aparece el video, se
   cambia sólo la placa de fondo en `between-togo1-real.py`.
4. En la portada To Go, **la mano tapa parte del logotipo del vaso** — es lo que
   pasa de verdad al sostener un vaso impreso, y la palabra se lee, pero si Eli
   lo quiere entero hay que cambiar el gesto, no el montaje.
5. **Nano Banana Pro está sin créditos** (`HTTP 502 · Error consuming credits`).
   No hizo falta —todo salió de fotografía— pero conviene saberlo antes de
   planificar una pieza que sí necesite generar ambiente.

---

## 2026-09-03 · Eli (Windows) — DOUBLETREE: la marca entra al estudio, y su tipografía queda cerrada

*(Tercera sesión del día. Las dos de Between están más abajo.)* **Primera sesión de DT
en el estudio**: hasta hoy la marca no tenía ni una entrada en esta bitácora.

**Qué se hizo.**

1. **La grilla de DT es legible y ya tiene línea base.** Se modificó hoy 20:28Z
   (Carlos Figueroa) y no existía copia previa contra la cual diffear. Bajada con
   `export?format=xlsx` (49,5 MB, va a `raw/`, no viaja) y volcada a texto con el
   script nuevo `scripts/grilla-instantanea.py`, que conserva **tachados e
   hipervínculos** — que es justo lo que se pierde al copiar y pegar la celda.
   Queda en `clients/hilton/grillas/dt-septiembre-2026.md`. **Desde mañana la ronda
   nueva se detecta por diff.**

2. **Estado real de septiembre en DT.** Entregado y en Drive: `C1 FT` (APROBADO),
   `C1 ER DT S2` (CORREGIDA), `C2 ER FIESTAS PATRIAS` (EN REVISIÓN) y las 2 historias
   de la S1 (APROBADO). **Producible y sin empezar: 4 piezas** — el estático de
   Opinión Booking (14-09) y las historias de Escapada Romántica (07-09), Gimnasio
   (10-09) y Día del Turismo (27-09). Bloqueadas: los 2 reels (POR GRABAR, con
   Sebastián Serrano, y la grilla prohíbe IA ahí), el saludo de Fiestas Patrias
   (PENDIENTE POR CLIENTE), «Tu día en DoubleTree» (REVISAR CONTENIDO) y el reel
   orgánico del 10-09, que está EN CAMBIOS **con la celda de DISEÑO vacía**.

3. **⭐ La tipografía de DT quedó cerrada por regla de Eli: Stag + Trade. Raleway
   fuera.** Escrito en el manual. Las 11 fuentes están en el repo
   (`public/assets/hilton/dt/fonts/`): 9 cortes de Stag y los 2 de Trade que Eli
   consiguió por su cuenta —el cliente no las entregó—, **más su conversión a WOFF2**,
   porque venían en `.otf` CFF, el formato que hizo que Remotion rindiera 27 piezas de
   Between con una serif de reemplazo sin avisar.

4. **⭐⭐ El reparto Stag/Trade no es estilístico, es de cobertura de glifos.** Los 9
   pesos de Stag traen 354 glifos y **no incluyen `$ % ¿ ¡ @`**. Por eso los precios
   («$125.000»), las preguntas («¿Ya eres Hilton Honors?») y el correo del CTA
   (`reservas.dtv@hilton.com`) **tienen que ser Trade**: Stag no puede escribirlos.

5. **⛔ Un error mío, corregido antes de causar daño.** Medí el ancho `1`/`0` de la
   cifra, vi que no era Stag, y —porque el `Informe.txt` del `.ai` nombraba Raleway—
   escribí en el manual que las piezas entregadas estaban fuera de sistema. **Era
   deducción, no medición.** La segunda huella, alto del `$` ÷ alto del `0` (invariante
   a tamaño y peso), da **1,225** en la pieza contra **1,24 de Trade** y **1,55 de
   Raleway**: era Trade desde el principio. **No hay nada que rehacer.** La regla
   quedó en la memoria `adn-desde-editables`: una huella descarta, dos confirman.

**Dónde quedó.** Manual de la marca con la sección de tipografía de DT completa y
corregida; grilla en texto; fuentes instaladas y verificadas; `_estado-sync.json` al
día. **El ADN no está hecho todavía** — no hay `marca.json`, ni `reglas.yaml`, ni
`src/brand/doubletree.ts`.

**Lo ya medido, para no repetirlo:** mesa **1080×1350** → entrega feed **2250×2813** e
historia **2250×4000** (2,083×); tinta plana **PANTONE 2766 C**; azul medido `#0B194A`
en feed y `#111C4E` en historia (el manual dice `#09194E`, falta afinarlo sobre zona
plana); **logo con proporción 1,2266**, confirmada contra dos archivos distintos
(`JUNIO/DT/S3/logo DT.png` y el de Abril).

**Qué sigue.** El ADN sobre las 7 piezas aprobadas: retícula y márgenes, geometría de
la píldora y de la caja de beneficios con separadores, jerarquía del titular a dos
pesos de Stag. Con eso, `marca.json` + `reglas.yaml` + `src/brand/doubletree.ts` y las
plantillas de feed e historia.

**Abierto.**
- **Falta el Trade Bold de ancho normal.** Es el corte con el que está compuesta la
  cifra de la pieza aprobada (ancho `1`/`0` = 0,764; los dos instalados dan 0,654 y
  0,600). Con lo que hay, el sustituto es Bold Condensed No. 20, pero **al mismo alto
  de dígito la píldora pasa de ~630 px a ~410 px** — cambia la proporción del bloque.
  Decisión de Eli, mirando el render, no leyendo.
- **La grilla se contradice sola:** `VISTA MENSUAL` pone el estático Booking el lunes 7
  y el carrusel Escapada Romántica el 14; la hoja `FEED` los pone al revés. **Lo
  confirma Carlos**, y cambia la fecha de entrega.
- **Falta el contenido de la reseña de Booking**: texto literal, iniciales del huésped
  y rating. El cliente aprobó «el que sugiere Carlos»
  (`imagen_2026-08-14_112424991.png`), pero la carpeta de reseñas
  (`1Dlki995RRdwueFGlZOkF9rybf7maMJ5u`) no devuelve archivos por el conector.
- **`DT-S2.ai` declara Raleway** en su `Informe.txt`. No está verificado en qué
  elemento. Con la regla nueva, revisarlo cuando se toque esa pieza.
- **Licencia:** las fuentes las consiguió Eli, no el cliente. Vale saberlo antes de
  repartirlas a otro diseñador que clone el repo.

---

## 2026-09-03 · Eli (Windows) — BETWEEN: auditoría de reproducibilidad y respaldo

*(Segunda sesión del día. La ronda 9 está en la entrada de más abajo.)*

**Qué se hizo.** Se instaló un segundo estudio en `~/copylab/EDITOR VIDEOS` y,
al verificarlo, apareció el problema de fondo: **el repo no alcanzaba para
reproducir Between**. Se auditaron las 32 imágenes que usa
`BetweenSeptiembre.tsx` cruzándolas contra git, y las 27 composiciones de
`Root.tsx` contra el disco. Resultado: **19 piezas rinden, 8 no** — las 8 son
historias cuyas imágenes de origen no existen en ninguna parte.

**Dónde quedó.**
- `togo-salida-3.png` (18 MB) faltaba en git: `.gitignore:69` tapa
  `public/assets/**` y el `/cierre` anterior subió 21 de 22. Commiteada (`dd36a5a`).
- Los 9 scripts `between-*.py` y las 20 imágenes que existen: verificados en
  GitHub. **Los 16 carruseles se rehacen desde un clon limpio** — comprobado
  rindiendo `BW-F-Cowork-1` y `BW-F-ToGo-1` (1080×1350 ✓).
- Las 8 historias irrecuperables estaban **sólo en el disco externo `F:`**. En el
  disco interno había 3 historias rendidas y eran justo las 3 que sí se rehacen.
  Copiadas a `out/_respaldo-F-between-sept/` (SHA256, 27 de 27 idénticas) y
  **subidas a Drive**: subcarpeta `respaldo` dentro de `S3 · BW`
  (`1vr5rwVu84cmcgQDrj8yjhCfxcFZHGZyE`), 8 de 8 verificadas, con
  `scripts/between-respaldo-historias.py` (`aac0686`). Decisión de Eli: carpeta
  aparte para no interferir con la entrega.
- El manual de la marca ya trae la sección con las 8 composiciones rotas y la
  regla para octubre.

**Qué sigue.** En octubre, guardar las imágenes de origen junto con las piezas y
subirlas con `git add -f` el mismo día — hoy se salvó por el disco externo. Y
antes de cerrar un mes, cruzar composiciones registradas contra archivos en disco.

**Abierto.** Las 12 imágenes de origen de esas 8 historias no aparecieron: se
buscó por nombre y por palabra suelta en las 2.568 imágenes de
`F:\Carpeta de grillas Hilton 2026`. Si están en el Mac, vale la pena traerlas;
si no, esas 8 piezas sólo se pueden rehacer desde cero. **Avisar antes de
comprometer plazo si el cliente pide cambios ahí.**

---

## 2026-09-03 · Eli (Windows) — BETWEEN ronda 9: las 4 piezas EN CAMBIOS de la S1, S2 y S3

**Qué pedía la grilla.** `BETWEEN _ GRILLA SEPTIEMBRE 2026` marcó cuatro piezas
de FEED en `EN CAMBIOS` y ninguna de STORIES:

| | Fecha | Semana | Pieza |
|---|---|---|---|
| FEED C | 01-09 | S1 | Carrusel Cowork — **reabierto hoy** (`CORREGIDO` → `EN CAMBIOS`) |
| FEED H | 09-09 | S2 | Carrusel «Primero la foto… ¿o no?» |
| FEED J | 11-09 | S2 | Ella habló / Ella escuchó |
| FEED L | 14-09 | S3 | Carrusel Promos To Go |

**Las 13 láminas están entregadas y verificadas byte a byte en Drive.** La
portada del Cowork se REEMPLAZÓ en su sitio (mismo enlace,
`1cF7afo5tP4Lixq_YyGWyd7iQJIEw6kb1`); las otras nueve son nuevas, sueltas en la
carpeta de su semana como pidió Eli:

- **S1 · `C1 COWORK`** (`1GB6NtoG3vy35rPj7bw-j8bc76-Jz8332`) — portada nueva.
- **S2 · `BW`** (`1Yh2Puq1ZEmbM2HaoTh-LUydKwtZRmpn1`) — las 4 de «Primero la foto»
  + «Ella habló Ella escuchó».
- **S3 · `BW`** (`1QOreVz6NVYvuri9RAYQRMNiilV_IN8XZ`), que estaba vacía — las 4
  del To Go.

Se sube con `python scripts/between-subir-c1.py s2r9 s3` (el script dejó de tener
la carpeta de render quemada: ahora acepta `--render` y `--solo`).

**⭐⭐ El hallazgo, y es de material: las tazas de loza del cliente traen KIMBO
impreso al costado.** Por eso el reclamo se repite desde la ronda 4 sin que nadie
diera con la causa. En las tomas **cenitales** el logotipo no se ve —queda en la
pared exterior—, así que el reclamo no obliga a generar tazas: **obliga a elegir
cenitales**, que es justo la otra mitad de lo que pide el cliente («desde arriba,
como la refe»). Las cuatro slides del FEED H salen ahora de fotos REALES de la
sesión `3 ENERO _ PLATOS - DESAYUNOS` del propio cliente, todas cenitales, sobre
su mesa de listones — con eso se cae también «el lugar no se parece en nada a
Between». La única sin cenital equivalente (el croissant de jamón y queso) se
resolvió borrándole la marca con `scripts/between-quitar-kimbo.py`, que **rellena
interpolando el esmalte**: clonar una franja vecina dejaba un rectángulo visible
porque la taza tiene degradado lateral.

**La portada del Cowork es el LOUNGE**, por indicación de Eli. Scarlette había
comentado hoy 09:33 «el espacio de la slide 1 ya no existe :((( si vamos a
mostrar de fuera tendría que ser del espacio más amplio de la terraza»; manda lo
que dijo Eli. La foto es `espacios/HDT_37.jpg` y el encuadre se eligió **por
exclusión**: esa toma tiene una placa KIMBO atornillada al muro, una bolsa de café
KIMBO sobre la barra y **una persona con rostro reconocible** tras el vidrio. De
528 encuadres 4:5 anclados abajo, sólo cuatro no tocan ninguna de las tres zonas.

**⛔ Los videos de la entrada de Between NO existen en el material del estudio.**
El cliente los ofreció para la slide 1 del To Go («tenemos algunos videos que
hemos hecho en la entrada de BT»). Se buscaron en las 7 carpetas de `GRILLA IA
BETWEEN` y en todo `raw/` —incluida la sesión BW 2023 de 596 fotos y los 91
fotogramas de los 25 MOV— y **no hay un solo plano exterior**. La slide se
resolvió con el método que el manual ya tenía escrito (ronda 6 §2): el local
real entra **muy desenfocado**, pasado por referencia. **Si Eli consigue esos
videos, la slide se rehace con un fotograma y queda mejor.**

**Lo demás que cambió, por pieza:**
- **FEED J** — escena rehecha entera: dos tazas separadas en diagonal, arte latte
  en la llena y cerco de café seco en la vacía, una mano por taza. Las manos se
  revisaron al 400 % y son **de mujer**, porque el copy dice «etiqueta a esa
  amiga» y la primera generación puso una mano que leía como masculina. Los
  textos van **sin caja**, como pidió el cliente: se pudo porque la escena nueva
  los deja sobre mesa oscura.
- **FEED L slide 4** — entra el **brownie**. Al cambiar la escena hubo que
  **volver a medir** las etiquetas «Salado» y «Dulce»: con las coordenadas viejas
  una caía sobre el producto y la otra dentro de la caja de la promo.
- El logotipo del vaso se **re-estampó desde el archivo real** en las dos slides
  del To Go, aunque la generación lo devolvía legible: proporción 3,0278 exacta.

**QA 12/13 limpias.** La única con aviso es `BW-F-EllaHablo` («el titular ocupa
29 %»), y es **falso positivo**: esa pieza no lleva titular por brief. Queda
escrito en el manual junto al otro falso positivo conocido. `npm run typecheck`
limpio.

**⭐ 2.ª vuelta del mismo día — la portada del To Go.** Eli devolvió tres cosas y
la pieza está **re-subida al mismo enlace** (`1lhUHAgIi_6mXPEpe_Yqxg5eaxyvqxjgG`):

1. **Fuera el lockup de arriba** — «borra el logo principal ya que está en el vaso
   TO GO». Es la regla 8 del manual (el vaso ya firma) aplicada donde más se nota.
2. **El logotipo del vaso, rehecho.** El defecto no era el estampado sino **la
   toma**: la mano envolvía el vaso a media altura y dejaba sólo 70 px de cartón
   limpio, así que el logo entraba al 0,60 del ancho del cuerpo y pegado a la
   tapa. Se editó la foto pidiendo **la mano agarrando abajo y el vaso de
   frente**: el cuerpo pasó de 335 a 670 px y el logo de 200 a 520.
3. **El horario sin caja** — «se ocupó en el texto de promo». `PilaDatos` tiene
   ahora `datosSinFondo`.

⚠️ Y una trampa que costó dos generaciones: **al re-generar la escena completa el
modelo vuelve a meter una persona borrosa al fondo** (los espacios que van de
referencia traen gente). La salida fue dejar de generar y **editar la versión
buena** como única referencia — `between-togo1-salida.py --editar <imagen>`. Salió
a la primera.

**⭐⭐ 3.ª vuelta — el carrusel To Go completo, re-subido a la S3 (mismos enlaces).**

1. **⭐⭐⭐ Las cifras eran de ESTILO ANTIGUO.** «Los números no se ven uno más
   arriba y abajo que los otros» no es avance horizontal: en «$4.290» el 4 y el 9
   bajaban de la línea base. **Raleway las trae así por defecto** —no tiene
   `onum`, y `lnum` es lo que las sube a caja alta— y el `lnum` se había **perdido
   al borrar la declaración que también llevaba el `tnum` inútil**. Ojo: activarlo
   **cambia los anchos** (el «0» de ExtraBold pasa de 614 a 707), así que hubo que
   **re-medir las dos tablas** de `cifrasTabulares` sobre los glifos `.lf`.
   ⚠️ Quedan dos piezas ya entregadas con cifras viejas: `StToGoDulce` (ST 01-09)
   y `StCowork` (ST 16-09). Ninguna otra del mes tiene dígitos.
2. **«Promo To Go» sale de las slides 2, 3 y 4** — sólo va en la portada. Con una
   sola línea, cada pila queda en una caja (la del precio), y de paso se cierra
   solo el choque que había quedado abierto con el «que quede como en la slide 1
   y 2» de Scarlette.
3. **El logotipo del vaso, re-medido contra un vaso REAL** (`Between-67.jpg`): ahí
   va al 0,92 del ancho del cuerpo y **centrado en la vertical (0,485)**. Lo
   entregado iba en 0,13, o sea pegado a la tapa — eso era lo que se veía falso.
   Corregido a 0,72 / 0,32, que es el máximo que deja la mano: el rectángulo de
   cartón limpio de esta foto es `x 1027–1497 · y 2272–2427`.
   ⛔ **La composición no se tocó**: modelo, tamaño de mano y encuadre son los que
   Eli aprobó. Se probó bajar el agarre con otra generación y el modelo volvió a
   agrandar el vaso e inventarle una faja — se descartó.

**⭐ 4.ª vuelta — S2 APROBADA por Eli. En la S3 quedaban dos slides.**

- **Slide 1**: «la mano se ve gigante… y el vaso también». Cierto, y la causa es
  de método: **para que el logotipo entrara al tamaño del manual se había
  agrandado el vaso, y con él la mano.** Eso invierte la jerarquía — la escala de
  un objeto la fija el cuerpo que lo sostiene, no lo que necesita el estampado.
  Se volvió a la toma de escala natural y el logo se corrigió dentro de lo que esa
  foto da: pasa de 200 px **42 px a la derecha del eje** a 230 px **en el eje**.
- **Slide 4**: «se ve extraño el vaso y el logo». El defecto era la **proporción**:
  el vaso generado tenía alto/ancho **1,26** contra **1,02** del vaso real del
  cliente, o sea 24 % estirado. Se regeneró con el vaso real como referencia y el
  cartón liso, y se estampó a los ratios medidos.
- Slides 2 y 3, sin tocar. Las cuatro re-subidas a los mismos enlaces.

⚠️ Dos trampas que quedaron escritas en el manual: `--clonar abajo` trae lo que
haya DEBAJO de la caja (acá pintó el brownie sobre el vaso), y la geometría de
`flechaBucle` —punta en (0,58·0,06), cola en (0,03·0,97)— que costó tres renders
adivinar.

**Abierto:**
0. ✅ RESUELTO en la 3.ª vuelta: al sacar «Promo To Go» de las interiores, las
   cuatro slides quedaron con una sola caja y el carrusel volvió a leerse parejo.
   ⚠️ Pendiente en su lugar: **re-rendir `StToGoDulce` y `StCowork`**, que quedaron
   con las cifras de estilo antiguo.
1. **Los videos de la entrada de BT** — si aparecen, se rehace la slide 1 del To Go.
2. **STORIES no tenía nada `EN CAMBIOS`**: H es el reel Café Bombón esperando que
   el cliente conteste lo de la leche condensada, J está `POR GRABAR` y M/O/Q/R/T/U
   están `OK PARA DISEÑAR` — son piezas nuevas, no correcciones. Falta acordar con
   Eli si se toman.
3. **FEED G (7-sep)** retrocedió de `APROBADO` a `CORREGIDO` en la grilla el
   03-09. Probable error de tipeo del CM: conviene confirmarlo antes de tocarlo.

**⭐⭐ Y lo primero del día, que es lo que hizo posible todo lo demás: la grilla
SÍ se puede leer desde este PC.** El cierre de ayer dejó la S2/S3 sin tomar
declarando un bloqueo de acceso. Era falso. El token da 404 porque tiene alcance
`drive.file`, pero **la grilla está compartida por enlace**: baja entera y con
formato con un `curl` sobre `uc?export=download` (78.206.603 B, calzados contra
el `fileSize` de Drive), y `openpyxl` con `rich_text=True` devuelve el **tachado**
y el color de cada run. Los comentarios vigentes de H, J y L salieron en dos
minutos. Está escrito en el manual, § *CÓMO SE BAJA LA GRILLA*.

De paso, **la ronda de hoy 09:33 fue SOLO DE ESTADO**: 11 celdas cambiadas y cero
comentarios nuevos. El valor estaba en el cambio `REVISAR CONTENIDO` → `EN CAMBIOS`
de H, J y L —luz verde para diseñar con el brief que ya estaba escrito— y en que
lo entregado ayer quedó marcado `CORREGIDO`, la ST Emergencia incluida. Se detectó
por **diff celda a celda** contra la copia de ayer, no leyendo la fila 15.

⭐ Y quedó resuelta una de las 4 decisiones abiertas del documento de Constanza:
**el «Intercambiemos fechas con el de cowork» está TACHADO**, o sea muerto.

> ℹ️ Hallazgo que no es de Hilton pero conviene que se sepa: el `/al-dia`
> consultaba `constanza.lizana@copywriters.cl` y daba cero desde el 28-08. La
> grilla de Selfie es de **`constanza.olivares@`**, que sí tiene movimiento. Hay
> dos Constanzas en el equipo. Anotado en `clients/_estado-sync.json`.

---

## 2026-09-02 (cierre) · Eli (Windows) — BETWEEN: la ST «Emergencia» de la S2, rehecha entera

**Qué se hizo.** La **ST Emergencia (9-sep, S2)** completa. Eli pasó el brief y
los dos comentarios por chat —la grilla sigue sin poder leerse desde acá, ver la
entrada de más abajo—, y los dos decían lo mismo desde dos lados:

    Cliente:   «No se cacha bien al tapar la vitrina con el texto, veamos otra
                diagramación?»
    Scarlette: «no se parece a na ref, hagámosla más simple, NO ambientada en un
                lugar sino que tenga más PROTAGONISMO LA MISMA CAJA, y ojo con la
                diagramación de los textos: tapa mucho la caja.»

Al mirar la versión anterior fallaba en **cinco** cosas, y las cinco están en
esos comentarios: era un **nicho en una pared** —o sea ambientada, y **sin
vidrio** aunque el brief pide «caja de emergencia CON VIDRIO»—, el titular iba
**dentro** de la caja sobre la pared del fondo, y **faltaba un producto**: el
brief pide TRES (café, pastelería y sándwich) y había dos, mientras la encuesta
ofrecía «algo salado» que no estaba en cuadro.

Ahora: vitrina frontal con vidrio sobre fondo liso, tres compartimentos con los
tres productos, y **el texto fuera de la caja** —titular arriba, bajada y
encuesta abajo—. El vaso es el **To Go de Between**: se generó liso y se le
estampó el logotipo real al 0,86 del ancho del cuerpo (la proporción medida del
manual). Cuatro generaciones hasta dar con el encuadre.

⭐ **El tamaño de la caja es una RESTA, no un gusto.** El sticker de la encuesta
mide 196 px y la zona segura inferior de Meta empieza en 1580, así que la
encuesta no puede arrancar después de 1384. Con la generación tal cual —la caja
llegaba a y=1355— `between-qa.py` marcaba «entra 52 px en la zona segura». En
9:16 **o la caja es enorme y el texto la pisa, o el texto respira y la caja cede
altura**; no hay tercera opción. Se monta a 675 px de alto (64 % del ancho).

**Dos cosas de método que quedaron en el código:**
· El fondo se monta **ADITIVO** (`between-emergencia-montar.py`): se suma al
  lienzo sólo lo que el recorte se aparta de su propio fondo, en vez de pegar un
  rectángulo. Pegarlo dejaba una banda donde la sombra se cortaba de golpe.
· `TitularBetween` **deja de poner la sombra cuando el tono es `cafe`**. Esa
  sombra existe para que el beige se lea sobre foto; sobre crema sólo ensucia el
  contorno. Es la única pieza con ese tono, así que no re-fluja nada.

**Dónde quedó.** Drive, carpeta **`BW` de la S2**
(`1Yh2Puq1ZEmbM2HaoTh-LUydKwtZRmpn1`, que Eli abrió hoy y no cuelga del `BW` de
la S1): `BW ST 09-09 Emergencia Between.png`, 3,07 MB verificados byte a byte.
Se sube con `python scripts/between-subir-c1.py s2`.
Código: `StEmergencia` en `BetweenSeptiembre.tsx`. Scripts nuevos:
`between-emergencia-magnific.py` y `between-emergencia-montar.py`. Los tres
assets versionados con excepción en `.gitignore`.
**QA 7/7 limpias, typecheck limpio.**

**Qué sigue.** Las otras cuatro piezas de la S2: **FEED G** (7-sep), **H**
(9-sep), **J** (11-sep) y **L** (14-sep). Están descritas en la entrada de más
abajo con lo que pide cada una.

**Abierto:**
1. ⛔ **La grilla sigue sin poder leerse desde este PC** — es el bloqueo real
   para tomar la S2/S3. El detalle del porqué y cómo se destraba está en la
   entrada siguiente. Hoy la ST salió sólo porque Eli pegó el brief y los
   comentarios en el chat.
2. ⚠️ **La referencia de Pinterest del cliente no se pudo abrir**
   (`cl.pinterest.com/pin/1040683426409551586`): Pinterest sirve una página vacía
   a los bots y lo que se logró bajar era un pin RELACIONADO, no el suyo. La
   pieza se hizo con las indicaciones escritas. **Si Eli quiere que calce con ese
   pin, tiene que pegar la imagen.** Vale para cualquier próxima ref de Pinterest.
3. Las 4 decisiones abiertas del documento de Constanza (tipografía rígida,
   cifras tabulares, interlineado, y si el «intercambiemos fechas» ya está muerto).

---

## 2026-09-02 (noche) · Eli (Windows) — BETWEEN ronda 8b: el C2 Cumpleaños, y por qué la S2/S3 quedó trabada

**C2 CUMPLEAÑOS entregado** en su carpeta `1TfFCqNfQw0ucTwqvJD8iqft7Y__voRUw`.
Los dos cambios de TEXTO que pedía el cliente —sacar «en septiembre» y la
píldora «¡VEN POR TU CAFÉ DE REGALO!»— **ya estaban aplicados desde la ronda 7**;
se verificó sobre la pieza entregada antes de tocar nada.

⭐ **La lección de la sesión: cuando el cliente señala UNA foto como el look
bueno, se EDITA esa foto, no se recrea la escena.** Primero se generó una escena
nueva (una mano, vaso liso) y se le estampó el logotipo con
`between-logo-vaso.py`, que es lo que manda el manual desde la ronda 4. Eli lo
devolvió: «el logo se ve mal montado, utiliza la referencia, solo era que la tapa
no estuviera y fuera cappucino». Tenía razón: **la referencia ya traía el
logotipo REAL impreso, con su perspectiva sobre el cilindro**, y recrear la
escena obligaba a estampar — un sello plano sobre un cilindro se nota. La regla
del estampado sigue viva para cuando hay que generar de cero; **pero si existe
una foto con el vaso ya marcado, se edita esa.**

**Y la G2 cambió de fondo otra vez.** En la ronda 7 se cumplió «distinta a G1»
generando el muro vegetal desenfocado; pero la G1 de hoy pasó a ser el muro
vegetal con globos, así que volvían a chocar. Entra `bar-servicio.jpg`.

**⛔ La S2 y la S3 NO se tomaron, y el motivo es de acceso, no de tiempo.**
Eli pidió aplicar «los comentarios en rojo del cliente, lo que no esté tachado».
**Ese formato no se puede leer desde acá:**

- La grilla `BETWEEN _ GRILLA SEPTIEMBRE 2026.xlsx` (`1wNF6qLil9qMFCGgXPlVqHBQcabfmCWWY`)
  es de Sebastián Serrano y pesa **68 MB**. El token del estudio tiene alcance
  `drive.file`: **no puede leer un archivo que no subió** (404).
- El conector de Drive sí lo lee, pero devuelve **texto plano**: se pierden el
  color de fuente y el tachado, que es justamente lo que separa lo pendiente de
  lo ya hecho. Bajarlo en base64 por el conector son ~91 MB, inviable.
- **No existe versión nativa de Google Sheets** de la grilla de septiembre
  (comprobado: sólo hay nativas hasta marzo 2026), así que tampoco sirve la API
  de Sheets, que sí tendría permiso.

⚠️ **Aplicar la ronda a ciegas era el riesgo caro**: la fila de comentarios
mezcla lo pendiente con lo resuelto y lo resuelto va TACHADO. Sin el formato se
rehace trabajo ya aprobado — el error que el manual documenta desde la ronda 4.

**Cómo se destraba, en 10 segundos:** que Eli baje el .xlsx y lo deje en
`raw/hilton/between/`. Con el archivo local, el método ya está escrito en el
manual (`zipfile` sobre `xl/comments1.xml` y `comments2.xml`, más el color y el
tachado de `styles.xml`).

**Lo que sí quedó levantado de la S2/S3**, del documento de Constanza
«BETWEEN S2 septiembre — análisis de cambios en diseño»
(`1PIshvFqHZnLlS3Fz-z6lmkV1O2Aa1mAHwTYzX__alpA`, 02-09 13:04): son **5 piezas**
—FEED G, H, J, L y STORY I— con los comentarios nativos de Scarlette del 31-08
sin aplicar. Ese documento además deja **4 decisiones abiertas para Eli**
(tipografía rígida sí/no en toda la S2, cifras tabulares, unificar interlineado,
y si el «intercambiemos fechas» de L ya está muerto).

⚠️ Y OJO: Scarlette dejó **comentarios NUEVOS el 02-09 a las 17:02 y 17:03**
(«dejaron nuevos comentarios acá», «acá tomar estos nuevos cambios pliss»), o sea
**posteriores** a ese análisis. Hay una ronda más encima de la que el documento
describe.

---

## 2026-09-02 (tarde) · Eli (Windows) — BETWEEN ronda 8: la portada del Cowork, con la terraza real y la jerarquía del texto corregida

**Qué pidió Eli.** Dos cosas en un mensaje: (1) «usa de fondo la terraza de
between, con café en mesa y laptop + celular que sea estilo cowork pero mejor
editada la foto» y (2) «mejoremos cómo se ven los textos, deben verse mejor en
jerarquía visual… ojo crítico con los espacios entre líneas de los textos y
párrafos». Sólo la **C1 (portada)**, y entregada en una carpeta suya.

**⭐⭐ El hallazgo de la sesión: la terraza SÍ es de Between, y estaba probado
dentro de la foto.** El manual venía diciendo que de las 12 tomas de
`espacios/` sólo `HDT_50` estaba identificada, y advertía «varias no son de
Between —la barra de ónix parece de QB— preguntar antes». QB también tiene
terraza, así que la duda era real. No hizo falta preguntar: ampliando
`HDT_52.jpg` a resolución completa aparece un **pizarrón que dice «BƎTWEEN /
COFFEE & BAR / Desde las 17 hrs.»** con la E quebrada del logotipo, y en
`HDT_51.jpg` los portamenús dicen «BƎTWEEN · CAFÉ A $1.000». **Quedan
identificadas las dos como LA TERRAZA** (manual §7), y con ellas el método:
antes de descartar una foto por dudosa, buscarle la marca adentro recortando a
1:1 — una miniatura no muestra un pizarrón de 900 px en una foto de 6719.

**La foto.** Base `HDT_52` (6719×4479), recorte `(200,900)-(3063,4479)` = 4:5
exacto. **El encuadre se eligió midiendo**, no a ojo: se probaron 12 recortes con
las bandas del logo (0,05–0,14) y del texto (0,55–0,92) superpuestas, y en 11 la
mesa caía dentro de la banda del titular. El puesto de trabajo —laptop, taza
blanca lisa, celular, libreta— se generó con Nano Banana Pro **sobre esa misma
foto como referencia** (`scripts/between-portada-terraza.py`): la terraza real
está vacía, es fotografía de arquitectura, y no hay una sola taza en las 12
tomas. Gradada con `neutro`: calidez 30,8 → 20,7, a tono con las otras tres
slides (20,7–21,0).

**⭐⭐⭐ La jerarquía, que era el otro medio pedido y resultó ser un defecto de
sistema.** Medido sobre la entrega anterior, el salto ENTRE niveles era MENOR
que el salto DENTRO del nivel:

    script «Tu oficina por hoy»   alto 124,3   ancho 735 (68 %)
    ↕ 12,0        ← entre niveles
    caps «PUEDE SER»              alto  84,0   ancho 601 (56 %)
    ↕ 29,8        ← dentro del nivel

O sea el ojo agrupaba al revés. Y encima la script —que el kit define como
acompañamiento— salía **más ancha y más alta que el titular al que acompaña**.
Se corrigió con dos props nuevas y OPT-IN en `TitularBetween` /
`PiezaFeedBodegon` (`aireScriptATitulo` y `sizeScript` reenviada), **sin tocar
los tokens**, que habrían re-flujado todo lo aprobado. Ritmo final: 47,0 /
30,2 / 59,0 / 12,0. La caja taupe pasó de 1,16 a 1,24 de interlínea: era el
renglón más apretado de la pieza (ratio 0,24 contra 0,35 del titular).

⛔ **El titular NO se agrandó, y es decisión medida.** 117 da 84 de alto de caja
y 56 % de ancho = la referencia aprobada del manual (85 y 52 %). Cuando dos
elementos compiten se baja el secundario, no se sube el principal.

**Dónde quedó.** Drive, carpeta **`C1 COWORK`** de Eli
(`1GB6NtoG3vy35rPj7bw-j8bc76-Jz8332`, dentro de `BW` de S1 HILTON SEP 2026),
que estaba vacía. **Quedó el CARRUSEL COMPLETO, las 4 piezas**, todas
verificadas byte a byte: la portada nueva (10,53 MB) y las slides 2, 3 y 4 tal
cual se entregaron en la ronda 7 (4,76 · 6,09 · 4,43 MB), sin re-rendir. Se
sube con `scripts/between-subir-c1.py`, que reemplaza en su sitio si se vuelve
a correr. QA limpia y typecheck limpio.

⭐ **`C1` y `C2` son CARRUSELES, no slides.** La carpeta hermana es
`C2 CUMPLEAÑOS BW` (`1TfFCqNfQw0ucTwqvJD8iqft7Y__voRUw`), y hay una `STS`
(`14Z4XnkM9sepmdPV0XjKzoqb1HXMbvIzO`). O sea que Eli está ordenando la S1 **por
carrusel**, y cada carpeta lleva la pieza completa: «súbelas a ese drive, mejor
así tenemos todo». Al entregar una corrección suelta, subir igual las hermanas —
el cliente revisa el carrusel entero, que es como se publica.

**Abierto — tres cosas, en orden:**

1. ⚠️ **El celular queda parcialmente cruzado por la script.** Se hicieron **6
   generaciones** para subirlo a la fila de la taza y el modelo lo devuelve
   siempre al canto cercano de la mesa. Subir el encuadre lo despejaría, pero
   saca la lona oscura de la sombrilla de detrás del logo — y el logo es
   elemento de marca con QA (hoy mide luma 123,3 contra 159,5 de la portada
   anterior, o sea que quedó MEJOR). Se priorizó el logo. **Falta que Eli diga
   si lo da por bueno o si prefiere sacrificar el fondo del logo.**
2. ⚠️ **C1 y C2 ahora muestran las dos una laptop con un café.** C1 es el plano
   general de la terraza y C2 el bodegón a la altura del asiento, así que se
   leen como progresión —dónde estás / tu mesa— y la paleta verde amarra. Pero
   es repetición de sujeto en un carrusel que el cliente ya devolvió por
   cohesión. **Es consecuencia directa de lo que pidió Eli**; si le hace ruido,
   lo que cambia es la C2, no la portada.
3. ⚠️ **La misma inversión de jerarquía está en las slides 2, 3 y 4** (C2: 8,6
   contra ~35,5; C3: 20,2; C4: 8,2). Es una línea por slide, pero re-flujarlas
   mueve piezas que el cliente ya vio. **Falta el OK de Eli.**

## 2026-09-02 (cierre) · Eli (Windows) — BETWEEN ronda 7: la S1 completa, el To Go desbloqueado y las cifras tabulares resueltas de verdad

**Qué se hizo:** Llegó la **RONDA 7 del cliente** y se aplicó entera a lo que se
podía. Se entregaron **12 piezas**: la S1 completa (Cowork 1-4, Cumpleaños 1-2 y
las dos stories) y el **carrusel To Go de la S3, completo por primera vez**.
La **FEED G quedó APROBADA** por el cliente.

· **El Cowork, rehecho por cohesión.** El reclamo por WhatsApp era doble: la
  portada «no la usaría por temas de calidad y porque mostramos a esas personas»
  y «cambiaría las fotos para que tenga más cohesión». Portada nueva: el MISMO
  rincón del muro vegetal en el fotograma donde las dos personas ya salieron de
  cuadro (`IMG_1148-3`, elegido MIDIENDO dominancia de verde sobre los 91
  fotogramas: +9,2 contra +3 del resto). Slide 2 rehecha: era un bodegón de
  ESTUDIO sobre un muro verde INVENTADO —«la del medio que hace ruido», y encima
  el fondo falso imitaba el de la portada—; ahora el muro es el real, entrando
  por referencia y muy desenfocado. Slide 3 regradada a `neutro`: venía 8 puntos
  de calidez más fría (+12,4 contra +21 de las otras) y era la que rompía el
  tono. Y el texto de la portada cambió por pedido de Javier Meza: «Espacio para
  trabajar, WiFi y atención a la mesa».
· ⛔ **La slide 4 NO se regradó, y es decisión medida.** `neutro` le sube la
  luminancia de 77 a 95 y le levanta los negros: el tapete deja de ser negro y el
  latte pierde fuerza. Se probó, se miró y se descartó. El cliente tampoco la
  objetó.
· **Cumpleaños:** fuera «en septiembre» y fuera la píldora «¡Ven por tu café de
  regalo!» (el cliente se desdijo de su propia ronda 4), y la G2 con **fondo
  nuevo**, porque las dos gráficas usaban el mismo archivo con otro recorte.
· **Stories:** se eliminó la CTA «Pasa por Between y llévalo contigo» —el cliente
  borró su propia CTA del brief— y la promo pasó a «Café + Dulce To Go · desde
  $3.790». La story del cumpleaños arrastra los textos del feed por la regla de
  una sola voz.
· ⭐ **El sándwich del To Go, recuperado de raíz.** `togo-sandwich-45.jpg` nunca
  se versionó y sólo existía en el Mac de Valeria, así que la slide 2 no se podía
  rendir acá. La sesión COMPLETA del 25-jul-2025 está en el Drive del cliente
  (carpeta `1YQ_28BQpnBhTPNKnWXZmmaC6Bvr0BodD`, 353 archivos). Se bajaron las
  **353 miniaturas** para elegir sin traer 3,5 GB y el sándwich salió del
  fotograma **-248**: el único con el relleno de palta a la vista («rico y
  contundente», que es el copy) y el logotipo del vaso entero.

**Dónde quedó:**
· Drive, **carpeta única y fechada**, por decisión de Eli («solo deja una carpeta
  con cambios de fecha de 2 de sep»):
  `9. SEPTIEMBRE / CAMBIOS 02-09 BETWEEN v3 (tabular corregida - USAR ESTA)`
  → `1xLp2vSDej0xc6UnHS59RKUN8oM7uSa8H`. Las 12 piezas, **verificadas byte a
  byte**. Las v1 y v2 quedaron renombradas con `_` adelante y «NO USAR».
· ⚠️ **Las carpetas de semana quedaron INTACTAS y eso NO es un olvido.** El token
  del estudio tiene alcance `drive.file`: no puede sobreescribir las 8 piezas que
  Eli subió A MANO el 01-09, y el conector de Drive tampoco puede moverlas («The
  caller does not have permission»). Por eso la entrega va aparte y las viejas
  siguen en `S1/BW` con sus comentarios y sus enlaces.
· ⭐ **De acá en adelante sí se reemplaza en su sitio.** Las 12 las subió nuestro
  token, así que `scripts/between-subir-r7.py --actualizar "<nombre>"` cambia el
  contenido conservando enlace y comentarios. Es la primera vez que la cuenta
  queda en ese estado. El manifiesto con los fileId vive en
  `out/entrega-r7/_subidas*.json`.
· Código: `BetweenSeptiembre.tsx`, `BetweenSistema.tsx`, `BetweenRecursos.tsx`.
  Scripts nuevos: `between-slide2-magnific.py`, `between-cumple2-magnific.py`,
  `between-subir-r7.py`. Assets nuevos versionados con excepción en `.gitignore`
  (7 archivos: las 5 fotos gradadas y las 2 generaciones de Magnific).
· **QA 12/12 limpias** con `between-qa.py`, typecheck limpio.

**Qué sigue:** El **carrusel H (9-sep)** y el **estático J (11-sep)**. No están
bloqueados por archivos que falten: lo que pide el cliente EXIGE generar
imágenes nuevas — fuera la taza Kimbo de la G1 de H, la G4 con el plato más vacío
y cenital «como los 2 anteriores», y las dos tazas de J con arte latte y una que
se vea usada. La clave de Magnific funciona (`scripts/magnific.py check`) y los
dos scripts de esta ronda sirven de plantilla.

**Abierto:**
1. **Borrar las 8 viejas de la S1** para poder mover las nuevas a su sitio con
   `addParents/removeParents` (de las nuevas sí somos dueños).
2. **Desajuste de fechas en 3 stories.** La grilla rotó las tres primeras y los
   nombres de archivo quedaron con las fechas viejas: Promo To Go dice 01-09 y la
   grilla 03-09; Café de regalo dice 03-09 y la grilla 04-09; Según mis cálculos
   dice 04-09 y la grilla 02-09. No se renombraron a propósito: el portal levanta
   por nombre y renombrar DUPLICA en vez de reemplazar.
3. **¿La slide 4 del Cowork lleva logo?** Sin respuesta desde el 01-09.
4. ⭐ **El brownie de la slide 4 del To Go tiene candidato.** Los fotogramas
   **263–269** de la sesión 25-jul traen un dulce de chocolate CON EL VASO
   VIGENTE — el pendiente estaba trabado porque la única foto de brownie era del
   vaso antiguo prohibido. Es un muffin, no un brownie («pongamos un brownie
   aunque sea», dijo Scarlette): falta que Eli decida si sirve.
5. **Faltan 16 de las 31 fotos en este PC** (`public/assets` no viaja completo).
   Es el techo real de lo que se puede rendir en Windows.
6. La **Semana 1 ya no está congelada**: la ronda 7 trajo los cambios que se
   estaban esperando.

---

### Las cifras tabulares: resueltas en la 5.ª pasada (y por qué costó tanto)

Eli lo pidió **tres veces** y se rechazaron **cuatro implementaciones**. El error
nunca fue la idea; fueron dos cosas de implementación y una de diagnóstico.

**1. El ancho de la caja estaba mal.** Se usaba el avance del «0» (0,614 em), el
dígito más gordo, así que el «1» quedaba centrado en una caja que le sobraba por
los dos lados y «10:00» se leía «1 0:00». Lo correcto es el **ancho MEDIO de los
diez dígitos DEL PESO que se está pintando** — y el peso importa mucho: el «1» va
de 518/1000 en ExtraBold a 450 en Medium y 375 en la variable. Se eligió
rindiendo cuatro tratamientos con la fuente real, no de oído.

**2. Faltaba compensar los bordes del grupo.** Con el ancho ya bien puesto
quedaba un espacio doble entre la «a» y el «10»: el hueco de la caja del PRIMER
dígito se suma al espacio de la palabra anterior. Ahora `cifrasTabulares` agrupa
los dígitos consecutivos y les pone un **margen negativo exacto en los dos
bordes**, calculado con el avance real de cada dígito
(`ANCHOS_DIGITO_POR_PESO`). El hueco se reparte sólo por DENTRO del grupo, donde
son ~25 milésimas de em (~1 px a cuerpo 40) y se leen como espaciado normal.

**3. Y el diagnóstico que se me pasó dos veces: el desorden no eran los dígitos,
era la ESCALERA.** Para que la caja de la promo no cruzara el rol de canela había
partido el texto en dos cajas, y quedaron **tres cajas de tres anchos distintos y
las dos primeras en el mismo peso** — sin jerarquía. Eli: «se ve todo desordenado
en los textos y no se ve pulcro… cuidado que los textos se vean bien igual en
jerarquía». Se volvió a **dos cajas con una sola línea fuerte**, y el ancho se
resuelve con la prop nueva **`igualarAncho`** de `PilaEsquina` (todas las cajas al
ancho de la más ancha), no partiendo el texto.

⛔ **El atajo que NO sirve:** sacar la tabular de las líneas livianas. Se probó y
Eli lo devolvió señalando la story del 3-sep. Además el brief de esa pieza APILA
los números en dos líneas, o sea que ahí la tabular tiene que estar. Va en toda
la grilla. Todo escrito en `clients/hilton/CLAUDE.md § Las cifras tabulares`.

### Cinco defectos de margen que venían de antes, cerrados

`between-qa.py` marcó tinta fuera de los 84 px de margen en `ToGo1`, `ToGo3`,
`ToGo4`, `Cumple1` y `Cumple2`. Cuatro tenían la MISMA causa: la cola del «¿» de
Brushwell **sobresale del ancho de avance** con el que el titular se autoescala,
así que la caja cabía y la tinta no. Aparece en toda pieza cuya script abre con
«¿». Se componen en la columna (810) en vez del margen (912) — y para poder
apretarlo en las stories hubo que **agregarle la prop `columnaTitular` a
`PiezaStoryBetween`**, que no la tenía. El quinto era el globo doodle de
`Cumple2`, a 82 px del canto: se corrió 12 px.

### Dos trampas de scripts, cerradas

· `between-entrega.py` hacía `rmtree` de la carpeta de salida y **se llevaba
  `_subidas.json`**, el manifiesto con los fileId de Drive — sin él se pierde la
  capacidad de reemplazar en su sitio. Pasó hoy y hubo que reconstruirlo a mano.
  Ahora el manifiesto se preserva.
· El mismo script tenía la semana **quemada en `'S1'`** en la comprobación de ppp
  y reventó en cuanto entraron piezas de S3.

### Y una de método

**La ronda nueva se detecta por DIFF, no leyendo la grilla.** Los comentarios
nuevos se **prependen** sobre los viejos en la misma celda, así que sin comparar
contra la copia anterior del xlsx se confunde ronda nueva con ronda vieja — y el
bloque viejo puede estar CONTRADICHO por el nuevo (en E15 el cliente pedía en la
ronda 4 agregar «¡Ven por tu café de regalo!» y en la 7 pidió eliminarlo). El
diff también cazó que **dos comentarios nativos nuevos sólo AVISABAN** («dejaron
nuevos comentarios acá»), que la grilla había **ROTADO** las tres primeras
stories, y que **media ronda ya estaba aplicada** desde la ronda 5: lo que el
cliente marcó en el To Go era un render viejo que nunca se re-entregó.

---

## 2026-09-02 — Eli (Windows)

**Qué se hizo:** Arrancó la **ronda 6 de la SEMANA 2** de Between, que son los
comentarios nativos de Scarlette del 31-08 (G15, H15, J15, L15, I15) que seguían
sin aplicar. Se cerraron **2 de 11** piezas y se entregaron a Drive.

· **FEED G (7-sep) APROBADA por Eli.** Foto nueva. El fondo de la r4 era una
  terraza tropical y Scarlette tenía razón, pero mi primera corrección perdió lo
  bueno: quedó una sala vacía y fría. Eli lo marcó —«en el post más se parece la
  ronda 4»— y la versión final es la síntesis: el plano corto y la calidez de la
  r4 con el espacio real del local MUY desenfocado detrás, transferido por
  REFERENCIA desde `raw/hilton/between/espacios/`. Gradada con perfil `neutro`
  (calidez 54,7 → 21,9). Tipografía rígida (fuera Brushwell), comillas y punto
  del brief, bloque abajo.
· **STORY I (9-sep)** rendida y entregada con los textos del brief: el
  «¿CUÁL TOMARÍAS?» que faltaba entero, las 4 opciones literales con «algo
  salado» recuperado, y la encuesta en 2×2 para no invadir la zona segura.
· El **llavero del estudio** quedó funcionando en este PC: `abrir`, `estado`,
  `logins` y `magnific.py check` (✓ VÁLIDA). Los dos scripts nuevos reventaban
  con UnicodeEncodeError al imprimir el «✓» DESPUÉS de haber hecho el trabajo —
  arreglados, van 9 scripts con el fix de cp1252.

**Dónde quedó:**
· Entregadas en Drive **S2 HILTON SEP 2026 / BW**
  (`1Yh2Puq1ZEmbM2HaoTh-LUydKwtZRmpn1`): `BW FEED 07-09 Humor cafecito.png` y
  `BW ST 09-09 Romper en caso de antojo.png`. Verificadas byte a byte.
  ⚠️ Quedan a nombre de **valeria@copywriters.cl**, porque el token del llavero
  es el de la cuenta del estudio, no el de Eli.
· Copia de trabajo para Eli en `COPYLAB-ENTREGAS\BETWEEN-S2-SEP2026` dentro de su
  carpeta de usuario — fuera de OneDrive, Escritorio, Documentos y Descargas, por
  pedido suyo (esos tres se vacían y el estudio se rompe en silencio).
· Código: `BetweenSeptiembre.tsx`, `BetweenSistema.tsx`, `BetweenRecursos.tsx`,
  `scripts/between-qa.py`. Fondo nuevo versionado con excepción en `.gitignore`:
  `ia-sept/humor-cafecito-4.png` (+ el descarte `-3` para documentar por qué).
· Material recuperado de Drive a `raw/hilton/between/desayunos-ago2026/` (28
  tomas) y `raw/hilton/between/togo-25jul2025/` (el original -257 de 5760 px).
  **`raw/` no viaja en git**: quien retome tiene que volver a bajarlo de
  `GRILLA IA BETWEEN`.
· Página de revisión con antes/después:
  https://claude.ai/code/artifact/6c7b1871-1a2c-47b0-8813-c8eca17294a0

**Qué sigue:** El **carrusel L (To Go, 14-sep)**, que es el más avanzado: falta
regradar las 4 slides con `neutro` —es el «se ven quemadas y con un filtro medio
raro» de Scarlette— y recortar el sándwich desde el original de 5760 px que ya
está bajado. Después el **carrusel H (9-sep)**, que necesita 2 imágenes
generadas, y la **J (11-sep)**, que hay que rehacer completa.

**Abierto:**
1. **La STORY I ya está entregada pero SIN visto bueno de Eli.** Scarlette pidió
   «más protagonismo la caja» y el producto se ve chico dentro de un nicho muy
   vacío. Si se regenera, el archivo se reemplaza con `--actualizar` y conserva
   el enlace que el cliente ya tiene.
2. **El croissant de jamón y queso de H3 NO EXISTE en el banco.** Las 28 tomas de
   `BETWEEN DESAYUNOS AGO 2026` son huevos, tostadas y palta — ni un croissant. Y
   vienen en **1620×1080**, o sea que no alcanzan los 2250 px de entrega. Falta
   saber si existen los originales grandes de esa sesión.
3. **La J necesita DOS manos**, porque Scarlette pide que se vea la interacción de
   las personas «aunque sea sus manos» — y dos manos es justo lo que hubo que
   descartar hoy por anatomía. Se le preguntó a Eli si tiene foto real; sin
   respuesta todavía.
4. **El brownie de la slide 4 de L**: Scarlette lo pide, y la única foto de
   brownie del banco es de las del **vaso antiguo**, que está prohibido.
5. **La SEMANA 1 está CONGELADA** por decisión de Eli: vienen cambios nuevos y le
   avisan de nuevo. NO se reemplaza `BW ST 01-09` en Drive, aunque su defecto de
   margen ya esté corregido en el código.
6. Sigue sin respuesta desde el 01-09: **¿la slide 4 lleva logo?**

---

### Los tres bugs de sistema que salieron hoy

**1. `PilaEsquina` nunca aplicó su margen.** Decía `[lado]: BETWEEN.bloque.margenX`
y `lado` vale «izquierda» o «derecha»: la clave calculada salía `izquierda: 84`,
que NO es una propiedad CSS. React la ignoraba y la caja quedaba pegada al borde
del lienzo en x=0, **cortada**. Lo cazó el QA en `BW ST 01-09`, que ya estaba
entregada, con la tinta a 22 px del canto contra los 84 de margen. Afecta a toda
pieza con `PilaEsquina` — las slides 2, 3 y 4 del carrusel To Go se arreglan
solas al rendirlas.

**2. ⛔ Las cifras tabulares NO van en texto corrido.** Eli pidió el 01-09 que los
precios se vieran «opentype tabular, como en Adobe Illustrator». Se construyó a
mano —Raleway **no trae la función `tnum`**, verificado en la tabla GSUB/GPOS de
los 5 pesos instalados y de la variable, así que el CSS que había era decorativo
y el «Tabular Lining» de Illustrator tampoco tendría efecto— y **Eli lo rechazó
al verlo rendido**: «los textos y números vuelven a verse extraños, en la
anterior estaba mejor». Tenía razón. Las tabulares existen para que los números
**cuadren en COLUMNA**; acá van DENTRO de una frase («desde $3.790», «08:00 a
10:00 hrs») y forzar cada dígito al ancho del más gordo dejaba al «1» flotando
con un hueco a cada lado: el «10:00» se leía como una palabra partida. En texto
corrido lo correcto son las PROPORCIONALES, que es lo que Raleway trae de
fábrica. Se retiró de los 8 sitios donde se había aplicado; el helper
`cifrasTabulares` queda en `BetweenSistema.tsx` **documentado y SIN USO**, para
el día en que una pieza apile precios en filas.
Los anchos medidos siguen siendo ciertos (em de 1000): 0=614 · 1=518 · 2=580 ·
3=569 · 4=578 · 5=558 · 6=608 · 7=576 · 8=607 · 9=589. El «1» es 18,5 % más
angosto que el «0».

**3. El QA confundía el logotipo con el titular** — y lo rompí dos veces más al
arreglarlo. El lockup se detecta como UNA banda de 118 px, más alta que una línea
de titular (~85), así que `max(alto)` elegía el logo y reportaba «el titular
ocupa 24 % del ancho» —los 263 px del logo— en piezas con el titular al 73 %.
Filtrar por la zona del lockup falló primero porque mezclé las zonas de los dos
formatos (las del story caen donde el feed pone su texto, y descartaba las tres
líneas correctas de «Cowork 2»), y después porque **«Emergencia» no lleva logo**
—el vaso ya trae el logotipo impreso, regla 8— y su titular ocupa legítimamente
esa franja. Ahora mide **la banda MÁS ANCHA**, que no depende de dónde esté el
logo y es lo que la regla quiere saber.

### Y una de método
Las manos se revisan **con zoom, no a ojo**. Se descartaron DOS versiones de la
G: en una la mano de arriba no resolvía —un dígito con uña, otro parcial al borde
y entre ellos una masa lisa sin nudillos—. Se bajó el riesgo a **una sola mano**,
y la duda que quedaba (dos uñas juntas al lado del asa) se resolvió con zoom 4×:
era un dedo más la sombra del asa.

---

## 2026-09-01 (cierre) · Eli (Windows) — BETWEEN ronda 6: la foto de la slide 2, la gradación neutra, y el brief de la slide 4 que estaba mal anotado

> ⚠️ **Tercera sesión del día sobre el mismo repo.** Mientras ésta trabajaba, otra
> commiteó `f22209e`. No se perdió nada —se verificó archivo por archivo— pero ya
> van dos días seguidos. **Una sola sesión por repo.**

**Qué pidió Eli.** «Mejoremos el carrusel de la S1 según lo que dice Scarlett y lo
que describe el brief. Mantén los textos, están correctos. Pero las fotografías del
fondo no corresponden.»

**El defecto era peor de lo que se veía.** Las slides 1 y 2 usaban **el mismo muro
verde**, y la slide 2 decía «al menos que sea con buen café / encuentra tu mesa»
sobre una foto **sin mesa, sin café y sin PC**. Es literal el comentario C15 de
Scarlette del 31-08: «acá estamos hablando de café como tal, yo cambiaria la imagen
donde se vea una mesa con un pc y un café».

**La foto ya existía.** `raw/hilton/between/ediciones-ia-eli/magnific_agrega-una-laptop-en-la-m_iAi90W63uK.png`
— mesa de madera, laptop, vaso con el logo BETWEEN, muro verde desenfocado atrás.
**No se generó nada con IA**: la regla del manual es agotar el banco antes de
generar, y el banco la tenía. Recortada 4:5 con `--top 0.20` (el follaje queda
ARRIBA, donde se apoya el bloque de texto).

**La gradación: perfil `neutro`, sin tocar el ADN.** El otro reclamo de la ronda 5
—«eliminar el filtro de color cálido que tiene el carrusel completo»— seguía
pendiente. En vez de mover el objetivo por defecto, que está MEDIDO sobre las
piezas aprobadas de Eli y habría re-flujado todo lo entregado, se abrió un segundo
perfil en `between-gradar.py`:

| | `eli` | `neutro` |
|---|---|---|
| calidez (R−B) | 50 | **20** |
| p95 (altas) | 227 | **210** |
| lum · p05 | 118 · 24 | iguales |

La prueba de que +20 no es frío: las fotos crudas del 2.º piso vienen en **+27**, o
sea el perfil las deja **bajo su propio natural**. Saca filtro, no lo suma.

**Qué se movió y qué no.**

| | |
|---|---|
| slide 1 | sólo regradada (+33,2 → +21,4). Diagramación intacta |
| slide 2 | foto nueva. **Texto sin tocar** — la tinta mide 687/721/601 px, igual que la r6 |
| slide 3 | **SIN TOCAR**, idéntica píxel a píxel (delta 0). Ya venía en +12,4 |

QA **4/4** limpias · `tsc` limpio · entregadas a `Escritorio\S1 BETWEEN` (ahí seguían
las de las 15:20, previas a la corrección de jerarquía de la r6).

⚠️ El archivo de la slide 2 **sigue llamándose «Cowork 2 winter garden»** a
propósito: el portal levanta por nombre y renombrarlo crearía un duplicado.

---

### ⭐ La slide 4: el brief pedía otra escena

Eli pasó el brief textual, y no coincidía con lo anotado. El manual, el comentario
del código y el prompt de Magnific decían **«una trabajadora sin rostro preparando
café»** — un pedido dicho al pasar, que mandaba a generar **el bar**. El brief dice:

> «Persona trabajando mientras un colaborador deja un café o plato sobre la mesa.
> El usuario continúa trabajando sin tener que levantarse.»

Son **dos personas y una MESA**, no un mesón. Dicen cosas opuestas: el bar cuenta
que el café *se va a buscar*; el brief vende el **servicio a la mesa**. Y el bar
repite el escenario de la portada.

**La lección, escrita en el manual y en la memoria:** un criterio dicho al pasar
manda sobre el **CÓMO** (tipografía, logo, color, jerarquía), **nunca sobre el QUÉ**
la pieza tiene que mostrar. Si chocan, manda el brief.

Los textos de la slide **ya eran literales del brief**: no se tocó ninguno.

**El banco está agotado, y quedó demostrado:** `espacios/` son 12 tomas de
arquitectura **vacía**; de los 91 fotogramas del 2.º piso, los que tienen gente son
huéspedes **con la cara reconocible**, nadie sirviendo, y son del **1.er piso**. Ahí
sí se justifica generar.

`scripts/between-slide4-magnific.py` **reescrito entero**: escena nueva,
referencias del 2.º piso real, y los tres reclamos de la ronda 4 convertidos en
restricciones (cero caras por construcción · trabajo y no desayuno · las manos
contadas). Más un QA de 5 puntos y la receta de gradado/render/entrega.

---

### ⛔ Magnific: no se pudo, y hay que saber por qué

- `~/.magnific_key` tenía **la contraseña de la cuenta** (`DISEÑO2025-VIDEOS`, 17
  caracteres), no una clave de API. Verificado con `magnific.py check`, que
  **no gasta créditos**: HTTP 401.
- **Magnific muestra la clave UNA SOLA VEZ.** En el menú de la fila sólo hay
  «Editar clave API», «Copiar secreto del webhook» y «Eliminar clave API» — no hay
  forma de volver a verla. Para recuperarla hay que **borrar `claudecw` y crearla
  de nuevo**, copiándola en el momento. El plan está en el tope de claves, así que
  primero se borra.
- Créditos NO son el problema: las 3 claves están activas con **1,8 M disponibles**.
- El MCP `magnific` **ya está registrado** en `~/.claude.json`
  (`http · https://mcp.magnific.com`) pero **sin autorizar**. Se autoriza con `/mcp`
  y después hay que abrir **chat nuevo**.
- ⚠️ El binario `claude` **no existe en este PC** (se usa la extensión de VS Code),
  así que `claude mcp add` no corre. Hay que editar la config a mano.

Queda listo en el Escritorio, carpeta **`SLIDE 4 - para Magnific`**: el `PROMPT.txt`,
las 3 referencias renombradas y un `LEEME.txt` con el QA de 5 puntos. Se genera a
mano en la web y yo hago recorte, gradado, render y QA.

**⭐ Dirección final de Eli:** «una persona dejando el capuccino, que no se vea el
rostro». O sea **UNA sola persona**, no las dos del brief. El prompt se ajustó a
eso, y de paso es más seguro: cada mano de más es una posibilidad de error
anatómico, y «hay una mano de más» ya fue un rechazo.

**Se buscó la mano en el banco y NO estaba.** Revisadas las 42 ediciones con IA de
Eli: las que tienen manos sin rostro son **todas de la serie To Go** —sostienen el
vaso de papel o una bolsa, en el mesón— y ninguna deja una taza de cappuccino en
una mesa. Montar una mano de otra foto es justo como se produce el «hay una mano
de más», así que **no se hizo**.

**⭐ Y NO hizo falta: Eli mandó fotos propias.** Dejó tres en `out/hilton/`
(`between-39/40/42.jpg`, 1500×2250, del bar de Between) y con eso la slide se
resolvió **sin generar nada**. Magnific quedó pendiente para otra cosa, no para
esto.

---

### ⭐ La slide 4, resuelta con foto real de Eli

La dirección fue: «una persona dejando el capuccino, que no se vea el rostro».
De las tres que mandó se eligió **`between-42.jpg`** — dos manos presentando la
taza terminada, con el corazón en el latte, sin ninguna cara.

**Por qué esa y no las otras dos:** la 39 y la 40 son el momento de **PREPARAR**
el café en la máquina, o sea el bar — y el bar cuenta que el café se va a buscar.
La 42 es el de **ENTREGARLO**, que es exactamente lo que dice el titular.

Verificado con zoom, no a ojo: **taza blanca limpia, sin raya ni logotipo** (regla
KIMBO), **dos manos con anatomía correcta y ninguna suelta** — que fue el rechazo
textual de la ronda 4.

**⚠️ NO se gradó, y es a propósito.** Venía en **calidez +8,2**, más FRÍA que el
objetivo del perfil `neutro` (+20). Pasarla por el gradador la habría **calentado**
—justo lo contrario de lo que reclamó el cliente— y le habría subido la luminancia
de 79 a 118, lavando el ambiente oscuro que es lo que la hace buena. Sólo recorte
4:5 y llevada a 2250 px. La ampliación de 1,5× se verificó al 100 %: la crema y el
borde de la taza quedan limpios.

**El recorte va pegado ARRIBA, y eso también se decidió rindiendo las dos:** con el
recorte abajo la taza sube y **la caja taupe le tapa el corazón del latte**. Pegado
arriba la taza cae al ~67 % del alto, el texto se apoya en el tapete oscuro y el
corazón queda libre.

Es la **única slide oscura** del carrusel. No es descuido: cierra la secuencia
—el lugar, tu mesa, los espacios, el café que te llega— y el cambio de clave se lee
como remate. Si algún día se quiere pareja con las otras tres, se sube la luz; se
dejó así con el visto bueno de Eli.

**Quedó `servicio-mesa.jpg` en el repo** (la mesa del 2.º piso con el café servido)
como el paso intermedio del día. No la usa ninguna pieza, pero es una foto válida
del 2.º piso por si sirve.

**APROBADO por Eli.**

---

### El estudio en Windows

- **Séptimo script caído por cp1252.** Windows lee y escribe la consola en cp1252 y
  revienta con «✅», «→» o una «Á» — a veces **después** de haber hecho el trabajo,
  así que parece que falló y estaba listo. Arreglados hoy: `between-qa.py`,
  `hoja-contacto.py`, `verificar-fuentes.py` (reventaba dos veces: al leer la ficha
  y al imprimir el error) y `qa/motor.py`.
  **Quedan ~25 lugares más** en `scripts/` que abren archivos sin declarar
  codificación, casi todos de marcas de Paulina y Coni. **Eli tiene que decidir si
  se hace el barrido completo** — es un cambio grande.
- **`pyyaml` instalado**: faltaba y el motor de QA moría antes de leer una regla.
- **Hilton no tiene `reglas.yaml`** — el motor lo dice claro ahora. Es la única
  marca de Eli sin QA por programa. Hay dos reglas medidas listas para entrar (la
  columna y la gradación), **pendiente que Eli las firme**.
- **Hilton tampoco tiene `marca.json`**, y por eso `verificar-fuentes.py` ni siquiera
  la revisa. Sus fuentes funcionan igual (Brushwell y Raleway están en el repo).
- Las **14 tipografías sin resolver NO son de Hilton**: son de Casablanca y Cava
  (Paulina) y de MyZoo y Selfie (Coni). Vale avisarles: hasta que las activen, sus
  piezas salen con la fuente equivocada sin que nadie lo note — que es exactamente
  lo que pasó con Brushwell y costó 27 piezas.

---

### Qué sigue, en orden

1. **Subir a Drive arrastrando** las **4** Cowork a `C1 COWORK` y las 2 Cumpleaños
   a `C2 CUMPLEAÑOS BW`. Sin token. Es lo primero.
2. **Sacar del medio las de la ronda 4** en `BW` — pedírselo a Valeria.
3. **La clave de Magnific** — ya NO bloquea la S1, pero sigue pendiente para lo que
   venga: borrar `claudecw`, recrearla y copiarla en el acto (Magnific la muestra
   una sola vez), o autorizar el MCP con `/mcp` + chat nuevo.
4. **Cambiar la contraseña** `DISEÑO2025-VIDEOS`: estaba en texto plano y quedó en
   el historial de la conversación. También regenerar el **secreto del webhook** de
   `claudecw`, que se pegó en el chat.
5. `credentials/token.json` — para las correcciones futuras, no para esta entrega.

**Abierto.**

1. ~~Slide 4 sin foto~~ **RESUELTA y aprobada.** El carrusel está completo, 4/4,
   con foto real de Eli. No quedó nada pendiente de esta pieza.
2. **¿La slide 4 lleva logo?** Sigue sin respuesta desde ayer. La regla escrita dice
   que en carrusel el logo va sólo en la portada, y se respetó.
3. **Barrido de codificación** (~25 lugares) — esperando el sí de Eli.
4. **`reglas.yaml` de Hilton** — esperando que Eli firme las reglas.
5. Sin cambios: el **listado del cumpleaños de CINCO ítems** contra los cuatro de
   nuestra pieza, y el **Café Bombón** esperando al cliente.

**Páginas de revisión.** Ronda 6 con antes/después:
`https://claude.ai/code/artifact/2a18c52f-d2c3-49d5-acc4-5a526046b2b6` ·
Paso a paso de lo que le toca a Eli:
`https://claude.ai/code/artifact/44ff22ef-5c0e-437a-93c1-2e360cb48331`

---

## 2026-09-01 (noche) · Eli (Windows) — BETWEEN: la COLUMNA como medida de composición, la slide 4 de vuelta, y dos bugs del doctor

> ⚠️ Esta entrada funde las **dos** que quedaron escritas esta noche: hubo otra vez
> dos sesiones sobre el mismo repo (la otra commiteó en `e14047e`, 16:32). Se
> conserva todo lo de ambas. **Conviene una sola sesión por repo.**

**Qué se hizo.** Segunda pasada del día sobre la S1. Eli marcó el carrusel Cowork
ya entregado: **«los textos están muy grandes y desproporcionados, mejorar la
jerarquía visual y el espacio entre textos»**. Se midió sobre los PNG (no a ojo) y
apareció un defecto de sistema, no de la pieza: `TitularBetween` y `PanelTaupe`
achicaban el texto **hasta caber en el margen** (912 px = 84,4 %), que está por
encima del `anchoMax: 0.8` que declara el propio kit. Resultado: cada slide se
achicaba por su cuenta y el carrusel salió con **tres cuerpos de titular distintos**
(117 · 99 · 88) — al deslizar, el titular cambiaba de tamaño.

| | slide 1 | slide 2 | slide 3 | **ref. aprobada** |
|---|---|---|---|---|
| ancho del titular | 55 % | **84 %** | **84 %** | **52 %** |
| cuerpo real | 117 | **99** | **88** | **117** |
| caja taupe | 50 % | 77 % | **84 %** | **55 %** |

**La regla que quedó escrita** (`clients/hilton/CLAUDE.md § LA COLUMNA`):

- El **margen (84 px) es un LÍMITE**; la **columna (`BETWEEN.bloque.columna` = 810 px
  = 75 %) es la MEDIDA** en la que se compone.
- En un carrusel, **las slides interiores comparten UN cuerpo de titular**. La
  portada puede ser mayor — es la única con Brushwell.
- **La caja taupe va más angosta que el titular** (670 contra 810): dos bandas del
  mismo ancho se leen como bloque; escalonadas, se leen como jerarquía.
- **Todo corte de línea va escrito a mano**, y el texto sigue siendo literal del
  brief: se cambia dónde cae el salto, nunca la palabra.

**⚠️ Es OPT-IN a propósito.** Cambiar el valor por defecto re-flujaba piezas ya
aprobadas (3 de las 4 entregadas de la S1 se movían entre 4,5 % y 5,3 % de sus
píxeles). Así que `PiezaFeedBodegon` sigue trayendo el margen y la columna se pasa
a mano (`columna` / `columnaCaja` / `aireTituloACaja`). **Comprobado:** re-rendidas
las 4 piezas aprobadas en `out/_verif/`, salen **idénticas píxel a píxel** a las
entregadas. `npx tsc --noEmit` limpio.

**La slide 4 volvió al carrusel.** La versión que rechazó el cliente era la única
que no usaba `PiezaFeedBodegon` —por eso no se parecía a ninguna—; ahora comparte
gramática, va **anclada arriba** y sus tres textos son literales del brief. Se
agregó el **velo** que pidió Eli: la transparencia multiplicada de Illustrator,
capa aparte al **10 %**, sobre la foto y **debajo** del logo y del texto.
**No es subir `oscurecer`** — eso el manual lo prohíbe («cuando un texto no se lee,
la solución es la caja taupe»). QA: **4/4 limpias**.

**⚠️ La foto de la slide 4 es INTERINA, no se entrega así.** Eli la pidió
*«una trabajadora sin rostro preparando café, y que se vea el espacio del bar»*.
Hoy lleva el **mesón real de servicio** de Between (`espacios/HDT_56.jpg`, recorte
derecho 4:5 desde el original de 6718 px, gradado →
`fotos-gradadas/bar-servicio.jpg`, con su excepción en `.gitignore`). Se eligió
sobre la barra del bar —más linda pero es una pared de destilados— porque **dice
«servicio»**, que es el mensaje de la slide, y no repite el fondo de la portada.
**Le falta el gesto de la mano.**

**Magnific: registrado pero NO operativo.** Se agregó
`magnific / http / https://mcp.magnific.com` a `mcpServers` del proyecto en
`~/.claude.json` (con respaldo). ⚠️ **El CLI `claude` no existe como binario en
este PC** —se usa la extensión de VS Code—, así que `claude mcp add` no se puede
correr: hay que editar la config a mano. Faltan dos cosas y basta con una:

1. El MCP **no carga hasta reconectar la sesión** (`/mcp` → reconnect, o chat nuevo).
2. La clave de `~/.magnific_key` da **401**. ⛔ **NO es la de Freepik**: la propia
   API responde con la URL buena → `magnific.com/developers/dashboard/api-key`.

El prompt ya está escrito en `scripts/between-slide4-magnific.py`, con las fotos
reales del bar como `--refs` para que no invente un bar de stock, y con la regla
KIMBO explícita (taza blanca total, sin logo).

**⭐ Dos bugs del doctor, y el segundo importaba.**

1. Reportaba **4 fichas «JSON inválido» siendo válidas las 8**: abría el archivo
   sin declarar codificación y en Windows Python lee en **cp1252**, que no tiene
   definidos los bytes `0x81`/`0x8D`/`0x90`. Las marcadas eran justo las que llevan
   `Á`, `Í`, `⭐` o `←`.
2. **Se saltaba EN SILENCIO la verificación de material** —la compuerta que detectó
   las 19 referencias rotas de Revex/Casablanca— porque exigía `~/copylab-venv`, que
   en este PC no existe (los paquetes están **globales**, ver `credentials/LEEME.md`).
   Ahora cae a un Python del sistema con PIL+numpy. **Corrió por primera vez acá:
   295 archivos revisados, 295 válidos, 0 rotos, 0 vacíos.**

También se parchó `between-entrega.py`, que reventaba con `UnicodeEncodeError` al
imprimir el «✓» **después** de haber escrito las piezas: parecía que la entrega
había fallado y en realidad ya estaba hecha.

**Dónde quedó.**

| | |
|---|---|
| Carrusel Cowork r6, las 4 slides | `out/hilton-between-cowork-r6/` |
| Las 3 entregables | `out/entrega-cowork-r6/S1/`, con nombre de portal, 2250 px y 150 ppp |
| Piezas aprobadas re-verificadas | `out/_verif/` — idénticas a la entrega |
| Página de revisión (antes/después con medidas) | `https://claude.ai/code/artifact/9688ec3b-7ebd-4707-8051-f7df8bd8e600` |
| Regla y medición | `clients/hilton/CLAUDE.md § LA COLUMNA` + `src/brand/hilton-between.ts` (`bloque.columna: 810`) |
| Props nuevos | `BetweenSistema.tsx`: `columna`, `columnaCaja`, `aireTituloACaja`, `velo` |
| Herramientas nuevas | `between-medir-bloque.py` (mide la **tinta**, no la caja del layout) · `between-slide4-magnific.py` |
| Segunda `/al-dia` (19:30) | `clients/_estado-sync.json`: **no hay ronda 6** |

**Qué sigue, en orden.**

1. **⛔ Copiar el Cowork r6 a la carpeta de entrega.** `Desktop\S1 BETWEEN` todavía
   tiene las 3 slides **viejas** de las 15:19 — las de la jerarquía mala. Las buenas
   están en `out/entrega-cowork-r6/S1/`. **Esto es lo primero de mañana.**
2. **Destrabar Magnific** y generar la foto de la mano. Después: apuntar
   `FOTO_SERVICIO`, rendir `BW-F-Cowork-4`, QA, y **descomentar `BW-F-Cowork-4` en
   `scripts/between-entrega.py`**.
3. **Subir a Drive.** Sigue faltando `credentials/token.json`, así que **nada de esto
   está en Drive**. Allá las 27 piezas siguen en la versión del **28-08 01:53
   (ronda 4)** y faltan los **5 PNG de feed** (Cowork 1/2/3 y Cumpleaños 1/2) aunque
   la grilla ya marca FEED E como `CORREGIDO`.
4. La ficha `clients/hilton/marca.json` **no existe** (lo marca el doctor; `abakos`
   está igual). Todo lo medido ya está en `src/brand/hilton-between.ts` y en el
   manual: es pasarlo a JSON.

**Abierto.**

1. ⚠️ **La slide 4 lleva foto interina.** No se entrega hasta tener la de la mano.
2. ⚠️ **Duplicados en Drive:** `BW ST 01-09`, `03-09` y `04-09` existen **dos veces**
   en la misma rama (la vieja del 28-08 en `BW` y la nueva en `BW/S1/STS`). El portal
   levanta **por nombre** — hay que limpiar.
3. **¿La slide 4 lleva logo?** Eli dijo «para que se vea el logo y los textos de
   arriba», pero la regla escrita es que **en carrusel el logo va sólo en la
   portada**. Se respetó la regla y quedó sin logo. **Falta que ella confirme.**
4. **`credentials/token.json`** — sin eso no se puede corregir ninguna pieza ya
   entregada en Drive. Mismo bloqueo desde el 31-08.
5. **NO hay ronda 6**: los 9 comentarios nativos de la grilla siguen siendo los del
   31-08 17:34–17:59. El guardado de hoy 19:25 sólo movió estados (FEED E y
   STORIES C y D pasaron a `CORREGIDO`).
6. **Hilton no tiene `reglas.yaml`** (Casablanca, Revex y Cava sí). La regla de la
   columna es medible y debería entrar al motor de QA cuando se abra ese archivo.
7. Sin cambios: el **listado del cumpleaños de CINCO ítems** contra los cuatro de
   nuestra pieza, y el **Café Bombón** esperando al cliente.

---

## 2026-09-01 (tarde) · Eli (Windows) — BETWEEN: la S1 de septiembre corregida entera, y el logo del vaso resuelto de raíz

**Qué se hizo.** Cuatro rondas de correcciones sobre las 7 piezas de la **S1**
(carrusel Cowork 1-sep, post Cumpleaños 3-sep y las dos stories), todas pedidas por
Eli en la sesión. Quedaron **entregadas en `Desktop\S1 BETWEEN`** con el nombre del
portal, 150 ppp verificados. **⛔ NO están en Drive** — sigue faltando el token.

**Lo que se arregló, pieza por pieza:**

| Pieza | Qué se hizo |
|---|---|
| **ST 1-sep** Promo To Go | La **CTA que faltaba**, literal del brief (`STORIES!C10`): «Pasa por Between y llévalo contigo». Pasó a **botón blanco** con la orden dentro y el cierre debajo. Las **medias lunas ya se ven completas** (el render viejo usaba un recorte más apretado de la foto). Confeti corrido: estaba encima del producto |
| **FEED 1-sep** Cowork slide 1 | La caja dejaba **«pendientes.» sola en la segunda línea**. Corte del brief, una frase por línea, interlínea 1,16 |
| **FEED 1-sep** slides 2 y 3 | **Fuera Brushwell**: la línea de acompañamiento pasa a Raleway 500 en caja alta (`scriptSans`). La portada queda como la única con script. En la slide 3 la pregunta estaba partida entre dos pesos y su caja dejaba «reunirte.» viuda |
| **FEED 3-sep** portada | **Fuera el lockup** — la marca ya está en el vaso. Cierra la decisión que estaba abierta desde el 31-08 |
| **ST 3-sep** | Volvió a ser **UNA sola** story con las dos informaciones (titular + listado con emojis). Cabe porque cambió el vaso |
| **Los dos vasos del cumpleaños** | Logo re-estampado de raíz: ver abajo |
| Precios y horas | Cifras `lnum` + `tnum` en las tres cajas |

**⭐⭐ El logo del vaso, la historia completa — porque costó cuatro intentos.**
El reclamo era «se ve sucia el logo» y después «no puedes curvarlo de esa manera».
Las dos cosas tenían una causa distinta y las dos quedaron medidas:

1. **La suciedad era un velo, no el logo.** El re-sellado masivo de la ronda 5
   borró el sello anterior con `--clonar lados`, que interpola cada FILA entre las
   franjas laterales; eso aplana la curvatura del cilindro y deja **un rectángulo
   más claro con los bordes rectos a la vista**. Y el cliente **nunca había
   reclamado por el logo de estas dos piezas** (en FEED E pidió «*incluir*» el
   logo; el «nada que ver» era del carrusel To Go). El arreglo en bloque dañó una
   pieza que estaba bien.
2. **La curvatura venía de la ronda 4.** Al volver a esa versión para rescatar su
   cartón limpio, se restauró el sello viejo con `curvar()`: comba sinusoidal **más
   acortado lateral del 18 %**. Medido: proporción **2,619** y **2,069** contra
   **3,027** real — 13 % y 32 % achatado.

**La salida, y es la lección de la sesión:** un logotipo **no es un bloque, son
líneas de 3–6 px**. Se borran **solo los trazos** con convolución normalizada
—cada píxel se reemplaza por el promedio de sus vecinos conocidos— así el gradiente
del cilindro y el grano del cartón no se inventan, se interpolan a 3 px. Después se
estampa el vector plano. `scripts/between-logo-vaso-plano.py`.

⛔ **Cuatro caminos que NO sirven y no hay que volver a intentar:** re-estampar
borrando un bloque (velo), pegar el recorte del vaso real encima (el vaso de la
escena es más ancho abajo y **asoma por el costado** — el «extraño y doblado»),
rellenar el fondo del vaso viejo (emborrona la estructura vertical), y trasplantar
la banda de cartón real (llega con la línea de base torcida).

**Y tres medidas nuevas que antes se hacían a ojo:**

| | valor |
|---|---|
| logo ÷ ancho visible del vaso, en el vaso oficial | **0,89** → se usa **0,86** (el sello va plano y hay que dejar aire en las puntas) |
| centro | el **eje de la silueta** del cuerpo, no el centro del sello anterior |
| altura | contra **lo que tapa**, no contra el cartón: los dedos suben a y 1236 aunque el cartón llegue a 1300 |

**Dónde quedó.**
- Piezas: `Desktop\S1 BETWEEN` (7 PNG) y `out/entrega-drive/S1/`.
- Assets nuevos versionados: **`logo-negro-vector.png`** (4214×1392, proporción
  3,0273) sacado del editable oficial `Between_logo_oficial.ai` que mandó Eli
  (Drive `1qIIz0OjsoOgRqv0TGFfE4e22xeelpsvE`, **página 1** de 8). El `.ai` es PDF
  1.6 por dentro: se rasteriza con `pypdfium2`, sin Illustrator.
- Scripts nuevos: `between-logo-vaso-plano.py` (borrado de trazos + sello plano +
  `--arco` sutil) y `between-logo-densidad.py`.
- Sistema: `TitularBetween` con `scriptSans`; `PanelTaupe` con `interlinea`;
  `Checklist` con `size`/`gap`; `BotonBlanco` nuevo en `BetweenRecursos`.
- ⛔ `fotos-reales/cumple-vela-real.jpg` **salió de producción** (era el montaje
  del vaso real). El archivo se deja como registro del intento.
- Todo el detalle medido está en `clients/hilton/CLAUDE.md` §§ 6–14.

**Qué sigue, en orden.**
1. **Subir la S1 al Drive.** Falta `credentials/token.json` (traerlo del Mac, ver
   `credentials/LEEME.md`). Después `python scripts\between-subir-drive.py`.
2. **La ilustración de personas del carrusel Cowork.** Eli la pidió con una
   referencia de Pinterest pero **el archivo no está**: no en
   `raw/hilton/between/de-eli` (vacía), ni en Descargas/Escritorio/capturas, ni
   entre las 25 imágenes incrustadas en la grilla. Pinterest bloquea la lectura.
   **Bloqueada hasta que deje el archivo en esa carpeta.**
3. **Slide 2 del Cowork sigue siendo el Winter Garden** y Scarlette pidió «una
   mesa con un pc y un café». La imagen ya está en la carpeta de Eli:
   `raw/hilton/between/ediciones-ia-eli/magnific_agrega-una-laptop-en-la-m_iAi90W63uK.png`.
   No se cambió porque ella acotó el carrusel a los comentarios de textos.
   ⚠️ Y `cowork-laptop.jpg` **no tiene ninguna laptop**: son dos hombres en el muro
   verde. El nombre engaña.
4. Lo que sigue en pie de la ronda 5: regradar bajando calidez y altas, y
   regenerar los montajes rechazados por ambiente (FEED 7-sep, 9-sep slides 2 y 4,
   11-sep, 14-sep slides 1 y 4, ST 9-sep).

**Abierto.**

1. ⚠️ **El listado del cumpleaños que adjuntó el cliente tiene CINCO ítems, no
   cuatro.** Está anclado en `FEED!E13` (`xl/media/image21.png`). Faltan «¡Elige el
   tamaño que quieras!» y «¡Pregúntanos por los cafés disponibles!», y el nuestro
   trae «Presenta tu carnet en la caja» que **no está en el adjunto**. Son dos
   condiciones comerciales sin comunicar. **Hay que resolverlo antes de la próxima
   entrega.**
2. **Del vaso vigente no existe toma frontal aislada en alta resolución.** Lo que
   destrabaría cualquier montaje futuro es una foto: el vaso de frente, superficie
   lisa, luz pareja. Ojo: los packshots frontales 336–339 de la sesión del cliente
   son del **vaso ANTIGUO** (cuerpo negro con faja kraft).
3. **`tnum` no está en los Raleway del proyecto** (sí `lnum`). El avance tabular
   estricto no lo puede dar esta fuente; si alguna vez se necesita una columna de
   precios milimétrica hay que traer la Raleway variable de Google Fonts.
4. **Café Bombón** sigue esperando al cliente (cómo se muestra la leche condensada
   y si va en vaso transparente o kraft).
5. ⚠️ **Hubo DOS sesiones trabajando en este repo hoy.** Los commits `9c0940f` y
   `65d38ae` (13:22 y 13:23) no salieron de esta sesión y uno reescribió la
   bitácora entera. No se perdió nada, pero **conviene trabajar con una sola
   sesión por repo** para no pelear la bitácora.

**Falso positivo conocido.** `between-qa.py` avisa «texto a 22 px del borde
izquierdo» en `BW-S-ToGoDulce`: arma la máscara con píxeles beige de trazo fino y
toma las hojaldres pálidas de las medias lunas por tipografía. Las otras 6 piezas
pasan limpias.

---

## 2026-09-01 · Eli (Windows) — BETWEEN: el conector de Drive NO puede entregar, y quedó probado

**Qué se hizo.** Día de desbloqueo, no de producción. Se cerró la duda que venía
arrastrándose desde el 31-08 sobre por qué no se sube nada al Drive. **No es un
problema de permisos:** Eli le dio permiso de escritura completo al conector de
Drive y no cambió nada. La causa está en el propio conector, verificada en su
esquema:

| Herramienta | Límite real |
|---|---|
| `Crear archivo` | solo acepta el contenido **incrustado en la llamada**, en base64 |
| `Actualizar archivo` | solo cambia **título y carpeta** — nunca el contenido |

Las 3 piezas del cumpleaños pesan 5,5 · 4,4 · 5,2 MB; en base64 son ~7 MB de texto
cada una, del orden de **2 millones de tokens por archivo**. No entran con permisos
ni sin ellos. Y como `Actualizar` no toca el contenido, **por el conector es
imposible reemplazar una pieza conservando su enlace** — que es exactamente lo que
necesitan las 27 piezas de la carpeta BW.

⛔ **Conclusión dura: la entrega a Drive depende de `credentials/token.json` y de
`between-subir-drive.py --actualizar`. No hay atajo por el conector.**

**El desvío que sí sirve hoy.** Las 3 del cumpleaños **no necesitan el token**: la
carpeta S1 (`19Bv7lfMBEIt_4JLRStWKObtCnf4OmPdD`) está vacía, así que son archivos
nuevos y no hay ningún enlace que conservar. Se suben arrastrándolas desde
`out/hilton-between-cumple-r5/entrega S1/` a drive.google.com, con el nombre tal
cual (lo espera el portal). El token solo es imprescindible para corregir piezas
**ya entregadas**.

**Estado del Drive al cierre.** S1 sigue vacía (comprobado). Las 27 piezas del mes
siguen en BW en su versión del 28-08 (ronda 4). Nada nuevo en el Drive después de
las 13:29.

**Dónde quedó.** Se commiteó la cola de la ronda 5 que estaba fuera de git desde el
31-08: las **7 fotos gradadas** nuevas (`segundo-nivel`, `cowork-laptop`,
`winter-garden`, `mesa-cafe-2piso`, `togo-vaso-foto`, `rol-canela`,
`taza-cappuccino-nobg`), sus excepciones en `.gitignore`, los scripts
`between-entrega.py` y `material-a-fotos.py`, y la story nueva `StCumpleDetalles`
registrada en `Root.tsx` y `BetweenEntry.tsx`. `npm run typecheck` limpio.

**Qué sigue.** Rendir el **carrusel Cowork** y la **ST Promo To Go** — el material
local ya está (`cowork-laptop.jpg` y `rol-canela.jpg` se bajaron). Pero no se puede
tocar ninguna de las dos sin resolver antes lo de abajo.

**Abierto.**

1. 🔴 **URGENTE Y NO RESUELTO HOY.** El 1-sep se publicaban el **carrusel Cowork**
   (10:00) y la **ST Promo To Go**, y las dos están *en cambios* por la ronda 5:
   **lo que el cliente tiene en Drive es la versión sin corregir, y el día ya pasó.**
   Hay que decidir con KAM si se corrige y re-sube igual o se deja publicado así.
2. **Siguen sin respuesta las dos preguntas de la regla del lockup** (del 31-08
   tarde), y bloquean `Cumple1`, `ToGo1`, `StToGoDulce` y `StCumple`:
   ¿el carrusel To Go queda sin lockup en las 4 slides, baja a otra slide, o la
   portada es excepción? ¿La regla alcanza a cualquier logotipo legible en la foto,
   solo al vaso, o solo al vaso en primer plano?
3. **Falta `credentials/token.json`** (está en el Mac, en `ASISTENTE PERSONAL/
   credentials/`). Sin él no se corrige nada ya entregado.
4. **Falta `.env`** con `FREEPIK_API_KEY` y `MAGNIFIC_API_KEY`: sin eso no se pueden
   regenerar los 9 montajes rechazados por ambiente.
5. Sin cambios: el **Café Bombón** sigue esperando que el cliente diga cómo se
   muestra la leche condensada y en qué vaso va.

---

## 2026-08-31 (noche) · Eli (Windows) — BETWEEN: el vaso pasó a ser fotografía, y el estudio ya corre en Windows

**Qué se hizo.** El cliente rechazó el vaso otra vez —«el vaso no se parece al
real… se ve quemado y extraño, debe verse hiperrealista»— y al ir a buscarlo a la
sesión del cliente aparecieron **dos vasos distintos**. Eli confirmó que el
vigente es el **B: cuerpo crema con el logotipo impreso directo y tapa negra
plana** (frames 255 · 257 · 264 · 266). El otro —cuerpo negro con faja kraft, el
que ella misma retocó en 245/281/293— es el antiguo. Se recortó el vaso real del
frame **255**, el único donde está entero y sin nada delante, y se montó sobre la
escena aprobada de la story del 3-sep.

**⭐ Y se resolvió por qué un recorte se ve pegado, con números.** No era el
recorte: era cómo estaba puesto. Medido entre recorte y escena:

| | Recorte | Escena | Qué se hizo |
|---|---:|---:|---|
| Nitidez (varianza del laplaciano) | **2095** | 13,5 | desenfoque de 3 px |
| Luz entra por | **derecha** | izquierda | re-iluminado con degradado lateral |
| Sombra de contacto | ninguna | — | elipse suave al lado opuesto de la luz |

⛔ **El vaso no se puede espejar** para arreglar la luz: invertiría el logotipo.
Todo quedó en `scripts/between-montar-vaso.py`, reutilizable.

**La vela se veía rara porque no era una vela:** era un pabilo con llama, sin nada
de cera. Se le dibujó el cuerpo, se subió la llama y se le añadió el resplandor
sobre la tapa.

**Dónde quedó.** Recorte reutilizable en
`public/assets/hilton/between/togo-vaso-real-nobg.png` (1341×1851, sin fondo).
Escena en `public/assets/hilton/between/fotos-reales/cumple-vela-real.jpg`.
`StCumple` apunta ahí. Las 3 piezas del cumpleaños rendidas en
`out/hilton-between-cumple-r5/entrega S1/`, con el nombre del portal.
Comparación visual: <https://claude.ai/code/artifact/71c547d8-0899-42d5-aa90-f9c8408becc1>

**⭐ El estudio ya corre en Windows.** Los scripts eran de Mac y cuatro cosas
fallaban en seco. Todas corregidas y **probadas**, no solo escritas:

1. `_entorno.py` → `python_venv()` caía a la cadena `"python3"`, inexistente acá.
2. `hilton-drive-pull.sh` → llamaba a `/usr/bin/python3` y dejaba un `
` en el
   nombre, que Windows convierte en `_` (`foto.jpg_`). **Usar
   `scripts/drive-carpeta.py`**, que además trae `--miniaturas` para revisar una
   sesión de 353 fotos sin bajar gigas. ⛔ El `.sh` quedó parchado pero el bueno
   es el `.py`.
3. `between-rendir.sh` → ruta de Chrome del Mac y sandbox de iCloud. **Usar
   `scripts/between-rendir.py`**, que fuerza UTF-8 en `subprocess` (con el cp1252
   de Windows la salida de Remotion revienta el hilo lector).
4. ⛔ **`credentials/` NO estaba en `.gitignore`.** Un token ahí se publicaba a
   todo el equipo en el siguiente push. Blindado y verificado con
   `git check-ignore`, junto con `.env` y `client_secret*.json`.

Instalado en la máquina: `google-api-python-client`, `google-auth`,
`google-auth-oauthlib`, `requests`, `python-dotenv`. Instrucciones en
`credentials/LEEME.md`, escrito para Windows, más `scripts/autorizar-google.py`
por si hay client secret pero no token.

**Qué sigue.** Las **dos piezas de feed** con el mismo tratamiento: ahí el vaso va
sujeto entre dos manos, así que hay que devolver los dedos por delante del vaso
real — más delicado que la story. Después, la cola de la ronda 5 que sigue en pie.

**Abierto.**

1. ⚠️ **Mi story choca con la regla 8 de la entrada anterior.** Al cambiar el vaso
   de IA por el real, **el logotipo impreso quedó mucho más legible**, y la pieza
   sigue llevando el lockup arriba. `StCumple` no estaba en las tres que se
   auditaron porque entonces su vaso apenas se leía. Ahora sí aplica: **necesita
   la misma decisión** que `Cumple1`, `ToGo1` y `StToGoDulce`.
2. ✅ **RESUELTO el «¿en agosto?»**: Eli confirmó que va **«¿Estás de cumpleaños en
   septiembre?»**. Ya está aplicado en el feed y en la story. Sale de la lista de
   abiertos de las dos entradas anteriores.
3. **Nada se subió al Drive todavía.** No es permiso —se comprobó subiendo y
   descartando un PNG de prueba en la carpeta S1—: el conector solo acepta el
   archivo incrustado en la llamada y estas piezas pesan 4–6 MB (≈1,5 M de tokens
   cada una). **Falta `credentials/token.json`** y se sube con un comando.
4. Siguen en pie: el Café Bombón esperando al cliente, y las dos preguntas de
   alcance de la regla del lockup.

---

## 2026-08-31 (tarde) · Eli (Windows) — BETWEEN: el vaso ya firma, y septiembre quedó desparejo

**Qué se hizo.** Eli enunció un criterio de la cuenta que nunca estaba escrito:
**cuando la foto trae el vaso con el logotipo impreso, la pieza no sobrepone el
lockup** — se lee dos veces la misma marca y se ve mal. Se auditó toda la grilla
de septiembre contra esa regla y **tres piezas la rompen**: `Cumple1` (FEED 3-sep),
`ToGo1` (FEED 14-sep, portada del carrusel) y `StToGoDulce` (ST 1-sep). Otras
cuatro ya la cumplían. La regla se venía aplicando **a criterio, pieza por pieza**
— `StEmergencia` hasta la trae comentada en el código — y por eso el mes salió
disparejo. Ahora quedó escrita en el manual (§ ⛔ 2), en la gramática como regla 8
y en la lista de QA.

**Dónde quedó.** Comparación visual antes/después publicada en
<https://claude.ai/code/artifact/6d2d656d-b199-421f-b086-79884308c1fc>, con
renders **reales** (`npx remotion still`, no montajes) de `Cumple1` y `ToGo1` con
y sin lockup. `BetweenSeptiembre.tsx` se parcheó solo para rendir y quedó
**restaurado byte a byte** (verificado con `cmp`); `npm run typecheck` limpio.
Los PNG viven en `out/hilton/regla-logo/` (gitignored). **Ninguna pieza se
corrigió todavía y no se subió nada al Drive.**

**Qué sigue.** Sin la respuesta a las dos decisiones de abajo no se tocan las
piezas. Con ellas: corregir las 3, y después retomar la cola que ya venía de la
ronda 5 — bajar el material (`scripts/hilton-drive-pull.sh` sobre GRILLA IA
BETWEEN, `10Wyq-JrVAwkIItMUJH2De6wuxTiBDuDh`), regradar bajando calidez y altas,
regenerar los 9 montajes rechazados por ambiente, rendir, `between-qa.py` y subir
con `between-subir-drive.py --actualizar`.

**Abierto.**

1. **Choca con la regla 5** («en carrusel el logo va SOLO en la portada»): la
   portada del To Go es justo la del vaso con logotipo. ¿El carrusel queda sin
   lockup en las 4 slides, el lockup baja a otra slide, o la portada es excepción?
2. **Alcance de la regla**: ¿cualquier logotipo legible en la foto (letrero del
   local, bolsa, faja), solo el vaso, o solo si además va en primer plano?
3. Sigue en pie lo de la ronda 5: el **«¿Estás de cumpleaños en agosto?»** de
   Scarlette para una pieza de septiembre, y el **Café Bombón** esperando al cliente.

**Notas de máquina.** Este Windows **sí tiene Python** (3.14.7 con PIL, openpyxl y
numpy): los scripts de imagen corren acá. Lo que falta es `requests`/
`googleapiclient`, el token de Google, `raw/` y **22 de las 32 imágenes** — por eso
`StToGoDulce` no se pudo rendir (le falta `rol-canela.jpg`). La memoria decía que
no había entorno de Python y era falso; ya está corregida.

## 2026-08-31 · Eli (Windows) — BETWEEN, ronda 5: el logo del vaso salía deformado

**Dónde quedó.** Llegó la **ronda 5** el mismo 31-08 entre las 17:34 y las 17:59:
**9 comentarios de Scarlette Muñoz**, todos asignados a Eli. Se arregló la causa
del reclamo transversal —el logotipo— y quedó todo el resto documentado y
pendiente de material.

**⚠️ Cómo llegaron los comentarios, que es media lección.** NO están en la fila 15
`COMENTARIOS DISEÑO`: son **comentarios nativos de Excel anclados a celdas**, en
`xl/comments1.xml` (FEED) y `xl/comments2.xml` (STORIES) dentro del propio xlsx.
La fila 15 seguía mostrando los de la ronda 4, la mitad ya tachados. **Leyendo
solo la fila 15, esta ronda entera se pierde.** Traen autor y fecha, que es como
se distingue lo nuevo.

**Lo que se arregló, y era culpa nuestra.** El cliente dijo «el vaso de café tiene
el logo de between **completamente distinto**» y «el vaso de café **nada que ver**
jajajaja». No era el generador: `scripts/between-logo-vaso.py` traía **dos
deformaciones encadenadas**. `resize((ancho, alto))` metía el logo en la caja que
le dieran ignorando su proporción —salió entre **2,59 y 3,02** cuando la real es
**3,0278**, hasta un 15 % achatado— y encima `curvar()` lo arqueaba sobre un
cilindro, con lo que «COFFEE & BAR» quedaba ilegible.

- ✅ Script **reescrito**: escala uniforme (el alto sale de la proporción del
  propio archivo y no hay parámetro para alterarla) e integración **por tono**,
  multiply contra el cartón. `curvar()` se eliminó.
- ✅ Las **5 imágenes con vaso re-estampadas** con el logo real, verificadas a
  escala de pieza: `togo-salida-2`, `togo-cafe-dulce`, `togo-trio-45`,
  `cumple-manos`, `cumple-vela`. Reproducible con
  `python3 scripts/between-relogo-ronda5.py --revisar`.
- ✅ Correcciones de texto en el carrusel To Go: fuera «Café grande» de las
  slides 2 y 3, y la info de promo de la slide 4 unificada con las otras.
  `npm run typecheck` limpio.

**Dos trampas del borrado que costaron dos pasadas**, ya resueltas en el script:
en `cumple-manos` no se puede clonar cartón ni de abajo (hay **dedos**) ni de
arriba (hay **tapa negra**) — hay que usar `--clonar lados`; y el difuminado del
empalme tenía un inset **fijo** de 10 px que en un vaso chico se comía el borde y
dejaba **asomar el logotipo viejo** (pasó en `togo-salida-2`). Ahora va proporcional.

**Las 3 piezas del cumpleaños (3-sep) quedaron RENDIDAS.** Eli confirmó que el
titular va «¿Estás de cumpleaños **en septiembre**?» —Scarlette había escrito «en
agosto»—. Con eso se aplicaron los tres cambios: los textos de la G1, la G2
convertida en **checklist** con emojis (fuera el mockup de Instagram, que metía un
post dentro de un post y encima dependía de una foto que no está acá) y la story
arrastrando el mismo titular. Salidas en `out/hilton-between-cumple-r5/entrega S1/`,
ya con el nombre del portal, en feed 2250×2812 y story 2250×4000.

⭐ **Y se destrabó el render entero.** Faltaban las 8 ilustraciones de
`public/assets/hilton/between/recursos/` (globos, confeti, flechas) y sin ellas no
rinde **ninguna** pieza de Between. Se re-extrajeron del .svg de Eli
(`1EZHJab1Rp8c8vuTHqAehF6tCk-CiRsXa`) rasterizándolo con Chrome headless y
recortando por canal alfa. Pesan 215 KB y **ahora se versionan**, para que no
vuelvan a faltar en la próxima máquina.

**⛔ La entrega al Drive quedó pendiente.** Las 3 piezas NO se subieron a la
carpeta `S1` (`19Bv7lfMBEIt_4JLRStWKObtCnf4OmPdD`): no hay token de Google acá, y
el conector MCP solo acepta el archivo incrustado en la llamada —estos PNG pesan
4–6 MB—. Se resuelve arrastrándolos desde el navegador, o dejando `token.json` en
`credentials/` y corriendo `between-subir-drive.py`.

**⛔ Lo demás que NO se pudo hacer acá, y por qué.** Esta máquina Windows **no tiene 22
de las 32 imágenes** que pide `BetweenSeptiembre.tsx`, ni la carpeta `raw/hilton/`,
ni token de Google. Al repo solo viajan las 10 corregidas en la ronda 4. Por eso:
**no se re-rindió ninguna pieza y no se subió nada al Drive.** Las 27 piezas del
Drive siguen en la versión del 28-08 01:53.

**Lo que falta, en orden.** Todo el detalle con los comentarios verbatim está en
[`feedback/2026-08-31-ronda5.md`](feedback/2026-08-31-ronda5.md).

1. Bajar el material: `scripts/hilton-drive-pull.sh` sobre **GRILLA IA BETWEEN**
   (`10Wyq-JrVAwkIItMUJH2De6wuxTiBDuDh`), que usa el visor público y no pide auth.
2. **Volver a gradar bajando calidez y altas.** Es el segundo reclamo transversal:
   «eliminar el filtro de color cálido» y «se ven quemadas… un filtro medio raro».
3. Regenerar los montajes rechazados por ambiente: FEED 1-sep slides 2 y 3, FEED
   7-sep, FEED 9-sep slides 2 y 4, FEED 11-sep, FEED 14-sep slides 1 y 4, ST 9-sep.
   ⭐ **El 2.º piso del local YA está fotografiado** («tenemos ese material», dice
   ella): se busca en el banco, no se genera.
4. Rendir, `between-qa.py` y subir con `between-subir-drive.py --actualizar` para
   conservar los enlaces.

**Decisiones abiertas.**

- **«¿Estás de cumpleaños en agosto?»** — así lo escribió Scarlette para una pieza
  de **septiembre**. Casi seguro es un lapsus, pero es el titular: hay que
  confirmarlo antes de escribirlo. Y la ST del 3-sep depende de ese mismo texto.
- El **Café Bombón** sigue esperando que el cliente conteste cómo se muestra la
  leche condensada, y nadie ha confirmado si va en vaso transparente o kraft.

## 2026-08-27 · Valeria — BETWEEN, ronda 4 del cliente resuelta

**Dónde quedó.** El cliente escribió comentarios nuevos en la grilla de
septiembre el mismo 27-08 por la tarde, después de que se entregaran las 27
piezas. Se aplicaron todos y **13 piezas están re-subidas al Drive con los mismos
enlaces**, así que quien ya tenía el link ve la versión nueva.

**Lo que se hizo, por pieza:**

| Pieza | Qué pidió el cliente | Cómo se resolvió |
|---|---|---|
| FEED 03-09 Cumpleaños G1 | más énfasis en el cumpleaños, con sus tres textos | «¿Estás de cumpleaños?» arriba, «ESTE CAFÉ ES PARA TI» de protagonista, «¡Ven por tu café de regalo!» en la caja |
| FEED 03-09 Cumpleaños G2 | el listado con emojis y más adornos | emojis a color (hubo que nombrar la fuente de emoji) y 4 adornos en vez de 2 |
| FEED 07-09 Humor cafecito | «ya no podemos usar estas modelos tal cual» | escena nueva y **sin rostro**, como la referencia que eligió el propio cliente |
| FEED 09-09 Primero la foto 1 y 2 | «fotos de cosas para comer, no de gente» | bodegones reales de la sesión de platos |
| FEED 14-09 To Go 1 | «se ve muy derrotada y el fondo no es muy Between» | sale del local sonriendo, con el interior real detrás |
| FEED 14-09 To Go 4 | dulce + salado en la foto, vaso como el resto, «¡Llévate los 3!» | bodegón con los tres productos y el titular textual |
| ST 01-09 Promo To Go | «Café con logo Between!» | logotipo real estampado sobre el vaso |
| ST 03-09 Cumpleaños | mismos textos del feed + vaso con logo | unificado con el post, misma escena |
| ST 04-09 Según mis cálculos | «Ok, enlace a carta!» | sticker de enlace nuevo (`StickerEnlace`) |
| ST 09-09 Emergencia | «no se cacha bien al tapar la vitrina» + «todas las anteriores» | rediagramada como la referencia: vitrina frontal, producto entero, texto en las bandas |
| FEED 14-09 To Go 2 y 3 | *(no lo pidió)* | ver abajo |

**El hallazgo de la sesión.** El cliente pidió que el vaso de la slide 4 fuera
«como el del resto de las slides», dando por hecho que el resto estaba bien. No
lo estaba: **la slide 3 llevaba el vaso antiguo**. La causa es que la tabla del
manual tenía las fotos **al revés** y el sufijo `-actual` de los archivos engaña
(`togo-dulce-actual.jpg` es la vieja). Ya está corregido en
`clients/hilton/CLAUDE.md § EL VASO TO GO`. De paso, las tres cajas de precio del
carrusel decían «$4.290» donde el brief dice **«desde $4.290»**; quedaron
alineadas al brief.

**Y la causa raíz de media ronda:** los generadores de imagen devuelven el vaso
To Go **sin marca**, y a veces con un logotipo inventado. Por eso el cliente
reclamó lo mismo en tres piezas distintas. Se resolvió con
`scripts/between-logo-vaso.py`, que envuelve el logotipo real sobre el cilindro
del vaso. **La regla ahora es: foto real siempre que exista; si hay que generar,
se pide el vaso liso y se estampa.**

**Qué quedó pendiente.**

1. **Reel Café Bombón (7-sep).** Pasó a `OK PARA DISEÑAR` y el cliente preguntó
   «¿Cómo mostraremos la leche condensada al principio?». Hay propuesta escrita
   con tres caminos y una recomendación en
   [`PROPUESTA-reel-cafe-bombon.md`](PROPUESTA-reel-cafe-bombon.md). **Falta que
   el cliente elija** y que exista una foto del Café Bombón real.
2. **«Así se hace tu café»** sigue `POR GRABAR` (el comentario de coordinar la
   sesión del viernes ya está tachado, o sea resuelto).
3. **Promociones de desayuno**, feed y story: `PENDIENTE POR CLIENTE`.
4. **Las miniaturas dentro de la grilla del Sheet no se tocaron.** El archivo es
   de Sebastián Serrano y reescribirlo desde fuera le borra imágenes y formato de
   todas las columnas. Las piezas nuevas están en el Drive con los mismos
   enlaces; el reemplazo de las miniaturas lo tiene que hacer alguien desde
   Sheets.

**Decisión abierta.** Nadie ha confirmado si el Café Bombón se sirve en vaso
transparente (el brief lo asume) o en el vaso kraft de la marca. De eso depende
todo el planteamiento visual del reel.

**Dónde está todo.**
- Piezas: carpeta `BW` de `S1 HILTON SEP 2026` — `1fQqtl-2X2A4o1L5hH7jlz9xUh_YzXRjq`
- Portal de revisión: https://portal-hilton.vercel.app/between-revision.html
- Código: `src/compositions/hilton/BetweenSeptiembre.tsx`
- Referencias que dejó el cliente: `raw/hilton/between/refs-sept-ronda4/`
- Render: `bash scripts/between-rendir.sh` · QA: `scripts/between-qa.py`
- Subir correcciones: `scripts/between-subir-drive.py --actualizar <ID> ...`

> ⚠️ **Antes de aplicar un comentario de la grilla, mira si está TACHADO.** La
> fila COMENTARIOS DISEÑO mezcla lo pendiente con lo ya resuelto, y lo resuelto
> va tachado. La fila 14 es del cliente y la 15 del equipo de diseño.
