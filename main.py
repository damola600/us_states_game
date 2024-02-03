import time
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
screen.tracer(0)

states_data = pandas.read_csv("50_states.csv")
states = states_data["state"].tolist()
print(states)


# correct_states = 0
# while correct_states < 50:
#     answer_state = input("What's another state's name? ")
#     print(answer_state.title())
#     if answer_state.title() in states:
#         print("correct")
#         correct_states += 1
#         state_x = states_data[states_data.state == answer_state.title()].x
#         state_y = states_data[states_data.state == answer_state.title()].y
#         print(state_x, state_y)


def create_turtle(state, x, y):
    state_turtle = turtle.Turtle()
    state_turtle.color("black")
    state_turtle.penup()
    state_turtle.hideturtle()
    state_turtle.goto(x, y)
    state_turtle.write(state)


correct_states = 0
guessed_states = []
while len(guessed_states) < 50:
    screen.update()
    time.sleep(0.1)
    answer_state = screen.textinput(title=f"{correct_states}/{len(states)} Guess The State",
                                    prompt="What's another state's name?")
    answer_state = answer_state.title()
    print(answer_state)
    if answer_state == "Exit":
        break
    if answer_state in states and answer_state not in guessed_states:
        print("correct")
        correct_states += 1
        guessed_states.append(answer_state)
        state_x = int(states_data[states_data.state == answer_state].x)
        state_y = int(states_data[states_data.state == answer_state].y)

        create_turtle(answer_state, state_x, state_y)

# states_not_guessed = {state for state in states if state not in guessed_states}

states_not_guessed = {}
states_not_guessed = {states_not_guessed["state"] for states_not_guessed["state"] in states if states_not_guessed["state"] not in guessed_states}

# for state in states:
#     if state not in guessed_states:
#         states_not_guessed["state"] = states_data.state

data = pandas.DataFrame(states_not_guessed)
data.to_csv("states_to_learn.csv")

# screen.exitonclick()
