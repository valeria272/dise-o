"""Una sola vez (21-08-2026): mueve todo lo que la agencia subió a la raíz de
SEPTIEMBRE a la subcarpeta «APRENDIZAJE IA — NO PUBLICAR». Septiembre se
publica con las piezas de Carlos; las nuestras son aprendizaje."""
import sys, importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("sync", Path(__file__).with_name("tc-drive-sync.py"))
sync = importlib.util.module_from_spec(spec); spec.loader.exec_module(sync)

d = sync.svc()
raiz = sync.raiz_aprendizaje(d)
print(f"Destino: {sync.RAIZ_NOMBRE}  ({raiz})")
for f in sync.hijos(d, sync.SEPTIEMBRE):
    if f["id"] == raiz:
        continue
    d.files().update(fileId=f["id"], addParents=raiz, removeParents=sync.SEPTIEMBRE,
                     fields="id,parents", supportsAllDrives=True).execute()
    print(f"  movido  {f['name']}")
print("\nQueda en la raíz (visible para la app):")
for f in sync.hijos(d, sync.SEPTIEMBRE):
    print("  ", f["name"])
print(f"\nhttps://drive.google.com/drive/folders/{raiz}")
