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
> Última cosecha: **2026-09-25** · Cosechas: **1**

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
| Ritmo | Grilla mensual; sólo se diseña lo que está `OK PARA DISEÑAR` |
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
- **R-04** · ALL YOU CAN DRINK es un bloque cerrado igual al KV: sólo cambia la foto; logo, nombre, botón con degradado y «TODOS LOS MARTES / POR $13.990 / 18:00 a 21:00 hrs» no se tocan — _Eli, 17-09: «botón verde con efecto de degradado y logo + el nombre no»; medido igual al píxel en las ST de junio y septiembre_ · ✔×2
- **R-05** · Se escribe «ALL YOU CAN DRINK», en versales («ALL» y «DRINK» ExtraBold, «YOU» y «CAN» itálica) — _Eli, 17-09; reglas.yaml `aycd-grafia`_ · ✔×1
- **R-06** · Se escribe «Sunset QB»: «Sunset» en Brushwell, enlazado con el logotipo — _Eli 15-09; medido en `Post n°2 QB SUNSET`; reglas.yaml `sunset-grafia`_ · ✔×1
- **R-07** · En una promo con KV, el KV gana a la redacción del brief; del brief se toma literal sólo lo que el KV no cubre — _ST AYCD 28-09, S5, 17-09_ · ✔×1
- **R-08** · El botón lleva el degradado horizontal (oscuro en bordes, claro al centro) y esquinas vivas — _barrido de `PROMOS QB 2026 AYCD 2026 ST.png`, 17-09; Eli lo declaró intocable_ · ✔×1
- **R-09** · El logotipo hace de **palabra** en la frase («MEJOR PAYA DE **QB**», «*Sunset* QB»), no de firma en la esquina — _medido en `ST n°2 S3 QB` y `Post n°2 QB SUNSET`, 15-09_ · ✔×2
- **R-10** · Todo va centrado; el titular es un bloque de dos pesos del mismo cuerpo — _medido en `ST n°2 S3 QB` (una pieza), 15-09_ · ✔×1
- **R-11** · Toda cifra en Raleway lleva **cifras de caja alta (`lnum`)**; activar «tabulares» no hace nada porque `tnum` no existe — _pedido de Eli 15-09 («los números suelen verse extraños»), diagnóstico con fontTools_ · ✔×1
- **R-12** · La letra chica no tiene una sola fuente: Bell MT Italic en el post de Sunset, Raleway Itálica en la ST de AYCD. Mira la pieza antes de elegir — _corrección del 17-09_ · ✔×1
- **R-13** · Antes de diagramar se pregunta **«¿esta va a paid?»**; si sí o hay duda, el texto va dentro de la zona segura (250 / 340 / 115 px en 9:16) — _Eli, 15-09: «El texto es importante que no pueda ir fuera del margen»_ · ✔×3
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
- **R-26** · Todo material que no sea real (generado o montado con IA) lleva «Imagen referencial» abajo — _cliente, grilla de octubre (STORIES 22-10), leído 24-09_ · ✔×1
- **R-27** · No se genera lo que ya está fotografiado: la fuente son las sesiones propias, y del video se saca la foto, la historia, el reel y el post en movimiento — _Eli, 15-09; aplicado en octubre con las sesiones en video, 24-09_ · ✔×2
- **R-28** · El material iPhone 4K HLG se tonemapea a 709 antes de usarlo (`qb-oct-fotogramas.py`) — _grilla de octubre, 24-09_ · ✔×1
- **R-29** · Las promos se mantienen en el tiempo: una vigente no se da por vencida sola, se confirma con Eli — _Eli, 15-09_ · ✔×1
- **R-30** · Ni títulos ni bajadas llevan punto (final ni intermedio), aunque el brief lo traiga — _regla del cliente Hilton, 23-09-2026, citada en el manual de QB_ · ✔×1
- **R-31** · Al corregir en Drive se sube con **nombre nuevo** (v4, v5…): la vista previa de Drive queda cacheada al reemplazar por el mismo ID — _17-09, Eli «no veo el cambio»; repetido en v5, v6 y v7_ · ✔×4
- **R-32** · Sólo se diseña lo que está `OK PARA DISEÑAR`; `PENDIENTE POR CLIENTE` no se toca — _bitácora 17-09, 21-09, 24-09 (Trivia de brindis, Reel DJ)_ · ✔×3
- **R-33** · No se entrega con menos bitrate que lo aprobado (la S5 salió a crf 10 para igualar 4.484 kb/s) — _ronda 5, 21-09_ · ✔×1
- **R-34** · Un negro saturado que el QA lee como «foto estirada» se arregla con grano de película sutil (±2), no bajando la foto con una franja negra lisa — _octubre, 24-09_ · ✔×1
- **R-35** · El video de octubre se rinde a 2,5× y se baja a 2250×4000 con lanczos (2,0833× da alto no entero) — _`scripts/qb-oct-render.sh`, 24-09_ · ✔×1
- **R-36** · Bell MT y Brushwell son licencia del cliente: no se reusan en otra marca — _manual §4_ · ✔×1

## 5. Excepciones

