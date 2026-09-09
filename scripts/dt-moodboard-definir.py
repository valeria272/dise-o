#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Define las láminas del MoodBoard de la sesión de DoubleTree.

    python scripts/dt-moodboard-definir.py

Escribe `clients/hilton/dt-moodboard-laminas.json`, que después arma
`dt-moodboard-armar.py`. Acá vive el CRITERIO: qué espacio, en qué orden, con qué
regla de rostros y en qué formato. Las rutas de las fotos salen de:

  raw/hilton/dt/moodboard-pin/     referencias (Pinterest, ver dt-moodboard-pinterest.py)
  raw/hilton/dt/sesion-real/       fotos REALES del hotel bajadas de Drive

⚠️ Las láminas «LO QUE YA TENEMOS» son fotos reales de la sesión del hotel y van a
propósito al lado de las referencias: el encargo de Eli fue mejorar lo que existe,
no reemplazarlo.
"""
import io
import json
import os

PIN = "raw/hilton/dt/moodboard-pin"
R1 = "raw/hilton/dt/sesion-real/muestra"    # FINAL 1 — salones y buffet
R2 = "raw/hilton/dt/sesion-real/muestra2"   # FINAL 2 — DT, QB, BW, habitaciones


def p(esp, *nums):
    return [os.path.join(PIN, esp, "%s-%s.jpg" % (esp, n)) for n in nums]


def r1(*n):
    return [os.path.join(R1, "_MG_%s.jpg" % x) for x in n]


def r2(*n):
    return [os.path.join(R2, "_MG_%s.jpg" % x) for x in n]


L = []


def add(titulo, regla, fotos):
    L.append({"titulo": titulo, "regla": regla, "fotos": fotos})


SINP = "Sin personas. El espacio limpio"

# ── 1 · FRONTIS — la altura y la ubicación ───────────────────────────────────
add("FRONTIS · LA ALTURA   —  POST (horizontal)",
    "El hotel es una torre: se fotografía desde abajo y con la ciudad alrededor. " + SINP,
    p("14-frontis", "12", "08", "11"))
add("FRONTIS · LA ALTURA Y LA UBICACIÓN   —  HISTORIA (vertical)",
    "Vertical: la torre completa y la ciudad que la rodea. Sin personas ni autos en primer plano",
    p("14-frontis", "04", "09", "13"))
add("FRONTIS · EL VOLUMEN   —  hora azul",
    "El vidrio devuelve la ciudad: hora azul y luz encendida. " + SINP,
    p("14-frontis", "03", "07", "14"))

# ── 2-4 · accesos e interiores públicos ──────────────────────────────────────
add("ENTRADA / ACCESO   (1/2)",
    "Sin personas. Si aparece un huésped, de espaldas o desenfocado",
    p("01-entrada", "01", "02", "03"))
add("ENTRADA / ACCESO   (2/2)",
    "Sin personas. Si aparece un huésped, de espaldas o desenfocado",
    p("01-entrada", "08", "09", "11"))
add("RECEPCIÓN   (1/2)",
    "Recepcionista SÍ puede aparecer. El huésped, de espaldas o del torso hacia abajo",
    p("02-recepcion", "02", "05", "08"))
add("RECEPCIÓN   (2/2)",
    "Recepcionista SÍ puede aparecer. El huésped, de espaldas o del torso hacia abajo",
    p("02-recepcion", "10", "11", "12"))
# ── 3b · LA LLEGADA Y LA COOKIE — el ícono de la marca ───────────────────────
# La cookie de bienvenida es el símbolo de DoubleTree y hoy NO existe fotografiada
# como producto: la carpeta COOKIE DAY 2026 son fotos del evento interno del
# equipo posando con carteles, todas con rostros. Va en MANOS y plano cerrado.
add("LA LLEGADA · RECEPCIÓN Y CHECK-IN",
    "Recepcionista SÍ puede aparecer. El huésped, de espaldas. La mano que entrega la tarjeta",
    p("21-llegada-cookie", "11", "14", "13"))
add("LA LLEGADA · EL DETALLE   —  la llave y la puerta",
    "Solo manos y objeto. Es el plano corto que hoy no existe y que sirve para historia",
    p("23-llegada-hotel", "07", "09", "11"))
add("LA COOKIE DE BIENVENIDA · EL PRODUCTO",
    "El ícono de la marca, en plano cerrado y sin manos. Fondo neutro, luz cálida",
    p("21-llegada-cookie", "02", "04", "05"))
add("LA COOKIE DE BIENVENIDA · LA ENTREGA",
    "Manos entregando la cookie. Nunca el rostro. Es el gesto que identifica a DoubleTree",
    p("21-llegada-cookie", "07", "09", "06"))
add("LA BIENVENIDA · LA BANDEJA Y EL MESÓN",
    "Bandeja de bienvenida y mesón de conserjería montados. " + SINP,
    [p("21-llegada-cookie", "01")[0]] + p("23-llegada-hotel", "14", "15"))

add("LOBBY   (1/2)", "Sin personas. Se permite silueta desenfocada de paso",
    p("03-lobby", "04", "05", "06"))
add("LOBBY   (2/2)", "Sin personas. Se permite silueta desenfocada de paso",
    p("03-lobby", "08", "09", "11"))

# ── 5 · ESPACIOS GENERALES ───────────────────────────────────────────────────
add("ESPACIOS GENERALES · PASILLOS",
    "El pasillo en fuga, vacío. Es lo que mide la escala del hotel",
    p("16-espacios-generales", "02", "04", "06"))
add("ESPACIOS GENERALES · ASCENSORES Y ESCALERAS",
    SINP + ". Material, luz y simetría",
    p("16-espacios-generales", "09", "10", "13"))

# ── 6 · HABITACIONES — el hotel tiene CINCO tipos ────────────────────────────
add("HABITACIÓN ESTÁNDAR",
    "Sin personas, nunca. Cama montada y la vista desde la ventana",
    p("04a-hab-estandar", "02", "03", "08"))
add("HABITACIÓN ESTÁNDAR · 2 CAMAS",
    "Sin personas, nunca. Las dos camas en el mismo cuadro",
    p("04b-hab-dos-camas", "03", "09", "10"))
add("HABITACIÓN CORNER   —  la esquina con dos ventanales",
    "Es la que justifica la altura: el ventanal de esquina y la ciudad. Sin personas",
    p("04c-hab-corner", "01", "04", "05"))
add("JUNIOR SUITE   —  la sala dentro de la habitación",
    "Sin personas. Se muestra la separación entre el estar y el dormitorio",
    p("04d-junior-suite", "02", "07", "12"))
add("SUITE", "Sin personas. El estar completo y la vista panorámica",
    p("04e-suite", "01", "04", "07"))
add("HABITACIONES · LO QUE YA TENEMOS",
    "De la sesión del hotel: correcto y limpio, pero SIEMPRE el mismo plano y en horizontal",
    r2("0286", "9578", "0472"))

# ── 7 · COWORK — que el empresario venga a trabajar al hotel ─────────────────
add("COWORK · EL ESPACIO   —  1er y 2do piso   (1/2)",
    "El espacio manda. Sin personas. Mostrar la relación entre los dos niveles",
    p("05-cowork", "b04", "b06", "b01"))
add("COWORK · EL ESPACIO   —  1er y 2do piso   (2/2)",
    "Doble altura, escalera y mezzanine en el mismo cuadro. " + SINP,
    p("05-cowork", "b08", "b07", "b09"))
add("COWORK · SILLONES Y MESAS   (1/2)",
    "El estar de trabajo: sillón, mesa baja y luz de ventanal. " + SINP,
    p("05d-cowork-sillones", "01", "05", "10"))
add("COWORK · SILLONES Y MESAS   (2/2)",
    "La mesa con el PC y el café encima, y nadie sentado. Es la foto que vende el espacio",
    p("05d-cowork-sillones", "04", "03", "14"))
add("COWORK · TRABAJAR AQUÍ   —  POST (horizontal)",
    "La persona VA DESENFOCADA y el espacio en foco. Nunca un rostro reconocible",
    p("05-cowork", "c04", "c03", "c13"))
add("COWORK · TRABAJAR AQUÍ   —  HISTORIA (vertical)",
    "De espaldas o fuera de foco. El PC y el café en foco; el espacio, protagonista",
    p("05-cowork", "c01", "c06", "c02"))
add("COWORK · EL DETALLE   —  el PC y el café en foco",
    "Primer plano de PC y taza; el salón detrás, desenfocado. Sirve para historia y para carrusel",
    p("05-cowork", "c15", "c07", "c12"))
add("COWORK · LO QUE YA TENEMOS   —  y qué le falta",
    "De la sesión del hotel. Mesa de trabajo y café REALES: falta el PC abierto, la taza servida y la persona desenfocada",
    r2("9627", "0321", "0633"))

# ── 8 · CAFETERÍA ────────────────────────────────────────────────────────────
add("CAFETERÍA · EL ESPACIO   (1/2)", "Sin rostros. El salón vacío y montado",
    p("06-cafeteria", "04", "06", "12"))
add("CAFETERÍA · EL ESPACIO   (2/2)", "Sin rostros. Luz natural y el ventanal como protagonista",
    p("06-cafeteria", "c14", "c13", "c01"))
add("CAFETERÍA · LA BARRA", "El mesón, la máquina y la estantería. Sin personas",
    p("06-cafeteria", "c02", "c03", "c04"))
add("CAFETERÍA · LA VITRINA   —  bollería",
    "Producto en foco, sin manos. Es el plano que hoy no existe en la sesión",
    p("06-cafeteria", "c09", "c10", "c11"))
add("CAFETERÍA · LAS MANOS   —  el barista",
    "Barista SÍ puede aparecer: manos preparando, delantal, nunca el rostro",
    p("06-cafeteria", "07", "08", "10"))

# ── 9-10 · LAS DOS TERRAZAS, como ESPACIOS del hotel ─────────────────────────
add("TERRAZA DE LA CAFETERÍA   —  POST (horizontal)",
    "Espacio del hotel, no la marca. Día, vegetación y mesas montadas. Sin personas",
    p("11-terraza-cafeteria", "c04", "c07", "c09"))
add("TERRAZA DE LA CAFETERÍA   —  HISTORIA (vertical)",
    "Espacio del hotel, no la marca. Vertical: el jardín y la mesa servida",
    p("11-terraza-cafeteria", "c13", "c10", "c06"))
add("TERRAZA DE LA CAFETERÍA · LO QUE YA TENEMOS",
    "De la sesión del hotel: el jardín vertical y la terraza cubierta. Falta la hora dorada y la mesa montada",
    r2("9380", "9398", "9463"))
add("TERRAZA DEL RESTAURANTE   —  POST (horizontal)",
    "Espacio del hotel, no la marca. Atardecer y noche: velas, guirnaldas y la ciudad de fondo",
    p("12-terraza-restaurant", "c09", "c16", "c06"))
add("TERRAZA DEL RESTAURANTE   —  HISTORIA (vertical)",
    "Vertical: la guirnalda arriba y la vista de la ciudad. Sin rostros",
    p("12-terraza-restaurant", "c07", "c08", "c02"))
add("TERRAZA DEL RESTAURANTE · LA BARRA   —  POST (horizontal)",
    "La barra de la terraza encendida, con la ciudad detrás. " + SINP,
    p("12b-terraza-qb", "05", "07", "14"))
add("TERRAZA DEL RESTAURANTE · LA HORA   —  HISTORIA (vertical)",
    "El atardecer y la hora azul son la firma de esta terraza. Vertical, sin rostros",
    p("12b-terraza-qb", "01", "04", "09"))
add("TERRAZA DEL RESTAURANTE · PÉRGOLA Y LOUNGE",
    "Guirnaldas, vegetación y lounge montado. El plano que muestra el espacio completo",
    p("12b-terraza-qb", "08", "11", "16"))

# ── 11 · RESTAURANTE ─────────────────────────────────────────────────────────
add("RESTAURANTE · EL SALÓN   (1/2)", "Sin comensales. Mesas montadas y la luz del local",
    p("07b-restaurant", "02", "03", "04"))
add("RESTAURANTE · EL SALÓN   (2/2)", "Sin comensales. La banqueta corrida y la lámpara como firma",
    p("07b-restaurant", "06", "07", "12"))
add("RESTAURANTE · MONTAJE Y DESAYUNO   (1/2)",
    "Sin rostros. Manos sirviendo o montaje de mesa sin comensales",
    p("07-restaurant", "03", "04", "05"))
add("RESTAURANTE · MONTAJE Y DESAYUNO   (2/2)", "Sin rostros. El buffet en primer plano",
    p("07-restaurant", "08", "11", "07"))
add("RESTAURANTE · LO QUE YA TENEMOS",
    "De la sesión del hotel: el comedor real. Falta plano cerrado y luz más limpia",
    r2("0733", "0763", "0852"))

# ── 11b · DESAYUNO BUFFET — DT se enfoca acá, no en el desayuno en habitación ─
# Eli, 09-09-2026: «DT quiere enfocarse más en el desayuno buffet del restaurante
# que en el desayuno en habitación». Las bandejas de room service de la sesión
# actual (_MG_9665, _MG_9681) quedan en segundo plano por decisión del cliente.
add("DESAYUNO BUFFET · LAS ESTACIONES   —  POST (horizontal)",
    "El buffet del RESTAURANTE, no la bandeja en la habitación. Estaciones montadas y sin gente",
    p("22-desayuno-buffet", "01", "04", "05"))
add("DESAYUNO BUFFET · EL PRODUCTO   —  HISTORIA (vertical)",
    "Plano cerrado del producto: la torre de bollería, la fruta, el plato servido. Sin manos",
    p("22-desayuno-buffet", "09", "10", "11"))
add("DESAYUNO BUFFET · LA FRUTA Y EL PAN",
    "El color lo pone la fruta. Bandejas alineadas y llenas, en plano medio. " + SINP,
    p("22-desayuno-buffet", "13", "15", "16"))
add("DESAYUNO BUFFET · EL SALÓN A LA HORA DEL DESAYUNO",
    "El comedor con luz de mañana y el buffet al fondo. Sin comensales",
    p("22-desayuno-buffet", "02", "03", "07"))

# ── 12-13 ────────────────────────────────────────────────────────────────────
add("GIMNASIO   (1/2)", "Sin personas. Equipos y sala vacía", p("08-gimnasio", "01", "02", "03"))
add("GIMNASIO   (2/2)", "Sin personas. Equipos y sala vacía", p("08-gimnasio", "07", "09", "10"))
add("WELLNESS LOUNGE / SPA   (1/2)", "Sin rostros. Manos, detalle y sala vacía",
    p("09-wellness-spa", "01", "03", "04"))
add("WELLNESS LOUNGE / SPA   (2/2)", "Sin rostros. Manos, detalle y sala vacía",
    p("09-wellness-spa", "07", "08", "10"))

# ── 14 · EVENTOS CORPORATIVOS — Astoria, Conrat y los demás ──────────────────
add("EVENTOS CORPORATIVOS · LO QUE YA TENEMOS   —  Astoria y Conrat",
    "Sesión real del hotel. Buen espacio, pero SIEMPRE el mismo plano general y en horizontal",
    r1("7166", "7702", "8114"))
add("EVENTOS CORPORATIVOS · LO QUE FALTA   —  el detalle",
    "Lo que la sesión casi no tiene: el puesto, la carpeta, el vaso. Y una persona DESENFOCADA al fondo",
    p("13-eventos-corporativos", "03", "01", "12"))
add("EVENTOS CORPORATIVOS · BOARD ROOM   —  la reunión chica",
    "Directorio montado, sin personas. Es el formato que busca la empresa que viene al hotel",
    p("13-eventos-corporativos", "09", "10", "11"))
add("EVENTOS CORPORATIVOS · MONTAJE   —  HISTORIA (vertical)",
    "Vertical para historia: la mesa en fuga, el material sobre la mesa, la sala en U",
    p("13-eventos-corporativos", "04", "06", "18"))
add("EVENTOS CORPORATIVOS · EL COFFEE BREAK",
    "De la sesión real: el buffet de salón y el detalle de mesa. Falta luz más limpia y plano cerrado",
    r1("8042", "7285", "7570"))

# ── 14b · EL SALÓN REAL — entrada, pantalla + mesas y montaje sencillo ───────
# Eli, 09-09-2026: «en salones me refiero al espacio real que existe». Lo que
# faltaba no era otro salón, sino TRES REGISTROS del que ya tenemos: cómo se
# entra, cómo se ve la pantalla con las mesas, y el montaje sencillo tipo cowork.
add("SALÓN · LA ENTRADA   —  cómo se llega",
    "La puerta del salón en clave corporativa: madera, vidrio y el interior asomando. Sin personas",
    p("17-salon-entrada", "01", "02", "05"))
add("SALÓN · LA SEÑALÉTICA   —  el detalle que ordena",
    "El nombre del salón sobre el muro o la puerta. Plano cerrado, sirve para historia y carrusel",
    p("17-salon-entrada", "07", "08", "09"))
add("SALÓN · EL FOYER   —  la antesala",
    "El espacio previo: alfombra, mesas altas y luz. Es donde espera la empresa antes de entrar. " + SINP,
    p("17-salon-entrada", "13", "14", "15"))
add("SALÓN · PANTALLA + MESAS   —  POST (horizontal)",
    "La pantalla encendida y las mesas montadas en el mismo cuadro. Sin personas",
    p("18-salon-pantalla-mesas", "03", "12", "15"))
add("SALÓN · PANTALLA + MESAS   —  HISTORIA (vertical)",
    "Vertical: la pantalla al fondo y la mesa entrando en cuadro. Sin personas",
    p("18-salon-pantalla-mesas", "02", "16", "11"))
add("SALÓN · PANTALLA + MESAS · LO QUE YA TENEMOS",
    "Sesión real: la pantalla con el logo DT y el montaje. Falta variar el plano y apagar el logo repetido",
    r1("8244", "7417", "7166"))
add("SALÓN SENCILLO · ESTILO COWORK   (1/2)",
    "Sala chica y clara, tabique de vidrio y mesa simple. Sin mantel largo ni faldón. " + SINP,
    p("19-salon-sencillo-cowork", "07", "08", "10"))
add("SALÓN SENCILLO · ESTILO COWORK   (2/2)",
    "Luz natural, madera clara y silla de oficina. El registro de reunión de trabajo, no de banquete",
    p("19-salon-sencillo-cowork", "03", "05", "13"))
add("SALÓN · EL CAFÉ DEL FOYER",
    "La estación de café del coffee break, montada y sin personas. Plano cerrado para historia",
    p("20-salon-foyer-cafe", "01", "08", "11"))

# ── 15 · MESAS REDONDAS — el montaje que NO está fotografiado ────────────────
add("SALONES · MESAS REDONDAS   —  POST (horizontal)",
    "El montaje que no tenemos fotografiado: redondas vestidas, salón completo y vacío",
    p("15-salones-redondas", "03", "05", "13"))
add("SALONES · MESAS REDONDAS   —  HISTORIA (vertical)",
    "Vertical: la redonda montada, el centro de mesa y la vajilla. Sin comensales",
    p("15-salones-redondas", "11", "10", "09"))
add("SALONES · MESAS REDONDAS   —  EL DETALLE",
    "Cenital del puesto y del centro de mesa. Es el plano de carrusel que hoy no existe",
    p("15-salones-redondas", "08", "12", "02"))
add("SALONES · MONTAJE SOCIAL", "Sin personas. Salón montado, vacío",
    p("10-salones", "01", "07", "08"))


def main():
    faltan = [f for x in L for f in x["fotos"] if not os.path.exists(f)]
    destino = "clients/hilton/dt-moodboard-laminas.json"
    json.dump(L, io.open(destino, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("laminas: %d  |  fotos: %d" % (len(L), sum(len(x["fotos"]) for x in L)))
    print("FALTAN:", faltan if faltan else "ninguna")
    print("->", destino)


if __name__ == "__main__":
    main()
