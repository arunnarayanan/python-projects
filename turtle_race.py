import turtle as t
import random

tim = t.Turtle()
wn = t.Screen()

colors = ['red', 'green', 'blue', 'orange', 'black', 'yellow', 'cyan', 'purple']

wn.title('Welcome to the Turtle Race!')

wn.setup(width=500, height=500, startx=0, starty=0)
selection = wn.textinput("Selection", f"Who do you think will win? \n {colors}")

turtles = []
x, y = -200, -100

for i in range(8):
    new_turtle = t.Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x, y)
    turtles.append(new_turtle)
    y += 40

race_over = False

while not race_over:
    turtle = random.choice(turtles)
    turtle.fd(random.randint(1, 20))
    if turtle.distance(-200, 0) >= 450:
        if turtle.fillcolor() == selection:
            print('You won!')
        print(f'{turtle.fillcolor()} won the race')
        race_over = True

wn.exitonclick()
