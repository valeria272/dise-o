# Estudio de diseño COPYLAB — empieza por acá

Esta guía asume que **no tienes nada instalado**. Son unos 40 minutos, de los cuales
30 son descargas mientras haces otra cosa.

No necesitas saber programar. Vas a escribirle a Claude en español, como en un chat.

---

# PARTE 1 — Instalar (una sola vez)

## 1. Google Chrome
Si no lo tienes: **google.com/chrome** → descargar → instalar.
El estudio lo usa por dentro para generar las gráficas. Tiene que estar sí o sí.

## 2. Node.js
Anda a **nodejs.org** y baja la versión que dice **LTS** (el botón de la izquierda).
Instalador normal: siguiente, siguiente, listo.

## 3. Visual Studio Code
Anda a **code.visualstudio.com** → Download for Mac → descomprime y **arrastra el ícono
a tu carpeta Aplicaciones**.

## 4. Claude Code
Abre VSCode. Arriba en el menú: **Terminal → New Terminal**. Se abre un panel abajo.
Copia esto, pégalo ahí y aprieta Enter:

```
npm install -g @anthropic-ai/claude-code
```

Va a escribir muchas líneas. Cuando vuelva a aparecer el cursor, terminó.

## 5. Tu cuenta de Claude
Necesitas la cuenta `@copywriters.cl` que te asignen. Con ella:

1. Entra a **claude.ai** e inicia sesión.
2. Anda a **Settings → Connectors**.
3. Activa **Google Drive** con ese mismo correo.

> ⚠️ **Esto es obligatorio y no viaja en el ZIP.** Los conectores son de tu cuenta, no
> del proyecto. Sin Google Drive no puedes ver el material de los clientes ni entregar.

## 6. La contraseña del llavero

Es **lo único** que le tienes que pedir a Valeria, y es **una sola vez**.

Las claves de las herramientas del estudio —Magnific/Freepik para generar imágenes,
Higgsfield para video, el acceso al Drive— ya vienen dentro del proyecto, guardadas
bajo llave. Esa contraseña es la que las abre. No la pidas por segunda vez: cuando la
escribes, el computador se acuerda.

> No la mandes por un grupo de WhatsApp ni la pegues en un chat de equipo. Es la llave
> de todas las herramientas pagadas de la agencia.

---

# PARTE 2 — Instalar el estudio

## 7. Dónde dejar la carpeta

Descomprime el ZIP que te pasaron y deja la carpeta acá:

```
~/copylab/EDITOR VIDEOS/
```

Osea: en tu carpeta de usuario, crea una carpeta `copylab` y adentro va esto.

> 🔴 **NO la dejes en Escritorio, Documentos ni Descargas.**
> Si tienes iCloud Drive activo, iCloud vacía el contenido de los archivos que no usas
> y el proyecto se rompe en silencio: los renders se cancelan solos, aparecen archivos
> en gris y salen errores raros. Ya nos pasó dos veces. En `~/copylab/` no pasa.

## 8. Abrir el estudio

En VSCode: **File → Open Folder…** y elige `~/copylab/EDITOR VIDEOS`.
Después **Terminal → New Terminal**, y escribe:

```
claude
```

La primera vez te va a pedir iniciar sesión: se abre el navegador, entras con tu cuenta
`@copywriters.cl`, y listo.

## 9. Dejar todo listo

Escribe esto y no hagas nada más:

```
/arranque
```

Claude instala lo que falte, revisa que todo esté en su lugar y te dice si te falta algo.
En algún momento te va a pedir **la contraseña del llavero** (la del paso 5): escríbela
y con eso quedan activas todas las herramientas de pago del estudio.

**No tienes que explicarle nada del proyecto**: los manuales de las marcas ya están
adentro.

---

# PARTE 3 — Trabajar

## Los cuatro comandos

| Escribes | Y pasa esto |
|---|---|
| `/al-dia` | Revisa el Drive de la agencia y te cuenta qué cambió: grillas nuevas, editables nuevos, comentarios de clientes |
| `/pieza <marca> <lo que necesitas>` | Produce. Lee el manual de la marca, el brief, arma, revisa y entrega |
| `/qa <marca o carpeta>` | Control de calidad antes de mostrarle algo a alguien |
| `/marca-nueva <nombre>` | Abre el sistema de un cliente que todavía no existe |

## Cómo se ve en la práctica

```
/al-dia
/pieza ebema las 11 gráficas de sucursal de octubre, feed y story
/qa ebema
```

Ejemplos reales de `/pieza`:
- `/pieza revex el refresh de Las Condes, cuadrado + story`
- `/pieza selfie el carrusel de la semana 2`
- `/pieza cava el mailing de último día con Black Series y Adventure`
- `/pieza between la grilla de la semana 1`

Le puedes hablar normal. Si algo no se entiende, Claude pregunta.

---

# Las tres reglas que no se rompen

**1. El brief manda el QUÉ; el sistema de marca manda el CÓMO.**
Cada cliente tiene su manual con su paleta, sus medidas y sus reglas, aprendidas de sus
propias piezas aprobadas. Una pieza nueva **extiende** ese sistema. Nunca inventa uno,
aunque el brief describa otra cosa.

**2. Los textos y los CTAs salen literales del brief.**
No se inventan botones, ni claims, ni precios. Si falta un dato, se pregunta.

**3. Cuando el cliente corrige algo, se escribe en el manual de su marca.**
Es lo que hace que el estudio mejore. Lo que no queda escrito, se vuelve a equivocar.

---

# Si algo se rompe

| Te pasa esto | Es esto | Se arregla así |
|---|---|---|
| Errores raros, archivos en gris, renders que se cancelan | La carpeta está en iCloud | Muévela a `~/copylab/` |
| «No encuentro el material del cliente» | Falta el conector de Drive | claude.ai → Settings → Connectors → Google Drive |
| El render no genera nada | Falta Chrome | Instálalo |
| «No encuentro la clave de Magnific» | El llavero está cerrado | Escribe en el chat: **`abre el llavero`** |
| Todo va lentísimo | iCloud está rematerializando archivos | Espera, o mueve la carpeta fuera de iCloud |

Si no sabes qué pasa, escribe en el chat: **`corre el doctor`**. Claude diagnostica y te
dice qué falta.

---

**Documentación completa:** [`docs/`](docs/) — el método está en
[`SISTEMA-DE-MARCAS.md`](docs/SISTEMA-DE-MARCAS.md) y el flujo de trabajo mes a mes en
[`FLUJO-MENSUAL.md`](docs/FLUJO-MENSUAL.md).
