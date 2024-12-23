"""
def my_decorator(func):
    def wrapper():
        print("Something 1st printing before func called")
        func()
        print("Something 1st printing after func called")
    return wrapper


@my_decorator
def say_hello():
    print("Hello")

say_hello()
"""

"""
def add_prefix(prefix):
    def dec_add_prefix(func):
        def wrapper(*args, **kwargs):
            result = func(*args,**kwargs)
            return f"{prefix}{result}"
        return wrapper
    return dec_add_prefix


@add_prefix("Mr. ")
def get_name(name):
    return name

print(get_name("Leo"))
"""
def repeat_times(num_times):
    def dec_repeat_times(func):
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                func(*args,**kwargs)
        return wrapper
    return dec_repeat_times

@repeat_times(num_times=3)
def greet(name):
    print(f"Hello, {name}")

greet("Immanuel")

