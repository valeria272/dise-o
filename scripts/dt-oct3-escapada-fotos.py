"""DT · FEED 07-10 · CARRUSEL Escapada Romántica (atemporal): las dos fotos.

1 · PORTADA — «Habitación ambientada al atardecer, pareja brindando. Tonos cálidos,
    luz tenue, con el espumante en primer plano». Método aprobado del banco de la
    familia (R-69): la foto REAL de DT es el fondo (`sep_26-505`, sesión SEP 2026, sin
    usar en el feed → R-75) y Nano Banana Pro sólo agrega la pareja, la cubeta y la luz
    del atardecer en la ventana. Pareja distinta de la familia y de la del feriado
    (R-68, R-08). Tono de ESCAPADA, no de noche de bodas (R-74): ropa de fin de semana,
    nada de pétalos ni batas.
2 · PERSONALIZA — «Detalle de mesa en QB Restaurant al atardecer con dos tragos». No
    hay foto real en alta (la terraza sólo está en miniaturas de noche): se genera la
    mesa de la terraza de QB tomando como referencia el visual Sunset QB aprobado.

    py scripts/dt-oct3-escapada-fotos.py portada a
    py scripts/dt-oct3-escapada-fotos.py sunset a
"""
import os, subprocess, sys
from PIL import Image

sys.path.insert(0, "scripts/dt-familia")
from ronda3 import ANAT, KEEP, NAT

R = "raw/hilton/dt/oct3-escapada/"
os.makedirs(R, exist_ok=True)
QUE = sys.argv[1]
SUF = sys.argv[2] if len(sys.argv) > 2 else "a"
RES = "4K" if QUE == "portada2" else "2K"


