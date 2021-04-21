# Python
import functools
import time


def timer(fun):
    """
    Display in terminal how much time it took to execute any function.
    """
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        begin = time.perf_counter()
        value = fun(*args, **kwargs)
        end = time.perf_counter()
        total = end - begin
        print(f' * Burner Timer: Finished task {fun.__name__} in {total:0.4f} seconds.')
        return value
    return wrapper
