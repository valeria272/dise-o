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
> **En Windows** el intérprete es `python` (no `python3`) y el venv queda en
> `~/copylab-venv/Scripts/python.exe`, no en `bin/python3`. Traduce esa ruta en TODOS
> los comandos de este documento antes de correrlos. Guía del diseñador:
> `docs/GUIA-INSTALACION-WINDOWS.html`.

Si no existe `~/copylab-venv`:
```bash
python3 -m venv ~/copylab-venv
~/copylab-venv/bin/python3 -m pip install --upgrade pip
~/copylab-venv/bin/python3 -m pip install pillow numpy requests certifi fonttools \
    cryptography google-api-python-client google-auth google-auth-oauthlib \
    openpyxl python-docx
```
Usa siempre `python3 -m pip`, nunca el binario `pip`.

### Las credenciales — salen del llavero del repo

No le pidas ninguna clave a nadie: **ya vienen en el repositorio, cifradas**.

```bash
python3 scripts/llavero.py abrir
```

Va a pedir **una contraseña**: la del estudio, la misma para todo el equipo, y es lo
único que Valeria entrega a mano, una sola vez. Si la persona no la tiene, dile
textual:

> «Pídele a Valeria la **contraseña del llavero del estudio**. Es una sola, se entrega
> una vez y no se te vuelve a pedir nunca más en este computador.»

Con eso quedan montadas la clave de Magnific/Freepik, la de Higgsfield y el token de
Google. Comprueba las dos cosas:

```bash
python3 scripts/llavero.py estado
python3 scripts/magnific.py check      # valida la clave SIN gastar créditos
```

⚠️ **Nunca escribas la contraseña en un archivo del repo** ni la repitas en el chat.
El detalle está en `credentials/LEEME.md`.

### Google Chrome
No lo puedes instalar en silencio. Si falta, dile:
**«Necesito que instales Google Chrome desde google.com/chrome — el estudio lo usa
por dentro para generar las gráficas.»**

### Memoria del estudio — sembrarla SIEMPRE en una máquina nueva

```bash
bash scripts/sembrar-memoria.sh
```

El repo trae en `docs/memoria-semilla/` las **56 notas de aprendizaje** del estudio
(ADN medido de cada marca, gotchas de render, recetas, feedback acumulado de Between,
EBEMA y las demás). La memoria de Claude vive en la cuenta de cada persona, no en el
repo: sin este paso, en una máquina nueva Claude arranca **sin nada de lo aprendido**
y repite errores que ya costaron rondas enteras. El script es idempotente y nunca
pisa memoria local — se puede correr tranquilo las veces que sea.

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
