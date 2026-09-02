# Credenciales del estudio — el llavero

> **Resumen para el diseñador nuevo:** no le pidas ninguna clave a nadie.
> Están todas en el repositorio, cifradas. Corre esto una vez y listo:
>
> ```bash
> python3 scripts/llavero.py abrir
> ```
>
> Te va a pedir **la contraseña del llavero del estudio**. Es una sola, la misma
> para todo el equipo, te la da Valeria una vez y no se te vuelve a pedir nunca
> más en este computador.

---

## Qué es el llavero

`credentials/llavero.copylab` es el **único** archivo con credenciales que viaja
en el repositorio. Viaja cifrado (AES-256, contraseña derivada con scrypt): si lo
abres con un editor solo vas a ver ruido. Sin la contraseña del estudio no sirve
de nada, ni siquiera para quien tenga el repo entero.

Dentro van:

| Qué | Para qué |
|---|---|
| `FREEPIK_API_KEY` | **Magnific / Freepik** — generar fondos y ambientes, escalar, Nano Banana Pro |
| `HF_API_KEY` · `HF_SECRET` | Higgsfield — video IA |
| `ANTHROPIC_API_KEY` | API de Claude, para los scripts que la llaman |
| `token.json` | Token OAuth de Google — bajar grillas y briefs, subir entregas al Drive |
| `client_secret.json` | Cliente OAuth, por si hay que volver a autorizar desde cero |
| `LOGIN_HERRAMIENTAS_*` | El **correo y la contraseña** con que se entra a Higgsfield, Canva, Magnific y CapCut |

Lo que **no** va: Slack, Trello, Meta, bancos, planillas de finanzas. El llavero
es del estudio de diseño, no de la agencia entera.

---

## Los cinco comandos

```bash
python3 scripts/llavero.py abrir     # monta las credenciales en este computador
python3 scripts/llavero.py logins    # los accesos de navegador y qué conectores activar
python3 scripts/llavero.py estado    # ¿qué tengo montado? ¿qué falta?
python3 scripts/llavero.py ver       # qué hay dentro (valores enmascarados)
python3 scripts/llavero.py guardar   # SOLO VALERIA: rehace el llavero
```

En **Windows** es `python` en vez de `python3`. Todo lo demás es igual.

Si `abrir` reclama que falta la librería de cifrado:

```bash
python3 -m pip install cryptography
```

### Comprobar que la clave de Magnific quedó buena

```bash
python3 scripts/magnific.py check
```

Autentica contra Freepik **sin gastar créditos**. Si dice `✓ VÁLIDA`, ya puedes
producir.

---

## ⚠️ Lo que el llavero NO puede hacer por ti: los conectores

`abrir` monta las claves de los **scripts**. Los **conectores de claude.ai**
—Google Drive, Higgsfield, Canva— son de la cuenta de Claude de cada persona: no
viajan en el repositorio y hay que activarlos una vez, a mano.

```bash
python3 scripts/llavero.py logins
```

Te muestra el correo y la contraseña de las herramientas de pago, y exactamente
qué activar en **claude.ai → Settings → Connectors**:

| Conector | Con qué cuenta | Para qué |
|---|---|---|
| **Google Drive** | **tu** correo `@copywriters.cl` | Briefs, referencias y entregas. **Es el indispensable** |
| **Higgsfield** | `contacto@copywriters.cl` | Video IA |
| **Canva** | `contacto@copywriters.cl` | Brand kit del estudio (`kAF_gMI0GAg`) |

Ojo con la diferencia: Drive va con **tu** cuenta personal del trabajo, porque
las entregas quedan a tu nombre. Higgsfield y Canva van con la cuenta de la
agencia, porque la suscripción de pago está ahí.

---

## Dónde queda todo después de `abrir`

| Archivo | Quién lo lee |
|---|---|
| `credentials/.env` | `scripts/_entorno.py`, y por él todos los scripts del estudio |
| `~/.magnific_key` | los scripts antiguos de Magnific/Freepik |
| `credentials/token.json` | la subida a Drive y la lectura de grillas |

**Ninguno de esos se versiona.** Están cubiertos por la regla `credentials/*` del
`.gitignore`; el único con permiso explícito para subir es `llavero.copylab`.
Compruébalo cuando quieras:

```bash
git check-ignore -v credentials/.env credentials/token.json
git check-ignore -v credentials/llavero.copylab   # este NO debe aparecer
```

