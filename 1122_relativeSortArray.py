#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:31:54 2020

@author: stephenchen

1122. Relative Sort Array
Easy

465

34

Add to List

Share
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
 

Constraints:

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.
Accepted
43,939
Submissions
65,327

"""


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        hist = dict()
        for c in arr1:
            if c not in hist:
                hist[c] = 1
            else:
                hist[c] += 1
        rslt = []        
        for c in arr2:
            cnt = hist[c]
            for i in range(cnt):
                rslt.append(c)
            del hist[c]
        keys = list(hist.keys())
        keys.sort()
        for k in keys:
            cnt = hist[k]
            for i in range(cnt):
                rslt.append(k)
            
        print(rslt)
        return rslt
    
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
Solution().relativeSortArray(arr1, arr2)