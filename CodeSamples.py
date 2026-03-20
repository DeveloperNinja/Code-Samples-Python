"""
================================================================================
  50 PYTHON CODE EXAMPLES — BEGINNER TO EXPERT
  Professor's Teaching Reference File
  
  Organized into 5 tiers:
    TIER 1 (Examples  1–10): Beginner       — Core syntax, types, I/O
    TIER 2 (Examples 11–20): Beginner+      — Functions, loops, collections
    TIER 3 (Examples 21–30): Intermediate   — OOP, files, error handling
    TIER 4 (Examples 31–40): Advanced       — Decorators, generators, lambdas
    TIER 5 (Examples 41–50): Expert         — Concurrency, metaclasses, design patterns
================================================================================
"""


# ==============================================================================
# TIER 1 — BEGINNER (Examples 1–10)
# Core syntax, variables, data types, basic I/O
# ==============================================================================

# ------------------------------------------------------------------------------
# Example 1: Hello World & Print Formatting
# Concept: print(), f-strings, basic output
# ------------------------------------------------------------------------------
print("--- Example 1: Hello World & Print Formatting ---")

name = "Alice"
age = 30
gpa = 3.85

# f-string (recommended modern style)
print(f"Hello, {name}! You are {age} years old with a GPA of {gpa:.2f}.")

# Older .format() style (still common in legacy codebases)
print("Hello, {}! You are {} years old.".format(name, age))

# Multi-line print using triple quotes
print("""
Student Profile:
  Name : Alice
  Age  : 30
  GPA  : 3.85
""")
# OUTPUT:
# Hello, Alice! You are 30 years old with a GPA of 3.85.
# Hello, Alice! You are 30 years old.
# (multi-line block shown above)


# ------------------------------------------------------------------------------
# Example 2: Variables & Data Types
# Concept: int, float, str, bool, type(), isinstance()
# ------------------------------------------------------------------------------
print("--- Example 2: Variables & Data Types ---")

my_int    = 42
my_float  = 3.14159
my_str    = "Python"
my_bool   = True
my_none   = None

# type() returns the type of a variable
print(type(my_int))    # <class 'int'>
print(type(my_float))  # <class 'float'>
print(type(my_str))    # <class 'str'>
print(type(my_bool))   # <class 'bool'>
print(type(my_none))   # <class 'NoneType'>

# isinstance() checks if a variable is of a given type (preferred over type() for checks)
print(isinstance(my_int, int))    # True
print(isinstance(my_str, float))  # False

# Python is dynamically typed — variables can be reassigned to different types
x = 10
x = "now I'm a string"
print(x)  # now I'm a string


# ------------------------------------------------------------------------------
# Example 3: Arithmetic & Math Operations
# Concept: operators, math module, integer division, modulo, exponentiation
# ------------------------------------------------------------------------------
print("--- Example 3: Arithmetic & Math Operations ---")

import math

a, b = 17, 5

print(a + b)    # Addition:        22
print(a - b)    # Subtraction:     12
print(a * b)    # Multiplication:  85
print(a / b)    # Division (float):  3.4
print(a // b)   # Integer division:  3
print(a % b)    # Modulo (remainder): 2
print(a ** b)   # Exponentiation: 1419857

# Math module
print(math.sqrt(144))      # 12.0
print(math.pi)             # 3.141592653589793
print(math.ceil(3.2))      # 4
print(math.floor(3.9))     # 3
print(math.log(100, 10))   # 2.0  (log base 10 of 100)

# Augmented assignment
counter = 0
counter += 1   # same as: counter = counter + 1
print(counter) # 1


# ------------------------------------------------------------------------------
# Example 4: Strings & String Methods
# Concept: string indexing, slicing, common methods
# ------------------------------------------------------------------------------
print("--- Example 4: Strings & String Methods ---")

s = "Hello, Python World!"

# Indexing (0-based, negative counts from the end)
print(s[0])    # H
print(s[-1])   # !

# Slicing [start:stop:step]
print(s[7:13])    # Python
print(s[:5])      # Hello
print(s[::2])     # Hlo yhnWrd  (every 2nd character)
print(s[::-1])    # !dlroW nohtyP ,olleH  (reversed)

# Common methods
print(s.upper())              # HELLO, PYTHON WORLD!
print(s.lower())              # hello, python world!
print(s.replace("World", "Universe"))  # Hello, Python Universe!
print(s.split(", "))          # ['Hello', 'Python World!']
print(s.strip())              # strips leading/trailing whitespace
print("  spaces  ".strip())   # 'spaces'
print(s.startswith("Hello"))  # True
print(s.find("Python"))       # 7  (index where "Python" starts, -1 if not found)
print(len(s))                 # 20

# String multiplication
print("=" * 30)  # prints 30 equal signs


# ------------------------------------------------------------------------------
# Example 5: Lists — Creation, Indexing & Methods
# Concept: list as ordered, mutable sequence
# ------------------------------------------------------------------------------
print("--- Example 5: Lists ---")

fruits = ["apple", "banana", "cherry", "date"]

# Access
print(fruits[0])    # apple
print(fruits[-1])   # date
print(fruits[1:3])  # ['banana', 'cherry']

# Mutation
fruits.append("elderberry")      # add to end
fruits.insert(1, "avocado")     # insert at index 1
fruits.remove("banana")         # remove first occurrence of value
popped = fruits.pop()           # remove & return last element
print(popped)                   # elderberry

# Useful operations
print(len(fruits))              # current count
print("apple" in fruits)        # True — membership test
fruits.sort()                   # sort in-place (alphabetically)
print(fruits)

fruits_copy = fruits.copy()     # shallow copy
fruits.reverse()                # reverse in-place

# List from range
numbers = list(range(1, 11))   # [1, 2, 3, ..., 10]
print(numbers)


# ------------------------------------------------------------------------------
# Example 6: Tuples & Sets
# Concept: immutable sequences vs. unordered unique collections
# ------------------------------------------------------------------------------
print("--- Example 6: Tuples & Sets ---")

# Tuple — immutable, ordered, allows duplicates
coordinates = (40.7128, -74.0060)  # NYC lat/lon
print(coordinates[0])   # 40.7128
# coordinates[0] = 0    # TypeError! Tuples cannot be changed

# Tuple unpacking
lat, lon = coordinates
print(f"Latitude: {lat}, Longitude: {lon}")

# Single-element tuple needs a trailing comma
single = (42,)
print(type(single))  # <class 'tuple'>

# Set — unordered, unique elements, mutable
colors = {"red", "green", "blue", "red"}  # duplicate 'red' is ignored
print(colors)    # {'red', 'green', 'blue'}  (order may vary)

# Set operations
a_set = {1, 2, 3, 4}
b_set = {3, 4, 5, 6}

print(a_set | b_set)    # Union:        {1, 2, 3, 4, 5, 6}
print(a_set & b_set)    # Intersection: {3, 4}
print(a_set - b_set)    # Difference:   {1, 2}
print(a_set ^ b_set)    # Symmetric difference: {1, 2, 5, 6}


# ------------------------------------------------------------------------------
# Example 7: Dictionaries
# Concept: key-value store (hash map), CRUD operations
# ------------------------------------------------------------------------------
print("--- Example 7: Dictionaries ---")

student = {
    "name": "Bob",
    "age": 22,
    "gpa": 3.5,
    "courses": ["Math", "CS101"]
}

# Read
print(student["name"])                # Bob
print(student.get("major", "N/A"))   # N/A  (safe get with default)

# Write / Update
student["email"] = "bob@school.edu"   # add new key
student["age"] = 23                   # update existing key
student.update({"gpa": 3.6, "year": 3})  # bulk update

# Delete
del student["year"]
removed = student.pop("email", None)  # pop with default avoids KeyError

# Iteration
for key, value in student.items():
    print(f"  {key}: {value}")

print(list(student.keys()))    # ['name', 'age', 'gpa', 'courses']
print(list(student.values()))  # ['Bob', 23, 3.6, ['Math', 'CS101']]
print("name" in student)       # True


# ------------------------------------------------------------------------------
# Example 8: Conditional Statements (if / elif / else)
# Concept: branching logic, comparison operators, ternary expression
# ------------------------------------------------------------------------------
print("--- Example 8: Conditionals ---")

score = 78

# Standard if/elif/else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} → Grade {grade}")   # Score 78 → Grade C

# Ternary (one-liner if/else)
status = "Pass" if score >= 60 else "Fail"
print(status)   # Pass

# Chained comparisons (Pythonic!)
temperature = 22
if 18 <= temperature <= 26:
    print("Comfortable temperature")   # prints this

# Logical operators
x, y = True, False
print(x and y)   # False
print(x or y)    # True
print(not x)     # False


# ------------------------------------------------------------------------------
# Example 9: Loops — for & while
# Concept: iteration, range(), enumerate(), break, continue
# ------------------------------------------------------------------------------
print("--- Example 9: Loops ---")

# Basic for loop over a list
animals = ["cat", "dog", "rabbit"]
for animal in animals:
    print(animal)

# range(start, stop, step)
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i, end=" ")
print()

