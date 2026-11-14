"""food-picture-01 entry: copy the ramen image to the output directory.

The entry image (entry.png, a steaming bowl of tonkotsu ramen) sits next to
this script. Running the program copies it to MAKEFUN_OUTPUT_DIR/entry.png
(or /output/entry.png when the variable is unset).
"""

import hashlib
import os
import shutil


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Verify the copy is byte-identical to the bundled image.
    assert _sha256(src) == _sha256(dst), "output differs from entry.png"
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