---

## Para Valeria: cambiar o rotar una clave

```bash
python3 scripts/llavero.py guardar --set FREEPIK_API_KEY=FPSX...
git add credentials/llavero.copylab
git commit -m "Llavero: clave nueva de Magnific"
git push
```

Para una **contraseña**, usa `--pedir` en vez de `--set`: te la pide a ciegas y
así no queda escrita en el historial del terminal.

```bash
python3 scripts/llavero.py guardar --pedir LOGIN_HERRAMIENTAS_PASS
```

`guardar` parte del llavero que ya existe y solo pisa lo que le pases, así que no
se pierde nada. Sin `--set`, recoge sola lo que encuentre en esta máquina
(`~/.magnific_key`, el `.env` del monorepo, `credentials/token.json`).

Los demás diseñadores se ponen al día con:

```bash
git pull && python3 scripts/llavero.py abrir --forzar
```

### Rotar la contraseña del llavero

```bash
rm ~/.copylab-llave                       # olvida la anterior en este equipo
python3 scripts/llavero.py guardar        # te la pide de nuevo, dos veces
```

Hazlo cuando alguien deja el equipo. Ojo: quien haya clonado antes conserva las
claves que ya descifró — para eso hay que rotar **las claves mismas** en Freepik
y Higgsfield, no solo la contraseña del llavero.

---

## Los 6 scopes del token de Google, y por qué no se recortan

```
calendar · gmail.send · gmail.modify · gmail.labels · spreadsheets · drive.file
```

Es el único token OAuth del monorepo. Si al refrescarlo Google devuelve menos
scopes y se guarda así, **se degradan los permisos de todos los demás proyectos**
(pasó el 29-07-2026: quedó solo con `gmail.modify` y murió todo lo de Sheets).
Por eso `between-subir-drive.py` se niega a guardar un token recortado.

> ⚠️ El scope es `drive.file`: puede **crear** archivos nuevos en una carpeta,
> pero no tocar los que subió otra persona. Para reemplazar una pieza ya
> entregada hay que usar `--actualizar <ID-del-archivo>` sobre algo que subimos
> nosotros — así se conservan los enlaces que el cliente ya tiene.

### Volver a autorizar desde cero

Si el token se venció del todo y `client_secret.json` está montado:

```bash
python3 scripts/autorizar-google.py
```

Se abre el navegador, inicias sesión con la cuenta del estudio, aceptas, y el
script escribe `credentials/token.json` solo. Después, para que el equipo lo
tenga: `python3 scripts/llavero.py guardar` y `git push`.

---

## ⛔ El conector de Drive NO reemplaza a este token (verificado 01-09-2026)

Es la pregunta que aparece siempre: *«si el conector de Google Drive de claude.ai
ya está conectado, ¿para qué el token?»*. Se probó dando **permiso de escritura
completo** al conector, y no alcanza. Dos límites del conector, leídos en su
propio esquema:

| Herramienta del conector | Lo que puede |
|---|---|
| `Crear archivo` | solo acepta el contenido **incrustado en la llamada**, en base64 |
| `Actualizar archivo` | solo cambia **título y carpeta** — nunca el contenido |

Una entrega es un PNG de varios MB: no cabe incrustado, y no se puede reemplazar
conservando el enlace. Por eso el token sigue siendo necesario.

---

## Qué NO hace falta instalar

Ya estaba puesto en el PC de Eli (31-08-2026):

| | Estado |
|---|---|
| Node 24 · Remotion · `node_modules` | ✅ |
| Google Chrome (lo usa el render) | ✅ |
| Python 3.14 | ✅ |
| `openpyxl` · `pillow` · `numpy` | ✅ |
| `google-api-python-client` · `google-auth` · `google-auth-oauthlib` | ✅ |
| `requests` · `python-dotenv` | ✅ |
| `cryptography` (la pide el llavero) | ⚠️ instalar si `abrir` reclama |
| `credentials\token.json` | ✅ **ya no se manda a mano — sale del llavero** |

---

## Historia de este archivo

Antes decía *«nada de esta carpeta se sube al repositorio»* y el token se pasaba
por pendrive o WhatsApp, uno por uno, cada vez que entraba alguien al equipo. Eso
se acabó el **02-09-2026**: la regla sigue en pie para todo lo que está en claro,
y la única excepción es el llavero cifrado.
