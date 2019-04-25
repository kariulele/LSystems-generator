# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

from draw_2d import *
from derivation import *

tree = "X"
remp = {"X" : {1 : "C0F-[C2[X]+C3X]+C1F[C3+FX]-X"}, "F": {1 : "FF"}}
res = stock_derivation(tree, remp, 5)
color = ["#654321","#017201", "#448918", "#5BBA1F"]
draw_turtle(res, 25, color)

