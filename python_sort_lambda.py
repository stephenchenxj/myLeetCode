#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:32:00 2020

@author: stephenchen
"""


chars = ['a','b','f','g', 'y', 'x']
#print(chars)

dis = dict()
for i, c in enumerate(chars, -3 ): # c in chars, i starts from -3
    dis[i] = c
print('Given a dictionary:')
print(dis)

print('Sort the items. Default sort by key:')
items_byKey = sorted(dis.items())
print(items_byKey)
print('Sort the items. use lambda function, sort by key**2:')
items_byKey2 = sorted(dis.items(), key = lambda x:x[0]**2)
print(items_byKey2)
print('Sort the items. use lambda function, sort by value:')
items_byValue = sorted(dis.items(), key = lambda x:x[1])
print(items_byValue)


print('items_byValue is sorted by Value. Let us check:')
for item in items_byValue:
    print(dis[item[0]])


    
