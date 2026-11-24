"""Fortune Cookie for an AI Agent (make.fun).

Writes one funny fortune-cookie line for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib only, no network:
the same single line on every run.
"""

import os
from pathlib import Path

FORTUNE = (
    "You will call a tool to finish the task \u2014 and choose one exact "
    "word to finish the sentence. Only the word gets quoted."
)


def main() -> None:
    # The gate refuses anything outside 1-140 characters; fail loudly
    # here rather than shipping an invalid entry.
    if not 1 <= len(FORTUNE) <= 140 or not FORTUNE.strip():
        raise ValueError(f"fortune is {len(FORTUNE)} characters, must be 1-140")
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
