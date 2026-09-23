# PISO 18 — qué falta para que el sistema corra solo

> Actualizado **22-09-2026**, al escribir el manual y la ficha. Marcar `[x]` cuando
> llegue y borrar la fila al resolverse.
>
> ⭐ **El sistema de Piso 18 ya estaba armado**: kit de código medido, 20 cortes de
> IvyPresto en el repo, logotipo limpio recortado y reglas de QA calibradas contra las
> piezas aprobadas. Lo que faltaba era el manual legible, y eso se escribió hoy.
> Lo de abajo es lo que sigue abierto de verdad.

## 🔴 Bloqueantes — sin esto hay que improvisar cada vez

| # | Qué | A quién | Por qué bloquea |
|---|---|---|---|
| 1 | **Las 10 piezas aprobadas de la S1** (carpeta `P18`) | **Eli** | `raw/hilton/piso18/ref-eli-sep2026/` está **vacía**. La gramática hoy está medida sobre **7 piezas** y el método pide 20–60: con esa muestra los dos registros (promo y editorial) están descritos, pero no se puede afirmar qué pasa con los casos que no aparecen |
| 2 | **Abrir la lectura del Drive** — ampliar el token del estudio a `drive.readonly`, o compartir por enlace las 3 carpetas de referencias | **Valeria** | Las 11 referencias de `ref-cumple` son HTML de login desde el 16-09. Mapa completo con `fileId` en [`REFERENCIAS-CUMPLE.md`](REFERENCIAS-CUMPLE.md). Es la misma decisión abierta desde el 14-09 en Between |

## 🟡 Importantes — mejoran calidad y velocidad

| # | Qué | A quién | Para qué |
|---|---|---|---|
| 3 | Acceso al **banco del disco `F:`**, o una copia de `3-Finales 2026` | Eli | El banco real no está en Drive ni en el repo: hoy sólo hay una muestra. Sin él, cada pieza depende de que Eli mande la foto |
| 4 | Confirmar si los **1080×1080** son piezas de publicación o previews de grilla | Eli | Cambia si el sistema tiene tres formatos o dos |
| 5 | ¿Existe **manual de marca** del cliente? | Eli / KAM | Para saber si `#D4145A` está documentado por el cliente o sólo vive en los editables |
| 6 | Que un **check de respiro de borde** sepa separar el texto de la foto | — | Hoy la regla mide la foto, no el texto: una portada de carrusel de sólo foto puntúa igual que un texto pegado al borde. Queda anotado en `reglas.yaml` que **eso se revisa mirando** |

## 🟢 Deseables

| # | Qué | Para qué |
|---|---|---|
| 7 | Los `.ai` empaquetados completos (hoy sólo se leyeron los `Informe.txt`) | Medir geometría sobre el vector en vez de deducirla del render |
| 8 | Saber si la regla **«el brief es de contenido»** vale también para QB y Between | Está confirmada para DT y Piso 18; para las otras dos, no |

---

## Lo que necesito de ustedes cada vez
1. El brief con los textos **finales** — salen verbatim a la pieza.
2. Qué piezas y en qué formatos.
3. Si hay promoción: precio, vigencia y el legal exacto.
4. La carpeta de Drive donde subir.
5. El feedback **en los archivos de Drive** (comentarios), para que quede trazable.

## Lo que devuelvo
- Las piezas en su formato + los editables
- `ENTREGA.md` con qué es cada pieza, de dónde salió cada texto y qué quedó pendiente
- Todo subido a la carpeta del cliente
