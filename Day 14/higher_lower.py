import art
import game_data
import random

score = 0
start = input('Type "run" to start game.')


def game_start():
    global score
    game_over = False
    most_followers = ''

    A = random.choice(game_data.data)
    B = random.choice(game_data.data)

    while not game_over:
        print("\n" * 20)
        print(A['follower_count'], B['follower_count'])
        if int(A['follower_count']) > int(B['follower_count']):
            most_followers = 'A'
        elif int(A['follower_count']) < int(B['follower_count']):
            most_followers = 'B'

        if A['name'] == B['name']:
            B = random.choice(game_data.data)
        else:
            print('Compare A: ', A['name'], ' a ',
                  A['description'], ' from ', A['country'])
            print(art.vs)
            print('With B: ', B['name'], ' a ',
                  B['description'], ' from ', B['country'])

            print('\n' * 10)
            guess = input('Who has more followers? type "A" of "B"')

            print(most_followers)
            if guess == most_followers:
                score += 1
                print('you won, current score: ', score)
                A = B
                B = random.choice(game_data.data)
            else:
                print('you lose')
                print('Final Score: ', score)
                game_over = True


if start == 'run':
    game_start()
