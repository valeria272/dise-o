# COPYWRITERS · Grupo Copylab (@copywriters.cl) — lo que el estudio sabe de este cliente

> **Qué es este archivo.** El cerebro de la cuenta: lo que se aprendió de este cliente
> sesión tras sesión, destilado. La bitácora cuenta **qué pasó**; esto dice **qué
> sabemos**. Si la diseñadora que lleva la cuenta falta mañana, con esto (más el
> manual `CLAUDE.md` y `marca.json`) otra persona retoma sin llamar a nadie.
>
> **Vale SOLO para COPYWRITERS.** Nada de acá se copia a otra marca, ni a una hermana.
> Que sea la cuenta de la casa no la hace un caso especial: el criterio del feed propio
> no cruza a ningún cliente. Se alimenta en cada `/cierre` — ver `docs/MEMORIA-POR-CLIENTE.md`.
>
> ⭐ **Desde el 24-09-2026 manda `creative-system/MASTER/`.** Si otro archivo lo contradice,
> se corrige el otro archivo sin consultar. Y por encima de las reglas escritas manda la
> **lámina** `MASTER/reference/LOOK_AND_FEEL_REFERENCE.png`.
>
> ⛔ **El universo G.C.L. / personaje G no se resume acá.** Tiene canon propio con candados:
> `gcl-agent/universo/CANON_LOCK.md`. Léelo ahí antes de tocar cualquier cosa de G.
>
> Criterio: **Valeria Traverso** · Aprueba: **Valeria Traverso (aprobación final de dirección de arte, `MASTER/13`)**
> Última cosecha: **2026-09-26** · Cosechas: **2**

## 1. Quién es el cliente

Es la cuenta propia de la agencia: Copywriters · Grupo Copylab, Santiago. **No es «sólo
copy»**: es agencia de marketing digital completa (estrategia, creatividad, IA agéntica,
paid media, contenido, foco en resultados); reducirla a «le ponemos palabras…» la subvende.
El feed tiene que parecer **una agencia haciendo buena publicidad sobre marketing**, no una
agencia hablando de marketing. Territorio: EDITORIAL × PUBLICIDAD × HUMANO × EXPERIMENTAL.
Mantra: **MENOS PLANTILLA. MÁS IDEA.** Tono: agudo, juguetón, seco, ligeramente insolente,
con humor de oficio y autoironía de agencia.

## 2. Cómo trabaja

| | |
|---|---|
| Quién pide / KAM | Valeria Traverso (dirección creativa y dueña del sistema) |
| Quién aprueba (cliente) | Valeria. El 24-09 hubo además feedback de un «director creativo» que llegó por ella, en 8 rondas el mismo día |
| Por dónde llega el feedback | Directo de Valeria en la sesión (texto y referencias visuales que se guardan en `MASTER/reference/`) |
| Dónde se entrega | `out/copylab/<lote>/` + Escritorio. Producción final: `out/copylab/produccion/`, JPG q95 1080×1350 |
| Ritmo | Por lotes: primero se aprueba dirección (board), recién después se produce. Nada de pieza suelta por inercia |
| Rondas típicas | Muchas y rápidas. Casi siempre vuelve por **idea o dirección de arte**, casi nunca por técnica |

## 3. Identidad en corto

- **Paleta (cerrada 24-09, `MASTER/11`):** tinta `#080F14` · paper `#F2F4F6` · blanco `#FFFFFF` ·
  **Copy Pink `#FF2D8B`** (la firma) · coral `#FF6B3D` · violeta `#9D4EDD` (raro, experimental).
- **Voces:** titular condensado (ver R-05 y §8: la familia exacta está en discusión) ·
  DM Serif Display Italic (comentario, remate, ironía) · IBM Plex Mono (metadata, siempre chica) ·
  Inter (funcional/secundario). Fuentes en `public/assets/fonts/copywriters/`.
