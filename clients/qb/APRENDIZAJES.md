# QB Restaurant (Quotidien Bistró) — lo que el estudio sabe de este cliente

> **Qué es este archivo.** El cerebro de la cuenta: lo que se aprendió de este cliente
> sesión tras sesión, destilado. La bitácora cuenta **qué pasó**; esto dice **qué
> sabemos**. Si la diseñadora que lleva la cuenta falta mañana, con esto (más el
> manual `CLAUDE.md` y `marca.json`) otra persona retoma sin llamar a nadie.
>
> **Vale SOLO para QB.** Nada de acá se copia a otra marca, ni a una hermana
> (DoubleTree, Piso 18 y Between son cuentas aparte aunque compartan hotel y Drive).
> Se alimenta en cada `/cierre` — ver `docs/MEMORIA-POR-CLIENTE.md`.
>
> Criterio: **Elisabet Soto «Eli»** · Aprueba: **el cliente, por la grilla nativa de QB; contenido (Nicolás Ávila) ajusta textos**
> Última cosecha: **2026-09-28** · Cosechas: **8**

## 1. Quién es el cliente

Restaurante **y bar** en Av. Vitacura 2727, Las Condes, dentro del complejo Hilton pero
con línea gráfica propia. El bar pesa tanto como la cocina: las promos eje son **ALL YOU
CAN DRINK** (barra) y **Sunset QB** (terraza al atardecer), más convenios bancarios,
tragos del mes y DJ. Muestra cócteles, platos y rostros. El tono es **minimalista y
elegante**; el CTA es reservar (reservas@qbrestaurant.cl · CoverManager).

## 2. Cómo trabaja

| | |
|---|---|
| Quién pide / KAM | Eli encarga al estudio; contenido (Nicolás Ávila) pide cambios de texto por Slack |
| Quién aprueba (cliente) | El cliente, en la grilla; Eli revisa cada ronda mirando video, estática y comparaciones en Drive |
| Por dónde llega el feedback | Celda `COMENTARIOS CLIENTE` de la grilla **Sheet nativa** (gid FEED `351027330` · STORIES `49019995` · ORGÁNICOS `1890610027`); Eli con marcas en rojo sobre capturas |
| Dónde se entrega | Drive `QB / STS` (`1Ve22wlyaFlOMe4FGgyPw4J-nXKYiP4UU`); octubre en `S<n> HILTON OCT 2026 / QB / STS` |
| Ritmo | Grilla mensual; sólo se diseña lo que está `OK PARA DISEÑAR`. `CAMBIADO` = contenido reescribió el brief tras el comentario del cliente y **vuelve a revisión**: no se diseña (grilla de octubre, 25-09). Contenido de octubre: Scarlette Muñoz |
| Rondas típicas | La ST animada de AYCD (S5) llegó a v7: montaje del celular (mate, perspectiva, croma) y nitidez de textos |

## 3. Identidad en corto

- **Raleway** (principal, Adobe Fonts) · **Bell MT** + Italic (editorial/legal, versionada) · **Brushwell** (mano; usa `.ttf`/`.woff2`, nunca la `.otf`).
- Verde de marca = **degradado** `linear-gradient(90deg, #354A3A 0%, #66886B 50%, #354A3A 100%)`, botón de esquinas vivas. Texto blanco.
- Logotipo blanco, 1,650:1; el `Logo QB.png` del Drive es un lienzo de historia 99,7 % transparente.
- Historia 1080×1920 → entrega 2250×4000 · feed 1080×1350 (mesa 1:1) → entrega 2250×2813.
- Kit: `src/brand/qb.ts` (`QB_BOTON_FONDO`, `QB_AYCD`).

## 4. Reglas firmes