# enumerate() — get index AND value
for index, animal in enumerate(animals, start=1):
    print(f"{index}. {animal}")
# 1. cat
# 2. dog
# 3. rabbit

# while loop
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print()  # 5 4 3 2 1

# break and continue
for n in range(10):
    if n == 3:
        continue    # skip 3
    if n == 7:
        break       # stop at 7
    print(n, end=" ")
print()  # 0 1 2 4 5 6

# for/else — else runs if loop completed without break
for i in range(5):
    pass
else:
    print("Loop finished normally")   # prints


# ------------------------------------------------------------------------------
# Example 10: User Input & Type Conversion
# Concept: input(), type casting, basic validation
# ------------------------------------------------------------------------------
print("--- Example 10: User Input & Type Conversion ---")

# NOTE: We simulate input here rather than blocking execution
simulated_input = "25"

# In a real program:  age = input("Enter your age: ")
age_str = simulated_input
age_int = int(age_str)       # cast str → int
print(f"Next year you will be {age_int + 1}")   # 26

# Common type conversions
print(int("42"))         # 42
print(float("3.14"))     # 3.14
print(str(100))          # '100'
print(bool(0))           # False
print(bool(1))           # True
print(bool(""))          # False
print(bool("hello"))     # True

# Safe conversion using try/except
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None

print(safe_int("123"))   # 123
print(safe_int("abc"))   # None


# ==============================================================================
# TIER 2 — BEGINNER+ (Examples 11–20)
# Functions, comprehensions, common algorithms, modules
# ==============================================================================

# ------------------------------------------------------------------------------
# Example 11: Functions — Basics, Default Args & Docstrings
# Concept: def, return, default parameters, docstrings
# ------------------------------------------------------------------------------
print("--- Example 11: Functions ---")

def greet(name, greeting="Hello"):
    """
    Return a formatted greeting string.

    Args:
        name (str): The person's name.
        greeting (str): The greeting word (default: 'Hello').

    Returns:
        str: A formatted greeting.
    """
    return f"{greeting}, {name}!"

print(greet("Alice"))               # Hello, Alice!
print(greet("Bob", "Good morning")) # Good morning, Bob!

# *args — variable positional arguments
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4, 5))   # 15

# **kwargs — variable keyword arguments
def build_profile(**info):
    return {key: value for key, value in info.items()}

profile = build_profile(name="Carol", role="Engineer", level=3)
print(profile)   # {'name': 'Carol', 'role': 'Engineer', 'level': 3}

# Combining: def func(pos, *args, key=default, **kwargs)


# ------------------------------------------------------------------------------
# Example 12: List Comprehensions & Generator Expressions
# Concept: concise, Pythonic loops that produce lists or lazy generators
# ------------------------------------------------------------------------------
print("--- Example 12: List Comprehensions & Generators ---")

# Basic: [expression for item in iterable]
squares = [x ** 2 for x in range(1, 11)]
print(squares)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(20) if x % 2 == 0]
print(evens)     # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Nested (equivalent to nested for loops)
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]
print(pairs)     # [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

# Dictionary comprehension
word = "banana"
char_count = {char: word.count(char) for char in set(word)}
print(char_count)  # {'b':1, 'a':3, 'n':2}  (order may vary)

# Set comprehension
unique_lengths = {len(w) for w in ["cat", "dog", "elephant", "ant"]}
print(unique_lengths)   # {3, 8}

# Generator expression — lazy, memory-efficient (use () not [])
gen = (x ** 2 for x in range(1_000_000))  # no list stored in memory
print(next(gen))  # 0
print(next(gen))  # 1


# ------------------------------------------------------------------------------
# Example 13: Recursion
# Concept: functions calling themselves, base case, call stack
# ------------------------------------------------------------------------------
print("--- Example 13: Recursion ---")

def factorial(n):
    """Return n! (n factorial) recursively."""
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)  # recursive case

print(factorial(5))    # 120  (5*4*3*2*1)
print(factorial(10))   # 3628800

