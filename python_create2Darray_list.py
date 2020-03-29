#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:07:41 2020

@author: stephenchen
"""

rows = 3
cols = 4
rslt = [[0 for i in range(cols)] for j in range(rows)] 

print(rslt)

print(len(rslt))
print(len(rslt[0]))

print('each element is changable')
for i in range( rows):
    for j in range( cols):
        rslt[i][j] = i*cols + j

print(rslt)