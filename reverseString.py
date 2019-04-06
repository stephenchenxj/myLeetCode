#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:09:51 2019

@author: dev
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = 0
        j = n-1
        
        while(i<j):
            temp = s[j]
            s[j] = s[i]
            s[i] = temp
            i+=1
            j-=1
        
        #return s
        
def main():
    s = ["h","e","l","l","o"]
    (Solution().reverseString(s))
    print(s)
    
if __name__ == '__main__':
    main()