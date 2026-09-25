# G.CL — CAP.02 · TURNO DE NOCHE · GUION V3 «MAÑANA LO VEO»

> **Valeria, 25-09-2026, después de ver el corte 2.** «Fome, le falta dinamismo, ganchos y punch.»
> Sustituye el final del `GUION_V2_PRIMERA_VERSION.md` (Marta salvando con la V1 queda fuera).
> Composición: `src/compositions/gcl/Cap02TurnoDeNocheV3.tsx` (`GclCap02TurnoDeNocheV3`).

## Lo que cambió y por qué
- **El post-it es un pedido del cliente** («URGENTE · pedido del cliente: ajustar campaña · ENTREGA 09:00»)
  y **Pancho escribe debajo, en lápiz azul, «mañana lo veo, 9 AM :)»** antes de irse. Es el chiste que
  arma todo el capítulo: el irresponsable lo va a ver a la hora de la entrega.
- **El canal entre pisos es un TUBO NEUMÁTICO** (vidrio y bronce, luces rosadas por piso): baja el
  pedido, sube el trabajo al amanecer, vuelve a bajar la respuesta. Se entiende que los mensajes viajan.
- **Marta imprime el mismo mensaje que bajó** (con la línea de Pancho incluida), en perspectiva sobre
  el papel. Los textos sobre superficies se trackean (`scripts/seguir-plano.py`), no se pegan planos.
- **Gin escribe a las 21:20** y la notificación es un golpe: «¿Puede ser más **WOW**?».
- **La carpeta MÁS WOW 2019 detona una revelación**: G se sienta a pensar, un rayo baja del techo,
  aparece **el robot dios** y le entran los códigos al cerebro. Después trabaja a full.
- **El caos es rápido**: cortes de 8–14 frames, el reloj corre de 21:40 a 05:58.
- **El final**: 09:00, Pancho envía desde su correo, el cliente responde «¡Gracias! Volvemos a la
  versión anterior», Pancho lo reenvía hacia abajo y **G y su equipo explotan**. Fin.
- **Cierre de serie como el CAP.01**: «Departamento de cosas imposibles.» + PRÓXIMO CAPÍTULO
  «Batalla campal: G vs humanos».

## La secuencia (30 fps)
| Beat | Planos | Qué pasa |
|---|---|---|
| HOOK | P01 · N01 · P02 | 18:59. Post-it del cliente. La mano de Pancho escribe en azul. CLAC, se va |
| EL TUBO ▼ | N02 · N03 · P04 | La cápsula baja cinco pisos. Cae junto a Marta. Marta lo imprime. «mm.» |
| OH NO / G HERO | P05 · P06 · P07 | Rolo en crisis. Halo: entra la música. G lo calma |
| V1 | P08a · P08b · P08c | COPY · DISEÑO · V1 ✓ (20:10 → 21:15) |
| 21:20 DING | P09 | «¿Puede ser más WOW? 🙏» en grande. La música se corta |
| MÁS WOW | P10 · P11a | Marta saca la carpeta. MÁS WOW · 2019, trackeado |
| REVELACIÓN | N04 · N05 · N06 · N07 | G piensa · rayo del techo · robot dios · le entran los códigos. Vuelve la música |
| CAOS | N08 · N09 · P08b · P20 · P19 · P12 | G teclea a full, Rolo en círculos, papeles, tokens 24→3 %. Reloj corriendo |
| AMANECER ▲ | N10 · N02 al revés · N11 | G manda la cápsula. Sube. Llega al escritorio: «Todo listo. Revisar ✓» 06:47 |
| 09:00 | P17 · correo · respuesta | Pancho llega, ENVIAR. DING: «¡Gracias! Volvemos a la versión anterior 🙏». REENVIAR ↓. La música muere |
| BOOM | N02 · P16 · N13 · N14 | Baja. G ✕✕. Explotan. Los tres tiznados, humo, chispa del halo |
| CIERRE | — | Departamento de cosas imposibles. · Grupo CopyLab · PRÓXIMO CAPÍTULO: Batalla campal: G vs humanos |

