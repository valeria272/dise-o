---
name: cliente-tierra-calma
description: "TIERRA-CALMA — cerebro del cliente: 51 reglas firmes, última cosecha 2026-09-25. Generado desde clients/tierra-calma/APRENDIZAJES.md; leerlo antes de diseñar para tierra-calma"
metadata:
  type: project
---

⚙️ **Nota generada por `scripts/memoria-cliente.py` en cada /cierre. No se edita acá:**
la fuente es `clients/tierra-calma/APRENDIZAJES.md` (léelo completo antes de producir; esto es
sólo lo más confirmado). ⛔ Vale sólo para tierra-calma: no se traspasa a otra marca.

Criterio: **Diego Aguilar** · Aprueba: **Fran (proyecto) · Blanca (comercial)**

## Reglas más confirmadas
- **R-29** · MAPA-1, MAPA-2 y cualquier referencia con topónimos corruptos no se publican nítidos; de una referencia se copia la gramática, nunca el contenido — _manual 14-09; referencias de Diego 24-09 y **25-09 (dos seguidas)**, todas con el mapa regenerado_ · ✔×4
- **R-41** · Cada ronda se re-sube **sobre el mismo fileId** de Drive — _bitácora 14-09 a 25-09_ · ✔×4
- **R-01** · Se llega por **Autopista del Sol · Ruta 78**; nunca «Ruta 68» ni escudos G-68 — _Carlos Figueroa, 21-08, brief reel ubicación; mapas corruptos 14-09; referencia de Diego 24-09_ · ✔×3
- **R-02** · Nunca «agua potable» ni «red de agua»: el agua es por noria o pozo que construye cada propietario — _Fran, brief de octubre 08-09 («dato verificado como falso»); alerta de sept 21-08; `reglas.yaml` 22-09_ · ✔×3
- **R-07** · Tuteo: «pásalo / pásala», nunca «pasalo»; los briefs de Ignacio traen voseo y se corrige siempre — _Diego, 23-09 (`sin-voseo`); se publicó «alcance» en sept; B4/D1 oct_ · ✔×3
- **R-20** · Una foto no se repite entre dos piezas del mismo mes (parecido > 0,85 = la misma, aunque el md5 difiera) — _Diego, 24-09, `c-20-10-1`; 25-09 medido antes de instalar `g-pareja2` (máx. +0,654) y detectado que `l-fondo` estaba en dos piezas_ · ✔×3
- **R-34** · Zonas seguras: story 250 arriba / 340 abajo; en PAID nada a menos de **70 px del filete** (se achica el elemento, no el margen) — _compuerta 23-09 `st-12-10`; Diego 24-09 PAID; 25-09 la compuerta atajó el titular subido a la fila 225_ · ✔×3
- **R-42** · Antes de entregar se corre la compuerta (`textos-tierracalma.py` + `qa/motor.py --marca tierra-calma`); si se toca el QA, se corre de nuevo sobre todas las piezas — _manual §4 septies, 23-09; bitácora 24-09; 25-09 atajó DOS bloqueantes (zona segura y foto estirada)_ · ✔×3
- **R-03** ⭐ · Sólo se publican datos de la lista blanca (~5.000 m², desde UF 2.500, 30 min de Santiago, 15 min del peaje, canchas, colegios/súper/bancos, electricidad subterránea, cierre perimetral, máx. 2 casas, Ruta 78 + Camino a Melipilla); lo demás, OK escrito de Fran o Blanca — _brief sept; propuesta de temas oct de Carlos, 08-09_ · ✔×2
- **R-04** · Prohibido sin validar: m² exactos, factibilidad de servicios, plusvalía numérica («2,8 % de rentabilidad»), cabañas/turismo (el reglamento limita a 2 casas) y otros condominios — _manual §2; alertas de la grilla sept, 21-08_ · ✔×2
- **R-06** · «Tierra Calma» en dos palabras y **nunca partido entre líneas**; tampoco «Padre Hurtado», «UF 2.500» ni «5.000 m²» — _Diego, 23-09 (grafía) y 24-09 reel `r-01-10` («siempre»), `p-29-10`_ · ✔×2
- **R-08** · Textos y CTA **verbatim** del brief; si no cabe se baja el cuerpo, el copy no se acorta — _Valeria, 19-08 (8 piezas parafraseadas); Diego, 23-09 `p-09-10`_ · ✔×2
- **R-09** · Tipografía **IvyOra + Inter Tight**; nunca Cormorant ni `loadGoogleFont()` — _Valeria, 19-08; Carlos 21-08 («cumple súper bien»)_ · ✔×2
- **R-14** · El bloque de texto va **centrado al medio** en la banda útil; si el medio lo ocupa el sujeto o una gráfica, se acota la banda (medida sobre el JPG de origen), no se mueve la gráfica — _Diego, 23-09 («que no tape las casas / a las personas»)_ · ✔×2
- **R-16** · El marco es **asset bloqueado**: no se redibuja ni se ensancha la píldora; cede el cuerpo del texto — _Diego, marcos 14-09; «botón muy apretado» `p-09-10`, 23-09_ · ✔×2
- **R-17** · El carrusel es un solo objeto: el filete se desplaza entre slides y se juzga montado en tira — _lenguaje de Carlos jul/ago; tira verificada 14-09_ · ✔×2
- **R-18** · Recuadro = **globo translúcido oscuro** (~0,55), derecho, centrado, ajustado al texto (`inline-block`), destacado y cuerpo juntos (8 px), sin cruzar las hairlines — _Diego, 22–23-09, `c-06-10-2`, `st-22-10`, `st-08-10`, `c-20-10-4`_ · ✔×2
- **R-23** · La IA respeta la **estructura real** (ladera, ripio ocre en curva, cerco de madera oscura, postes) y la vegetación se idealiza con **nativas** (espino, quillay, litre, peumo); nunca pradera europea, flores masivas ni cordillera nevada de postal — _Carlos #7, 21-08; Diego, 22-09 `st-08-10`_ · ✔×2
- **R-24** · La imagen tiene que verse **creíble**: si hay foto real que sirve, cambio mínimo sobre ella («do not add, do not remove»); no se inventa paisaje (nada de skyline de Santiago); lo que la foto no muestra lo cuenta el texto — _Diego, 24-09, PAID 02-B y casacabe_ · ✔×2
- **R-26** · Gente **de espaldas o de lejos**, nunca mirando a cámara; sin personas identificables — _brief (manual §5); Diego, 23-09 PAID_ · ✔×2

