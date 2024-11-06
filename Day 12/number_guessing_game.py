import random

run = input('Type run to start game!')

ATTEMPTS = 0
NUM_TO_GUESS = random.randint(1, 100)
GAME_OVER = False


def set_attempts(response):
    global ATTEMPTS
    if response == "easy":
        ATTEMPTS = 10
    elif response == "hard":
        ATTEMPTS = 5
    else:
        return print('Please input the correct response.')


def game_start():
    global ATTEMPTS
    global NUM_TO_GUESS
    game_over = False
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input('Choose a difficulty. Type "easy" or "hard"')
    set_attempts(difficulty)

    while not game_over:
        if ATTEMPTS == 0:
            game_over = True
            print('You lose')
            play_again = input('Do you want to play again? "yes" or "no"?')
            if play_again == 'yes':
                game_start()
            else:
                return print('Thanks for playing!')
        else:
            guess = int(input('Make a guess: '))

            if guess == NUM_TO_GUESS:
                print(f'Correct guess! {NUM_TO_GUESS}')
                game_over = True
            elif guess < NUM_TO_GUESS:
                ATTEMPTS -= 1
                print(ATTEMPTS)
                print('Too low')
            elif guess > NUM_TO_GUESS:
                ATTEMPTS -= 1
                print(ATTEMPTS)
                print('Too high')


if run == 'run':
    game_start()
