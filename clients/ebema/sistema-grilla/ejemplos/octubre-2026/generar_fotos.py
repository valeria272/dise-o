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

ZONA_ARRIBA = ("Encuadre con aire arriba: en el tercio superior sólo hay fondo "
               "fotográfico desenfocado y de tono parejo — muro, cielo o profundidad "
               "de campo —, sin objetos que llamen la atención. " + LLENA)
ZONA_ABAJO  = ("Encuadre con aire abajo: en la mitad inferior sólo hay superficie "
               "continua y de tono parejo — suelo, pasto, terreno o piso —, sin "
               "objetos que llamen la atención. " + LLENA)

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
  ("04", "cierre",
   "Clóset empotrado terminado, integrado de muro a muro en un dormitorio luminoso y "
   "ordenado, puertas de tablero melamínico de tono madera claro. Imagen suavemente "
   "DESENFOCADA en conjunto, como fondo: sin ningún detalle que compita con el centro "
   "de la composición, que queda libre. " + COMUN, ["02"]),
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
   "Patio trasero de una casa chilena a comienzos de primavera, con el pasto natural "
   "descuidado: manchones amarillos, tierra pelada a la vista y bordes irregulares. "
   "Un muro de cierre simple al fondo y algo de vegetación. Día nublado suave, sin "
   "personas. Plano general tranquilo. " + ZONA_ABAJO + " " + COMUN, []),
  ("03", "escena",
   "Instalador desenrollando un rollo de pasto sintético sobre una base de tierra "
   "compactada y nivelada en un patio. Se ve el rollo a medio extender, el borde de "
   "la lámina y el respaldo por el reverso. El hombre está agachado, de perfil, con "
   "guantes de trabajo. Patio despejado, día luminoso. " + ZONA_ARRIBA + " " + COMUN, ["02"]),
  ("04", "ambiente",
   "Patio residencial terminado con pasto sintético verde parejo, integrado con una "
   "terraza de madera y una zona de juegos simple. Ordenado, luminoso, primavera, "
   "sin personas. Plano general amplio. " + ZONA_ARRIBA + " " + COMUN, ["02"]),
  ("05", "cierre",
   "Un rollo de pasto sintético apoyado de pie sobre un piso de patio, mostrando el "
   "canto enrollado y el verde de las fibras. Imagen suavemente DESENFOCADA en "
   "conjunto, como fondo, con el centro de la composición libre. " + COMUN, ["02"]),
 ],

 # ------------------------------------------------------------------- CBB ---
 "cbb": [
  ("05", "cierre",
   "Pila ordenada de sacos de cemento de papel kraft gris claro, apilados sobre un "
   "pallet de madera en una bodega luminosa. Los sacos están LISOS, sin ninguna "
   "impresión, sin texto y sin logotipo. Imagen suavemente DESENFOCADA en conjunto, "
   "como fondo, con el centro de la composición libre. " + COMUN, []),
  ("01", "ambiente",
   "Fundación de hormigón recién hormigonada en un terreno agrícola chileno: zanjas "
   "corridas y sobrecimiento a la vista sobre tierra de cultivo oscura, con un cerco "
   "de campo y un potrero verde al fondo. Día despejado, luz de la tarde, sin personas. "
   "Plano general tranquilo. " + ZONA_ABAJO + " " + COMUN, []),
  ("02", "producto",
   "Macro de catálogo de una superficie de hormigón deteriorado por ataque químico: "
   "la pasta de cemento disgregada y pulverulenta, los áridos quedando expuestos, "
   "microfisuras y una eflorescencia blanquecina. Textura muy nítida, luz rasante que "
   "marca el relieve del daño. " + ZONA_ARRIBA + " " + COMUN, []),
  ("03", "escena",
   "Maestro hormigonero chileno vaciando cemento gris desde un saco de papel kraft "
   "liso y sin impresión dentro de una carretilla con árido, junto a una fundación en "
   "construcción en un terreno de campo. El hombre de perfil, con guantes y camisa de "
   "trabajo. Escena limpia, luz natural. " + ZONA_ARRIBA + " " + COMUN, ["05"]),
  ("04", "ambiente",
   "Radier y fundación de hormigón ya terminados y curados en una parcela agrícola, "
   "superficie gris pareja y bien platachada, con el campo abierto al fondo. Ordenado, "
   "sin personas, luz natural suave. " + ZONA_ARRIBA + " " + COMUN, []),
 ],

 # ------------------------------------------------------------- VOLCANITA ---
 # La cara VERDE es lo que hace reconocible a una placa de yeso-cartón resistente a
 # la humedad. Sin ese verde es una placa cualquiera, así que va en todos los prompts.
 "volcanita": [
  ("05", "cierre",
   "Varias planchas de yeso-cartón resistente a la humedad, de CARA VERDE clara, "
   "apoyadas de canto contra el muro de una bodega luminosa. Se ve el canto rebajado "
   "y el papel verde. Las planchas están LISAS, sin ninguna impresión, sin texto y sin "
   "logotipo. Imagen suavemente DESENFOCADA en conjunto, como fondo, con el centro de "
   "la composición libre. " + COMUN, []),
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
  ("05", "cierre",
   "Pila ordenada de sacos de cemento de papel kraft gris claro sobre un pallet de "
   "madera en una bodega luminosa. Los sacos están LISOS, sin ninguna impresión, sin "
   "texto y sin logotipo. Imagen suavemente DESENFOCADA en conjunto, como fondo, con "
   "el centro de la composición libre. " + COMUN, []),
  ("01", "ambiente",
   "Estanque de acumulación de agua de hormigón en construcción en un predio rural: "
   "muros circulares de hormigón a la vista, todavía sin agua, con el moldaje recién "
   "retirado. Campo abierto al fondo, día despejado, sin personas. Plano general "
   "tranquilo. " + ZONA_ABAJO + " " + COMUN, []),
  ("02", "producto",
   "Macro de catálogo de un muro de hormigón deteriorado por contacto permanente con "
   "agua: manchas de humedad oscuras, eflorescencias blancas de sales, una fisura "
   "vertical y la superficie descascarada dejando el árido a la vista. Textura muy "
   "nítida, luz rasante. " + ZONA_ARRIBA + " " + COMUN, []),
  ("03", "escena",
   "Maestro hormigonero mezclando cemento gris en una betonera junto a un pozo en "
   "construcción en el campo, vaciando el contenido de un saco de papel kraft liso y "
   "sin impresión. De perfil, guantes y camisa de trabajo. Escena limpia, luz natural. "
   + ZONA_ARRIBA + " " + COMUN, ["05"]),
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
   "afiladas abiertas en cruz. El metal galvanizado gris mate, sin óxido. Fondo de "
   "campo completamente desenfocado. Luz natural lateral que marca el brillo del "
   "alambre. " + ZONA_ARRIBA + " " + COMUN, []),
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
  ("05", "cierre",
   "Un rollo de alambre de púas galvanizado apoyado sobre el pasto de un potrero, con "
   "las espiras del rollo y las púas a la vista. Imagen suavemente DESENFOCADA en "
   "conjunto, como fondo, con el centro de la composición libre. " + COMUN, ["03"]),
 ],
}


# ⛔ EL BUILD CONSUME .jpg, NO .png. Magnific devuelve un PNG de 4K y ~18 MB; el
# render sale a 2250 de ancho, así que se guarda como JPEG de 2400 y calidad 92
# (sin submuestreo de croma) y ESE es el archivo que se versiona en
# public/assets/ebema/grilla-oct26/ y el que leen los carruseles. Es la regla de
# «el render vuelve al repo el mismo día»: sin el fondo versionado la pieza no se
# puede volver a sacar igual, porque una imagen de IA no se regenera dos veces igual.
def ruta(slug, nombre):
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
