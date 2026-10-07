from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before fucntion runs")
        func()
        print("After fucntion runs")
    return wrapper

@my_decorator 
def greet():
    print("hello from decorators learning")

greet()


print(greet.__name__)