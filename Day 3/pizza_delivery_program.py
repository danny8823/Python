print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L:")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == 'S':
    bill = 15
    if pepperoni == 'Y':
        bill += 2
    else:
        bill
    if extra_cheese == 'Y':
        bill += 1
    else:
        bill
    print(f"Final price is ${bill}.")
elif size == 'M':
    bill = 20
    if pepperoni == 'Y':
        bill += 3
    else:
        bill
    if extra_cheese == 'Y':
        bill += 1
    else:
        bill
    print(f"Final price is ${bill}.")
elif size == 'L':
    bill = 25
    if pepperoni == 'Y':
        bill += 3
    else:
        bill
    if extra_cheese == 'Y':
        bill += 1
    else:
        bill
    print(f"Final price is ${bill}.")
else:
    print('Error please enter the right size.')
