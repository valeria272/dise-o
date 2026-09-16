# Bitácora — Casablanca

## 2026-09-16 — Serena Abarca (con Claude)

**Qué se hizo:** Jenny corrigió por WhatsApp el Cumaru: *«viene en largo variable y
tabla corta. No larga como dice el anuncio»*. Se rehízo `cb_sep_c1-4-cumaru` en los tres
formatos — etiqueta `12/2 · 120 mm` (sin cifra de largo) y bajada **«LARGO VARIABLE: EL
ENTABLADO DE TODA LA VIDA»**. La bajada costó cuatro intentos, y los tres primeros
fallaron por arrastrar la copy vieja: se conservaba «angosta» —que es el ANCHO, ya va en
la etiqueta y nadie discutía— y en el primero incluso se perdió «corta», que es lo que
Jenny vino a corregir. Serena lo paró dos veces. Después, viendo la pieza corregida, la
propia Jenny sacó también «tabla corta»: *«dejar solo largo variable en la primera línea
por favor»*. Su primer mensaje nombraba la tabla corta para **explicar el error**, no
para que fuera la copy — en un anuncio «corta» se lee como defecto. La regla que queda:
cuando se corrige un dato, la línea habla del dato corregido y de nada más. La causa raíz no fue nuestra redacción: la ficha
oficial del cliente dice **«Largo (mm): 2.130 LV»** y al transcribirla se copió el 2130 y
se perdió el `LV` (largo variable), que es el tope y no el largo. Se propagó la corrección
a los 10 lugares donde vivía el dato malo: `marca.json`, el manual, la receta de fondos,
los dos generadores de ambientes, el compositor de pisos —que ahora acepta `largo` como
rango y lo sortea tabla por tabla— y las 4 composiciones TSX registradas en Studio, que
de paso seguían con «Cumarú» con tilde pese a la derogación del 31-08. Detalle completo en
[`feedback/2026-09-16-cliente-cumaru.md`](feedback/2026-09-16-cliente-cumaru.md).

**Dónde quedó:** Las 12 de C1 rendidas en `out/casablanca/septiembre` (las otras 3
tarjetas salen iguales: el cambio está acotado al Cumaru) y copiadas al Escritorio, en
`CASABLANCA — Cumaru corregido 16-09-2026`, con los tres formatos del Cumaru sueltos, el
carrusel completo en una subcarpeta y un `LEEME.txt` para Jenny. QA del estudio: **las 12
pasan las 11 reglas**, esta vez con los textos declarados vía `--textos`, así que las
reglas de copy —«Cumaru» sin tilde, palabra sola en la última línea, sin precios— quedaron
verificadas de verdad y no «SIN VERIFICAR». Typecheck limpio. **Nada subido al Drive** —
este Mac no tiene token.

> ⚠️ **El primer render quedó atrás de la copy.** Las PNG de las 10:00 todavía decían
> «TABLA CORTA Y LARGO VARIABLE» (la versión 3): el cambio de las 11:13, cuando la clienta
> sacó «tabla corta», se escribió en el script y en los cuatro TSX pero **no se volvió a
> renderizar**. Se rehizo el 16-09 a las 12:16. Si se toca una copy, se re-renderiza y se
> mira el PNG: el script corregido no es la entrega.

**El cuerpo de la bajada no se disparó.** Quedaba anotado medirlo después de sacar «TABLA
CORTA Y», porque la bajada se autoajusta al ancho del filete. Medido: el cuerpo no se
mueve (24,5 en feed · 26,5 en 4:5 · 30,6 en story, idéntico a la versión 3), porque la
línea que manda no era «TABLA CORTA Y LARGO VARIABLE:» sino «EL ENTABLADO DE TODA LA
VIDA» —617,8 px @1080 contra un tope de 701,1—, y ésa no cambió. Contra las hermanas en
4:5: Aserrado 25,0 · Cumaru 26,5, dentro del rango que ya existía en el carrusel. No hubo
que topear nada.

**Este Mac se había quedado sin las librerías de Python.** Faltaban `fontTools`, `numpy` y
`scipy`: sin las dos primeras el script no arranca, y sin `scipy` el QA **no falla, pasa**
—las 8 comprobaciones geométricas se reportan como «la comprobación reventó» y el resumen
dice «0 avisos»—. Se instalaron. Un QA que no puede correr una regla no es un QA aprobado:
hay que leer la línea de «sin verificar», no sólo la de avisos.

