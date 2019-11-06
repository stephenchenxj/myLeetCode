# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 05:42:56 2019

@author: stephen.chen

Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:

Input: numerator = 2, denominator = 1
Output: "2"

Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

   Hide Hint #1  
No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
   Hide Hint #2  
Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
   Hide Hint #3  
Notice that once the remainder starts repeating, so does the divided result.
   Hide Hint #4  
Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        ans = []
        fractional_part = []
        fractional_dict = dict()
        positive = (numerator < 0) is (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        int_part = numerator // denominator
        numerator = numerator % denominator
        ans.append(str(int_part))
#        print(int_part)
#        print(numerator)
        if numerator != 0:
            ans.append('.')
        index = 0
        repeated_loc = -1
        while numerator != 0:
            numerator *= 10   
            if numerator in fractional_dict.keys():
                repeated_loc = fractional_dict[numerator]
                break
            else:
                fractional_dict[numerator] = index
            fractional_part.append(str(numerator // denominator))
            numerator = numerator % denominator
#            print(numerator) 
            index += 1
#        print(fractional_part[repeated_loc:index+1]) 
        if repeated_loc == -1: # no repeated fractional part
            ans.extend(fractional_part)
        else: 
            if repeated_loc != 0:
                ans.extend(fractional_part[:repeated_loc])
            ans.append('(')
            ans.extend(fractional_part[repeated_loc:index])
            ans.append(')')
        if positive == False:
            temp = ['-']
            temp.extend(ans)
            ans = temp
        temp =''.join((ans))    
        return temp
            
test = Solution()

print(test.fractionToDecimal(1,19))
            
            
            
            
        

