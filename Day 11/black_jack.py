import random

cards = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

players_cards = []
computer_cards = []

p_score = 0
computer_score = 0

game = 'on'


def draw_players_card():
    players_cards.append(cards[random.randint(0, 12)])


def draw_computers_cards():
    computer_cards.append(cards[random.randint(0, 12)])
    computer_cards.append(cards[random.randint(0, 12)])


def count_p_score():
    p_score = 0

    for card in players_cards:
        if card == 'Ace':
            p_score += 11
        elif card == 2:
            p_score += 2
        elif card == 3:
            p_score += 3
        elif card == 4:
            p_score += 4
        elif card == 5:
            p_score += 5
        elif card == 6:
            p_score += 6
        elif card == 7:
            p_score += 7
        elif card == 8:
            p_score += 8
        elif card == 9:
            p_score += 9
        elif card == 10:
            p_score += 10
        elif card == 'Jack':
            p_score += 10
        elif card == 'Queen':
            p_score += 10
        elif card == 'King':
            p_score += 10

    return p_score


def count_c_score():
    c_score = 0

    for card in computer_cards:
        if card == 'Ace':
            c_score += 11
        elif card == 2:
            c_score += 2
        elif card == 3:
            c_score += 3
        elif card == 4:
            c_score += 4
        elif card == 5:
            c_score += 5
        elif card == 6:
            c_score += 6
        elif card == 7:
            c_score += 7
        elif card == 8:
            c_score += 8
        elif card == 9:
            c_score += 9
        elif card == 10:
            c_score += 10
        elif card == 'Jack':
            c_score += 10
        elif card == 'Queen':
            c_score += 10
        elif card == 'King':
            c_score += 10

    return c_score


draw_players_card()
draw_players_card()
draw_computers_cards()

user_score = count_p_score()
pc_score = count_c_score()

print("User's cards:", players_cards)
print("User score:", user_score)
print("PC's first card:", computer_cards[0])
print("PC score:", pc_score)

draw = input('type "y" to get another card, type "n" to pass:')

if draw == 'y':
    draw_players_card()
    draw_computers_cards()

    user_score = count_p_score()
    pc_score = count_c_score()

    print("User's cards: ", players_cards, "User's score: ", user_score)
    print("Pc's cards: ", computer_cards, "Pc's score: ", pc_score)
else:
    user_score = count_p_score()
    pc_score = count_c_score()