def fibonacci(n):
    """Return the nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Note: naive recursion is O(2^n) — use memoization for large n
print([fibonacci(i) for i in range(10)])  # [0,1,1,2,3,5,8,13,21,34]

# Recursion with memoization using functools.lru_cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_fast(n):
    if n <= 1:
        return n
    return fib_fast(n - 1) + fib_fast(n - 2)

print(fib_fast(50))   # 12586269025  (instant vs. billions of calls without cache)


# ------------------------------------------------------------------------------
# Example 14: Sorting & Searching Algorithms
# Concept: built-in sort, custom key, binary search
# ------------------------------------------------------------------------------
print("--- Example 14: Sorting & Searching ---")

# Python's built-in sort (Timsort — O(n log n))
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = sorted(numbers)          # returns new list
numbers.sort()                         # sorts in place
print(sorted_nums)    # [11, 12, 22, 25, 34, 64, 90]

# Custom sort key
words = ["banana", "apple", "kiwi", "cherry"]
words.sort(key=len)                    # sort by string length
print(words)   # ['kiwi', 'apple', 'banana', 'cherry']

words.sort(key=lambda w: (-len(w), w))  # longest first, alphabetical tie-break
print(words)   # ['banana', 'cherry', 'apple', 'kiwi']

# Sort list of dicts
students = [{"name": "Bob", "gpa": 3.5}, {"name": "Alice", "gpa": 3.9},
            {"name": "Carol", "gpa": 3.1}]
students.sort(key=lambda s: s["gpa"], reverse=True)
print([s["name"] for s in students])   # ['Alice', 'Bob', 'Carol']

# Binary search (list must be sorted first!)
import bisect
data = [1, 3, 5, 7, 9, 11, 13]
index = bisect.bisect_left(data, 7)     # index where 7 is / would be
print(index)   # 3
print(data[index])  # 7


# ------------------------------------------------------------------------------
# Example 15: File I/O — Reading & Writing Text Files
# Concept: open(), context manager (with), read/write/append modes
# ------------------------------------------------------------------------------
print("--- Example 15: File I/O ---")

import os

filename = "/tmp/students.txt"

# Writing — 'w' creates or overwrites
with open(filename, "w", encoding="utf-8") as f:
    f.write("Alice,90\n")
    f.write("Bob,85\n")
    f.writelines(["Carol,92\n", "Dave,78\n"])

# Reading entire file as a string
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# Reading line by line (memory-efficient for large files)
with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        name, score = line.strip().split(",")
        print(f"{name} scored {score}")

# Appending
with open(filename, "a", encoding="utf-8") as f:
    f.write("Eve,95\n")

# Reading all lines into a list
with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"Total students: {len(lines)}")   # 5

os.remove(filename)   # cleanup


# ------------------------------------------------------------------------------
# Example 16: Exception Handling
# Concept: try/except/else/finally, raising exceptions, custom exceptions
# ------------------------------------------------------------------------------
print("--- Example 16: Exception Handling ---")

# Basic try/except
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    else:
        # Runs only if NO exception occurred
        print(f"{a} / {b} = {result}")
        return result
    finally:
        # ALWAYS runs, even if exception was raised
        print("divide() call complete.")

divide(10, 2)    # 10 / 2 = 5.0 → divide() call complete.
divide(10, 0)    # Error: Cannot divide by zero! → divide() call complete.

# Raising exceptions
def set_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be int, got {type(age).__name__}")
    if age < 0 or age > 150:
        raise ValueError(f"Age {age} is out of valid range (0–150)")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)   # Age -5 is out of valid range (0–150)

# Custom exception class
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        super().__init__(f"Cannot withdraw ${amount:.2f}; balance is ${balance:.2f}")
        self.amount = amount
        self.balance = balance

try:
    raise InsufficientFundsError(500, 200)
except InsufficientFundsError as e:
    print(e)


# ------------------------------------------------------------------------------
# Example 17: Lambda Functions & Functional Tools
# Concept: lambda, map(), filter(), reduce()
# ------------------------------------------------------------------------------
print("--- Example 17: Lambda, map, filter, reduce ---")

from functools import reduce

# Lambda: anonymous one-expression function
square = lambda x: x ** 2
print(square(9))   # 81

# map() — apply function to each element, returns iterator
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)     # [1, 4, 9, 16, 25]

# Equivalent list comprehension (preferred in modern Python)
squared = [x ** 2 for x in numbers]

# filter() — keep elements where function returns True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)       # [2, 4]

# reduce() — accumulate a single result
product = reduce(lambda acc, x: acc * x, numbers)
print(product)     # 120  (1*2*3*4*5)

# Practical: sort by multiple criteria using lambda
data = [("Alice", 85), ("Bob", 92), ("Carol", 85), ("Dave", 78)]
data.sort(key=lambda row: (-row[1], row[0]))   # sort by score desc, name asc
print(data)   # [('Bob', 92), ('Alice', 85), ('Carol', 85), ('Dave', 78)]


# ------------------------------------------------------------------------------
# Example 18: Working with CSV and JSON
# Concept: csv module, json module, serialization/deserialization
# ------------------------------------------------------------------------------
print("--- Example 18: CSV and JSON ---")

import csv
import json

csv_file = "/tmp/data.csv"

# Writing CSV
rows = [
    ["name", "age", "city"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Chicago"],
]
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# Reading CSV as list of dicts (DictReader is very convenient)
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(dict(row))   # {'name': 'Alice', 'age': '30', 'city': 'New York'}

os.remove(csv_file)

# JSON serialization (Python object → JSON string)
person = {"name": "Carol", "age": 28, "skills": ["Python", "SQL"]}
json_str = json.dumps(person, indent=2)
print(json_str)

# JSON deserialization (JSON string → Python object)
data = json.loads(json_str)
print(data["skills"])   # ['Python', 'SQL']
print(type(data))       # <class 'dict'>

# Write/read JSON file
json_file = "/tmp/person.json"
with open(json_file, "w") as f:
    json.dump(person, f, indent=2)
with open(json_file, "r") as f:
    loaded = json.load(f)
print(loaded["name"])   # Carol
os.remove(json_file)


# ------------------------------------------------------------------------------
# Example 19: Regular Expressions
# Concept: pattern matching, re module, search/match/findall/sub
# ------------------------------------------------------------------------------
print("--- Example 19: Regular Expressions ---")

import re

text = "Contact us at support@example.com or sales@company.org for info."

# re.findall — return all non-overlapping matches as a list
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)   # ['support@example.com', 'sales@company.org']

# re.search — find first match anywhere in string
phone_text = "Call 555-867-5309 or 555-123-4567"
match = re.search(r"\d{3}-\d{3}-\d{4}", phone_text)
if match:
    print(match.group())   # 555-867-5309

# re.findall all phone numbers
phones = re.findall(r"\d{3}-\d{3}-\d{4}", phone_text)
print(phones)   # ['555-867-5309', '555-123-4567']

# re.sub — replace matches
cleaned = re.sub(r"\s+", " ", "too   many    spaces")
print(cleaned)   # 'too many spaces'

# Groups — extract parts of a match
date_str = "2025-03-15"
m = re.match(r"(\d{4})-(\d{2})-(\d{2})", date_str)
if m:
    year, month, day = m.groups()
    print(f"Year={year}, Month={month}, Day={day}")

# Compiled pattern for repeated use (more efficient)
pattern = re.compile(r"\b[A-Z][a-z]+\b")   # capitalized words
names_found = pattern.findall("Alice and Bob met Carol in Dallas.")
print(names_found)   # ['Alice', 'Bob', 'Carol', 'Dallas']


# ------------------------------------------------------------------------------
# Example 20: Modules, Packages & the Standard Library
# Concept: import styles, datetime, random, collections, itertools
# ------------------------------------------------------------------------------
print("--- Example 20: Modules & Standard Library ---")

import datetime
import random
from collections import Counter, defaultdict, deque
import itertools

# datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M"))   # e.g. 2025-03-15 14:30
birthday = datetime.date(1995, 7, 4)
age_days = (datetime.date.today() - birthday).days
print(f"Age in days: {age_days}")

# random
random.seed(42)   # for reproducibility in teaching
print(random.randint(1, 100))      # random int 1–100
print(random.choice(["a", "b", "c"]))  # random element
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)
print(random.sample(items, 3))     # 3 unique random elements

# Counter — frequency map
words_list = "the quick brown fox jumps over the lazy dog the".split()
counter = Counter(words_list)
print(counter.most_common(3))   # [('the', 3), ('quick', 1), ...]

# defaultdict — no KeyError on missing keys
dd = defaultdict(list)
for k, v in [("a", 1), ("b", 2), ("a", 3)]:
    dd[k].append(v)
print(dict(dd))   # {'a': [1, 3], 'b': [2]}

# deque — efficient append/pop from both ends
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(list(dq))    # [0, 1, 2, 3, 4]
dq.popleft()
print(list(dq))    # [1, 2, 3, 4]

# itertools
print(list(itertools.combinations("ABC", 2)))   # [('A','B'),('A','C'),('B','C')]
print(list(itertools.permutations("AB", 2)))    # [('A','B'),('B','A')]


# ==============================================================================
# TIER 3 — INTERMEDIATE (Examples 21–30)
# OOP, properties, dunder methods, context managers, dataclasses
# ==============================================================================

# ------------------------------------------------------------------------------
# Example 21: Classes & Object-Oriented Programming (OOP) Basics
# Concept: class, __init__, instance methods, self
# ------------------------------------------------------------------------------
print("--- Example 21: OOP Basics ---")

class BankAccount:
    """Represents a simple bank account."""

    bank_name = "PyBank"   # class attribute (shared by all instances)

    def __init__(self, owner, balance=0.0):
        self.owner = owner          # instance attributes
        self._balance = balance     # _prefix = "protected by convention"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError(amount, self._balance)
        self._balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")

    def get_balance(self):
        return self._balance

    def __str__(self):
        """Human-readable representation."""
        return f"{self.bank_name} Account | Owner: {self.owner} | Balance: ${self._balance:.2f}"

    def __repr__(self):
        """Developer representation."""
        return f"BankAccount(owner={self.owner!r}, balance={self._balance!r})"

acc = BankAccount("Alice", 1000)
acc.deposit(250)
acc.withdraw(100)
print(acc)         # PyBank Account | Owner: Alice | Balance: $1150.00
print(repr(acc))   # BankAccount(owner='Alice', balance=1150.0)


# ------------------------------------------------------------------------------
# Example 22: Inheritance & Polymorphism
# Concept: subclassing, super(), method overriding, isinstance
# ------------------------------------------------------------------------------
print("--- Example 22: Inheritance & Polymorphism ---")

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def __str__(self):
        return f"Animal({self.name})"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")  # call parent __init__
        self.breed = breed

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"

    def __str__(self):
        return f"Dog({self.name}, {self.breed})"

class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Meow")
        self.indoor = indoor

    def speak(self):
        # Override parent method
        return f"{self.name} says {self.sound}... and ignores you."

# Polymorphism — same interface, different behavior
animals = [Dog("Rex", "Labrador"), Cat("Whiskers"), Animal("Bird", "Tweet")]
for a in animals:
    print(a.speak())    # each calls its own version of speak()

rex = Dog("Rex", "Labrador")
print(isinstance(rex, Dog))     # True
print(isinstance(rex, Animal))  # True — rex IS-A Animal
print(isinstance(rex, Cat))     # False


# ------------------------------------------------------------------------------
# Example 23: Properties, Getters & Setters
# Concept: @property decorator, encapsulation without verbosity
# ------------------------------------------------------------------------------
print("--- Example 23: Properties ---")

class Temperature:
    """Stores temperature in Celsius, exposes Fahrenheit via property."""

    def __init__(self, celsius=0):
        self._celsius = celsius   # store internally in Celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Computed property — no stored value."""
        return (self._celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9   # convert and use celsius setter

    def __str__(self):
        return f"{self._celsius:.2f}°C / {self.fahrenheit:.2f}°F"

t = Temperature(100)
print(t)                   # 100.00°C / 212.00°F
t.fahrenheit = 32
print(t)                   # 0.00°C / 32.00°F
t.celsius = -300           # raises ValueError


# ------------------------------------------------------------------------------
# Example 24: Dunder (Magic) Methods
# Concept: __len__, __getitem__, __contains__, __add__, __eq__, __lt__
# ------------------------------------------------------------------------------
print("--- Example 24: Dunder Methods ---")

class Vector:
    """2D mathematical vector with operator overloading."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5   # magnitude

    def __len__(self):
        return 2   # always 2D

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)   # (4, 6)
print(v2 - v1)   # (2, 2)
print(v1 * 3)    # (3, 6)
print(v1 == Vector(1, 2))  # True
print(abs(v2))   # 5.0
print(len(v1))   # 2


# ------------------------------------------------------------------------------
# Example 25: Context Managers (__enter__ / __exit__ & contextlib)
# Concept: with statement, resource management, contextlib.contextmanager
# ------------------------------------------------------------------------------
print("--- Example 25: Context Managers ---")

from contextlib import contextmanager
import time

# Custom context manager as a class
class Timer:
    """Measures execution time of a block."""

    def __enter__(self):
        self.start = time.perf_counter()
        return self                     # bound to 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f}s")
        return False                    # False = don't suppress exceptions

with Timer() as t:
    total = sum(range(1_000_000))
# Elapsed: ~0.05s (depends on system)

# Context manager using @contextmanager generator
@contextmanager
def managed_resource(name):
    print(f"Acquiring resource: {name}")
    resource = {"name": name, "data": []}
    try:
        yield resource                  # 'with' block runs here
    except Exception as e:
        print(f"Error during use: {e}")
        raise
    finally:
        print(f"Releasing resource: {name}")

with managed_resource("database_connection") as conn:
    conn["data"].append("query result")
    print(conn)


# ------------------------------------------------------------------------------
# Example 26: Dataclasses
# Concept: @dataclass, automatic __init__/__repr__/__eq__, field(), frozen
# ------------------------------------------------------------------------------
print("--- Example 26: Dataclasses ---")

from dataclasses import dataclass, field, asdict
from typing import List

@dataclass
class Point:
    x: float
    y: float = 0.0   # default value

    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

@dataclass(order=True)   # enables <, >, <=, >=
class Student:
    # sort_index is used for comparison; exclude from repr
    sort_index: float = field(init=False, repr=False)
    name: str
    gpa: float
    courses: List[str] = field(default_factory=list)   # mutable default

    def __post_init__(self):
        self.sort_index = self.gpa   # compare by GPA

@dataclass(frozen=True)   # immutable — instances are hashable
class Color:
    r: int
    g: int
    b: int

p = Point(3, 4)
print(p)                          # Point(x=3, y=4.0)
print(p.distance_to_origin())     # 5.0

s1 = Student("Alice", 3.9, ["CS", "Math"])
s2 = Student("Bob", 3.5)
print(s1 > s2)    # True (GPA 3.9 > 3.5)
print(asdict(s1)) # {'name': 'Alice', 'gpa': 3.9, 'sort_index': 3.9, 'courses': ['CS', 'Math']}

red = Color(255, 0, 0)
# red.r = 128  # FrozenInstanceError!
print(red)    # Color(r=255, g=0, b=0)


# ------------------------------------------------------------------------------
# Example 27: Iterators & the Iterator Protocol
# Concept: __iter__, __next__, StopIteration, custom iterables
# ------------------------------------------------------------------------------
print("--- Example 27: Iterators ---")

class CountUp:
    """Iterator that counts from start to stop."""

    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self     # iterator IS the iterable here

    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

counter = CountUp(1, 5)
for n in counter:
    print(n, end=" ")   # 1 2 3 4 5
print()

# iter() and next() on built-in types
my_list = [10, 20, 30]
it = iter(my_list)
print(next(it))   # 10
print(next(it))   # 20
print(next(it))   # 30
# next(it)        # would raise StopIteration

# Infinite iterator — use with care!
class InfiniteCounter:
    def __init__(self):
        self.n = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.n += 1
        return self.n

inf = InfiniteCounter()
first_five = [next(inf) for _ in range(5)]
print(first_five)   # [1, 2, 3, 4, 5]


# ------------------------------------------------------------------------------
# Example 28: Generators
# Concept: yield, generator functions vs. classes, send(), pipelines
# ------------------------------------------------------------------------------
print("--- Example 28: Generators ---")

def count_up(start, stop):
    """Generator version of CountUp — much cleaner."""
    current = start
    while current <= stop:
        yield current   # suspends here, resumes on next()
        current += 1

gen = count_up(1, 5)
print(list(gen))   # [1, 2, 3, 4, 5]

# Infinite Fibonacci generator
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_gen()
print([next(fib) for _ in range(10)])  # [0,1,1,2,3,5,8,13,21,34]

# Generator pipeline — lazy, memory-efficient
def read_numbers(data):
    for n in data:
        yield n

def square_gen(numbers):
    for n in numbers:
        yield n ** 2

def filter_evens(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

raw = range(1, 11)
pipeline = filter_evens(square_gen(read_numbers(raw)))
print(list(pipeline))   # [4, 16, 36, 64, 100]


# ------------------------------------------------------------------------------
# Example 29: Type Hints & Static Type Checking
# Concept: PEP 484, typing module, Optional, Union, generics
# ------------------------------------------------------------------------------
print("--- Example 29: Type Hints ---")

from typing import Optional, Union, Dict, Tuple, Callable, Any
# Python 3.10+ can also use: str | None  instead of Optional[str]

def greet_typed(name: str, times: int = 1) -> str:
    """Type-hinted function — hints don't enforce at runtime."""
    return (f"Hello, {name}! " * times).strip()

def find_student(db: Dict[str, float], name: str) -> Optional[float]:
    """Returns GPA or None if not found."""
    return db.get(name)   # returns None if key missing

def process(value: Union[int, float, str]) -> str:
    """Accepts int, float, or str."""
    return str(value).upper()

# Type aliases
Vector2D = Tuple[float, float]
Transform = Callable[[float], float]

def apply(func: Transform, value: float) -> float:
    return func(value)

print(greet_typed("Alice", 2))   # Hello, Alice! Hello, Alice!

db: Dict[str, float] = {"Alice": 3.9, "Bob": 3.5}
print(find_student(db, "Alice"))  # 3.9
print(find_student(db, "Eve"))    # None

print(apply(lambda x: x * 2, 5.0))  # 10.0

# Runtime type inspection is separate (use isinstance())
# Use mypy or pyright to check types statically:  mypy script.py


# ------------------------------------------------------------------------------
# Example 30: Abstract Base Classes & Interfaces
# Concept: abc module, ABC, @abstractmethod, enforcing contracts
# ------------------------------------------------------------------------------
print("--- Example 30: Abstract Base Classes ---")

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class — cannot be instantiated directly."""

    @abstractmethod
    def area(self) -> float:
        """Subclasses MUST implement area()."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def describe(self) -> str:
        """Concrete method available to all subclasses."""
        return (f"{type(self).__name__}: "
                f"area={self.area():.2f}, perimeter={self.perimeter():.2f}")

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(s.describe())
# Circle: area=78.54, perimeter=31.42
# Rectangle: area=24.00, perimeter=20.00

# Shape()   # TypeError: Can't instantiate abstract class Shape


# ==============================================================================
# TIER 4 — ADVANCED (Examples 31–40)
# Decorators, closures, slots, enums, protocols, pathlib, logging
# ==============================================================================

# ------------------------------------------------------------------------------
# Example 31: Closures & Decorators
# Concept: nested functions, closures, @decorator syntax, wraps()
# ------------------------------------------------------------------------------
print("--- Example 31: Closures & Decorators ---")

from functools import wraps

# Closure — inner function "closes over" outer variable
def make_multiplier(factor):
    """Returns a function that multiplies its input by factor."""
    def multiplier(x):
        return x * factor   # 'factor' is captured from the enclosing scope
    return multiplier

triple = make_multiplier(3)
print(triple(7))    # 21
print(triple(10))   # 30

# Basic decorator — a function that wraps another function
def log_calls(func):
    @wraps(func)   # preserves original function metadata
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls   # syntactic sugar for: add = log_calls(add)
def add(a, b):
    return a + b

add(3, 4)
# Calling add((3, 4), {})
# add returned 7

# Decorator with parameters
def repeat(n):
    """Decorator factory — returns a decorator."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say(msg):
    print(msg)

say("Hello!")   # prints "Hello!" 3 times


# ------------------------------------------------------------------------------
# Example 32: Caching & Memoization
# Concept: lru_cache, cache, manual memoization, performance
# ------------------------------------------------------------------------------
print("--- Example 32: Caching & Memoization ---")

from functools import lru_cache, cache
import time

# Manual memoization using a dict
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# Better: @lru_cache (Least Recently Used — bounded cache)
@lru_cache(maxsize=128)
def fib_lru(n):
    if n <= 1:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)

# @cache (Python 3.9+) — unbounded, simplest option
@cache
def fib_cache(n):
    if n <= 1:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)

# Timing comparison
start = time.perf_counter()
print(fib_lru(40))
print(f"lru_cache: {time.perf_counter() - start:.6f}s")

# Inspect cache stats
print(fib_lru.cache_info())
# CacheInfo(hits=38, misses=41, maxsize=128, currsize=41)

fib_lru.cache_clear()  # clear the cache if needed


# ------------------------------------------------------------------------------
# Example 33: Enumerations
# Concept: enum.Enum, IntEnum, auto(), Flag
# ------------------------------------------------------------------------------
print("--- Example 33: Enumerations ---")

from enum import Enum, IntEnum, auto, Flag

class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST  = "E"
    WEST  = "W"

print(Direction.NORTH)        # Direction.NORTH
print(Direction.NORTH.value)  # N
print(Direction.NORTH.name)   # NORTH
print(Direction("S"))         # Direction.SOUTH  (lookup by value)

# auto() assigns sequential int values automatically
class Color(Enum):
    RED   = auto()   # 1
    GREEN = auto()   # 2
    BLUE  = auto()   # 3

print(list(Color))   # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]

# IntEnum — members are also integers
class Priority(IntEnum):
    LOW    = 1
    MEDIUM = 2
    HIGH   = 3

print(Priority.HIGH > Priority.LOW)   # True (int comparison works)

# Flag — for bitmask permissions
class Permission(Flag):
    READ    = auto()   # 1
    WRITE   = auto()   # 2
    EXECUTE = auto()   # 4
    ALL     = READ | WRITE | EXECUTE

user_perms = Permission.READ | Permission.WRITE
print(user_perms)                            # Permission.READ|WRITE
print(Permission.READ in user_perms)         # True
print(Permission.EXECUTE in user_perms)      # False


# ------------------------------------------------------------------------------
# Example 34: __slots__ & Memory Optimization
# Concept: __slots__ to reduce per-instance memory, faster attribute access
# ------------------------------------------------------------------------------
print("--- Example 34: __slots__ ---")

import sys

class PointDict:
    """Regular class — stores attributes in a __dict__."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointSlots:
    """Uses __slots__ — no __dict__, lower memory footprint."""
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

pd = PointDict(1, 2)
ps = PointSlots(1, 2)

print(sys.getsizeof(pd.__dict__))   # ~232 bytes (includes dict overhead)
# ps has no __dict__:
try:
    print(ps.__dict__)
except AttributeError:
    print("PointSlots has no __dict__ (slots only)")

# Benchmark: for 1 million instances, __slots__ uses ~50-70% less RAM
# and attribute access is ~20% faster.

# Caveat: you cannot add arbitrary attributes to slotted instances
# ps.z = 3   # AttributeError!


# ------------------------------------------------------------------------------
# Example 35: Pathlib — Modern File System Handling
# Concept: pathlib.Path, replacing os.path, cross-platform paths
# ------------------------------------------------------------------------------
print("--- Example 35: Pathlib ---")

from pathlib import Path

# Create Path objects
home = Path.home()
cwd  = Path.cwd()
tmp  = Path("/tmp")

# Build paths with / operator
data_dir = tmp / "my_project" / "data"
data_dir.mkdir(parents=True, exist_ok=True)   # mkdir -p equivalent

# Write and read files
readme = data_dir / "readme.txt"
readme.write_text("Hello from pathlib!\nLine 2.", encoding="utf-8")
print(readme.read_text())

# Path components
print(readme.name)       # readme.txt
print(readme.stem)       # readme
print(readme.suffix)     # .txt
print(readme.parent)     # /tmp/my_project/data

# Glob — find files
py_files = list(Path(".").rglob("*.py"))   # all .py files recursively
print(f"Found {len(py_files)} .py files in current tree")

# Checking existence and type
print(readme.exists())    # True
print(readme.is_file())   # True
print(data_dir.is_dir())  # True

# Iterating directory contents
for item in data_dir.iterdir():
    print(item)

# Rename, move, delete
new_path = data_dir / "README.txt"
readme.rename(new_path)
new_path.unlink()            # delete file
data_dir.rmdir()             # remove empty directory
(tmp / "my_project").rmdir()


# ------------------------------------------------------------------------------
# Example 36: Logging
# Concept: logging module, levels, handlers, formatters, best practices
# ------------------------------------------------------------------------------
print("--- Example 36: Logging ---")

import logging

# Basic configuration — logs to console
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S"
)

