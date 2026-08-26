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
1. Que Valeria abra la carpeta en drive.google.com y le dé **«Agregar acceso
   directo a Mi unidad»**. Con eso entra al índice y el conector la lista completa.
2. Compartirla explícitamente (no por link) con la cuenta de Claude.

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
