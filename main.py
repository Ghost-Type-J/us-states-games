import turtle, pandas as pd

# from state_writer import StateWriter
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guessed Correctly", prompt="What's the another "
                                                                                                "state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(state_data.x.iloc[0], state_data.y.iloc[0])
        t.write(state_data.state.item())

missing_states = [x for x in all_states if x not in guessed_states]
new_data = pd.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")
