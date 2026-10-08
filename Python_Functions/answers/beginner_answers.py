# ============================================================
#        PYTHON FUNCTIONS - BEGINNER LEVEL ANSWERS
# ============================================================
# Questions are in: questions/beginner_questions.py
# ============================================================

# A1. Function that prints "Hello, World!"
def greet():
    print("Hello, World!")

greet()
# Output: Hello, World!


# A2. Function that greets a user by name
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Divya")
# Output: Hello, Divya!


# A3. Function that returns the sum of two numbers
def add(a, b):
    return a + b

print(add(3, 5))
# Output: 8


# A4. Function that checks if a number is even
def is_even(n):
    return n % 2 == 0

print(is_even(4))   # Output: True
print(is_even(7))   # Output: False


# A5. Function that returns the square of a number
def square(n):
    return n ** 2

print(square(6))
# Output: 36


# A6. Function that returns the larger of two numbers
def max_of_two(a, b):
    return a if a > b else b

print(max_of_two(10, 20))
# Output: 20


# A7. Celsius to Fahrenheit converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(100))
# Output: 212.0


# A8. Function that checks if a number is positive
def is_positive(n):
    return n > 0

print(is_positive(5))    # Output: True
print(is_positive(-3))   # Output: False


# A9. Function with a default parameter value
def multiply(a, b=1):
    return a * b

print(multiply(5))     # Output: 5  (b defaults to 1)
print(multiply(5, 3))  # Output: 15


# A10. Function that returns full name
def full_name(first_name, last_name):
    return first_name + " " + last_name

print(full_name("Divya", "Sharma"))
# Output: Divya Sharma


# A11. Count vowels in a string
def count_vowels(s):
    count = 0
    for char in s.lower():
        if char in "aeiou":
            count += 1
    return count

print(count_vowels("Hello World"))
# Output: 3


# A12. Reverse a string
def reverse_string(s):
    return s[::-1]

print(reverse_string("Python"))
# Output: nohtyP


# A13. Check if a string is a palindrome
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False


# A14. Factorial using a loop
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))
# Output: 120


# A15. Print multiplication table
def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

print_table(5)
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50