logger = logging.getLogger("my_app")

logger.debug("Debug message — verbose diagnostic info")
logger.info("Info message — normal operational message")
logger.warning("Warning — something unexpected but not fatal")
logger.error("Error — a serious problem occurred")
logger.critical("Critical — application may not continue")

# File handler — log to a file simultaneously
file_handler = logging.FileHandler("/tmp/app.log")
file_handler.setLevel(logging.ERROR)  # only ERROR and above to file
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.error("This goes to both console and file")
Path("/tmp/app.log").unlink(missing_ok=True)   # cleanup

# Best practice: use module-level loggers, not root logger
# Best practice: never use print() for diagnostic output in libraries


# ------------------------------------------------------------------------------
# Example 37: Comprehension Mastery & zip/enumerate Tricks
# Concept: advanced unpacking, zip, enumerate, walrus operator
# ------------------------------------------------------------------------------
print("--- Example 37: Advanced Iteration Tricks ---")

# zip — iterate multiple iterables in parallel
names  = ["Alice", "Bob", "Carol"]
scores = [92, 85, 88]
grades = ["A", "B", "B+"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name}: {score} ({grade})")

# zip creates tuples — use dict() to make a mapping
score_map = dict(zip(names, scores))
print(score_map)   # {'Alice': 92, 'Bob': 85, 'Carol': 88}

