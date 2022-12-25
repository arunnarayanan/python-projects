import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


states_data = pd.read_csv('50_states.csv')
print(states_data.dtypes)
all_states = states_data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'Score: {len(guessed_states)} / 50', prompt='What\'s another state name?').title()
    if answer_state == 'Exit':
        print(guessed_states)
        missing_states = [x for x in all_states if x not in guessed_states]
        missing_states_df = pd.DataFrame(missing_states)
        missing_states_df.to_csv('missing_states.csv', header=False, index=False)
        break

    if answer_state in all_states:
        print(f"Match Found for {answer_state}")
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        matching_state_data = states_data[states_data.state == answer_state]
        t.goto(int(matching_state_data.x), int(matching_state_data.y))
        t.write(matching_state_data.state.item())
        guessed_states.append(answer_state)

    else:
        print("No luck")

screen.exitonclick()

