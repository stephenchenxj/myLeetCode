#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:17:42 2020

@author: chen
"""


# Python3 program for demonstration of clip() function 
 
# importing the numpy 
import numpy as np 
 
 
input_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
print ("The input array : ", input_array) 
 
output_array = np.clip(input_array, a_min =[50, 30, 20, 50, 20, 20, 80, 80, 100, 90], a_max = 70) 
print ("The output array : ", output_array)

output_array = np.clip(input_array, 0, a_max = 70) 
print ("The output array : ", output_array)