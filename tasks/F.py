import time


def log_exec_time(func):
    """Decorator that logs function execution time."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        exec_time = time.time() - start_time
        print(f"Function {func.__name__} was executed at {round(exec_time * 1000, 1)} ms\n")
        return res
    return wrapper