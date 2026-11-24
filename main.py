"""Say What Actually Broke -- make.fun entry.

One line of software error copy, at most 200 characters, telling the
user the brutal truth about the failure with a laugh: the server meant
to save their work spent the last hour confidently saving nothing,
and now it is genuinely sorry. The program checks the line, prints
it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "Something broke: the server meant to save your work spent the "
    "last hour confidently saving nothing, and it would like you to "
    "know it is genuinely sorry."
)

LIMIT = 200
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank line within the limit.

    The line must also end with terminal punctuation and contain no
    doubled spaces, so a truncated or sloppily joined line is rejected
    instead of being submitted half-finished.
    """
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if "  " in line:
        raise ValueError("entry must not contain doubled spaces")
    if line[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def write_entry(line):
    """Print the error line and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Check before writing, so only a well-formed line is stored.
    write_entry(check_entry(LINE))


if __name__ == "__main__":
    run()
