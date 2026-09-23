#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Puente con el Adobe Illustrator que está corriendo en esta máquina.

⭐ QUÉ ES ESTO
Illustrator expone una interfaz **COM** en Windows (`Illustrator.Application`,
verificado registrado en esta máquina) y esa interfaz trae `DoJavaScript`, que
ejecuta **ExtendScript adentro del Illustrator abierto**. O sea: se puede leer
el documento vivo —qué hay, dónde está, qué tiene seleccionado la diseñadora— y
también modificarlo, sin exportar ni reimportar nada.

Es la diferencia entre mandarle un archivo y trabajar los dos sobre el mismo
documento.

⚠️ DOS COSAS QUE HAY QUE SABER DEL COM DE ILLUSTRATOR
1. Si Illustrator NO está abierto, `Dispatch` lo **lanza**. No es un efecto
   secundario escondido: es la única forma de conectarse.
2. Mientras Illustrator está ocupado —abriendo un archivo, con un diálogo
   modal arriba, rasterizando— el COM contesta `RPC_E_CALL_REJECTED` («Call was
   rejected by callee»). No es un error de verdad: es «estoy ocupado, insiste».
   Por eso todo pasa por `_reintentar`.

⛔ REGLA DE TRABAJO: leer se hace sin preguntar; **escribir en el documento de
Eli se avisa antes**. Un `DoJavaScript` que mueve objetos entra al historial de
deshacer de Illustrator, pero ella puede tener trabajo sin guardar arriba.

Uso:
    python scripts/ai-puente.py --estado
    python scripts/ai-puente.py --jsx ruta/al/script.jsx
    python scripts/ai-puente.py --js "app.documents.length"
    python scripts/ai-puente.py --abrir "ruta/al/archivo.svg"
"""
import argparse
import sys
import time
from pathlib import Path

import pythoncom
import win32com.client

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                  # noqa: BLE001
    pass

RAIZ = Path(__file__).resolve().parent.parent
# «Call was rejected by callee» y «The message filter indicated that the
# application is busy» — los dos quieren decir lo mismo: insiste.
OCUPADO = (-2147418111, -2147417846, -2147417851)


def _reintentar(fn, intentos=40, espera=3.0):
    ultimo = None
    for i in range(intentos):
        try:
            return fn()
        except pythoncom.com_error as e:                            # noqa: PERF203
            ultimo = e
            if e.hresult not in OCUPADO and i > 2:
                raise
            time.sleep(espera)
    raise ultimo


def conectar():
    """Se engancha al Illustrator abierto; si no hay ninguno, lo lanza."""
    pythoncom.CoInitialize()
    return _reintentar(lambda: win32com.client.Dispatch("Illustrator.Application"))


def js(ai, codigo: str) -> str:
    """Corre ExtendScript adentro de Illustrator y devuelve lo que retorne.

    ⚠️ ExtendScript devuelve SIEMPRE una cadena por COM. Si quieres estructura,
    ármala tú con separadores; `JSON` no existe en ExtendScript sin cargarlo.
    """
    return _reintentar(lambda: ai.DoJavaScript(codigo))


# El informe de estado: qué documento hay arriba y qué está seleccionado.
ESTADO_JSX = r"""
(function () {
  var L = [];
  L.push('Illustrator ' + app.version);
  L.push('documentos abiertos: ' + app.documents.length);
  if (app.documents.length === 0) { L.push('(no hay ninguno arriba)'); return L.join('\n'); }
  var d = app.activeDocument;
  L.push('');
  L.push('DOCUMENTO  ' + d.name);
  L.push('  ruta       ' + (d.saved ? d.fullName : '(sin guardar)'));
  L.push('  mesa       ' + Math.round(d.width * 100) / 100 + ' x ' + Math.round(d.height * 100) / 100 + ' pt');
  L.push('  mesas      ' + d.artboards.length);
  for (var a = 0; a < d.artboards.length; a++) {
    var r = d.artboards[a].artboardRect;
    L.push('    [' + a + '] ' + d.artboards[a].name + '  ' +
           Math.round((r[2] - r[0]) * 100) / 100 + ' x ' + Math.round((r[1] - r[3]) * 100) / 100);
  }
  L.push('  color      ' + (d.documentColorSpace == DocumentColorSpace.RGB ? 'RGB' : 'CMYK'));
  L.push('  capas      ' + d.layers.length);
  for (var i = 0; i < d.layers.length; i++) {
    L.push('    - ' + d.layers[i].name + '  (' + d.layers[i].pageItems.length + ' objetos)');
  }
  L.push('  textos     ' + d.textFrames.length);
  var faltan = [];
  for (var t = 0; t < d.textFrames.length; t++) {
    try {
      var f = d.textFrames[t].textRange.characterAttributes.textFont;
      var nom = f.name;
      var ok = false;
      for (var k = 0; k < app.textFonts.length; k++) { if (app.textFonts[k].name == nom) { ok = true; break; } }
      if (!ok) faltan.push(nom);
    } catch (e) {}
  }
  L.push('  fuentes que faltan: ' + (faltan.length ? faltan.join(', ') : 'ninguna'));
  L.push('');
  L.push('SELECCION  ' + d.selection.length + ' objeto(s)');
  for (var s = 0; s < Math.min(d.selection.length, 12); s++) {
    var o = d.selection[s];
    var b = o.geometricBounds;
    L.push('  - ' + o.typename + '  "' + (o.name || '') + '"  x ' + Math.round(b[0] * 10) / 10 +
           '  y ' + Math.round(-b[1] * 10) / 10 +
           '  ' + Math.round((b[2] - b[0]) * 10) / 10 + ' x ' + Math.round((b[1] - b[3]) * 10) / 10 +
           (o.typename == 'TextFrame' ? '  texto: «' + o.contents.substr(0, 40) + '»' : ''));
  }
  return L.join('\n');
})();
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--estado", action="store_true",
                    help="qué documento hay arriba, sus capas y la selección")
    ap.add_argument("--jsx", help="archivo .jsx a ejecutar en Illustrator")
    ap.add_argument("--js", help="una línea de ExtendScript")
    ap.add_argument("--abrir", help="abre un archivo en Illustrator")
    a = ap.parse_args()

    ai = conectar()
    if a.abrir:
        ruta = Path(a.abrir).resolve()
        if not ruta.exists():
            print(f"⛔ No existe: {ruta}")
            return 1
        _reintentar(lambda: ai.Open(str(ruta)))
        print(f"✅ abierto: {ruta.name}")
    if a.jsx:
        print(js(ai, Path(a.jsx).read_text(encoding="utf-8")))
    if a.js:
        print(js(ai, a.js))
    if a.estado or not (a.jsx or a.js or a.abrir):
        print(js(ai, ESTADO_JSX))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
