"""Topic 2 - Selection statements: if / elif / else, logical operators, membership tests.

STARTER FILE: finish every function marked TODO, then run the tests for this
topic (see README.md). Functions marked WORKED EXAMPLE are already done.
"""

from utils import header


# WORKED EXAMPLE: this one is already finished. Read it, then copy its style.
def grade_letter(score):
    """Convert a 0-100 score to a letter grade (if / elif / else chain)."""
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def is_leap_year(year):
    """Divisible by 4, except centuries, unless divisible by 400.

    Hint: Divisible by 4, but a century year must also be divisible by 400.
          Check: 1900 -> False, 2000 -> True.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write is_leap_year()")


def classify_triangle(a, b, c):
    """Return 'invalid', 'equilateral', 'isosceles' or 'scalene'.

    Hint: Test for 'invalid' first (a side <= 0, or two sides not longer than
          the third). Then count equal sides.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write classify_triangle()")


def bmi_category(bmi_value):
    """Standard adult BMI bands.

    Hint: Use an if / elif chain from the lowest band up: under 18.5, under
          25, under 30, otherwise obese.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write bmi_category()")


def day_type(day):
    """Group a day name using membership tests (`in`).

    Python 3.10 added a `match` statement for this kind of job; it is avoided
    here so the whole project runs on Python 3.9.

    Hint: Normalise with strip().lower(), then test membership with `in`
          against tuples of day names.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write day_type()")


def ticket_price(age):
    """Child (under 13) 5, adult 10, senior (65 and over) 7; negative ages are invalid.

    Hint: Check for a negative age first (raise ValueError). Child (under 13)
          = 5, senior (65 and over) = 7, everyone else = 10.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write ticket_price()")


def fizzbuzz_word(n):
    """The classic: Fizz for 3s, Buzz for 5s, FizzBuzz for both.

    Hint: Test 15 first, then 3, then 5. Otherwise return the number as a
          string.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write fizzbuzz_word()")


def demo():
    header("2. SELECTION: if / elif / else, and / or / not, in")

    print("Letter grades (if / elif / else):")
    for score in (95, 84, 71, 65, 40):
        print(f"  {score:>3} -> {grade_letter(score)}")

    print("\nLeap years (and / or / not):")
    for year in (1900, 2000, 2024, 2026):
        print(f"  {year}: {'leap' if is_leap_year(year) else 'not leap'}")  # ternary

    print("\nTriangles:")
    for sides in ((3, 3, 3), (3, 3, 5), (3, 4, 5), (1, 2, 8)):
        print(f"  {sides}: {classify_triangle(*sides)}")

    print("\nBMI bands:")
    for value in (17.0, 22.9, 27.5, 33.0):
        print(f"  {value}: {bmi_category(value)}")

    print("\nMembership tests with `in`:")
    for day in ("Saturday", "Wednesday", "Funday"):
        print(f"  {day}: {day_type(day)}")

    print("\nTicket prices by age:")
    for age in (8, 13, 40, 70):
        print(f"  age {age:>2}: {ticket_price(age)}")

    print("\nFizzBuzz 1-15:")
    print("  " + " ".join(fizzbuzz_word(n) for n in range(1, 16)))

    print("\nTruthiness: empty things are False")
    for item in ([], [0], "", "0", 0, None):
        print(f"  {item!r:<5} -> {'truthy' if item else 'falsy'}")


if __name__ == "__main__":
    demo()
