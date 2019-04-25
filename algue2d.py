# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from derivation import *
from draw_2d import *


tree = "F"
remp = {"F":"F[+F]F[-F]F"}


res = derivation(tree, remp, 4)

draw_turtle(res, 25,[])
