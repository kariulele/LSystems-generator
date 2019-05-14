#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:30:37 2019

@author: heldhy
"""
import math
import bpy
import numpy as np
from draw import draw_pattern, draw_cylinder, draw_straight
from matrix_rotation import RU, RL, RH
from derivation import derivation
from draw3dleaf import draw_leaf, draw_flower


'''
pattern initialisation
'''

angled=22.5
pattern = "F[^FA][&FC]"
iteration = 6
remplacement = {"A":"!!![LLLBf]<<<<[LLLB]<<<<[LLLBf]<<<<B", "B":"^LLLFLLLFpA", "C" : "!!![LLLDf]>>>>[LLLD]>>>>[LLLDf]>>>>D", "D" : "&LLLFLLLFpC"}
'''
pattern computation
'''
res = derivation(pattern, remplacement, iteration)

draw_straight(res, angled)