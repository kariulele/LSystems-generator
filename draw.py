#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:30:37 2019

@author: heldhy
"""
import numpy as np
import math
import bpy
from matrix_rotation import RH, RU, RL

def draw_cylinder(fr, to, r, color):
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
    if (color is not None):
        o = bpy.context.selected_objects[0] 
        o.active_material = color

def draw_pattern(pattern, angled):
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
        elif (i == "/" or i == "<"):
            M = np.dot(M, rhn)
        elif (i == "\\" or i == ">"):
            M = np.dot(M, rh)
        elif (i == "&"):
            M = np.dot(M, rl)
        elif (i == "∧" or i == "^"):
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