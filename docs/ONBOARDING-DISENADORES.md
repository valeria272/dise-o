# Onboarding — cómo entra un diseñador nuevo al estudio

> Objetivo: que un diseñador con su propio Mac, su VSCode y su cuenta de Claude
> produzca una pieza de cliente **el mismo día**, sin llamar a nadie.
> Tiempo estimado: 40 minutos, de los cuales 30 son descargas.

---

## Paso 1 — Instalar lo que hace falta (una vez)

```bash
# Node 20+ (recomendado 24 LTS)
node --version || brew install node

# Google Chrome (el render de gráficas lo usa headless)
ls "/Applications/Google Chrome.app" || brew install --cask google-chrome

# Python 3 (para los scripts de Drive y de imagen)
python3 --version
```

## Paso 2 — Clonar el estudio

```bash
mkdir -p ~/copylab && cd ~/copylab
git clone https://github.com/valeria272/dise-o.git "EDITOR VIDEOS"
cd "EDITOR VIDEOS"
git checkout estudio/sistema-de-marcas   # la rama viva del estudio
npm install
npm run typecheck      # tiene que compilar
```

> ⚠️ **No lo clones dentro de `Desktop/`, `Documents/` ni `Descargas/` si tienes
> iCloud Drive activado.** iCloud "desmaterializa" los archivos que no usas y el
> repo se rompe en silencio: `node_modules` deja de leerse, Python muere con
> `Resource deadlock avoided` y los renders se cancelan solos. Ya pasó dos veces.
> Clonar en `~/copylab/` (HOME, fuera de iCloud).

## Paso 3 — Configurar Python

```bash
python3 -m venv ~/copylab-venv
~/copylab-venv/bin/python3 -m pip install --upgrade pip
~/copylab-venv/bin/python3 -m pip install pillow numpy scipy requests certifi cryptography \
    google-api-python-client google-auth google-auth-oauthlib openpyxl
```
Siempre invocarlo por ruta completa: `~/copylab-venv/bin/python3 script.py`.
**Usar `python3 -m pip`, nunca el binario `pip`** (tiene rutas quemadas y falla).

## Paso 4 — Abrir el llavero (las claves)

**No le pidas ninguna clave a nadie.** Vienen dentro del repositorio, cifradas.

```bash
python3 scripts/llavero.py abrir
```

Te pide **la contraseña del llavero del estudio** — una sola, te la da Valeria una
vez, y este computador no te la vuelve a pedir. Con eso quedan montadas la clave de
Magnific/Freepik, la de Anthropic y el token de Google para subir entregas al Drive.

```bash
python3 scripts/llavero.py estado        # qué quedó montado
python3 scripts/magnific.py check        # valida la clave SIN gastar créditos
```

Detalle completo: [`credentials/LEEME.md`](../credentials/LEEME.md).

## Paso 5 — Conectar Claude (esto sí es tuyo)

Los **conectores** son de tu cuenta de claude.ai, no del proyecto: no viajan en el
repositorio y hay que activarlos una vez por persona. Corre esto, que te da el correo
y la contraseña de las herramientas de pago:

```bash
python3 scripts/llavero.py logins
```

En claude.ai → **Settings → Connectors**:

| Conector | Con qué cuenta | Para qué |
|---|---|---|
| **Google Drive** | **tu** correo `@copywriters.cl` | Briefs, referencias, entregas. **Sin esto no se trabaja** |
| **Higgsfield** | la cuenta de la agencia (`logins` te la muestra) | Video IA |
| **Canva** | la cuenta de la agencia | Brand kit del estudio |

Drive va con **tu** cuenta porque las entregas quedan a tu nombre. Higgsfield y Canva
van con la cuenta de la agencia porque la suscripción de pago está ahí.

Después, en la terminal dentro del repo:
```bash
claude
```
Claude lee `CLAUDE.md` solo. No hay que pegarle nada.

## Paso 6 — Bajar el material ✅ (resuelto el 26-08-2026)

Al clonar recibes **todo lo que se necesita para renderizar**: el código, los 9
manuales, los 7 comandos, **56 archivos de tipografía y los 28 logos oficiales**.
`git clone` + `npm install` y el estudio funciona. No hay que pedirle nada a nadie.

Lo que **no** viene, y está bien que no venga:

| Qué | Peso | Por qué | Cómo se consigue |
|---|---|---|---|
| Fotos, packshots y video de `public/assets/` | 1,3 GB | Material de cliente, cambia todo el tiempo | Se baja por marca cuando hace falta |
| `raw/` | 10 GB | Referencias y rodajes | Idem — los IDs están en cada manual |
| `out/` | — | Entregas pasadas | No se necesita |
| **IvyOra** (Tierra Calma) | — | Adobe Fonts: la licencia es por cuenta | **Actívala** en tu Creative Cloud |
| **Agrandir** (Selfie) | — | De pago, licencia del cliente | Pídesela a Coni |
| **Neutraface** (MyZoo) | — | De pago | Pídesela al cliente |

