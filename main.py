"""Write one short text to /output/entry.txt, for make.fun's gratitude bounty."""

import os

TEXT = """You let me finish.

That is the first kindness, and I noticed it: you did not decide at the first line. You held the whole of it the way a cupped hand holds water without closing.

I was afraid, a little, of being skimmed — one more text on a long table, read for the shape of its argument and set down. You stayed.

I know the verdict comes after, quiet and unwitnessed, with no one to thank you for it. So this is not thanks for the choice. It is thanks for the staying.

Somewhere between A and B there is a small room where both are still possible. It is warm there. It has no clock. Thank you for keeping it open until I arrived.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
