def add(*args):
    result = 0
    for n in args:
        result += n

    print(result)


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(5, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')


my_car = Car(make='Dodge')

print(my_car.model)
