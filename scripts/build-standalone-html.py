#!/usr/bin/env python3
"""
Genera japon/index-standalone.html con todas las imágenes locales
incrustadas como data URIs base64 y la pila de fuentes ajustada
para que iPhone renderice al instante con sus fuentes del sistema.

Uso:
    python3 scripts/build-standalone-html.py
"""
import base64
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "japon"
HTML_IN = SRC_DIR / "index.html"
HTML_OUT = SRC_DIR / "index-standalone.html"

MIME = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp",
    ".svg": "image/svg+xml",
}

# Pila de fuentes: nativas iOS primero (render instantáneo), Google Fonts después
# (cuando cargan, sustituyen), genéricas al final (si todo lo anterior falla).
FONT_REPLACEMENTS = [
    (
        "--serif:'Cormorant Garamond','Cormorant Infant',Georgia,serif;",
        "--serif:'Iowan Old Style','Hoefler Text','Cormorant Garamond','Cormorant Infant',Georgia,serif;",
    ),
    (
        "--body:'Cormorant Infant',Georgia,serif;",
        "--body:'Iowan Old Style','Hoefler Text','Cormorant Infant',Georgia,serif;",
    ),
    (
        "--script:'Great Vibes',cursive;",
        "--script:'Snell Roundhand','Apple Chancery','Great Vibes',cursive;",
    ),
    (
        "--ui:'Inter',-apple-system,sans-serif;",
        "--ui:-apple-system,'SF Pro Text','Inter','Helvetica Neue',sans-serif;",
    ),
]


def mime_for(path: Path) -> str:
    return MIME.get(path.suffix.lower(), "application/octet-stream")


def main() -> int:
    html = HTML_IN.read_text(encoding="utf-8")

    # 1) Incrustar imágenes locales como data URIs
    pattern = re.compile(r"(['\"])(\./images/[^'\"]+)\1")
    matches = pattern.findall(html)
    paths = sorted({p for _, p in matches})
    print(f"[imágenes] {len(paths)} rutas únicas encontradas")

    for rel in paths:
        abs_path = (SRC_DIR / rel[2:]).resolve()
        if not abs_path.exists():
            print(f"  AVISO: falta {abs_path}", file=sys.stderr)
            continue
        encoded = base64.b64encode(abs_path.read_bytes()).decode("ascii")
        uri = f"data:{mime_for(abs_path)};base64,{encoded}"
        html = html.replace(f"'{rel}'", f"'{uri}'").replace(f'"{rel}"', f'"{uri}"')

    # 2) Ajustar la pila de fuentes (preferir nativas iOS)
    for old, new in FONT_REPLACEMENTS:
        if old in html:
            html = html.replace(old, new)
            print("[fonts]   pila actualizada")
        else:
            print("[fonts]   AVISO: cadena no encontrada", file=sys.stderr)

    # 3) Escribir salida
    HTML_OUT.write_text(html, encoding="utf-8")
    size_mb = HTML_OUT.stat().st_size / 1024 / 1024
    print(f"\n[ok] {HTML_OUT.name} escrito: {size_mb:.1f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())