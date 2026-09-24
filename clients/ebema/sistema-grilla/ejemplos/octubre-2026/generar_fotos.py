#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBEMA GRILLA · las fotos del lote de octubre 2026 — Magnific / Nano Banana Pro.

⛔ LAS CINCO REGLAS DE IMAGEN DE PAULINA (§5 del manual) están aplicadas acá:

1. MINIMALISTA — la imagen nunca destaca más que el texto. Plano limpio, un solo
   sujeto, fondo tranquilo. Nada de paneles de herramientas ni estantes cargados.
2. El velo lo pone el CSS, no el prompt. Acá sólo se pide la ZONA TRANQUILA donde
   cae el bloque de texto: arriba en las láminas de desarrollo, abajo en la portada.
3. El producto de proveedor SE GENERA, fiel al real. Nunca el packshot de marca:
   ni etiquetas, ni logos, ni texto legible dentro de la imagen.
4. EL TIPO DE IMAGEN LO DICTA EL TEXTO DE LA LÁMINA:
      especificación técnica  → ZOOM de producto, acabado de catálogo
      aplicación o uso        → ESCENA de un profesional usando el producto
5. LA ESCALA SE RESPETA — las proporciones reales entran al prompt.

⭐ Y LA ESCENA SE GENERA CON EL ZOOM DEL PRODUCTO COMO REFERENCIA. Por eso cada
carrusel genera PRIMERO su lámina de producto y después las escenas con `--refs`:
sin ese paso cada lámina inventa su propio producto y el carrusel deja de ser del
mismo. Nano Banana Pro admite hasta 14 referencias.