- **R-01** · QB es marca independiente: nada de DT, Between ni Piso 18 entra, y nada de QB va para allá — _Eli, 15-09: «QB Restaurant es una marca independiente…»_ · ✔×1
- **R-02** · El feed se ve minimalista y elegante; una pieza cargada no es de QB aunque cumpla el brief — _Eli, 15-09_ · ✔×1
- **R-03** · Cada pieza muestra cóctel, plato o rostro — _Eli, 15-09_ · ✔×1
- **R-04** · ALL YOU CAN DRINK es un bloque cerrado igual al KV: sólo cambia la foto; logo, nombre, botón con degradado y «TODOS LOS MARTES / POR $13.990 / 18:00 a 21:00 hrs» no se tocan — _Eli, 17-09: «botón verde con efecto de degradado y logo + el nombre no»; medido igual al píxel en las ST de junio y septiembre; ST n°2 S1 oct (AYCD 06-10), Eli 28-09: «la veo perfecta»_ · ✔×3
- **R-05** · Se escribe «ALL YOU CAN DRINK», en versales («ALL» y «DRINK» ExtraBold, «YOU» y «CAN» itálica) — _Eli, 17-09; reglas.yaml `aycd-grafia`_ · ✔×1
- **R-06** · Se escribe «Sunset QB»: «Sunset» en Brushwell, enlazado con el logotipo — _Eli 15-09; medido en `Post n°2 QB SUNSET`; reglas.yaml `sunset-grafia`_ · ✔×1
- **R-07** · En una promo con KV, el KV gana a la redacción del brief; del brief se toma literal sólo lo que el KV no cubre — _ST AYCD 28-09, S5, 17-09; Sunset 09-10, Eli 25-09_ · ✔×2
- **R-08** · El botón lleva el degradado horizontal (oscuro en bordes, claro al centro) y esquinas vivas — _barrido de `PROMOS QB 2026 AYCD 2026 ST.png`, 17-09; Eli lo declaró intocable_ · ✔×1
- **R-09** · El logotipo hace de **palabra** en la frase («MEJOR PAYA DE **QB**», «*Sunset* QB»), no de firma en la esquina — _medido en `ST n°2 S3 QB` y `Post n°2 QB SUNSET`, 15-09_ · ✔×2
- **R-10** · Todo va centrado; el titular es un bloque de dos pesos del mismo cuerpo — _medido en `ST n°2 S3 QB` (una pieza), 15-09_ · ✔×1
- **R-11** · Toda cifra en Raleway lleva **cifras de caja alta (`lnum`)**; activar «tabulares» no hace nada porque `tnum` no existe — _pedido de Eli 15-09 («los números suelen verse extraños»), diagnóstico con fontTools; Eli 28-09 sobre la ST n°1 S1 (Banco de Chile): «los números del 20 OFF y del 30 OFF queden armónicos, se ve desordenado… es una regla de Raleway, que se vea todo recto»_ · ✔×2. Ojo: todo componente propio (cajas, cifras sueltas) tiene que llevar `...QB_CIFRAS`; `Linea` y `BotonVerde` lo traen, una caja escrita a mano no
- **R-12** · La letra chica no tiene una sola fuente: Bell MT Italic en el post de Sunset, Raleway Itálica en la ST de AYCD. Mira la pieza antes de elegir — _corrección del 17-09_ · ✔×1
- **R-13** · Antes de diagramar se pregunta **«¿esta va a paid?»**; si sí o hay duda, el texto va dentro de la zona segura (250 / 340 / 115 px en 9:16) — _Eli, 15-09: «El texto es importante que no pueda ir fuera del margen»; Eli 25-09: «ten cuidado con las medidas que aparecen en Instagram»; Eli 28-09 sobre el legal del Sunset: «cuidando siempre los márgenes de Instagram y en caso de que se utilice paid»_ · ✔×5. Desde el 25-09 se aplica a **las 11 historias** de octubre, orgánicas incluidas, y también al logo (tope ≥ 250)
- **R-14** · En una pieza animada, la zona segura se mide en el **último** fotograma — _manual §6_ · ✔×1
- **R-15** · Nunca le pidas a un modelo de imagen que escriba la promo: la escena se genera con la pantalla en **verde plano** y encima se monta, con homografía, la gráfica rendida con las fuentes reales — _ST AYCD S5, 17-09; repetido en octubre (06-10 AYCD, 21-10 ticket)_ · ✔×2
- **R-16** · `minAreaRect` sirve para encontrar la pantalla, nunca para montar: los vértices salen de ajustar una recta a cada lado — _Eli, 21-09, ronda 6: «no se ve realista de acuerdo a la perspectiva del celular»_ · ✔×1
- **R-17** · El vidrio del celular refleja el bar (campo de luz desenfocado, espejado, fuerte arriba y débil abajo) — _ronda 6, 21-09; acerca la pieza al KV (35,1 vs 30,5)_ · ✔×1
- **R-18** · El despill se limita a la orla; ningún verde de croma queda en el canto (regla `croma-en-el-mockup`) — _ronda 6, 21-09_ · ✔×1
- **R-19** · El mate del celular se mide por **tono** (chasis neutro vs bar cálido), no por brillo, y se ajusta un modelo de silueta; el filo de acero no es el canto — _Eli lo marcó en rojo en las rondas 3, 4 y 5_ · ✔×1
- **R-20** · En Remotion nunca encuadres con `transform: scale()` sobre un `<Img>`: usa el tamaño real del elemento — _Eli, rondas 3–4: «se ve mal los textos pequeños», «mal recorte en la máscara»_ · ✔×1
- **R-21** · En la ST animada de AYCD lo del celular es estático (sólo se mueve UNLIMITED) y el legal va fuera del celular — _Eli, S5: «sólo el texto de UNLIMITED en movimiento, nada más»_ · ✔×1
- **R-22** · Un comentario tachado en la grilla no se ejecuta; uno que cambia el concepto se verifica (`font.strike`) antes, y si contradice al brief, se pregunta — _Eli, 17-09: «No tomes en cuenta el comentario ya tachado»_ · ✔×1
- **R-23** · En una pieza en bucle, el fotograma de la estática se identifica por diff contra la entrega anterior (AYCD S5: frame 0, no 239) — _v7, 23-09_ · ✔×1
- **R-24** · Al cambiar un solo texto de una pieza aprobada, se entrega el diff: cuántos píxeles se movieron y dónde — _v7, 23-09: 23.386 px, todos en la franja del texto_ · ✔×1
- **R-25** · El QA de QB se corre **con `--textos`**; sin eso el copy queda «SIN VERIFICAR» — _v7, 23-09 (las rondas 1–6 salieron sin verificar el copy)_ · ✔×1
- **R-26** · Todo material que no sea real (generado o montado con IA) lleva «Imagen referencial» abajo — _cliente, grilla de octubre (STORIES 22-10), leído 24-09; el cliente lo volvió a escribir en la celda del 22-10 el 25-09; aplicado en las 7 piezas generadas del 28-09 y retirado de la CMR al pasar a foto real_ · ✔×3
- **R-27** · No se genera lo que ya está fotografiado: la fuente son las sesiones propias, y del video se saca la foto, la historia, el reel y el post en movimiento — _Eli, 15-09; aplicado en octubre con las sesiones en video, 24-09; 09, 23 y 26 pasaron a foto real el 25-09_ · ✔×3
- **R-28** · El material iPhone 4K HLG se tonemapea a 709 antes de usarlo (`qb-oct-fotogramas.py`) — _grilla de octubre, 24-09_ · ✔×1
- **R-29** · Las promos se mantienen en el tiempo: una vigente no se da por vencida sola, se confirma con Eli — _Eli, 15-09_ · ✔×1
- **R-30** · Ni títulos ni bajadas llevan punto (final ni intermedio), aunque el brief lo traiga — _regla del cliente Hilton, 23-09-2026, citada en el manual de QB; el cliente le sacó los puntos al 09-10 en la grilla, 25-09_ · ✔×2
- **R-31** · Al corregir en Drive se sube con **nombre nuevo** (v4, v5…): la vista previa de Drive queda cacheada al reemplazar por el mismo ID — _17-09, Eli «no veo el cambio»; repetido en v5, v6 y v7_ · ✔×4 · ⚠️ **25-09 se incumplió**: la ronda de Eli se subió reemplazando con el mismo nombre (se le avisó del caché). La próxima ronda va con nombre nuevo
- **R-32** · Sólo se diseña lo que está `OK PARA DISEÑAR`; `PENDIENTE POR CLIENTE` no se toca — _bitácora 17-09, 21-09, 24-09 (Trivia de brindis, Reel DJ); 25-09: 8 piezas en CAMBIADO no se diseñaron; 28-09: el feed de S1 entero en CAMBIADO, no se tocó; 28-09 tarde: 6 historias en CAMBIADO sin tocar_ · ✔×6
- **R-33** · No se entrega con menos bitrate que lo aprobado (la S5 salió a crf 10 para igualar 4.484 kb/s) — _ronda 5, 21-09_ · ✔×1
- **R-34** · Un negro saturado que el QA lee como «foto estirada» se arregla con grano de película sutil (±2), no bajando la foto con una franja negra lisa — _octubre, 24-09_ · ✔×1
- **R-35** · El video de octubre se rinde a 2,5× y se baja a 2250×4000 con lanczos (2,0833× da alto no entero) — _`scripts/qb-oct-render.sh`, 24-09_ · ✔×1
- **R-36** · Bell MT y Brushwell son licencia del cliente: no se reusan en otra marca — _manual §4_ · ✔×1
- **R-37** · Si la promo ya tiene pieza aprobada (bancos, Sunset), se hace **sobre la aprobada**: cambian sólo la foto y los textos del brief; logo, sellos, marco, cajas, tarjetas y logos del banco no se redibujan — _Eli 25-09: «Banco de Chile y todos los bancos ya tenemos los diseños aprobados, los logos que hay que utilizar» · «Sunset QB, usa tal cual la pieza gráfica seleccionada, sólo cambia textos… el logo de Sunset QB déjalo tal cual» · «el 8 de octubre, el banco ya está aprobado, solamente cambios de fotografías»; Eli 28-09 sobre la ST n°4 S1 (CMR): «el texto de todos los días tiene que quedar igual de curvo, con esa curvatura… el 20 % de descuento déjalo como estaba el original»; y sobre la n°5 (Sunset): «que se vea un poco más similar a la de referencia»; CMR r5 aprobada el 28-09 con el bloque de la aprobada intacto_ · ✔×3. **Se calca midiendo** la aprobada (cajas de glifo por componentes conexos), no a ojo: una curva no se aproxima con `rotate()` y el cuerpo del 20 sale de la altura medida. Plantillas y elementos: manual «Piezas de banco y promos: sobre la APROBADA»
- **R-38** · Pocas tipografías: la pieza va en **Raleway**, y Bell MT sólo como acento en una palabra (en la 14, «Adivina») — _Eli 25-09 sobre la 14-10: «estás usando muchas tipografías, sólo usa Raleway, y en adivina puede ser la distinta, Bell»_ · ✔×1
- **R-39** · Nadie que parezca trabajador del hotel (traje, uniforme, garzón) aparece como invitado: en las escenas sociales, sólo invitados — _Eli 25-09 sobre la 26-10: «salen trabajadores del hotel, no pueden usar esa»; 28-09: en el post de cumpleaños la «QB 13 oct-108» se encuadró para dejar fuera a una persona de camisa blanca_ · ✔×2
- **R-40** · La foto no se sobregradúa: nada de quemado ni saturado. La fuente preferida es el **shooting de la carta de enero 2026** (foto de estudio, va casi sin tocar) — _Eli 25-09 sobre la 01-10: «se ve como quemado, muy saturado, no me gusta… usa del shooting nuevo… una foto mucho más bonita, más elegante»_ · ✔×1
- **R-41** · Las alternativas de un sticker de encuesta las fija el cliente en la celda INTERACCIÓN y van literales; el ✅ marca la respuesta para contenido y **no** se pinta en la pieza — _grilla de octubre, ST 14-10, leída 25-09_ · ✔×1
- **R-42** · Un carrusel de promo abre con la **G1 limpia** (sólo la foto, sin texto) y la promo va en la lámina siguiente — _cliente, grilla QB oct FEED!E14 (post AYCD 07-10, pasó de estático a carrusel), leído 28-09-2026: «Que sea como esos carruseles que hicimos antes, en que la G1 está limpia y luego viene la promo»_ · ✔×1
- **R-43** · Una historia muestra **la información más importante de inmediato**: ante un concepto elaborado (collage de 3 fotos con cortes y dibujos), va la opción más simple — _cliente, grilla QB oct STORIES!E14 (cumpleaños 07-10): «veamos opción más simple, siendo una story mostraría la información más importante de inmediato»_ · ✔×1
- **R-44** · Una pieza se identifica por su **título**, nunca por la columna ni la fecha: la grilla las corre sin avisar — _diff de la grilla QB oct, 28-09-2026: ST Banco de Chile 01→02-10, el REEL DJ de la semana 5 pasó de la columna R a la Q y el carrusel de bancos apareció en una columna sin fecha (H); 28-09 tarde: se corrieron otra vez las fechas de casi todas las historias y aparecieron 8 columnas nuevas_ · ✔×2
- **R-45** · En la itálica de Raleway la ligadura **«ff»** se ve pegada: en «office» y similares se apaga (`fontVariantLigatures: "none"`) y se da aire entre las f; y una bajada que acompaña al titular no se deja chica (en Sunset, 32 → 38 en mesa) — _Eli 28-09 sobre la ST n°5 S1 (Sunset): «Tu after office a otro nivel lo encuentro un poco extraño. Podrías aumentar un poco el tamaño. Y las dos F de Office separarlo un poco porque se ve muy juntos»_ · ✔×1

