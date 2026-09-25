# Responde y resuelve en Drive los comentarios de la ronda 1 ya aplicados (25-09-2026).
import sys, os, importlib.util
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
spec = importlib.util.spec_from_file_location("dc", os.path.join(R, "scripts", "drive-comentarios.py"))
dc = importlib.util.module_from_spec(spec); spec.loader.exec_module(dc)
from googleapiclient.discovery import build
d = build("drive", "v3", credentials=dc.creds())
RESP = {  # (fileId, prefijo del comentario) -> respuesta
 ("1YBrrXEf4dUhG_bMpZlUtuGaRLo3HUo0l", "bajemosle"): "Listo: la frase bajó de 112 a 90 pt.",
 ("1YBrrXEf4dUhG_bMpZlUtuGaRLo3HUo0l", "la ropa"): "Listo: imagen nueva con ropa formal de oficina (camisa y pantalón de vestir).",
 ("1B845SvlLB_X_f-3qS-XOBWKH8xQmpYf2", "dejemos este bloque"): "Listo: el bloque subió y quedó un 20 % más chico.",
 ("1p3rPInThnMqGWnOlkGr3XOSTJw7V8JOR", "cierre perfecto"): "¡Gracias! Quedó congelado tal cual.",
 ("1ZjnisFJn6ZxqXOECaAyOhAUVf2xrzzkR", "la palabra camion"): "Listo: «camión» pasó a la segunda línea.",
 ("1AxyBR7ZjaOpa6--2PTsp5QGsAB6nTxJA", "dejemos este bloque"): "Listo: el bloque va arriba y la bajada quedó abajo, un poco más arriba que antes.",
 ("1z7_zN5KNwnL2bwnJtiI3hkjmFPeWEY3M", "dejemos este texto"): "Listo: el texto pasó a la zona del cielo despejado.",
 ("1ztiFAmYSecZeEIIv54Id2xBl_EkY2a3-", "dejemos la frase"): "Listo: «Orden, coordinación y compromiso» en Bold sin caja arriba, y «en cada despacho.» en la segunda línea con caja roja y Bold.",
 ("1bdasdQV0G3zG2KGIjvmn6C-DLHql1ft5", "la ropa"): "Listo: imagen nueva con el vendedor en camisa y pantalón de vestir.",
 ("1bdasdQV0G3zG2KGIjvmn6C-DLHql1ft5", "dejemos este bloque"): "Listo: el bloque pasó a la zona de arriba.",
 ("1Cg09JO8xJgDCH65IuD3OwyPR6PDjmvuP", "ordenar este texto"): "Listo: quedó en 3 líneas.",
 ("14D2wtDEIh_bzMRGuTeJJ7Ih0hvIUE1-s", "eliminar esta zona"): "Listo: borré la bodega de la derecha; ahora es terreno baldío y la obra se lee como una casa aparte.",
 ("1qjaR1ZOMdLtrY2qwvqAG3YXJBpukGyQf", "muy buena"): "¡Gracias! Quedó congelada tal cual.",
}
solo = sys.argv[1:]
for (fid, pref), txt in RESP.items():
    if solo and fid not in solo: continue
    for c in d.comments().list(fileId=fid, fields="comments(id,content,resolved)", includeDeleted=False).execute()["comments"]:
        if not c.get("resolved") and c["content"].lower().startswith(pref):
            d.replies().create(fileId=fid, commentId=c["id"], fields="id", body={"content": txt, "action": "resolve"}).execute()
            print("✓", fid[:8], pref)
