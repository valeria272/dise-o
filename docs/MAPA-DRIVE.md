# Mapa del Drive de la agencia — dónde está cada cosa

> Levantado el 25-08-2026. Los IDs son estables: se pueden pasar directo al conector.

## Raíz
**AGENCIA COPYWRITERS** — `16kNWE2mkbLh1uTb5Jc5TuDhYwM0OOw0A`
16 carpetas de cliente. Pero las planificaciones de medios revelan **~24 cuentas activas**
(ver [`ESTADO-MARCAS.md`](ESTADO-MARCAS.md)).

## ⭐ LOGO CLIENTES — la fuente canónica de logos
`1Nplwe3IJtQy8y9ESLklyplu-T75Qs95v` (dentro de `COPYWRITERS/`, de Constanza Lizana)

Estructura: `LOGO CLIENTES/<MARCA>/PNG/`

| Marca | ID de carpeta | Marca | ID de carpeta |
|---|---|---|---|
| ABAKOS | `1MIYH787asks_a5Nyw3CYDC_c2BjTMvru` | INU | `1DeQMiM7oCZcL52JGCAZvfUwjV8qdFXqJ` |
| BETWEEN | `1qmZoK5H_nd4xLg5sO92OMuoIp2LdBkdP` | JAPIJANE | `1fSuq-wx6n3Jath-B29kZm-RmljWQsm_C` |
| CASABLANCA | `1euwxTwTtFBo8Njoh3QK4uWac0aTOEdAT` | MAS CENTER | `1bZJV8vAjLccf3MtaCtghlJ9bF_su78ak` |
| CAVA | `1IhUJwgtAYsgAdfR2qWrH1rySmE5tWOw1` | MERINO | `1CICUUuQIEahm_PbT5X6TpiR-zAeaTm09` |
| DHEMAX | `1rCetktMJN0a1bBEUUmONxck2BW9hVFi3` | MYZOO | `12A2fADHDGLHuDW3XQmA2gV4FGNBa_I4a` |
| EBEMA | `1BKvUl9FV0G7EuGT4Y7_0CnA1FGkh_YCE` | PISO 18 | `1s14qnR2dh91_tzMgax-j2MRtCUN7aCIW` |
| EGLO | `18x7Y5wfSep25EeUpYt2I9QcP9IYnQ5FA` | QB | `1JplIe94uLkvQxTU2PhmBXTEXHeA_vbKB` |
| ETERSOL | `1-x1eBPbZHKqjHwInEEf1oL4D6Osp0Q-B` | REM | `1ku6cZi3tVbBxLDVPOFOXFT1p6uDLVyuu` |
| FORK | `1fxYC5u4bh4NS3vnSi8lLC4r9PUsil5Io` | REVEX | `11r8gYt4YH8d7kBnGuYu3_D9HCQM4KIQs` |
| HILTON | `1UJoc9bHGiqhG0PSSbiu5q5VV9V0q81V3` | RINU | `1OyI4Uj3SnbAFAfFUFX_cQeWzBQfNRNDM` |
| SELFIE | `1_1CmvBGx6ffl85i2vLZ6FVWt8usKxJUL` | SGS | `1yf1R3fISm5zYTgf5PWchm2f2ZMha32zv` |
| TIERRACALMA | `1aPGTyZB1wcgdy-asWH35r4iOGiXMQhSa` | TINYPAIHUEN | `1NTpY3sK1OHzpcCvwG85IXWG2eBtQsqg6` |

> **Regla:** el logo de una pieza sale SIEMPRE de acá. Nunca se recrea a mano ni se
> saca de una pieza publicada si existe el PNG oficial.

Marcas de esta lista que **no** aparecían en mi mapa: SGS, EGLO, DHEMAX, REM,
MERINO, TINYPAIHUEN, ETERSOL.

## ⭐ QB — los editables de Eli (levantado 17-09-2026)

`1p1lhX45R5hMCat3cSoLeZhYydm5oG9D9` — **la raíz de los editables de QB**, de
`elisabet.soto@copywriters.cl`. Una carpeta por pieza; dentro, los PNG/JPG a
72 y 150 ppp y el `.eps`.