Uso:  python generar_fotos.py [--solo masisa] [--listar]
"""
import argparse, os, subprocess, sys

# En Windows la consola sale en cp1252 y cualquier acento o simbolo revienta
# el print con UnicodeEncodeError. Los archivos ya se escriben en utf-8.
for _f in (sys.stdout, sys.stderr):
    if hasattr(_f, "reconfigure"):
        _f.reconfigure(encoding="utf-8", errors="replace")

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", "..", ".."))
MAGNIFIC = os.path.join(RAIZ, "scripts", "magnific.py")

# Lo que toda lámina cumple, se escriba lo que se escriba en su prompt propio.
COMUN = ("Fotografía publicitaria profesional de materiales de construcción, "
         "composición minimalista y limpia, un solo sujeto claro, fondo tranquilo "
         "y desenfocado, luz natural difusa, color realista y neutro. "
         "SIN texto, SIN letreros, SIN logos, SIN marcas, SIN etiquetas legibles, "
         "SIN marcas de agua, SIN franjas ni bordes vacíos: la foto cubre todo el cuadro. "
         "UNA SOLA fotografía continua, tomada de una vez con una sola cámara: SIN collage, "
         "SIN paneles, SIN dípticos ni trípticos, SIN cortes ni costuras horizontales.")

# ⛔ RONDA 2 · 24-09-2026 — Paulina, sobre pointfix3: «hiciste un montaje de la imagen
# sobre otra imagen. La imagen de fondo debe ser sólo una.» No fue un montaje nuestro:
# Nano Banana Pro devolvió un COLLAGE de tres franjas horizontales (pointfix3 y
# sanjuan2, costuras a ~25 % y ~75 % del alto). Pasa cuando el prompt describe dos
# planos distintos — un detalle y un paisaje — y el modelo los resuelve en paneles.
# La frase «una sola fotografía continua» va ahora en TODO prompt.

# Para las escenas donde el saco REAL entra como referencia: COMUN prohíbe logos y
# etiquetas, y eso le pide al modelo que borre la gráfica del saco.
FONDO_SIN_TEXTO = ("Fotografía publicitaria profesional, color realista, luz natural "
                   "difusa. La gráfica de los sacos es la de la referencia, sin "
                   "inventar otra. SIN carteles, SIN letreros ni texto agregado, SIN "
                   "marcas de agua. UNA SOLA fotografía continua: SIN collage, SIN "
                   "paneles, SIN cortes ni costuras.")

# ⛔ NUNCA NOMBRAR EL TITULAR NI EL TEXTO EN EL PROMPT — aprendido el 23-09-2026.
# La primera versión decía «el tercio superior queda tranquilo: AHÍ VA EL TITULAR» y
# Nano Banana Pro lo entendió al pie de la letra: devolvió las imágenes con una
# FRANJA BLANCA LISA ocupando el 17 % de arriba, reservando el hueco para el texto.
# La zona tranquila se pide en términos FOTOGRÁFICOS — fondo desenfocado, cielo,
# muro liso — y se prohibe explícitamente cualquier franja o borde vacío.
LLENA = ("La fotografía llena TODO el encuadre de borde a borde, sin franjas lisas, "
         "sin bandas de color plano, sin bordes ni marcos y sin zonas vacías.")

# ⛔ CORREGIDO EL 23-09-2026 — Paulina, sobre cbb2: «este cuadro no debe ir; en esta
# parte debe ir un velo difuminado detrás del texto, mas no un bloque sólido».
# La versión anterior pedía que arriba «sólo hubiera fondo de tono parejo» y eso
# devolvía un VACÍO: con el velo encima se leía como un rectángulo gris con borde
# duro justo donde empieza el sujeto (medido: luminancia 55-60 hasta el 18 % y
# salto a 115-128 de golpe). La zona tranquila tiene que seguir siendo FOTO — con
# textura, profundidad y gradación—, sólo que sin nada que compita.
ZONA_ARRIBA = ("Encuadre con aire arriba: el tercio superior muestra el CONTEXTO REAL "
               "de la escena con profundidad y textura — la continuación del muro, el "
               "cielo, el fondo del taller o del terreno —, suavemente desenfocado y "
               "sin nada que compita con el sujeto. Nunca un fondo liso, ni un color "
               "plano, ni una superficie uniforme sin detalle. " + LLENA)
# ⛔ RONDA 2 · 24-09-2026 — Paulina, sobre cbb1: «en esta zona se ve raro, no tiene
# textura, sólo se ve como una mancha oscura». Es el mismo error que ZONA_ARRIBA en la
# ronda 1, ahora abajo: «superficie de tono parejo» devolvió tierra negra LISA, y con
# el velo de portada encima quedó un parche plano. La zona tranquila es FOTO con
# textura, nunca un tono parejo.
ZONA_ABAJO  = ("Encuadre con aire abajo: la mitad inferior es el mismo terreno de la "
               "escena en primer plano — tierra con terrones y surcos, pasto, piso — con "
               "su TEXTURA NATURAL bien visible y buena luz, sin objetos que llamen la "
               "atención. Nunca una superficie lisa, oscura o de un solo tono. " + LLENA)

# ⭐ LA LÁMINA FINAL — RONDA 2 · 24-09-2026. Deroga la de la ronda 1.
# Paulina: «el saco de cemento debe ir incluido en la escena del fondo, como que los
# sacos están disponibles en la bodega. Nunca poner el png del producto así: hace que
# el logo se pierda. Esto debe ser así para TODAS las slides finales de carrusel de
# productos.» La ronda 1 ponía el producto AL CENTRO, justo debajo del anillo EBEMA,
# y le competía al logo. Ahora el producto es STOCK: pallets y racks a los costados y
# al fondo, y el centro del encuadre —donde van el anillo y el botón— es pasillo
# despejado. El packshot ya no se pega encima (`cierre_compuesto.py` queda retirado):
# entra como REFERENCIA de la escena, y el desenfoque del conjunto hace el resto.
def stock(producto):
    return ("Interior de la bodega de una distribuidora de materiales de construcción, "
            "amplia, luminosa y ordenada, vista de frente desde el pasillo central. A "
            "AMBOS COSTADOS y al fondo, racks metálicos y pallets cargados de " + producto +
            ", apilados como existencias: muchas unidades iguales, ordenadas, que llenan "
            "los costados del encuadre y se pierden en profundidad. El CENTRO del encuadre "
            "es el pasillo despejado, con piso de hormigón pulido, sin nada apilado ni "
            "ningún objeto al medio. Profundidad de campo baja: todo suavemente "
            "DESENFOCADO, con poco contraste, sin que nada se vea nítido. ")

# ---------------------------------------------------------------------------
# Cada entrada: (archivo, tipo, prompt, [refs])
#   tipo: "producto" = zoom de catálogo · "escena" = profesional usando el producto
#         "ambiente" = situación sin producto protagonista · "cierre" = fondo borroso
# El orden importa: la lámina de producto va PRIMERO y las demás la referencian.
# ---------------------------------------------------------------------------
LOTE = {
 # ---------------------------------------------------------------- MASISA ---
 # ⭐ MEDIDAS REALES, dadas por Paulina el 23-09-2026:
 #     formato estándar 122 × 244 cm (1220 × 2440 mm) · espesor 8 mm
 # Regla 5 de §5: las medidas entran al prompt en milímetros Y traducidas a la
 # escena, con la RAZÓN de las proporciones difíciles — «unas 150 veces más ancha
 # que gruesa» funciona mejor que repetir «8 mm», que el modelo ignora.
 # 2,44 m es más alto que una persona; 8 mm es un canto finísimo, jamás un bloque.
 "masisa": [
  ("02", "producto",
   "Primer plano de catálogo de un tablero estructural de madera reconstituida "
   "apoyado en un banco de mueblería, con una huincha de medir metálica y un lápiz "
   "de carpintero sobre la superficie. Se ve con nitidez la cara lisa y mate del "
   "tablero y, sobre todo, EL CANTO: una franja de virutas de madera comprimidas, "
   "veteado pálido, de aspecto granulado. La placa mide 1220 × 2440 mm y sólo "
   "8 mm de espesor: el canto es una lámina FINÍSIMA, unas 150 veces más angosta "
   "que el ancho de la placa — casi una lámina de cartón, jamás un bloque. "
   "Fondo de taller desenfocado, luz de estudio suave y direccional, sombra corta. "
   + ZONA_ARRIBA + " " + COMUN, []),
  ("01", "escena",
   "Un maestro mueblista chileno, de unos 40 años, con camisa de trabajo arremangada, "
   "tomando medidas con una huincha metálica DENTRO del nicho vacío de un muro donde "
   "se va a instalar un clóset empotrado. Se entiende con claridad que es un espacio "
   "empotrado de muro a muro y que el mueble se está fabricando a medida: se ven las "
   "jambas del nicho y un tablero apoyado de canto a un costado. Ese tablero mide "
   "1220 × 2440 mm: sus 2,44 m lo hacen claramente MÁS ALTO QUE EL HOMBRE, y su "
   "canto de 8 mm se ve finísimo de perfil, casi una lámina. "
   "Dormitorio en obra, limpio y luminoso, muros lisos sin pintar, piso protegido. "
   "Plano medio, el hombre a un costado. " + ZONA_ABAJO + " " + COMUN, ["02"]),
  ("03", "escena",
   "Interior de un clóset empotrado a medio armar, visto de frente: repisas "
   "horizontales y divisiones verticales de tablero estructural ya montadas, con los "
   "puntos de apoyo y los cantos a la vista. Las piezas son de 8 mm de espesor: sus "
   "cantos se leen FINOS y ligeros de perfil, nunca gruesos como un tablón. "
   "Un mueblista al costado, de espaldas "
   "parciales, ajustando una repisa. Dormitorio limpio y luminoso, luz natural lateral. "
   + ZONA_ARRIBA + " " + COMUN, ["02"]),
  # RONDA 1 — lineamiento de Paulina para TODA lámina final: «bodega de materiales
  # en el fondo y el producto en el centro, siempre la imagen total con desenfoque
  # para que el texto destaque». Acá el producto SÍ se genera: un tablero no es un
  # packshot de marca, no tiene etiqueta que falsificar (§5).
  ("04", "cierre",
   stock("tableros estructurales de madera reconstituida de 1220 × 2440 mm y 8 mm de "
         "espesor, en rumas horizontales con los cantos de viruta a la vista") + COMUN, ["02"]),
 ],

 # --------------------------------------------------------------- ETERSOL ---
 "etersol": [
  ("02", "producto",
   "Macro de catálogo de la textura de un pasto sintético de jardín de alta gama, "
   "visto muy de cerca y en ángulo: fibras verticales de dos verdes distintos, uno "
   "más claro y otro más oscuro, con hebras beige cortas en la base que imitan la "
   "paja seca del pasto natural. Se ve la densidad del pelo y que las fibras son "
   "flexibles. Luz natural difusa, sin brillos plásticos. " + ZONA_ARRIBA + " " + COMUN, []),
  ("01", "ambiente",
   # RONDA 1: «cambiar imagen por un ambiente estético; sólo el pasto debe verse
   # desgastado, con huecos con tierra sin pasto. Eliminar los ladrillos o algún
   # otro material.» Lo feo es el pasto, no el patio.
   "Patio trasero de una casa bonita y bien cuidada, a comienzos de primavera: "
   "terraza limpia, arbustos y un muro de cierre prolijo al fondo. Lo ÚNICO "
   "descuidado es el pasto, que está gastado y con huecos de tierra pelada a la "
   "vista. NO hay ladrillos, sacos, escombros ni material de construcción en "
   "ninguna parte. Día luminoso y suave, sin personas. Plano general ordenado. " + ZONA_ABAJO + " " + COMUN, []),
  ("03", "escena",
   "Instalador desenrollando un rollo de pasto sintético sobre una base de tierra "
   "compactada y nivelada en un patio. Se ve el rollo a medio extender, el borde de "
   "la lámina y el respaldo por el reverso. El hombre está agachado, de perfil, con "
   "guantes de trabajo. Patio despejado, día luminoso. " + ZONA_ARRIBA + " " + COMUN, ["02"]),
  ("04", "ambiente",
   # RONDA 1: «la imagen se ve muy falsa; el fondo plano hace que se vea incómodo.
   # Por favor aplicar en contexto de la vida real.»
   "Fotografía real de un patio de casa con pasto sintético verde parejo, vivido y "
   "en uso: terraza de madera con muebles de exterior, macetas con plantas, un "
   "juguete en el pasto, la fachada de la casa con sus ventanas a un costado y "
   "árboles del vecindario asomándose por sobre el cierre. Luz natural de tarde con "
   "sombras largas y reales. Sin personas. Plano general amplio y con profundidad. " + ZONA_ARRIBA + " " + COMUN, ["02"]),
  # RONDA 1 — lineamiento de lámina final (ver masisa 04).
  ("05", "cierre",
   stock("rollos de pasto sintético verde, acostados y apilados, con el canto "
         "enrollado a la vista") + COMUN, ["02"]),
 ],

 # ------------------------------------------------------------------- CBB ---
 "cbb": [
  # RONDA 1 — igual que San Juan: se genera SÓLO la bodega y el saco real se compone
  # encima con `cierre_compuesto.py`. El packshot de marca no lo toca la IA (§5).
  ("05", "cierre",
   stock("sacos de cemento de papel KRAFT con los costados verdes, IDÉNTICOS al de la imagen de referencia, apilados en pallets") + FONDO_SIN_TEXTO,
   ["packshots/cbb_saco.png"]),
  ("01", "ambiente",
   # RONDA 2: «en esta zona se ve raro, no tiene textura, sólo se ve como una mancha
   # oscura» — la tierra salió negra y lisa. Ahora es tierra de cultivo café con
   # surcos y terrones iluminados por el sol bajo, que se lee como terreno.
   "Fundación de hormigón recién hormigonada en un terreno agrícola chileno: zanjas "
   "corridas y sobrecimiento a la vista, con un cerco de campo y un potrero verde al "
   "fondo. En primer plano, tierra de cultivo CAFÉ recién trabajada, con surcos, "
   "terrones y algo de pasto, iluminada por el sol bajo de la tarde que marca su "
   "relieve. Día despejado, sin personas. Plano general tranquilo, cámara a la altura "
   "de una persona. " + ZONA_ABAJO + " " + COMUN, []),
  ("02", "producto",
   # RONDA 1: «la imagen está bien pero el plano debe ser más amplio; mucho zoom no
   # se ve estético.» Se abre a un plano de situación, sin perder el daño.
   "Plano ABIERTO de una fundación de hormigón deteriorada por ataque químico en un "
   "terreno agrícola: se ve el tramo de sobrecimiento completo y, sobre él, la pasta "
   "de cemento disgregada, los áridos expuestos, microfisuras y eflorescencias "
   "blanquecinas. Al fondo, el campo y el cielo dando profundidad. Luz rasante de "
   "la mañana que marca el relieve del daño. Sin macro ni acercamiento extremo. " + ZONA_ARRIBA + " " + COMUN, []),
  # RONDA 1 — «el saco debe ser el saco original de CBB». Paulina confirmó que el
  # envase que EBEMA distribuye es el INACESA kraft, no el verde del sitio de cbb.cl.
  # El packshot oficial entra como REFERENCIA para que el modelo reproduzca ese saco.
  # ⚠️ La etiqueta se revisa con zoom 3×: si sale deformada, se compone como el cierre.
  ("03", "escena",
   # RONDA 2: «este saco debe ser el que te dejé en drive, este no es el correcto».
   # El de la ronda 1 era el INACESA; el que EBEMA vende es el CBB Especial de
   # 25 kg: kraft con los costados verdes, «es Cbb Cementos» y la gran curva verde y
   # azul marino en la cara. Referencia: el packshot del producto en Sodimac
   # (3316939), que mandó Paulina «para que no cometas el error nuevamente».
   "Maestro hormigonero chileno vaciando cemento gris desde un saco de cemento "
   "IDÉNTICO al de la imagen de referencia — papel kraft con los costados y la parte "
   "de arriba VERDES, y en la cara una gran curva verde y otra azul marino — dentro "
   "de una carretilla con árido, junto a una fundación en construcción en un terreno "
   "de campo. El saco se ve de frente, completo, con su gráfica nítida, sin deformar "
   "y sin inventar otra. El hombre de perfil, con guantes y camisa de trabajo. "
   "Escena limpia, luz natural. " + ZONA_ARRIBA + " " + FONDO_SIN_TEXTO,
   ["packshots/cbb_saco.png"]),
  # RONDA 1 — la primera versión salió 90 % losa gris plana y la lámina quedaba vacía.
  # Se abre el encuadre: la losa ocupa el primer plano en diagonal y detrás entra el
  # campo, que es lo que da profundidad y contexto.
  ("04", "ambiente",
   "Radier y fundación de hormigón ya terminados y curados en una parcela agrícola "
   "chilena, vistos en DIAGONAL desde una esquina: la losa gris pareja y bien "
   "platachada ocupa el primer plano y detrás se ve el campo abierto — pasto, unos "
   "árboles y el cerco de la parcela— con el cielo de la tarde. Ordenado, sin "
   "personas, luz natural cálida y rasante. " + ZONA_ARRIBA + " " + COMUN, []),
 ],

 # ------------------------------------------------------------- VOLCANITA ---
 # La cara VERDE es lo que hace reconocible a una placa de yeso-cartón resistente a
 # la humedad. Sin ese verde es una placa cualquiera, así que va en todos los prompts.
 "volcanita": [
  # RONDA 1 — lineamiento de lámina final (ver masisa 04).
  ("05", "cierre",
   stock("planchas de yeso-cartón de CARA VERDE clara, en rumas horizontales, lisas, "
         "sin impresión ni logotipo") + COMUN, ["03"]),
  ("01", "ambiente",
   "Baño residencial en plena remodelación, desnudo: la estructura metálica de "
   "tabiquería a la vista, el muro abierto, la cerámica vieja retirada y el piso "
   "protegido. Limpio y ordenado, sin escombros, luz natural entrando por una ventana. "
   "Sin personas. Plano general. " + ZONA_ABAJO + " " + COMUN, []),
  ("02", "producto",
   "Macro de catálogo del borde de una placa de yeso-cartón COMÚN, de cara gris "
   "blanquecina, dañada por humedad: el papel hinchado y despegado por el canto, el "
   "núcleo de yeso reblandecido y desmoronándose, manchas de humedad. Textura muy "
   "nítida, luz rasante. " + ZONA_ARRIBA + " " + COMUN, []),
  ("03", "escena",
   "Instalador atornillando una plancha de yeso-cartón de CARA VERDE a una estructura "
   "metálica de tabiquería en un baño en obra. Sostiene la plancha con una mano y el "
   "atornillador eléctrico con la otra. De perfil, camisa de trabajo. Obra limpia y "
   "luminosa. " + ZONA_ARRIBA + " " + COMUN, ["05"]),
  ("04", "producto",
   "Primer plano de la junta entre dos planchas de yeso-cartón de CARA VERDE ya "
   "atornilladas: se ven las cabezas de los tornillos alineadas y hundidas a ras, la "
   "cinta de papel aplicada sobre la junta y la pasta de empaste extendida con "
   "espátula. Luz lateral suave que marca el relieve. " + ZONA_ARRIBA + " " + COMUN, ["05"]),
 ],

 # -------------------------------------------------------------- SAN JUAN ---
 "sanjuan": [
  # RONDA 1 — nuevo lineamiento de Paulina para TODA lámina final: «bodega de
  # materiales en el fondo y el producto original en el centro, siempre la imagen
  # total con desenfoque para que el texto destaque». Acá se genera SÓLO la bodega:
  # el saco real se compone encima con `cierre_compuesto.py`, porque el packshot de
  # marca no lo toca la IA (§5). Por eso el centro va deliberadamente despejado.
  ("05", "cierre",
   stock("sacos de cemento AMARILLOS Y NEGROS, IDÉNTICOS al de la imagen de referencia, apilados en pallets") + FONDO_SIN_TEXTO,
   ["packshots/sanjuan_saco.png"]),
  ("01", "ambiente",
   # RONDA 2: «no me gusta la imagen de fondo. Hazla más comercial, sin productos,
   # pero que sea más llamativa». La de ronda 1 era un llano pardo y plano. Ahora es
   # foto publicitaria: hora dorada, campo productivo verde, cielo con volumen.
   "Fotografía publicitaria de campo chileno a la hora dorada: un estanque circular "
   "de acumulación de agua de hormigón, nuevo y bien terminado, en medio de un predio "
   "agrícola productivo — hileras de cultivo verdes y ordenadas, cerros azulados al "
   "fondo y un cielo amplio con nubes iluminadas por el sol bajo. Luz cálida y "
   "rasante, colores ricos y saturados sin exagerar, sensación de prosperidad. "
   "El estanque en el tercio superior del encuadre, sin personas ni productos. "
   + ZONA_ABAJO + " " + COMUN, []),
  ("02", "producto",
   # RONDA 1: «arreglar imagen para que no se vea como un cuadro en la zona de
   # arriba, mismo comentario del carrusel de CBB.»
   # RONDA 2: «la imagen no se entiende, genérala nuevamente con un contexto
   # realista» — salió un collage (muro arriba, galpón al medio, muro abajo). Ahora
   # se ve de una: un estanque viejo CON agua, en su predio, y el daño en su muro.
   "Un estanque circular de hormigón antiguo en un predio rural chileno, visto en "
   "tres cuartos desde afuera y a poca distancia, lleno de agua hasta cerca del "
   "borde. Su muro está deteriorado por el contacto permanente con el agua: manchas "
   "de humedad oscuras bajo la línea del agua, eflorescencias blancas de sales, una "
   "fisura vertical y el hormigón descascarado con el árido a la vista. Detrás, el "
   "campo y unos árboles, fuera de foco. Luz natural de la mañana. Se entiende de "
   "inmediato que es un estanque de agua y que su muro se está degradando. "
   + ZONA_ARRIBA + " " + COMUN, []),
  # RONDA 1 — «debe ser el saco original de cemento San Juan». El packshot oficial
  # entra como REFERENCIA para que el modelo reproduzca ese saco y no invente otro.
  # ⚠️ La etiqueta se revisa con zoom 3× en el render: si sale deformada, la lámina
  # se resuelve componiendo el packshot, como el cierre.
  ("03", "escena",
   "Maestro hormigonero chileno junto a una betonera, al lado de un pozo en "
   "construcción en el campo, vaciando el contenido de un SACO DE CEMENTO AMARILLO Y "
   "NEGRO idéntico al de la imagen de referencia: cuerpo amarillo con un gran logotipo "
   "oscuro y franja negra en la base. El saco se ve completo y de frente, con su "
   "gráfica nítida y sin deformar. El hombre de perfil, con guantes y camisa de "
   "trabajo. Escena limpia, luz natural. "
   + ZONA_ARRIBA + " " + COMUN, ["packshots/sanjuan_saco.png"]),
  ("04", "ambiente",
   "Estanque de agua de hormigón terminado en un predio rural, con el muro gris parejo "
   "y bien terminado y el agua adentro reflejando el cielo. Ordenado, sin personas, luz "
   "de la tarde. " + ZONA_ARRIBA + " " + COMUN, []),
 ],

 # -------------------------------------------------------------- POINTFIX ---
 # Las 4 PUNTAS son el dato del brief y lo que hace reconocible al producto: van
 # descritas en todos los prompts donde el alambre se ve de cerca.
 "pointfix": [
  ("03", "producto",
   # RONDA 1: «muy bien; el fondo cambiarlo por un campo abierto rural estético
   # desenfocado.» · RONDA 2: «hiciste un montaje de la imagen sobre otra imagen, la
   # imagen de fondo debe ser sólo una» — salió un collage de 3 franjas. Se describe
   # como UNA toma de teleobjetivo: el alambre nítido y el campo como bokeh detrás.
   "Una sola fotografía tomada con teleobjetivo y diafragma abierto: en primer plano, "
   "nítido, un tramo de alambre de púas galvanizado tensado en horizontal, dos hebras "
   "torcidas entre sí con una púa de CUATRO PUNTAS afiladas abiertas en cruz, metal "
   "gris mate sin óxido. Detrás, fuera de foco en la MISMA toma, un campo abierto "
   "chileno: potrero verde, árboles lejanos y el cielo de la tarde, que se funden "
   "en un desenfoque continuo de arriba abajo. Luz natural lateral que marca el "
   "brillo del alambre. " + ZONA_ARRIBA + " " + COMUN, []),
  ("01", "ambiente",
   "Perímetro de una parcela agrícola chilena SIN CERCAR: el límite del terreno abierto, "
   "pastizal seco, unos árboles al fondo y cerros a lo lejos. Ningún poste ni alambre. "
   "Día despejado, luz de la tarde, sin personas. Plano general tranquilo y amplio. "
   + ZONA_ABAJO + " " + COMUN, []),
  ("02", "escena",
   "Un hombre de campo chileno instalando postes de madera para un cerco en el límite "
   "de un potrero: sostiene un poste recién hincado y a su lado se ve la línea de "
   "postes ya puestos, alineados hacia el horizonte. Camisa de trabajo y guantes, de "
   "perfil. Campo abierto, luz natural. " + ZONA_ARRIBA + " " + COMUN, ["03"]),
  ("04", "ambiente",
   "Cerco de campo terminado: postes de madera alineados y varias corridas de alambre "
   "de púas de cuatro puntas tensadas parejo, recorriendo el límite de un potrero verde "
   "hacia el horizonte. Sin personas, día despejado. " + ZONA_ARRIBA + " " + COMUN, ["03"]),
  # RONDA 1 — lineamiento de lámina final (ver masisa 04).
  ("05", "cierre",
   stock("rollos de alambre de púas galvanizado, apilados en pallets, con las espiras "
         "metálicas a la vista") + COMUN, ["03"]),
 ],
}


# ⛔ EL BUILD CONSUME .jpg, NO .png. Magnific devuelve un PNG de 4K y ~18 MB; el
# render sale a 2250 de ancho, así que se guarda como JPEG de 2400 y calidad 92
# (sin submuestreo de croma) y ESE es el archivo que se versiona en
# public/assets/ebema/grilla-oct26/ y el que leen los carruseles. Es la regla de
# «el render vuelve al repo el mismo día»: sin el fondo versionado la pieza no se
# puede volver a sacar igual, porque una imagen de IA no se regenera dos veces igual.
def ruta(slug, nombre):
    # Una referencia con "/" es una ruta del lote — se usa para meter el PACKSHOT
    # OFICIAL del proveedor como referencia de la escena, que es lo que pidió
    # Paulina para sanjuan3: «debe ser el saco original de cemento San Juan».
    if "/" in nombre:
        return os.path.join(AQUI, nombre)
    return os.path.join(AQUI, "fotos", slug, nombre + ".jpg")


def generar(slug, nombre, prompt, refs, rehacer=False):
    destino = ruta(slug, nombre)
    if os.path.exists(destino) and not rehacer:
        print(f"    · {slug}/{nombre}.png ya está, se salta")
        return True
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    cmd = [sys.executable, MAGNIFIC, "pro", prompt,
           # 4:5 = 1080x1350, el lienzo del carrusel. Con "feed" (1:1) el montaje
           # recorta un 20 % del ancho y se come a quien vaya a un costado.
           "--aspecto", "carrusel", "--resolucion", "4K", "--out", destino]
    faltan = [r for r in refs if not os.path.exists(ruta(slug, r))]
    if faltan:
        print(f"    ✗ {slug}/{nombre}: falta la referencia {faltan} — se genera primero")
        return False
    if refs:
        cmd += ["--refs"] + [ruta(slug, r) for r in refs]
    print(f"    → {slug}/{nombre}.png" + (f"  (ref: {', '.join(refs)})" if refs else ""))
    crudo = destino[:-4] + "__4k.png"
    cmd[cmd.index("--out") + 1] = crudo
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode == 0 and os.path.exists(crudo):
        from PIL import Image
        im = Image.open(crudo).convert("RGB")
        if im.size[0] > 2400:
            im = im.resize((2400, round(2400 * im.size[1] / im.size[0])), Image.LANCZOS)
        im.save(destino, quality=92, subsampling=0, optimize=True)
        os.remove(crudo)
    if r.returncode != 0 or not os.path.exists(destino):
        print(f"    ✗ FALLÓ {slug}/{nombre}")
        print("      " + (r.stdout or "").strip()[-600:])
        print("      " + (r.stderr or "").strip()[-600:])
        return False
    return True


def escribir_prompts_md():
    p = os.path.join(AQUI, "..", "PROMPTS.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write("# Los prompts de las fotos — EBEMA grilla octubre 2026\n\n")
        f.write("> Regla 5 de §5 del manual: **el prompt queda escrito junto a la "
                "pieza.** Si no está escrito, la imagen no se puede rehacer.\n\n")
        f.write("Todos con **Nano Banana Pro** (`text-to-image/nano-banana-pro`), "
                "aspecto `carrusel` (4:5), resolución 4K.\n\n")
        f.write("La lámina marcada `producto` se genera PRIMERO y entra como "
                "`--refs` de las demás del mismo carrusel: es lo que hace que el "
                "producto no cambie entre láminas.\n\n")
        for slug, items in LOTE.items():
            f.write(f"\n## {slug}\n\n")
            for nombre, tipo, prompt, refs in items:
                f.write(f"### `fotos/{slug}/{nombre}.png` — {tipo}\n")
                if refs:
                    f.write(f"Referencias: {', '.join(refs + ['.png'])[:-5]}\n\n")
                f.write(f"```\n{prompt}\n```\n\n")
    print(f"\n✓ prompts escritos en {os.path.normpath(p)}")


# RONDA 2 · 24-09-2026 — las 11 fotos que se rehacen por los comentarios de Paulina.
# Las anteriores se respaldan en fotos/<tema>/_r1/ antes de pisarlas.
RONDA2 = [("cbb", "01"), ("cbb", "03"), ("cbb", "05"), ("pointfix", "03"),
          ("pointfix", "05"), ("sanjuan", "01"), ("sanjuan", "02"), ("sanjuan", "05"),
          ("masisa", "04"), ("etersol", "05"), ("volcanita", "05")]


# El modelo no desenfoca lo que se le pide: la bodega de stock sale NÍTIDA aunque el
# prompt diga «todo desenfocado». El desenfoque del cierre se hace acá, con una
# cifra fija, y la toma nítida queda al lado (`05_nitida.jpg`) para poder rehacerlo.
DESENFOQUE_CIERRE = 9.0      # radio gaussiano sobre la foto de 2400 px de ancho


def suavizar_cierre(destino):
    import shutil
    from PIL import Image, ImageFilter
    nitida = destino[:-4] + "_nitida.jpg"
    shutil.copy2(destino, nitida)
    im = Image.open(nitida).convert("RGB").filter(ImageFilter.GaussianBlur(DESENFOQUE_CIERRE))
    im.save(destino, quality=92, subsampling=0, optimize=True)
    print(f"    ~ {os.path.relpath(destino, AQUI)} desenfocada (radio {DESENFOQUE_CIERRE})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ronda2", action="store_true", help="rehace sólo las fotos de RONDA2")
    ap.add_argument("--solo", help="un solo carrusel")
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--rehacer", action="store_true")
    a = ap.parse_args()

    escribir_prompts_md()
    if a.listar:
        for slug, items in LOTE.items():
            print(f"{slug}: " + ", ".join(f"{n}({t})" for n, t, _, _ in items))
        return

    if a.ronda2:
        import shutil
        ok = faltan = 0
        for slug, nombre in RONDA2:
            if a.solo and slug != a.solo:
                continue
            _, _t, prompt, refs = next(e for e in LOTE[slug] if e[0] == nombre)
            d = ruta(slug, nombre)
            if os.path.exists(d):
                os.makedirs(os.path.join(os.path.dirname(d), "_r1"), exist_ok=True)
                resp = os.path.join(os.path.dirname(d), "_r1", nombre + ".jpg")
                if not os.path.exists(resp):
                    shutil.copy2(d, resp)
                os.remove(d)
            if generar(slug, nombre, prompt, refs, True):
                if _t == "cierre":
                    suavizar_cierre(d)
                ok += 1
            else:
                faltan += 1
        print(f"\n{ok} listas · {faltan} fallaron")
        return

    slugs = [a.solo] if a.solo else list(LOTE)
    ok = faltan = 0
    for slug in slugs:
        print(f"\n── {slug} ──")
        for nombre, _tipo, prompt, refs in LOTE[slug]:
            if generar(slug, nombre, prompt, refs, a.rehacer):
                ok += 1
            else:
                faltan += 1
    print(f"\n{'='*50}\n{ok} listas · {faltan} fallaron")


if __name__ == "__main__":
    main()
