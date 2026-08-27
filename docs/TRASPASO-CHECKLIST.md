# Traspaso del estudio a un diseñador — checklist ejecutable

> Para el traspaso del **lunes 31-08-2026**. Dos partes: lo que Valeria deja listo
> **antes** (sin esto el lunes se pierde en pivoteos), y lo que el diseñador hace
> en su máquina **el día 1**, en orden, con la prueba que confirma cada paso.
>
> **¿Se necesita VPS? NO.** El estudio corre 100 % local: VSCode + Claude Code +
> Node + Chrome en el Mac del diseñador. El VPS (187.127.50.136) es de COPYLAB OS
> y no tiene nada que ver con esto. Lo único "remoto" que el estudio usa es el
> repo de GitHub y el Drive de la agencia.

---

## Parte A — Valeria, ANTES del lunes (≈30 min)

| # | Qué | Cómo | Listo |
|---|---|---|---|
| A1 | **Push del repo al día** | `git push` en la rama `estudio/sistema-de-marcas`. Sin esto ella clona una versión vieja sin el QA ni la semilla de memoria | ☐ |
| A2 | **Invitarla al repo privado** | github.com/valeria272/dise-o → Settings → Collaborators → su cuenta de GitHub (si no tiene, que se cree una con el correo @copywriters.cl). El repo es privado: sin invitación no puede clonar | ☐ |
| A3 | **Cuenta de Claude con plan pago** | ✅ Resuelto 28-08: Valeria compró **Max 200** — capacidad de sobra para el uso intensivo de diseño. Definir con qué login entra cada diseñador (ideal: un login por persona, para que la memoria y las sesiones no se mezclen) | ☑ |
| A4 | **Permisos de Drive con SU cuenta** | Su cuenta @copywriters.cl necesita ver: la carpeta AGENCIA COPYWRITERS (`16kNWE2mkbLh1uTb5Jc5TuDhYwM0OOw0A`), las carpetas de las diseñadoras (Coni/Eli) y las carpetas de entrega por cliente. Probar ANTES: que abra 2–3 links de los manuales desde su navegador | ☐ |
| A5 | **Adobe Creative Cloud** | Ella necesita licencia para activar **Futura PT** (Casablanca) e **IvyOra** (Tierra Calma). Si no tiene CC, los fallbacks del repo funcionan pero el calce tipográfico baja | ☐ |
| A6 | **Clave de Freepik/Magnific** | Los scripts de imagen leen `FREEPIK_API_KEY`. Decidir: ¿se le comparte la clave `claudecw` o se crea una propia? Entregar por canal seguro (no por el repo, no por WhatsApp) | ☐ |
| A7 | **Fuentes de pago que no viajan** | Agrandir (Selfie) → pedirla a Coni. Neutraface (MyZoo) → cliente. Stag LCG (DT) → confirmar licencia. Solo si va a tocar esas marcas la semana 1 | ☐ |

---

## Parte B — El diseñador, día 1, en orden

### B1 · Instalar (15 min, la mitad es descarga)

```bash
# 1. Herramientas base (verificar; instalar lo que falte)
node --version        # necesita 20+ — si falta: brew install node
ls "/Applications/Google Chrome.app"   # si falta: brew install --cask google-chrome
git --version

# 2. Clonar FUERA de iCloud — esto no es negociable
mkdir -p ~/copylab && cd ~/copylab
git clone https://github.com/valeria272/dise-o.git "EDITOR VIDEOS"
cd "EDITOR VIDEOS"
git checkout estudio/sistema-de-marcas
npm install
```

> ⛔ **Jamás clonar en Desktop/Documents/Descargas con iCloud Drive activo.**
> iCloud desmaterializa archivos y el estudio muere en silencio (pasó dos veces:
> 19 días de crons caídos una, el repo entero evictado la otra). `~/copylab/` está
> fuera de iCloud.

**VSCode:** abrir la carpeta `~/copylab/EDITOR VIDEOS` e instalar la extensión
**Claude Code** (o usar `claude` en la terminal integrada — da lo mismo, es el
mismo agente).

### B2 · Conectores en SU cuenta de claude.ai

Los conectores viven en la cuenta, no en el repo — **hay que activarlos una vez**
en claude.ai → Settings → Connectors, y después **abrir un chat/sesión nueva**
(un conector activado a mitad de sesión no carga).

