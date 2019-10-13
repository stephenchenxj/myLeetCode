# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 03:09:29 2019

@author: stephen.chen

Hamming Distance

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

"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        dist = 0
        while x or y:
            if (x & 1) != (y & 1):
                dist += 1
            if x:
                x = x >> 1
            if y:
                y = y >> 1
        return dist
            
test = Solution()
print(test.hammingDistance(0b1, 0b100))