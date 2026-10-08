# ============================================================
#        PYTHON FUNCTIONS - ADVANCED LEVEL ANSWERS
# ============================================================
# Questions are in: questions/advanced_questions.py
# ============================================================

import time
import functools
import asyncio
from collections import OrderedDict
from contextlib import contextmanager
from concurrent.futures import ThreadPoolExecutor


# ------------------------------------------------------------------
# A1. Memoize decorator — caches results of a function
# ------------------------------------------------------------------
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)

print(fib_slow(35))
# Output: 9227465  (fast due to caching)


# ------------------------------------------------------------------
# A2. Retry decorator — retries a function n times on exception
# ------------------------------------------------------------------
def retry(n=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
            raise Exception(f"Function '{func.__name__}' failed after {n} retries.")
        return wrapper
    return decorator

call_count = {"count": 0}

@retry(n=3)
def unstable_function():
    call_count["count"] += 1
    if call_count["count"] < 3:
        raise ValueError("Not ready yet!")
    return "Success!"

print(unstable_function())
# Output:
# Attempt 1 failed: Not ready yet!
# Attempt 2 failed: Not ready yet!
# Success!


# ------------------------------------------------------------------
# A3. validate_types decorator — checks argument types via annotations
# ------------------------------------------------------------------
def validate_types(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        hints = func.__annotations__
        all_args = {**dict(zip(func.__code__.co_varnames, args)), **kwargs}
        for arg_name, expected_type in hints.items():
            if arg_name == "return":
                continue
            if arg_name in all_args:
                if not isinstance(all_args[arg_name], expected_type):
                    raise TypeError(
                        f"Argument '{arg_name}' expected {expected_type.__name__}, "
                        f"got {type(all_args[arg_name]).__name__}"
                    )
        return func(*args, **kwargs)
    return wrapper

@validate_types
def typed_add(a: int, b: int) -> int:
    return a + b

print(typed_add(3, 4))       # Output: 7
# typed_add(3, "four")       # Raises: TypeError: Argument 'b' expected int, got str


# ------------------------------------------------------------------
# A4. Generator — infinite counter
# ------------------------------------------------------------------
def infinite_counter(start=0, step=1):
    value = start
    while True:
        yield value
        value += step

counter = infinite_counter(0, 2)
print([next(counter) for _ in range(6)])
# Output: [0, 2, 4, 6, 8, 10]


# ------------------------------------------------------------------
# A5. Generator — lazy chunked reading of a large list
# ------------------------------------------------------------------
def read_in_chunks(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

large_list = list(range(1, 21))
for chunk in read_in_chunks(large_list, 5):
    print(chunk)
# Output:
# [1, 2, 3, 4, 5]
# [6, 7, 8, 9, 10]
# [11, 12, 13, 14, 15]
# [16, 17, 18, 19, 20]


# ------------------------------------------------------------------
# A6. compose — right-to-left function composition
# ------------------------------------------------------------------
def compose(*funcs):
    def composed(x):
        result = x
        for f in reversed(funcs):
            result = f(result)
        return result
    return composed

double = lambda x: x * 2
add_one = lambda x: x + 1
square = lambda x: x ** 2

transform = compose(double, add_one, square)  # double(add_one(square(x)))
print(transform(3))
# square(3)=9 → add_one(9)=10 → double(10)=20
# Output: 20


# ------------------------------------------------------------------
# A7. curry — transform multi-arg function into chained single-arg calls
# ------------------------------------------------------------------
def curry(func):
    arity = func.__code__.co_argcount
    def curried(*args):
        if len(args) >= arity:
            return func(*args)
        return lambda *more: curried(*(args + more))
    return curried

@curry
def add_three(a, b, c):
    return a + b + c

print(add_three(1)(2)(3))   # Output: 6
print(add_three(1, 2)(3))   # Output: 6
print(add_three(1)(2, 3))   # Output: 6


# ------------------------------------------------------------------
# A8. deep_merge — recursively merge nested dictionaries
# ------------------------------------------------------------------
def deep_merge(d1, d2):
    result = dict(d1)
    for key, value in d2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

d1 = {"a": {"x": 1, "y": 2}, "b": 3}
d2 = {"a": {"y": 10, "z": 5}, "c": 4}
print(deep_merge(d1, d2))
# Output: {'a': {'x': 1, 'y': 10, 'z': 5}, 'b': 3, 'c': 4}


# ------------------------------------------------------------------
# A9. Context manager using contextlib.contextmanager
# ------------------------------------------------------------------
@contextmanager
def managed_resource():
    print("Resource acquired")
    resource = {"data": []}
    try:
        yield resource
    except Exception as e:
        print(f"Exception handled: {e}")
    finally:
        print("Resource released")

with managed_resource() as res:
    res["data"].append(42)
    print(f"Using resource: {res}")
# Output:
# Resource acquired
# Using resource: {'data': [42]}
# Resource released


# ------------------------------------------------------------------
# A10. run_parallel — run functions in parallel using ThreadPoolExecutor
# ------------------------------------------------------------------
def run_parallel(funcs):
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(f) for f in funcs]
        return [f.result() for f in futures]

tasks = [
    lambda: 1 + 1,
    lambda: "hello".upper(),
    lambda: [x**2 for x in range(5)],
]
print(run_parallel(tasks))
# Output: [2, 'HELLO', [0, 1, 4, 9, 16]]


# ------------------------------------------------------------------
# A11. safe_divide — reduce a list of numbers by dividing sequentially
# ------------------------------------------------------------------
def safe_divide(numbers):
    try:
        return functools.reduce(lambda a, b: a / b, numbers)
    except ZeroDivisionError:
        print("Error: Division by zero encountered.")
        return None

print(safe_divide([100, 2, 5]))   # Output: 10.0
print(safe_divide([100, 0, 5]))   # Output: Error: Division by zero encountered. → None


# ------------------------------------------------------------------
# A12. LRU Cache using OrderedDict
# ------------------------------------------------------------------
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)   # Mark as recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used

lru = LRUCache(3)
lru.put("a", 1)
lru.put("b", 2)
lru.put("c", 3)
lru.put("d", 4)          # "a" gets evicted
print(lru.get("a"))       # Output: -1 (evicted)
print(lru.get("b"))       # Output: 2


# ------------------------------------------------------------------
# A13. flatten_dict — flatten nested dict with dot-separated keys
# ------------------------------------------------------------------
def flatten_dict(d, parent_key="", sep="."):
    items = {}
    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, sep))
        else:
            items[new_key] = value
    return items

