## 2026-09-24 — Coni (con Claude) · CYBER: ocho rondas sobre las cuatro piezas

**Qué se hizo:** día entero de correcciones sobre las tres propuestas y la pieza
PRUEBA del Cyber de octubre. Ninguna pieza nueva: las cuatro que ya existían,
afinadas ronda por ronda con el feedback de Coni —parte por chat y parte por
**comentario de Drive**, que se lee con `scripts/drive-comentarios.py`.

**Lo que cambió, en orden:**

1. **El sello Descorchados, igual en las cuatro.** Estaba en 517 px en A, 364 en
   B y 435 en C. Coni: «el Prop C es el mejor tamaño». Se unifica en 435 y —lo
   importante— **el diámetro deja de depender del encuadre**: antes, al agrandar
   una escena, el sello crecía con ella.
2. **La escena de C, menos agrandada** (×1,26 → ×1,08): se perdían los
   acompañamientos.
3. **El descuento**, tres rondas: del recuadro naranja al negro del Cyber, y de
   ahí a un **DISCO**. Ver abajo.
4. **UNA SOLA ADVERTENCIA por pieza.** Se había entendido mal «agregar otro
   recuadro» y se pusieron dos. Va una, la de conducir.
5. **La sombra de la botella en PRUEBA**, tres rondas hasta quedar bien.

**⛔ LA ADVERTENCIA DE CONDUCIR: NO SIRVE CUALQUIER PÁGINA DEL PDF.**
`ADVERTENCIAS_BEBIDAS-ALCOHOLICAS.pdf` la trae en 11 páginas y casi ninguna vale:

| Páginas | Problema |
|---|---|
| 27 y 43 | dicen «LIMITA LA CAPACIDA DE CONDUCIR» — **les falta la D**. Errata del documento oficial |
| 6, 10, 30, 34, 38 | llevan el Ministerio y la banda tricolor **arriba**, al revés que en CAVA |
| 22 | correcta, pero cuadrada: al ancho que deja la banda legible su alto se va a 620 px y la banda **cae fuera** de los primeros 520, que es donde `franja_legal` la busca |

**Se usa la 18**, exportada a **940 px** de ancho y no a los 808 de la anterior:
el check exige 60 px de azul y de rojo en la misma fila **sobre la pieza
reducida**, y a 808 daban 56 → rechazaba la pieza. A 940 dan 65.

**⛔ LA SOMBRA: EL DIAGNÓSTICO BUENO ERA EL TERCERO.** Coni la marcó tres veces.
Las dos primeras se diagnosticó mal —se culpó a la orientación y luego al
fondo—. Lo que pasaba, apagando las capas una por una:

- estaba armada con **elipses superpuestas** y la suma de sus bordes difuminados
  dejaba un borrón que no correspondía a ninguna forma real;
- era **enorme**: la capa mayor daba 1632 px contra 887 que mide la botella;
- e iba **corrida 266 px** al costado.

Ahora **se deriva del alfa de la propia botella**: su tercio inferior, aplastado
contra la mesa, desplazado apenas y difuminado. Medido: ocupa de −454 a +236 px
respecto al centro, con la botella en ±443. Queda **debajo**.

**El disco del descuento** terminó calcado de una maqueta que Coni hizo en
Illustrator: «50%» en una línea y «OFF» debajo, centrado y fino. En **Raleway
Black** —la que el propio `CYBER_CAVA.ai` usa para sus porcentajes— y **Avenir
Next Ultra Light** para el OFF, que `marca.json` ya declara como apoyo.

⚠️ **De las nueve Raleway del editable sólo sirve la Black.** Las demás traen el
mapa de caracteres completo pero **los contornos vacíos**: se les pide la «F» y
devuelven un hueco. El primer render salió con «50%» y una sola «o» debajo.

**Dónde quedó:** las cuatro en `out/cava/prueba/` y subidas a `CAVA > DISEÑO ia >
PRUEBA`, con los mismos enlaces de siempre. Se rinden con
`scripts/cava-cyber-propuestas.py --todas` y
`scripts/cava-cyber-octubre-prueba.py`. Las 4 pasan las 11 reglas de
`qa/motor.py --marca cava`.

**Qué sigue:** entra el **precio real** y se elige propuesta. Nada más bloquea.

**Abierto:**
- ⛔ **EL PRECIO.** Las cuatro van con **$9.245 / $18.490, DE MUESTRA**. No está
  en ningún editable ni en los briefs de junio a septiembre. **Nada es
  publicable hasta que llegue.**
- ⛔ **La etiqueta de la botella de A, B y C la redibujó Magnific.** Hay que
  reponerla con el packshot antes de publicar.
- Faltan las **fechas del Cyber de octubre**.
- Los **5 PDFs del kit digital** que subió Coni (7Colores, Morandé, Adventure,
  Vistamar, Mancura) están **sin usar**: pueden traer el packshot en mejor
  resolución.
- La **revisión automática de comentarios** sigue sin montar. El agente en la
  nube NO sirve: el conector de Drive sólo lee comentarios en Docs y Sheets, y
  los de Coni están en PNG.

## 2026-09-23 — Coni (con Claude) · CYBER DE OCTUBRE: tres propuestas en prueba

