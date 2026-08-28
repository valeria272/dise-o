"""Saca de la PPT vieja los mapas y planimetrías limpios, sin el encabezado en Calibri.

Trampas del archivo original, todas comprobadas:
  · el título va a veces como texto y a veces como IMAGEN, y se superpone en altura
    con la foto útil — por eso se borran cajas puntuales, no una banda;
  · varias páginas tienen fondo rosado, no blanco: si se tapa con blanco queda una
    caja visible, así que se tapa con el color real del fondo;
  · un marco rojo pegado al borde de la página sobrevive a cualquier recorte por
    contenido, así que se recorta la página hacia adentro ANTES de ajustar.
"""
import fitz, re, numpy as np
from PIL import Image

RUTA = "/Users/Vale/Downloads/Mas Center- Proyectos Operativos (1).pdf"
CABECERA = re.compile(r"(strip\s*center|placa\s*comercial|locales?\b|m[áa]s\s*center|"
                      r"grupo\s*ifb|inversiones|presentaci[óo]n)", re.I)
CAFE = (0.337, 0.173, 0.173)          # banner "PRIMER PISO" del original

def limpiar(pag, salida, dpi=300, margen=0.025):
    d = fitz.open(RUTA); p = d[pag-1]; H, W = p.rect.height, p.rect.width
    px = p.get_pixmap(dpi=dpi); k = dpi/72.0
    a = np.array(Image.frombytes("RGB", (px.width, px.height), px.samples))
    alto, ancho = a.shape[:2]

    # 1. recortar hacia adentro: mata el marco rojo del borde
    mx, my = int(ancho*margen), int(alto*margen)
    a = a[my:alto-my, mx:ancho-mx]
    fondo = np.median(a[:12, :12].reshape(-1,3), axis=0).astype(np.uint8)   # color real del papel

    def borrar(r):
        x0 = int(r.x0*k)-mx-2; y0 = int(r.y0*k)-my-2
        x1 = int(r.x1*k)-mx+2; y1 = int(r.y1*k)-my+2
        a[max(0,y0):max(0,y1), max(0,x0):max(0,x1)] = fondo

    # 2. borrar encabezado viejo (texto o imagen) y el banner café
    for b in p.get_text("dict")["blocks"]:
        r = fitz.Rect(b["bbox"])
        if not (0 <= r.y0 < H) or r.height <= 0: continue
        arriba = r.y0 < H*0.22 and r.height < H*0.12
        if b["type"] == 1:
            if arriba: borrar(r)
        else:
            t = " ".join(s["text"] for l in b["lines"] for s in l["spans"])
            if arriba or (r.y0 < H*0.30 and CABECERA.search(t)): borrar(r)
    for dr in p.get_drawings():
        r = dr["rect"]; col = dr.get("fill") or dr.get("color")
        if col and r.y0 < H*0.25 and r.height < H*0.10 and r.width < W*0.55 \
           and all(abs(col[i]-CAFE[i]) < .12 for i in range(3)):
            borrar(r)
    d.close()

    # 3. ajustar al contenido, midiendo contra el fondo real
    # líneas rojas sueltas del marco original, arriba y abajo
    rojiza = ((a[...,0].astype(int) > a[...,1].astype(int)+30) &
              (a[...,0].astype(int) > a[...,2].astype(int)+30))
    for banda in (slice(0, int(a.shape[0]*0.09)), slice(int(a.shape[0]*0.91), None)):
        for y in range(*banda.indices(a.shape[0])):
            fila = rojiza[y]
            if fila.sum() > a.shape[1]*0.45:      # una línea, no un elemento del plano
                a[y] = fondo

    dist = np.linalg.norm(a.astype(int) - fondo.astype(int), axis=-1)
    ys, xs = np.where(dist > 16)
    if not len(ys): return None
    im = Image.fromarray(a).crop((max(0,xs.min()-8), max(0,ys.min()-8),
                                  min(a.shape[1], xs.max()+9), min(a.shape[0], ys.max()+9)))
    im.save(salida, optimize=True)
    return im.size

if __name__ == "__main__":
    for pg in [9,10,1,2,23,24,49,50]:
        print(pg, limpiar(pg, f"_t{pg}.png"))


def satelites(pag):
    """Devuelve las fotos satelitales CRUDAS de una página de mapa (sin marco ni título).

    Reusar la página entera era pelear con el marco rojo y el fondo rosado; las fotos
    embebidas salen limpias y la anotación se vuelve a dibujar en el sistema nuevo.
    """
    d = fitz.open(RUTA); p = d[pag-1]; W = p.rect.width
    vistos, fotos = set(), []
    for i in sorted(p.get_image_info(xrefs=True),
                    key=lambda i: -(fitz.Rect(i["bbox"]).width * fitz.Rect(i["bbox"]).height)):
        xref = i.get("xref"); r = fitz.Rect(i["bbox"])
        if not xref or xref in vistos: continue
        img = d.extract_image(xref)
        if img["width"] < 300 or r.width < W*0.25: continue    # descarta logos y cajas de título
        vistos.add(xref)
        fotos.append({"xref": xref, "bytes": img["image"], "ext": img["ext"],
                      "px": (img["width"], img["height"]),
                      "caja": (r.x0, r.y0, r.x1, r.y1)})
    d.close()
    return fotos[:2]          # [detalle, contexto]