def nb(prompt, refs, out):
    r = subprocess.run(["py", "scripts/magnific.py", "pro", prompt, "--refs", *refs,
                        "--aspecto", "carrusel", "--resolucion", RES, "--out", out],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    print((r.stdout + r.stderr)[-500:])


if QUE == "portada":
    O = Image.open("raw/hilton/sesion-sep2026/alta/sep_26-505.jpg")
    w, h = O.size
    cw = int(h * 4 / 5)
    x0 = int(w * 0.47) - cw // 2          # ventana + cama
    O.crop((x0, 0, x0 + cw, h)).resize((1600, 2000), Image.LANCZOS).save(R + "fondo-505.jpg", quality=93)
    WHO = ("Add ONE couple in their early thirties, Chilean, natural look: she has long wavy chestnut hair, he has short "
           "black hair and light stubble. Weekend-getaway clothes: she wears a soft camel knit sweater and jeans, he a "
           "rolled-sleeve white linen shirt and dark chinos. Different faces from any other photo.")
    ACT = ("They sit side by side on the foot of the bed, relaxed and turned to each other, clinking two flutes of "
           "sparkling wine with calm, closed-mouth smiles. In the FOREGROUND, lower left, a small side table with a "
           "silver ice bucket holding a sparkling wine bottle, slightly out of focus. Through the window, the city at "
           "golden-hour sunset: warm orange sky seen through the sheer curtain, soft warm light in the room, lamps on. "
           "A spontaneous escape weekend in the city, NOT a wedding night: no rose petals, no bathrobes, no candles, "
           "no bridal details. Keep exactly the same camera framing, room and furniture as image 1.")
    nb(f"{KEEP} {WHO} {ACT} {ANAT} {NAT}", [R + "fondo-505.jpg"], R + f"portada-{SUF}.png")

elif QUE == "portada2":
    # ⭐ Ronda 4 (Eli 29-09): «la pareja se ve extraña, debe ser realista y una foto actual de
    # sesión de habitación mejor lograda». Se cambia la base por `sep_26-476` (king con banqueta y
    # ventanal con sol de tarde, sesión SEP 2026, sin usar) y la pareja se pide en registro de
    # FOTO DE SESIÓN: luz y color de la foto original, sin atardecer pintado ni naranja.
    O = Image.open("raw/hilton/sesion-sep2026/alta/sep_26-476.jpg")
    w, h = O.size
    cw = int(h * 4 / 5)
    x0 = int(w * 0.42) - cw // 2          # ventana + cama, sin el mueble del minibar
    O.crop((x0, 0, x0 + cw, h)).resize((2400, 3000), Image.LANCZOS).save(R + "fondo-476.jpg", quality=94)
    WHO = ("Add ONE real couple in their early thirties, Chilean, ordinary attractive people (not models): she has "
           "shoulder-length dark brown hair loosely tucked behind one ear, he has short dark brown hair and a short "
           "neat beard. Simple weekend clothes with real fabric texture and natural wrinkles: she wears a cream "
           "fine-knit sweater and light blue jeans, he a navy crewneck sweater and grey trousers, white sneakers.")
    ACT = ("They sit close together on the leather bench at the foot of the bed, both seated fully on the bench "
           "cushion, feet flat on the carpet, turned slightly toward each other, clinking two flutes of sparkling wine "
           "held at chest height, looking at each other with soft natural smiles, mid-conversation. On the right "
           "bedside table, a small silver ice bucket with a sparkling wine bottle. Keep the real afternoon daylight "
           "of image 1: the soft sun coming through the sheer curtain and the lamps on, same colours and same muted "
           "neutral grading — do NOT add an orange sunset, do NOT warm or saturate the image. People at correct scale "
           "for the bench and the bed. A spontaneous city escape, NOT a wedding night: no rose petals, no bathrobes, "
           "no candles, no bridal details. Keep exactly the same camera framing, room and furniture as image 1.")
    REAL = ("Photographic realism is the priority: it must look like an unretouched frame from the same professional "
            "hotel photo session, shot on a full-frame camera with a 24mm lens at f/5.6, natural skin with pores and "
            "slight imperfections, no plastic or painted look, no illustration, no HDR, no glow, no cinematic colour "
            "grading, faces sharp and proportionate to the bodies.")
    nb(f"{KEEP} {WHO} {ACT} {ANAT} {NAT} {REAL}", [R + "fondo-476.jpg"], R + f"portada2-{SUF}.png")

elif QUE == "subir2":
    Image.open(R + f"portada2-{SUF}.png").convert("RGB").resize((2250, 2813), Image.LANCZOS).save(
        "public/assets/hilton/dt/oct3/er-portada.jpg", quality=92)
    print("ok er-portada.jpg (ronda 4)")

elif QUE == "subir":
    # La variante elegida deja las caras a la altura del titular (y≈0,31). Sobra alfombra
    # abajo: se EXPANDE el techo (Flux Pro expand, sólo arriba) y se recorta lo mismo de
    # alfombra, así la pareja baja ~11 % sin redibujarla. Encima va la variante original
    # con borde suave: pareja, cubeta y habitación son los píxeles ya revisados.
    from PIL import ImageFilter
    sys.path.insert(0, "scripts")
    import magnific as M
    src = Image.open(R + f"portada-{SUF}.png").convert("RGB")
    w, h = src.size
    top = int(h * 0.11)
    entrada = R + f"portada-{SUF}-entrada.jpg"
    src.save(entrada, quality=94)
    crudo = R + f"portada-{SUF}-expandida.jpg"
    if not os.path.exists(crudo):
        r = M.pedir("/v1/ai/image-expand/flux-pro", {
            "image": M.b64_de(entrada),
            "prompt": "the same hotel room ceiling continues upward: smooth warm beige ceiling, the top of the brown "
                      "curtains and the dark headboard panel, soft warm lamp light. No people, no objects, no lamps added.",
            "left": 0, "right": 0, "top": top, "bottom": 0})
        M.guarda(M.espera("/v1/ai/image-expand/flux-pro", r.get("data", r).get("task_id")), crudo)
    exp = Image.open(crudo).convert("RGB").resize((w, h + top), Image.LANCZOS)
    borde = 40
    mascara = Image.new("L", (w, h), 255)
    mascara.paste(Image.new("L", (w, borde), 0), (0, 0))
    mascara = mascara.filter(ImageFilter.GaussianBlur(borde / 2))
    exp.paste(src, (0, top), mascara)
    exp = exp.crop((0, 0, w, h))                       # fuera la alfombra de abajo
    os.makedirs("public/assets/hilton/dt/oct3", exist_ok=True)
    exp.resize((2250, 2813), Image.LANCZOS).save("public/assets/hilton/dt/oct3/er-portada.jpg", quality=92)
    print("ok er-portada.jpg")

elif QUE == "sunset-final":
    Image.open(R + f"sunset-{SUF}.png").convert("RGB").resize((2250, 2813), Image.LANCZOS).save(
        "public/assets/hilton/dt/oct3/er-sunset.jpg", quality=92)
    print("ok er-sunset.jpg")

elif QUE == "sunset":
    ref = R + "ref-sunset-qb.jpg"
    Image.open("raw/hilton/qb/aprobadas/KV SUNSET QB 1.png").convert("RGB").save(ref, quality=92)
    P = ("Image 1 is the approved visual of the QB Restaurant terrace at sunset: use it ONLY as reference for the place "
         "(wooden slatted table, glass roof with iron frame, woven rattan pendant lamps, plants, warm low sun). "
         "Create a NEW close detail photo on that same terrace table at golden-hour sunset with exactly TWO cocktails for "
         "two people: one Aperol-style spritz in a wine glass with an orange slice, and one gin tonic in a balloon glass "
         "with lime and rosemary, placed a little apart as if a couple were sharing them, plus a small plate with a "
         "starter in soft focus behind. Shallow depth of field, warm backlight, real professional food-and-drink "
         "photography, natural condensation. NO text, NO logos, NO people, NO hands. The top half of the frame is the "
         "blurred terrace with lamps and sky (space for text).")
    nb(P, [ref], R + f"sunset-{SUF}.png")
