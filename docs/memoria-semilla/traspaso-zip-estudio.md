---
name: traspaso-zip-estudio
description: Cómo se traspasa el estudio a otro diseñador por ZIP — qué viaja, qué no, y el resolutor de rutas portable que reemplazó las rutas quemadas
metadata:
  type: project
---

`bash scripts/empaquetar.sh` arma el ZIP de traspaso (**7,4 MB**; `--completo` suma
los 331 MB de foto y video). El diseñador lo descomprime en `~/copylab/`, abre la
carpeta en VSCode, corre `claude` y escribe **`/arranque`**.

**Verificado el 25-08-2026 de verdad:** descomprimido en carpeta limpia, `_entorno.py`
resolvió la raíz nueva, y el sistema EBEMA generó los 34 HTML y rindió las piezas
idénticas a las aprobadas. El ZIP no lleva ningún secreto.

**No viaja:** los **conectores MCP** (son de la cuenta de claude.ai, cada persona los
activa en Settings → Connectors), las credenciales, `raw/` (1,1 GB), `out/`, y las
fuentes de pago (IvyOra de Adobe Fonts, Agrandir de Selfie).

**Conectores verificados hoy:** Google Drive ✅ (el único imprescindible), Meta Ads ✅,
Context7 ✅. Gmail/Calendar/Slack/Windsor piden autorización. **Higgsfield y Canva
están desconectados** — eso bloquea los personajes IA de Abakos y el UGC.

**El arreglo que hizo esto posible:** había **12 scripts con rutas quemadas** a
`/Users/Vale/...` que reventaban en cualquier otro Mac. Ahora todos usan
`scripts/_entorno.py`, que deriva la raíz del repo desde el propio archivo y busca
credenciales en cadena (`COPYLAB_TOKEN`/`COPYLAB_ENV` → repo → monorepo →
`~/copylab-work/respaldo-credenciales/`). **Compatible hacia atrás**: en el Mac de
Valeria encuentra exactamente lo mismo que antes.

**Why:** el plan es que 4 diseñadores más produzcan desde sus propios Mac. Sin esto,
el ZIP llegaba y no corría nada.

**How to apply:** cualquier script nuevo importa de `_entorno` en vez de escribir una
ruta absoluta. `python3 scripts/_entorno.py` muestra qué encuentra en cada máquina, y
`bash scripts/doctor.sh` diagnostica la copia completa.

⏳ **Pendiente real:** correr `/arranque` en un Mac que no sea el de Valeria. Hasta
entonces el traspaso está probado en simulación, no en terreno.
