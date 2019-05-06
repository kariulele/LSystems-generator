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
from derivation import derivation, stock_derivation, iteration_random
from draw3dleaf import draw_leaf, draw_flower

'''
pattern initialisation
'''
angled0=22.5
pattern0 = "^FA"
iteration0 = 5
remplacement0 = {"A":"!![LB]<<<<[LB]<<<<[LB]<<<<B", "B":"&LFLFA"}
'''
pattern computation
'''

'''
pattern initialisation
'''
angled1=22.5
pattern1 = "A"
iteration1 = 3
remplacement1 = {"A":"[&FL!A]<<<<<'[&FL!A]<<<<<<<'[&FL!A]", "F":"S<<<<<F", "S":"FL", "L":""}
'''
pattern computation
'''


'''
pattern initialisation
'''
angled2=22.5
pattern2 = "^FA"
iteration2 = 6
remplacement2 = {"A":"!![LLLBf]<<<<[LLLB]<<<<[LLLBf]<<<<B", "B":"&LLLFLLLFA"}
'''
pattern computation
'''

'''
pattern initialisation
'''
angled3=22.5
pattern3 = "^FA"
iteration3 = 5
remplacement3 = {"A" : {0.33 : "!![LLLBf]<<<<[LLLB]<<<<[LLLBf]<<<<B",
                       0.66 : "[&FL!A]<<<<<'[&FL!A]<<<<<<<'[&FL!A]",
                       1 : "!![LB]<<<<[LB]<<<<[LB]<<<<B"},
                "B" : {0.5 : "&LLLFLLLFA",
                       1 : "&LFLFA"}}
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
# pattern, remplacement, nbiterationm=, gauss_nb_iteration, stocastic?, angle, gauss_len, gauss_angle
dico = {0 : [pattern0, remplacement0, iteration0, 1.5, 0, angled0, 0.2, 0.5],
        1 : [pattern1, remplacement1, iteration1, 1.5, 0, angled1, 0.2, 0.5],
        2 : [pattern2, remplacement2, iteration2, 1.5, 0, angled2, 0.2, 0.5],
        3 : [pattern3, remplacement3, iteration3, 1.5, 1, angled3, 0.2, 0.5]}

def draw_gauss(pattern, angled, loc, randomdist, randomangle):
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

def draw_random(dico, loc):
    n = random.randint(0, len(dico) - 1)
    res = dico[n]
    iteration = iteration_random(res[2], res[3])
    if res[4]:
        deriv = stock_derivation(res[0], res[1], iteration)
    else:
        deriv = derivation(res[0], res[1], iteration)
    draw_gauss(deriv, res[5], loc, res[6], res[7])

def draw_forest(dico, n):
    if (n < 1 or n > 25):
        return

    forest = np.zeros([5, 5])
    loc = [0, 0, 0]
    draw_random(dico, loc)
    forest[2][2] = 1
    n = n - 1
    while n > 0:
        while True:
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            if forest[x][y] == 0:
                forest[x][y] = 1
                break
        loc = [(-2 + x) * 2, (-2 + y) * 2, 0]
        draw_random(dico, loc)
        n = n - 1

draw_gauss(derivation(pattern0, remplacement0, 5), angled2, [0,0,0], 0.2, 0.5)
#draw_random(dico, [0,0,0])
#draw_forest(dico, 1)
