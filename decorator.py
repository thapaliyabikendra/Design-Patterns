def add_twice(func):
    def wrapper(x, y):
        x = 2 * x
        y = 2 * y
        return func(x, y)        
    return wrapper


@add_twice
def add(num1, num2):
    return num1 + num2


print(add(2, 2))