nested = {"a": {"b": {"c": 1}}, "d": 2}
print(flatten_dict(nested))
# Output: {'a.b.c': 1, 'd': 2}


# ------------------------------------------------------------------
# A14. throttle — limit a function to once per interval seconds
# ------------------------------------------------------------------
def throttle(interval):
    def decorator(func):
        last_called = [0]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - last_called[0] < interval:
                print(f"Throttled! Wait {interval - (now - last_called[0]):.2f}s before calling again.")
                return None
            last_called[0] = now
            return func(*args, **kwargs)
        return wrapper
    return decorator

@throttle(interval=2)
def send_request(msg):
    print(f"Request sent: {msg}")
    return "OK"

send_request("Hello")    # Output: Request sent: Hello
send_request("Again")    # Output: Throttled! (called too soon)


# ------------------------------------------------------------------
# A15. Pipeline class — chain functions using the | operator
# ------------------------------------------------------------------
class Pipeline:
    def __init__(self, value):
        self.value = value

    def __or__(self, func):
        return Pipeline(func(self.value))

    def __repr__(self):
        return f"Pipeline({self.value})"

result = Pipeline(5) | (lambda x: x * 2) | (lambda x: x + 3)
print(result.value)
# Output: 13


# ------------------------------------------------------------------
# A16. memoize_with_expiry — cache with TTL (time-to-live)
# ------------------------------------------------------------------
def memoize_with_expiry(ttl_seconds):
    def decorator(func):
        cache = {}   # key → (result, timestamp)
        @functools.wraps(func)
        def wrapper(*args):
            now = time.time()
            if args in cache:
                result, timestamp = cache[args]
                if now - timestamp < ttl_seconds:
                    print(f"Cache hit for {args}")
                    return result
            result = func(*args)
            cache[args] = (result, now)
            return result
        return wrapper
    return decorator

