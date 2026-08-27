---
name: no-inventar-sistema-de-marca
description: "Feedback duro 24-08/25-08: si el cliente ya tiene plantilla viva aprobada, la pieza nueva la EXTIENDE. Incluye la lección de MEDIR las referencias en vez de aplicar criterios propios (zonas seguras) que las contradicen"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 2ee37e44-26d8-4ffd-98e0-423ea7592df4
  modified: 2026-08-24T21:28:14.084Z
---

# Cuando el cliente ya tiene sistema, no se inventa otro

En un carrusel de septiembre 2026 diseñé las 4 piezas desde cero: fondos oscuros con velo
lateral, texto alineado a la izquierda en minúsculas, bloques rojos macizos con
párrafos, cajas blancas y listas de horarios. Valeria lo rechazó de una:
«cuando hiciste los archivos de prueba habías respetado lineamientos,
ahora son un desastre».

**Por qué:** el cliente ya tenía una **plantilla viva aprobada** —el carrusel de
laminados ya aprobado— con su gramática: foto
full-bleed, bloque rojo del logo colgando arriba, texto centrado en la mitad
inferior, titular MAYÚSCULAS 800 con la línea clave en barra roja, bajada bold +
regular, cápsula de borde blanco, CTA en cápsula negra y el sitio al pie. Cada
pieza nueva que se sale de eso rompe la serie y obliga a rehacer.

**Cómo aplicarlo:**
1. Antes de escribir una línea, **abrir la composición aprobada y las salidas en
   `out/<cliente>/`** y copiar los valores reales (tamaños, paddings, colores,
   posiciones), no una idea general del estilo.
2. Los recursos que describe el brief o las referencias de la clienta se
   **traducen a la gramática existente**: si el brief pide «bloque de datos
   separado» o «dato en recuadro», eso se resuelve con la cápsula de borde blanco
   del sistema, no con un elemento nuevo.
3. El brief manda en **qué** dice la pieza (datos, CTA, medidas, tono). El sistema
   de la marca manda en **cómo** se ve. No confundir los dos.
4. Si de verdad hay que salirse del sistema, se avisa y se explica antes de
   rendir, no después.

Ver [[ctas-verbatim-del-brief]].


## Corolario (25-08): medir la referencia, no aplicar mi criterio por encima

Valeria tuvo que corregirme **dos veces lo mismo**: los logos quedaban «al medio
volando». La causa no fue descuido: fue que **apliqué un criterio propio —bajar el
logo para respetar la zona segura de Instagram— por encima de lo que hacen las
referencias**, que lo llevan pegado al borde (`top = 0`).

Lecciones concretas:
1. **Cuando exista la referencia, se MIDE.** Abrir el archivo y sacar los valores con
   PIL/numpy (posición, tamaño, hex) en vez de estimar a ojo o razonar desde
   principios generales. Así se resuelven los valores de un sistema.
2. **Una buena práctica general no vence a la marca.** Las zonas seguras son un buen
   criterio de pauta, pero si la diseñadora pone el logo al borde en todas sus piezas,
   eso es el sistema. Lo correcto es respetarlo y, si preocupa, **decirlo** — no
   corregirlo en silencio.
3. **Dos marcas hermanas necesitan esqueletos distintos, no solo paletas distintas.**
   La primera ronda de previews usó el mismo layout con otro color y Valeria lo cazó al
   instante: «son MUY similares».
4. **Ojo con los derechos de imagen:** las fotos con personas del equipo no se usan.
   Preguntar antes de dar por hecho que una foto entregada se puede publicar.

## Nota técnica: no truncar archivos al editarlos
`io.open(p,"w").write(io.open(p).read()+extra)` **borra el archivo**: Python abre en
modo `w` (truncando) antes de evaluar el argumento que lo lee. Esto destruyó cuatro
memorias en esta sesión y hubo que reescribirlas. Siempre leer a una variable primero,
después abrir en escritura.

## Corolario 2 (26-08): un RANGO en palabras no es una medida — y la marca vive en el techo

Between se rechazó entero por esto. El kit decía «titular rango 40–122» porque así lo
describió la diseñadora, y yo me senté cómodo en la mitad (56–70). Al medir sus piezas
publicadas, los titulares reales son de **97**. Todo lo demás se caía en cascada: la
script quedó como segunda línea decorativa (1,2× en vez de 1,92×), el bloque centrado
y flotando en vez de anclado arriba a la izquierda, y faltaban dos elementos enteros
del lenguaje (la caja taupe y el texto en arco).

**Cómo aplicarlo:**
1. **Un rango descrito en palabras es una señal de que falta medir, no un permiso para
   elegir.** Si el manual dice «entre X e Y», ir a las piezas y sacar el número real.
2. **La fuente más fiel son las ENTREGAS TERMINADAS del diseñador**, no el brief y no
   los `.ai` (pesan 500–700 MB y no se abren). Están en las carpetas de entrega semanal
   del Drive. Buscarlas antes de inventar un layout genérico.
3. **Si no puedes abrir el editable, no rellenes el hueco con un layout seguro.**
   Pide un PDF de las mesas de trabajo o mide las piezas publicadas. Un template
   genérico repetido 27 veces se lee como plantilla, no como grilla.
4. **Calibrar contra el propio render.** No basta con despejar el cuerpo tipográfico por
   cálculo: Brushwell sale ~20 % más ancha en Chrome que en PIL. Renderizar, medir la
   propia pieza con la misma máscara que la del diseñador, y corregir hasta que la
   tinta calce.
5. **Dejar una prueba A/B en el repo** (`BW-P-MatchPerfecto`) para poder verificar antes
   de rehacer una grilla completa.

Ver [[between-sistema-grilla]] · [[hilton-cliente-4-marcas]].


## Corolario 3 (25-08): el benchmark es el FEED PUBLICADO, no la entrega del mes

Una cuenta se rehízo entera por esto. Yo tenía documentado como "el sistema" el
carrusel de mayo de la diseñadora —caja blanca de logo centrada arriba, muestra
vertical con caja gris, todo centrado— y las piezas salían con esa gramática.
Valeria mandó cuatro publicaciones del **feed real de la marca** y eran otro
sistema: foto a sangre, placa gris del logo al costado, bloque de texto editorial
alineado a la izquierda.

**Cómo aplicarlo:**
1. Antes de cerrar el sistema de una marca, **mirar lo que publica**, no sólo los
   editables de la entrega del mes. Una marca puede tener dos registros vivos.
2. Cuando el cliente diga "esto no alcanza el estándar", **no ajustar**: preguntar
   contra qué referencia se está midiendo y replantear desde ahí.
3. Si la instrucción nueva contradice el brief (acá: "un mismo ambiente en las 4
   tarjetas" y "el texto nunca va sobre la madera"), **se deja escrito en el
   código y en el manual** para que no se lea como descuido.

## Corolario 4 (25-08): una métrica no reemplaza al ojo

Para calzar el piso con la foto oficial del producto armé una gradación en Lab
que bajaba el ΔE de 16 a 5… y dejaba la madera **naranja** y con manchones sobre
las cortinas. El número mejoraba y la pieza empeoraba. La corrección se descartó
y el script quedó como **medidor** (ΔE ≥ 20 = es otro producto), no como
corrector. El color de la madera se controla en el prompt del generador.
