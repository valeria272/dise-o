---
description: Primer arranque del estudio en una máquina nueva — corre esto al descomprimir el ZIP
---

Es el primer arranque de este estudio en esta máquina. Hazlo **sin preguntar** y
termina con un resumen claro de qué quedó listo y qué le falta a la persona.

## 1. Diagnóstico
```bash
bash scripts/doctor.sh
```

## 2. Arreglar lo que se pueda solo
- Si falta `node_modules/`: `npm install` (tarda unos minutos, espérala).
- Si falta el venv de Python, créalo:
  ```bash
  python3 -m venv ~/copylab-venv
  ~/copylab-venv/bin/python3 -m pip install --upgrade pip
  ~/copylab-venv/bin/python3 -m pip install pillow requests certifi \
      google-api-python-client google-auth google-auth-oauthlib openpyxl
  ```
  Usa siempre `python3 -m pip`, nunca el binario `pip`.
- Verifica que compile: `npx tsc --noEmit`. Errores preexistentes en composiciones
  de cliente no bloquean — repórtalos, no los arregles ahora.

## 3. Comprobar lo que NO puedes arreglar tú
- **Google Chrome**: si no está, el render de gráficas no funciona. Dilo.
- **Conector de Google Drive**: prueba `search_files` con cualquier término.
  Si falla, la persona tiene que activarlo en claude.ai → Settings → Connectors.
  Sin eso no hay referencias de cliente ni entregas.
- **Ubicación**: si la carpeta está bajo `Desktop/`, `Documents/` o `Downloads/`,
  advierte del problema de iCloud y recomienda `~/copylab/`.

## 4. Mostrar el mapa
Lee `docs/ESTADO-MARCAS.md` y resume: qué marcas tienen sistema listo, cuáles no,
y cuál es el estado del material local (`public/assets/`, `raw/`).

## 5. Cerrar
Termina con:
- ✅ lo que quedó funcionando
- ⚠️ lo que la persona tiene que hacer (con el paso exacto)
- Las tres formas de trabajar: `/pieza`, `/qa`, `/marca-nueva`
- Un ejemplo concreto de `/pieza` con una marca que sí tenga sistema

No hagas una pieza en este arranque. Solo dejar la máquina lista.
