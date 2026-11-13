"""Python Basics Lab (STARTER) - run every topic demo from one menu.

Usage:
    python main.py          interactive menu
    python main.py --all    run every demo straight through

While you are still writing the TODO functions, a demo stops at the first
unfinished function and tells you which one it is. As you finish functions,
more of each demo comes to life.
"""

import sys

import basics
import functions
import gradebook
import lists_demo
import loops
import matrix
import selection
import strings_demo
from utils import safe_input

MENU = [
    ("Basics", basics.demo),
    ("Selection statements", selection.demo),
    ("Loops", loops.demo),
    ("Functions", functions.demo),
    ("Lists", lists_demo.demo),
    ("Strings", strings_demo.demo),
    ("Multidimensional lists", matrix.demo),
    ("Capstone: Gradebook report", gradebook.demo),
]


def run_demo(title, demo):
    """Run one demo; if it reaches an unfinished function, explain instead of crashing."""
    try:
        demo()
    except NotImplementedError as error:
        print(f"\n[Not finished yet] {title}: {error}")
        print("Open the file, finish that function, and run this again.")


def run_all():
    for title, demo in MENU:
        run_demo(title, demo)


def print_menu():
    print("\n" + "=" * 40)
    print("   PYTHON BASICS LAB (STARTER)")
    print("=" * 40)
    for number, (title, _) in enumerate(MENU, start=1):
        print(f"  {number}. {title}")
    print("  a. Run everything")
    print("  g. Interactive gradebook")
    print("  0. Quit")


def main(argv):
    if "--all" in argv:
        run_all()
        return

    while True:
        print_menu()
        choice = (safe_input("Choose: ", "0") or "0").strip().lower()
        if choice in ("0", "q"):
            print("Happy coding!")
            break
        elif choice == "a":
            run_all()
        elif choice == "g":
            run_demo("Interactive gradebook", gradebook.interactive)
        elif choice.isdigit() and 1 <= int(choice) <= len(MENU):
            title, demo = MENU[int(choice) - 1]
            run_demo(title, demo)
        else:
            print("  Please pick a number from the menu.")


if __name__ == "__main__":
    main(sys.argv[1:])
