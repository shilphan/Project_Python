"""Capstone - Student Gradebook.

Uses every topic in the project:
  basics        variables, arithmetic, f-strings
  selection     grade letters, validation (if / elif / else)
  loops         for / while over students and subjects
  functions     small reusable helpers
  lists         names and subjects
  strings       formatting, split(), strip(), title()
  2-D lists     the score table: one row per student, one column per subject

STARTER FILE: finish every function marked TODO, then run the tests for this
topic (see README.md). Functions marked WORKED EXAMPLE are already done.
"""

from matrix import col_sums, row_sums
from selection import grade_letter
from utils import ask_int, header, safe_input

SUBJECTS = ["Math", "Science", "English", "History"]
STUDENTS = ["Asha", "Ben", "Chen", "Divya", "Ethan"]
SCORES = [
    [88, 92, 79, 85],
    [67, 58, 72, 64],
    [95, 98, 91, 89],
    [74, 81, 86, 90],
    [45, 52, 60, 38],
]


# WORKED EXAMPLE: this one is already finished. Read it, then copy its style.
def student_average(row):
    """Average of one student's marks, rounded to 1 decimal place."""
    return round(sum(row) / len(row), 1)


def class_subject_averages(scores):
    """Average per subject (column), reusing col_sums from the matrix module.

    Hint: Reuse col_sums(scores). Divide each total by the number of students
          and round to 1 decimal place.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write class_subject_averages()")


def top_student(names, scores):
    """(name, average) of the best student.

    Hint: Compute every student's average, find the highest with max(), and
          use .index() to get the matching name.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write top_student()")


def validate_marks(marks, subject_count):
    """Raise ValueError unless there is one 0-100 mark per subject.

    Hint: Raise ValueError if the number of marks is wrong, or if any mark is
          outside 0 to 100.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write validate_marks()")


def add_student(names, scores, subjects, name, marks):
    """Append a new student (in place) after validating the input.

    Hint: Use strip().title() on the name. Reject an empty name and a
          duplicate name (ignore case). Call validate_marks, then append to
          both lists.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write add_student()")


def build_report(names, scores, subjects):
    """Return the whole gradebook as one formatted string.

    Hint: Build each line with f-string widths such as f'{mark:>9}'. Use
          row_sums(), student_average-style rounding and grade_letter(). Match
          the expected report in the instructions.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write build_report()")


def summary_lines(names, scores, subjects):
    """A few headline facts about the class.

    Hint: Use top_student(), class_subject_averages() and grade_letter() to
          find the best student, strongest and weakest subject, and anyone
          with an F. Return four lines of text.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write summary_lines()")


def grade_distribution(scores):
    """Count of each letter grade across all individual marks.

    Hint: Start from {letter: 0 for letter in 'ABCDF'}, then loop over every
          mark and add 1 to its grade_letter().
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write grade_distribution()")


def demo():
    header("8. CAPSTONE: STUDENT GRADEBOOK")
    print(build_report(STUDENTS, SCORES, SUBJECTS))
    print()
    for line in summary_lines(STUDENTS, SCORES, SUBJECTS):
        print(line)
    print("\nGrade distribution across all marks:")
    for letter, count in grade_distribution(SCORES).items():
        print(f"  {letter}: {'#' * count} {count}")


def interactive():
    """Menu loop: view the report or add students. Works on copies of the data."""
    names = list(STUDENTS)
    scores = [list(row) for row in SCORES]
    header("INTERACTIVE GRADEBOOK")
    while True:
        print("\n1) Show report   2) Add student   3) Class summary   0) Back")
        choice = ask_int("Choose: ", 0, 3)
        if choice is None or choice == 0:
            break
        if choice == 1:
            print(build_report(names, scores, SUBJECTS))
        elif choice == 2:
            name = safe_input("Student name: ", "") or ""
            raw = safe_input(f"Marks for {', '.join(SUBJECTS)} (separated by spaces): ", "") or ""
            try:
                marks = [int(part) for part in raw.split()]
                add_student(names, scores, SUBJECTS, name, marks)
                print(f"Added {name.strip().title()}.")
            except ValueError as error:
                print(f"Could not add student: {error}")
        else:
            for line in summary_lines(names, scores, SUBJECTS):
                print(line)


if __name__ == "__main__":
    demo()
