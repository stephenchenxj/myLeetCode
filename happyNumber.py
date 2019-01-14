#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 22:46:49 2019

@author: dev
"""

class Solution(object):
#    def __init__(self):
#        self.l = set()
    l = set()
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        print ('analyzing ' + str(n))
        self.l.add(n)
        
        result = self.sumSquares(n) 
        # if sum of the squares of its digits equals 1
        if result == 1:
            return True
        
        #else: 
        else:
            if result not in self.l:  
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
    
    n =13
    ret = Solution().isHappy(19)
    ret = Solution().isHappy(n)

    out = (ret)
    print (out)
    
    
if __name__ == '__main__':
    main()