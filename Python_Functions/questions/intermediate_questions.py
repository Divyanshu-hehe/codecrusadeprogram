# ============================================================
#      PYTHON FUNCTIONS - INTERMEDIATE LEVEL QUESTIONS
# ============================================================
# Instructions: Try to solve each question on your own first.
# Answers are in: answers/intermediate_answers.py
# ============================================================

# Q1. Write a function `factorial_recursive` that calculates the
#     factorial of a number using RECURSION.

# Q2. Write a function `fibonacci` that takes n and returns a list
#     of the first n Fibonacci numbers.
#     Example: fibonacci(6) → [0, 1, 1, 2, 3, 5]

# Q3. Write a function `flatten_list` that takes a nested list and
#     returns a flat (1D) list.
#     Example: flatten_list([1, [2, 3], [4, [5]]]) → [1, 2, 3, 4, 5]

# Q4. Write a function `is_prime` that returns True if a number
#     is prime, False otherwise.

# Q5. Write a function `get_primes` that takes a number n and
#     returns a list of all prime numbers up to n.

# Q6. Write a function `word_frequency` that takes a sentence (string)
#     and returns a dictionary with each word and its frequency.
#     Example: "hello world hello" → {"hello": 2, "world": 1}

# Q7. Write a function `sort_by_key` that takes a list of
#     dictionaries and a key name, and returns the list sorted
#     by that key.
#     Example: sort_by_key([{"age": 25}, {"age": 18}], "age")

# Q8. Write a function `merge_dicts` that takes two dictionaries
#     and merges them. If a key exists in both, add their values.
#     Example: merge_dicts({"a": 1}, {"a": 2, "b": 3}) → {"a": 3, "b": 3}

# Q9. Write a function using *args called `total_sum` that accepts
#     any number of arguments and returns their sum.

# Q10. Write a function using **kwargs called `display_info` that
#      accepts any keyword arguments and prints them as
#      "key: value" on separate lines.

# Q11. Write a function `apply_twice` that takes a function `f`
#      and a value `x`, and returns f(f(x)).
#      Example: apply_twice(lambda x: x+3, 10) → 16

# Q12. Write a function `make_multiplier` that takes a number `n`
#      and returns a NEW function that multiplies its input by n.
#      (This is a closure.)
#      Example: triple = make_multiplier(3); triple(5) → 15

# Q13. Write a function `filter_evens` that uses the built-in
#      `filter()` function to return only even numbers from a list.

# Q14. Write a function `squares_map` that uses the built-in
#      `map()` function to return the squares of all numbers in a list.

# Q15. Write a function `binary_search` that takes a sorted list
#      and a target value. Return the index if found, else return -1.

# Q16. Write a function `caesar_cipher` that takes a string and a
#      shift value, and returns the encrypted string by shifting
#      each letter by the given amount (wraps around the alphabet).
#      Example: caesar_cipher("abc", 2) → "cde"

# Q17. Write a function `chunk_list` that splits a list into
#      chunks of size n.
#      Example: chunk_list([1,2,3,4,5], 2) → [[1,2],[3,4],[5]]

# Q18. Write a function `count_chars` that takes a string and
#      returns a dictionary of each character and its count.
#      Ignore spaces.

# Q19. Write a decorator function `timer` that measures and prints
#      how long a function takes to execute.

# Q20. Write a function `power_set` that takes a list and returns
#      all possible subsets (the power set).
#      Example: power_set([1,2]) → [[], [1], [2], [1,2]]
