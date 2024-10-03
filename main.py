import turtle as t
import pandas

#screen setup
screen = t.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
# Retrieve data
data = pandas.read_csv("50_states.csv")
info_dict = data.to_dict('list')
state_names = info_dict['state']
x_cors = info_dict['x']
y_cors = info_dict['y']

# function to plot data
def plot_state(name_index, state_name):
    plotter = t.Turtle()
    plotter.penup()
    plotter.hideturtle()
    plotter.goto(x = int(x_cors[name_index]), y = int(y_cors[name_index]))
    plotter.write(state_name)


count = 0
while count < 50:
    answer_state = screen.textinput("Guess the State", "What's another state's name?").title()
    if answer_state in state_names:
        idx = state_names.index(answer_state)
        print(answer_state)
        #call function to plot state name and then increase count
        plot_state(idx, answer_state)
        count += 1
    else:
        pass

t.mainloop()