# zip_longest — pads shorter iterables with fillvalue
from itertools import zip_longest
for a, b in zip_longest([1, 2, 3], ["x", "y"], fillvalue=None):
    print(a, b)

# Walrus operator (:=) — assign and test in one expression (Python 3.8+)
data = [4, 7, 2, 9, 1, 5, 8]
filtered = [y for x in data if (y := x * 2) > 10]
print(filtered)   # [14, 18, 16]

# Unpacking with *
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)   # 1 [2, 3, 4] 5

# Transposing a matrix using zip(*matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [list(row) for row in zip(*matrix)]
print(transposed)   # [[1,4,7],[2,5,8],[3,6,9]]


# ------------------------------------------------------------------------------
# Example 38: Protocol & Structural Subtyping (Duck Typing Formalized)
# Concept: typing.Protocol, structural typing, @runtime_checkable
# ------------------------------------------------------------------------------
print("--- Example 38: Protocols (Structural Typing) ---")

from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    """Any class with a draw() method satisfies this protocol."""
    def draw(self) -> str:
        ...

class Circle2:
    def __init__(self, radius):
        self.radius = radius
    def draw(self) -> str:
        return f"○ Circle(r={self.radius})"

class Square:
    def __init__(self, side):
        self.side = side
    def draw(self) -> str:
        return f"□ Square(s={self.side})"

