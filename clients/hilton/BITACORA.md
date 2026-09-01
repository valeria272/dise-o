# Bitácora — HILTON (DT · QB · Between · Piso18)

> Una entrada por sesión, la más nueva arriba. Sirve para que otro diseñador
> retome la cuenta mañana sin preguntar nada. Se escribe en el `/cierre`.

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
