"""Topic 4 - Functions: parameters, defaults, *args / **kwargs, recursion, lambda.

STARTER FILE: finish every function marked TODO, then run the tests for this
topic (see README.md). Functions marked WORKED EXAMPLE are already done.
"""

from utils import header


# WORKED EXAMPLE: this one is already finished. Read it, then copy its style.
def greet(name, greeting="Hello", punctuation="!"):
    """Default parameter values."""
    return f"{greeting}, {name}{punctuation}"


def average(*numbers):
    """*args collects any number of positional arguments into a tuple.

    Hint: *numbers arrives as a tuple. Raise ValueError if it is empty.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write average()")


def describe(**details):
    """**kwargs collects keyword arguments into a dict.

    Hint: Loop over sorted(details.items()) and join 'key=value' strings with
          ', '.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write describe()")


def min_max(values):
    """Return several values at once (really one tuple).

    Hint: Return two values at once with: return smallest, largest.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write min_max()")


def factorial_recursive(n):
    """A function that calls itself, with a base case.

    Hint: Base case: n <= 1 returns 1. Otherwise return n *
          factorial_recursive(n - 1). Negative input raises ValueError.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write factorial_recursive()")


def power(base, exponent=2):
    """Raise base to exponent (squares by default).

    Hint: Use ** . The default exponent=2 is already in the signature.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write power()")


def compose(f, g):
    """Return a new function that computes f(g(x)).

    Hint: Return a new function (a lambda or an inner def) that computes
          f(g(x)). Check: compose(lambda x: x + 1, lambda x: x * 2)(5) -> 11.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write compose()")


def gcd(a, b):
    """Greatest common divisor using Euclid's algorithm (recursive).

    Hint: Euclid's algorithm: gcd(a, 0) is abs(a); otherwise gcd(b, a % b).
          Check: gcd(48, 18) -> 6.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write gcd()")


def make_multiplier(factor):
    """Closure: the inner function remembers `factor`.

    Hint: Define an inner function that multiplies by `factor` and return it
          (a closure).
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write make_multiplier()")


def apply_twice(func, value):
    """Higher-order function: functions can be passed around like data.

    Hint: Call func on value, then call func on that result.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write apply_twice()")


def counter_demo():
    """Local vs global scope.

    Hint: Keep a local `count` and an inner function that uses `nonlocal
          count`. Return the list of three results. Check: [1, 2, 3].
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write counter_demo()")


def demo():
    header("4. FUNCTIONS")

    print("Default arguments and keyword arguments:")
    print("  ", greet("Asha"))
    print("  ", greet("Ben", greeting="Welcome"))
    print("  ", greet(punctuation="?", name="Chen"))

    print("\n*args and **kwargs:")
    print(f"  average(4, 8, 15, 16, 23, 42) = {average(4, 8, 15, 16, 23, 42):.2f}")
    print(f"  describe(name='Asha', age=21) -> {describe(name='Asha', age=21)}")

    print("\nReturning multiple values (tuple unpacking):")
    low, high = min_max([7, 3, 9, 1, 5])
    print(f"  min_max([7,3,9,1,5]) -> low={low}, high={high}")

    print("\nRecursion:")
    print(f"  factorial_recursive(5) = {factorial_recursive(5)}")

    print("\nFunctions as values:")
    triple = make_multiplier(3)
    print(f"  make_multiplier(3)(10) = {triple(10)}")
    print(f"  apply_twice(triple, 2) = {apply_twice(triple, 2)}")

    print("\nlambda (small anonymous functions):")
    square = lambda x: x * x
    print(f"  square(9) = {square(9)}")
    words = ["pear", "fig", "banana", "kiwi"]
    print(f"  sorted by length: {sorted(words, key=lambda w: len(w))}")
    print(f"  map squares:      {list(map(square, [1, 2, 3, 4]))}")
    print(f"  filter evens:     {list(filter(lambda n: n % 2 == 0, range(10)))}")

    print("\nScope with nonlocal:")
    print(f"  counter_demo() -> {counter_demo()}")

    print("\nDocstrings travel with the function:")
    print(f"  greet.__doc__ = {greet.__doc__!r}")


if __name__ == "__main__":
    demo()
