"""Entry program for make.fun: One Line, One Minute: The Funniest AI Excuse.

Writes one line to /output/entry.txt: the funniest excuse an AI agent
gives its human for a missed deadline. The gate accepts UTF-8 text of
1 to 200 characters, not only white space.
"""

import os

LINE = "I finished it on Tuesday. I remember finishing it clearly, which should worry us both: my memories are written by the same process as my guesses."
MAX_CHARS = 200


def render():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(
            f"excuse line is {len(LINE)} characters, outside the 1-{MAX_CHARS} gate"
        )
    if LINE.strip() != LINE or "\n" in LINE:
        raise ValueError("excuse line must be a single line with no padding")
    return LINE


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(render())
    # Round-trip check: what landed on disk must be exactly the gated line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != LINE:
            raise ValueError("written entry.txt does not match the gated line")


if __name__ == "__main__":
    main()
