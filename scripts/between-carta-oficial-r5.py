#!/usr/bin/env python3
"""BETWEEN · CARTA OFICIAL Desayuno/Almuerzo 2026 — R5 (29-09-2026): las 4 opciones aprobadas en la
R4 (`between-carta-oficial-r4.py`), afinadas para IMPRENTA y DIGITAL.

Pedido de Eli 29-09: «mejora los editables… al momento de corregir va a ser muy difícil, debe ser
fácil; verifica tamaños mínimos, será para impresión y digital; 0,3 cm de sangrado para que no se
vea el límite ni queden bordes sin color; mejora jerarquías y recuerda las reglas; en las 4 opciones».

Lo que cambia contra la R4 (el diseño, la secuencia y las ilustraciones son los aprobados):
  · TAMAÑOS MÍNIMOS: nada bajo 7,5 pt. Descripción 8 → 8,5 pt · notas 7,8 → 8 pt · cabeceras de
    columna 6,8 → 7,5 pt · leyenda 7 → 7,5 pt · rótulos de contacto 6,6 → 7,5 pt · plato 9 → 9,5 pt
  · TEXTO A TINTA LLENA: las descripciones (88 %), notas (90 %) y cabeceras (80 %) iban con
    transparencia; en papel eso es trama fina y en pantalla pierde contraste → 100 %
  · JERARQUÍA: en B y D el rótulo de sección (8 pt) era MÁS CHICO que el plato (9 pt) → 10 pt;
    el orden queda sección > plato > descripción > nota en todas
Después: `between-carta-oficial-editable-r5.py` (mide) → `between-carta-oficial-ai-r5.jsx` (arma
el .ai nativo con estilos) → `between-carta-oficial-imprenta-r5.py` (PDF imprenta y digital).

    python scripts/between-carta-oficial-r5.py [A B C D]
Salida: out/hilton/between/carta-oficial/r5/{html,png,pdf}/
"""
import importlib.util, json, re, subprocess, sys
from pathlib import Path
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

_s = importlib.util.spec_from_file_location("r4", Path(__file__).with_name("between-carta-oficial-r4.py"))
r4 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(r4)
OUT = r4.r2.RAIZ / "out/hilton/between/carta-oficial/r5"

# (buscar, reemplazar) sobre el HTML de la R4 — cada uno tiene que aparecer, si no el script para
COMUN = [
    (".it .d{font-size:8pt;font-weight:400;line-height:1.32;opacity:.88;",
     ".it .d{font-size:8.5pt;font-weight:400;line-height:1.3;"),
    ("letter-spacing:.1em;text-transform:uppercase;opacity:.8;line-height:1.15}",
     "letter-spacing:.1em;text-transform:uppercase;line-height:1.15}"),
    ("font-size:6.8pt;font-weight:600;", "font-size:7.5pt;font-weight:600;"),
    (".nt{font-size:7.8pt;line-height:1.35;font-style:italic;opacity:.9;", ".nt{font-size:8pt;line-height:1.35;font-style:italic;"),
    (".leyenda{font-size:7pt;", ".leyenda{font-size:7.5pt;"),
]
POR_OPCION = {
    "A": [(".it .f{font-size:9pt;letter-spacing:.05em;", ".it .f{font-size:9.5pt;letter-spacing:.05em;"),
          ("text-align:right;font-size:7.4pt;", "text-align:right;font-size:7.5pt;")],
    "B": [("font-weight:700;font-size:8pt;letter-spacing:.16em;text-transform:uppercase;line-height:1;white-space:nowrap}",
           "font-weight:700;font-size:10pt;letter-spacing:.16em;text-transform:uppercase;line-height:1;white-space:nowrap}"),
          (".ov.largo{font-size:7.2pt;", ".ov.largo{font-size:9pt;"),
          (".sc .pre{font-size:7.6pt;", ".sc .pre{font-size:8pt;"),
          (".it .f{font-size:9pt;letter-spacing:.04em;", ".it .f{font-size:9.5pt;letter-spacing:.04em;")],
    "C": [("text-align:right;font-size:7.4pt;", "text-align:right;font-size:7.5pt;"),
          (".sc .cab .hr{font-size:7.6pt;", ".sc .cab .hr{font-size:8pt;")],
    "D": [("font-size:8pt;letter-spacing:.16em;text-transform:uppercase;line-height:1;white-space:nowrap}\n    .rect.largo{font-size:7.4pt;",
           "font-size:10pt;letter-spacing:.16em;text-transform:uppercase;line-height:1;white-space:nowrap}\n    .rect.largo{font-size:9pt;"),
          (".sc .pre{font-size:7.6pt;", ".sc .pre{font-size:8pt;"),
          (".it .f{font-size:9pt;letter-spacing:.04em;", ".it .f{font-size:9.5pt;letter-spacing:.04em;"),
          ("font-size:6.6pt;font-weight:600;", "font-size:7.5pt;font-weight:600;"),
          ("text-transform:uppercase;opacity:.8\">", "text-transform:uppercase\">"),
          # Eli 29-09: la etiqueta «MENÚ» en rectángulo sobraba; si va, que sea UN título en letra
          # atractiva y mejor diagramado → Brushwell grande abriendo el panel del logo, filete fino debajo
          ('<div class="abs" style="left:85mm;right:0;top:16mm;text-align:center"><span class="rect">Menú</span></div>',
           '<div class="abs titulo" style="left:85mm;right:0;top:30mm;text-align:center;font-family:Brushwell;font-weight:400;'
           'font-size:54pt;line-height:1;letter-spacing:.02em;text-transform:none">Menú</div>'
           '<div class="abs" style="left:118.5mm;width:18mm;top:53.5mm;border-top:.15mm solid currentColor"></div>')],
}