| Qué | ID |
|---|---|
| **KV de promos (AYCD + QBTIME), historia 1080×1920** | `1gcIlQwCJQWyZ4ol_BtKPCc7dXotsjxQR` |
| AYCD junio 2026 (post + 2 ST) | `178pdd3gBzNu96TSv8TJ3i478-FPMLRYk` |
| **Logotipos QB (PNG blanco/negro/verde, sin fondo)** | `14JOfcpGLEomQlQSp7gV2cweb9hiy0Kzo` |
| KV FLYER QB GENERAL 2026 SEP | `1GvGAqELOkKQmnFYIe-N7hT63k5Oo8cXK` |
| KV / PROMO SUNSET QB | `1jOLWs51spp5ZDGmaHhm4WIs5BCJYDJd2` · `1wegNpaYd-1_lOw8B8UZE7Cd4ANrb9trq` |

⭐ **Estos archivos SÍ bajan con el endpoint de `usercontent`** (ver la memoria
`bajar-grilla-ajena-de-drive`), sin token y sin tope de tamaño:

```bash
curl -sL "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t" -o archivo
```

⚠️ **Pero el compartido es POR ARCHIVO, no por carpeta.** En la misma carpeta un
PNG baja y el de al lado devuelve la página de login — pasó el 17-09 con
`AllYouCanDrink9.16.png`. Y una carpeta **recién creada** por Eli no está
compartida por enlace, así que no baja nada de adentro: hay que pedirle que la
ponga en «cualquiera con el enlace».

⚠️ **Verifica siempre con `file`**, nunca por tamaño: la página de login pesa
~915 KB y parece un archivo bueno.

## 🔑 CON QUÉ CUENTA ENTRA EL CONECTOR (verificado 27-08-2026)

**`constanza.olivares@copywriters.cl`.** No es la de Valeria ni la de Serena.
Comprobado con `owner = 'me'`: todos los archivos que devuelve tienen ese dueño.

> **Consecuencia:** una carpeta compartida al correo de *Serena* —o de cualquier otra
> persona— **no la ve el conector**, y no es cuestión de esperar el índice: no la va a
> ver nunca. Agregar un acceso directo a la «Mi unidad» de Serena **tampoco sirve**,
> porque esa no es la unidad que se lee.

**Para que el conector vea una carpeta nueva**, en orden de preferencia:
1. Compartirla **explícitamente** (no por link) con `constanza.olivares@copywriters.cl`.
2. Moverla o copiar su contenido dentro de `AGENCIA COPYWRITERS` — esa se lee completa.
3. Que Constanza Olivares le agregue **«Agregar acceso directo a Mi unidad»**.

⚠️ Ojo con los nombres: **Constanza Olivares** (la cuenta del conector) **no es**
Constanza Lizana «Coni», la diseñadora dueña de `LOGO CLIENTES` y `Diseños EDITABLES`.
Son dos personas distintas.

## Cómo llegar a las carpetas de los diseñadores

El conector **no lista por `parentId`** una carpeta compartida solo por link que no
esté en el índice de la cuenta (pasa con `Diseños EDITABLES` y con `CONI`). Pero
**sí encuentra sus archivos buscando por dueño**, que es el camino que funciona:

```
owner = 'constanza.lizana@copywriters.cl' and mimeType = 'application/vnd.google-apps.folder'
owner = 'constanza.lizana@copywriters.cl' and title contains 'Informe'
owner = 'elisabet.soto@copywriters.cl' and modifiedTime > '2026-07-01T00:00:00Z'
```

Con eso se llega a todo su árbol y desde ahí se navega por `parentId` normalmente.

## ⚠️ Diseños EDITABLES — visible pero NO indexado
`1nsGClWZUvqDHh_oFpc0h7QiN5flxK4xE` — de Constanza Lizana, modificada el 25-08-2026.

El conector **lee los metadatos de la carpeta pero no lista su contenido**: una
carpeta compartida por link recién no entra al índice de búsqueda de la cuenta hasta
que se abre desde Drive. Ver el pendiente en [`ESTADO-MARCAS.md`](ESTADO-MARCAS.md).

