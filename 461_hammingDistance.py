#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:02:34 2020

@author: stephenchen

461. Hamming Distance
Easy

1556

150

Add to List

Share
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
Accepted
287,106
Submissions
403,019

"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        
        cnt = 0
        for i in range(32):
            cnt += (0x00000001 & z )
            z = z>>1
            
        return cnt
        
print(Solution().hammingDistance(2**31,2**31))