- **E-01** · El ajuste de zona segura de `reglas.yaml` (5,8 % de tinta abajo) existe porque las orgánicas aprobadas rematan al pie; **no salva una pieza de pauta** — _reglas.yaml, 17-09_
- **E-02** · La ST de AYCD de la S5 va a grilla (orgánica): el legal pudo quedar al pie. Vale para esa pieza, la siguiente se vuelve a preguntar — _Eli, 17-09: «va a grilla»_
- **E-03** · El ancho desparejo de las cifras sólo importa **apiladas** (listas de precios, horarios en columna): ahí Bell MT (0,500 em exactos) o caja alta + alineación por código. En una línea suelta no fuerces el ancho — _manual §4, 15-09_
- **E-04** · Un cambio de texto de contenido manda sobre la grilla: desde la v7 la bajada es «Los martes saben diferente en QB.», no «Los números están claros.» — _Nicolás Ávila, 23-09_
- **E-05** · «LA LEY DE ELI» de DT (en DT sólo diseño, el brief no se toca) **no** se da por extendida a QB — _manual; sin confirmar_

## 6. Lo que se aprueba a la primera

- **A-01** · El bloque de AYCD tal como el KV, con sólo la foto nueva — _ST AYCD junio y septiembre 2026, aprobadas por el cliente (referencia en `raw/hilton/qb/aprobadas/`)_
- **A-02** · Logo como palabra + pastilla verde con el horario + legal chico centrado — _`Post n°2 QB SUNSET`, aprobado_
- **A-03** · Foto a sangre oscurecida arriba y abajo, titular de dos pesos y franja verde a sangre al pie — _`ST n°2 S3 QB`, aprobada_
- **A-04** · Medir el canto real del chasis por tono y ajustar la silueta: «Mejoró mucho la máscara de capa» — _ST AYCD S5 ronda 5, Eli 21-09 (con un ajuste pendiente arriba a la derecha)_
- ⚠️ Todavía **ninguna pieza del estudio** para QB tiene un «aprobado» explícito: la v6 y la v7 no tienen veredicto escrito.

## 7. Lo que se rechaza

- **X-01** · Ejecutar un comentario tachado: se sacó el celular, que era el centro del brief — _ST AYCD S5, ronda 1, 17-09, 1 ronda perdida_
- **X-02** · Celular chico y textos de la pantalla ilegibles («El celular necesito que aumente», «no aumentaste el tamaño») — _ST AYCD S5, rondas 3–4, 2 rondas_
- **X-03** · Encuadrar con `transform: scale()`: textos y filo del recorte reventados — _ST AYCD S5, rondas 3–4, 2 rondas_
- **X-04** · Un mate dibujado desde una forma ideal (más grande o más chico que el teléfono): la letra se corta en el aire o pisa el chasis — _ST AYCD S5, rondas 3, 4 y 5, 3 rondas_
- **X-05** · Pegar la gráfica sin perspectiva (paralelogramo en vez de trapecio) y sin reflejo: «se ve como calcomanía» — _ST AYCD S5, ronda 6, 21-09, 1 ronda_
- **X-06** · Filo verde de croma alrededor de la pantalla (~13.000 px) — _ST AYCD S5, rondas 1–5, cazado en la ronda 6_
- **X-07** · (interno) Estática en el frame 239 porque lo decía la cabecera: la estática y el video mostraban las bandas en lugares distintos — _v7, 23-09, cazado antes de entregar_

## 8. Preguntas abiertas

- ¿Cómo van las cifras: caja alta en Raleway, Bell MT o según el caso? (`adn/cifras-comparacion.png`) → **Eli**.
- ¿De dónde sale **PANTONE 361 C**, que el `.ai` declara y es más brillante que los dos extremos del degradado? → Eli.
- La v6 (21-09) y la v7 (23-09) de la ST de AYCD no tienen veredicto escrito → Eli.
- ¿La regla «el brief es de contenido» (DT, Piso 18) vale también para QB? → Eli.
- ¿Qué quiso decir «las promos no son sólo de bancos»? ¿Hay legales obligatorios de alcohol? ¿El CTA de CoverManager es fijo? → Eli.
- Octubre: el premio del 14-10 («xxxx») lo confirma Eli; las alternativas Aperol Spritz / Mimosa / Negroni se validan con contenido.
- Créditos de Magnific agotados: Sunset sin gente y la ensalada sin la mano → **Valeria**.
- «VIDEO QB TERRAZA 2025» no baja por enlace; falta el logo vectorial y versiones sobre fondo claro → Eli.
- Las bandas de UNLIMITED quedaron sólo arriba: ¿se quiere tipografía también abajo? (obliga a rehacer la escena) → Eli.
- No hay ninguna pieza **rechazada** en disco: los topes del QA no prueban que atrapen lo malo → estudio.

## 9. Registro de cosechas

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-36** · destilados de `CLAUDE.md` (§1–§8), `reglas.yaml` v1, `marca.json` y 8 entradas de bitácora (15 al 24-09).
- nuevo **E-01…E-05**, **A-01…A-04**, **X-01…X-07** · la mayor parte sale de las 7 versiones de la ST de AYCD de la S5.
- ✔×N contados sobre la bitácora: R-31 (4 subidas con nombre nuevo), R-13 y R-32 (3 veces cada una).
- Contradicciones anotadas, no resueltas: `marca.json` dice pipeline «falta» e identidad «parcial» y el manual dice «existe» y «medida»; el manual cuenta 8 reglas de QA y la v7 pasa 9; la cabecera de `src/QbEntry.tsx` dice `--frame=239` y la entrega va en el frame 0; `CHECKLIST-CLIENTE.md` (15-09) sigue pidiendo el verde y las tipografías, ya resueltos.
- Fuera de alcance: no se leyó `clients/hilton/`; no hay notas de memoria con «qb» en el nombre.
