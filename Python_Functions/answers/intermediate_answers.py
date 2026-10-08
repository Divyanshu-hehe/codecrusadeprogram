# ============================================================
#      PYTHON FUNCTIONS - INTERMEDIATE LEVEL ANSWERS
# ============================================================
# Questions are in: questions/intermediate_questions.py
# ============================================================

import time

# A1. Factorial using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))
# Output: 120


# A2. First n Fibonacci numbers
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

print(fibonacci(6))
# Output: [0, 1, 1, 2, 3, 5]


# A3. Flatten a nested list
def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

print(flatten_list([1, [2, 3], [4, [5]]]))
# Output: [1, 2, 3, 4, 5]


# A4. Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))   # Output: True
print(is_prime(10))   # Output: False


# A5. List all primes up to n
def get_primes(n):
    return [i for i in range(2, n + 1) if is_prime(i)]

print(get_primes(30))
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# A6. Word frequency counter
def word_frequency(sentence):
    freq = {}
    for word in sentence.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_frequency("hello world hello"))
# Output: {'hello': 2, 'world': 1}


# A7. Sort list of dictionaries by a key
def sort_by_key(lst, key):
    return sorted(lst, key=lambda d: d[key])

data = [{"name": "Zara", "age": 25}, {"name": "Amit", "age": 18}, {"name": "Riya", "age": 22}]
print(sort_by_key(data, "age"))
# Output: [{'name': 'Amit', 'age': 18}, {'name': 'Riya', 'age': 22}, {'name': 'Zara', 'age': 25}]


# A8. Merge two dictionaries, adding values for shared keys
def merge_dicts(d1, d2):
    merged = dict(d1)
    for key, value in d2.items():
        merged[key] = merged.get(key, 0) + value
    return merged

print(merge_dicts({"a": 1}, {"a": 2, "b": 3}))
# Output: {'a': 3, 'b': 3}


# A9. *args — sum of any number of arguments
def total_sum(*args):
    return sum(args)

print(total_sum(1, 2, 3, 4, 5))
# Output: 15


# A10. **kwargs — display key-value pairs
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Divya", age=20, city="Delhi")
# Output:
# name: Divya
# age: 20
# city: Delhi


# A11. Apply a function twice (higher-order function)
def apply_twice(f, x):
    return f(f(x))

print(apply_twice(lambda x: x + 3, 10))
# Output: 16


# A12. Closure — make_multiplier
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

triple = make_multiplier(3)
print(triple(5))
# Output: 15


# A13. filter() — keep only even numbers
def filter_evens(lst):
    return list(filter(lambda x: x % 2 == 0, lst))

print(filter_evens([1, 2, 3, 4, 5, 6]))
# Output: [2, 4, 6]


# A14. map() — return squares of numbers
def squares_map(lst):
    return list(map(lambda x: x ** 2, lst))

print(squares_map([1, 2, 3, 4, 5]))
# Output: [1, 4, 9, 16, 25]


# A15. Binary search
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9, 11], 7))
# Output: 3
print(binary_search([1, 3, 5, 7, 9, 11], 4))
# Output: -1


# A16. Caesar cipher
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

print(caesar_cipher("abc", 2))
# Output: cde
print(caesar_cipher("xyz", 3))
# Output: abc


# A17. Split list into chunks
def chunk_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

print(chunk_list([1, 2, 3, 4, 5], 2))
# Output: [[1, 2], [3, 4], [5]]


# A18. Character frequency (ignoring spaces)
def count_chars(s):
    freq = {}
    for char in s:
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
    return freq

print(count_chars("hello world"))
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}


# A19. Decorator — timer
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(0.1)
    return a + b

print(slow_add(3, 4))
# Output: slow_add took 0.1xxxxx seconds
#         7


# A20. Power set of a list
def power_set(lst):
    result = [[]]
    for item in lst:
        result += [subset + [item] for subset in result]
    return result

print(power_set([1, 2]))
# Output: [[], [1], [2], [1, 2]]
print(power_set([1, 2, 3]))
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