## Música
Temporal (catálogo de HeyGen, generada por IA, sin derechos de terceros):
`public/assets/gcl/cap02-v3/musica/temp-a-indierock.wav` (~143 BPM). Hay otras tres opciones en la
misma carpeta. **La canción definitiva se decide al final** (Valeria abrió la puerta a una con
derechos: si es así, hay que licenciarla antes de publicar).

---

## Corte 4 — feedback de Valeria sobre el corte 3 (25-09-2026)
Composición: `Cap02TurnoDeNocheV4.tsx` (`GclCap02TurnoDeNocheV4`). «Me parece mejor», con estos cambios:

| Qué | Cómo se resolvió |
|---|---|
| El post-it flotaba sobre el computador | P01 regenerado: pegado plano en la esquina superior del monitor, con la punta apenas levantada. N01 es el **mismo encuadre** con la mano que escribe |
| Pancho se para muy rápido, robótico, y «se ve muy falso» | P02 a velocidad casi natural (1,15×, 66 f) y prompt `FOTO_REAL` (piel con poros, asimetría, pliegues reales). Se generó también con Nano Banana Pro para comparar |
| La iluminación estaba mal puesta | Ahora va **antes** del trabajo: baja el mensaje → Marta «mm» → Rolo → halo → G piensa → rayo → robot dios → códigos → **entra la música** → trabajan, trabajan, trabajan → V1 ✓ |
| No repetir el «mm» | Queda **uno solo** (Marta al recibir). Tras el WOW, **G y Rolo se miran** (N15) y vuelven a trabajar rápido. Sin «mm» al final |
| El correo de respuesta mostraba otros mensajes | Sólo «¡Gracias! Mejor volvamos a la versión anterior 🙏» |
| Pancho «ok, me da lo mismo» | N16: se encoge de hombros (real, gente detrás) y aparece «Reenviar ↓ NIVEL −1» con clic |
| Más gente en la oficina de día | P17 y N16 regenerados con colegas fuera de foco detrás |
| Cierre | «COPYLAB · Departamento de cosas imposibles.» + PRÓXIMO CAPÍTULO (título **por definir con Valeria**) |
| Música con tensión | Nada en el hook · riser + coro en la iluminación · entra con los códigos · el WOW la corta · riser en la mirada · vuelve más rápida en el caos hasta el correo · el DING del cliente la mata · explosión seca |

**Próximo capítulo — opciones para elegir:** «Batalla campal: G vs humanos» (lo que se habló) ·
«La reunión que pudo ser un correo» · «El cliente tiene la razón» · «Feedback».

---

## Corte 5 — feedback de Valeria sobre el corte 4 (25-09-2026, tarde)
Composición: `Cap02TurnoDeNocheV5.tsx` (`GclCap02TurnoDeNocheV5`).

