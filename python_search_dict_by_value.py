#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:06:15 2020

@author: chen
"""

mydict = {1:'a', 2:'b', 3:'a'}
value = 'a'
keys = [ key for key,val in mydict.items() if val==value ]
print(keys)