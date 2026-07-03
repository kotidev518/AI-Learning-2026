# utils.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def square(x):
    return x * x

def cube(x):
    return x ** 3

def is_even(x):
    return x % 2 == 0

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def reverse_string(text):
    return text[::-1]

def count_vowels(text):
    return sum(1 for c in text.lower() if c in "aeiou")