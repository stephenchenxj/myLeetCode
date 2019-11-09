# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 03:20:55 2019

@author: stephen.chen

Sum of Two Integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = -2, b = 3
Output: 1


"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK    = 0x100000000
        
        carry = b
        add = a
        while carry:
            '''
            add = (a%MASK) ^ (carry%MASK)   
            carry = (a%MASK) & (carry%MASK)
            carry <<= 1
            a = add
            '''
            
            add = (a%MASK) ^ (carry%MASK)   
            carry = (a%MASK) & (carry%MASK)
            carry <<= 1
            a = add
        
        if a <= MAX_INT:
            return a 
        else:
            return ~((a % MIN_INT) ^ MAX_INT) 
        
        
test = Solution()
print((test.getSum(-00, -1)))

def hexToSignedInt32(a):
    MAX_INT = 0x7FFFFFFF
    MIN_INT = 0x80000000
    MASK    = 0x100000000
    if a <= MAX_INT:
        return a
    else:
        return ~(a%MIN_INT)^MAX_INT
    
print(hexToSignedInt32(0x80fffffe))
    
    