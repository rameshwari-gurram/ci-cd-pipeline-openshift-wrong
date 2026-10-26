"""Small sample application functions for CI/CD demonstration."""


def add_numbers(first, second):
    """Return the sum of two numbers."""
    return first + second


def greet(name):
    """Return a friendly greeting."""
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("name must not be empty")
    return f"Hello, {cleaned_name}!"
