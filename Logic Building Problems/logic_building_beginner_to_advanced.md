# Python Logic Building Problems: Beginner to Advanced (Up to Loops)

---

## BEGINNER LEVEL

### Variables, Operators & Basic Logic

1. Write a program to swap two numbers without using a third variable.
2. Write a program to find the largest of three numbers.
3. Write a program to check if a number is divisible by both 3 and 5.
4. Write a program to calculate simple interest.
   - Formula: SI = (P * R * T) / 100
5. Write a program to convert Celsius to Fahrenheit.
   - Formula: F = (C * 9/5) + 32
6. Write a program to find the area and perimeter of a rectangle.
7. Write a program to check if a number is positive, negative, or zero.
8. Write a program to check if a person is eligible to vote (age >= 18).
9. Write a program to find the absolute value of a number without using `abs()`.
10. Write a program to check if two numbers are equal.

---

### String Logic

11. Write a program to count the number of vowels in a string.
12. Write a program to reverse a string without using slicing.
13. Write a program to check if a string is a palindrome.
14. Write a program to count the number of words in a sentence.
15. Write a program to convert the first letter of each word to uppercase without using `.title()`.

---

### Conditional Logic

16. Write a program to find the grade of a student based on marks:
    - 90-100 → A
    - 75-89  → B
    - 60-74  → C
    - Below 60 → F
17. Write a program to check if a year is a leap year.
18. Write a program to find the largest of four numbers using only `if-else`.
19. Write a program to check if a character is a vowel or consonant.
20. Write a program to determine the day of the week based on a number (1=Monday, 7=Sunday).

---

## INTERMEDIATE LEVEL

### Loop Logic — Numbers

21. Write a program to print all even numbers from 1 to 100.
22. Write a program to print all odd numbers between two given numbers.
23. Write a program to find the sum of digits of a number.
    - Example: 1234 → 1+2+3+4 = 10
24. Write a program to reverse a number.
    - Example: 1234 → 4321
25. Write a program to check if a number is a palindrome.
    - Example: 121 → palindrome, 123 → not
26. Write a program to find the factorial of a number using a loop.
27. Write a program to check if a number is prime.
28. Write a program to print all prime numbers between 1 and 100.
29. Write a program to find the GCD (Greatest Common Divisor) of two numbers.
30. Write a program to find the LCM of two numbers.
31. Write a program to print the Fibonacci sequence up to `n` terms.
32. Write a program to find the `nth` Fibonacci number.
33. Write a program to check if a number is an Armstrong number.
    - Example: 153 = 1³ + 5³ + 3³ = 153 ✓
34. Write a program to print all Armstrong numbers between 1 and 1000.
35. Write a program to find the sum of all prime numbers up to `n`.

---

### Loop Logic — Patterns

36. Print the following pattern for `n` rows:
    ```
    1
    1 2
    1 2 3
    1 2 3 4
    ```
37. Print the following pattern:
    ```
    *
    * *
    * * *
    * * * *
    * * * * *
    ```
38. Print the inverted triangle pattern:
    ```
    * * * * *
    * * * *
    * * *
    * *
    *
    ```
39. Print the number pyramid:
    ```
        1
       1 2
      1 2 3
     1 2 3 4
    1 2 3 4 5
    ```
40. Print the following pattern:
    ```
    1
    2 2
    3 3 3
    4 4 4 4
    ```

---

### Loop Logic — String & Mixed

41. Write a program to count the frequency of each character in a string using a loop.
42. Write a program to check if a string has all unique characters.
43. Write a program to find the most repeated character in a string.
44. Write a program to remove all spaces from a string using a loop.
45. Write a program to print all substrings of a string.

---

## ADVANCED LEVEL (Still within Loops)

### Number Theory & Logic

46. Write a program to find all factors of a given number.
47. Write a program to check if a number is a perfect number.
    - A perfect number equals the sum of its factors (excluding itself).
    - Example: 6 = 1 + 2 + 3 ✓
48. Write a program to print all perfect numbers up to 1000.
49. Write a program to find the sum of the series:
    - 1 + 1/2 + 1/3 + ... + 1/n
50. Write a program to find the power of a number without using `**`.
51. Write a program to check if a number is a strong number.
    - A strong number's digit factorials sum equals the number.
    - Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145 ✓
52. Write a program to print all strong numbers up to 1000.
53. Write a program to find the digital root of a number.
    - Keep summing digits until a single digit remains.
    - Example: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2
54. Write a program to find the number of digits in a number without converting to string.
55. Write a program to check if a number is a Disarium number.
    - Each digit raised to its position power, summed equals the number.
    - Example: 89 = 8¹ + 9² = 8 + 81 = 89 ✓

---

### Pattern Challenges

56. Print a hollow square pattern of size `n`:
    ```
    * * * * *
    *       *
    *       *
    *       *
    * * * * *
    ```
57. Print a diamond pattern for `n`:
    ```
        *
       * *
      * * *
       * *
        *
    ```
58. Print Pascal's Triangle up to `n` rows:
    ```
         1
        1 1
       1 2 1
      1 3 3 1
     1 4 6 4 1
    ```
59. Print a zigzag number pattern.
60. Print a spiral of numbers using nested loops.

---

### Combined Logic Problems

61. Write a program to find the second largest number among `n` numbers entered by the user.
62. Write a program to count how many numbers between 1 and 1000 are divisible by 3 but not by 5.
63. Write a program to find all twin primes up to 100.
    - Twin primes are pairs of primes that differ by 2. Example: (3,5), (11,13)
64. Write a program to print numbers from 1 to 100, but:
    - Print "Fizz" for multiples of 3
    - Print "Buzz" for multiples of 5
    - Print "FizzBuzz" for multiples of both
65. Write a program to simulate a simple ATM:
    - Start with a balance
    - Loop: ask the user to deposit, withdraw, or check balance
    - Stop when user chooses to exit
66. Write a program to find the longest word in a sentence using a loop.
67. Write a program to generate a multiplication table for numbers 1 to 10 in a grid format.
68. Write a program to find the number of 1s in the binary representation of all numbers from 1 to `n`.
69. Write a program to check how many numbers from 1 to 500 are palindromes.
70. Write a program to find the sum of all numbers in a range that are neither divisible by 3 nor by 7.

---

> **Tip:** Try solving each problem first on your own before looking up solutions. Focus on understanding the logic, not just the syntax.
