---
description: Primer arranque del estudio en una máquina nueva — deja todo listo sin que la persona instale nada
---

Es el primer arranque de este estudio en esta máquina, y **quien lo corre es un
diseñador, no un programador**. No sabe qué es Node, ni npm, ni un venv, y no tiene
por qué saberlo.

**Hazlo TODO tú.** No le pidas que instale nada ni que entienda nada técnico. Las
únicas dos cosas que no puedes hacer por ella son: escribir la contraseña de su Mac
cuando el sistema se la pida, y activar los conectores en su cuenta de claude.ai.

Habla en español de Chile, sin jerga. Cuando algo tarde, dilo y sigue.

---

## 0. ¿Dónde estamos?

Si la conversación NO está dentro de la carpeta del estudio (no existe
`clients/` ni `docs/SISTEMA-DE-MARCAS.md`), entonces hay que traerlo:

```bash
mkdir -p ~/copylab && cd ~/copylab
git clone <URL-DEL-REPOSITORIO> estudio
```

Si no tienes la URL, **pídesela** — es lo único que necesitas de la persona en este
paso. Después dile que abra esa carpeta (`~/copylab/estudio`) y vuelva a correr
`/arranque` ahí.

⚠️ **Nunca dentro de `Desktop/`, `Documents/` ni `Downloads/`**: iCloud los
sincroniza, deja los archivos "dataless" y el estudio se cae. Ya pasó.

---

## 1. Diagnóstico

```bash
bash scripts/doctor.sh
```

Léelo entero antes de actuar. Te dice qué falta.

---

## 2. Instala lo que falte — sin preguntar

### Node.js
Si `node --version` falla o es menor que 20, instálalo tú. En macOS:

```bash
# Averigua la versión LTS actual y bájala
curl -fsSL https://nodejs.org/dist/index.json | \
  python3 -c "import json,sys;d=[x for x in json.load(sys.stdin) if x['lts']][0];print(d['version'])"
```

Con esa versión, baja el `.pkg` de `https://nodejs.org/dist/<version>/node-<version>.pkg`
e instálalo con `sudo installer -pkg <archivo> -target /`.

> Avísale antes: **«El Mac te va a pedir tu contraseña. Es la misma con la que
> inicias sesión en el computador, y es normal — se necesita para instalar
> programas.»** Es lo único que tiene que escribir ella.

Si prefiere no dar la contraseña, ofrece Homebrew como alternativa, pero también
pide permisos. Si se niega a las dos, dilo claro: sin Node no hay render.

### Dependencias del proyecto
```bash
npm install
```
Tarda varios minutos. Avísale y espérala; no la interrumpas.

### Python
Si no existe `~/copylab-venv`:
```bash
python3 -m venv ~/copylab-venv
~/copylab-venv/bin/python3 -m pip install --upgrade pip
~/copylab-venv/bin/python3 -m pip install pillow numpy requests certifi fonttools \
    google-api-python-client google-auth google-auth-oauthlib openpyxl python-docx
```
Usa siempre `python3 -m pip`, nunca el binario `pip`.

### Google Chrome
No lo puedes instalar en silencio. Si falta, dile:
**«Necesito que instales Google Chrome desde google.com/chrome — el estudio lo usa
por dentro para generar las gráficas.»**

---

## 3. Comprueba lo que depende de su cuenta

### Conector de Google Drive — es el indispensable
Pruébalo de verdad: haz una búsqueda con `search_files`. Si falla, dile
**exactamente** esto:

> «Anda a claude.ai → Settings → Connectors y activa **Google Drive** con tu correo
> @copywriters.cl. Sin eso no puedo bajar briefs ni referencias ni subir entregas.
> Avísame cuando esté y lo pruebo de nuevo.»

Los otros (Canva, Gmail, Higgsfield) son deseables, no bloqueantes. Menciónalos una
vez, sin insistir.

### Tipografías
```bash
~/copylab-venv/bin/python3 scripts/verificar-fuentes.py
```
Las de Adobe Fonts **no se pueden copiar**: dile cuáles activar en
**Creative Cloud → Fuentes** (no necesita Photoshop ni Illustrator). Las de pago
hay que pedírselas al cliente; dile a cuál.

### Material
```bash
~/copylab-venv/bin/python3 scripts/verificar-material.py raw clients public/assets
```
Si el repo viene recién clonado, `raw/` va a estar vacío y **eso está bien**: se baja
por marca cuando haga falta. Explícaselo para que no crea que algo salió mal.

---

## 4. Verifica que de verdad funciona

```bash
npx tsc --noEmit
```
Si compila limpio, dilo. Errores preexistentes en composiciones de cliente no
bloquean: repórtalos, no los arregles ahora.

---

## 5. Muéstrale el mapa

Lee `docs/ESTADO-MARCAS.md` y resume **en lenguaje de diseño, no de código**: qué
marcas están listas para producir, cuáles todavía no, y qué le falta a cada una.

---

## 6. Cierra

Termina con tres bloques, cortos:

- ✅ **Listo:** lo que quedó funcionando.
- ⚠️ **Te toca a ti:** sólo lo que ella tiene que hacer, con el paso exacto y por qué.
- ▶️ **Cómo se trabaja:** los tres comandos (`/al-dia`, `/pieza`, `/qa`) y **un
  ejemplo concreto** con una marca que sí tenga sistema, listo para copiar.

**No hagas una pieza en este arranque.** El trabajo de hoy es dejar la máquina lista.
