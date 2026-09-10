## 2026-09-09 — Valeria Traverso (con Claude)

**Qué se hizo:** Reel de bienvenida «Los de siempre» de punta a punta, en dos vueltas. (1) Versión
inicial con la línea 350 g y anatomía humanoide, montada y rendida (26 s) — sirvió para probar el
pipeline. (2) Brief final: canon 450 g (Mostaza Suave · Mostaza Tradicional · Ketchup), anatomía
de corpóreo, CHARACTER LOCK aprobado tras tres rondas (hombros bajo el anillo, smoking largo que
cubre toda la etiqueta, camisa y corbatín en todas las vistas), sets, 18 keyframes, paquete de
edición «THE ENTRANCE» (timeline sobre beats medidos, lista de clips, transiciones, sound design),
15 clips con Kling y montaje coreografiado en Remotion. Copy final del cierre: «AHORA TAMBIÉN EN
NUESTRA MESA.» (decisión de Valeria).
**Dónde quedó:** biblia `clients/traverso/reel-los-de-siempre/BIBLIA-v2.md` + paquete
`EDICION-THE-ENTRANCE.md`; masters en `public/assets/traverso/lds2/casting/LOCKED/`; keyframes y
sets en `lds2/keyframes`, `lds2/sets` (JPEG en git, PNG local); clips en `lds2/clips` (local, no
viajan); composición `src/compositions/traverso/LosDeSiempreEntrance.tsx` (`TraversoEntrance`);
render `out/traverso/lds2/los-de-siempre-THE-ENTRANCE-v1.mp4` y copia en el Escritorio.
Generadores: `scripts/traverso-lds2-keyframes.py`, `-clips.py`, `-musica.py`.
**Ronda 2 (22:30), feedback de Valeria sobre el v1 → v2 rendida** (`out/traverso/lds2/los-de-siempre-THE-ENTRANCE-v2.mp4`,
composición `TraversoEntranceV2`, 25 s): hook «Ya se supo...» a máquina con pulso grave y CLACKs con micro
push-in; textos que entran por golpe y salen por corte; en la oficina UNA sola sentada (entran como
rockstars → corte a la mesa), sin «Primera reunión»; cierre con texto a máquina «Traverso. Los de
siempre, ahora también en nuestra mesa. Bienvenidos a Grupo CopyLab.» y el logo animado de Copylab
(el punto que viaja, adaptado de GclOrigenReel). Música nueva «drama teleserie» (`v2-drama.mp3`,
golpe en 9,2 s); alternativas en el Escritorio (A drama · B runway · C la de la v1). Se cambia con
la constante `MUSICA` y el `DROP` de la composición.
**Ronda 3 (22:45), feedback frame a frame de Valeria → V3** (`out/traverso/lds2/los-de-siempre-THE-ENTRANCE-v3.mp4`,
`TraversoEntranceV3`, 23 s). Regla: «no más escenas, más dirección en los segundos que hay» → cero
clips nuevos. Microhook tráiler 0–2 s (CLACK/CLACK/TAC/BOOM, cortes de 0,4 s, «Ya se supo...» chico
sobre imagen, nunca sobre negro); tres personalidades a tres escalas por recorte; sin pantalla negra
antes del reveal (microvacío de audio de 4 f); reveal con bass hit + impacto de cámara + push-in que
frena; triple product porn de 0,4 s; puerta → sobreexposición → ventana; wipe → ya sentados con
«Primera reunión / Cero presentaciones»; end card de 2,5 s y hard cut. **Banda sonora EDITADA para la
película** (`scripts/traverso-lds2-banda.py` → `audio/banda-v3.mp3`): tramos de las pistas
generadas cortados al mapa musical (tensión → groove con golpes en 3/4,5/6/7,5 → microvacío →
DROP 9,75 → riser → groove suave en la reunión → HIT 22,4 → corte 23,0) + foley encima.
**Ronda 4 (22:50), nueva dirección musical → test de rutas sobre 12 s:** `out/traverso/lds2/RUTA-A-12s.mp4`
(garage/indie desde el primer beat) y `RUTA-B-12s.mp4` (cuerdas italianas 0–1,64 s que se rompen en garage
en el BOOM). Misma garage original (`audio/rutas/A-garage-1.mp3`, 130 bpm) cortada a sus golpes medidos con
`scripts/beatmap.py`; vacío de música 9,02–9,52 y DROP en 9,52. Documento `reel-los-de-siempre/EDICION-RUTAS-MUSICALES.md`.
Composición `LosDeSiempreTestRutas.tsx`. Cero clips nuevos. **Decisión pendiente de Valeria: ruta A o B.**
**Ronda 5 (23:05), decisión: RUTA B híbrida → V4 definitiva** (`out/traverso/lds2/los-de-siempre-THE-ENTRANCE-v4-rutaB.mp4`,
`TraversoEntranceV4`, 22,5 s). Banda `audio/banda-v4.mp3` armada con `scripts/traverso-lds2-banda-v4.py`:
cuerdas italianas sólo 0–1,3 s (falsa expectativa, −5 dB) → QUIEBRE con la garage entrando en su golpe →
vacío 8,66–9,18 sobre el bache natural → DROP 9,18 = reveal → tres golpes 11,94/12,38/12,86 = product
porn → parada natural 14,16–14,66 + riser → hit 15,16 = luz de la puerta → 17,66–20,0 la banda «da un
paso atrás» (pasa-bajos 900 Hz, −7 dB) para el deadpan → vuelve 20,0 → HIT 21,66 → corte 22,5.
Todos los cortes del montaje están sobre esos eventos medidos. Cero clips nuevos.
**Ronda 6 (23:12), V4 no aprobada → V5 de montaje y storytelling** (`out/traverso/lds2/los-de-siempre-V5.mp4`,
`TraversoV5`, 22,5 s). UNA sola canción de punta a punta (`audio/banda-v5.mp3` = la garage desde 1,52 s,
único vacío 9,1–9,5); con ese offset los baches y golpes naturales caen donde la historia los pide
(breakdown antes del reveal, parada al cruzar la puerta, bajón en la reunión, HIT final 21,94).
Historia única: llegan → los descubrimos (Suave → whip → Tradicional → whip → Ketchup → vuelta al trío
en el hit) → reveal → match cut a GRUPO COPYLAB → cruzan, Ketchup tapa la lente → ya sentados →
end card. Fuera el product porn y toda caminata dentro de la oficina. Test sin textos/audio: pasa.
**Qué sigue:** que Valeria ESCUCHE el v1 (pista y mezcla cuadradas por envolvente, no de oído) y
decida si la música original se queda o se licencia una; ajustar niveles de SFX; subir clips y
render al Drive de Traverso; si se aprueba, versión 1:1 para feed.
**Abierto:** foto del corpóreo real de Traverso (el brief la nombra, nunca llegó); packshots en
alta del resto del catálogo (los del sitio salen de `r.bolder.run/4093/original/`); decisión de
música licenciada vs. original.
