"""
Project decorators.
"""

# Python
import functools
import time
from typing import Callable


def timer(fun: Callable) -> Callable:
    """Decorator to display in terminal how much time it took to execute the
    decorated function.

    Parameters
    ----------
    fun : Callable
        Function or method to wrap and measure execution time.

    Return
    ------
    wrapper : Wrapper to serve as a decorator.
    """
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        begin = time.perf_counter()
        value = fun(*args, **kwargs)
        end = time.perf_counter()
        total = end - begin
        print(f' * Burner Timer: Finished task in {total:0.4f} seconds.')
        return value
    return wrapper