- **R-46** · Una historia se parece a su **referencia en elementos concretos**, no sólo en el mood: la tipografía del titular (p. ej. sans fina + una palabra caligráfica grande), el recurso gráfico (rótulo a mano con flecha, pastilla blanca con emojis, polaroids, nota escrita, ticket) y el tipo de fondo. Con las voces de QB: la caligráfica de la ref es **Brushwell**, la serif es **Bell MT** — _Eli 28-09: «revisando bien las referencias de las historias no se asemeja… las historias tienen que ser con elementos similares a la referencia… la ST del banco, la tipografía puede ser la del título principal igual a la referencia»; aprobadas así el mismo día: Banco de Chile, 14 Adivina («sumamente bien»), 08 CMR y 09 Sunset_ · ✔×4
- **R-47** · El fondo es **QB real**: la terraza (pérgola, plantas, maceteros de concreto, lámparas de mimbre de noche, mesas de listones) o la barra iluminada del shooting. Primero la foto real; si hay que generar, se genera **con una foto real de QB como referencia** — _Eli 28-09: Sunset «no me gusta que se vea una playa al fondo… tiene que ser con la terraza real que tenemos en QB»; CMR «quiero que sea una foto real de barra que tengamos»; estacionamiento «con el fondo de lo que describe el brief respecto a cómo es QB realmente»_ · ✔×3
- **R-48** · Un trago real de QB **no cambia de forma** al editar la escena: se conserva la copa real (bowl, pie, base, guarnición) y, si hay que ajustar su tamaño, se escala **parejo**, nunca se estira el pie — _Eli 28-09 sobre la sangría del AYCD: «tiene que ser igual a la real»; «la copa cambió de forma»; «la parte de abajo muy gruesa» (3 rondas)_ · ✔×1
- **R-49** · Tragos en fila van con el **borde de las copas a la misma altura** — _Eli 28-09, AYCD 06-10: «tanto el primero, el segundo y el tercer cóctel a la misma altura, la copa»_ · ✔×1
- **R-50** · El texto impreso sobre un objeto en la mano (ticket, nota) vive **sólo sobre el papel**: se enmascara con la silueta del papel medida en la foto; el dedo y la uña quedan encima — _Eli 28-09, ST 21-10: «la línea de puntitos sobresale de la uña, se solapa, eso no debería haber pasado»_ · ✔×1
- **R-51** · Cifra grande con % y OFF: **aire** entre la cifra y el bloque %/OFF, nunca se tocan (≥ 14 px en un ticket de 300 de ancho) — _Eli 28-09, ST 21-10: «el OFF está muy cerca del cero, se solapan… y el porcentaje también: que se vea mucho más armónico»_ · ✔×1
- **R-52** · El legal se tiene que **leer**: ≥ 19 px en mesa (no 14), lo más abajo que deje la zona segura (≤ 1580), en dos líneas si hace falta; cuando va al costado de un objeto, **alineado a la izquierda** — _Eli 28-09: Sunset «aumenta un poco el tamaño de los legales… en este momento no se ve nada, y en el fondo igual es un texto importante»; estacionamiento «lo de nuestro personal déjalo abajo como otra línea… alineado hacia la izquierda para que tenga más coherencia»_ · ✔×2
- **R-53** · Un logo o título blanco sobre una foto clara se **oscurece por arriba** hasta leerse limpio (Sunset: velo de 820 px al 80 %) — _Eli 28-09: «Sunset QB arriba, oscurece un poco hacia arriba para que se pueda leer claro»_ · ✔×1
- **R-54** · El objeto que la mano sostiene no se ve gigante: el ticket de adelante quedó en ~326 px de ancho sobre 1080 (≈ 30 %), y van **dos** tickets en abanico, uno destacado — _Eli 28-09, ST 21-10: «está demasiado grande» (r6), «se ve muy gigante todavía… que en vez de un ticket sean dos, que ella los tenga en las manos, cosa de que uno destaque» (r7)_ · ✔×1