@memoize_with_expiry(ttl_seconds=5)
def expensive_computation(n):
    time.sleep(0.1)
    return n ** 2

print(expensive_computation(4))   # Computed
print(expensive_computation(4))   # Cache hit (within 5s)
# Output:
# 16
# Cache hit for (4,)
# 16


# ------------------------------------------------------------------
# A17. zip_with — apply a function element-wise to two lists
# ------------------------------------------------------------------
# Version 1: using a loop
def zip_with_loop(func, lst1, lst2):
    result = []
    for a, b in zip(lst1, lst2):
        result.append(func(a, b))
    return result

# Version 2: using map + zip
def zip_with_map(func, lst1, lst2):
    return list(map(lambda pair: func(*pair), zip(lst1, lst2)))

print(zip_with_loop(lambda a, b: a + b, [1, 2, 3], [4, 5, 6]))
# Output: [5, 7, 9]
print(zip_with_map(lambda a, b: a * b, [1, 2, 3], [4, 5, 6]))
# Output: [4, 10, 18]


# ------------------------------------------------------------------
# A18. Tail-recursive factorial with trampolining
# ------------------------------------------------------------------
# Standard tail-recursive style (Python doesn't optimize this):
def tail_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    return tail_factorial(n - 1, accumulator * n)  # Python will hit RecursionError for large n

# Trampoline version to avoid stack overflow:
def trampoline(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        while callable(result):
            result = result()
        return result
    return wrapper

@trampoline
def tramp_factorial(n, acc=1):
    if n == 0:
        return acc
    return lambda: tramp_factorial(n - 1, acc * n)

print(tail_factorial(10))         # Output: 3628800
print(tramp_factorial(1000))      # Works without RecursionError
print(tramp_factorial(1000) > 0)  # Output: True


# ------------------------------------------------------------------
# A19. Custom partial application (without functools.partial)
# ------------------------------------------------------------------
def my_partial(func, *fixed_args, **fixed_kwargs):
    def wrapper(*args, **kwargs):
        combined_args = fixed_args + args
        combined_kwargs = {**fixed_kwargs, **kwargs}
        return func(*combined_args, **combined_kwargs)
    return wrapper

def power(base, exponent):
    return base ** exponent

square = my_partial(power, exponent=2)
cube   = my_partial(power, exponent=3)

print(square(base=5))   # Output: 25
print(cube(base=3))     # Output: 27


# ------------------------------------------------------------------
# A20. async_gather_results — run async tasks concurrently with asyncio
# ------------------------------------------------------------------
async def async_task(task_id, delay):
    await asyncio.sleep(delay)
    result = f"Task {task_id} done after {delay}s"
    print(result)
    return result

async def async_gather_results():
    tasks = [
        async_task(1, 0.3),
        async_task(2, 0.1),
        async_task(3, 0.2),
    ]
    results = await asyncio.gather(*tasks)
    return results

# Run the async function:
results = asyncio.run(async_gather_results())
print(results)
# Output (order by completion time):
# Task 2 done after 0.1s
# Task 3 done after 0.2s
# Task 1 done after 0.3s
# ['Task 1 done after 0.3s', 'Task 2 done after 0.1s', 'Task 3 done after 0.2s']
