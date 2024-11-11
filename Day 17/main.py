from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
moneyMachine = MoneyMachine()

latte = MenuItem(name='latte', water=200, milk=150,  coffee=24, cost=2.5)
espresso = MenuItem(name='espresso', water=50, milk=0, coffee=18, cost=1.5)
cappuccino = MenuItem(name='cappucino', water=250,
                      milk=100, coffee=24, cost=3.0)

coffeeMaker = CoffeeMaker()

menu_items = menu.get_items()


machine_power_on = True

while machine_power_on:
    user_order = input(f"What would you like to order? ({menu_items}):")
    if user_order == 'off':
        print('Machine powering down')
        machine_power_on = False
    elif user_order == 'report':
        print('Machine report')
        print(coffeeMaker.report())
    elif user_order == 'latte':
        if moneyMachine.make_payment(latte.cost) == True:
            print(coffeeMaker.make_coffee(latte))
    elif user_order == 'espresso':
        if moneyMachine.make_payment(espresso.cost) == True:
            print(coffeeMaker.make_coffee(espresso))
    elif user_order == 'cappuccino':
        if moneyMachine.make_payment(cappuccino.cost) == True:
            print(coffeeMaker.make_coffee(cappuccino))
    else:
        print('Wrong prompt')
