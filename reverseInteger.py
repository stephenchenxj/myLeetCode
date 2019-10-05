# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 00:44:11 2019

@author: stephen.chen
"""

'''
Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [−2^31,  2^31 -1]. For the purpose of 
this problem, assume that your function returns 0 when the reversed integer 
overflows.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        sign = 1
        
        if x < 0:
            sign = -1
            x= -1*x
        
            
        result = 0    
        while x > 0:
            y = x % 10
            x = int((x-y)/10)  
            result = result*10 + y
            
        result = sign*result
        
        if result < -2**31 or result > 2**31-1:
            return 0
        
        
        
        return result
            
        
        
def main():
    mySolution = Solution()
    print (mySolution.reverse(12030))
    
if __name__ == "__main__":
    main()