## Lo que ya costó rondas
- **X-01** · Reusar los clips genéricos `tc1_mist`…`tc5_flare` (ya publicados) — _Valeria, 19-08_
- **X-02** · Estáticos sobre dron con neblina, maquetados a ojo («el post del 18 es horrible, plano, fome») — _entrega sept, 19-08, rechazo completo y rehecha_
- **X-03** · Parafrasear el brief o meter montos de la ficha técnica en la historia comercial — _Valeria, 19-08, 8 piezas_
- **X-04** · Marco con divs superpuestos (muñón en las esquinas), textos pegados a filetes, píldora a 6 px de la flecha — _Valeria, 20-08, 3.ª ronda de sept_
- **X-05** · Logo con las líneas laterales del PNG fuente — _Carlos, 21-08_
- **X-06** · Titular sobre el terreno, la casa o el pasto — _Carlos, 21-08_
- **X-07** · Praderas verdes con cordillera nevada (otro país) y, en el otro extremo, el sitio árido sin idealizar — _entrega 14-09; Diego 22-09_
- **X-08** · Cursiva a 96–104 pt aplastando la sans; bold de la sans para destacar; demasiadas tipografías — _Diego, 22–23-09_
- **X-09** · Cajas de color macizo o tarjetas inclinadas como recuadro de texto — _Diego, 22-09_
- **X-10** · Degradado azul que se come el mapa — _Diego, 23-09, `st-12-10`_
- **X-11** · Mapa inventado: captura velada, celdas dibujadas, máscara radial, recuadro-estampilla — _`st-12-10`/`c-20-10-2`, 22–24-09, 4 rondas_
- **X-12** · Nuestro rótulo o pin encima del pin de Google Maps de Tierra Calma — _Diego, 24-09_
- **X-13** · Post-it dibujado con CSS (se lee como tarjeta digital) y el dato comercial en un recuadro de marca sobre el refrigerador — _Diego, 24-09, `p-29-10`, 3 vueltas_
- **X-14** · Reusar la cenital DJI_0335 y la foto del asado ya publicadas en pauta — _Diego, 23-09, PAID ronda 2_
- **X-15** · Santiago en el horizonte generado con IA («se ve demasiado falsa») — _Diego, 24-09, PAID 02-B, rondas 4–5_
- **X-16** · Elementos pegados al borde del marco en PAID («que ningún elemento quede tan al borde») — _Diego, 24-09, mapa30min 4:5_
- **X-17** · El mapa **trazado**: líneas extraídas por gradiente, en cuatro vueltas —tinta proporcional, línea binaria, línea engrosada y calle maciza—. «Los trazos quedan mal y pixelados» — _Diego, 25-09, 4 rondas_
- **X-18** · **Ampliar** una captura de mapa para llenar la ventana (873 px estirados a 1080 = 24 %) — _Diego, 25-09_
- **X-19** · Cambiar el copy de una slide por un panel de datos que el brief no pidió — _Diego, 25-09, «no cambies el contenido, vuelve al texto de antes»_
