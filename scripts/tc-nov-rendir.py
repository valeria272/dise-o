#!/usr/bin/env python3
"""Tierra Calma · noviembre 2026 — rinde los estáticos y los deja con el nombre de entrega.

    python scripts/tc-nov-rendir.py            # todo
    python scripts/tc-nov-rendir.py E Stories  # sólo esas hojas

Un frame = una pieza (`--sequence`), igual que octubre. Los nombres salen de
`GRUPOS` — el mismo orden que los arrays `NOV_*` de `Noviembre.tsx` y que el mapa
de `qa/textos-tierracalma.py`. Nomenclatura del portal: `c-DD-MM-n`, `p-DD-MM`,
`st-DD-MM`.

Salida: out/tierracalma/nov2026/entrega/
"""
import pathlib
import shutil
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
OUT = RAIZ / "out/tierracalma/nov2026"
CHROME = pathlib.Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

GRUPOS = {
    "E": ("TCNovCarrE", [f"c-09-11-{i}" for i in range(1, 6)]),
    "F": ("TCNovCarrF", [f"c-11-11-{i}" for i in range(1, 8)]),
    "M": ("TCNovCarrM", [f"c-30-11-{i}" for i in range(1, 7)]),
    "Posts": ("TCNovPosts", ["p-17-11", "p-24-11"]),
    "Stories": ("TCNovStories", ["st-13-11", "st-20-11", "st-26-11"]),
}


def main() -> None:
    pedidos = sys.argv[1:] or list(GRUPOS)
    entrega = OUT / "entrega"
    entrega.mkdir(parents=True, exist_ok=True)
    remotion = RAIZ / ("node_modules/.bin/remotion" + (".cmd" if sys.platform == "win32" else ""))
    for g in pedidos:
        comp, ids = GRUPOS[g]
        seq = OUT / "seq" / g
        shutil.rmtree(seq, ignore_errors=True)
        cmd = [str(remotion), "render", comp, str(seq), "--sequence", "--image-format=png", "--log=error"]
        if CHROME.exists():
            cmd.append(f"--browser-executable={CHROME}")
        print(f"rindiendo {comp}…", flush=True)
        r = subprocess.run(cmd, cwd=RAIZ)
        if r.returncode:
            sys.exit(f"✗ falló {comp}")
        frames = sorted(seq.glob("element-*.png"), key=lambda p: int(p.stem.split("-")[1]))
        if len(frames) != len(ids):
            sys.exit(f"✗ {comp}: {len(frames)} frames y se esperaban {len(ids)}")
        for f, pid in zip(frames, ids):
            shutil.copyfile(f, entrega / f"{pid}.png")
            print(f"  ✓ {pid}.png")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