## 5. Excepciones

- **E-01** · El ajuste de zona segura de `reglas.yaml` (5,8 % de tinta abajo) existe porque las orgánicas aprobadas rematan al pie; **no salva una pieza de pauta** — _reglas.yaml, 17-09_
- **E-02** · La ST de AYCD de la S5 va a grilla (orgánica): el legal pudo quedar al pie. Vale para esa pieza, la siguiente se vuelve a preguntar — _Eli, 17-09: «va a grilla»_
- **E-03** · El ancho desparejo de las cifras sólo importa **apiladas** (listas de precios, horarios en columna): ahí Bell MT (0,500 em exactos) o caja alta + alineación por código. En una línea suelta no fuerces el ancho — _manual §4, 15-09_
- **E-04** · Un cambio de texto de contenido manda sobre la grilla: desde la v7 la bajada es «Los martes saben diferente en QB.», no «Los números están claros.» — _Nicolás Ávila, 23-09_
- **E-06** · Si la pieza aprobada dejaba texto fuera de la zona segura (CMR: titular a 206 y legal a 1819; Sunset: legal a 1846), la versión nueva lo sube: manda R-13 sobre R-37 — _decisión del estudio 25-09 tras el aviso de Eli; **confirmada por Eli el 28-09** al pedir el legal del Sunset «cuidando siempre los márgenes de Instagram y en caso de que se utilice paid»_
- **E-07** · R-31 (nombre nuevo por ronda) cede cuando Eli pide la carpeta limpia: se sube con el **nombre base** y lo anterior va a la **papelera**, una pieza = un archivo — _Eli 28-09, S1 de octubre: «puedes subir reemplazando la S1 de QB, de nuevo, y borra lo anterior»_. Ojo: el token del estudio (`drive.file`) sólo ve lo que subió él; la carpeta se mira con el conector de Drive antes de borrar
- **E-08** · R-37 (sobre la aprobada, sólo cambian foto y textos) **cede** cuando Eli pide parecerse a la referencia: en los bancos se cambió la tipografía del titular y el fondo, y se mantuvieron marco, pastilla, cajas, curva, 20 % y logos — _Eli 28-09: «la tipografía puede ser la del título principal igual a la referencia. Lo demás queda tal cual. Puedes cambiar la imagen del fondo»_
- **E-05** · «LA LEY DE ELI» de DT (en DT sólo diseño, el brief no se toca) **no** se da por extendida a QB — _manual; sin confirmar_

