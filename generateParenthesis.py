# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 05:34:33 2019

@author: stephen.chen

Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rst = []
        if n <= 0:
            return rst
        l = n
        r = n
        self.addParenthesis(l, r, '', rst)
        return rst
        
    def addParenthesis(self, l, r, item, rst):
        if r < l:
            return
        if l == 0 and r == 0:
            rst.append(item)
        if l > 0:
            self.addParenthesis(l-1, r, item+'(', rst)
        if r > 0:
            self.addParenthesis(l, r-1, item+')', rst)
        
                
test = Solution()
print (test.generateParenthesis(4))            
            
