# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle as tl

def draw_turtle(tree, angle, color=[], posx=0, posy=-350, size=8):
    stack = []
    tl.up()
    tl.left(90)
    tl.setpos(posx, posy)
    tl.down()
    tl.pensize(2)
    j = -1
    for i in tree:
        j += 1
        if (i == "F"):
            tl.forward(size);
        elif (i == "+"):
            tl.left(angle)
        elif (i == "-"):
            tl.right(angle)
        elif(i == "["):
            stack.append((tl.position(), tl.heading()))
        elif (i == "]"):
            tl.up()
            ((x,y), t) = stack.pop()
            tl.setheading(t)
            tl.setpos(x, y)
            tl.down()
        elif (i == "C"):
            tl.pencolor(color[int(tree[j+1])])
    tl.up()
    tl.setpos(0,-350)
    tl.done()
