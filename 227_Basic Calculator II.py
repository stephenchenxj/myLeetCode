#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:41:49 2020

@author: chen

227. Basic Calculator II
Medium

1198

214

Add to List

Share
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
Accepted
164,732
Submissions
455,870

"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        stack, num, sign = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10+ord(s[i])-ord("0")
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign == "-": # the previous sign is -
                    stack.append(-num)
                elif sign == "+":# the previous sign is +
                    stack.append(num)
                elif sign == "*":# the previous sign is *, take action now
                    stack.append(stack.pop()*num)
                else:# the previous sign is /, take action now
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                sign = s[i] #save the new sign as the previous sign
                num = 0
        return sum(stack)
    
    
s = "31+2*2 +1"
print(Solution().calculate(s))