import turtle
from turtle import *
import time

import custommodules as cs

## 1 - красный 2 - синий 3 - зеленый
## F - заливка (нужна завершенная фигура)
## W A S D - ВВЕРХ ВЛЕВО ВНИЗ ВПРАВО (100)

height = 900
width = 700

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (92, 194, 91)
NICE_GREEN = (112, 196, 118)
RED = (194, 51, 25)
NICE_RED = (219, 121, 121)
NICE_TEAL = (119, 146, 189)
NICE_BRIGHT_YELLOW = (251, 255, 222)

screen = Screen()
screen.setup(width, height)
t = Turtle()
screen.tracer(0)
screen.listen()
colormode(255)

t.width(5)
t.shape('circle')
t.speed(0)
t.move_x = 0
t.move_y = 0

t_dot = Turtle()
t_dot.teleport(190, 380)
t_dot.hideturtle()
t_dot.dot(10, "black")


def draw_small_box(t, step, main_color):
    t.begin_fill()
    t.width(3)

    if bgcolor() == "black":
        t.color((255,255,255), main_color)
    else:
        t.color((0,0,0), main_color)
    for _ in range(4):
        t.forward(step)
        t.right(90)
    t.end_fill()
    t.width(5)

def draw(x, y):
    t.goto(x, y)


def move(x, y):
    cs.move(t, x, y)



colors = {
        "1": "red",
        "2": "blue",
        "3": "green",
        "4": "yellow",
        "5": "black"
    }

def color(key):
    t.color(colors[key])

def width_change(key):
    step = 5
    if key == "+" and t.width() < 30:
        t.width(min(30, t.width() + step))
        t_dot.dot(min(80, t.width() * 2), t.color()[1])
    elif key == "-" and t.width() > 1:
        t.width(max(1, t.width() - step))
        t_dot.clear()
        t_dot.dot(max(10, t.width() * 2), t.color()[1])

def background_change(key):
    if key == "g" and screen.bgcolor() == "white":
        screen.bgcolor("black")
        t.color("white")
        ui("white")

    elif key == "g" and screen.bgcolor() == "black":
        screen.bgcolor("white")
        t.color("black")
        ui("black")


def on_press(key):
    if key == "w":
        t.move_y = 1
    elif key == "s":
        t.move_y = -1
    elif key == "a":
        t.move_x = -1
    elif key == "d":
        t.move_x = 1

def on_release(key):
    if key == "w" and t.move_y == 1:
        t.move_y = 0
    elif key == "s" and t.move_y == -1:
        t.move_y = 0
    elif key == "a" and t.move_x == -1:
        t.move_x = 0
    elif key == "d" and t.move_x == 1:
        t.move_x = 0


def drawline(key):
    t.goto(t.xcor() + 5, t.ycor() + 5)

for i, (key, color) in enumerate(colors.items()):
    screen.onkey(lambda c=color: t.color(c), key)



screen.onkeypress(lambda: on_press("w"), "w")
screen.onkeypress(lambda: on_press("s"), "s")
screen.onkeypress(lambda: on_press("a"), "a")
screen.onkeypress(lambda: on_press("d"), "d")

screen.onkeyrelease(lambda: on_release("w"), "w")
screen.onkeyrelease(lambda: on_release("s"), "s")
screen.onkeyrelease(lambda: on_release("a"), "a")
screen.onkeyrelease(lambda: on_release("d"), "d")

fill_turn = True
def fill():
    global fill_turn

    if fill_turn:
        t.begin_fill()
        fill_turn = False
    elif not fill_turn:
        t.end_fill()
        fill_turn = True

screen.onkey(fill, "f")
screen.onkey(t.clear, "space")
screen.onkey(lambda: width_change("+"), "=")
screen.onkey(lambda: width_change("-"), "-")
screen.onkey(lambda: background_change("g"), "g")

t.ondrag(draw)
screen.onclick(move)

# draw ui
def ui(border_color):
    t_ui = Turtle()
    t_ui.clear()
    t_ui.color(border_color)
    t_ui.width(5)
    t_ui.teleport(-350, 330)
    t_ui.forward(700)
    t_ui.teleport(5, 330)
    t_ui.setheading(90)
    t_ui.forward(400)
    for i in range(5):
        step_off = 70
        t_ui.teleport(-340 + step_off * i, 350)
        draw_small_box(t_ui, 50, colors[str(i + 1)])
    t_ui.teleport(65, 330)
    t_ui.setheading(90)
    t_ui.forward(80)
    t_ui.teleport(5, 330 + 80)
    t_ui.setheading(0)
    t_ui.forward(140)

    color_bw = ["white", "black"]
    for i in range(2):
        step_off = 35
        t_ui.teleport(20, 400 - step_off * i)
        draw_small_box(t_ui, 30, color_bw[i])

    t_ui.teleport(145, 330)
    t_ui.setheading(90)
    t_ui.forward(230)


    # Компас WASD — все элементы относительно центра квадрата
    center_x = 105
    center_y = 365


    t_ui.teleport(center_x - 2, center_y + 15)
    t_ui.write("↑", align="center", font=("Arial", 15, "normal"))

    t_ui.teleport(center_x - 25, center_y - 3)
    t_ui.write("←", align="center", font=("Arial", 15, "normal"))

    t_ui.teleport(center_x + 25, center_y - 3)
    t_ui.write("→", align="center", font=("Arial", 15, "normal"))

    t_ui.teleport(center_x - 2, center_y - 24)
    t_ui.write("↓", align="center", font=("Arial", 15, "normal"))

    # Клавиши WASD
    t_ui.teleport(center_x - 2, center_y + 2)
    t_ui.write("W", align="center", font=("Arial", 8, "normal"))

    t_ui.teleport(center_x - 10, center_y - 2)
    t_ui.write("A", align="center", font=("Arial", 8, "normal"))

    t_ui.teleport(center_x + 8, center_y - 2)
    t_ui.write("D", align="center", font=("Arial", 8, "normal"))

    t_ui.teleport(center_x - 2, center_y - 8)
    t_ui.write("S", align="center", font=("Arial", 8, "normal"))

    t_ui.hideturtle()
    t_ui.teleport(190, 420)
    t_ui.write("Width", align="center", font=("Arial", 20, "normal"))
    t_ui.teleport(155, 380)
    t_ui.write("+", align="center", font=("Arial", 15, "normal"))
    t_ui.teleport(225, 380)
    t_ui.write("-", align="center", font=("Arial", 15, "normal"))

    t_ui.teleport(75, 415)
    t_ui.write("Controls", align="center", font=("Arial", 20, "normal"))

    t_ui.teleport(-340, 415)
    t_ui.write("Press 'G' to change background color", align="left", font=("Arial", 15, "normal"))


    for i in range(0, 5):
        t_ui.color("grey")
        t_ui.teleport(-325 + 70 * i, 350)
        t_ui.write(str(i + 1), align="left", font=("Arial", 30, "normal"))

ui("black")

while True:
    new_x = t.xcor() + t.move_x * 10
    new_y = t.ycor() + t.move_y * 10

    # Ограничение движения границами экрана (300х300 от центра)
    if -350 < new_x < 350:
        t.setx(new_x)
    if -400 < new_y < 330:
        t.sety(new_y)


    screen.update()
    time.sleep(0.01)
