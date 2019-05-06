#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:30:37 2019

@author: heldhy
"""
import math
import bpy
import numpy as np
from draw import draw_cylinder
from matrix_rotation import RU, RL, RH
from derivation import derivation
from draw3dleaf import draw_leaf, draw_flower

'''
pattern initialisation
'''

angled=22.5
pattern = "^FA"
iteration = 7
remplacement = {"A":"!![LLLBf]<<<<[LLLB]<<<<[LLLBf]<<<<B", "B":"&LLLFLLLFA"}
'''
pattern computation
'''
res = derivation(pattern, remplacement, iteration)

def draw(pattern, angled):
    if (not("BRN" in bpy.data.materials)):
        mat = bpy.data.materials.new("BRN")
        mat.diffuse_color = (0.6,0.44,0.16)
    else:
        mat = bpy.data.materials["BRN"]
    loc = [0, 0, 0]
    diameter = 0.1
    colorIndex = 0
    H = [0, 0, 1]
    L = [1, 0, 0]
    U = [0, 1, 0]
    M = [H, L, U]
    angle = math.radians(angled)
    rh = RU(angle)
    rl = RH(angle)
    ru = RL(angle)
    rhn = RU(-angle)
    rln = RH(-angle)
    run = RL(-angle)
    ru180 = RL(math.radians(180))
    stack = []
    for i in pattern:
        if (i == "F"):
            D = M[0]
            newloc = np.add(loc, D)
            draw_cylinder(loc, newloc, diameter, mat)
            loc = newloc
        elif (i == "+"):
            M = np.dot(M, ru)
        elif (i == "-"):
            M = np.dot(M, run)
        elif (i == "<"):
            M = np.dot(M, rhn)
        elif (i == ">"):
            M = np.dot(M, rh)
        elif (i == "&"):
            M = np.dot(M, rl)
        elif (i == "^"):
            M = np.dot(M, rln)
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

draw(res, angled)

