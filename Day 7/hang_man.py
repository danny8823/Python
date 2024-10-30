import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ['camel', 'turkey', 'hello', 'church', 'laptop']

random_word = word_list[random.randrange(0, 5)]

print(random_word)

placeholder = ''

for num in range(len(random_word)):
    placeholder += ' _ '

print(placeholder)

game_over = False

correct_letters = []
lives = 6

while not game_over:
    user_guess = input('Guess a letter!').lower()
    display = ''
    for letter in random_word:
        if letter == user_guess:
            display += letter
            correct_letters.append(user_guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    print(display)
    if user_guess not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print('You lose')

    if "_" not in display:
        game_over = True
        print('You Win')

    print(stages[lives])