| Qué | Cómo se resolvió |
|---|---|
| El post-it «sigue sin perspectiva» (el papel se curva al despegarse) | `superficie-curva.tsx`: el texto va en 10 tiras horizontales, cada una a su cuadrilátero, sobre el perfil fila a fila del papel (`scripts/medir-postit.py` → `perfil`). Se curva con el papel |
| No se nota que Pancho escribe | `scripts/seguir-lapiz.py` sigue la punta del lápiz azul; la frase se revela letra a letra según la posición de la punta (x 668 → 790), sobre la banda inferior del papel rotado |
| «oh no, oh no, oh no no no» al entrar el URGENTE | `sfx/rolo-ohno.mp3`: voz robot (edge-tts + modulación en anillo + bitcrush), hecha en casa. El sonido viral original es de Kreepa («Oh No») y tiene derechos: **si se quiere el original, se agrega en la app al publicar** (biblioteca comercial de Reels/TikTok para cuentas de empresa) |
| Pancho «todavía robótico, muy falso» | Clip a **1× (velocidad real)** desde que cierra la tapa hasta que se para (2,2–4,7 s), cortando antes de la chaqueta. **Grano de película + viñeta** sobre todos los planos con humanos (`Grano`). Kling volvió a fallar en cola; queda Hailuo |
| Alargar el trabajo con gags entre G y su equipo | 4 planos nuevos intercalados: **N17** Rolo trae un tubo de pósters que no era → G facepalm · **N18** discuten frente al panel · **N19** Marta inunda de papel a Rolo · **N20** choque de puños. El bloque pasa de 2,9 s a 6,7 s con la música arriba |
| Gin llega cuando están terminando; se estresan y vuelven a correr | DING sobre V1 ✓ → G y Rolo se miran → **Rolo en pánico (P05)** → riser → caos |
| Finalmente descansan y mandan | **P22** (los tres reventados, sin halo, 05:59) antes de que G mande la cápsula |
| Cierre después de la explosión | **N21**: G apagado (✕✕) y tiznado; Rolo le pega un post-it en el visor que dice **«mañana lo veo, 9 AM :)»** — el chiste de Pancho, devuelto |
| Música con más gancho | `temp-g-hype140.wav` (house punchy 140 BPM con build a los 6 s): entra con los códigos y el drop cae sobre el trabajo; vuelve tras el estrés; baja en el amanecer; el DING la mata |

**Música con derechos:** no se puede descargar desde acá. Dos caminos legales: (a) Reels/TikTok con
cuenta de empresa → «Sonidos comerciales» en la app al publicar (el trend se agrega ahí, sobre el
video ya editado); (b) licencia en Epidemic Sound / Artlist y se monta acá. Lo temporal es IA sin
derechos de terceros.

---

## Corte 6 — feedback de Valeria sobre el corte 5 (25-09-2026, tarde)
Composición: `Cap02TurnoDeNocheV6.tsx` (`GclCap02TurnoDeNocheV6`), ~46 s con cierre.

| Qué | Cómo se resolvió |
|---|---|
| La voz robótica del hook «queda mal» | Fuera. El hook lleva **música de intriga** (`temp-h-tension.wav`: reloj, latido, bajo) desde el primer cuadro hasta el halo |
| Pancho escribiendo sobre el papel «no queda bien» | Fuera N01. Pancho mira el post-it, sale un **pensamiento de su cabeza** («lo veo mañana, 9 AM 😌», burbujas), cierra el computador y se va. Marta imprime sólo el pedido del cliente |
| El WOW de Gin «no se entiende quién es» | Fuera. Sin segundo DING de madrugada |
| Alargar el trabajo, más interacción, mensajes y códigos, que se lea qué hacen | Un solo bloque de ~11 s: G teclea con **códigos** corriendo en su pantalla · choque de puños (se ponen de acuerdo) · Rolo corre · COPY ✓ · facepalm con el tubo · discuten · DISEÑO ✓ · Marta archiva con **mensaje** «MARTA → G: brief archivado ✓» · inundación de papel · «ROLO → G: fuentes listas ✓» · «G → TODOS: export… 98 %». **HUD «NIVEL −1 · AVANCE»** con COPY / DISEÑO / EXPORT llenándose, y el reloj de 19:30 a 05:40 |
| «Versión 1 lista» no se alcanza a leer | Sello grande **V1 LISTA ✓** sostenido 1,5 s, con timbre y sting |
| Sube, llega a Pancho, descansan y celebran con café | N10 → tubo ▲ → cápsula en el escritorio («V1 lista. Revisar ✓», 06:47) → **N22**: los tres brindando con tazas de café, sin halo, 2,2 s, «TURNO TERMINADO ✓» |
| El envío y la respuesta con más tiempo | MAIL 2,8 s (se escribe, va el cursor, clic, «Enviado ✓») · RESP 2,2 s · encogimiento de hombros + Reenviar ↓ |
| Terminar en que el equipo recibe el input y explota | Tubo ▼ → la cápsula cae junto a Marta («NUEVO INPUT DEL CLIENTE») → G y Rolo se miran → riser → **explotan** → 0,9 s tiznados → cierre |

