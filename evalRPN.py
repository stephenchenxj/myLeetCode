#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 21:24:14 2019

@author: dev
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        print (int(1/(-10)))
        res = 0
        stack = []
        for a in tokens:
            
            if a == '+':
                y = stack.pop()
                x = stack.pop()
                res = int(int(x) + int(y))
                stack.append(res)
                print(res)
                
            elif a == '-' :
                y = stack.pop()
                x = stack.pop()
                res = int(int(x) - int(y))
                stack.append(res)
                print(res)
                
            elif a == '*':
                y = stack.pop()
                x = stack.pop()
                res = int(int(x) * int(y))
                stack.append(res)
                print(res)
                
            elif a == '/':
                y = int(stack.pop())
                x = int(stack.pop())
                if x < 0 and y > 0:
                    res = -1*int(int(-1*x) / int(y))
                elif x > 0 and y < 0:
                    res = -1*int(int(-1*x) / int(y))
                else:
                    res = int(int(x) / int(y))
                stack.append(res)
                print(res)
                
            else:
                res = a
                stack.append(a)
                
            
            
        
        return(res)
        
        
        
print(Solution().evalRPN(["4","13","5","/","+"]))