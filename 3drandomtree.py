#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 19:42:40 2019

@author: kariulele
"""

import math
import random
import bpy
import numpy as np
from draw import draw_cylinder
from matrix_rotation import RU, RL, RH
from derivation import derivation, stock_derivation
from draw3dleaf import draw_leaf, draw_flower

'''
pattern initialisation
'''
angled0=22.5
pattern0 = "^FA"
iteration0 = 7
remplacement0 = {"A":"!![LB]<<<<[LB]<<<<[LB]<<<<B", "B":"&LFLFA"}
'''
pattern computation
'''

'''
pattern initialisation
'''
angled1=22.5
pattern1 = "A"
iteration1 = 4
remplacement1 = {"A":"[&FL!A]<<<<<'[&FL!A]<<<<<<<'[&FL!A]", "F":"S<<<<<F", "S":"FL", "L":""}
'''
pattern computation
'''


'''
pattern initialisation
'''
angled2=22.5
pattern2 = "^FA"
iteration2 = 7
remplacement2 = {"A":"!![LLLBf]<<<<[LLLB]<<<<[LLLBf]<<<<B", "B":"&LLLFLLLFA"}
'''
pattern computation
'''

'''
pattern initialisation
'''
angled3=22.5
pattern3 = "^FA"
iteration3 = 7
remplacement3 = {"A" : {0.33 : "!![LLLBf]<<<<[LLLB]<<<<[LLLBf]<<<<B",
                       0.66 : "[&FL!A]<<<<<'[&FL!A]<<<<<<<'[&FL!A]",
                       1 : "!![LB]<<<<[LB]<<<<[LB]<<<<B"},
                "B" : {0.5 : "&LLLFLLLFA",
                       0.5 : "&LFLFA"}}
'''
pattern computation
'''

'''
pattern initialisation
'''
angled=22.5
pattern = "A"
iteration = 5
remplacement = {""}
'''
pattern computation
'''
res = np.array([derivation(pattern0, remplacement0, iteration0),
                derivation(pattern1, remplacement1, iteration1),
                derivation(pattern2, remplacement2, iteration2),
                stock_derivation(pattern3, remplacement3, iteration3)])
loc = [0, 0, 0]

def draw_random(pattern, angled, loc, randomdist, randomangle):
    if (not("BRN" in bpy.data.materials)):
        mat = bpy.data.materials.new("BRN")
        mat.diffuse_color = (0.6,0.44,0.16)
    else:
        mat = bpy.data.materials["BRN"]
    diameter = 0.1
    colorIndex = 0
    H = [0, 0, 1]
    L = [1, 0, 0]
    U = [0, 1, 0]
    M = [H, L, U]
    angle = math.radians(angled)
    ru180 = RL(math.radians(180))
    stack = []
    for i in pattern:
        if (i == "F"):
            D = M[0] + random.gauss(0, randomdist)
            newloc = np.add(loc, D)
            draw_cylinder(loc, newloc, diameter, mat)
            loc = newloc
        elif (i == "+"):
            M = np.dot(M, RL(angle * random.gauss(0, randomangle)))
        elif (i == "-"):
            M = np.dot(M, RL(-angle * random.gauss(0, randomangle)))
        elif (i == "<"):
            M = np.dot(M, RU(-angle * random.gauss(0, randomangle)))
        elif (i == ">"):
            M = np.dot(M, RU(angle * random.gauss(0, randomangle)))
        elif (i == "&"):
            M = np.dot(M, RH(angle * random.gauss(0, randomangle)))
        elif (i == "^"):
            M = np.dot(M, RH(-angle * random.gauss(0, randomangle)))
        elif (i == "|"):
            M = np.dot(M, ru180)
        elif (i == "!"):
            diameter -= 0.01
        elif (i == "'"):
            colorIndex += 1
        elif (i == "["):
            stack.append((M, loc, diameter))
        elif (i == "]"):
            M, loc, diameter = stack.pop()
        elif (i == "L"):
            draw_leaf(loc)
        elif (i == "f"):
            draw_flower(loc, 3)

draw_random(res[3], angled3, loc, 0.2, 0.5)
