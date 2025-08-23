def get_user_name():
    return "John Doe"
def greet_user():
    name = get_user_name()
    return "Hello {}".format(name)

def divide(a:int, b: int):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return a//b
