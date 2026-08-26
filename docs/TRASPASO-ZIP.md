# Traspaso del estudio por ZIP — qué viaja y qué no

> Verificado el **25-08-2026** empaquetando y desempaquetando de verdad.
> ZIP liviano: **7,2 MB comprimido / 15 MB en disco**.

## Cómo se hace

```bash
# En el Mac de Valeria
bash scripts/empaquetar.sh              # liviano (~7 MB) — el recomendado
bash scripts/empaquetar.sh --completo   # + fotos y videos pesados (~470 MB)
```
Deja `~/Desktop/ESTUDIO-COPYLAB-<fecha>.zip`. El diseñador lo descomprime en
`~/copylab/`, abre la carpeta en VSCode, corre `claude` y escribe `/arranque`.

---

## ✅ Lo que SÍ viaja en el ZIP

| Qué | Por qué importa |
|---|---|
| `clients/` — manuales, fichas `marca.json`, checklists, sistema EBEMA completo | **Es el activo.** Todo el criterio de marca acumulado |
| `src/` — kits de marca, composiciones Remotion, componentes | El código de producción |
| `docs/` — método, onboarding, estado de marcas, este archivo | Cómo se trabaja |
| `scripts/` — pipelines, doctor, empaquetado | Las herramientas |
| `.claude/commands/` — `/pieza`, `/qa`, `/marca-nueva`, `/arranque` | La interfaz del diseñador |
| **30 fuentes OFL** + todos los logos oficiales | El núcleo sin el cual no renderiza nada |
| `CLAUDE.md` y `LEEME-PRIMERO.md` | Claude se autoconfigura al abrir la conversación |

## ⛔ Lo que NO viaja — y qué hacer con cada cosa

| Qué | Por qué | Solución |
|---|---|---|
| **Conectores MCP** (Google Drive, Meta Ads…) | Son de la **cuenta de Claude**, no del proyecto | Cada diseñador los activa en claude.ai → Settings → Connectors |
| **Credenciales** (`token.json`, `.env`) | Son secretos; el script los excluye a propósito | Se entregan por separado, o se usa el conector de Drive en vez del token |
| `raw/` (1,1 GB) y `out/` | Material del cliente y entregas | Se bajan de Drive por marca — los IDs están en cada manual |
| **331 MB de fotos y video** en `public/assets/` | Pesan y casi nunca se necesitan todos | `--completo`, o pedírselos a Claude por marca |
| **IvyOra** (Tierra Calma) | Adobe Fonts — no se empaqueta por licencia | Cada diseñador la activa en su Creative Cloud. Fallback: Instrument Serif |
| **Bebas Neue Pro · Brandon Grotesque** (CAVA) | Adobe Fonts | Se activan en Creative Cloud. La Bebas Neue libre (OFL) sí viaja, como base |
| **Agrandir** (Selfie) | Fuente de pago, licencia del cliente | Pedírsela a Coni o al cliente |
| `node_modules/` | Se reconstruye | `npm install` lo hace `/arranque` |

---

## Estado real de los conectores y las claves — verificado 26-08-2026

Todo lo de esta tabla se **probó en vivo**, no se copió de una sesión anterior.

### Conectores MCP (viven en la cuenta de claude.ai, no en el repo)

| Conector | Estado | Cómo se comprobó | Para qué se usa |
|---|---|---|---|
| **Google Drive** | ✅ Vivo | Listadas las carpetas de Copywriters y las compartidas | Bajar referencias y briefs, subir entregas, leer comentarios |
| **Canva** | ✅ Vivo | Brand kit `kAF_gMI0GAg` responde | Diseño y plantillas de marca |
| **Higgsfield** | ⚠️ Conectado, **saldo 0,43 créditos** | `balance` → plan Plus activo | Personajes IA, UGC, video. **Bloqueado hasta recargar** |
| **Gmail** | ✅ Disponible | — | Feedback de clientes que llega por correo |
| **Context7** | ✅ Disponible | — | Documentación de librerías |
| Apollo · Notion · WordPress | ❌ Piden autorizar | — | Son de ventas y web, no de diseño |
| Meta Ads · Slack · Calendar · Windsor.ai | ❌ **No existen en esta sesión** | — | Estaban en la tabla vieja por error |

### Claves de API (viven en el `.env` compartido o en el HOME)

| Servicio | Estado | Dónde vive |
|---|---|---|
| **Freepik / Magnific** | ✅ **Vivo** — API responde 200 | `FREEPIK_API_KEY` en el `.env` **y** `~/.magnific_key`. Son **dos claves distintas y las dos sirven** |
| **Gemini** | ✅ Vivo — `/v1beta/models` responde 200 | `GEMINI_API_KEY` en el `.env` |
| **OpenAI** | ⚠️ Clave **válida**, pero `billing_hard_limit_reached` | `OPENAI_API_KEY` en el `.env` |

