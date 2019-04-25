# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

from draw_2d import *
from derivation import *

tree = "F"
remp = {"F" : {1 : "C0FF-[C1-F+F+F]+[C2+F-F-F]"}}
res = stock_derivation(tree, remp, 4)
color = ["#654321", "#448918", "#5BBA1F"]
draw_turtle(res, 22, color, -100)