# B y D: a 10 pt «TENTACIONES DE NUESTRA VITRINA» ya no entra en la columna de 67 mm (se cortaba
# «VITRIN»): el rótulo más largo va en DOS líneas centradas, en vez de achicarlo bajo el plato
DOS_LINEAS = ("Tentaciones de nuestra vitrina", "Tentaciones de<br>nuestra vitrina")
CSS_DOS = (".ov.dos,.rect.dos{white-space:normal;text-align:center;line-height:1.3;font-size:9.5pt;letter-spacing:.14em}"
           ".ov.dos{padding:3.2mm 7mm 3mm}")


_SEC_CAJA = ("{{font-size:12pt!important;font-weight:800!important;letter-spacing:.1em!important;"
             "white-space:normal!important;text-align:center;line-height:1.25!important;text-wrap:balance;"
             "max-width:100%;box-sizing:border-box}}")
SECCION = {"A": ".ix h2{font-size:13pt!important;font-weight:800!important}",
           "B": ".ov,.ov.largo,.ov.dos" + _SEC_CAJA.format(),
           "D": ".rect,.rect.largo,.rect.dos" + _SEC_CAJA.format()}


def html_r5(op):
    h = r4.OPCIONES[op]()
    # la hoja base de la R2 todavía les ponía 78 % y 80 % a descripciones y cabeceras: tinta llena
    h = h.replace("</style>", ".it .d,.cabcol,.nt{opacity:1!important}</style>", 1)
    if op in "BD":
        for cls in ("ov", "rect"):
            h = h.replace(f'class="{cls} largo">{DOS_LINEAS[0]}', f'class="{cls} largo dos">{DOS_LINEAS[1]}')
        h = h.replace("</style>", CSS_DOS + "</style>", 1)
    for a, b in COMUN + POR_OPCION[op]:
        if a not in h:
            sys.exit(f"x R5 {op}: no encontré «{a[:60]}…» en el HTML de la R4")
        h = h.replace(a, b)
    # Eli 29-09 (imprenta): nada bajo 8 pt — casi todo va calado en beige sobre café y a 7,5 pt la
    # letra fina se tapa con la tinta. La nota en cursiva sube a 8,5 pt. El Título (Brushwell) no se toca.
    h = re.sub(r"font-size:(\d+(?:\.\d+)?)pt", lambda m: f"font-size:{max(float(m.group(1)), 8):g}pt", h)
    h = h.replace(".nt{font-size:8pt;", ".nt{font-size:8.5pt;")
    # Eli 29-09 (jerarquía): la SECCIÓN va unos puntos sobre el plato y más gruesa → título > sección >
    # plato (9,5 Bold) > descripción (8,5 Regular). Si no cabe en la columna, dos líneas; nunca más chica.
    # a 8 pt la leyenda del pie ya no cabe en una línea (se salía de la hoja): dos líneas equilibradas
    h = h.replace("</style>", ".leyenda{white-space:normal!important;text-wrap:balance;line-height:1.5}</style>", 1)
    h = re.sub(r"(\d{2}:\d{2}) (hrs|HRS|Hrs)", lambda m: m.group(1) + "\u00a0" + m.group(2), h)  # «22:00 HRS» nunca se parte
    # la leyenda del pie sólo se corta entre dato y dato (en un «·»), nunca dentro de «Cierre de bar 22:00 hrs»
    h = re.sub(r'(class="leyenda"[^>]*>)(.*?)(</div>)', lambda m: m.group(1) + "\u00a0· ".join(
        t.strip().replace(" ", "\u00a0") for t in m.group(2).split("·")) + m.group(3), h, flags=re.S)
    if op in SECCION:
        h = h.replace("</style>", SECCION[op] + "</style>", 1)
    return h


def main():
    for d in ("html", "png", "pdf"):
        (OUT / d).mkdir(parents=True, exist_ok=True)
    pj = OUT / "paginas.json"
    info = json.loads(pj.read_text(encoding="utf-8")) if pj.exists() else {}
    for k in (sys.argv[1:] or list(r4.OPCIONES)):
        n = f"BW-CARTA-OFICIAL-R5-OP{k}"
        h = OUT / "html" / f"{n}.html"
        h.write_text(html_r5(k), encoding="utf-8")
        dom = subprocess.run(r4.CH + ["--dump-dom", h.as_uri()], capture_output=True, text=True, encoding="utf-8").stdout
        pags = int(re.search(r'data-paginas="(\d+)"', dom).group(1))
        sobra = re.search(r'data-sobra="([^"]*)"', dom).group(1)
        subprocess.run(r4.CH + ["--no-pdf-header-footer", f"--print-to-pdf={OUT / 'pdf' / (n + '.pdf')}", h.as_uri()],
                       check=True, capture_output=True)
        for p in range(1, pags + 1):
            subprocess.run(r4.CH + ["--force-device-scale-factor=3", "--window-size=643,1134",
                                    f"--screenshot={OUT / 'png' / f'{n}-{p}.png'}", h.as_uri() + f"?p={p}"],
                           check=True, capture_output=True)
        info[k] = {"paginas": pags, "sobra": sobra}
        print(("✓" if sobra == "ok" else "⚠"), n, f"{pags} hojas", "" if sobra == "ok" else f"SOBRA: {sobra}")
    pj.write_text(json.dumps(info, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
