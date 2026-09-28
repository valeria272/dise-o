"""Pendones DT 0,8x3 m: toma el PDF de Illustrator con las mesas a 82x302 cm (arte + 1 cm de sangrado)
y arma el PDF de imprenta: hoja con margen, marcas de corte vectoriales FUERA del sangrado,
TrimBox 80x300 cm y BleedBox 82x302 cm. Illustrator por script no respeta el sangrado (28-09-2026)."""
import sys, pymupdf as fitz

CM = 72 / 2.54
SANG, MARGEN, LARGO, SEP = 1 * CM, 2.5 * CM, 1.2 * CM, 0.3 * CM

def armar(entrada, salida):
    src = fitz.open(entrada)
    out = fitz.open()
    for i, sp in enumerate(src):
        w, h = sp.rect.width, sp.rect.height            # 82 x 302 cm
        pg = out.new_page(width=w + 2 * MARGEN, height=h + 2 * MARGEN)
        pg.show_pdf_page(fitz.Rect(MARGEN, MARGEN, MARGEN + w, MARGEN + h), src, i)
        t = fitz.Rect(MARGEN + SANG, MARGEN + SANG, MARGEN + w - SANG, MARGEN + h - SANG)  # corte 80x300
        reg = (0, 0, 0, 1)  # negro de registro
        for x in (t.x0, t.x1):
            for y, s in ((t.y0, -1), (t.y1, 1)):
                a = y + s * (SANG + SEP)
                pg.draw_line((x, a), (x, a + s * LARGO), color=(0, 0, 0), width=0.5)
        for y in (t.y0, t.y1):
            for x, s in ((t.x0, -1), (t.x1, 1)):
                a = x + s * (SANG + SEP)
                pg.draw_line((a, y), (a + s * LARGO, y), color=(0, 0, 0), width=0.5)
        pg.set_bleedbox(fitz.Rect(MARGEN, MARGEN, MARGEN + w, MARGEN + h))
        pg.set_trimbox(t)
        pg.insert_text((MARGEN, MARGEN - 0.6 * CM), f"Pendón DT {i+1} · corte 80 x 300 cm · sangrado 1 cm",
                       fontsize=14, color=(0, 0, 0))
    out.save(salida, garbage=3, deflate=True)
    print("→", salida)

if __name__ == "__main__":
    armar(sys.argv[1], sys.argv[2])
