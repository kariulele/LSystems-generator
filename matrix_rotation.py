#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:30:37 2019

@author: heldhy
"""
import math

def RU(angle):
    return [[math.cos(angle), -math.sin(angle), 0],[math.sin(angle), math.cos(angle), 0],[0, 0, 1]]

def RL(angle):
    return [[math.cos(angle), 0, -math.sin(angle)],[0, 1, 0],[math.sin(angle), 0, math.cos(angle)]]

def RH(angle):
    return [[1, 0, 0],[0, math.cos(angle), -math.sin(angle)],[0, math.sin(angle), math.cos(angle)]]
