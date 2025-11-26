"""
Example: Python decorators (@decorator)
- What: A decorator is a callable that takes a function (or class) and returns a new function (or class).
- Purpose: Add or modify behavior of functions transparently (logging, caching, access control, retries, timing, etc.)
- Advantages: Reuseable, composable, keeps core logic clean, separates concerns.
- Syntax: Use @decorator above a function to apply it (syntactic sugar for: f = decorator(f))
"""

from functools import wraps
import time

# ---------- Simple decorator: logging / debug ----------
def debug(func):
    """Log function calls and results."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[DEBUG] {func.__name__} called with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] {func.__name__} returned {result!r}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

# ---------- Parameterized decorator ----------
def repeat(times):
    """Call the wrapped function `times` times (and return last result)."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return f"Hello, {name}"

# ---------- Memoization (caching) decorator ----------
def memoize(func):
    """Simple cache for single-argument functions."""
    cache = {}
    @wraps(func)
    def wrapper(n):
        if n in cache:
            return cache[n]
        res = func(n)
        cache[n] = res
        return res
    return wrapper

# Count calls to illustrate benefits
counters = {"no_cache": 0, "cached": 0}

def fib_no_cache(n):
    counters["no_cache"] += 1
    if n < 2:
        return n
    return fib_no_cache(n - 1) + fib_no_cache(n - 2)

@memoize
def fib_cached(n):
    counters["cached"] += 1
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

# ---------- Tests / Demonstration ----------
def run_tests():
    print("\n-- debug decorator test --")
    assert add(2, 3) == 5  # triggers debug logs

    print("\n-- repeat decorator test --")
    result = greet("Alice")
    assert result == "Hello, Alice"  # was called 3 times, but returns last result

    print("\n-- memoize / performance illustration --")
    n = 10
    counters["no_cache"] = 0
    counters["cached"] = 0

    start = time.perf_counter()
    fib_no_cache(n)
    t1 = time.perf_counter() - start

    start = time.perf_counter()
    fib_cached(n)
    t2 = time.perf_counter() - start

    print(f"fib_no_cache calls: {counters['no_cache']}, time: {t1:.4f}s")
    print(f"fib_cached calls: {counters['cached']}, time: {t2:.4f}s")

    assert counters["cached"] < counters["no_cache"]  # caching reduced work
    print("\nAll assertions passed.")

if __name__ == "__main__":
    run_tests()