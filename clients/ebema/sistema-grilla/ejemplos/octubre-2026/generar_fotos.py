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
         "SIN marcas de agua, SIN franjas ni bordes vacíos: la foto cubre todo el cuadro.")

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
ZONA_ABAJO  = ("Encuadre con aire abajo: en la mitad inferior sólo hay superficie "
               "continua y de tono parejo — suelo, pasto, terreno o piso —, sin "
               "objetos que llamen la atención. " + LLENA)

# ⭐ LA LÁMINA FINAL, ronda 1 de octubre. Tres piezas de prompt que comparten las
# cinco: bodega desenfocada atrás, producto al centro, y el conjunto suave.
BODEGA = ("Interior de una bodega de materiales de construcción, luminosa y ordenada, "
          "con estanterías y pallets a ambos lados perdiéndose en profundidad, MUY "
          "DESENFOCADA. ")
CIERRE = "Al centro del encuadre, en primer plano y algo más nítido que el fondo: "
TODO   = ("La imagen entera va suave y con poco contraste, para que un texto puesto "
          "encima destaque. ")

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
   BODEGA + CIERRE +
   "dos tableros estructurales de madera reconstituida apoyados de canto, con la "
   "cara lisa y el canto de virutas comprimidas a la vista. " + TODO + COMUN, ["02"]),
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
   BODEGA + CIERRE +
   "un rollo de pasto sintético apoyado de pie, con el canto enrollado y el verde de "
   "las fibras a la vista. " + TODO + COMUN, ["02"]),
 ],

 # ------------------------------------------------------------------- CBB ---
 "cbb": [
  # RONDA 1 — igual que San Juan: se genera SÓLO la bodega y el saco real se compone
  # encima con `cierre_compuesto.py`. El packshot de marca no lo toca la IA (§5).
  ("05_bodega", "cierre",
   "Interior de una bodega de materiales de construcción, luminosa y ordenada: "
   "estanterías metálicas a ambos lados con pallets de sacos, tablas y perfiles "
   "apilados, y un pasillo central despejado que se pierde en profundidad. Vista "
   "frontal del pasillo. El CENTRO del encuadre queda libre, sin nada apilado. "
   "Imagen entera suavemente DESENFOCADA, como fondo. " + COMUN, []),
  ("01", "ambiente",
   "Fundación de hormigón recién hormigonada en un terreno agrícola chileno: zanjas "
   "corridas y sobrecimiento a la vista sobre tierra de cultivo oscura, con un cerco "
   "de campo y un potrero verde al fondo. Día despejado, luz de la tarde, sin personas. "
   "Plano general tranquilo. " + ZONA_ABAJO + " " + COMUN, []),
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
   "Maestro hormigonero chileno vaciando cemento gris desde un SACO DE PAPEL KRAFT "
   "CAFÉ idéntico al de la imagen de referencia — con su franja verde y su banda azul "
   "oscura en la cara — dentro de una carretilla con árido, junto a una fundación en "
   "construcción en un terreno de campo. El saco se ve de frente, con su gráfica "
   "nítida y sin deformar. El hombre de perfil, con guantes y camisa de trabajo. "
   "Escena limpia, luz natural. " + ZONA_ARRIBA + " " + COMUN, ["packshots/cbb_saco.png"]),
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
   BODEGA + CIERRE +
   "varias planchas de yeso-cartón de CARA VERDE clara apoyadas de canto, con el "
   "canto rebajado y el papel verde a la vista. Están LISAS, sin impresión, sin texto "
   "y sin logotipo. " + TODO + COMUN, []),
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
  ("05_bodega", "cierre",
   "Interior de una bodega de materiales de construcción, luminosa y ordenada: "
   "estanterías metálicas a ambos lados con pallets de sacos, tablas y perfiles "
   "apilados, y un pasillo central despejado que se pierde en profundidad. Vista "
   "frontal del pasillo. El CENTRO del encuadre queda libre, sin nada apilado. "
   "Imagen entera suavemente DESENFOCADA, como fondo. " + COMUN, []),
  ("01", "ambiente",
   "Estanque de acumulación de agua de hormigón en construcción en un predio rural: "
   "muros circulares de hormigón a la vista, todavía sin agua, con el moldaje recién "
   "retirado. Campo abierto al fondo, día despejado, sin personas. Plano general "
   "tranquilo. " + ZONA_ABAJO + " " + COMUN, []),
  ("02", "producto",
   # RONDA 1: «arreglar imagen para que no se vea como un cuadro en la zona de
   # arriba, mismo comentario del carrusel de CBB.»
   "Plano ABIERTO del muro de un estanque de hormigón deteriorado por el contacto "
   "permanente con agua: manchas de humedad oscuras, eflorescencias blancas de "
   "sales, una fisura vertical y la superficie descascarada con el árido a la "
   "vista. Se ve el muro completo y, detrás, el predio rural y el cielo dando "
   "profundidad. Luz natural lateral. Sin macro ni acercamiento extremo. " + ZONA_ARRIBA + " " + COMUN, []),
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
   "Macro de catálogo de un alambre de púas galvanizado tensado en horizontal: dos "
   "hebras de alambre torcidas entre sí y, cada cierto tramo, una púa de CUATRO PUNTAS "
   # RONDA 1: «muy bien; el fondo cambiarlo por un campo abierto rural estético
   # desenfocado.»
   "afiladas abiertas en cruz. El metal galvanizado gris mate, sin óxido. Detrás, "
   "un campo abierto chileno bonito y suavemente desenfocado: potrero verde, unos "
   "árboles a lo lejos y el cielo de la tarde. Luz natural lateral que marca el "
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
   BODEGA + CIERRE +
   "un rollo de alambre de púas galvanizado, con las espiras y las púas de cuatro "
   "puntas a la vista. " + TODO + COMUN, ["03"]),
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", help="un solo carrusel")
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--rehacer", action="store_true")
    a = ap.parse_args()

    escribir_prompts_md()
    if a.listar:
        for slug, items in LOTE.items():
            print(f"{slug}: " + ", ".join(f"{n}({t})" for n, t, _, _ in items))
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
