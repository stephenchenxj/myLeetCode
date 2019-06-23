#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 22:29:07 2019

@author: chen
"""
#s = "3[a2[c]]", return "accaccacc".


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for c in s:
            if c != ']':
                stack.append(c)
            else: #find ]. need to find [
                
                #find alphabet between []
                temp = []
                a = stack.pop()
                while a  != '[':
                    temp.append(a)
                    a = stack.pop()
                temp.reverse()
                #print(temp)
                
                # find digit before []
                num = []
                a = stack[-1]
                #print(a)
                while a  >= '0' and a <= '9':
                    num.append(a)
                    stack.pop()
                    if stack == []:
                        break
                    a = stack[-1]
                num.reverse()
                digi = (int(''.join(num)))
                st = ((''.join(temp)))
                
                stack.append(digi*st)
                
        return ( ''.join(stack))
        
        
s = "3[a2[c]]"
mySolution = Solution()
print(mySolution.decodeString(s))
        