class TextLabel:
    """Does NOT implement draw()."""
    def __init__(self, text):
        self.text = text

def render_all(items):
    for item in items:
        if isinstance(item, Drawable):
            print(item.draw())
        else:
            print(f"Skipping {type(item).__name__} — not Drawable")

shapes = [Circle2(5), Square(3), TextLabel("Hello")]
render_all(shapes)
# ○ Circle(r=5)
# □ Square(s=3)
# Skipping TextLabel — not Drawable

# Key insight: Circle2 and Square never inherit from Drawable —
# they satisfy the protocol purely by having the right methods.
# This is "structural subtyping" (Go-style interfaces in Python).


# ------------------------------------------------------------------------------
# Example 39: Functools & Operator Tools
# Concept: partial, reduce, attrgetter, itemgetter, methodcaller
# ------------------------------------------------------------------------------
print("--- Example 39: functools & operator ---")

from functools import partial
from operator import attrgetter, itemgetter, methodcaller

# partial — fix some arguments of a function
def power(base, exponent):
    return base ** exponent

square_fn = partial(power, exponent=2)
cube_fn   = partial(power, exponent=3)

print(square_fn(5))   # 25
print(cube_fn(3))     # 27

# Partial with print (useful for callbacks)
print_tab = partial(print, sep="\t", end="\n")
print_tab("col1", "col2", "col3")   # col1	col2	col3

# itemgetter — faster than lambda for key functions
records = [{"name": "Bob", "age": 25}, {"name": "Alice", "age": 30}]
records.sort(key=itemgetter("name"))
print([r["name"] for r in records])   # ['Alice', 'Bob']

# attrgetter — access object attributes
from dataclasses import dataclass as dc
@dc
class Emp:
    name: str
    salary: float

employees = [Emp("Charlie", 75000), Emp("Alice", 90000), Emp("Bob", 82000)]
employees.sort(key=attrgetter("salary"), reverse=True)
print([e.name for e in employees])   # ['Alice', 'Bob', 'Charlie']

# methodcaller — call a named method on each element
words2 = ["hello", "WORLD", "Python"]
upper_words = list(map(methodcaller("upper"), words2))
print(upper_words)   # ['HELLO', 'WORLD', 'PYTHON']


# ------------------------------------------------------------------------------
# Example 40: Packing/Unpacking, Named Tuples & Structured Data
# Concept: collections.namedtuple, typing.NamedTuple, structured records
# ------------------------------------------------------------------------------
print("--- Example 40: Named Tuples ---")

from collections import namedtuple
from typing import NamedTuple

# Old-style namedtuple
Point3D = namedtuple("Point3D", ["x", "y", "z"])
p = Point3D(1, 2, 3)
print(p)        # Point3D(x=1, y=2, z=3)
print(p.x)      # 1
print(p[0])     # 1  (indexing still works)
x, y, z = p    # unpacking
print(p._asdict())  # OrderedDict([('x', 1), ('y', 2), ('z', 3)])

