#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:30:37 2019

@author: heldhy
"""
import numpy as np
import math
import bpy

def draw_cylinder(fr, to, r):
    dx = to[0] - fr[0]
    dy = to[1] - fr[1]
    dz = to[2] - fr[2]    
    dist = math.sqrt(dx**2 + dy**2 + dz**2)
    bpy.ops.mesh.primitive_cylinder_add(
      radius = r, 
      depth = dist,
      location = (dx/2 + fr[0], dy/2 + fr[1], dz/2 + fr[2])   
    ) 

    phi = math.atan2(dy, dx) 
    theta = math.acos(dz/dist) 
    bpy.context.object.rotation_euler[1] = theta 
    bpy.context.object.rotation_euler[2] = phi

def RU(angle):
    return [[math.cos(angle), math.sin(angle), 0],[-math.sin(angle), math.cos(angle), 0],[0, 0, 1]]

def RL(angle):
    return [[math.cos(angle), 0, -math.sin(angle)],[0, 1, 0],[math.sin(angle), 0, math.cos(angle)]]

def RH(angle):
    return [[1, 0, 0],[0, math.cos(angle), -math.sin(angle)],[0, math.sin(angle), math.cos(angle)]]

def derivation(pattern, rempl, iteration):
    res = pattern
    for k in range(iteration):
        pattern = res
        res = ""
        for i in pattern:
            if (i in rempl):
                res += rempl[i]
            else:
                res += i
    return res

'''
pattern initialisation
'''
angled = 90
pattern = "A"
iteration = 1
remplacement = {"A": "B-F+CFC+F-D&F∧D-F+&&CFC+F+B//", "B": "A&F∧CFB∧F∧D∧∧-F-D∧|F∧B|FC∧F∧A//", "C":"|D∧|F∧B-F+C∧F∧A&&FA&F∧C+F+B∧F∧D//", "D":"|CFB-F+B|FA&F∧A&&FB-F+B|FC//"}

'''
pattern computation
'''
res = derivation(pattern, remplacement, iteration)


def draw(pattern, angled):
    loc = [0, 0, 0]
    diameter = 0.1
    colorIndex = 0
    H = [1, 0, 0]
    L = [0, 1, 0]
    U = [0, 0, 1]
    M = [H, L, U]
    angle = math.radians(angled)
    rh = RH(angle)
    rl = RL(angle)
    ru = RU(angle)
    rhn = RH(-angle)
    rln = RL(-angle)
    run = RU(-angle)
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
            diameter -= 0.1
        elif (i == "'"):
            colorIndex += 1
        elif (i == "["):
            stack.append((M, loc))
        elif (i == "]"):
            M, loc = stack.pop()

draw(res, 90)