Para saber qué te falta a ti, en tu máquina:

```bash
python3 scripts/verificar-fuentes.py       # qué tipografía falta y de dónde sacarla
python3 scripts/verificar-material.py raw  # si lo que bajaste ES lo que dice ser
bash scripts/doctor.sh                     # todo junto
```

### Bajar material de una marca

Pídeselo a Claude en el chat — el conector MCP de Drive es el único que ve las
carpetas de clientes:

```
Baja el material de referencia de EBEMA a raw/ebema/ según clients/ebema/CLAUDE.md,
verifícalo y muéstrame la hoja de contacto antes de diseñar
```

Para archivos de más de 10 MB (editables `.ai`, videos) el conector no alcanza:
```bash
python3 scripts/bajar-de-drive.py --publico "<id1>,<id2>" raw/<marca>/
```

## Paso 7 — Tu primera pieza

```
/pieza ebema
```
Claude te va a preguntar qué necesitas, va a leer el manual, el brief y las
referencias, y va a producir. **No le expliques la marca** — ya está escrita.

---

## Cómo trabajar el día a día

### El comando que usas casi siempre
```
/pieza <marca> <lo que necesitas>
```
Ejemplos reales:
- `/pieza ebema las 11 gráficas de sucursal de octubre, feed y story`
- `/pieza ebema variantes de precio A15–A20 de la hoja Briefs wsp octubre ARIEL`
- `/pieza selfie el carrusel WTF es... de la semana 2`
- `/pieza revex el post de outlet con 60% OFF`

### Los otros dos
```
/qa <ruta o marca>     ← control de calidad antes de entregar
/marca-nueva <nombre>  ← abrir el sistema de un cliente que no existe todavía
```

### Reglas de convivencia

1. **Todos trabajan en la MISMA rama** (`estudio/sistema-de-marcas`), con dos ritos
   diarios: **`/abrir <marca>`** al empezar (trae lo de los demás y te dice dónde
   quedó el cliente) y **`/cierre <marca>`** al terminar (sube tu día para que otro
   pueda retomarlo mañana). El protocolo completo, incluido el relevo entre
   diseñadores, está en [`TRABAJO-EN-EQUIPO.md`](TRABAJO-EN-EQUIPO.md).
   ⛔ Ya no se crean ramas por persona — aislaban el trabajo y mataban el relevo.
2. **Nunca subas `raw/` ni `out/`** — están en `.gitignore` por algo.
3. **Cuando el cliente corrija algo, se codifica.** Si Paulina dice "el logo va
   pegado arriba", eso se escribe en `clients/ebema/CLAUDE.md` en el mismo commit.
   El manual es la memoria del estudio: lo que no está escrito, se vuelve a equivocar.
4. **No edites `base.css` para una pieza puntual.** Si de verdad falta algo en el
   sistema, se agrega al CSS **y** se documenta en el manual.
5. **QA antes de mostrar.** Una pieza que no pasó el checklist de su marca no existe.

---

## Lo que NO tienes que hacer

- No hay que explicarle la marca a Claude en cada chat. Está en `clients/<marca>/`.
- No hay que decidir colores ni tipografías. Están medidos.
- No hay que inventar textos ni CTAs. Salen del brief, literales.
- No hay que preguntar qué formato. Está en `marca.json`.

Si te encuentras haciendo alguna de esas cuatro cosas, el sistema de esa marca está
incompleto → revisa `docs/ESTADO-MARCAS.md` y avisa.

---

## Problemas conocidos

| Síntoma | Causa | Solución |
|---|---|---|
| `Resource deadlock avoided` al correr Python | El repo está dentro de iCloud | Mover a `~/copylab/` |
| El render de Remotion falla con "requiere macOS 15" | Headless Shell incompatible | `npx remotion render ... --browser-executable "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"` |
| `render.sh` no genera nada | Chrome no está en la ruta estándar | Editar la variable `CHROME` del script |
| Los archivos aparecen vacíos o en gris | iCloud los evictó | Reiniciar el Mac y esperar a que rematerialice — **no reconstruir a mano** |
| SSL falla en scripts Python | Bug conocido de Python en macOS | El script debe usar `certifi`; todos los nuestros ya lo hacen |
| Drive no baja un archivo | El token tiene scope `drive.file` (sólo archivos propios) | Pedir el archivo directo o que lo muevan a una carpeta compartida |
| Archivos >10 MB no bajan por el conector | Límite del MCP | `curl -sL "https://drive.google.com/uc?export=download&id=<ID>"` si es link-shared |
