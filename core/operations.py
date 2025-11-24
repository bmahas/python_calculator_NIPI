# calculator_math.py

def multiply(a, b):
    """
    Returns the product of two numbers.
    """
    if b == 0:
        raise ValueError("Cannot multiply by zero!")
    return a * b


def divide(a, b):
    """
    Returns the result of dividing a by b.
    Raises ValueError if dividing by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
def sqrt(a):

    if a == 0:
        raise ValueError("Cannot multiply by zero!")
    return a * a

