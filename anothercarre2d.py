# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from derivation import *
from draw_2d import *

tree = "-L"
remp = {"L":"LF+RFR+FL-F-LFLFL-FRFR+", "R":"-LFLF+RFRFR+F+RF-LFL-FR"}


res = derivation(tree, remp, 3)

draw_turtle(res, 90,[], -100, -200, 8)
