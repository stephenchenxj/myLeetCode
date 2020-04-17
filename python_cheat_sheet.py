#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:19:48 2020

@author: chen
"""

strList = ['1', '2', '3', '4', 'a', 'b', '.', 'z']
string = ':'.join(strList)
print(string)

string = ''.join(strList)
print(string)

print(type(strList))

def convert(lst): 
    return ' '.join(lst).split() 
      
  
# Driver code 
lst =  ['Hello, Geeks for geeks'] 
print( convert(lst)) 


for i, s in enumerate(strList):
    print('strList['+str(i)+']=' + s)


print(int('011', 2)) 	
print(int('0b11', 2)) 	
print(int('011', 8)) 	
print(int('11', 8)) 	
print(int('0x11', 16)) 	
print(int('011', 16)) 	
print(int('0b11', 16)) 	


mydict = {1:'a', 2:'b', 3:'a', 0:'z'}
keys=sorted(mydict)
print(mydict)
print(keys)


keys = sorted(mydict, key=mydict.get)
print(keys)

v = (mydict.get(0))
print(v)
v = (mydict.get(4, 'new'))
print(v)


for key, value in sorted(mydict.items(), key=lambda kv: kv[1], reverse=False):
    print("%s: %s" % (key, value))
    
kv = sorted(mydict.items(), key=lambda kv: kv[1], reverse=False)
keys, values = zip(*kv)
print(type(keys))
print(list(keys))
print(list(values))


list_a = [1, 2, 3, 0]
list_b = ['a', 'b', 'a', 'z']
mydict = dict(zip(list_a, list_b))
print(mydict)
list_tuple = list(zip(list_a, list_b))
print(list_tuple)


print(mydict.get(2))
print(mydict)
print(mydict.get(100))
print(mydict.get(100, 'default'))

d2 = {0:'updated value', 4:'new value', 5:'new value', 1:'updated value'}
mydict.update(d2)
print(mydict)

del mydict[4]
print(mydict)

for k, v in dict(mydict).items():
        if v == 'updated value':
            del mydict[k]
print(mydict)

newdict = {k:v for k, v in mydict.items() if v!='new value'}
print(newdict)
print(mydict)

print(mydict.pop(2)) 
#print(mydict.pop(22)) 
print(mydict.pop(22, 'default')) 


newdict.clear()
print(newdict)
if not newdict:
    print("Empty")
else:
    print("Not empty")

# import sys
# maxv = (sys.maxsize)
# minv = -sys.maxsize -1
# print(maxv)
# print(minv)
print(float('inf'))
print(float('-inf'))
if 10**100000 > float('inf'):
    print('>')
else:
    print('<')
    
import copy
a = [[1,2],[3,4],5]
b = a
c = a[:] #shallow copy
d = copy.deepcopy(a) # deep copy
s = copy.copy(a)  #shallow copy
a[0][0] = 9
a[2] = 8
print(b)
print(c)
print(d)
print(s)


lst = [[1,'z', 'b'], [3,'a','c'],[5,'a','a'], [2, 'a','a']]
lst.sort(key = lambda x:x[0])
print(lst)
lst.sort(key = lambda x:x[1:])
print(lst)


lst = list(range(2,6))
print(lst)
lst = [1]*3
lst[0] = 2
print(lst)

