# def get_top_students(**kwargs):
#     top_students = []
#     for student,score in kwargs.items():
#         if score > 90:
#             top_students.append(student)
#     return top_students
# print(get_top_students(tim=91, stacy=83, carlos=97, jim=69))  # Output: ['tim', 'carlos']

# def count_vowels(string):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count
# print(count_vowels("Hello World"))  # Output: 3

# def reverse_string(string):
#     return string[::-1]
# print(reverse_string("Hello World"))  # Output: "dlroW olleH"

# def is_palindrome(string):
#     if string == string[::-1]:
#         return True
#     else:
#         return False
# print(is_palindrome("racecar"))  # Output: True
# print(is_palindrome("hello"))  # Output: False

# def find_max(numbers):
#     if not numbers:
#         return None
#     max_num = numbers[0]
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#     return max_num
# print(find_max([3, 7, 2, 9, 5]))  # Output: 9

# def sum_even(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 == 0:
#             total += num
#     return total
# print(sum_even([1, 2, 3, 4, 5, 6]))  # Output: 12


# def sum_odd(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 == 1:
#             total += num
#     return total
# print(sum_odd([1, 2, 3, 4, 5, 6]))  # Output: 12

# def word_count(string):
#     words = string
#     return len(words)
# print(word_count("Hello World"))  # Output: 2

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))  # Output: 120

# def remove_duplicates(lst):
#     result = []
#     for item in lst:
#         if item not in result:
#             result.append(item)
#     return result
# print(remove_duplicates([1, 2, 2, 4,3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]

# n = 10
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
import calendar as calc
print(calc.weekday(2023, 10, 1))
  # Output: 6 (Sunday)


    