"""Topic 7 - Multidimensional lists: 2-D grids (matrices) and a 3-D example.

STARTER FILE: finish every function marked TODO, then run the tests for this
topic (see README.md). Functions marked WORKED EXAMPLE are already done.
"""

from utils import header


# WORKED EXAMPLE: this one is already finished. Read it, then copy its style.
def create_matrix(rows, cols, fill=0):
    """Build a rows x cols grid.

    Never write [[fill] * cols] * rows: that repeats the SAME inner list, so
    changing one row changes them all. A comprehension makes separate rows.
    """
    return [[fill for _ in range(cols)] for _ in range(rows)]


def pascal_triangle(rows):
    """First `rows` rows of Pascal's triangle as a list of lists (jagged 2-D list).

    Hint: Each row starts and ends with 1; every middle entry is the sum of
          the two entries above it. Check: pascal_triangle(5)[4] -> [1, 4, 6,
          4, 1].
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write pascal_triangle()")


def identity(n):
    """n x n identity matrix: 1s on the main diagonal, 0s elsewhere.

    Hint: Start from create_matrix(n, n) and set matrix[i][i] = 1.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write identity()")


def transpose(matrix):
    """Rows become columns.

    Hint: Entry [c][r] of the result is entry [r][c] of the input.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write transpose()")


def row_sums(matrix):
    """Total of each row.

    Hint: Take sum() of each row.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write row_sums()")


def col_sums(matrix):
    """Total of each column.

    Hint: For each column index c, add up row[c] over all rows.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write col_sums()")


def diagonal_sums(matrix):
    """(main diagonal, anti-diagonal) of a square matrix.

    Hint: Raise ValueError if the matrix is not square. The main diagonal is
          [i][i]; the anti-diagonal is [i][n - 1 - i].
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write diagonal_sums()")


def matrix_multiply(a, b):
    """Standard matrix product using three nested loops.

    Hint: Use three nested loops: result[i][j] += a[i][k] * b[k][j]. Raise
          ValueError if the columns of a do not equal the rows of b.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write matrix_multiply()")


def rotate_90_clockwise(matrix):
    """Rotate a grid a quarter turn clockwise.

    Hint: Reverse the order of the rows, then transpose the result (zip(*rows)
          is handy).
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write rotate_90_clockwise()")


def flatten(matrix):
    """Turn a 2-D list into one flat list, row by row.

    Hint: A list comprehension with two for clauses.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write flatten()")


def find_max(matrix):
    """Return (value, row, col) of the largest entry.

    Hint: Loop with enumerate over the rows and over each row's values;
          remember (value, row, col) of the largest.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write find_max()")


def tic_tac_toe_winner(board):
    """Return 'X', 'O' or None for a 3x3 board of 'X', 'O' and ' '.

    Hint: Collect all 8 lines (3 rows, 3 columns, 2 diagonals). A line wins if
          its first cell is not ' ' and all three cells match.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write tic_tac_toe_winner()")


def format_matrix(matrix, indent="  "):
    """Right-aligned text grid, one line per row.

    Hint: Find the widest value, then right-align each value with
          f'{v:>{width}}' and join each row with spaces.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write format_matrix()")


def demo():
    header("7. MULTIDIMENSIONAL LISTS")

    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print("A 2-D list is a list of lists:")
    print(format_matrix(grid))
    print(f"  grid[1][2] = {grid[1][2]}  (row 1, column 2)")
    print(f"  grid[0]    = {grid[0]}  (a whole row)")
    print(f"  len(grid)={len(grid)} rows, len(grid[0])={len(grid[0])} columns")

    print("\nTraversing with nested loops:")
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if (r + c) % 2 == 0:
                print(f"  grid[{r}][{c}] = {value}")

    print("\nSums:")
    print(f"  row sums      {row_sums(grid)}")
    print(f"  column sums   {col_sums(grid)}")
    print(f"  diagonal sums {diagonal_sums(grid)}")

    print("\nTranspose:")
    print(format_matrix(transpose(grid)))
    print("Rotate 90 degrees clockwise:")
    print(format_matrix(rotate_90_clockwise(grid)))

    print("\nMatrix multiplication [[1,2],[3,4]] x [[5,6],[7,8]]:")
    print(format_matrix(matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])))
    print("Multiplying by the identity changes nothing:")
    print(format_matrix(matrix_multiply([[1, 2], [3, 4]], identity(2))))

    print(f"\nflatten -> {flatten(grid)}")
    print(f"find_max -> value, row, col = {find_max(grid)}")

    print("\nThe shared-row trap:")
    bad = [[0] * 3] * 2
    bad[0][0] = 9
    good = create_matrix(2, 3)
    good[0][0] = 9
    print(f"  [[0]*3]*2 then set [0][0]=9 -> {bad}  (both rows changed!)")
    print(f"  comprehension version       -> {good}")

    print("\nJagged (uneven) rows are allowed:")
    triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    for row in triangle:
        print("  " + str(row).center(20))

    print("\nTic-tac-toe board:")
    board = [["X", "O", "X"],
             ["O", "X", "O"],
             [" ", " ", "X"]]
    print(format_matrix(board))
    print(f"  winner: {tic_tac_toe_winner(board)}")

    print("\nThree dimensions: 2 classes x 2 students x 3 test scores")
    school = [
        [[90, 85, 70], [60, 75, 80]],
        [[88, 92, 95], [55, 65, 70]],
    ]
    for c, klass in enumerate(school, start=1):
        for s, scores in enumerate(klass, start=1):
            print(f"  class {c}, student {s}: scores={scores} avg={sum(scores) / len(scores):.1f}")


if __name__ == "__main__":
    demo()
