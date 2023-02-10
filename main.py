import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "india-states.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("india_states.csv")
point = 0
all_states = data.state.to_list()
print(all_states)
guessed_states = []
missed_states = []

while point != 29:
    answer = turtle.textinput(title=f"{point}/50 States Correct", prompt="Name a State").title()
    print(answer)
    guessed_states.append(answer)

    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(f"{answer}")
        point += 1

    if answer == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)

        file = pandas.DataFrame(missed_states)
        file.to_csv("Learn_States.csv")
        break

screen.exitonclick()
