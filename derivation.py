#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:30:37 2019

@author: heldhy
"""

import random

def derivation_replacement(pattern, rempl, iteration):
    res = derivation(pattern, rempl, iteration)
    re = list(res)
    for i in range(len(re)):
        if(re[i] in rempl):
            re[i] = "F"
    return ''.join(re)

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

def stock_derivation(pattern, rempl, iteration):
    r = random.Random()
    res = pattern
    for k in range(iteration):
        pattern = res
        res = ""
        for i in pattern:
            if (i in rempl):
                proba = r.random()
                l = list(rempl[i].keys())
                l.sort()
                for u in l:
                    if (proba <= u):
                        res += rempl[i][u]
                        break
            else:
                res += i
    return res
