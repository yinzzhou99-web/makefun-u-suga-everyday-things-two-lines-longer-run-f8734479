import os
from pathlib import Path

TEXT = (
    "A toaster is a little sun trapped in a metal box, browning your bread "
    "the way summer browns your shoulders at the beach.\n"
    "The heat is what fits: it turns pale things golden on both sides, "
    "but a real sun never pops up, never burns just one side, and never "
    "runs on a timer."
)


def main():
    out = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


main()
