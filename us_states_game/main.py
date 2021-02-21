import turtle
import pandas

ALIGN='center'
FONT=('courier', 8, 'normal')

data = pandas.read_csv("50_states.csv")
with open('user_data.txt') as user_data:
    correct = int(user_data.read())

t = turtle.Turtle()
t.penup()
t.hideturtle()

screen = turtle.Screen()
screen.title("Naru's US States game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

state_names = data['state']


while correct < 50:

    answer = screen.textinput(title="Guess", prompt=f"{correct}/50 State name")
    answer = answer.lower()
    for i in state_names:
        if i.lower() == answer:
            state_x = int(data[data['state']==i]['x'])
            state_y = int(data[data['state']==i]['y'])

            t.goto(state_x, state_y)
            t.write(f"{i}", align=ALIGN, font=FONT)

            correct +=1

    with open('user_data.txt', mode='w') as user_data:
        user_data.write(str(correct))

    # turtle.mainloop()

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

