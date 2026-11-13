"""Topic 6 - Strings: indexing, slicing, methods, formatting, text algorithms.

STARTER FILE: finish every function marked TODO, then run the tests for this
topic (see README.md). Functions marked WORKED EXAMPLE are already done.
"""

import string

from utils import header


# WORKED EXAMPLE: this one is already finished. Read it, then copy its style.
def is_palindrome(text):
    """Ignore case, spaces and punctuation."""
    cleaned = [ch.lower() for ch in text if ch.isalnum()]
    return cleaned == cleaned[::-1]


def count_vowels(text):
    """Number of vowels (a, e, i, o, u) in the text, ignoring case.

    Hint: Lower-case the text and count the characters found in 'aeiou'.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write count_vowels()")


def strong_password(text):
    """True if the text has an upper-case letter, a lower-case letter, a digit and a symbol.

    Hint: Use any(...) with ch.isupper(), ch.islower(), ch.isdigit() and `ch
          in string.punctuation`. Check: 'Abc123!x' -> True, 'abc123' ->
          False.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write strong_password()")


def reverse_words(sentence):
    """'one two three' -> 'three two one'.

    Hint: split() the sentence, reverse the list with [::-1], then '
          '.join(...) it.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write reverse_words()")


def caesar(text, shift):
    """Shift letters by `shift` places, leaving other characters alone.

    Hint: For letters: choose the base ord('A') or ord('a'), shift, wrap with
          % 26, convert back with chr(). Leave other characters unchanged.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write caesar()")


def is_anagram(a, b):
    """True if both texts use the same letters, ignoring case, spaces and punctuation.

    Hint: Compare sorted lists of the lower-cased letters of each text,
          skipping non-letters.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write is_anagram()")


def word_frequency(text):
    """Case-insensitive word counts with punctuation stripped.

    Hint: Lower-case each word, strip punctuation with
          word.strip(string.punctuation), and count in a dict.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write word_frequency()")


def compress(text):
    """Run-length encoding: 'aaabbc' -> 'a3b2c1'.

    Hint: Walk through the text counting runs of the same character: 'aaabbc'
          -> 'a3b2c1'. Empty text returns ''.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write compress()")


def capitalize_words(sentence):
    """Capitalise the first letter of every word: 'the quick fox' -> 'The Quick Fox'.

    Hint: split() the sentence, capitalize() each word, and join with single
          spaces.
    """
    # TODO: write your code here, then delete the raise line below.
    raise NotImplementedError("TODO: write capitalize_words()")


def demo():
    header("6. STRINGS")

    s = "Hello, Python!"
    print(f"s = {s!r}")
    print(f"  s[0]={s[0]!r}  s[-1]={s[-1]!r}  s[7:13]={s[7:13]!r}  s[::-1]={s[::-1]!r}")
    print(f"  len(s) = {len(s)}   'Py' in s: {'Py' in s}")
    print("  Strings are immutable: s[0] = 'J' would raise TypeError")

    print("\nCommon methods:")
    print(f"  upper / lower / title: {s.upper()} | {s.lower()} | {s.title()}")
    print(f"  replace('Python','World'): {s.replace('Python', 'World')}")
    print(f"  find('o')={s.find('o')}  count('l')={s.count('l')}  find('z')={s.find('z')}")
    print(f"  startswith('Hell')={s.startswith('Hell')}  endswith('?')={s.endswith('?')}")
    print(f"  '  padded  '.strip() -> {'  padded  '.strip()!r}")
    print(f"  isdigit: '123'->{'123'.isdigit()}  'a1'->{'a1'.isdigit()}")

    print("\nsplit and join:")
    csv = "red,green,blue"
    parts = csv.split(",")
    print(f"  {csv!r}.split(',') -> {parts}")
    print(f"  ' | '.join(parts)  -> {' | '.join(parts)!r}")

    print("\nLooping over a string:")
    print("  ", [f"{i}:{ch}" for i, ch in enumerate("abc")])

    print("\nText algorithms:")
    print(f"  is_palindrome('A man, a plan, a canal: Panama') = "
          f"{is_palindrome('A man, a plan, a canal: Panama')}")
    print(f"  count_vowels('Programming')   = {count_vowels('Programming')}")
    print(f"  reverse_words('one two three') = {reverse_words('one two three')!r}")
    print(f"  caesar('Hello, World!', 3)     = {caesar('Hello, World!', 3)!r}")
    print(f"  caesar(..., -3) restores it    = {caesar(caesar('Hello, World!', 3), -3)!r}")
    print(f"  is_anagram('Listen','Silent')  = {is_anagram('Listen', 'Silent')}")
    print(f"  compress('aaabbbbc')           = {compress('aaabbbbc')!r}")
    print(f"  capitalize_words('the quick brown fox') = "
          f"{capitalize_words('the quick brown fox')!r}")

    text = "the cat and the hat and the bat"
    print(f"  word_frequency({text!r})")
    print("   ", word_frequency(text))

    print("\nFormatting a mini table:")
    for name, price in (("Tea", 2.5), ("Coffee", 3.75), ("Juice", 4.0)):
        print(f"  {name:<8}{price:>6.2f}")


if __name__ == "__main__":
    demo()
