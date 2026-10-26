import turtle
import random

def move(operator, xlen, ylen):
    operator.setheading(0)
    operator.penup()
    operator.goto(xlen, ylen)
    operator.pendown()

def Random_Move(operator, xmin, xmax, ymin, ymax):
    move(
        operator,
        random.randint(xmin, xmax),
        random.randint(ymin, ymax)
    )

def writeFont(operator, text, fontsize=30):
    operator.clear()
    operator.write(text, font=("Arial", fontsize, "normal"))