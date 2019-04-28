# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

from draw_2d import *
from derivation import *

tree = "F"
remp = {"F" : {0.33 : "C1F[+C2F]F[-C3F]C1F", 0.66 : "C1F[-C3F]C1F", 1 : "C1F[+C2F]C1F"}}
res = stock_derivation(tree, remp, 5)
color = ["#654321","#017201", "#448918", "#5BBA1F"]
draw_turtle(res, 25, color)

