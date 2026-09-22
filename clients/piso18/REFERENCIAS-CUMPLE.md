# `ref-cumple/` — de dónde sale cada archivo

> Escrito el **22-09-2026**. Cuatro `/arranque` seguidos (16, 17, 21 y 22-09)
> reportaron «11 archivos rotos» sin que nadie supiera **de dónde** rebajarlos.
> Acá está el origen, identificado por peso exacto de los dos que sí llegaron bien.
>
> ✅ **RESUELTO el mismo 22-09, por la tarde.** Eli compartió la carpeta por enlace
> como Lector y los 7 PNG que faltaban bajaron **byte a byte exactos** por
> `curl`. Los 4 `.jpg` fantasma se borraron. **Piso 18 ya no está bloqueado.**
> Lo que sigue abajo se deja como estaba porque explica la causa y las vías
> probadas — sirve la próxima vez que una carpeta ajena no baje.

Todo cuelga de `PISO18 › <carpeta de referencias de Eli>`
(`1MDm5JLRBe_Ep99hhK7fHgZ2mg35y9MJ2`), creada por Eli el 15-09-2026 —
la misma fecha y hora en que se creó esta carpeta local.

## El mapa

| Local | Origen en Drive | fileId | Bytes | Estado |
|---|---|---|---|---|
| `actual-1.png` | `CARRUSEL CUMPLE ACTUAL 2026` › `C1 S3 n°1.png` | `1_4BJqdQXgj5zgZI32nGCRD9I7YxsQvWx` | 2.979.282 | ✅ bueno |
| `actual-2.png` | `CARRUSEL CUMPLE ACTUAL 2026` › `C1 S3 n°2.png` | `1u-3lMmvCvg3bd42dl8ym_Ip3W2QvyIr6` | 8.660.362 | ✅ bajado 22-09 |
| `actual-3.png` | `CARRUSEL CUMPLE ACTUAL 2026` › `C1 S3 n°3.png` | `1PToN-oAda05MLhIvIzyDVxrH7ZC23tIj` | 7.021.442 | ✅ bajado 22-09 |
| `actual-4.png` | `CARRUSEL CUMPLE ACTUAL 2026` › `C1 S3 n°4.png` | `1-VeOblL2AXm20yNh0yZLL6K3wkl8fe4Z` | 7.325.533 | ✅ bajado 22-09 |
| `benef-1.png` | `BENEFICIOS CUMPLEAÑOS` › `C2 S1 P18 1.png` | `1w7ZW4SZZezFpSATA8hRxoqA4EA0GCFUw` | 10.014.738 | ✅ bajado 22-09 |
| `benef-2.png` | `BENEFICIOS CUMPLEAÑOS` › `C2 S1 P18 2.png` | `1pUMS5OCX7Po4JhSzk4wNOo7Hob-EaMnZ` | 7.162.976 | ✅ bajado 22-09 |
| `benef-3.png` | `BENEFICIOS CUMPLEAÑOS` › `C2 S1 P18 3.png` | `18GJDwwzggwRdubmfLU-TAWqXTYe4opX4` | 8.649.502 | ✅ bajado 22-09 |
| `viejo-1.png` | `CARRUSEL CUMPLEAÑOS` › `C1 S4 N°1.png` | `1_EVRCEBuNFI6qb-7exyDsZJC1raclXag` | 2.360.602 | ✅ bajado 22-09 |
| `viejo-2.png` | `CARRUSEL CUMPLEAÑOS` › `C1 S4 N°2.png` | `1GjGtDxZQKgK066fiMX1CTZi7w81QyA0q` | 2.552.923 | ✅ bueno |

Las tres carpetas de origen:

| Carpeta | folderId |
|---|---|
| `CARRUSEL CUMPLE ACTUAL 2026` | `1cA0YdoriGf5MqojdPvn6ITG8T3xOBoWj` |
| `BENEFICIOS CUMPLEAÑOS` | `1PB29U8qiujZPWHV9H5r0f2uFzQcGtXqx` |
| `CARRUSEL CUMPLEAÑOS` | `1zcVji_qzbYZ_-6evVzHLxD41Ra5VXTEt` |

