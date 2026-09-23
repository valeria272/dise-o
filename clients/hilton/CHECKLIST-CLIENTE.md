# HILTON — qué falta para que el sistema corra solo

> Actualizado 09-09-2026. Marcar `[x]` cuando llegue y borrar la fila al resolverse.
> Cubre **DT** y **PISO18**, en bloques separados. QB y Between se agregan cuando entren.
>
> ⛔ **Los bloques no se cruzan.** Piso18 es marca propia y nada de DT le sirve de
> reemplazo — ni una tipografía, ni un color, ni una foto.

## 🔴 DT — Bloqueantes — sin esto hay que improvisar cada vez

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
| 5 | ~~**Fotos del gimnasio**, no video~~ **RESUELTO 21-09** | — | Los 7 `.MOV` de `CONTENIDO HOTEL 2026 › GYM` **sí sirven**: traen la misma ficha técnica que la sesión de video del hotel y resolvieron la lámina del gym del carrusel S5 (`IMG_1700`). Para una estática, un fotograma de esos MOV o las fotos `HDT_81/82/83` |

## 🟢 Deseables

| # | Qué | Para qué |
|---|---|---|
| 6 | Las 24 fotos `.HEIC` de «Recursos gráficos» convertidas a JPG | HEIC no lo abre Chrome ni Remotion. Hoy esa carpeta es inutilizable desde código |
| 7 | Confirmar el azul: `#09194E` del manual vs `#111C4E` del Pantone exportado | Para fijar uno solo y que el QA rechace el resto |

---

## 🔴 PISO18 — Bloqueantes

> Piso18 tiene **0 de las 7 capas** del sistema. Nada de DT sirve de reemplazo.

| # | Qué | A quién | Por qué bloquea |
|---|---|---|---|
| P1 | **Las 10 piezas aprobadas de la carpeta `P18`** de la S1 (`1TR-CiAE84ryQ1gTA2PvkEthsWhwSm5yA`) — por enlace, o copiadas a `raw/hilton/piso18/ref-eli-sep2026/` | Eli | Es la única gramática que existe. Las 14 piezas conocidas **devuelven ~908 KB de página de login**. Sin ellas no se miden las capas 1, 2 y 3, y el examen de admisión (reproducir una pieza ya aprobada hasta que quede idéntica) **es imposible** |
| P2 | **Los editables de Piso18** — el `.ai` con sus carpetas `Fonts/` y `Links/`, y sobre todo el **`Informe.txt`** | Eli — ya comprometidos el 09-09 | El `Informe.txt` es la fuente más fiel de fuentes, mesa de trabajo y prompts, y evita bajar un `.ai` de cientos de MB. Con eso corre `/adn piso18` |
| P3 | **El logo P18 en PNG con transparencia**, y qué versión va sobre fondo claro y cuál sobre oscuro | Eli | Hay un pendiente del cliente —«aquí quedó algo extraño detrás del logo de P18, podemos revisarlo?»— que **no se puede ni diagnosticar** sin el archivo |
| P4 | **Las tipografías propias de Piso18** | Eli / Cliente | ⛔ **No son las de DT.** El repo no tiene ninguna de las dos familias, y asumir Stag/Trade sería mezclar marcas |
| P5 | **La carpeta de la galería del fotógrafo** | Eli / Cliente | La grilla la nombra en 4 piezas («galería fotografo», ambiente de matrimonio, arreglos florales). Sin ella no hay imagen, y la jerarquía obliga a foto real antes que IA |

## 🟡 PISO18 — Importantes

| # | Qué | A quién | Para qué |
|---|---|---|---|
| P6 | La medida del **máster** de feed y de story | Eli | DT y Between son 2250 × 2813. Para P18 **no se asume** |
| P7 | Fotos de **bautizo** y de **corporativo** | Cliente | Son dos de las cinco verticales. El banco no las cubre y **bautizo no aparece ninguna vez** en septiembre |

## Decisiones abiertas de Piso18 — las dicta Eli, no se resuelven solas

- ¿La **§G** (en esta cuenta sólo se diseña; el brief es del cliente) vale para Piso18?
  Se dictó para DT y sigue sin extenderse.
- ¿La regla de **no usar rostros de trabajadores** vale para Piso18? La grilla de P18
  pide por su cuenta «cambiar caras con IA» y «sin caras directas», así que va en la
  misma dirección — pero la regla no está dictada.
- **¿Quién hace las semanas 2 y 3?** Hay **13 piezas en `OK PARA DISEÑAR`** y no existe
  carpeta `P18` en la S2 ni en la S3, mientras Between tiene las tres.

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