# New-style (type-hinted, supports defaults)
class Employee(NamedTuple):
    name: str
    department: str
    salary: float = 50000.0   # default value

emp = Employee("Alice", "Engineering", 95000)
print(emp)
print(emp.salary)   # 95000

# Named tuples are immutable (like regular tuples)
# emp.salary = 100000  # AttributeError!

# Use _replace() to create a modified copy
promoted = emp._replace(salary=110000)
print(promoted)

# Great for: return values with multiple fields, CSV rows, DB records


# ==============================================================================
# TIER 5 — EXPERT (Examples 41–50)
# Metaclasses, descriptors, concurrency, testing, design patterns
# ==============================================================================

# ------------------------------------------------------------------------------
# Example 41: Descriptors
# Concept: __get__, __set__, __delete__, reusable attribute logic
# ------------------------------------------------------------------------------
print("--- Example 41: Descriptors ---")

class Validated:
    """
    Reusable descriptor that enforces type and range on numeric attributes.
    Descriptors sit at the class level and intercept attribute access on instances.
    """

    def __set_name__(self, owner, name):
        self.public_name  = name
        self.private_name = "_" + name   # stores actual value here

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self   # class-level access returns the descriptor itself
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.public_name} must be numeric")
        if value < 0:
            raise ValueError(f"{self.public_name} must be non-negative")
        setattr(obj, self.private_name, value)

class Product:
    price    = Validated()
    quantity = Validated()

    def __init__(self, name, price, quantity):
        self.name     = name
        self.price    = price       # calls Validated.__set__
        self.quantity = quantity

    @property
    def total_value(self):
        return self.price * self.quantity

item = Product("Widget", 9.99, 100)
print(item.total_value)   # 999.0

try:
    item.price = -5   # raises ValueError
except ValueError as e:
    print(e)

try:
    item.quantity = "lots"   # raises TypeError
except TypeError as e:
    print(e)


# ------------------------------------------------------------------------------
# Example 42: Metaclasses
# Concept: type, __new__ in metaclass, class creation hooks
# ------------------------------------------------------------------------------
print("--- Example 42: Metaclasses ---")

# type is the metaclass of all classes
print(type(int))    # <class 'type'>
print(type(list))   # <class 'type'>

# Metaclass that auto-registers subclasses in a registry
class PluginMeta(type):
    registry = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if bases:   # skip the base class itself
            mcs.registry[name] = cls
            print(f"  Registered plugin: {name}")
        return cls

class Plugin(metaclass=PluginMeta):
    """Base class — all subclasses auto-register."""
    def run(self):
        raise NotImplementedError

class AuthPlugin(Plugin):
    def run(self):
        return "Running authentication"

class LogPlugin(Plugin):
    def run(self):
        return "Running logging"

print("Registry:", list(PluginMeta.registry.keys()))
# ['AuthPlugin', 'LogPlugin']

# Metaclass that enforces naming conventions
class UpperCaseMeta(type):
    def __new__(mcs, name, bases, namespace):
        for key, value in namespace.items():
            if callable(value) and not key.startswith("_"):
                if key != key.upper():
                    raise TypeError(f"Method '{key}' must be UPPERCASE in {name}")
        return super().__new__(mcs, name, bases, namespace)

# class BadClass(metaclass=UpperCaseMeta):
#     def my_method(self): pass   # would raise TypeError


# ------------------------------------------------------------------------------
# Example 43: Concurrency — Threading
# Concept: threading.Thread, locks, race conditions, thread safety
# ------------------------------------------------------------------------------
print("--- Example 43: Threading ---")

import threading
import time as tm

# Basic threading
def download_file(filename, delay):
    """Simulates downloading a file."""
    print(f"Starting download: {filename}")
    tm.sleep(delay)   # simulate I/O wait
    print(f"Finished download: {filename}")

files = [("report.pdf", 0.1), ("data.csv", 0.05), ("image.png", 0.08)]

start = tm.perf_counter()
threads = []
for fname, delay in files:
    t = threading.Thread(target=download_file, args=(fname, delay))
    threads.append(t)
    t.start()

for t in threads:
    t.join()   # wait for all threads to complete

print(f"All downloads done in {tm.perf_counter() - start:.3f}s")

# Thread safety with Lock — prevent race conditions
counter = 0
lock = threading.Lock()

def increment(n):
    global counter
    for _ in range(n):
        with lock:      # only one thread can hold lock at a time
            counter += 1

threads2 = [threading.Thread(target=increment, args=(1000,)) for _ in range(5)]
for t in threads2: t.start()
for t in threads2: t.join()
print(f"Counter (should be 5000): {counter}")

# NOTE: Python's GIL limits true parallelism in threads for CPU work.
# Use multiprocessing or asyncio for CPU-bound or async I/O tasks.


# ------------------------------------------------------------------------------
# Example 44: Concurrency — asyncio (Async/Await)
# Concept: async def, await, asyncio.gather, event loop
# ------------------------------------------------------------------------------
print("--- Example 44: asyncio ---")

import asyncio

async def fetch_data(source, delay):
    """Coroutine — suspends during I/O without blocking the thread."""
    print(f"Fetching from {source}...")
    await asyncio.sleep(delay)   # non-blocking sleep
    print(f"Got data from {source}")
    return {"source": source, "records": 42}

async def main_async():
    # Run coroutines concurrently
    results = await asyncio.gather(
        fetch_data("database", 0.1),
        fetch_data("API", 0.05),
        fetch_data("cache", 0.02),
    )
    for r in results:
        print(f"  {r['source']}: {r['records']} records")
    return results

# Run the event loop
results = asyncio.run(main_async())

# Async generator
async def async_range(n):
    for i in range(n):
        await asyncio.sleep(0)   # yield control to event loop
        yield i

async def use_async_gen():
    async for val in async_range(5):
        print(val, end=" ")
    print()

asyncio.run(use_async_gen())   # 0 1 2 3 4


# ------------------------------------------------------------------------------
# Example 45: multiprocessing — True Parallelism
# Concept: Process, Pool, shared memory, bypassing GIL
# ------------------------------------------------------------------------------
print("--- Example 45: multiprocessing ---")

from multiprocessing import Pool
import os

def cpu_intensive(n):
    """Compute sum of squares up to n (CPU-bound work)."""
    return sum(i * i for i in range(n))

if __name__ == "__main__":   # REQUIRED guard for multiprocessing on Windows/macOS
    numbers = [10**6, 2*10**6, 3*10**6, 4*10**6]

    # Sequential
    start = tm.perf_counter()
    seq_results = [cpu_intensive(n) for n in numbers]
    print(f"Sequential: {tm.perf_counter() - start:.3f}s")

    # Parallel — uses all CPU cores
    start = tm.perf_counter()
    with Pool() as pool:
        par_results = pool.map(cpu_intensive, numbers)
    print(f"Parallel (Pool): {tm.perf_counter() - start:.3f}s")

    print(seq_results == par_results)   # True — same results, faster


# ------------------------------------------------------------------------------
# Example 46: Design Pattern — Singleton
# Concept: ensure only one instance, metaclass or __new__ approach
# ------------------------------------------------------------------------------
print("--- Example 46: Singleton Pattern ---")

