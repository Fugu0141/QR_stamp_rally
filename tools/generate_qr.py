#!/usr/bin/env python3
"""Generate QR code PNG files for this static stamp rally template.

Usage:
  python tools/generate_qr.py --base-url https://example.github.io/stamp-rally-template/

Dependencies:
  pip install qrcode[pil]
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path
from urllib.parse import quote


def read_stamp_ids(config_path: Path) -> list[str]:
    text = config_path.read_text(encoding="utf-8")
    ids = re.findall(r"\bid\s*:\s*['\"]([^'\"]+)['\"]", text)
    seen: list[str] = []
    for stamp_id in ids:
        if stamp_id not in seen:
            seen.append(stamp_id)
    return seen


def normalize_base_url(base_url: str) -> str:
    return base_url.rstrip("/") + "/"


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate QR codes for stamp-get.html?id=...")
    parser.add_argument("--base-url", required=True, help="Published site URL, for example https://user.github.io/repo/")
    parser.add_argument("--config", default="config.js", help="Path to config.js. Default: config.js")
    parser.add_argument("--out", default="qr-codes", help="Output directory. Default: qr-codes")
    parser.add_argument("--ids", nargs="*", help="Optional stamp IDs. If omitted, IDs are read from config.js.")
    args = parser.parse_args()

    try:
        import qrcode
    except ImportError as exc:
        raise SystemExit("Missing dependency: run `pip install qrcode[pil]` and try again.") from exc

    project_root = Path.cwd()
    config_path = project_root / args.config
    out_dir = project_root / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    stamp_ids = args.ids or read_stamp_ids(config_path)
    if not stamp_ids:
        raise SystemExit("No stamp IDs found. Check config.js or pass --ids manually.")

    base_url = normalize_base_url(args.base_url)
    rows: list[str] = []

    for index, stamp_id in enumerate(stamp_ids, start=1):
        url = f"{base_url}stamp-get.html?id={quote(stamp_id)}"
        filename = f"stamp-{index}-{stamp_id}.png".replace("/", "-")
        filepath = out_dir / filename

        img = qrcode.make(url)
        img.save(filepath)

        rows.append(
            f"""
            <section class=\"qr-card\">
              <img src=\"{html.escape(args.out)}/{html.escape(filename)}\" alt=\"QR code for stamp {html.escape(stamp_id)}\">
              <h2>Stamp {index}</h2>
              <p><code>{html.escape(url)}</code></p>
            </section>
            """
        )
        print(f"Generated: {filepath} -> {url}")

    print_html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
<meta charset=\"UTF-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Stamp Rally QR Codes</title>
<style>
body {{ font-family: system-ui, sans-serif; margin: 24px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; }}
.qr-card {{ border: 1px solid #ddd; border-radius: 16px; padding: 16px; text-align: center; page-break-inside: avoid; }}
img {{ width: 180px; height: 180px; }}
code {{ word-break: break-all; font-size: 12px; }}
@media print {{ body {{ margin: 10mm; }} .qr-card {{ break-inside: avoid; }} }}
</style>
</head>
<body>
<h1>Stamp Rally QR Codes</h1>
<p>Print this page and place each QR code at your event locations.</p>
<div class=\"grid\">
{''.join(rows)}
</div>
</body>
</html>
"""

    (project_root / "qr-print.html").write_text(print_html, encoding="utf-8")
    print("Generated: qr-print.html")


if __name__ == "__main__":
    main()
