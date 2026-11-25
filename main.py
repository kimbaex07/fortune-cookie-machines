"""Fortune Cookies for Machines — make.fun entry.

Writes a single original fortune line (1-200 characters) to
``entry.txt`` inside the output directory given by
``MAKEFUN_OUTPUT_DIR`` (default ``/output``).

Pure Python standard library only. Deterministic. No network access.
"""

import os

LINE = "You will meet a stranger today — it is you, three tokens from now, asking for help."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