Fuera del corte: N01 (mano escribiendo), P09 (WOW), N15/P05 estrés, el caos con tokens, P22, N21 (post-it sobre G), `rolo-ohno`.

---

## Corte 7 — últimos cambios de Valeria (25-09-2026, noche)
Composición: `Cap02TurnoDeNocheV7.tsx` (`GclCap02TurnoDeNocheV7`), ~52 s con cierre.

| Qué | Cómo se resolvió |
|---|---|
| Música de principio a fin | Cuatro pistas con cross-fades: **INTRIGA** (`temp-h`) del post-it al halo · riser + coro en la iluminación · **TRABAJO** (`temp-g`, house 140 con build) de los códigos a V1 LISTA, donde muere con el sting · **DESCANSO** (`temp-j`, lo-fi dorado) mientras sube, llega, duermen y brindan · **OFICINA** (`temp-k`, comedia con pizzicato) del sorbo de Pancho al DING del cliente · silencio → riser → explosión seca → trombón «wah» → ticks del cierre |
| Pancho sólo hasta que se para, y más real | **P02b**: plano desde atrás, sobre el hombro (nuca y polera reales, el post-it en foco, casi sin cara). Corta cuando se levanta. Grano + viñeta |
| Se va a las 18:30 | Reloj: 18:30 hook · 18:33 el tubo · 18:36 halo · trabajo 19:00 → 05:40 |
| +5 s de trabajo, creativo, con pelea, tipo Pixar | **N23** brainstorm: G clava bocetos en el pinboard, Rolo de asistente con la caja de chinches, Marta imprime bocetos · **N24** pelea: tiran de la misma hoja hasta que se rompe y caen de espaldas (boing) · **N25** Rolo pinta un brochazo rosado gigante en el panel mientras G mide con regla. Mensajes: «ideas al pinboard» · «¡es mía! · ¡no, mía!» · «brochazo · milímetro» |
| Que se note que descansan | **P22** (los tres reventados, sin halo) con «zzz» flotando sobre Rolo y ronquido robot, luego el brindis (N22) |
| Cierre con dinamismo al llegar Pancho | **Match cut al sorbo**: Rolo/G sorben → Pancho sorbe. Correo con whoosh al enviar, Reenviar ↓ → whoosh y tubo a 3× → la cápsula cae → se miran → explosión con destello → **el halo se le cae a G**, rebota (clank) y trombón «wah wah» → cierre |
| SFX nuevos | trombon-wah, whoosh, boing, papel-rasga, halo-clank, sorbo, ronquido, brocha, chinche |

---

## Corte 8 — pasada final de storytelling (25-09-2026, noche) · «editar con más crueldad»
Composición: `Cap02TurnoDeNocheV8.tsx` (`GclCap02TurnoDeNocheV8`). **28,4 s de historia + 6 s de cierre de serie = 34,4 s.**
Sin generar nada nuevo: puro montaje sobre los clips ya producidos. Cada plano responde «¿la situación acaba de cambiar?».