**Cómo destrabarlo (cualquiera de las dos):**
1. Que **Constanza Olivares** —la cuenta del conector, ver arriba— abra la carpeta en
   drive.google.com y le dé **«Agregar acceso directo a Mi unidad»**. Con eso entra al
   índice y el conector la lista completa. ⚠️ Antes acá decía «que Valeria abra»: **era
   incorrecto**, el conector no entra con la cuenta de Valeria (corregido 27-08-2026).
2. Compartirla explícitamente (no por link) con la cuenta de Claude.

## ⚠️ LCD — carpeta del PROPIO CLIENTE, no indexable
`1BLjPGmnMJIer-nAkZOkp5WQtefaqwrEI` — **dueño `jcampos@gruporevex.cl`**, o sea Grupo
Revex, no la agencia. Creada 27-05-2026, modificada 23-06-2026.

Compartida **sólo por link**, así que el conector la ve pero no la abre. Verificado el
27-08-2026, las cuatro vías fallan:

| Vía | Resultado |
|---|---|
| `title = 'LCD'` | vacío |
| `parentId = '<id>'` | vacío |
| `owner = 'jcampos@gruporevex.cl'` | vacío |
| `sharedWithMe = true` | no aparece |
| `get_file_metadata` con el ID | ✅ **lo único que responde** — devuelve nombre y dueño |

**Cómo destrabarla:** abrirla en drive.google.com y darle **«Agregar acceso directo a
Mi unidad»**. Con eso entra al índice de la cuenta y se lista completa. (Mismo problema
y misma solución que `Diseños EDITABLES` y `CONI`, más arriba.)

> 💡 **Y de paso:** si el cliente ordenó su material por sucursal, al lado de `LCD`
> debería haber una carpeta de **Temuco** — que es la que de verdad falta para poder
> verificar esa pieza. Al abrir la carpeta, mirar el nivel de arriba.

## Briefs y planificaciones
| Qué | Dónde |
|---|---|
| Brief de diseño (el formato bueno) | `1JegSXFNuM0SWxuRU6g5dfplXiF2ktD93` — Revex sep 2026 |
| Grilla Performance EBEMA sep 2026 | `1zHFfSsXCwo25ID2RylsVCB7daxTXIdvGXWkjCpdkUjI` |
| Grilla Selfie sep 2026 | `1bpZdVtpDwTEHnwEcVhibJGHBmh6qAI3gm-IvqvmXDuM` |
| Grilla Revex \| Casablanca sep 2026 | `13hI9czHimNuaa636YfutYO8RzuSFcrne` |
| Carpeta de trabajo Revex/Casablanca sep | `1h-oBJqEbzFGRAwi_P5bd2bt_a-DMFhNt` → `DISEÑO PAID` `1uMPBBoOpspRKBEqtiZOElJuMEDuaisl2` |

## El equipo de diseño (por quién firma los archivos)
| Persona | Correo | Marcas |
|---|---|---|
| **Constanza Lizana** «Coni» | `constanza.lizana@copywriters.cl` | Selfie, QB, packaging (Xtreme Vet, shampoos), KV de campaña. **Dueña de LOGO CLIENTES y de Diseños EDITABLES** |
| **Elisabet Soto** «Eli» | `elisabet.soto@copywriters.cl` | Hilton completo: DT, QB, Between, Piso18. Nomenclatura `C1 S1 N°1`, `ST n°1 S4`, `KV SUNSET QB` |
| **Paulina Bustamante** | `paulina.bustamante@copywriters.cl` | EBEMA y MyZoo. ⚠️ Tiene correo de la agencia — mi manual de EBEMA la trataba como diseñadora *del cliente*. **Por confirmar** |
| **Diego Aguilar** | `diego.aguilar@copywriters.cl` | Pivot Connect |

## Límites conocidos del conector
- Archivos **>10 MB** no bajan por MCP → `curl "https://drive.google.com/uc?export=download&id=<ID>"` si es link-shared.
- El token OAuth tiene scope `drive.file`: **no baja archivos de terceros**. Usar el conector.
- Carpetas compartidas solo por link no se listan hasta que entran al índice (ver arriba).
- Los `.ai` no se pueden abrir. Sí se leen las carpetas `Links/` y el `Informe.txt`
  del paquete, que traen fuentes, imágenes enlazadas y medidas de mesa de trabajo.
