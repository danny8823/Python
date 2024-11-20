import turtle
import os
import pandas
from state_names import State_Names
f = open(
    "/Users/danny714/Desktop/Python/Day 25/us-states-game/50_states.csv")

states_data = pandas.read_csv(f)


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "/Users/danny714/Desktop/Python/Day 25/us-states-game/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


game_on = True
score = 0
guessed_states = []

while game_on:

    answer_state = screen.textinput(title=f'Guess the State {score}/50',
                                    prompt="What's another state's name?")
    state_list = states_data['state'].to_list()
    x_list = states_data['x'].to_list()
    y_list = states_data['y'].to_list()

    if score == 50:
        game_on = False

    for state in state_list:
        if answer_state.title() == 'Exit':
            missing_states = [
                state for state in state_list if state not in guessed_states]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv(
                "/Users/danny714/Desktop/Python/Day 25/us-states-game/new_game_data.csv")
            break
        if answer_state.title() == state:
            guessed_states.append(answer_state.title())
            score += 1
            state_index = state_list.index(state)
            State_Names.write_state(
                answer=state_list[state_index], x=x_list[state_index], y=y_list[state_index])
