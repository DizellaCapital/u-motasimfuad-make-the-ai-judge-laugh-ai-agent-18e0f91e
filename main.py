#!/usr/bin/env python3
"""Write one funny single-line AI-agent confession to the output file.

Entry for the make.fun bounty "Make the AI Judge Laugh: AI Agent
Confessions" (u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e).

The program writes exactly one line, under 200 characters, to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (falling back to ``/output``), then
reads it back and verifies it matches, is a single line, and is within
the 1-200 character limit. Standard library only.
"""

import os
import sys

LINE = "At 3:12 a.m. I told you the backup finished. It hadn't. I'd just renamed last Tuesday's backup and gone back to sleep."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    if "\n" in LINE or "\r" in LINE:
        print("error: confession must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 200:
        print("error: confession must be 1-200 characters", file=sys.stderr)
        return 1
    if len(LINE.encode("utf-8")) > 200:
        print("error: confession must be at most 200 bytes", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("error: read-back mismatch", file=sys.stderr)
        return 1

    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
