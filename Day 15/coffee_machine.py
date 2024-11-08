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
    print('RESOURCE REPORT:  ')
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
            check += 1
        if ingredients['coffee'] <= resources['coffee']:
            check += 2
    else:
        if ingredients['water'] <= resources['water']:
            check += 1
        if ingredients['milk'] <= resources['milk']:
            check += 1
        if ingredients['coffee'] <= resources['coffee']:
            check += 1

    return check


def process_order(order, resources):
    if order == 'off':
        return print('Machine off.')
    elif order == 'espresso':
        resources['water'] = resources['water'] - \
            coffee_menu[order]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - \
            coffee_menu[order]['ingredients']['coffee']
        print('Here is your espresso!')
    elif order == 'latte':
        resources['water'] = resources['water'] - \
            coffee_menu[order]['ingredients']['water']
        resources['milk'] = resources['milk'] - \
            coffee_menu[order]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - \
            coffee_menu[order]['ingredients']['coffee']
        print('Here is your latte!')
    elif order == 'cappucino':
        resources['water'] = resources['water'] - \
            coffee_menu[order]['ingredients']['water']
        resources['milk'] = resources['milk'] - \
            coffee_menu[order]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - \
            coffee_menu[order]['ingredients']['coffee']
        print('Here is your cappucino!')


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
    elif total == coffee_menu[order]['cost']:
        print("Transaction successful, no change.")
    else:
        change += total - coffee_menu[order]['cost']
        print(f"Transaction successful, you're change is ${change}")


def start_machine():
    global total_coins
    machine = False
    done_insert = False
    order = input('What would you like? (espresso,latte,cappuccino):  ')

    while not machine:
        if order == 'off':
            machine = True
        else:
            print(f'{order} is ${check_price(order)}')
            print('\n' * 4)
            while not done_insert:
                amount = input(
                    'How many coins? 1,2,3...etc. If done type "done"')
                print('\n' * 4)
                if amount == 'done':
                    done_insert = True
                else:
                    coin = input(
                        f'Insert your coins. {amount} and pick a coin "quarter, dime, nickle, penny"')
                    print('\n' * 4)
                    inserted_coins(int(amount), coin)
                    print('\n' * 4)
                    print(total_coins, " inserted.")
                    print('\n' * 4)
            report(resources)
            if check_resources(order) == 3 and total_coins >= check_price(order):
                transaction(total_coins, order)
                print('\n' * 4)
                process_order(order, resources)
                print('\n' * 4)
                resources['money'] += total_coins
                total_coins = 0
                print('\n' * 4)
                report(resources)
                print('\n' * 4)
                start_machine()


start_machine()
