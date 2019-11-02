# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 07:09:21 2019

@author: stephen.chen
Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:

Input: "A"
Output: 1

Example 2:

Input: "AB"
Output: 28

Example 3:

Input: "ZY"
Output: 701

"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for c in s:
            n = ord(c)-64
            result = n+result*26
        return result
            
test = Solution()
print(test.titleToNumber(''))

