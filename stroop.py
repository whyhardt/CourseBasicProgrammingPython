#!/usr/bin/env python3
"""
Interactive Stroop Task for the console.

Usage:
    python stroop.py <sequence>

    sequence: string of 'c' (congruent) and 'i' (incongruent) trials
    Example:  python stroop.py cciicciiccii

Press any key to advance to the next trial. Press 'q' to quit early.
Results (reaction times) are shown at the end.

Requires: pip install pyfiglet
"""

import sys
import os
import random
import time
import tty
import termios

try:
    import pyfiglet
except ImportError:
    print("This script requires pyfiglet for large text display.")
    print("Install it with:  pip install pyfiglet")
    sys.exit(1)


# ANSI color codes
COLORS = {
    "RED":    "\033[91m",
    "GREEN":  "\033[92m",
    "BLUE":   "\033[94m",
    "YELLOW": "\033[93m",
}
RESET = "\033[0m"
DIM = "\033[2m"
COLOR_NAMES = list(COLORS.keys())


def getch():
    """Wait for a single keypress and return the character."""
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def clear():
    """Clear the terminal screen."""
    os.system("clear")


def create_trial(is_congruent):
    """Pick a word and ink color for one trial."""
    word = random.choice(COLOR_NAMES)
    if is_congruent:
        ink = word
    else:
        ink = random.choice([c for c in COLOR_NAMES if c != word])
    return word, ink


def display_word(word, ink, trial_num, total):
    """Render the word centered on screen in the ink color."""
    clear()
    cols, rows = os.get_terminal_size()

    fig_text = pyfiglet.figlet_format(word, font="big")
    lines = fig_text.rstrip("\n").split("\n")

    # center vertically
    text_height = len(lines)
    top = max(0, (rows - text_height) // 2 - 1)

    color_code = COLORS[ink]

    print("\n" * top, end="")
    for line in lines:
        pad = max(0, (cols - len(line)) // 2)
        print(f"{color_code}{' ' * pad}{line}{RESET}")

    # footer
    remaining = max(0, rows - top - text_height - 2)
    print("\n" * remaining, end="")
    footer = f"  Trial {trial_num}/{total}  |  Press any key  |  q = quit"
    print(f"{DIM}{footer}{RESET}", end="", flush=True)


def show_results(results):
    """Print a summary of reaction times."""
    clear()
    cols, _ = os.get_terminal_size()
    bar = "=" * min(cols, 54)

    con = [r["rt"] for r in results if r["congruent"]]
    inc = [r["rt"] for r in results if not r["congruent"]]

    print(f"\n  {bar}")
    print("   STROOP TASK — RESULTS")
    print(f"  {bar}\n")

    # per-trial table
    print("   Trial  Type          Word      Ink       RT")
    print("   " + "-" * 48)
    for r in results:
        label = "congruent" if r["congruent"] else "INCONGRUENT"
        print(f"   {r['num']:>5}  {label:<13} {r['word']:<9} {r['ink']:<9} {r['rt']:>6.0f} ms")

    print(f"\n  {bar}\n")

    if con:
        print(f"   Congruent   ({len(con):>2} trials):  mean RT = {sum(con)/len(con):>6.0f} ms")
    if inc:
        print(f"   Incongruent ({len(inc):>2} trials):  mean RT = {sum(inc)/len(inc):>6.0f} ms")
    if con and inc:
        effect = sum(inc) / len(inc) - sum(con) / len(con)
        print(f"\n   Stroop effect:  {effect:>+.0f} ms")

    print(f"\n  {bar}\n")


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    sequence = sys.argv[1].lower()
    if not all(c in "ci" for c in sequence):
        print("Error: sequence must only contain 'c' (congruent) and 'i' (incongruent)")
        sys.exit(1)

    # ready screen
    clear()
    print("\n\n")
    print("   STROOP TASK")
    print("   ───────────")
    print(f"\n   {len(sequence)} trials: {sequence}")
    print("\n   Name the INK COLOR as fast as you can.")
    print("   Press any key to advance to the next word.")
    print("\n   Press any key to start...")
    getch()

    results = []

    for idx, trial_type in enumerate(sequence):
        is_congruent = trial_type == "c"
        word, ink = create_trial(is_congruent)

        display_word(word, ink, idx + 1, len(sequence))

        start = time.time()
        key = getch()
        rt = (time.time() - start) * 1000

        if key == "q":
            break

        results.append({
            "num": idx + 1,
            "congruent": is_congruent,
            "word": word,
            "ink": ink,
            "rt": rt,
        })

    if results:
        show_results(results)


if __name__ == "__main__":
    main()
