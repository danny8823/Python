import random

rock = ('    ________'
        '____;    ____)'
        '        (______)'
        '        (______)'
        '        (____) '
        '----.___(___)')


paper = ('      ________'
         '______;_______)_______'
         '         _____________)'
         '         _____________)'
         '         _____________)'
         '------- __________)')


scissor = ('       _____________'
           '      ;         _____)_____'
           '------             ________)'
           '             ______________)'
           '            (_______)'
           '------.______(____)'
           )

games_images = [rock, paper, scissor]

your_choice = int(input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
print(games_images[your_choice])

computer_choice = random.randint(0, 2)
print(f'Computer choice: {computer_choice}')
print(games_images[computer_choice])

if your_choice == 0 and computer_choice == 0:
    print('TIE')
elif your_choice == 0 and computer_choice == 1:
    print('You lose')
elif your_choice == 0 and computer_choice == 2:
    print('You Win')

if your_choice == 1 and computer_choice == 0:
    print('You win')
elif your_choice == 1 and computer_choice == 1:
    print('Tie')
elif your_choice == 1 and computer_choice == 2:
    print('You Lose')

if your_choice == 2 and computer_choice == 0:
    print('You lose')
elif your_choice == 2 and computer_choice == 1:
    print('You Win')
elif your_choice == 2 and computer_choice == 2:
    print('You Tie')
