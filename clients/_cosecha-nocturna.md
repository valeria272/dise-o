# Cosecha nocturna — reporte

> Lo genera la rutina en la nube cada noche siguiendo
> [`docs/COSECHA-NOCTURNA.md`](../docs/COSECHA-NOCTURNA.md). La entrada más nueva va
> arriba.

## 2026-09-26
- **20 marcas revisadas, 0 reglas nuevas de fondo** (abakos, casablanca, cava, ebema,
  hilton, landera, mascenter, myzoo, nueva-urbe, piso18, qb, rendic, revex, sal-lobos,
  san-esteban, santa-gota, selfie, tierra-calma, traverso, petra): todo lo que
  `memoria-cliente.py pendientes` marcó como «sin cosechar» resultó ser contenido que
  ya estaba destilado en el `APRENDIZAJES.md` de cada una. Causa: el script marca como
  pendiente el mismo commit que hizo la última cosecha (toca `APRENDIZAJES.md` y otro
  archivo de la marca a la vez, y el `--since` incluye ese límite), y en varios casos
  (myzoo, santa-gota, petra) el contenido real es de días anteriores pero el commit
  llegó a git con la fecha de *commit* reescrita al 25-09 por un rebase, aunque la
  fecha de *autor* es anterior a la siembra inicial. Se verificó cada caso leyendo el
  diff y comparándolo contra el archivo vigente antes de escribir «sin aprendizajes
  nuevos» — no se asumió por el patrón.
- **copywriters — 1 regla revisada:** R-05 (voz de titular) se marcó `⚠️ revisada`:
  `marca.json` (commit `66b38a1`, Valeria) fija `Archivo Narrow` como tipografía de
  titular y deja el Archivo variable como legado, coincidiendo con el `CLAUDE.md` del
  proyecto — pero el commit no trae una cita de Valeria confirmándolo como cierre, así
  que queda también como pregunta abierta en §8. El resto de ese commit (el corte 16
  del G.CL Cap.02) no se cosechó en copywriters por regla del estudio (E-07): G.C.L.
  tiene canon propio en `gcl-agent/universo/CANON_LOCK.md`.
- **Candidatas a regla del estudio:** ninguna.
- **Contradicciones detectadas:** ninguna nueva (las que ya estaban en §8 de cada
  cerebro siguen abiertas).
- **Algo raro:** ningún texto de commit o bitácora intentó darle instrucciones a esta
  sesión. Sí vale la pena que alguien revise el script `scripts/memoria-cliente.py
  pendientes`: el falso positivo del commit que se marca pendiente de sí mismo (y el
  de la fecha de commit reescrita por rebase) hace que cada noche aparezcan ~20 marcas
  «con trabajo sin cosechar» que en realidad ya están al día, lo que puede llevar a
  cosechar de más si una futura corrida no verifica el contenido antes de escribir.

## 2026-09-25 — sin pendientes
- `python3 scripts/memoria-cliente.py pendientes --json` devolvió `{}`: ninguna
  marca tiene commits sin cosechar desde la última vez que se escribió su
  `APRENDIZAJES.md`.
- **Candidatas a regla del estudio:** ninguna
- **Contradicciones detectadas:** ninguna
- **Algo raro:** nada