- **Logo:** no va por defecto. **Formato master:** feed 1080×1350; story/reel 1080×1920.
- ⛔ El crema/navy/**lime** de `src/brand/copywriters.ts` es de la **web** y no entra al feed.
- Motor en `src/brand/copylab/`; piezas en `src/compositions/copylab/`, **una pieza = un archivo**.

## 4. Reglas firmes

- **R-01** · No hay plantilla: una pieza = un archivo con su dirección de arte escrita en la cabecera; no existe composición genérica con prop `plantilla` — _Valeria, brief Creative OS v1.0, 03-09-2026; reforzado en el 4º feedback del 24-09 («no existe el look Copywriters»)_ · ✔×2
- **R-02** · Idea antes que diseño: INSIGHT → IDEA → 3 RUTAS → CONCEPTO → DA → FORMATO → COPY → IMAGEN → DISEÑO. Sin dirección aprobada no se construye — _Creative OS §9, 03-09; `MASTER/00` y `START_HERE`, 24-09_ · ✔×2
- **R-03** · Paleta cerrada de 6 colores; rosa `#FF2D8B`, coral `#FF6B3D`. Un color nuevo dominante necesita aprobación explícita — _Valeria, `MASTER/11`, 24-09 (cierra la duda #FF2D8D/#FF2D8B)_ · ✔×1
- **R-04** · El rosa es señal, no relleno: intervención, objeto, material, cinta, una palabra… o no está. Máximo 5 de cada 12 posts con rosa evidente — _Creative OS §3 (03-09); `MASTER/00` y `MASTER/09` «menos branding evidente»; 4º feedback del director, 24-09_ · ✔×3
- **R-05** · Titulares con la voz condensada y pesada; «una palabra manda, el resto acompaña». `marca.json` fijó el rol **`titular` en Archivo Narrow** (wght 400–700) el 25-09; el Archivo variable de la ronda del 24-09 queda como `impacto_legado` — _`marca.json`, commit 66b38a1, 25-09-2026; coincide con el manual del proyecto (`CLAUDE.md` raíz: «Archivo Narrow (titulares)»)_ · ✔×1 · ⚠️ revisada 2026-09-26 (ver §8: falta la cita explícita de Valeria confirmándolo como cierre definitivo, no sólo como valor de config)
- **R-06** · Máximo 3 voces tipográficas por pieza; la Mono nunca es héroe — _`MASTER/03`, 24-09; `marca.json` topes_ · ✔×2
- **R-07** · La escritura manual NO es voz: sólo intervención excepcional sobre foto, idealmente trazada a mano de verdad. Nada de manuscrita falsa como sistema — _Valeria, `MASTER/03`, 24-09_ · ✔×1
- **R-08** · El logo no va por defecto: sólo pieza institucional, cierre de reel, campaña corporativa o identificación explícita. El índice en Mono reemplaza al logo — _Creative OS §7 (lote v1: 1 de 9); `MASTER/00` y `/04`, 24-09_ · ✔×3
- **R-09** · Una anomalía fuerte por pieza; 1–2 intervenciones, cada una con razón semántica; del kit gráfico, 1 gesto por pieza (2 como excepción) — _Creative OS §5 y §8, 03-09; `MASTER/13`, 24-09_ · ✔×2
- **R-10** · Nunca inventar métricas, casos, clientes, personas del equipo ni backstage. Si falta material real: **PLACEHOLDER — NO PUBLICABLE** — _`MASTER/00`, `/07`, `/13`, 24-09; se sacó DATA «43» del board v2; el −37 % de PROOF y el +73 % de Santa Gota son de maqueta_ · ✔×3
- **R-11** · Recreaciones con IA sí, pero **declaradas** en el arte («Recreación publicitaria»); nunca se hacen pasar por hallazgo documental — _`MASTER/09`, feedback del director 24-09 (HERO2 con sello «RECREACIÓN · NO SE PUBLICA»)_ · ✔×2
- **R-12** · VISUAL MATCH TEST (30 % del QA): la pieza se pone al lado de la lámina (`qa/visual_match.py`) y se pregunta «¿podría estar en la lámina?». Si no, FAIL aunque colores y fuentes estén perfectos. `qa/motor.py` es sólo QA **técnico**: nunca decir «pasa el QA» sin decir cuál — _director creativo vía Valeria, 24-09; `MASTER/09`_ · ✔×1
- **R-13** · IMAGE-FIRST TEST: sin texto ni rosa, ¿la foto sola es de campaña? Si es sólo «correcta», vuelve a Magnific/Seedream. El diseño remata la imagen, no la rescata — _2º feedback del director, 24-09; `MASTER/09`_ · ✔×1
- **R-14** · La imagen dice A, el copy dice B, la cabeza completa C. Si el copy describe la imagen → FAIL — _7º feedback, 24-09_ · ✔×1
- **R-15** · Copy en pieza corto (2–9 palabras el hook); la explicación va al caption. Antes de diseñar se proponen 10 copies por pieza en territorios distintos y Valeria elige — _`MASTER/07`; 7º feedback 24-09 (`creative-system/FEED-12/COPY-60.md`)_ · ✔×1
- **R-16** · Antes de componer se decide **qué manda** (imagen, texto, objeto, dato o intervención: uno solo) — _8º feedback, 24-09 (`Recompuesta.tsx`)_ · ✔×1
- **R-17** · El diseño muchas veces vive **dentro** del mundo fotografiado (diario, hoja, etiqueta, letrero): ¿dónde vive la idea? → ¿qué soporte la vuelve real? → recién ahí la imagen. Si la IA escribe el texto en el objeto, la ortografía se revisa a mano — _`MASTER/13`; 3er feedback 24-09 (`Posts12.tsx`)_ · ✔×1
- **R-18** · Curaduría de grilla: máximo 2 piezas tipográficas seguidas; ningún mecanismo dos veces seguido; cada 3–4 posts, gente, trabajo o proceso real — _Creative OS §12 (03-09); `MASTER/01` y `/04`, 24-09_ · ✔×2
- **R-19** · En metáforas visuales la primera queda descartada: mínimo 5 rutas, se tachan las obvias — _Creative OS v1.1 §9, 03-09_ · ✔×1
- **R-20** · Zonas seguras: en 9:16 el margen derecho de la marca es **155 px** (Meta ocupa 115); 4:5 deja 135 px abajo — _error del cover «0:14», 03-09; `reglas.yaml`_ · ✔×1
- **R-21** · Casos de cliente: el trabajo es el héroe; la marca del cliente se respeta entera y nuestra tipografía no le gana — _`MASTER/03` y `/05`, 24-09_ · ✔×1
- **R-22** · Nunca mostrar bocetos planos para juzgar una cuenta que vive de la imagen: menos piezas, pero terminadas — _Valeria, 24-09 («¿estos son tus diseños finales?!»)_ · ✔×1
- **R-23** · Firma de cierre aprobada: **COPYWRITERS** + bajada cursiva «estrategia, creatividad y resultados.» — _memoria `copywriters-agency-positioning` (Valeria)_ · ✔×1

## 5. Excepciones

- **E-01** · Pieza 100 % rosa: legítima cuando el concepto la pide (TYPE LAB), una cada 12–15; ahí no hay intervención a mano (sobre rosa no existe). `reglas.yaml` la exime por nombre (`*typelab*`, `*rosa-total*`) — _brief v1.0 §3, 03-09_
- **E-02** · Caveat, Archivo variable como titular v1 y el rosa `#FF2D8D` siguen en piezas ya entregadas (v1, gcl, traverso) **a propósito**: no se retocan — _Valeria, 24-09_
- **E-03** · `src/brand/gcl.tokens.json` y `GclPost.tsx` (deprecado) no se tocan: los lee `AGENTE SOCIAL MEDIA` en producción — _Creative OS, 03-09_
- **E-04** · Margen 80 px es punto de partida, no retícula: una pieza puede sangrar y el titular puede cortarse fuera del lienzo — _Creative OS §6; `MASTER/09`, 24-09_
- **E-05** · Mundo cliente y mundo calle (NADIE LO FIRMÓ): color real cuando es identidad del cliente o parte del hallazgo, aunque rompa el B/N+rosa — _`MASTER/13`, 24-09_
- **E-06** · NADIE LO FIRMÓ usa sólo carteles **reales** fotografiados; Magnific sólo revela/amplía, nunca inventa un cartel «encontrado» — _board v2, 24-09_
- **E-07** · G.C.L. es la familia 06 del sistema, pero su canon es propio: `gcl-agent/universo/CANON_LOCK.md` — _CLAUDE.md del estudio_

## 6. Lo que se aprueba a la primera

- **A-01** · La identidad v1 (paleta, voces, metadata, tratamiento editorial, B/N, rosa como intervención) se aprobó tal cual y no se rediseña — _lote v1, 13 stills, 03-09-2026_
- **A-02** · Board de 16 posts aprobado como dirección oficial (`MASTER/reference/CREATIVE_DIRECTION_BOARD_APROBADO_24-09.png`); aprobados como dirección 01 02 04 07 09 11 12 — _24-09-2026_
- **A-03** · «LA GOMA», primera pieza del pack nuevo: `ESCRIBIMOS CON LA GOMA.` + *(la de borrar)* + mono «LO QUE SACAMOS / TAMBIÉN ES TRABAJO.»; en el feed, versión **macro sin cara** — _`CL-Goma`, 24-09_
- **A-04** · Copies elegidos por Valeria: «Nadie lee el diario. Tú acabas de leer esto.» · «Lo anotamos.» · «Este texto tenía tres párrafos.» · «mejor no.» · «Mejor esto que otro "somos líderes".» · «Amén.» — _`Recompuesta.tsx`, 24-09_
- **A-05** · El texto dentro del objeto fotografiado (diario, hoja arrugada, hoja rosa en la impresora) funcionó mejor que el texto encima — _grilla de 12 posts, 3er feedback 24-09_

## 7. Lo que se rechaza

- **X-01** · La misma fórmula en serie: condensada + remate serif rosa + fondo negro (7 de 9 piezas) — _lote v1, 03-09; «no es de diseño, es de amplitud creativa»; costó la capa v1.1_
- **X-02** · Cumplir el manual y perder la dirección de arte: HERO v1 (titular arriba, serif rosa abajo, mono al pie) pasaba `motor.py` y no el QA creativo — _24-09, 1ª ronda_
- **X-03** · Variaciones de sistema en vez de posts («ejercicio de escuela de diseño»); lo propio era «muy plano» — _24-09, 3ª ronda_
- **X-04** · El «look Copywriters»: foto + negro + rosa + Narrow + grano también es plantilla — _24-09, 4ª ronda_
- **X-05** · Copy que describe la imagen («¿Y si lo vende una monja?», «DELETE» sobre la tecla Delete) — _24-09, 7ª ronda_
- **X-06** · Foto full bleed + Archivo enorme + B/N + texto cortado: «brutalista, duro, masculino, uniforme» — _24-09, 8ª ronda; reset en `Recompuesta.tsx`_
- **X-07** · Grilla con bocetos de formas planas presentada como diseño — _24-09_
- **X-08** · Damero claro/oscuro en la grilla; relleno sin idea («El punto final», «Ronda 4») — _board v2, 24-09_
- **X-09** · La Goma con cara: la cara pesaba más que la goma. Mystic pone lápiz rosado en vez de goma y pinta uñas → Seedream 5 Pro, o se edita la buena con Nano Banana Pro — _`CL-Goma`, 24-09, 4 rondas_
- **X-10** · Estética Claude/SaaS: cards redondeadas, glassmorphism, dashboards, cerebros IA, robots, circuitos, degradados tech — _`MASTER/00` y `/08`, 24-09_
- **X-11** · Remate rosa sobre gris medio (ilegible a tamaño feed); cifra de PROOF desbordada 15 px; lámina de carrusel que se salía (se arregla **reescribiendo el copy**, no bajando el cuerpo) — _lote v1, 03-09_

## 8. Preguntas abiertas

- **¿Qué familia titula de verdad?** (Valeria) `MASTER/03` cerró Archivo Narrow Bold; la ronda
  tipográfica del mismo día pasó a Archivo variable 900; `MASTER/13` pide una grotesk condensada
  de Adobe (recomendación del estudio: Trade Gothic Next Condensed Heavy; falta Acumin Pro Extra
  Condensed) y las Adobe no se ven en Chrome si no están activadas en el sistema. El 25-09
  (commit 66b38a1) `marca.json` pasó a declarar `titular: Archivo Narrow` y dejó el Archivo
  variable como `impacto_legado` — apunta a que se resolvió en Narrow, pero el commit no trae
  una cita de Valeria confirmándolo como cierre (sólo cambió el archivo de config). Confirmar.
- **Escritura real del equipo** (plumón negro y rosado, digitalizada): mientras no exista, la manuscrita es placeholder (Valeria / equipo).
- **La agencia no tiene fotografía propia versionada.** PEOPLE y buena parte de WORK dependen de eso; el post 10 se fotografía al equipo real (Valeria).
- Post 05 «2,29 MM»: **dato sin verificar**. No se publica sin fuente (Valeria).
- Post 04 Traverso: son cuadros reales del reel «Los de siempre» (personajes IA sobre packshots). ¿El cliente aprobó ese reel? (Valeria / KAM de Traverso).
- Post 08 (Santa Gota): el director lo pidió sin copy y la ronda tipográfica con titular; hay dos versiones. ¿Cuál va? ¿Y hay autorización del cliente para usarlo como caso? (Valeria).
- Posts 03, 05, 10, 14 y 15 por rehacer; el 03 lleva afiches en inglés que hay que cambiar en la final.
- Copy del reel SEÑAL («NO ES TU PRODUCTO. / Es cómo lo dices.») lo propuso el estudio, no un brief: ¿queda? (Valeria).
- Migrar `AGENTE SOCIAL MEDIA` fuera de `GclPost` (deprecado): decisión pendiente de Valeria.

## 9. Registro de cosechas

### 2026-09-26 — Claude nocturno (nube) · sesión de Valeria Traverso (66b38a1)
- corrige **R-05** · `marca.json` fija `titular: Archivo Narrow`, deja el Archivo variable como `impacto_legado` y Caveat como `mano_legado_no_es_voz` — coincide con el `CLAUDE.md` del proyecto. ⚠️ marcada revisada porque el commit no trae la cita de Valeria confirmándolo, sólo el cambio de config; sigue en §8 como pregunta.
- fuera de alcance a propósito: el mismo commit (66b38a1) trae el corte 16 del G.CL Cap.02 «Turno de noche» (25 planos, música, 8 elementos eliminados por feedback de Valeria) y ajustes de Santa Gota y Petra — no se cosecha acá por **E-07**: G.C.L. tiene canon propio (`gcl-agent/universo/CANON_LOCK.md`) y Santa Gota/Petra son marcas aparte con su propio cerebro.
- el resto del commit (paleta `#FF2D8B`/`#FF6B3D` en `marca.json` y `reglas.yaml`) ya estaba cosechado como **R-03** desde la siembra inicial; sólo alcanzó al archivo de config, no es aprendizaje nuevo.

### 2026-09-25 — Claude (siembra inicial) · destilado del manual, la bitácora y el feedback histórico
- nuevo **R-01…R-23** · sembradas desde `clients/copywriters/` (CLAUDE.md, BITACORA.md, reglas.yaml, marca.json), el Creative OS v1.1 y el pack `creative-system/MASTER/` del 24-09, que manda.
- nuevo **X-01…X-11** · las 8 rondas del 24-09 (memorias `copywriters-la-lamina-manda` y `copywriters-pack-marca-24-09-goma`) más los errores del lote v1 del 03-09.
- corrige **R-03** · el rosa es `#FF2D8B` y el coral `#FF6B3D` (MASTER/11); `#FF2D8D`/`#FF683D` quedan sólo en piezas viejas.
- abierto · la familia del titular tiene tres versiones distintas en el MASTER (ver §8); R-05 refleja lo que está en código hoy.
- G.C.L. queda fuera a propósito: remite a `CANON_LOCK.md`.