| Conector | ¿Obligatorio? | Para qué | Prueba de que funciona |
|---|---|---|---|
| **Google Drive** | 🔴 SÍ — sin esto no hay estudio | Bajar referencias y briefs, subir entregas, leer comentarios de clientes | Pedirle a Claude: «busca la carpeta AGENCIA COPYWRITERS en Drive» |
| **Canva** | 🟡 Recomendado | Plantillas y diseño de apoyo | «lista mis brand kits de Canva» — debe aparecer `kAF_gMI0GAg` |
| **Gmail** | 🟡 Recomendado | El feedback de clientes llega por correo | «busca correos de linkedin.com» o similar |
| **Higgsfield** | ⚪ Opcional | UGC/video IA — hoy sin créditos, no bloquea | — |
| Apollo / Notion / WordPress | ⚪ NO activar | Son de ventas y web, no de diseño | — |

> Meta Ads, Slack y Calendar **no existen como conectores de este flujo** — si
> alguien los menciona, es una tabla vieja.

### B3 · Arranque asistido — lo hace Claude, no ella

En la terminal, dentro del repo:

```bash
claude
```

y escribir **`/arranque`**. Claude instala lo que falte, **siembra la memoria del
estudio** (las 56 notas de aprendizaje — sin esto arranca amnésico), verifica el
conector de Drive, revisa tipografías y corre el doctor. Si algo depende de ella
(Chrome, un permiso), se lo pide con la instrucción exacta.

Verificación manual del paso más importante del traspaso:

```bash
bash scripts/sembrar-memoria.sh
# debe decir: ✓ Memoria sembrada … 56+ notas
```

### B4 · Diagnóstico completo

```bash
bash scripts/doctor.sh
```

Todo ✓ o con ▲ explicado. Cualquier ✗ se resuelve antes de seguir.

### B5 · La prueba de fuego (30 min) — sin esto el traspaso NO está hecho

Reproducir una pieza real de la marca de referencia, de punta a punta:

1. En Claude: **`/pieza ebema <algo simple de la grilla vigente>`** — o rehacer
   una pieza ya aprobada de `clients/ebema/`.
2. Renderizar (Claude sabe cómo; usa el Chrome del sistema).
3. Correr la compuerta de calidad:
   ```bash
   ~/copylab-venv/bin/python3 qa/motor.py --marca casablanca out/casablanca/sep2026/*.png
   ```
   (con las piezas que existan de la marca que tocó — el punto es ver el QA
   bloquear/aprobar con las citas de la diseñadora del cliente en pantalla).

**Criterio de éxito del día 1:** una pieza rendida + el QA corrido + ella entendió
que el feedback de cada cliente vive en `clients/<marca>/` y que el QA no se salta.

### B6 · Lo que tiene que leer (en este orden, ~40 min)

1. [`LEEME-PRIMERO.md`](../LEEME-PRIMERO.md) — el mapa
2. [`docs/SISTEMA-DE-MARCAS.md`](SISTEMA-DE-MARCAS.md) — **la ley** del estudio
3. [`docs/FLUJO-MENSUAL.md`](FLUJO-MENSUAL.md) — cómo se corre un mes
4. [`qa/README.md`](../qa/README.md) — la compuerta de calidad y por qué no se salta
5. El manual de la marca que le toque: `clients/<marca>/CLAUDE.md`

---

## Qué viaja y qué no — para que nadie busque lo que no está

| | Viaja con el clon | Cómo se consigue lo que no |
|---|---|---|
| Manuales, fichas, reglas de QA, kits, componentes, comandos | ✅ | — |
| **Memoria del estudio** (56 notas) | ✅ vía `docs/memoria-semilla/` + siembra | `bash scripts/sembrar-memoria.sh` |
| Fuentes OFL + logos oficiales (núcleo) | ✅ (~18 MB en git) | — |
| Fotos/packshots/video de `public/assets/` (~330 MB) | ⛔ | Se bajan por marca desde Drive (IDs en cada manual) |
| `raw/` (referencias, ~10 GB) y `out/` (entregas) | ⛔ | Ídem — y `verificar-material.py` antes de diseñar |
| Conectores MCP | ⛔ (son de la cuenta) | B2 |
| Credenciales (`FREEPIK_API_KEY`, tokens) | ⛔ (a propósito) | A6, por canal seguro |
| Fuentes Adobe/de pago | ⛔ (licencia por cuenta) | A5 / A7 |
| Historial de chats de Claude de Valeria | ⛔ (imposible e innecesario) | El aprendizaje ya está destilado en manuales + memoria-semilla |

---

## Los 3 errores que van a pasar si no se siguen los pasos

1. **Clonar dentro de iCloud** → todo funciona dos días y muere en silencio. B1.
2. **Saltarse la siembra de memoria** → Claude amnésico repite errores que
   costaron rondas enteras (Brushwell, compuerta de material, render en Mac). B3.
3. **Trabajar sin el conector de Drive activo** → diseña a ciegas sin referencias,
   que es exactamente lo que produjo el desastre Revex/Casablanca del 25-08. B2.