## 6. Lo que se aprueba a la primera

- **A-01** · El bloque de AYCD tal como el KV, con sólo la foto nueva — _ST AYCD junio y septiembre 2026, aprobadas por el cliente (referencia en `raw/hilton/qb/aprobadas/`)_
- **A-02** · Logo como palabra + pastilla verde con el horario + legal chico centrado — _`Post n°2 QB SUNSET`, aprobado_
- **A-03** · Foto a sangre oscurecida arriba y abajo, titular de dos pesos y franja verde a sangre al pie — _`ST n°2 S3 QB`, aprobada_
- **A-04** · Medir el canto real del chasis por tono y ajustar la silueta: «Mejoró mucho la máscara de capa» — _ST AYCD S5 ronda 5, Eli 21-09 (con un ajuste pendiente arriba a la derecha)_
- **A-05** · Close friends: manos brindando semicenital, de noche, con una nota de papel escrita en Brushwell — _ST 23-10, Eli 25-09: «me parece bastante bien» (único ajuste: estrellas verdes)_
- **A-06** · ST n°2 S1 oct (AYCD 06-10): el bloque del KV con foto nueva — _Eli 28-09: «la veo perfecta»_. Primera pieza del estudio para QB con visto explícito de Eli
- **A-07** · ST 14-10 Adivina, como «Guess the Destination»: «ADIVINA EL» en Raleway ExtraBold + «trago» en Brushwell grande, las pistas en una pastilla blanca, las 4 alternativas del cliente — _Eli 28-09: «está sumamente bien… ese quedó ok», a la primera (r4)_
- **A-08** · Banco de Chile con el titular de la ref: «TU SEMANA TIENE MÁS DE UN» en Raleway Light + «buen momento» en Brushwell + «EN QB», sobre la plantilla aprobada — _Eli 28-09: «me parece que está bien, déjala así», a la primera (r4)_
- **A-09** · El ticket de estacionamiento **lo diseñó Eli** (`raw/hilton/qb/ref-oct/R-21-ticket-eli-28sep.png`): flechas, código de barras, «P» en recuadro, TICKET / ESTACIONAMIENTO, 50 grande con %/OFF apilado, tinta gris verdosa. Es la plantilla de ticket de QB — _Eli 28-09: «el ticket tiene que ser exactamente como el que realicé yo»_
- ⚠️ Del cliente todavía no hay «aprobado» explícito para ninguna pieza del estudio; la v6 y la v7 de la S5 no tienen veredicto escrito.

