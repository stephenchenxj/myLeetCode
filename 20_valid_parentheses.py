#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:19:17 2020

@author: stephenchen


20. Valid Parentheses
Easy

4310

202

Add to List

Share
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        right = (')', ']', '}')
        
        def match(l, r):
            if l == '(':
                if r != ')':
                    return False
            if l == '[':
                if r != ']':
                    return False
            if l == '{':
                if r != '}':
                    return False
            return True
        

        count = 0
        for c in s:
            if c not in right:
                stack.append(c)
                count += 1
            else:
                if not stack:
                    return False
                left = stack.pop()
                count -= 1
                if not match(left, c):
                    return False
                
        return count == 0