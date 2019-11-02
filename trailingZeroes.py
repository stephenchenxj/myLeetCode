# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 00:00:35 2019

@author: stephen.chen

Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.

"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n != 0:
            cnt +=n//5
            n = n//5
        return cnt
            
            
            
test = Solution()

print(test.trailingZeroes(25))

            
            
            