## 7. Lo que se rechaza

- **X-01** · Ejecutar un comentario tachado: se sacó el celular, que era el centro del brief — _ST AYCD S5, ronda 1, 17-09, 1 ronda perdida_
- **X-02** · Celular chico y textos de la pantalla ilegibles («El celular necesito que aumente», «no aumentaste el tamaño») — _ST AYCD S5, rondas 3–4, 2 rondas_
- **X-03** · Encuadrar con `transform: scale()`: textos y filo del recorte reventados — _ST AYCD S5, rondas 3–4, 2 rondas_
- **X-04** · Un mate dibujado desde una forma ideal (más grande o más chico que el teléfono): la letra se corta en el aire o pisa el chasis — _ST AYCD S5, rondas 3, 4 y 5, 3 rondas_
- **X-05** · Pegar la gráfica sin perspectiva (paralelogramo en vez de trapecio) y sin reflejo: «se ve como calcomanía» — _ST AYCD S5, ronda 6, 21-09, 1 ronda_
- **X-06** · Filo verde de croma alrededor de la pantalla (~13.000 px) — _ST AYCD S5, rondas 1–5, cazado en la ronda 6_
- **X-08** · Foto sobregradada (brillo/saturación en código sobre un fotograma): «se ve como quemado, muy saturado» — _ST 01-10 Banco de Chile, Eli 25-09, 1 ronda_
- **X-09** · Rehacer desde cero una promo que ya tiene pieza aprobada: «no se parece a nada a la ya aprobada» — _ST 09-10 Sunset, Eli 25-09, 1 ronda_ (y las dos de banco, que tampoco usaban los diseños aprobados)
- **X-10** · Trabajadores del hotel en la escena social — _ST 26-10 Terraza (clip nanvo8519), Eli 25-09, 1 ronda_
- **X-11** · Tres familias en una historia y alternativas presentadas como formulario (cajas con letras A/B/C): «se ve un poco feo» — _ST 14-10, Eli 25-09, 1 ronda_
- **X-12** · (interno) Borrar el texto de una pieza aprobada con inpainting de OpenCV: sobre el bokeh deja manchas y la sombra del texto deja las letras fantasma. El fondo limpio estaba en el PDF de la promo — _09-10, 25-09, cazado antes de entregar_
- **X-13** · Sobre una pieza aprobada, aproximar a ojo lo que la aprobada tenía medido: «¡Todos los días!» recto y girado en vez de en curva, el 20 % 15 % más chico y con cifras de estilo antiguo — _ST n°4 S1 oct (CMR), Eli 28-09: «se ve muy desordenado… se ve muy mal», 1 ronda_
- **X-14** · Cifras de estilo antiguo en las cajas de descuento (2 y 0 chicos, 3 bajo la línea) — _ST n°1 S1 oct (Banco de Chile), Eli 28-09, 1 ronda_
- **X-15** · Historias que no se parecen a su referencia (sólo el mood, sin su tipografía ni su recurso gráfico) — _las 11 de octubre r3, Eli 28-09: «no se asemeja a lo que vimos», 1 ronda para toda la grilla_
- **X-16** · Fondo genérico que no es QB: una **playa** detrás del Sunset (r4–r5), un bar genérico en la CMR (r4), la mesa del plato como fondo del ticket en vez de la mano (r5) — _Eli 28-09, 1–2 rondas por pieza_
- **X-17** · Dejar que la IA cambie un trago real: sangría genérica (r4), copa con otra forma y el pie estirado (r6), pie grueso con nudo (r7) — _ST 06-10 AYCD, Eli 28-09, 3 rondas_
- **X-18** · El ticket del 21-10: sobre la mesa y sin mano (r5), gigante (r6 y r7), tinta sobre la uña (r6), OFF y % pegados al 0 (r7) — _Eli 28-09, 4 rondas_
- **X-19** · Legal a 14 px en mesa: «no se ve nada» — _ST 09-10 Sunset r5, Eli 28-09, 1 ronda_
- **X-07** · (interno) Estática en el frame 239 porque lo decía la cabecera: la estática y el video mostraban las bandas en lugares distintos — _v7, 23-09, cazado antes de entregar_

