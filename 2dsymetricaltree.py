# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from derivation import *
from draw_2d import *

tree = "X"
remp = {"F":"FF", "X":"F[+X][-X]FX"}


res = derivation(tree, remp, 7)

draw_turtle(res, 25.7, size=2, pen=1)