**Qué se hizo:** Se abrió el Cyber de octubre para el **7Colores Limited Edition
Carmenere al 50 %**, formato mail/historia 2250×4000. Partió como una pieza suelta
y terminó en **tres propuestas**, una por cada referencia que dejó Coni en
`CAVA > DISEÑO ia > REFERENCIAS CYBER` (bajadas a `raw/cava/ref-cyber-oct2026/`):

- **A «rayo»** — mesa de piedra, haz de luz duro, fondo azul noche.
- **B «mano»** — botella sobre una palma, fondo naranja de marca.
- **C «descorche»** — dos manos abriendo, sobre tabla de charcutería.

El acompañamiento sale del Carmenere: queso, jamón curado, nueces, almendras, higos.

**El cambio de método que ordenó todo.** Las primeras versiones montaban el
packshot sobre un fondo generado y Coni dijo que **se notaba el montaje**. Ahora la
escena se genera CON la botella, pasándole el packshot oficial a Magnific como
referencia: la sombra, el reflejo y la luz son los de la foto.

**Dónde quedó:** las tres en `out/cava/prueba/` y subidas a
`CAVA > DISEÑO ia > PRUEBA`. Se rinden con
`scripts/cava-cyber-propuestas.py --todas`. Escenas en
`public/assets/cava/kv/cyber-oct2026-esc-*.png`. Las 3 pasan `qa/motor.py --marca cava`.

**Tres cosas que se resolvieron y conviene no volver a pelear:**

1. ⭐ **Bebas Neue Pro no está en ninguna máquina del estudio.** Es de Adobe Fonts,
   `empaquetable: false`, y el Mac sólo tiene «Bebas Kai», que es otra fuente. Se
   reconstruye desde los subconjuntos CFF incrustados en el propio `.ai` con
   `scripts/cava-fuentes-desde-editable.py`. Verificado: altura de mayúscula 167 px
   contra 165 px reales. **Hay que fundir DOS editables**: el de septiembre no trae
   la «L» mayúscula y el del Cyber no trae la «r» minúscula.
2. ⭐ **El logo tiene DOS tintas.** Se estaba extrayendo del PNG con máscara de
   luminancia y salía todo blanco: se perdían el racimo de la V y la tilde de
   MORANDÉ. Ahora sale del vector del `.ai` con
   `scripts/cava-logo-desde-editable.py`. **`marca.json` decía #DD660E y el vector
   dice #E1670E** — corregido, comprobado contra dos piezas publicadas.
3. **El apoyo de la botella no era falta de sombra, era falta de oclusión de
   contacto.** La botella tapa la luz rasante, así que la piedra se apaga alrededor
   de su base. Sin eso quedaba un halo claro y se leía flotando.

**Qué sigue:** entra el **precio real del 7Colores Limited Edition Carmenere**, que
es lo único que falta para que esto sea publicable, y se eligen una o dos
propuestas. El script ya tiene `--precio` y `--precio-antes`.

**Abierto:**
- ⛔ **EL PRECIO.** Las tres van con **$9.245 / $18.490, que son DE MUESTRA**. No
  está en los editables de 2026 ni en los briefs de CAVA de junio a septiembre. Hay
  que pedírselo a la ejecutiva. **Ninguna de las tres es publicable hasta entonces.**
- ⛔ **La etiqueta de la botella la redibujó Magnific** al integrarla, y
  `marca.json` lo prohíbe. Son propuestas de dirección, no piezas finales: antes de
  salir hay que reponer la etiqueta con el packshot. Se intentaron las dos vías
  automáticas —`scripts/cava-encaja-packshot.py` y `cava-etiqueta-oficial.py`— y
  ninguna dio un resultado limpio; las dos quedan en el repo con su diagnóstico.
  En Illustrator es directo: pegar el packshot con máscara.
- Faltan las **fechas del Cyber de octubre**. En la pieza de junio iban en dorado
  bajo el titular.
- Quedó sin montar la **revisión automática de comentarios**. El agente en la nube
  NO sirve para esto: el conector de Drive sólo lee comentarios en Docs y Sheets, y
  los de Coni están en PNG. Lo único que los lee es
  `scripts/drive-comentarios.py`, que necesita el token local — y funciona **sólo
  con archivos que subió este mismo token**.

## 2026-09-09 — Valeria Traverso (con Claude)

**Qué se hizo:** No se produjo nada. En el arranque del estudio el verificador detectó que las
**3 referencias del brief de agosto** en `raw/cava/ref/` (`CAVA_AGO_BRIEF1.png`,
`CAVA_AGO_BRIEF2-02.png`, `CAVA_AGO_BRIEF2-03_liviana.png`) no son imágenes: son la página de
login de Google guardada con extensión `.png`.

**Dónde quedó:** Sin reparar. Los archivos **existen en el Drive** —los subió Constanza Lizana el
14-08-2026— pero **no están compartidos por enlace**: la descarga directa devuelve la pantalla de
inicio de sesión.

**Qué sigue:** Pedirle a Coni que comparta esa carpeta por enlace, o abrirlos con la cuenta y
bajarlos a mano. Después correr `verificar-material.py raw/cava` para confirmar.

**Abierto:** **No se puede diseñar CAVA con el brief de agosto hasta reponer esas 3 referencias.**
Aparte, sigue pendiente de antes la tipografía: **Bebas Neue Pro** y **Brandon Grotesque** hay que
activarlas en Creative Cloud → Fuentes.

