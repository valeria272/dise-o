# `ref-cumple/` — de dónde sale cada archivo

> Escrito el **22-09-2026**. Cuatro `/arranque` seguidos (16, 17, 21 y 22-09)
> reportaron «11 archivos rotos» sin que nadie supiera **de dónde** rebajarlos.
> Acá está el origen, identificado por peso exacto de los dos que sí llegaron bien.

Todo cuelga de `PISO18 › <carpeta de referencias de Eli>`
(`1MDm5JLRBe_Ep99hhK7fHgZ2mg35y9MJ2`), creada por Eli el 15-09-2026 —
la misma fecha y hora en que se creó esta carpeta local.

## El mapa

| Local | Origen en Drive | fileId | Bytes | Estado |
|---|---|---|---|---|
| `actual-1.png` | `CARRUSEL CUMPLE ACTUAL 2026` › `C1 S3 n°1.png` | `1_4BJqdQXgj5zgZI32nGCRD9I7YxsQvWx` | 2.979.282 | ✅ bueno |
| `actual-2.png` | `CARRUSEL CUMPLE ACTUAL 2026` › `C1 S3 n°2.png` | `1u-3lMmvCvg3bd42dl8ym_Ip3W2QvyIr6` | 8.660.362 | ⛔ HTML |
| `actual-3.png` | `CARRUSEL CUMPLE ACTUAL 2026` › `C1 S3 n°3.png` | `1PToN-oAda05MLhIvIzyDVxrH7ZC23tIj` | 7.021.442 | ⛔ HTML |
| `actual-4.png` | `CARRUSEL CUMPLE ACTUAL 2026` › `C1 S3 n°4.png` | `1-VeOblL2AXm20yNh0yZLL6K3wkl8fe4Z` | 7.325.533 | ⛔ HTML |
| `benef-1.png` | `BENEFICIOS CUMPLEAÑOS` › `C2 S1 P18 1.png` | `1w7ZW4SZZezFpSATA8hRxoqA4EA0GCFUw` | 10.014.738 | ⛔ HTML |
| `benef-2.png` | `BENEFICIOS CUMPLEAÑOS` › `C2 S1 P18 2.png` | `1pUMS5OCX7Po4JhSzk4wNOo7Hob-EaMnZ` | 7.162.976 | ⛔ HTML |
| `benef-3.png` | `BENEFICIOS CUMPLEAÑOS` › `C2 S1 P18 3.png` | `18GJDwwzggwRdubmfLU-TAWqXTYe4opX4` | 8.649.502 | ⛔ HTML |
| `viejo-1.png` | `CARRUSEL CUMPLEAÑOS` › `C1 S4 N°1.png` | `1_EVRCEBuNFI6qb-7exyDsZJC1raclXag` | 2.360.602 | ⛔ HTML |
| `viejo-2.png` | `CARRUSEL CUMPLEAÑOS` › `C1 S4 N°2.png` | `1GjGtDxZQKgK066fiMX1CTZi7w81QyA0q` | 2.552.923 | ✅ bueno |

Las tres carpetas de origen:

| Carpeta | folderId |
|---|---|
| `CARRUSEL CUMPLE ACTUAL 2026` | `1cA0YdoriGf5MqojdPvn6ITG8T3xOBoWj` |
| `BENEFICIOS CUMPLEAÑOS` | `1PB29U8qiujZPWHV9H5r0f2uFzQcGtXqx` |
| `CARRUSEL CUMPLEAÑOS` | `1zcVji_qzbYZ_-6evVzHLxD41Ra5VXTEt` |

⚠️ **Los cuatro `.jpg`** (`actual-2/3/4.jpg`, `benef-1.jpg`) no existen en Drive:
en el origen **todo es PNG**. Son un segundo intento de descarga que volvió a traer
el mismo HTML. No hay nada que rebajar para ellos — se borran.

## ⛔ Por qué falló, y por qué sigue fallando

Los dos archivos buenos son **el primero de su carpeta**: se bajaron por el conector
MCP de Drive, que va autenticado. Los otros siete se intentaron por `curl`, y ahí
Drive devuelve los ~915 KB de la **página de login**.

Verificado hoy, 22-09, archivo por archivo:

| Vía | Resultado |
|---|---|
| `drive.usercontent.google.com/download?…&confirm=t` | ⛔ 915.456 bytes de `<!doctype html>` — **las carpetas de Eli no están compartidas por enlace** |
| Token del estudio (`scripts/drive-bajar.py`) | ⛔ `HttpError 404 File not found` — el token es scope `drive.file` y no ve archivos que no creó él |
| Conector MCP `download_file_content` | ✅ funciona, pero devuelve **base64 al contexto**: estos PNG son de 7 a 10 MB cada uno y no caben |

## Las dos salidas — es decisión de Eli

1. **Compartir por enlace** las tres carpetas de arriba («cualquiera con el enlace
   puede ver»). Con eso `curl` las baja sin tope y en paralelo
   (memoria `bajar-grilla-ajena-de-drive`). Es lo más rápido. Ojo con la alerta
   `drive-agencia-permiso-abierto`: abrir carpetas tiene costo.
2. **Ampliar el token del estudio a `drive.readonly`.** Arregla esto y todo lo que
   venga después, en todas las marcas. Es la misma decisión que quedó abierta el
   14-09 en Between.

Hasta entonces **Piso 18 sigue bloqueado para diseñar**: sus referencias no se abren.
