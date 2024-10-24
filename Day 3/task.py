print('Welcome to the rollercoaster')
height = int(input("What is your height in CM? "))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Please pay $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    elif age >= 45 and age <= 55:
        print("Everything is okay, free ride on us.")
    else:
        bill = 12
        print("Please pay $12")

    wants_photo = input(
        "Do you want to have a photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        bill += 3
        print(f"Please pay ${bill}")
    else:
        bill
else:
    print("You can't ride the rollercoaster")


# num = int(input("Enter a number to see if its even or odd."))

# if num % 2 == 0:
#     print('Even!')
# else:
#     print('Odd!')
