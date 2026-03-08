"""
Part B — Decorators Implementation
Day 10 PM Assignment
"""

import time
import random
from functools import wraps


# ------------------------------
# TIMER DECORATOR
# ------------------------------
def timer(func):
    """
    Decorator that measures execution time of a function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"[TIMER] {func.__name__} executed in {end-start:.4f} seconds")

        return result

    return wrapper


# ------------------------------
# LOGGER DECORATOR
# ------------------------------
def logger(func):
    """
    Decorator that logs function name, arguments and return value.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"[LOGGER] Calling function: {func.__name__}")
        print(f"[LOGGER] Arguments: args={args}, kwargs={kwargs}")

        result = func(*args, **kwargs)

        print(f"[LOGGER] Returned: {result}")

        return result

    return wrapper


# ------------------------------
# RETRY DECORATOR
# ------------------------------
def retry(max_attempts=3):
    """
    Retries a function if it raises an exception.
    """

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            attempts = 0

            while attempts < max_attempts:

                try:
                    return func(*args, **kwargs)

                except Exception as e:

                    attempts += 1
                    print(f"[RETRY] Attempt {attempts} failed: {e}")

                    if attempts == max_attempts:
                        raise Exception("Max retry attempts exceeded")

        return wrapper

    return decorator


# ------------------------------
# TEST FUNCTIONS
# ------------------------------

@timer
def slow_function():
    """Function to simulate delay"""
    time.sleep(1)
    return "Task Completed"


@logger
def add_numbers(a, b):
    """Simple addition"""
    return a + b


@retry(max_attempts=3)
def unstable_function():
    """Function that randomly fails"""
    if random.random() < 0.7:
        raise ValueError("Random failure occurred")
    return "Success"


# ------------------------------
# MAIN EXECUTION
# ------------------------------

if __name__ == "__main__":

    print("\n--- TIMER TEST ---")
    print(slow_function())

    print("\n--- LOGGER TEST ---")
    print(add_numbers(5, 3))

    print("\n--- RETRY TEST ---")
    print(unstable_function())