⚠️ **Los cuatro `.jpg`** (`actual-2/3/4.jpg`, `benef-1.jpg`) no existen en Drive:
en el origen **todo es PNG**. Son un segundo intento de descarga que volvió a traer
el mismo HTML. No hay nada que rebajar para ellos — **borrados el 22-09**.

## ⛔ Por qué falló, y por qué sigue fallando

Los dos archivos buenos son **el primero de su carpeta**: se bajaron por el conector
MCP de Drive, que va autenticado. Los otros siete se intentaron por `curl`, y ahí
Drive devuelve los ~915 KB de la **página de login**.

Verificado hoy, 22-09, archivo por archivo:

| Vía | Resultado |
|---|---|
| `drive.usercontent.google.com/download?…&confirm=t` | ⛔ 915.456 bytes de `<!doctype html>` — **las carpetas de Eli no están compartidas por enlace**.  ✅ **Con la carpeta compartida (misma tarde) baja los 7 exactos, y también un PNG de 15 MB y un GIF de 15 MB: el endpoint no tiene tope** |
| Token del estudio (`scripts/drive-bajar.py`) | ⛔ `HttpError 404 File not found` — el token es scope `drive.file` y no ve archivos que no creó él |
| Conector MCP `download_file_content` | ✅ funciona, pero devuelve **base64 al contexto**: estos PNG son de 7 a 10 MB cada uno y no caben |

## Las dos salidas — y cuál se tomó

1. ✅ **Compartir por enlace.** Es la que se tomó el 22-09. Eli abrió **la carpeta
   madre** —`Grillas aprobadas`, no las tres subcarpetas— con rol **Lector**, y en
   Drive el permiso baja a todo lo que cuelga. Verificado:
   `permissions` devuelve `{"role":"reader","type":"anyone"}`. Con eso `curl` las
   baja sin tope (memoria `bajar-grilla-ajena-de-drive`).
   ⚠️ Es **Lector, no Editor** — la alerta `drive-agencia-permiso-abierto` nació de
   una carpeta que quedó abierta para editar. Ésta no lo está.
2. ⏳ **Ampliar el token del estudio a `drive.readonly`.** Sigue pendiente y sigue
   siendo lo que conviene: arregla esto y todo lo que venga después, en todas las
   marcas, sin abrir ninguna carpeta. Es decisión de Valeria, no de Eli
   (memoria `a-eli-no-se-le-llevan-decisiones-tecnicas`). La n°1 resolvió este caso;
   la n°2 evita el próximo.

## ⭐ Y la carpeta traía mucho más que las 11

Al abrirse se pudo listar entera, y resultó tener **seis** subcarpetas, no tres, más
**12 archivos sueltos**. Todo bajado el 22-09 a `raw/hilton/piso18/ref-aprobadas/`:

| Qué | Dónde quedó | Estado |
|---|---|---|
| `CARRUSEL ESTACIÓN` — C1 S1 n°1/2/3 | `carrusel-estacion/` | nuevo, no estaba |
| `CARRUSEL NOVIOS` — C2 S1 n°1/2 | `carrusel-novios/` | ya estaba, íntegro |
| `PROMOS PISO18` — 2 post + ST N°1 y N°3 S1 | raíz | N°3 era nuevo |
| Sueltos de la S3 (2 PNG, 1 MP4, 1 GIF) | `sueltos-s3/` | nuevos |
| Histórico jun–sep 2026 (6 PNG + 1 MP4) | `historico/` | nuevos |

⚠️ En el histórico **hay nombres repetidos entre meses** (`ST n°2 S1.png` existe en
julio y en agosto, `ST n°4 S1.png` en julio y septiembre), así que se guardaron con
la fecha por delante. Bajarlos por nombre se pisaría uno a otro.

⏳ **Falta a propósito** `Reel n°1 Recap Novios F 2026.mp4`: pesa **312 MB** y no se
bajó sin preguntar. El enlace está en la carpeta.

**⭐ Lo que esto habilita:** Piso 18 queda con **26 piezas fijas aprobadas** en
disco (9 en `ref-cumple/` + 17 en `ref-aprobadas/`) y 3 piezas de movimiento. Ése
es el corpus que le faltaba a `qa/calibrar.py` para medirle topes propios a la
marca en vez de dejarle los de agencia: hoy `clients/piso18/reglas.yaml` tiene
**2 reglas** y ninguna calibrada contra material propio.
