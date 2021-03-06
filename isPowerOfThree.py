# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:46:05 2019

@author: stephen.chen
Power of Three

Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true

Example 2:

Input: 0
Output: false

Example 3:

Input: 9
Output: true

Example 4:

Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?

"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n <= 0:
        	return False

        while n % 3 == 0:        	
        	n = n / 3

        return True if n == 1 else False
            
mySolution = Solution()
print(mySolution.isPowerOfThree(19684))


        