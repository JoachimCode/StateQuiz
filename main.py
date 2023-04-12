import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Quiz")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
screen.tracer(0)
data = pandas.read_csv("50_states.csv")
list_state = []
guessed_states = []
for state in data["state"]:
    list_state.append(state)


#answer box
def question():
    global game
    correct = False
    answer = screen.textinput(title=f"Your score is {points}/50", prompt="Name a state")
    answer = answer.lower()
    answer = answer.title()
    if answer == "Exit":
        game = False
        return 0
    #check answer
    for state in list_state:
        if answer in guessed_states:
            print("already guessed that state")
            return 0
        elif answer == state:
            print("correct")
            list_state.remove(state)
            guessed_states.append(state)
            guess = state
            correct = True
            break
    if not correct:
        print("wrong")
        return 0
    if correct:
        row = data[data.state == guess]
        x1 = row["x"].values
        x = x1[0]
        y1 = row["y"].values
        y = y1[0]
        write(guess, x, y)

        return 1
#if correct, print state name on map
def write(state, x, y):
    text = turtle.Turtle()
    text.color("black")
    text.penup()
    text.goto(x,y)
    text.hideturtle()
    text.write(state)
    screen.update()

screen.update()

points = 0
game = True
while game:
    points += question()
    if points == 50:
        print("Congratulation, you've plotted all the states")
        game = False
df = pandas.DataFrame(list_state, columns=["column"])
df.to_csv("remaining_states", index=False)

screen.exitonclick()