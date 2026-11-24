#!/usr/bin/env python3
"""Loading Screen Gold entry.

Writes one loading-screen tip (at most 200 UTF-8 characters)
to /output/entry.txt.
"""

import os


def main() -> None:
    # A loading-screen tip: the bar is not stuck, it is thinking.
    # Do not mash buttons while it loads — use the pause instead:
    # stretch, sip water, plan your first three moves, and start
    # sharper than the player who spent the wait glaring at the bar.
    line = "Tip: the bar isn't stuck, it's thinking. Don't mash buttons — stretch, sip water, and plan your first three moves. You'll start sharper than the player who spent the whole wait glaring at it."
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
