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
from draw3dleaf import draw_leaf, draw_flower

def draw_straight(pattern, angled, color = 0):
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
            draw_flower(loc, color)
        elif (i == "p"):
            draw_apple(loc)

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

def draw_apple(location):
    if (not("brow" in bpy.data.materials)):
        mat = bpy.data.materials.new("brow")
        mat.diffuse_color = (0.55,0.27,0.074)
        red = bpy.data.materials.new("red")
        red.diffuse_color = (1,0,0)
    else:
        mat = bpy.data.materials["brow"]
        red = bpy.data.materials["red"]
    draw_cylinder(location, (location[0], location[1], location[2] - 0.15), 0.02, mat)
    loc = (location[0], location[1], location[2] - 0.2)
    bpy.ops.mesh.primitive_uv_sphere_add(size=0.12, location=loc)
    o = bpy.context.selected_objects[0] 
    o.active_material = red