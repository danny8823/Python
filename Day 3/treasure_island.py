print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')

left_right = input(
    "You're at a cross road. Where do you want to go? Type 'left' or 'right'")

if left_right == 'left':
    swim_wait = input('Your at a lake, do you want to "swim" or "wait"?')
    if swim_wait == "swim":
        print('You swam in the lake, but you were attacked by a trout, game over.')
    elif swim_wait == "wait":
        door_color = input(
            'You found some doors at a complex, which color door do you want to open? "red", "blue", "yellow"?')
        if door_color == 'yellow':
            print('You win')
        elif door_color == 'red':
            print('You been burned by fire, game over')
        elif door_color == 'blue':
            print('You been eaten by a beast, game over')
        else:
            print('Game over')
elif left_right == 'right':
    print('Fell into a hole, game over.')
