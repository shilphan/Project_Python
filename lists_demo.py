"""Topic 5 - Lists: indexing, slicing, methods, comprehensions, sorting.

STARTER FILE: finish every function marked TODO, then run the tests for this
topic (see README.md). Functions marked WORKED EXAMPLE are already done.
"""

from utils import header


# WORKED EXAMPLE: this one is already finished. Read it, then copy its style.
def remove_duplicates(items):
    """Remove repeats but keep the original order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def second_largest(numbers):
    """Second largest *distinct* value, or None if there isn't one.

    Hint: Work with sorted(set(numbers)). Return None if there are fewer than
          2 distinct values.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write second_largest()")


def rotate_left(items, k):
    """Move the first k items to the end.

    Hint: Reduce k with k %= len(items), then slice: items[k:] + items[:k]. An
          empty list returns [].
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write rotate_left()")


def merge_sorted(a, b):
    """Merge two sorted lists into one sorted list without calling sort().

    Hint: Keep an index into each list; keep appending the smaller front item;
          then add whatever is left over. Do not call sort().
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write merge_sorted()")


def running_total(numbers):
    """Cumulative sums: [1, 2, 3] -> [1, 3, 6].

    Hint: Keep a total, add each number to it, and append the total each time.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write running_total()")


def frequency(items):
    """Count occurrences with a dict.

    Hint: Use a dict and counts.get(item, 0) + 1.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write frequency()")


def chunk(items, size):
    """Split a list into pieces of at most `size` items.

    Hint: range(0, len(items), size) gives the start of every slice.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write chunk()")


def bubble_sort(numbers):
    """Sort a copy of the list by repeatedly swapping neighbours.

    Hint: Work on list(numbers) so the input is not changed. Swap neighbours
          with data[i], data[i + 1] = data[i + 1], data[i].
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write bubble_sort()")


def demo():
    header("5. LISTS")

    nums = [10, 20, 30, 40, 50]
    print("Indexing and slicing on", nums)
    print(f"  nums[0]={nums[0]}  nums[-1]={nums[-1]}")
    print(f"  nums[1:4]={nums[1:4]}  nums[::2]={nums[::2]}  nums[::-1]={nums[::-1]}")

    print("\nChanging a list:")
    fruits = ["apple", "banana"]
    fruits.append("cherry")
    fruits.insert(1, "blueberry")
    fruits.extend(["date", "elderberry"])
    print("  after append / insert / extend:", fruits)
    fruits.remove("banana")
    last = fruits.pop()
    print(f"  after remove('banana') and pop() -> popped {last!r}: {fruits}")
    fruits[0] = "apricot"
    print("  after item assignment:", fruits)

    print("\nUseful built-ins on", nums)
    print(f"  len={len(nums)} sum={sum(nums)} min={min(nums)} max={max(nums)}")
    print(f"  30 in nums: {30 in nums}   nums.index(30) = {nums.index(30)}")

    print("\nSorting:")
    messy = [5, 2, 9, 1, 7]
    print("  sorted(messy)             ->", sorted(messy), "(new list)")
    print("  sorted(..., reverse=True) ->", sorted(messy, reverse=True))
    messy.sort()
    print("  messy.sort() changed it   ->", messy)
    print("  bubble_sort([5,2,9,1,7])  ->", bubble_sort([5, 2, 9, 1, 7]))

    print("\nList comprehensions:")
    print("  squares:        ", [n * n for n in range(1, 8)])
    print("  even squares:   ", [n * n for n in range(1, 11) if n % 2 == 0])
    print("  upper-cased:    ", [f.upper() for f in ["fig", "plum"]])

    print("\nProblem-solving helpers:")
    data = [4, 1, 4, 2, 9, 9, 3]
    print("  data                 =", data)
    print("  remove_duplicates    =", remove_duplicates(data))
    print("  second_largest       =", second_largest(data))
    print("  rotate_left(data, 2) =", rotate_left(data, 2))
    print("  running_total        =", running_total(data))
    print("  frequency            =", frequency(data))
    print("  chunk(data, 3)       =", chunk(data, 3))

    print("\nCopy gotcha:")
    original = [1, 2, 3]
    alias = original          # same list, two names
    clone = original.copy()   # a real copy
    alias.append(99)
    print(f"  original={original} (changed via alias)   clone={clone} (unchanged)")


if __name__ == "__main__":
    demo()
