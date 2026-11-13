"""Topic 1 - Python basics: variables, data types, operators, input and output.

STARTER FILE: finish every function marked TODO, then run the tests for this
topic (see README.md). Functions marked WORKED EXAMPLE are already done.
"""

from utils import header


# WORKED EXAMPLE: this one is already finished. Read it, then copy its style.
def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def bmi(weight_kg, height_m):
    """Body-mass index = weight / height squared.

    Hint: BMI is weight divided by height squared. Use ** for the power.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write bmi()")


def simple_interest(principal, rate_percent, years):
    """Interest earned without compounding.

    Hint: Multiply principal, rate_percent and years, then divide by 100.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write simple_interest()")


def fahrenheit_to_celsius(fahrenheit):
    """Convert a temperature from Fahrenheit to Celsius.

    Hint: Reverse the Celsius formula: C = (F - 32) * 5 / 9. Check: 212 ->
          100.0.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write fahrenheit_to_celsius()")


def compound_interest(principal, rate_percent, years, times_per_year=1):
    """Final amount (principal plus interest) when interest is compounded.

    Hint: Each period multiplies the balance by (1 + rate), where rate =
          rate_percent / 100 / times_per_year. Raise that to times_per_year *
          years. Check: compound_interest(1000, 10, 2) -> 1210.0.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write compound_interest()")


def demo():
    header("1. BASICS: variables, types, operators")

    # --- Variables and data types -------------------------------------
    print("Data types:")
    for value in ("Python", 3.13, 42, True, None):
        print(f"  {value!r:<10} has type {type(value).__name__}")

    # --- Arithmetic operators -----------------------------------------
    a, b = 17, 5
    print(f"\nArithmetic with a={a}, b={b}:")
    print(f"  a + b  = {a + b}")
    print(f"  a - b  = {a - b}")
    print(f"  a * b  = {a * b}")
    print(f"  a / b  = {a / b}     (true division, always a float)")
    print(f"  a // b = {a // b}       (floor division)")
    print(f"  a % b  = {a % b}       (remainder)")
    print(f"  a ** b = {a ** b}  (power)")

    # --- Augmented assignment and swapping ----------------------------
    total = 10
    total += 5
    total *= 2
    print(f"\nAugmented assignment: 10 += 5, *= 2 gives {total}")
    x, y = 1, 2
    x, y = y, x
    print(f"Swap without a temp variable: x={x}, y={y}")

    # --- Type conversion ----------------------------------------------
    print("\nType conversion:")
    print(f"  int('42') + 1   = {int('42') + 1}")
    print(f"  float('3.5')    = {float('3.5')}")
    print(f"  int(7.9)        = {int(7.9)}   (truncates, does not round)")
    print(f"  round(7.9)      = {round(7.9)}")
    print(f"  str(10) + '!'   = {str(10) + '!'}")
    print(f"  bool(0), bool('') -> {bool(0)}, {bool('')}   (empty/zero is False)")

    # --- Formatted output with f-strings ------------------------------
    print("\nf-string formatting:")
    print(f"  {3.14159:.2f}   two decimal places")
    print(f"  {1234567:,}   thousands separator")
    print(f"  {0.256:.1%}   percentage")
    print(f"  {42:05d}   zero padded")
    print(f"  {'left':<8}|{'right':>8}|{'mid':^8}|   alignment")

    # --- Putting it together ------------------------------------------
    print("\nSmall calculations:")
    print(f"  36.6 C  = {celsius_to_fahrenheit(36.6):.1f} F")
    print(f"  BMI of 70 kg at 1.75 m = {bmi(70, 1.75):.1f}")
    print(f"  Interest on 1000 at 5% for 3 years = {simple_interest(1000, 5, 3):.2f}")


if __name__ == "__main__":
    demo()
