"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    """Multiply two numbers with input validation"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b


def divide(a, b):
    """Divide a by b with error handling"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Return a raised to the power of b"""
    return a**b


def square_root(a):
    """Return square root of a (raises ValueError if negative)"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative")
    return math.sqrt(a)


if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
