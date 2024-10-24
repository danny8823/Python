print('Welcome to the tip calculator!')

total = input('What was the total bill?')

tip = input('How much tip would like to give? 10, 12, or 15?')

people = input('How many people are splitting the bill?')

total_after_tip = round((int(total) * int(tip)/100) + int(total), 2)
print(total_after_tip)
print(
    f"Each person should pay, ${round(int(total_after_tip) / int(people),2)}")
