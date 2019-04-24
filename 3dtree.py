#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:30:37 2019

@author: heldhy
"""
import math
import bpy
import numpy as np
from draw import draw_pattern, draw_cylinder
from matrix_rotation import RU, RL, RH
from derivation import derivation


'''
pattern initialisation
'''

angled=22.5
pattern = "A"
iteration = 4
remplacement = {"A":"[&FL!A]/////'[&FL!A]///////'[&FL!A]", "F":"S///F", "S":"FL", "L":""}
'''
pattern computation
'''
res = derivation(pattern, remplacement, iteration)

def draw(pattern, angled):
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
    ru180 = RU(math.radians(180))
    stack = []
    for i in pattern:
        if (i == "F"):
            D = M[0]
            newloc = np.add(loc, D)
            draw_cylinder(loc, newloc, diameter)
            loc = newloc
        elif (i == "+"):
            M = np.dot(M, ru)
        elif (i == "-"):
            M = np.dot(M, run)
        elif (i == "/"):
            M = np.dot(M, rhn)
        elif (i == "\\"):
            M = np.dot(M, rh)
        elif (i == "&"):
            M = np.dot(M, rl)
        elif (i == "∧"):
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
        elif (i == "o"):
            bpy.ops.mesh.primitive_uv_sphere_add(size=0.1, location=loc)

draw(res, angled)

