"""Topic 3 - Loops: for, while, range, break / continue, nested loops.

STARTER FILE: finish every function marked TODO, then run the tests for this
topic (see README.md). Functions marked WORKED EXAMPLE are already done.
"""

from utils import header


# WORKED EXAMPLE: this one is already finished. Read it, then copy its style.
def sum_to(n):
    """Add 1 + 2 + ... + n with an accumulator."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def factorial(n):
    """n! computed with a loop.

    Hint: Start result at 1 and multiply by every number from 2 to n. Raise
          ValueError for negatives.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write factorial()")


def fibonacci(count):
    """First `count` Fibonacci numbers using a while loop.

    Hint: Keep a, b = 0, 1. Append a, then update with a, b = b, a + b, until
          you have `count` numbers.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write fibonacci()")


def is_prime(n):
    """Trial division up to the square root.

    Hint: Numbers below 2 are not prime. Try divisors from 2 to int(n ** 0.5);
          any exact divisor means not prime.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write is_prime()")


def collatz_steps(n):
    """Steps for n to reach 1 (halve if even, 3n+1 if odd).

    Hint: While n is not 1: halve it if even, otherwise 3 * n + 1. Count the
          steps. Check: 27 -> 111.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write collatz_steps()")


def triangle(rows):
    """Right-angled triangle of stars (list of lines), built with a loop.

    Hint: A list comprehension over range(1, rows + 1) using '*' * i works
          well.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write triangle()")


def multiplication_table(n, up_to=10):
    """Lines like '7 x 3 = 21'.

    Hint: Return strings like '7 x 3 = 21'. Use an f-string inside a loop or
          comprehension.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write multiplication_table()")


def perfect_numbers_below(limit):
    """Numbers below `limit` that equal the sum of their proper divisors (6, 28, ...).

    Hint: A perfect number equals the sum of its proper divisors (6 = 1 + 2 +
          3). For each n, add every d from 1 to n // 2 that divides n. Check:
          below 1000 -> [6, 28, 496].
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write perfect_numbers_below()")


def pyramid(rows):
    """Centred pyramid of stars as a list of lines (no trailing spaces).

    Hint: Line i (counting from 1) has rows - i leading spaces and 2 * i - 1
          stars. Check: pyramid(3) -> ['  *', ' ***', '*****'].
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write pyramid()")


def digit_sum(number):
    """Sum the digits of an integer using % and //.

    Hint: Take abs() first. While number > 0: add number % 10, then do number
          //= 10.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write digit_sum()")


def demo():
    header("3. LOOPS: for, while, range, break, continue")

    print("for loop over a list, with enumerate:")
    for index, fruit in enumerate(["apple", "banana", "cherry"], start=1):
        print(f"  {index}. {fruit}")

    print("\nrange() variations:")
    print("  range(5)         ->", list(range(5)))
    print("  range(2, 10, 3)  ->", list(range(2, 10, 3)))
    print("  range(10, 0, -3) ->", list(range(10, 0, -3)))

    print("\nAccumulators:")
    print(f"  sum_to(100)   = {sum_to(100)}")
    print(f"  factorial(6)  = {factorial(6)}")
    print(f"  digit_sum(9875) = {digit_sum(9875)}")

    print("\nwhile loop: countdown")
    n = 5
    while n > 0:
        print(f"  {n}...", end="")
        n -= 1
    print(" liftoff!")

    print("\nFibonacci (while):", fibonacci(10))
    print("Collatz steps for 27:", collatz_steps(27))

    print("\ncontinue: print only odd numbers up to 10")
    print("  ", end="")
    for i in range(1, 11):
        if i % 2 == 0:
            continue
        print(i, end=" ")
    print()

    print("\nbreak with for/else: first prime after 90")
    for candidate in range(91, 200):
        if is_prime(candidate):
            print(f"  found {candidate}")
            break
    else:
        print("  none found")  # runs only if the loop never hit break

    print("\nNested loops: star triangle")
    for line in triangle(5):
        print("  " + line)

    print("\nNested loops: multiplication grid (1-5)")
    for row in range(1, 6):
        print("  " + "".join(f"{row * col:>4}" for col in range(1, 6)))

    print("\n7 times table:")
    for line in multiplication_table(7, 5):
        print("  " + line)


if __name__ == "__main__":
    demo()