**Qué sigue:** Entregarle a Jenny las 3 del Cumaru y avisarle que su propio sitio publica
el dato igual de confuso (`120 x 2130` sin el LV, y con la especie escrita «Camarú»).

**Abierto:**
- Lo anterior del 27-08 sigue abierto: c2-3, la serif sustituta y el SKU 8001021068.

**Dos cosas que se cerraron el mismo día:**
- ✅ **La foto del Cumaru está bien.** Yo había dicho que mostraba tablas largas y que
  había que regenerarla: **era un diagnóstico equivocado**, hecho leyendo el prompt en vez
  de mirar el piso de cerca. El ambiente aprobado tiene juntas de tope frecuentes y
  salteadas. Se intentó regenerar igual y salió peor en todo (Δtono 9,3° contra 1,0°,
  Δsat 0,149 contra 0,062, y la madera se leía como roble con nudos, que es justo lo que
  Jenny rechazó el 28-08). La generación se descartó. **No rehacer este ambiente.**
- ✅ **`clients/casablanca/reglas.yaml` corregida.** La regla `grafia-cumaru` exigía
  «Cumarú» CON tilde citando a Valeria (25-08), cuando la clienta lo derogó el 31-08. El
  QA llevaba dos semanas pidiendo lo contrario de lo que manda; no saltaba sólo porque
  quedaba «SIN VERIFICAR».


## 2026-08-27 — Serena Abarca (con Claude)

**Qué se hizo:** Septiembre pasó a 4:5 + story por decisión de Serena, lo que cierra el
punto 5 del `CHECKLIST-CLIENTE.md`. Se ordenó la carpeta del Drive, que tenía dos
entregas con numeración cruzada —los 14 sueltos se autodenominaban «v3» siendo anteriores
a la subcarpeta «V2»—. Se resolvió el choque entre los lineamientos 2 y 5 del brief, que
no se pueden cumplir juntos con el texto anclado al pie: se dejó el texto abajo y el nº5
se cumplió por donde importaba, la legibilidad, con `velo_medido()` — mide el fondo y
calcula el alfa justo para 5:1, así el cumarú casi no lleva velo y conserva su madera.
Se rehicieron tres muestras de tabla desde la foto oficial del cliente y se regeneró el
ambiente del cumarú, cuyo prompt decía «chocolate» y salía más oscuro que el producto real.
De los comentarios de Serena sobre C2: degradado detrás del texto en las tres, encuadre
de c2-1 para que no corte «Pisos de Madera», y logo despegado del borde en c2-2.

**Dónde quedó:** Las 14 rendidas en `out/casablanca/septiembre` (feed45 + story) y en el
escritorio, carpeta `version nueva`, ordenadas en C1 y C2. En el Drive sólo están las 6
de C2, subidas antes de estas correcciones. QA del estudio sin avisos.

**Qué sigue:** Subir las 8 de C1 al Drive y revisarlas — es donde vive la preocupación de
Serena de que el piso del ambiente corresponda al SKU.

**Abierto:**
- **c2-3 sin resolver.** El «6359» no sale con ningún encuadre 4:5 sin romper otra cosa;
  se probaron tres. Falta la foto: el brief pide «un piso instalado o una vista acogedora»
  y de las 36 de la clienta, 32 son fachada.
- **Cumarú o Camarú** — el brief dice uno, el sitio del cliente el otro. Va en grande.
- **La serif del titular es un sustituto** (Bodoni Moda Italic). 5 minutos de Valeria en
  Creative Cloud, punto 1 del checklist.
- **El SKU 8001021068 (167 × 1200)** no tiene foto oficial: es el único cuyo piso no se
  pudo verificar por ΔE. Los otros tres pasan con 14,5 / 15,4 / 17,3 sobre umbral 20.
- **La geometría 4:5 es la de Valeria**, medida contra 6 piezas reales de Paulina. Sus
  ambientes 4:5 nativos existen pero ella los marcó no entregables (el techo con vigas
  ocupa el tercio superior y el logo cae encima); hoy se usan los cuadrados recortados.
