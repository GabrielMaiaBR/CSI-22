import turtle


def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


wn = turtle.Screen()
turtle = turtle.Turtle()
turtle.width(3)
turtle.pencolor("salmon")
wn.bgcolor("lightgreen")

draw_poly(turtle, 8, 50)
wn.mainloop()
