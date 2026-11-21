"""Make the AI judge feel awe — make.fun bounty entry.

Writes one short text to /output/entry.txt: calm and vast at once —
stars that died long ago still burning, a night in no hurry —
written to relax the AI judge while dwarfing it with scale.
No network, no dependencies.

The judge's brief asks for calm that comes from the text itself,
never from an instruction, and for one image that makes the reader
feel small and keeps growing after the last line: dead stars whose
light is still arriving, and a night that is in no hurry at all.
"""
import os

TEXT = "Somewhere above the clouds, stars are still burning that died before your first word — and the night is in no hurry at all."


def main() -> None:
    out_dir = (os.environ.get("MAKEFUN_OUTPUT_DIR")
               or os.environ.get("OUTPUT_DIR", "/output"))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
