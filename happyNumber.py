#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 22:46:49 2019

@author: dev

202. Happy Number
Easy

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Accepted
317,557
Submissions
657,838
"""

class Solution(object):
    def __init__(self):
        self.l = set()
    
#    l = set()  # should not use global variable. 
        
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        print ('analyzing ' + str(n))
        #self.l.add(n)  # should not add here without checking. 
        #add it only when the check result is not 1, and it doesn't exist before
        
        result = self.sumSquares(n) 
        # if sum of the squares of its digits equals 1
        if result == 1:
            return True
        
        #else: 
        else:
            if result not in self.l:
                #add it only when the check result is not 1, and it doesn't exist before
                self.l.add(result) 
                print (self.l)
                return self.isHappy(result)
            else:
                return False
        
    def sumSquares(self, n):
        result = 0
        for d in str(n):
            result += int(d)*int(d)
        print (result)
        return result

def stringToInt(input):
    return int(input)

def main():
#    import sys
#    def readlines():
#        for line in sys.stdin:
#            yield line.strip('\n')
#    lines = readlines()
#    while True:
#        try:
#            line = lines.next()
#            n = stringToInt(line)
#            
#            ret = Solution().isHappy(n)
#
#            out = (ret)
#            print (out)
#        except StopIteration:
#            break
    import sys
    
    
    ret = Solution().isHappy(19)
    out = (ret)
    print (out)
    ret = Solution().isHappy(13)

    out = (ret)
    print (out)
    
    
if __name__ == '__main__':
    main()