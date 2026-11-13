# Python Basics Lab: Starter Files

These are the starter files for the **Student Gradebook** project. Every function has a
name, a docstring and a hint, but its body is empty. You write the code; the tests tell you
when it is right.

Requires **Python 3.9 or newer**. No extra packages.

## How to work

1. Check your version: `python --version` (3.9 or higher).
2. Run the tests to see where you start: `python -m unittest discover tests`. Most fail at
   first. That is expected.
3. Work through the topics in the order below. For each one:
   - open the file and read the **WORKED EXAMPLE** at the top (already finished);
   - find each function marked `TODO`, read its docstring and **Hint**, and write the body;
   - delete the `raise NotImplementedError(...)` line when your code is ready;
   - run that topic's tests (command in the table) until they pass.
4. Run `python main.py` at any time. A demo stops at the first unfinished function and names it.
   Each function you finish brings more of the demo to life.

## Order of work

| # | Topic | File | Run just these tests | Functions to write |
|---|-------|------|----------------------|--------------------|
| 1 | Basics | `basics.py` | `python -m unittest tests.test_all.BasicsTests -v` | `bmi`, `simple_interest`, `fahrenheit_to_celsius`, `compound_interest` |
| 2 | Selection | `selection.py` | `python -m unittest tests.test_all.SelectionTests -v` | `is_leap_year`, `classify_triangle`, `bmi_category`, `day_type`, `ticket_price`, `fizzbuzz_word` |
| 3 | Loops | `loops.py` | `python -m unittest tests.test_all.LoopTests -v` | `factorial`, `fibonacci`, `is_prime`, `collatz_steps`, `triangle`, `multiplication_table`, `perfect_numbers_below`, `pyramid`, `digit_sum` |
| 4 | Functions | `functions.py` | `python -m unittest tests.test_all.FunctionTests -v` | `average`, `describe`, `min_max`, `factorial_recursive`, `power`, `compose`, `gcd`, `make_multiplier`, `apply_twice`, `counter_demo` |
| 5 | Lists | `lists_demo.py` | `python -m unittest tests.test_all.ListTests -v` | `second_largest`, `rotate_left`, `merge_sorted`, `running_total`, `frequency`, `chunk`, `bubble_sort` |
| 6 | Strings | `strings_demo.py` | `python -m unittest tests.test_all.StringTests -v` | `count_vowels`, `strong_password`, `reverse_words`, `caesar`, `is_anagram`, `word_frequency`, `compress`, `capitalize_words` |
| 7 | Multidimensional lists | `matrix.py` | `python -m unittest tests.test_all.MatrixTests -v` | `pascal_triangle`, `identity`, `transpose`, `row_sums`, `col_sums`, `diagonal_sums`, `matrix_multiply`, `rotate_90_clockwise`, `flatten`, `find_max`, `tic_tac_toe_winner`, `format_matrix` |
| 8 | Capstone | `gradebook.py` | `python -m unittest tests.test_all.GradebookTests -v` | `class_subject_averages`, `top_student`, `validate_marks`, `add_student`, `build_report`, `summary_lines`, `grade_distribution` |

The practice tasks in your instructions map to these functions: `fahrenheit_to_celsius` and
`compound_interest` (basics), `ticket_price` (selection), `perfect_numbers_below` and
`pyramid` (loops), `compose` and `gcd` (functions), `merge_sorted` (lists),
`strong_password` (strings) and `pascal_triangle` (multidimensional lists).

`utils.py` and `main.py` are already complete. You do not need to change them.

## Tips

- Read the failing test first. It shows exactly what your function must return.
- Fix one function at a time and re-run only its topic's tests.
- Put `print(...)` calls in while you debug, and remove them before you submit.
- Build grids with a list comprehension, never `[[0] * 3] * 3`.
- Stuck? Re-read the worked example, then the hint, then ask for help.

## When you are done

- `python -m unittest discover tests -v` reports **OK** with all 48 tests passing.
- `python main.py --all` runs every demo with no "Not finished yet" messages.
- Every function has its docstring and no `TODO` or `NotImplementedError` is left.
