# AUDITORÍA DEL SISTEMA EXISTENTE — 03-09-2026

Antes de construir nada se revisó lo que ya había: assets, fuentes, tokens,
componentes, plantillas, generadores, scripts, prompts, imágenes, motion y
exports. Esto es el veredicto.

---

## ✅ CONSERVAR

| Qué | Dónde | Por qué |
|---|---|---|
| **El motor de QA** | `qa/motor.py` · `checks.py` · `agencia.yaml` | Infraestructura sólida: una corrida = una marca, y ninguna regla vive en el código. Se reusó tal cual y se le sumó `clients/copywriters/reglas.yaml` + un check nuevo |
| **El generador de imagen** | `scripts/magnific.py` | Mystic + Nano Banana Pro funcionando, clave viva en el llavero del repo. No hacía falta nada nuevo |
| **La biblia de G.CL** | `gcl-agent/GCL_CHARACTER_BIBLE.md` + `character-master/` | El personaje es IP propia con 5 candados de consistencia ya escritos. Pasa intacto a ser la familia 06 |
| **Tres de los seis colores** | `gcl.tokens.json` | `#080F14`, `#F2F4F6`, `#9D4EDD` coinciden exactamente con las referencias |
| **La receta de render de este Mac** | memoria `render-remotion-fix-mac` | Sandbox fuera de iCloud + Chrome del sistema. Sin esto no se renderiza nada acá |
| **El kit de la web** | `src/brand/copywriters.ts` | Crema/navy/lime **se queda para la web y la pauta**. No es basura: es otro medio |

---

## 🔧 MODIFICAR

| Qué | Problema | Qué se hizo |
|---|---|---|
| **Dos hexadecimales** | `gcl.tokens.json` dice rosado `#FF2D8B` y coral `#FF6B3D`; las referencias dicen `#FF2D8D` y `#FF683D` | Los valores correctos quedaron en `src/brand/copylab/tokens.json`. **No se tocó `gcl.tokens.json`**: lo lee `AGENTE SOCIAL MEDIA` y cambiarlo sin avisar rompería una integración viva. Queda como pendiente declarado |
| **La tipografía** | Space Grotesk + Inter: un pareo grotesk/tech correcto pero genérico, sin voz editorial ni voz humana | Cuatro voces nuevas: Archivo variable · DM Serif Display Italic · IBM Plex Mono · Caveat |
| **La firma de pieza** | `Firma` se pintaba en TODAS las piezas | Reemplazada por el **índice en mono**. El logo aparece en 1 de 9 |

---

## ❌ ELIMINAR (del sistema del feed)

Todo esto vive en `src/brand/gclUI.tsx` y `src/compositions/gcl/GclPost.tsx`, y
todo contradice el brief:

| Elemento | Por qué se va |
|---|---|
| `Halo` — orbe rosado difuso con `blur()` | Gradiente decorativo. Anti-patrón explícito |
| `AnilloLed` — 46 puntos en círculo | «Partículas». Anti-patrón explícito |
| `Pastilla` — etiqueta con `borderRadius: 6` | Chip de SaaS. El sistema usa metadata mono plana |
| `CALOR` / `PROFUNDO` — gradientes de fondo | «Gradientes morado/azul». Anti-patrón explícito |
| `Firma` obligatoria en cada pieza | Contradice §7: el logo se gana su lugar |
| **`plantilla: "statement" \| "resultado" \| "tip" \| "tendencia" \| "testimonio" \| "cultura"`** | **Esto es lo de fondo.** Seis layouts fijos con campos que se rellenan es, literalmente, la definición de lo que el brief pide no hacer |

### Cómo se ejecutó la eliminación

**Se deprecó, no se borró.** `GclPost` lo invoca
`AGENTE SOCIAL MEDIA/tools/remotion_render.py`: borrarlo hoy deja al agente
social sin poder publicar. Los archivos llevan una cabecera de DEPRECADO que
apunta al sistema nuevo, y siguen registrados en `Root.tsx` hasta que el agente
social se migre.

**Pendiente para Valeria:** decidir cuándo se migra el agente social a las
composiciones `CL-*`. Es una decisión de operación, no de diseño.

---

## Lo que la auditoría encontró de paso

- **`public/assets/fonts/` tiene 38 tipografías** de todas las marcas del estudio.
  Ninguna servía para este sistema: no había ni una condensada variable, ni una
  Didone display, ni una manuscrita de marcador. Las cuatro voces se bajaron nuevas.
- **`out/` y `raw/` estaban limpios de material de Copywriters**: la agencia no
  tenía fotografía propia versionada. Por eso la pieza PEOPLE del lote v1 usa un
  placeholder declarado y sin caras.
- **`qa/calibrar.py` ya documentaba** que `contraste_texto` no discrimina para
  Casablanca. Ese hallazgo previo ahorró el día: el mismo problema volvió a
  aparecer acá y ya estaba escrito por qué.
