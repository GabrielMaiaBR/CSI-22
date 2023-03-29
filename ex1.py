import turtle


def draw_square(turtle, side):
    for i in range(5):
        turtle.penup()
        turtle.goto(-side/2, -side/2)
        turtle.pendown()
        for j in range(4):
            turtle.forward(side)
            turtle.left(90)
        side += 20


wn = turtle.Screen()
turtle = turtle.Turtle()
turtle.width(3)
turtle.pencolor("salmon")
wn.bgcolor("lightgreen")

draw_square(turtle, 20)
wn.mainloop()
