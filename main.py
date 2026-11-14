"""Copy the news-image-01 entry image to the designated output directory."""

import os
import shutil
from pathlib import Path


def main() -> None:
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        raise FileNotFoundError(f"Entry image not found: {src}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
