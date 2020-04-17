#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:13:27 2020

@author: chen

231. Power of Two
Easy

654

165

Add to List

Share
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
Accepted
281,644
Submissions
656,228
"""


class Solution(object):
    def isPowerOfTwo2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n%2 == 0: 
            n /= 2
        if n == 1:
            return True
        else:
            return False
            
            
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        for i in range(32):
            if n >1:
                if n & 0x01 == 1:
                    return False
            else:
                return True

            n=n>>1
        
    
n = 0
print(Solution().isPowerOfTwo(n))
print(Solution().isPowerOfTwo2(n))


