# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from derivation import *
from draw_2d import *

tree = "F"
remp = {"F":"F+F-F-F-G+F+F+F-F", "G":"GGG"}


res = derivation_replacement(tree, remp, 3)

draw_turtle(res, 90,[], 0, -200, 14)
