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
from draw import draw_cylinder, draw_apple
from matrix_rotation import RU, RL, RH
from derivation import derivation, stock_derivation, iteration_random
from draw3dleaf import draw_leaf, draw_flower

'''
pattern initialisation
'''
angled0=22.5
pattern0 = "^FA"
iteration0 = 6
remplacement0 = {"A":"!![LB]<<<<[LB]<<<<[LB]<<<<B", "B":"&LFLFA"}


'''
pattern initialisation
'''
angled1=22.5
pattern1 = "A"
iteration1 = 4
remplacement1 = {"A":"[&FL!A]<<<<<'[&FL!A]<<<<<<<'[&FL!A]", "F":"S<<<<<F", "S":"FL", "L":""}


'''
pattern initialisation
'''
angled2=22.5
pattern2 = "^FA"
iteration2 = 6
remplacement2 = {"A":"!![LLLBf]<<<<[LLLB]<<<<[LLLBf]<<<<B", "B":"&LLLFLLLFA"}


'''
pattern initialisation
'''
angled3=22.5
pattern3 = "^FA"
iteration3 = 6
remplacement3 = {"A" : {0.33 : "!![LLLBf]<<<<[LLLB]<<<<[LLLBf]<<<<B",
                       0.66 : "[&FL!A]<<<<<'[&FL!A]<<<<<<<'[&FL!A]",
                       1 : "!![LB]<<<<[LB]<<<<[LB]<<<<B"},
                "B" : {0.5 : "&LLLFLLLFA",
                       1 : "&LFLFA"}}


'''
pattern initialisation
'''
angled4=22.5
pattern4 = "F[^FA][&FC]"
iteration4 = 6
remplacement4 = {"A":"!!![LLLBf]<<<<[LLLB]<<<<[LLLBf]<<<<B", "B":"^LLLFLLLFpA", "C" : "!!![LLLDf]>>>>[LLLD]>>>>[LLLDf]>>>>D", "D" : "&LLLFLLLFpC"}


'''
pattern initialisation
'''
angled5=22.5
pattern5 = "F[^FA][&FC]"
iteration5 = 6
remplacement5 = {"A":"!!![LLLBf]<<<<[LLLB]<<<<[LLLBf]<<<<B", "B":"^LLLFLLLFpA", "C" : "!!![LLLDf]>>>>[LLLD]>>>>[LLLDf]>>>>D", "D" : "&LLLFLLLFpC"}


# pattern, remplacement, nbiterationm=, gauss_nb_iteration, stocastic?, angle, gauss_len, gauss_angle
dico = {0 : [pattern0, remplacement0, iteration0, 1.5, 0, angled0, 0.2, 0.05],
        1 : [pattern1, remplacement1, iteration1, 1.5, 0, angled1, 0.2, 0.05],
        2 : [pattern2, remplacement2, iteration2, 1.5, 0, angled2, 0.2, 0.05],
        3 : [pattern3, remplacement3, iteration3, 1.5, 1, angled3, 0.2, 0.05],
        4 : [pattern4, remplacement4, iteration4, 1.5, 0, angled4, 0.2, 0.05],
        5 : [pattern5, remplacement5, iteration5, 1.5, 0, angled5, 0.2, 0.05]}

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
        angleg = angle + random.gauss(0, randomangle)
        if (i == "F"):
            g = random.gauss(0, randomdist)
            D = [M[0][0] + g, M[0][1] + g, M[0][2] + g]
            newloc = np.add(loc, D)
            draw_cylinder(loc, newloc, diameter, mat)
            loc = newloc
        elif (i == "+"):
            M = np.dot(M, RL(angleg))
        elif (i == "-"):
            M = np.dot(M, RL(-angleg))
        elif (i == "<"):
            M = np.dot(M, RU(-angleg))
        elif (i == ">"):
            M = np.dot(M, RU(angleg))
        elif (i == "&"):
            M = np.dot(M, RH(angleg))
        elif (i == "^"):
            M = np.dot(M, RH(-angleg))
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
        elif (i == "p"):
            draw_apple(loc)

def draw_random(dico, loc):
    n = random.randint(0, len(dico) - 1)
    res = dico[n]
    iteration = iteration_random(res[2], res[3])
    if res[4]:
        deriv = stock_derivation(res[0], res[1], iteration)
    else:
        deriv = derivation(res[0], res[1], iteration)
    draw_gauss(deriv, res[5], loc, res[6], res[7])

def draw_random_forest(dico, n):
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

#if tree_number == -1 then the tree is chosen at random from all trees in the dico
def draw_unique_forest(dico, n, tree_number=-1):
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

        if (tree_number==-1):
            tree_number = random.randint(0, len(dico) - 1)
        res = dico[tree_number]

        iteration = iteration_random(res[2], res[3])
        if res[4]:
            deriv = stock_derivation(res[0], res[1], iteration)
        else:
            deriv = derivation(res[0], res[1], iteration)
        draw_gauss(deriv, res[5], loc, res[6], res[7])

        n = n - 1

#pour dessiner un seul abre
draw_gauss(derivation(pattern4, remplacement4, 5), angled4, [0,0,0], 0.2, 0.05)
#pour dessiner un arbre random dans le dico
#draw_random(dico, [0,0,0])
#pour dessiner une foret d'une espece (l'espece est son numero dans le dico)
#draw_unique_forest(dico, 1, 0)
#pour dessiner une foret de n arbre random dans le dico
#draw_random_forest(dico, 1)
