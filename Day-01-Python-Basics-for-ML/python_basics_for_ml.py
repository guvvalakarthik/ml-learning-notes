"""
Python Basics for Machine Learning
Author: Guvvala Karthik

This file covers all Python fundamentals required before learning ML.
"""

# -------------------------------
# 1. VARIABLES & DATA TYPES
# -------------------------------

x = 10              # integer
y = 3.5             # float
name = "Karthik"    # string
is_ml_fun = True    # boolean

print(x, y, name, is_ml_fun)

# -------------------------------
# 2. LISTS (VERY IMPORTANT FOR ML)
# -------------------------------

numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[0])        # indexing
print(numbers[-1])       # last element
print(len(numbers))      # length

# List operations
numbers.append(6)
numbers.remove(3)
print(numbers)

# -------------------------------
# 3. TUPLES (IMMUTABLE)
# -------------------------------

dimensions = (64, 128)
print(dimensions)

# -------------------------------
# 4. SETS (UNIQUE VALUES)
# -------------------------------

unique_values = {1, 2, 2, 3, 4}
print(unique_values)

# -------------------------------
# 5. DICTIONARIES (KEY-VALUE PAIRS)
# -------------------------------

student = {
    "name": "Karthik",
    "branch": "CSE",
    "cgpa": 8.5
}

print(student)
print(student["cgpa"])

# -------------------------------
# 6. CONDITIONAL STATEMENTS
# -------------------------------

score = 75

if score >= 90:
    print("Excellent")
elif score >= 60:
    print("Good")
else:
    print("Needs Improvement")

# -------------------------------
# 7. LOOPS
# -------------------------------

# for loop
for i in range(5):
    print(i)

# loop through list
for num in numbers:
    print(num)

# while loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# -------------------------------
# 8. FUNCTIONS (USED EVERYWHERE IN ML)
# -------------------------------

def square(n):
    return n * n

print(square(5))

# Function with default argument
def greet(name="User"):
    print("Hello", name)

greet()
greet("Karthik")

# -------------------------------
# 9. LAMBDA FUNCTIONS (SHORT FUNCTIONS)
# -------------------------------

add = lambda a, b: a + b
print(add(3, 4))

# -------------------------------
# 10. LIST COMPREHENSION (IMPORTANT)
# -------------------------------

squares = [x**2 for x in range(1, 6)]
print(squares)

# -------------------------------
# 11. STRING OPERATIONS
# -------------------------------

text = "machine learning"
print(text.upper())
print(text.lower())
print(text.split())

# -------------------------------
# 12. FILE HANDLING (BASICS)
# -------------------------------

# Writing to a file
with open("sample.txt", "w") as f:
    f.write("Python for Machine Learning")

# Reading from a file
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# -------------------------------
# 13. EXCEPTION HANDLING
# -------------------------------

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# -------------------------------
# 14. MODULES & IMPORTS
# -------------------------------

import math

print(math.sqrt(16))
print(math.pi)

# -------------------------------
# 15. BASIC NUMPY INTRO (PRE-ML)
# -------------------------------

import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr)
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

# -------------------------------
# 16. WHY THIS MATTERS FOR ML
# -------------------------------

"""
- Lists & arrays store datasets
- Loops process data
- Functions define ML logic
- NumPy enables fast numerical computation
- Clean Python = better ML code
"""

print("Python basics for ML completed successfully!")
