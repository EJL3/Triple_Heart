import turtle

turtle.bgcolor("black")
turtle.pensize(5)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(0)
turtle.color("pink", "red")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()

#2        
turtle.bgcolor("black")
turtle.pensize(5)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(0)
turtle.color("pink", "indigo")

turtle.begin_fill()
turtle.left(45)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()

#3        
turtle.bgcolor("black")
turtle.pensize(5)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(0)
turtle.color("pink", "violet")

turtle.begin_fill()
turtle.left(30)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
        
