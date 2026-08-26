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
git clone https://github.com/duvanchat2/editor-pro-max.git "EDITOR VIDEOS"
cd "EDITOR VIDEOS"
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
~/copylab-venv/bin/python3 -m pip install pillow requests certifi \
    google-api-python-client google-auth google-auth-oauthlib openpyxl
```
Siempre invocarlo por ruta completa: `~/copylab-venv/bin/python3 script.py`.
**Usar `python3 -m pip`, nunca el binario `pip`** (tiene rutas quemadas y falla).

## Paso 4 — Conectar Claude

En claude.ai → **Settings → Connectors**, activar **Google Drive** con la cuenta
`@copywriters.cl` que te asignen. Sin eso no puedes bajar referencias ni subir entregas.

Después, en la terminal dentro del repo:
```bash
claude
```
Claude lee `CLAUDE.md` solo. No hay que pegarle nada.

## Paso 5 — Bajar el material 🔴

**Esto es lo único que hoy no es automático, y es el punto que más fricción genera.**

Al clonar el repo recibes **el código y los manuales, pero no los assets**:

| Carpeta | Peso | ¿En git? | Qué pasa si falta |
|---|---|---|---|
| `public/assets/` | 433 MB | **NO** | Ninguna composición renderiza: sin logos, sin fuentes, sin packshots |
| `raw/` | 1,1 GB | NO (a propósito) | No tienes las referencias del cliente contra las cuales comparar |
| `out/` | — | NO (a propósito) | Sólo entregas pasadas |

`raw/` y `out/` está bien que no estén: son material del cliente y entregas, se
bajan del Drive cuando se necesitan. **`public/assets/` es distinto** — ahí viven
las fuentes y los logos oficiales, que son lo mínimo para que algo funcione.

### Mientras no exista el espejo en Drive (ver más abajo)
Pídele el material a Claude, marca por marca. Cada manual tiene la sección
"Dónde está el material" con los IDs de carpeta:

```
Baja el material de referencia de EBEMA a raw/ebema/ según clients/ebema/CLAUDE.md
```

O cópialo directo desde el Mac de Valeria por AirDrop / disco externo:
`EDITOR VIDEOS/public/assets/` completo.

### La solución definitiva — pendiente de decisión
Dos caminos, hay que elegir uno:

1. **Versionar el núcleo** (fuentes + logos ≈ **18 MB**) y dejar en Drive sólo lo
   pesado (videos, fotos en alta, 331 MB). Con esto, `git clone` + `npm install`
   deja el repo funcionando y las piezas se bajan por marca cuando hagan falta.
   **Es lo recomendado.** Se hace una vez y no se vuelve a tocar.
2. **Espejo completo en una carpeta de Drive** de `public/assets/`, con un script
   de sincronización. Más simple de mantener, pero cada clon parte con 30 minutos
   de descarga.

Corre `bash scripts/doctor.sh` para ver en qué estado está tu copia.

## Paso 6 — Tu primera pieza

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

1. **Trabaja en una rama.** `git checkout -b <tu-nombre>/<cliente>-<mes>`
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
