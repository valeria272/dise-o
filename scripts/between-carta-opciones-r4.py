#!/usr/bin/env python3
"""BETWEEN · carta — RONDA 4 (25-09-2026): Eli se queda con la opción C · Taupe y sticker.

Feedback sobre la ronda 3: «las ilustraciones se ven muy toscas; que sean texturas, que no
destaquen». Se cambia SÓLO el fondo de trazos: en vez de 15–20 dibujos grandes sueltos, una
textura fina (muchos íconos chicos de línea delgada, repartidos parejo, como papel de
pastelería) al 6 % en beige. Sigue variando por hoja: desayuno · pastelería · café.
Todo lo demás es la opción C de `between-carta-opciones-r3.py`.

    python scripts/between-carta-opciones-r4.py
Salida: out/hilton/between/carta-opciones/r4/{html,png,pdf}/
"""
import importlib.util, sys
from pathlib import Path
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
_s = importlib.util.spec_from_file_location("r3", Path(__file__).with_name("between-carta-opciones-r3.py"))
r3 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(r3)

A_ = r3.r2.BW / "carta"
for tema in ("desayuno", "pasteleria", "cafe"):
    r3.R3[f"fondo_{tema}"] = r3.u(A_ / f"tex-{tema}.png")

_fondo = r3.fondo_trazos
# textura: más tenue que los trazos sueltos (0,075) porque cubre toda la hoja
r3.fondo_trazos = lambda url, color, opacidad: _fondo(url, color, 0.06)

OUT = r3.r2.RAIZ / "out/hilton/between/carta-opciones/r4"


def main():
    for d in ("html", "png", "pdf"):
        (OUT / d).mkdir(parents=True, exist_ok=True)
    for hoja, html in zip(r3.HOJAS, r3.op_c()):
        n = f"BW-CARTA-R4-OPC-{hoja}"
        h = OUT / "html" / f"{n}.html"
        h.write_text(html, encoding="utf-8")
        r3.render(h, OUT / "png" / f"{n}.png", OUT / "pdf" / f"{n}.pdf")
        print("✓", n)


if __name__ == "__main__":
    main()
