# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle as tl

def draw(tree, angle):
    color = ["#654321","#017201", "#448918", "#5BBA1F"]
    stack = []
    tl.up()
    tl.left(90)
    tl.setpos(0, -350)
    tl.down()
    tl.pensize(2)
    j = -1
    for i in tree:
        j += 1
        if (i == "F"):
            tl.forward(8);
        elif (i == "+"):
            tl.left(angle)
        elif (i == "-"):
            tl.right(angle)
        elif(i == "["):
            stack.append((tl.position(), tl.heading()))
        elif (i == "]"):
            tl.up()
            ((x,y), t) = stack.pop()
            tl.setheading(t)
            tl.setpos(x, y)
            tl.down()
        elif (i == "C"):
            tl.pencolor(color[int(tree[j+1])])
    tl.up()
    tl.setpos(0,-350)
    tl.done()

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
    re = list(res)
    for i in range(len(re)):
        if(re[i] == "X"):
            re[i] = "F"
    return ''.join(re)

class Pat1L:
    def __init__(self, pattern, angle, iteration, ignore=None, lst=None):
        self.pattern = pattern
        self.angle = angle
        self.iteration = iteration
        if (lst is None):
            self.lst = []
        else:
           self.lst = lst
        if (ignore is None):
            self.ignore = []
        else:
            self.ignore = ignore
        self.res = pattern

    def get_prec(self, rank):
        i = rank - 1
        while (i >= 0):
            p = self.pattern[i]
            if (p in self.ignore or p == "["):
                i -= 1
            elif (p == "]"):
                br = 1
                while (br != 0):
                    i -= 1
                    q = self.pattern[i]
                    if (q == "["):
                        br -= 1
                    if (q == "]"):
                        br += 1
            else:
                return self.pattern[i]
        return None

    def get_next(self, rank):
        i = rank + 1
        while (i < len(self.pattern)):
            p = self.pattern[i]
            if (p in self.ignore):
                i += 1
            elif (p == "]"):
                return None
            elif (p == "["):
                br = 1
                while (br != 0):
                    i += 1
                    q = self.pattern[i]
                    if (q == "["):
                        br += 1
                    if (q == "]"):
                        br -= 1
            else:
                return self.pattern[i]
        return None

    def get_pattern(self, pv, cr, nt):
        for i in self.lst:
            if (i.cr == cr and (i.nt == nt or (i.nt == '*' and not(nt is None))) and (i.pv == pv or (i.pv == '*' and not(pv is None)))):
                print(pv + " " + cr + " " + nt + " => " + i.res)
                return i.res
        return None

    def iterate(self):
        while(self.iteration > 0):
            self.res = ""
            j = 0
            for i in self.pattern:
                if (not(i in ("[", "]"))):
                    pr = self.get_prec(j)
                    nt = self.get_next(j)
                    nw = self.get_pattern(pr, i, nt)
                    if (nw is None):
                        self.res += i
                    else:
                        self.res += nw
                else:
                    self.res += i
                j += 1
            self.iteration -= 1
            self.pattern = self.res


class ILr:
    def __init__(self, pv, cr, nt, res):
        self.pv = pv
        self.cr = cr
        self.nt = nt
        self.res = res


tree = "F"
remp = {"F":"F[+F]F[-F]F"}

tree2 = "X"
remp2 = {"X" : "C0F-[C2[X]+C3X]+C1F[C3+FX]-X", "F":"FF"}
res = derivation(tree, remp, 2)
print(res)

draw(res, 25)

'''
tree = Pat1L("F1F1F1", 22.5, 30, ["+", "-", "F"])
tree.lst.append(ILr("0", "0", "0", "1"))
tree.lst.append(ILr("0", "0", "1", "1[-F1F1]"))
tree.lst.append(ILr("0", "1", "0", "1"))
tree.lst.append(ILr("0", "1", "1", "1"))
tree.lst.append(ILr("1", "0", "0", "0"))
tree.lst.append(ILr("1", "0", "1", "1F1"))
tree.lst.append(ILr("1", "1", "0", "0"))
tree.lst.append(ILr("1", "1", "1", "0"))
tree.lst.append(ILr("*", "+", "*", "-"))
tree.lst.append(ILr("*", "-", "*", "+"))
tree.iterate()
draw(tree.res, tree.angle)
'''