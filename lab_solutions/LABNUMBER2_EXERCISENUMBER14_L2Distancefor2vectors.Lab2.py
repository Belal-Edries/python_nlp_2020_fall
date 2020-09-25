#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2020 Belal Edries <edries.belal.95@edu.bme.hu>

def l2_distance(vector1, vector2):
    # (x1,y1) , (x2,y2)
    xdiff=pow((vector1[0]-vector2[0]),2)
    ydiff=pow((vector1[1]-vector2[1]),2)
    l2distance = pow((xdiff+ydiff),0.5)
    return l2distance

assert abs(l2_distance([1, 0], [1, 0]) - 0) < 1e-5
assert abs(l2_distance([1, 0], [0, 1]) - 2 ** 0.5) < 1e-5