# Credenciales — Windows

**Nada de esta carpeta se sube al repositorio.** Está ignorada en `.gitignore`
justo para eso: el repo lo comparten varios diseñadores y un token acá dentro se
publicaría a todo el equipo en el siguiente `push`. Comprobado con
`git check-ignore -v credentials/token.json`.

---

## Lo que falta: un archivo

```
C:\Users\Elisabet\EDITOR VIDEOS\credentials\token.json
```

Es el token OAuth del estudio. Con él funcionan la subida a Drive, la lectura de
grillas y los correos. **No hay nada más que instalar** — las librerías de Python
ya quedaron puestas el 31-08-2026.

### Camino A — traerlo del Mac (lo más rápido)

En el Mac donde ya funciona, el archivo está en:

```
~/Desktop/COPYLAB PROJECTS/ASISTENTE PERSONAL/credentials/token.json
```

Cópialo a esta carpeta por el medio que prefieras (pendrive, Drive, WhatsApp Web).
Es un archivo de texto de unos pocos KB.

> ⚠️ **No lo mandes por un canal público ni lo pegues en un chat de grupo.** Da
> acceso a la cuenta de Google del estudio.

### Camino B — autorizarlo desde este PC

Sirve si tienes el **client secret** del estudio (`client_secret.json`, también en
`ASISTENTE PERSONAL/credentials/`) pero no el token. Déjalo en esta carpeta y corre:

```powershell
python scripts\autorizar-google.py
```

Se abre el navegador, inicias sesión con la cuenta del estudio, aceptas, y el
script escribe `credentials\token.json` solo.

---

## Comprobar que quedó bien

```powershell
python scripts\_entorno.py
```

Tiene que decir:

```
token Google    C:\Users\Elisabet\EDITOR VIDEOS\credentials\token.json
```

Si dice `✗ no está en esta máquina`, el archivo no está donde corresponde o tiene
otro nombre.

---

## Con el token puesto, subir piezas

```powershell
python scripts\between-subir-drive.py --carpeta 19Bv7lfMBEIt_4JLRStWKObtCnf4OmPdD `
    "out\hilton-between-cumple-r5\entrega S1\BW FEED 03-09 Cumpleanos 1.png" `
    "out\hilton-between-cumple-r5\entrega S1\BW FEED 03-09 Cumpleanos 2 detalles.png" `
    "out\hilton-between-cumple-r5\entrega S1\BW ST 03-09 Cafe de regalo cumpleanos.png"
```

> ⚠️ El scope es `drive.file`: puede **crear** archivos nuevos en una carpeta, pero
> no tocar los que subió otra persona. Para reemplazar una pieza ya entregada hay
> que usar `--actualizar <ID-del-archivo>` sobre algo que subimos nosotros — así se
> conservan los enlaces que el cliente ya tiene.

---

## Los 6 scopes, y por qué no se recortan

```
calendar · gmail.send · gmail.modify · gmail.labels · spreadsheets · drive.file
```

Si el refresco devuelve un token con menos, `between-subir-drive.py` **se niega a
guardarlo**: sobrescribirlo degradaría el token de todo el monorepo y dejaría sin
correo ni calendario a los demás scripts.

---

## Qué NO hace falta instalar

Ya está todo puesto en este PC (31-08-2026):

| | Estado |
|---|---|
| Node 24 · Remotion · `node_modules` | ✅ |
| Google Chrome (lo usa el render) | ✅ |
| Python 3.14 | ✅ |
| `openpyxl` · `pillow` · `numpy` | ✅ |
| `google-api-python-client` · `google-auth` · `google-auth-oauthlib` | ✅ |
| `requests` · `python-dotenv` | ✅ |
| **`credentials\token.json`** | ❌ **es lo único que falta** |
