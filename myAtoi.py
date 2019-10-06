# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 05:08:07 2019

@author: stephen.chen
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        start = 0
        sign = 1
        result = 0
        for c in str:
            if c == ' ':
                if start == 1:
                    break
                continue
            #start = 1 #find the first none-space character, start convertion
            if c.isalpha():
                break
            if c == '.':
                break
            
            if c == '-' :
                if start == 1: # have sign before:
                    break
                sign = -1
                start = 1
                continue
            elif c == '+' :
                if start == 1: # have sign before:
                    break
                sign = 1
                start = 1
                continue
                
            start = 1 #find the first none-space character, start convertion     
            if c.isdigit():
                result = result*10 + int(c)                
        result = result * sign        
        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        return result
    
                
        
        
def main():
    mySolution = Solution()
    print(mySolution.myAtoi("   -1+4"))
    
    
if __name__ == '__main__':
    main()