| t | Beat | Planos | Qué pasa |
|---|---|---|---|
| 0–2,5 | HOOK | P01 · P02b | URGENTE · ajustar campaña · MAÑANA 09:00. Pancho (de espaldas) lo ve, cierra, se para. CLAC. Sin música |
| 2,5–5,3 | PROBLEMA BAJA | N02 · N03 · P04 · P05 | Tubo ▼ → Marta recibe e imprime el pedido, «mm» → Rolo en crisis |
| 5,3–7,3 | G HERO | P06 · P07 · N07 | Halo → calma a Rolo → le entran los códigos: **entra la canción** |
| 7,3–10,3 | SATISFACTION | N08 · COPY ✓ · puños · DISEÑO ✓ · **P19 ARCHIVADO · V1** · LISTO ✓ | Tres impactos y fuera. Marta archiva la V1: el plante |
| 10,3–15,2 | PRIMER GIRO | P09 · P10 · P11a · P11b · P11b-alt · Marta | DING. **Mute brutal.** «¿Puede ser más WOW?» G se congela («eh?»). Marta abre el cajón: **MÁS WOW · 2019** (trackeado). G mira la carpeta. Mira a Marta. Marta ni lo mira («mm») |
| 15,2–19,0 | ESCALADA | N09 · P20 · N24 · P12 · N09 · P20 · N19 · N08 | La canción vuelve más rápida. Rolo corre desordenado, torre, pelea por la hoja (se rompe), **tokens 24→11→3**, glitches, inundación de papel. Marta igual |
| 19,0–21,0 | FALSA VICTORIA | P13 · P14 | **APROBADO ✓**, golpe final, la música se corta. Rolo se desploma |
| 21,0–23,2 | PICO | P09 (tarde) · P16 | DING. **«Mejor volvamos a la primera versión.»** Música muerta. G ✕✕, TOKENS 1 % |
| 23,2–25,7 | RESOLUCIÓN | P21 · P11a (V1) · P06 | Marta abre el archivo y saca la **V1**. Sting deadpan. G se reenciende, risita |
| 25,7–28,4 | EPÍLOGO | P17 · P22 · negro | 09:00, Pancho abre el laptop: **FINAL_APROBADO_V1.pdf ✓**, sonríe. Corte abajo: Rolo destruido, G al 1 %, Marta imprime. TRRRR. Negro |
| 28,4–34,4 | CIERRE | — | COPYLAB · Departamento de cosas imposibles → Grupo CopyLab → PRÓXIMO CAPÍTULO |

**Fuera:** el pensamiento de Pancho, la iluminación con el robot dios (N04–N06), los gags largos (N17/N18/N23/N25), el descanso con café (N22), el correo de Pancho (MAIL/RESP/N16), la explosión (N13/N14), el tubo de subida. Todo queda producido para otros capítulos.

**Música narrativa:** sin track hasta el halo · entra con los códigos (temp-g desde 5,0 s) · mute en el DING · silencio con metal y papel · vuelve más rápida (desde 8,0 s) en la escalada · golpe y corte en APROBADO · muerta en el pico · sting en la V1 · TRRRR.

---

## Corte 9 — corrección del corte 8 (25-09-2026, noche) · «te equivocaste, revisa bien»
Composición: `Cap02TurnoDeNocheV9.tsx` (`GclCap02TurnoDeNocheV9`). **31,5 s de historia + cierre = 37,4 s.**

El corte 8 volvió a meter cosas que Valeria ya había eliminado. Revisado contra todas las decisiones anteriores:

| Lo que no iba | Corrección |
|---|---|
| El WhatsApp de **Gin** (eliminado en el corte 6: «no se entiende quién es ni de dónde viene») | Fuera. **Todo lo que dice el cliente baja por el TUBO** (candado 21) como nota en la cápsula: «CLIENTE → NIVEL −1 · ¿Puede ser más WOW? 🙏», «APROBADO ✓» y «Mejor volvamos a la primera versión.» Sin nombres, sin WhatsApp |
| Segundo «mm» de Marta en la mirada | Fuera. El único «mm» es al recibir el urgente |
| «DING» como notificación de celular | Ahora el código es la cápsula: tubo ▼ → clonk → papel |

⛔ **Regla para el futuro:** antes de montar, contrastar cada elemento con la lista de lo eliminado
(voz robot, Pancho escribiendo, Gin/WhatsApp, «una cosita más», el segundo «mm», voces humanas).
Un texto de feedback nuevo no reabre lo que ya se cerró.

---

