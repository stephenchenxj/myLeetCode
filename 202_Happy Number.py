#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:33:29 2020

@author: chen


202. Happy Number
Easy

1876

397

Add to List

Share
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Accepted
473,956
Submissions
950,491


"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        appeared = dict()
        return self.helper(n, appeared)
        
    def helper(self, n, appeared):
        if n == 1:
            return True
        
        print(appeared)
        print(n)
        if appeared.get(n) != None:
            return False
        else:
            appeared[n] = True
            
        m = 0
        while n != 0:
            m += (n % 10)**2
            n = n//10

            
        return self.helper(m, appeared)
    
    
n = 81
print(Solution().isHappy(n))