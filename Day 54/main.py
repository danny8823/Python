import time


def outer_function(n, n1):
    answer = n+n1

    def nested_function(answer):
        print('innie')
        print(answer*2)

    return nested_function(answer)


inner_function = outer_function(5, 2)

#! PYTHON DECORATOR


def plus_num(num1, num2):
    return print(num1 + num2)


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function


@delay_decorator
def say_hello():
    print('hello')


@delay_decorator
def say_bye():
    print('bye')


def say_greeting():
    print('how are you?')


decorated_func = delay_decorator(say_greeting)
decorated_func()
say_hello()

say_bye()