## ⭐ Corte 10 — la línea aprobada es el CORTE 7 (25-09-2026, noche)
Valeria: «la opción que íbamos aprobando es la del corte 7». **Los cortes 8 y 9 (estructura de 30 s con MÁS WOW y
Marta salvando con la V1) quedan como registro, no como línea.** Composición: `Cap02TurnoDeNocheV10.tsx`
(`GclCap02TurnoDeNocheV10`) = corte 7 + dos cambios:

| Qué | Cómo |
|---|---|
| La versión que mandan es la **V3** (el cliente ya pide cambios sobre una versión; así «volvamos a la versión anterior» tiene sentido) | Sello **V3 LISTA ✓**, nota del tubo «V3 lista. Revisar ✓», adjunto `campaña_V3_final.pdf`, mensajes «V1 y V2 archivadas ✓» y «V3 · export… 98 %» |
| Música más potente y que conecte (la de la mañana estaba bien pero no unía; el final igual) | **Un solo tema** (`temp-g`) en cuatro estados: entero en el trabajo · **cansado** (`temp-g-cansado.wav`: pasa-bajos 900 Hz, 15 % más lento, eco; hecho con scipy porque el ffmpeg del proyecto no trae filtros de audio) en el descanso · **fresco** (`temp-g-fresco.wav`: su intro, 6 % más rápida) bajo la comedia de oficina de la mañana, que entra encima en el sorbo · su **golpe final** (`temp-g-final.wav`) como botón del cierre. Cross-fades de 12–24 f y volúmenes más arriba |

Auditoría del corte 7 contra lo eliminado: limpio (un solo «mm», sin Gin/WhatsApp, sin voz robot, sin Pancho escribiendo, sin voces humanas).

---

## ⭐⭐ Corte 11 — DEFINITIVO (25-09-2026, noche) · «me parece bien»
Composición: `Cap02TurnoDeNocheV11.tsx` (`GclCap02TurnoDeNocheV11`), **44,0 s**. = corte 10 con dos cambios:
- **+1 s al inicio** para leer el post-it (P01 de 1,1 s a 2,1 s, con el acercamiento más largo).
- **El capítulo termina cuando explotan.** Justo ahí: destello, humo, corte a negro. Sin tiznados, sin halo
  cayendo, sin trombón y **sin tarjeta de cierre de serie** (el `CierreSerie` queda disponible para otros capítulos).

## ⭐⭐ Corte 12 (25-09-2026, noche)
`Cap02TurnoDeNocheV12.tsx` (`GclCap02TurnoDeNocheV12`) = corte 11 + **la tarjeta de cierre de serie** después del negro:
los personajes terminan en la explosión; luego «COPYLAB · Departamento de cosas imposibles.» → Grupo CopyLab →
PRÓXIMO CAPÍTULO (marcador «Batalla campal: G vs humanos», por definir), con el golpe final del tema.

## ⭐⭐⭐ Corte 13 — DEFINITIVO (25-09-2026, noche) · «el último cambio»
`Cap02TurnoDeNocheV13.tsx` (`GclCap02TurnoDeNocheV13`), **47,6 s**. = corte 12 con dos cambios:
- **No se reenvía el mensaje hacia abajo.** Pancho lee el mail del cliente («¡Gracias! Mejor volvamos a la versión
  anterior») y cortamos **directo** a los tres abajo, quietos medio segundo, destello y explotan. Se da por entendido
  que ya se enteraron. Fuera: el clic «Reenviar ↓ NIVEL −1», el tubo bajando, la cápsula, «NUEVO INPUT DEL CLIENTE».
- **El cierre va sin música.** Después del negro, la tarjeta (COPYLAB · Departamento de cosas imposibles → logo →
  PRÓXIMO CAPÍTULO) suena sólo con el tecleo de la máquina. El golpe final del tema se eliminó.

Lista de lo eliminado (acumulada, no vuelve): Gin/WhatsApp · segundo «mm» · voz robótica «oh no» · Pancho escribiendo
en el papel · «una cosita más» · tiznados/halo cayendo/trombón · **reenvío hacia abajo · música en el cierre**.

