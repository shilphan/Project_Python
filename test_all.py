"""Unit tests for every module. Run from the project folder with:

    python -m unittest discover tests -v
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import basics
import functions
import gradebook
import lists_demo
import loops
import matrix
import selection
import strings_demo


class BasicsTests(unittest.TestCase):
    def test_temperature(self):
        self.assertAlmostEqual(basics.celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(basics.celsius_to_fahrenheit(-40), -40)

    def test_bmi_and_interest(self):
        self.assertAlmostEqual(basics.bmi(70, 1.75), 22.857, places=3)
        self.assertAlmostEqual(basics.simple_interest(1000, 5, 3), 150)

    def test_exercise_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(basics.fahrenheit_to_celsius(212), 100)
        self.assertAlmostEqual(basics.fahrenheit_to_celsius(-40), -40)

    def test_exercise_compound_interest(self):
        self.assertAlmostEqual(basics.compound_interest(1000, 10, 2), 1210)
        self.assertAlmostEqual(basics.compound_interest(1000, 12, 1, 12), 1126.825, places=3)


class SelectionTests(unittest.TestCase):
    def test_grade_letters(self):
        cases = {100: "A", 90: "A", 89: "B", 80: "B", 70: "C", 60: "D", 59: "F", 0: "F"}
        for score, letter in cases.items():
            self.assertEqual(selection.grade_letter(score), letter)

    def test_grade_rejects_out_of_range(self):
        with self.assertRaises(ValueError):
            selection.grade_letter(101)
        with self.assertRaises(ValueError):
            selection.grade_letter(-1)

    def test_leap_year(self):
        self.assertTrue(selection.is_leap_year(2000))
        self.assertTrue(selection.is_leap_year(2024))
        self.assertFalse(selection.is_leap_year(1900))
        self.assertFalse(selection.is_leap_year(2026))

    def test_triangle(self):
        self.assertEqual(selection.classify_triangle(3, 3, 3), "equilateral")
        self.assertEqual(selection.classify_triangle(3, 3, 5), "isosceles")
        self.assertEqual(selection.classify_triangle(3, 4, 5), "scalene")
        self.assertEqual(selection.classify_triangle(1, 2, 8), "invalid")
        self.assertEqual(selection.classify_triangle(0, 4, 5), "invalid")

    def test_bmi_category_and_day_type(self):
        self.assertEqual(selection.bmi_category(18.4), "underweight")
        self.assertEqual(selection.bmi_category(18.5), "normal")
        self.assertEqual(selection.bmi_category(25), "overweight")
        self.assertEqual(selection.bmi_category(30), "obese")
        self.assertEqual(selection.day_type("Sunday"), "weekend")
        self.assertEqual(selection.day_type(" friday "), "weekday")
        self.assertEqual(selection.day_type("Funday"), "unknown")

    def test_fizzbuzz(self):
        words = [selection.fizzbuzz_word(n) for n in (1, 3, 5, 15, 7)]
        self.assertEqual(words, ["1", "Fizz", "Buzz", "FizzBuzz", "7"])

    def test_exercise_ticket_price_boundaries(self):
        cases = {0: 5, 12: 5, 13: 10, 64: 10, 65: 7, 90: 7}
        for age, price in cases.items():
            self.assertEqual(selection.ticket_price(age), price)
        with self.assertRaises(ValueError):
            selection.ticket_price(-1)


class LoopTests(unittest.TestCase):
    def test_sum_and_factorial(self):
        self.assertEqual(loops.sum_to(100), 5050)
        self.assertEqual(loops.sum_to(0), 0)
        self.assertEqual(loops.factorial(0), 1)
        self.assertEqual(loops.factorial(6), 720)
        with self.assertRaises(ValueError):
            loops.factorial(-1)

    def test_fibonacci(self):
        self.assertEqual(loops.fibonacci(0), [])
        self.assertEqual(loops.fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_primes(self):
        primes = [n for n in range(30) if loops.is_prime(n)]
        self.assertEqual(primes, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_collatz_and_digits(self):
        self.assertEqual(loops.collatz_steps(1), 0)
        self.assertEqual(loops.collatz_steps(27), 111)
        self.assertEqual(loops.digit_sum(9875), 29)
        self.assertEqual(loops.digit_sum(-123), 6)

    def test_triangle_and_table(self):
        self.assertEqual(loops.triangle(3), ["*", "**", "***"])
        self.assertEqual(loops.multiplication_table(7, 2), ["7 x 1 = 7", "7 x 2 = 14"])

    def test_exercise_perfect_numbers(self):
        self.assertEqual(loops.perfect_numbers_below(1000), [6, 28, 496])
        self.assertEqual(loops.perfect_numbers_below(6), [])

    def test_exercise_pyramid(self):
        self.assertEqual(loops.pyramid(3), ["  *", " ***", "*****"])
        self.assertEqual(loops.pyramid(1), ["*"])


class FunctionTests(unittest.TestCase):
    def test_greet_defaults(self):
        self.assertEqual(functions.greet("Asha"), "Hello, Asha!")
        self.assertEqual(functions.greet("Ben", greeting="Hi", punctuation="?"), "Hi, Ben?")

    def test_args_kwargs(self):
        self.assertEqual(functions.average(2, 4, 6), 4)
        with self.assertRaises(ValueError):
            functions.average()
        self.assertEqual(functions.describe(b=2, a=1), "a=1, b=2")

    def test_misc(self):
        self.assertEqual(functions.min_max([7, 3, 9]), (3, 9))
        self.assertEqual(functions.factorial_recursive(5), 120)
        self.assertEqual(functions.power(3), 9)
        self.assertEqual(functions.make_multiplier(4)(5), 20)
        self.assertEqual(functions.apply_twice(lambda x: x + 3, 1), 7)
        self.assertEqual(functions.counter_demo(), [1, 2, 3])

    def test_exercise_compose(self):
        add_one_after_double = functions.compose(lambda x: x + 1, lambda x: x * 2)
        self.assertEqual(add_one_after_double(5), 11)

    def test_exercise_gcd(self):
        self.assertEqual(functions.gcd(48, 18), 6)
        self.assertEqual(functions.gcd(7, 13), 1)
        self.assertEqual(functions.gcd(7, 0), 7)


class ListTests(unittest.TestCase):
    def test_remove_duplicates_keeps_order(self):
        self.assertEqual(lists_demo.remove_duplicates([3, 1, 3, 2, 1]), [3, 1, 2])

    def test_second_largest(self):
        self.assertEqual(lists_demo.second_largest([4, 1, 9, 9, 3]), 4)
        self.assertIsNone(lists_demo.second_largest([5, 5]))
        self.assertIsNone(lists_demo.second_largest([]))

    def test_rotate(self):
        self.assertEqual(lists_demo.rotate_left([1, 2, 3, 4], 1), [2, 3, 4, 1])
        self.assertEqual(lists_demo.rotate_left([1, 2, 3, 4], 6), [3, 4, 1, 2])
        self.assertEqual(lists_demo.rotate_left([], 3), [])

    def test_totals_frequency_chunks(self):
        self.assertEqual(lists_demo.running_total([1, 2, 3]), [1, 3, 6])
        self.assertEqual(lists_demo.frequency("aab"), {"a": 2, "b": 1})
        self.assertEqual(lists_demo.chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_bubble_sort_does_not_mutate(self):
        original = [5, 2, 9, 1]
        self.assertEqual(lists_demo.bubble_sort(original), [1, 2, 5, 9])
        self.assertEqual(original, [5, 2, 9, 1])
        self.assertEqual(lists_demo.bubble_sort([]), [])

    def test_exercise_merge_sorted(self):
        self.assertEqual(lists_demo.merge_sorted([1, 4, 9], [2, 3, 10]), [1, 2, 3, 4, 9, 10])
        self.assertEqual(lists_demo.merge_sorted([], [1, 2]), [1, 2])
        self.assertEqual(lists_demo.merge_sorted([5], []), [5])
        self.assertEqual(lists_demo.merge_sorted([1, 1], [1]), [1, 1, 1])


class StringTests(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(strings_demo.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(strings_demo.is_palindrome("Python"))
        self.assertTrue(strings_demo.is_palindrome(""))

    def test_vowels_and_words(self):
        self.assertEqual(strings_demo.count_vowels("Programming"), 3)
        self.assertEqual(strings_demo.reverse_words("one two  three"), "three two one")

    def test_caesar_round_trip(self):
        encoded = strings_demo.caesar("Hello, World!", 3)
        self.assertEqual(encoded, "Khoor, Zruog!")
        self.assertEqual(strings_demo.caesar(encoded, -3), "Hello, World!")
        self.assertEqual(strings_demo.caesar("xyz", 3), "abc")

    def test_anagram_and_compress(self):
        self.assertTrue(strings_demo.is_anagram("Listen", "Silent"))
        self.assertFalse(strings_demo.is_anagram("abc", "abd"))
        self.assertEqual(strings_demo.compress("aaabbbbc"), "a3b4c1")
        self.assertEqual(strings_demo.compress(""), "")

    def test_word_frequency_and_capitalize(self):
        counts = strings_demo.word_frequency("The cat. The hat!")
        self.assertEqual(counts, {"the": 2, "cat": 1, "hat": 1})
        self.assertEqual(strings_demo.capitalize_words("the quick fox"), "The Quick Fox")

    def test_exercise_strong_password(self):
        self.assertTrue(strings_demo.strong_password("Abc123!x"))
        self.assertFalse(strings_demo.strong_password("abc123"))
        self.assertFalse(strings_demo.strong_password("ABC123!!"))   # no lower case
        self.assertFalse(strings_demo.strong_password("Abcdef!!"))   # no digit
        self.assertFalse(strings_demo.strong_password("Abcdef12"))   # no symbol


class MatrixTests(unittest.TestCase):
    GRID = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test_create_makes_independent_rows(self):
        m = matrix.create_matrix(2, 3)
        m[0][0] = 9
        self.assertEqual(m, [[9, 0, 0], [0, 0, 0]])

    def test_identity_and_transpose(self):
        self.assertEqual(matrix.identity(3), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(matrix.transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])

    def test_sums(self):
        self.assertEqual(matrix.row_sums(self.GRID), [6, 15, 24])
        self.assertEqual(matrix.col_sums(self.GRID), [12, 15, 18])
        self.assertEqual(matrix.diagonal_sums(self.GRID), (15, 15))
        with self.assertRaises(ValueError):
            matrix.diagonal_sums([[1, 2, 3], [4, 5, 6]])

    def test_multiply(self):
        a, b = [[1, 2], [3, 4]], [[5, 6], [7, 8]]
        self.assertEqual(matrix.matrix_multiply(a, b), [[19, 22], [43, 50]])
        self.assertEqual(matrix.matrix_multiply(a, matrix.identity(2)), a)
        with self.assertRaises(ValueError):
            matrix.matrix_multiply([[1, 2, 3]], [[1, 2, 3]])

    def test_rotate_flatten_max(self):
        self.assertEqual(matrix.rotate_90_clockwise([[1, 2], [3, 4]]), [[3, 1], [4, 2]])
        self.assertEqual(matrix.flatten(self.GRID), list(range(1, 10)))
        self.assertEqual(matrix.find_max(self.GRID), (9, 2, 2))

    def test_tic_tac_toe(self):
        x_wins = [["X", "O", "X"], ["O", "X", "O"], [" ", " ", "X"]]
        o_column = [["O", "X", " "], ["O", "X", " "], ["O", " ", "X"]]
        nobody = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
        self.assertEqual(matrix.tic_tac_toe_winner(x_wins), "X")
        self.assertEqual(matrix.tic_tac_toe_winner(o_column), "O")
        self.assertIsNone(matrix.tic_tac_toe_winner(nobody))

    def test_exercise_pascal_triangle(self):
        self.assertEqual(matrix.pascal_triangle(0), [])
        self.assertEqual(matrix.pascal_triangle(1), [[1]])
        self.assertEqual(matrix.pascal_triangle(5)[4], [1, 4, 6, 4, 1])
        self.assertEqual(len(matrix.pascal_triangle(6)), 6)


class GradebookTests(unittest.TestCase):
    def test_averages(self):
        self.assertEqual(gradebook.student_average([88, 92, 79, 85]), 86.0)
        self.assertEqual(gradebook.class_subject_averages([[80, 60], [100, 80]]), [90.0, 70.0])

    def test_top_student(self):
        name, avg = gradebook.top_student(gradebook.STUDENTS, gradebook.SCORES)
        self.assertEqual(name, "Chen")
        self.assertEqual(avg, 93.2)

    def test_add_student_validation(self):
        names, scores = ["Asha"], [[80, 80]]
        subjects = ["Math", "Art"]
        gradebook.add_student(names, scores, subjects, "  ben ", [70, 90])
        self.assertEqual(names, ["Asha", "Ben"])
        self.assertEqual(scores[-1], [70, 90])
        for bad_name, bad_marks in (("ASHA", [1, 2]), ("", [1, 2]), ("Cy", [1]), ("Cy", [1, 101])):
            with self.assertRaises(ValueError):
                gradebook.add_student(names, scores, subjects, bad_name, bad_marks)
        self.assertEqual(len(names), 2)

    def test_report_contains_every_student_and_footer(self):
        report = gradebook.build_report(gradebook.STUDENTS, gradebook.SCORES, gradebook.SUBJECTS)
        for name in gradebook.STUDENTS:
            self.assertIn(name, report)
        self.assertIn("Class avg", report)

    def test_grade_distribution_totals(self):
        counts = gradebook.grade_distribution(gradebook.SCORES)
        self.assertEqual(sum(counts.values()), 20)

    def test_summary_flags_failing_student(self):
        lines = gradebook.summary_lines(gradebook.STUDENTS, gradebook.SCORES, gradebook.SUBJECTS)
        self.assertTrue(any("Ethan" in line for line in lines))


if __name__ == "__main__":
    unittest.main()
