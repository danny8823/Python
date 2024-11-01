def my_function():
    result = 3 * 2
    return result


print(my_function())


def format_name(f_name, l_name):
    return f_name.title() + ' ' + l_name.title()


print(format_name('Danny', 'Yoo'))


def function_1(text):
    return text + text


def function_2(text):
    return text.title()


output = function_2(function_1('hello'))

print(output)

print(1989/4)
print(497.25 % 2)
