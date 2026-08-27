---
name: el-render-vuelve-al-repo
description: "Si una pieza se rindió, su código y sus fondos se commitean el MISMO día — Revex rehizo 3 rondas de cero porque los scripts vivían sólo en el working tree"
metadata:
  type: feedback
---

# El código que rindió una entrega vuelve al repo el mismo día

Si una pieza salió y se entregó, **su script y su material se commitean ese día**.
No al cerrar el mes, no cuando alguien lo pida.

**Why:** Revex septiembre se rehízo **tres veces desde cero** por esto (27-08-2026).
Los scripts existían sólo en el working tree; lo commiteado era una corrida vieja con
`FEED = (2250, 2250)` — un formato cuadrado **que nunca se entregó a nadie**. Serena, con
el repo al día, no podía reproducir ninguna de las tres rondas y concluyó —con razón— que
"el script del repo sólo hace cuadrado". Cada ronda de correcciones partía en blanco.

El riesgo se dispara cuando se rinde en un sandbox fuera de iCloud (`~/copylab-work/...`,
ver [[icloud-repo-evictado]]): el trabajo queda lejos del repo y es fácil no devolverlo.
El sandbox **no** es una bifurcación — es una copia; no hay nada que "traer de vuelta"
salvo el commit.

**How to apply:**

1. Entregaste una pieza → `git status` en `scripts/`. Lo modificado **y lo untracked**
   (`??` es el caso que más se escapa: `revex-temuco-showroom.py` nunca estuvo trackeado).
2. **Versiona también los fondos.** El código sin su material no reproduce nada:
   `public/assets/**` está ignorado salvo fuentes y `logo*.png`, así que las fotos de la
   grilla necesitan una excepción explícita y comentada en el `.gitignore`
   (patrón: `!public/assets/<marca>/<mes>/**`). 29 MB por marca-mes es barato al lado de
   rehacer una ronda.
3. **Prueba antes de decir que quedó reproducible.** Corre el script y compara con `cmp`
   contra lo entregado. En Revex las 8 piezas salieron byte a byte idénticas — eso es la
   prueba, no el diff.
4. Cuando alguien reporte "no puedo reproducir esto", **compara el working tree con lo
   commiteado antes de buscar otra máquina**. Casi siempre es un commit que falta, no
   código perdido.
5. Verifica las medidas en los archivos entregados (`Image.open(f).size`), no en lo que
   dice el script ni en lo que recuerda la gente. En Revex las medidas que circulaban por
   chat estaban malas y se perseguía un formato que nunca existió.

Lo que no se commiteó **se pierde**: la v1 de Revex a 1080×1350 no está en ningún commit
y no se recupera.

Relacionado: [[revex-sep2026-estado]], [[icloud-repo-evictado]],
[[no-inventar-sistema-de-marca]], [[traspaso-zip-estudio]].