> 🔑 **Magnific es Freepik.** Freepik compró Magnific: se usa la misma API
> (`api.freepik.com`). No hay un endpoint "magnific.com" aparte que conectar.

> 💳 **OpenAI: el plan de ChatGPT NO es el mismo producto que la API.** La cuenta
> tiene los 6 modelos de imagen disponibles (`gpt-image-1`, `-mini`, `1.5`, `2`,
> `chatgpt-image-latest`), la clave autentica bien, pero toda generación muere con
> **`billing_hard_limit_reached`**. Se arregla en platform.openai.com → Settings →
> Billing → Limits, subiendo el tope y cargando saldo. Pagar ChatGPT Plus o Team
> **no** habilita la API: son dos facturas distintas.

> **No hay servidores MCP locales** (`.mcp.json` no existe, `mcpServers` global está
> vacío). Todo viene de conectores de claude.ai. Eso es bueno para el traspaso: no
> hay nada que instalar, pero **cada persona tiene que activarlos en su cuenta**.

**Mínimo para trabajar:** Google Drive (bajar material) + Freepik/Magnific (generar fondos).
Con esos dos ya se produce y se entrega.

---

## Portabilidad — lo que se arregló el 25-08-2026

Había **12 scripts con rutas quemadas** a `/Users/Vale/...` que reventaban en
cualquier otro Mac, y dependencias de `ASISTENTE PERSONAL/credentials/` que está
fuera del repo.

Ahora todos usan [`scripts/_entorno.py`](../scripts/_entorno.py), que resuelve:
- **La raíz del repo** desde la ubicación del propio archivo — nunca quemada.
- **Credenciales**, en este orden: variable `COPYLAB_TOKEN` / `COPYLAB_ENV` →
  `credentials/` dentro del repo → `../ASISTENTE PERSONAL/` (el layout de Valeria) →
  `~/copylab-work/respaldo-credenciales/`.

Es **compatible hacia atrás**: en el Mac de Valeria encuentra exactamente lo mismo
que antes. Verificado: los 16 scripts compilan y `subir-piezas-drive.py` resuelve
las mismas rutas que tenía quemadas.

```bash
~/copylab-venv/bin/python3 scripts/_entorno.py   # muestra qué encuentra en esta máquina
```

---

## Prueba de que funciona

Antes de mandarle el ZIP a alguien, la prueba honesta es descomprimirlo en otra
carpeta y correr `/arranque` ahí. Lo verificado hasta ahora:

- ✅ El ZIP no lleva ningún secreto (`.env`, `token.json`, `credentials/`)
- ✅ Lleva las 30 fuentes libres y excluye las dos de pago
- ✅ `clients/ebema/sistema/` viaja completo (CSS + fuentes + logos + generador)
- ✅ El sistema EBEMA, copiado a una carpeta limpia, genera los 34 HTML y rinde
  piezas idénticas a las aprobadas
- ⏳ **Falta:** correr `/arranque` en un Mac que no sea el de Valeria. Hasta que eso
  pase, el traspaso está probado en teoría pero no en terreno.


---

## ⚠️ Las fuentes de Adobe Fonts NO se copian al repo

Verificado el 25-08-2026: en el Mac de Valeria, Adobe Fonts sincroniza en
`~/Library/Application Support/Adobe/CoreSync/plugins/livetype/` con **nombres de
archivo ofuscados** (`.51753.otf`, `.51761.otf`…). Técnicamente se pueden leer.

**No se hace.** La licencia de Adobe Fonts es **por asiento y mientras dure la
suscripción**: permite usarlas en la máquina y embeberlas en un PDF o una imagen
exportada, **no redistribuir el archivo**. Copiarlas al repo y mandarlas en el ZIP a
cuatro diseñadores es redistribuir.

**Lo correcto:** cada diseñador las activa en su propio Creative Cloud. El repo lleva
solo fuentes libres (OFL) y las que el cliente nos licenció.

Para ver qué tiene activo una máquina:
```bash
python3 - <<'EOF'
import pathlib
from fontTools.ttLib import TTFont
lt = pathlib.Path.home()/"Library/Application Support/Adobe/CoreSync/plugins/livetype"
for f in sorted(lt.rglob("*")):
    if f.is_file():
        try:
            n={r.nameID:str(r) for r in TTFont(str(f),lazy=True)["name"].names if r.platformID==3}
            print(f"{n.get(1,'?')} — {n.get(2,'?')}")
        except Exception: pass
EOF
```
