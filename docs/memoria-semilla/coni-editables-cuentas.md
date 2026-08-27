---
name: coni-editables-cuentas
description: Cómo llegar a las carpetas de los diseñadores en Drive (buscar por owner, no por parentId) y qué se levantó de MyZoo, CAVA y Selfie
metadata:
  type: reference
---

**La técnica que funciona.** El conector de Drive **no lista por `parentId`** una
carpeta compartida solo por link que no esté en el índice de la cuenta (pasó con
`Diseños EDITABLES` `1nsGClWZUvqDHh_oFpc0h7QiN5flxK4xE` y con `CONI`
`1knb1O6u3SC5_DJ8fJpRrIbGhL_5riaZ_`). Pero **sí encuentra sus archivos buscando por
dueño**:

```
owner = 'constanza.lizana@copywriters.cl' and mimeType = 'application/vnd.google-apps.folder'
owner = 'constanza.lizana@copywriters.cl' and title contains 'Informe'
```
Desde ahí se navega por `parentId` normalmente. **Usar esto antes de pedir que
compartan de nuevo.**

**MyZoo** (`clients/myzoo/`) — son **dos disciplinas**: envase (CMYK, 140×160 mm,
`PANTONE 114 C` / `708 C` / `Neutral Black C`, **Neutraface Text** + Roboto, 100%
vectorial) y digital (sin medir todavía). Bajada: **«AM♥R QUE SE SIENTE»**. Líneas:
Avena Coloidal (1:2), Expert Care, Groomer Grade (1:10), Xtreme Vet. Los packs tienen
variante **«OJOS AMARILLOS»** y siempre llevan «Imágenes referenciales». Los claims
(99,9999 % de hongos, Cruelty Free ONG Te Protejo…) son **regulados**: van literales.

**CAVA** (`clients/cava/`) — hay estructura pero **NO paleta ni tipografías**: no se
puede producir todavía. El mes son 8 briefs numerados
(`CAVA_<MES>_BRIEF<N>-<nn>.png`) y las campañas grandes son un **embudo de urgencia**
con una pieza por momento: PRE → YA COMENZÓ → CARRITO → POCAS HORAS → ÚLTIMO DÍA →
SE AGOTAN. Falta confirmar los **legales de alcohol** obligatorios en Chile.

**Selfie** — estructura de Coni: `S<n>/` con `FEED/ ST/ MAIL/ BANNER/`. Mailing:
`MAILS_<MES><Sn>_<CAMPAÑA>-<nn>.png`. Usa GIF animados, no solo estáticos. Banners
`300x250` y `1200x…` además del 2001×686.

**How to apply:** para cualquier marca nueva, correr `/adn <marca> <id>` y buscar
primero el `Informe.txt`. Ver [[adn-desde-editables]].
