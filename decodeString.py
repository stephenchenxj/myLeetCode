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
        rst = []
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
                
                #print (digi*st)
                rst.append(digi*st)
                rst.reverse()
                
        return ( ''.join(rst))
                
                    
                
                
        
        
        
        
        
s = "3[a12[cb]]"
mySolution = Solution()
print(mySolution.decodeString(s))
        