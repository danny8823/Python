def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1/n2


calc_on = True
result = 0

while calc_on:
    if result == 0:
        n1 = int(input("What's the first number?"))
    else:
        n1 = result
    operation = input("What operation? + - * /")
    n2 = int(input("What's the second number?"))

    if operation == '+':
        result = add(n1, n2)
        print(result)
        more_calc = input(
            f"Do you want to continue calculation with {result}? y or n:\n")
        if more_calc == 'n':
            print(result)
            calc_on = False
    elif operation == '-':
        result = subtract(n1, n2)
        print(result)
        more_calc = input(
            f"Do you want to continue calculation with {result}? y or n:\n")
        if more_calc == 'n':
            print(result)
            calc_on = False
    elif operation == '*':
        result = multiply(n1, n2)
        print(result)
        more_calc = input(
            f"Do you want to continue calculation with {result}? y or n:\n")
        if more_calc == 'n':
            print(result)
            calc_on = False
    elif operation == '/':
        result = divide(n1, n2)
        print(result)
        more_calc = input(
            f"Do you want to continue calculation with {result}? y or n:\n")
        if more_calc == 'n':
            print(result)
            calc_on = False
    else:
        print('Pick the right operation please.')