class SingletonMeta(type):
    """Metaclass that enforces the singleton pattern."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, url="sqlite:///default.db"):
        self.url = url
        self.connected = False
        print(f"  DB connection created: {url}")

    def connect(self):
        self.connected = True

db1 = DatabaseConnection("postgres://localhost/mydb")
db2 = DatabaseConnection("should_be_ignored")   # same url as db1

print(db1 is db2)       # True — same object
print(db2.url)          # postgres://localhost/mydb


# ------------------------------------------------------------------------------
# Example 47: Design Pattern — Observer (Event System)
# Concept: loose coupling, subscribers, event-driven architecture
# ------------------------------------------------------------------------------
print("--- Example 47: Observer Pattern ---")

from collections import defaultdict
from typing import Callable

class EventBus:
    """Simple publish/subscribe event system."""

    def __init__(self):
        self._listeners: dict[str, list[Callable]] = defaultdict(list)

    def subscribe(self, event: str, callback: Callable):
        self._listeners[event].append(callback)

    def unsubscribe(self, event: str, callback: Callable):
        self._listeners[event].remove(callback)

    def publish(self, event: str, **data):
        for callback in self._listeners[event]:
            callback(**data)

# Subscribers
def send_email(username, **kwargs):
    print(f"Email: Welcome, {username}!")

def create_profile(username, email, **kwargs):
    print(f"Profile created for {username} ({email})")

def log_event(username, **kwargs):
    print(f"LOG: user_registered event for {username}")

bus = EventBus()
bus.subscribe("user_registered", send_email)
bus.subscribe("user_registered", create_profile)
bus.subscribe("user_registered", log_event)

bus.publish("user_registered", username="Alice", email="alice@example.com")
# Email: Welcome, Alice!
# Profile created for Alice (alice@example.com)
# LOG: user_registered event for Alice


# ------------------------------------------------------------------------------
# Example 48: Design Pattern — Strategy
# Concept: interchangeable algorithms, dependency injection, open/closed principle
# ------------------------------------------------------------------------------
print("--- Example 48: Strategy Pattern ---")

from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        arr = data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

class MergeSort(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        mid   = len(data) // 2
        left  = self.sort(data[:mid])
        right = self.sort(data[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i]); i += 1
            else:
                result.append(right[j]); j += 1
        return result + left[i:] + right[j:]

class BuiltInSort(SortStrategy):
    def sort(self, data):
        return sorted(data)   # Timsort — O(n log n)

class DataProcessor:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def process(self, data):
        return self._strategy.sort(data)

raw = [64, 34, 25, 12, 22, 11, 90]

processor = DataProcessor(BubbleSort())
print(processor.process(raw))   # [11, 12, 22, 25, 34, 64, 90]

processor.set_strategy(MergeSort())
print(processor.process(raw))   # [11, 12, 22, 25, 34, 64, 90]


# ------------------------------------------------------------------------------
# Example 49: Unit Testing with unittest
# Concept: TestCase, assertions, setUp/tearDown, mocking
# ------------------------------------------------------------------------------
print("--- Example 49: Unit Testing ---")

import unittest
from unittest.mock import patch, MagicMock

# Function under test
def celsius_to_fahrenheit(c: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32

def fetch_user_from_db(user_id: int) -> dict:
    """Would normally call a database — we'll mock this."""
    raise NotImplementedError("Real DB call not made in tests")

class TestCelsiusToFahrenheit(unittest.TestCase):

    def test_freezing(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)

    def test_boiling(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0)

    def test_body_temperature(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, places=1)

    def test_negative(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_return_type(self):
        self.assertIsInstance(celsius_to_fahrenheit(20), float)

class TestWithMock(unittest.TestCase):

    @patch("__main__.fetch_user_from_db")
    def test_fetch_user(self, mock_fetch):
        # Set mock return value — no real DB call happens
        mock_fetch.return_value = {"id": 1, "name": "Alice"}

        result = fetch_user_from_db(1)

        mock_fetch.assert_called_once_with(1)
        self.assertEqual(result["name"], "Alice")

# Run tests programmatically
loader  = unittest.TestLoader()
suite   = unittest.TestSuite()
suite.addTests(loader.loadTestsFromTestCase(TestCelsiusToFahrenheit))
suite.addTests(loader.loadTestsFromTestCase(TestWithMock))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)


# ------------------------------------------------------------------------------
# Example 50: Advanced Data Pipeline with Generators & Context Managers
# Concept: combining everything — generator pipeline, dataclass, context manager,
#          type hints, logging, and exception handling in a real-world pattern
# ------------------------------------------------------------------------------
print("--- Example 50: Advanced Data Pipeline ---")

import csv
import io
import logging
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Iterator, Generator

pipeline_logger = logging.getLogger("pipeline")

@dataclass
class Record:
    """Represents a single data record in the pipeline."""
    id:     int
    name:   str
    value:  float
    tags:   list = field(default_factory=list)

    def is_valid(self) -> bool:
        return self.value >= 0 and bool(self.name)

@contextmanager
def pipeline_context(name: str) -> Generator:
    """Context manager that logs pipeline lifecycle and handles errors."""
    pipeline_logger.info(f"Pipeline '{name}' starting")
    stats = {"processed": 0, "skipped": 0, "errors": 0}
    try:
        yield stats
        pipeline_logger.info(
            f"Pipeline '{name}' complete: {stats}"
        )
    except Exception as e:
        pipeline_logger.error(f"Pipeline '{name}' failed: {e}")
        raise

def parse_records(raw_csv: str) -> Iterator[Record]:
    """Generator: parse CSV rows into Record objects lazily."""
    reader = csv.DictReader(io.StringIO(raw_csv))
    for row in reader:
        try:
            yield Record(
                id=int(row["id"]),
                name=row["name"].strip(),
                value=float(row["value"]),
                tags=row.get("tags", "").split("|") if row.get("tags") else []
            )
        except (ValueError, KeyError) as e:
            pipeline_logger.warning(f"Skipping malformed row {row}: {e}")

def validate(records: Iterator[Record]) -> Iterator[Record]:
    """Generator: filter out invalid records."""
    for record in records:
        if record.is_valid():
            yield record

def transform(records: Iterator[Record]) -> Iterator[Record]:
    """Generator: apply transformations to each record."""
    for record in records:
        record.value = round(record.value * 1.1, 2)   # apply 10% uplift
        record.name  = record.name.title()
        yield record

def load(records: Iterator[Record], stats: dict) -> list[Record]:
    """Terminal: materialize the pipeline into a list (simulate DB insert)."""
    results = []
    for record in records:
        results.append(record)
        stats["processed"] += 1
    return results

# Sample data (could come from a file, S3, etc.)
raw_data = """id,name,value,tags
1,alice,100.0,vip|premium
2,bob,-5.0,
3,carol,200.0,vip
4,,300.0,
5,dave,150.0,standard
"""

with pipeline_context("sales_etl") as stats:
    # Build the lazy pipeline — nothing executes yet
    source    = parse_records(raw_data)
    validated = validate(source)
    transformed = transform(validated)

    # Execute pipeline
    output = load(transformed, stats)
    stats["skipped"] = 5 - stats["processed"]   # 5 rows total

for record in output:
    print(f"  {record.id}: {record.name} → ${record.value} {record.tags}")

# OUTPUT:
#   1: Alice → $110.0 ['vip', 'premium']
#   3: Carol → $220.0 ['vip']
#   5: Dave → $165.0 ['standard']
# (bob skipped: negative value; row 4 skipped: empty name)

print("\n" + "=" * 70)
print("  All 50 examples complete. Happy coding!")
print("=" * 70)