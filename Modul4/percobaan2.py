#percobaan 2
def uppercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

result = say_hi()
print(result)