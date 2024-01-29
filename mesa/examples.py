#   Here are some examples of each concept:

#   Modulo operator:

print(5 % 2)  # Output: 1

print(7 % 3)  # Output: 1

#   User input/output:

name = input("Enter your name: ")

print("Hello, " + name + "!")

#   Control and conditional statements:

x = 5

if x > 0:

    print("x is positive")

elif x < 0:

    print("x is negative")

else:

    print("x is zero")

#   Loops, iterations, and nesting:
for i in range(3):

    print("Hello, world!")


for i in range(1, 6):

    for j in range(1, 6):

        print(i * j, end=" ")

    print()

#   Boolean Algebra:
print(True and False)  # Output: False

print(True or False)  # Output: True

print(not True)  # Output: False

#   Lists:
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # Output: apple

print(fruits[1:])  # Output: ['banana', 'cherry']

#   Functions and user-defined functions:

def greet(name):

    return "Hello, " + name + "!"


print(greet("Alice"))  # Output: Hello, Alice!

#   Arithmetic:

print(2 + 3)  # Output: 5

print(5 - 2)  # Output: 3

print(3 * 4)  # Output: 12

print(8 / 2)  # Output: 4.0

print(7 // 2)  # Output: 3

print(7 % 2)  # Output: 1

print(2 ** 3)  # Output: 8

#   Order of operations:

print(2 + 3 * 4)  # Output: 14

print(2 * 3 + 4)  # Output: 10

print(2 + 3 ** 2)  # Output: 7

print(2 ** 3 + 4)  # Output: 14

#   Evaluating Expressions and Equations:

import sympy as sp

x = sp.Symbol('x')

expr = x ** 2 + 3 * x + 2

solution = sp.solve(expr, x)

print(solution)  # Output: [-1, 2]

#   Properties of equalities and inequalities:

x = 5

y = 5

z = 7


# Reflexivity

print(x == x)  # Output: True


# Symmetry

print(x == y)  # Output: True

print(y == x)  # Output: True


# Transitivity

print(x == y)  # Output: True

print(y == z)  # Output: False

print(x == z)  # Output: False


# Additive identity

print(0 + x)  # Output: 5


# Multiplicative identity

print(1 * x)  # Output: 5


# Additive inverse

print(x + (-x))  # Output: 0


# Multiplicative inverse

print(1 / x)  # Output: 0.2


# Zero property

print(0 * x)  # Output: 0


# One property

print(1 * x)  # Output: 5


# Trichotomy law

print(x < y)  # Output: False

print(x > y)  # Output: False

print(x == y)  # Output: True


# Inequality reversal

print(x > y)  # Output: False

print(y < x)  # Output: True


# Inequality transitivity

print(x < y)  # Output: False

print(y < z)  # Output: True

print(x < z)  # Output: True


# Inequality with zero

print(0 < x)