## 8. Preguntas abiertas

- ¿Cómo van las cifras: caja alta en Raleway, Bell MT o según el caso? (`adn/cifras-comparacion.png`) → **Eli**.
- ¿De dónde sale **PANTONE 361 C**, que el `.ai` declara y es más brillante que los dos extremos del degradado? → Eli.
- La v6 (21-09) y la v7 (23-09) de la ST de AYCD no tienen veredicto escrito → Eli.
- ¿La regla «el brief es de contenido» (DT, Piso 18) vale también para QB? → Eli.
- ¿Qué quiso decir «las promos no son sólo de bancos»? ¿Hay legales obligatorios de alcohol? ¿El CTA de CoverManager es fijo? → Eli.
- ~~Octubre: premio del 14-10 y alternativas~~ → resuelto 25-09: el cliente sacó el premio y fijó las alternativas.
- ¿Las fotos de «Hotel general sesión SEP 2026» (`117N-uJjrMSwWj_4Y2cSIH4IwsmMkapQM`) sirven para QB o son sólo del hotel? → Eli.
- ¿Un garzón sirviendo (no posando) también cuenta como «trabajador» en cuadro? Por precaución se sacó de la 26 → Eli.
- E-06 (subir el texto de una aprobada a la zona segura): ¿de acuerdo? → Eli.
- ~~Créditos de Magnific agotados~~ → resuelto 28-09: hay créditos (el Sunset ya tiene la gente desenfocada). Falta la mano con tenedor de la 22: `qb-oct-clips.py` usa Kling 2.1, que falla → pasarlo a 2.5 Pro → **estudio**.
- ~~«VIDEO QB TERRAZA 2025» no baja~~ → resuelto 25-09: es la carpeta CAM (245 clips S-Log3). Sigue faltando el logo vectorial de QB y del Banco de Chile (hoy se usa el recorte de la aprobada) → Eli.
- Las bandas de UNLIMITED quedaron sólo arriba: ¿se quiere tipografía también abajo? (obliga a rehacer la escena) → Eli.
- No hay ninguna pieza **rechazada** en disco: los topes del QA no prueban que atrapen lo malo → estudio.

- ~~FEED 05-10: ¿qué formato?~~ → resuelto 28-09: pasó a OK y se hizo **post estático 4:5**, como pide el comentario del cliente.
- Post cumpleaños: el brief dice «Cuenta separadas» (va literal): ¿«Cuentas separadas»? → **contenido**. Y ¿con qué número se entrega el post de la S1 (`Post n°1 S1 QB OCT 26`)? → **Eli**
- La ref del 22-10 (reel de Instagram) ya no carga: ¿hay otra? → **Eli**
- El carrusel de bancos pasó a **CMR Falabella 40 % sábados + 30 % débito** (Banco de Chile salió) y el cliente lo pidió para S2. Cuando pase a OK va sobre la pieza CMR aprobada (R-37). Ojo: el brief lo sigue rotulando «SLIDE 2 — BANCO DE CHILE» y no trae slide 3 → contenido

- Las 8 casillas APROBADO nuevas de STORIES (5 «ST APROBADA», 3 «ST BANCO FALABELLA» CMR 40 %) no traen brief: ¿se republican las aprobadas tal cual o hay que prepararlas con fecha/foto nueva? → **Eli**
- La Ensalada animada está dos veces en STORIES (19-10 y una sin fecha, mismo brief): ¿es un duplicado o son dos publicaciones? → contenido

## 9. Registro de cosechas

### 2026-09-28 (noche) — Claude con Eli · rondas 4 a 8: las historias acercadas a su referencia + post cumpleaños 05-10
- **Reglas nuevas (Eli, verbatim en la fuente):** R-46 (parecerse a la ref en elementos concretos) · R-47 (fondo QB real; si se genera, desde una foto real de QB) · R-48 (un trago real no cambia de forma) · R-49 (copas en fila con el borde a la misma altura) · R-50 (la tinta sólo sobre el papel, la uña encima) · R-51 (aire entre la cifra y el %/OFF) · R-52 (legal legible, ≥ 19, a la izquierda si va al costado) · R-53 (oscurecer arriba para leer el logo) · R-54 (el objeto en la mano no gigante; dos tickets).
- **✔ que suben:** R-13 (×5) · R-26 (×3) · R-37 (×3, CMR aprobada) · R-39 (×2).
- **Aprobadas:** Banco de Chile (A-08), 14 Adivina (A-07), 08 CMR, 09 Sunset; 15 «me parece bien». **El ticket de Eli es la plantilla (A-09)**.
- **Excepción nueva:** E-08 (R-37 cede cuando se pide parecerse a la ref). **E-06 confirmada** por Eli.
- **Rechazos:** X-15 a X-19; lo que más rondas costó fue el ticket (4) y la sangría (3).
- §8: 2 resueltas (créditos, formato del 05-10) y 3 nuevas.

