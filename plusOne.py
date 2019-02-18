#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 20:42:15 2019

@author: dev
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        n = len(digits)
        
        if n == 0:
            return [1]
        
        #print(n)
        
        #print(digits[0:(n-1)])
        
        if digits[n-1] == 9:
            #print(digits[n-1]) 
            temp = self.plusOne(digits[0:(n-1)])
            temp.append(0)
            return temp
        else:
            digits[n-1] += 1
            #print(digits[n-1]) 
            return digits
            
        
        
        
        
        
def main():
    ret = Solution().plusOne([9,9,8,9])
    print(ret)
    
if __name__ == '__main__':
    main()