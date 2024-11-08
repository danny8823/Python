import menu

machine = 'on'
coffee_menu = menu.MENU
ingredient_words = ['water', 'milk', 'coffee']
total_coins = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def report(resources):
    print("Water: ", resources['water'], 'ml')
    print("Milk: ", resources['milk'], 'ml')
    print("Coffee: ", resources['coffee'], 'g')
    print("Money: ", resources['money'])


def check_price(order):
    price = menu.MENU[order]['cost']
    return price


def check_resources(order):
    ingredients = menu.MENU[order]['ingredients']
    check = 0
    if order == 'espresso':
        if ingredients['water'] <= resources['water']:
            print('enough')
            check += 1
        else:
            print('not enough')
        if ingredients['coffee'] <= resources['coffee']:
            print('enough')
            check += 2
        else:
            print('not enough')
    else:
        if ingredients['water'] <= resources['water']:
            print('enough')
            check += 1
        else:
            print('not enough')
        if ingredients['milk'] <= resources['milk']:
            print('enough')
            check += 1
        else:
            print('not enough')
        if ingredients['coffee'] <= resources['coffee']:
            print('enough')
            check += 1
        else:
            print('not enough')


def process_order(order):
    if order == 'off':
        return print('Machine off.')
    elif order == 'espresso':
        print('espresso')
    elif order == 'latte':
        print('latte')
    elif order == 'cappucino':
        print('cappucino')


def inserted_coins(amount, coin):
    global total_coins
    if coin == 'quarter':
        result = amount * 0.25
        total_coins += result
    elif coin == 'dime':
        result = amount * 0.10
        total_coins += result
    elif coin == 'nickle':
        result = amount * 0.5
        total_coins += result
    elif coin == 'penny':
        result = amount * 0.1
        total_coins += result

    return total_coins


def transaction(total, order):
    change = 0
    if total < coffee_menu[order]['cost']:
        print("Sorry that's not enough money.")
        return False
    elif total == coffee_menu[order]['cost']:
        print("Transaction successful, no change.")
        return True
    else:
        change += total - coffee_menu[order]['cost']
        print(f"Transaction successful, you're change is ${change}")
        return True


def start_machine():
    machine = False
    order = input('What would you like? (espresso,latte,cappuccino):  ')
    while not machine:
        print(order)
        print(f'${check_price(order)}')
        report(resources)
        check_resources(order)
        machine = True


start_machine()
