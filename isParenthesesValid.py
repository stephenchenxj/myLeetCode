#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 20:38:28 2019

@author: dev
"""

class Solution(object):
    def isParenthesesValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.stack = []
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                self.stack.append(c)
            else:
                right = c
                if self.stack: # stack is not empty
                    left = self.stack.pop()
                else:
                    return False
                if not self.isMatch(left, right) :
                    return False
                
        if self.stack != []:
            return False
        else:
            return True
                
            
        
    def isMatch(self, left, right):
        if left == '(':
            if right == ')':
                return True
            else:
                return False
    
        if left == '[':
            if right == ']':
                return True
            else:
                return False
            
        if left == '{':
            if right == '}':
                return True
            else:
                return False
            
            
        
        
        
def main():
    inpt = "[]"
    print (Solution().isParenthesesValid(inpt))
    
    inpt = "()[]{}"
    print (Solution().isParenthesesValid(inpt))
    
    inpt = "{[]}"
    print (Solution().isParenthesesValid(inpt))
    
    inpt = "{[)}"
    print (Solution().isParenthesesValid(inpt))

if __name__ == '__main__':
    main()