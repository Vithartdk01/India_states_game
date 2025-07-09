import turtle
import pandas

screen=turtle.Screen()
screen.title("INDIA States Game")
image="blank_india_map.gif"
screen.addshape(image)

turtle.shape(image)

guessed_states=[]
data=pandas.read_csv("states.csv")
state_list=data.state.to_list()


while len(guessed_states)<50:

    guess = screen.textinput(title=f"{len(guessed_states)}/28 States Correct",
                             prompt="What's another state's name?").title()

    if guess=="Exit":
        missed_states=[]
        for state in state_list:
            if state not in guessed_states:
                missed_states.append(state)
        new_data=pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn")
        break

    if guess in state_list:
        guessed_states.append(guess)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == guess]
        x_cor=state_data.x.item()
        y_cor = state_data.y.item()
        t.goto(x_cor,y_cor)
        t.write(guess)

