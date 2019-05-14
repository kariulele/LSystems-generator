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
from derivation import derivation, stock_derivation
from draw3dleaf import draw_leaf, draw_flower


'''
pattern initialisation
'''

angled=22.5
pattern = "F[^FA][&FC]"
iteration = 8
remplacement = {"A":{0.33 : "!![LLLBf]<<<<<<<<[LLLB]<<<<B", 0.66 : "!![LLLB]<<<[LLLBf]<<<[LLLB]<<<[LLLBf]<<<<B" ,1 : "!![LLLBf]<<<<[LLLB]<<<<[LLLBf]<<<<B"}, "B": {0.5 : "^LLLFLLLFpA", 1 : "^LLLFLLLFfA"}, "C" : {0.33: "!![LLLD]>>>>>>>>[LLLDf]>>>>D", 0.66: "!![LLLD]>>>[LLLDf]>>>[LLLD]>>>[LLLDf]>>>>D" , 1: "!![LLLDf]>>>>[LLLD]>>>>[LLLDf]>>>>D"}, "D" : {0.5 : "&LLLFLLLFfC", 1: "&LLLFLLLFpC"}}
'''
pattern computation
'''
res = stock_derivation(pattern, remplacement, iteration)

draw_straight(res, angled)