### 2026-09-28 (tarde) — Claude con Eli · ronda 3 de la S1 de octubre + relectura de la grilla
- **Feedback de Eli, 4 historias de la S1:** n°1 cifras rectas (R-11 ✔×2, X-14) · n°2 «perfecta» (A-06, R-04 ✔×3) · n°4 curva y 20 % como el original (R-37 ✔×2, X-13) · n°5 más parecida a la referencia (R-37) y bajada más grande con las ff separadas (**R-45 nueva**).
- Grilla: R-32 ✔×6 (nada en CAMBIADO se tocó), R-44 ✔×2 (columnas corridas otra vez). R-31 cumplida: v3 con nombre nuevo.
- §8: 2 preguntas nuevas (las 8 APROBADO sin brief, la Ensalada duplicada).
- **E-07 nueva:** Eli pidió subir la S1 reemplazando y borrando lo anterior; la carpeta queda con un archivo por pieza, con el nombre base.

### 2026-09-28 — Claude con Eli · `/al-dia hilton`, foco S1 de octubre (sin piezas)
- **Reglas nuevas del cliente (grilla, verbatim):** R-42 (carrusel con G1 limpia y la promo después) y R-43 (story simple, la info principal de inmediato). R-44 sale del diff: la pieza se busca por título.
- ✔ sube: R-32 (×5), no se diseñó nada en CAMBIADO.
- Sin feedback de Eli. §8: 2 preguntas nuevas (formato del 05-10 y carrusel CMR).

### 2026-09-26 — Claude nocturno (nube) · revisión de rutina, sin sesiones nuevas
- sin aprendizajes nuevos: los 3 commits de ayer (2fe1995, e7e3f76, adead40) ya están cosechados en las entradas de abajo (5 reglas nuevas y 4 rechazos de la ronda de Eli sobre octubre; bitácora del `/arranque` en Windows; relectura de la grilla, sin piezas). El único que `pendientes` marcó (adead40) es el mismo que hizo la última cosecha del día.

### 2026-09-25 (noche) — Claude con Eli · relectura de la grilla de octubre, sin piezas
- **Sin aprendizajes nuevos:** no se diseñó nada. Las 11 historias OK PARA DISEÑAR siguen siendo las mismas ya entregadas; feed entero CAMBIADO o PENDIENTE POR CLIENTE, orgánicos EN REVISIÓN o pendientes.

### 2026-09-25 — Claude con Eli · `/arranque` de la máquina
- sin aprendizajes nuevos: la sesión fue sólo diagnóstico, sin piezas ni feedback. Anotado en la bitácora el `09-sunset-canva.jpg` roto (no se usa).

### 2026-09-25 — Claude con Eli · octubre: ronda del cliente en la 14 y ronda de Eli sobre lo subido
- nuevo **R-37** (promo con aprobada → se hace sobre la aprobada), **R-38** (sólo Raleway + Bell de acento), **R-39** (sin trabajadores del hotel), **R-40** (foto sin sobregradar; shooting de la carta enero 2026), **R-41** (alternativas del sticker literales, sin ✅).
- ✔ sube: R-07 (×2), R-13 (×4), R-26 (×2), R-27 (×3), R-30 (×2), R-32 (×4). R-31 marcada: **se incumplió** hoy.
- nuevo **E-06** (la zona segura manda sobre la aprobada), **A-05** (Close friends, «bastante bien»), **X-08…X-12** (cuatro rondas de Eli + un error interno cazado).
- §2: `CAMBIADO` = vuelve a revisión, no se diseña. §8: 2 preguntas resueltas, 3 nuevas.

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-36** · destilados de `CLAUDE.md` (§1–§8), `reglas.yaml` v1, `marca.json` y 8 entradas de bitácora (15 al 24-09).
- nuevo **E-01…E-05**, **A-01…A-04**, **X-01…X-07** · la mayor parte sale de las 7 versiones de la ST de AYCD de la S5.
- ✔×N contados sobre la bitácora: R-31 (4 subidas con nombre nuevo), R-13 y R-32 (3 veces cada una).
- Contradicciones anotadas, no resueltas: `marca.json` dice pipeline «falta» e identidad «parcial» y el manual dice «existe» y «medida»; el manual cuenta 8 reglas de QA y la v7 pasa 9; la cabecera de `src/QbEntry.tsx` dice `--frame=239` y la entrega va en el frame 0; `CHECKLIST-CLIENTE.md` (15-09) sigue pidiendo el verde y las tipografías, ya resueltos.
- Fuera de alcance: no se leyó `clients/hilton/`; no hay notas de memoria con «qb» en el nombre.