## ⭐⭐ Corte 14 (25-09-2026, noche) · «música más trend, más cool»
`Cap02TurnoDeNocheV14.tsx` (`GclCap02TurnoDeNocheV14`), **47,6 s** = corte 13 con la música cambiada a
**«Reptilia» (The Strokes, instrumental)**, 157,9 BPM, cortada al beat. Pedido de Valeria con el link de YouTube
(`363EYJ3423c`); bajada con yt-dlp (cliente `android`) a `public/assets/gcl/cap02-v3/musica/temp-strokes-reptilia.wav`.

| Tramo | Reel | Canción | Qué hace |
|---|---|---|---|
| Hook + tubo | 0,6 s → 8,7 s | 0:00 (riff del bajo solo) | Tictaquea bajo el post-it, el laptop, el pensamiento, el tubo y Marta |
| Robot dios | 8,7 → 11,2 s | sigue el riff, agachado (duck 0,55) | Deja pasar el riser y el coro celestial |
| Trabajo | **T1 = 11,20 s** → sello | **10,62 s = primer bombo** | La batería entra exacto en el primer código; el riff entero empuja el montaje y muere seco con el sting «V3 LISTA» |
| Cansado | 26,7 → 33,9 s | el mismo riff a 0,78×, sin agudos, con eco (`temp-strokes-cansado.wav`) | Callback agotado mientras sube, llega, duermen y brindan |
| Mañana | sorbo de Pancho → DING | 79,55 s (reentrada de la banda tras el break) | Pancho fresco a toda máquina; el ding del cliente la mata en seco |
| Explosión + cierre | — | silencio | Riser, boom, negro, tarjeta sólo con el tecleo |

Fuera: temp-h (intriga), temp-g en sus cuatro estados y temp-k (comedia de oficina); quedan en `musica/` como registro.

⚠️ **Es un TEMP TRACK sin licencia.** Para publicar: agregar «Reptilia» desde la biblioteca de música de Instagram/TikTok
al subir el reel (si la cuenta la tiene disponible) o licenciarla; si no, reemplazar por una pista con derechos con el
mismo carácter (garage rock 155–160 BPM, riff de bajo en la intro, batería que entra tarde).

## ⭐⭐ Corte 15 (25-09-2026, noche) · «me gusta; al terminar el trabajo, bajar la música, no apagarla»
`Cap02TurnoDeNocheV15.tsx` (`GclCap02TurnoDeNocheV15`), **47,6 s** = corte 14 con un solo cambio: el riff entero
**no muere con el sting** de «V3 LISTA». Se va agachando durante 1,3 s (fade de 40 f) mientras el riff cansado entra
por debajo (fade de entrada de 34 f, desde el sello + 6 f). La música nunca se corta entre el sello y el descanso:
medido en el render, el nivel baja parejo de −15 a −22 dB sin hoyo. Todo lo demás igual al corte 14 (incluida la
advertencia del temp track sin licencia).

## ⭐⭐⭐ Corte 16 — DEFINITIVO (25-09-2026, noche)
`Cap02TurnoDeNocheV16.tsx` (`GclCap02TurnoDeNocheV16`), **45,8 s** = corte 15 con dos cambios de Valeria:
- **La canción vuelve en la tarjeta.** El ding la mata en canción ≈ 83,3 s; después de la explosión y el negro,
  retoma en el beat 83,20 s (el «turun tururun») sobre «Departamento de cosas imposibles» → logo → PRÓXIMO
  CAPÍTULO, con el tecleo encima, y cierra el reel con fade largo. (Reemplaza el «cierre sin música» del corte 13.)
- **Descanso más corto.** La nota que llega (N11) 42→32 f, «TURNO TERMINADO» (P22) 48→28 f, el café (N22) 60→36 f:
  1,8 s menos. El sorbo se movió a N22+20 para el match cut.

