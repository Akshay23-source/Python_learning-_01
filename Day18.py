def greet():
    print("Hello")
    
    
    def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

def greet():
    print("Hello")

greet()

def my_decorator(func):
    def wrapper(name):
        print("Before function")
        func(name)
        print("After function")
    return wrapper

@my_decorator
def greet(name):
    print("Hello", name)

greet("Akshay")