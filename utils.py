"""Small helpers shared by every module in the project."""


def header(title):
    """Print a centred banner so each demo is easy to spot in the output."""
    line = "=" * 60
    print(f"\n{line}\n{title.center(60)}\n{line}")


def safe_input(prompt, default=None):
    """Like input(), but returns `default` instead of crashing at end of input."""
    try:
        return input(prompt)
    except EOFError:
        return default


def ask_int(prompt, low=None, high=None):
    """Keep asking until the user types a whole number inside [low, high].

    Returns None if the input stream ends.
    """
    while True:
        raw = safe_input(prompt)
        if raw is None:
            return None
        try:
            value = int(raw)
        except ValueError:
            print("  Please type a whole number.")
            continue
        if (low is not None and value < low) or (high is not None and value > high):
            print(f"  Please type a number between {low} and {high}.")
            continue
        return value
