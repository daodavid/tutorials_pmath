from turtle import *
import numpy as np


def draw_spiral():
    color('red', 'yellow')
    begin_fill()
    i = 0
    while True:
        forward(20)
        left(-i * 3)
        if abs(pos()) < 1 or i > 30:
            break
        i = i + 1
    end_fill()
    done()


def draw_line(lenght, angle_alfa):
    lenght = lenght * 100
    i = lenght * np.sin(angle_alfa)
    j = lenght * np.cos(angle_alfa)
    color('blue', 'red')
    begin_fill()
    pensize(10)
    forward(100)
    right(30)
    forward(100)
    end_fill()
    done()


def draw_triangle(a, b, c):
    a1 = np.sin(a / (a / 2))
    b1 = np.sin(b / (c / 2))
    color('blue', 'black')
    begin_fill()
    i = 0
    j = 0


# draw_spiral()


def draw_branch(branch_length, angle, tick):
    if branch_length > 5:
        forward(branch_length)
        right(angle)

        pensize(tick)

        if (tick <= 10):
            color('red', 'yellow')
        if (tick <= 0.5):
            color('green', 'yellow')
        draw_branch(branch_length - 15, angle, tick / 2)
        left(2 * angle)

        draw_branch(branch_length - 15, angle, tick / 2)
        right(angle)
        pensize(tick)
        if(tick>10):
           color('brown', 'brown')
        backward(branch_length)


def draw_tree(trunk_length, angle):
    color('brown', 'yellow')
    thick = trunk_length / 5;
    speed("fastest")
    left(90)
    up()
    backward(trunk_length)
    down()
    draw_branch(trunk_length, angle, thick)
    done()


draw_tree(100, 30)
# draw_line(10, 30)
