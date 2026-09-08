# HILTON — qué falta para que el sistema corra solo

> Actualizado 08-09-2026. Marcar `[x]` cuando llegue y borrar la fila al resolverse.
> Por ahora sólo cubre **DT**; QB, Between y Piso18 se agregan cuando entren al sistema.

## 🔴 Bloqueantes — sin esto hay que improvisar cada vez

| # | Qué | A quién | Por qué bloquea |
|---|---|---|---|
| 1 | **Trade Gothic LT Std Bold** (ancho normal, archivo `.otf`/`.ttf`) | Cliente — DT | Es el corte con el que está compuesta la cifra de las piezas aprobadas. Sin él **ningún bloque de precio se reproduce igual**: el único sustituto, Bold Condensed No. 20, comprime la píldora de ~630 px a ~410 px al mismo alto de dígito. Afecta a Family Time, Escapada Romántica, Noche de Bodas y a toda pieza con tarifa |
| 2 | **Stag LCG** — Bold, SemiBold Italic, Medium Italic y Book Italic | Cliente — DT | Es la tipografía primaria que nombra el manual. La Stag que tenemos trae **354 glifos y no incluye `$ % ¿ ¡ @`**, así que hoy un titular **no puede llevar signo de pregunta ni de peso**. Es la causa real de la regla «precios y preguntas en Trade» |

> Las dos son de licencia Hilton y **no se pueden comprar por fuera para saltarse el
> trámite**: el manual (§2.4) dice que las fuentes oficiales no se comparten ni se
> descargan. Tienen que llegar del cliente o de su equipo de marca
> (`dt.marketing@hilton.com`).

## 🟡 Importantes — mejoran calidad y velocidad

| # | Qué | A quién | Para qué |
|---|---|---|---|
| 3 | El **contenido de la reseña de Booking**: texto literal, iniciales del huésped y rating | Carlos Figueroa | El estático del 14-09 está `OK PARA DISEÑO` pero **no se puede componer sin el texto**. La carpeta de reseñas (`1Dlki995RRdwueFGlZOkF9rybf7maMJ5u`) no devuelve archivos por el conector |
| 4 | El **`Informe.txt`** de `GRILLA FEED DT S1 SEP` | Eli | Es el único de los nueve paquetes que llegó sin informe. Son 15 KB de texto y evitan bajar un `.ai` de 373 MB para saber sus fuentes y mesas |
| 5 | **Fotos del gimnasio**, no video | Cliente — DT | La grilla pide contenido propio del gimnasio sin modelos, y lo único que hay son 7 `.MOV` de iPhone. Se puede sacar un fotograma, pero una foto real es mejor |

## 🟢 Deseables

| # | Qué | Para qué |
|---|---|---|
| 6 | Las 24 fotos `.HEIC` de «Recursos gráficos» convertidas a JPG | HEIC no lo abre Chrome ni Remotion. Hoy esa carpeta es inutilizable desde código |
| 7 | Confirmar el azul: `#09194E` del manual vs `#111C4E` del Pantone exportado | Para fijar uno solo y que el QA rechace el resto |

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
