import turtle


def draw_spiral(turtle, turn_angle):
    sz = 2
    for i in range(100):
        turtle.right(turn_angle)
        turtle.forward(sz)
        sz += 2


wn = turtle.Screen()
turtle = turtle.Turtle()
turtle.pencolor("blue")
wn.bgcolor("lightgreen")

draw_spiral(turtle, 90)

turtle.penup()
turtle.goto(300, 0)
turtle.pendown()

draw_spiral(turtle, 89)

wn.mainloop()
