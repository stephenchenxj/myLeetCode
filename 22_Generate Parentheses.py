#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:05:03 2020

@author: chen

22. Generate Parentheses
Medium

4460

244

Add to List

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
Accepted
498,636
Submissions
822,431

"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        
        ans = []
        cur = ''
        
        def dfs(l, r, cur, ans):

            if r == 0 and l == 0:
                ans.append(cur)
                return
            if l > 0:
                dfs(l-1, r, cur + '(', ans)
            if r > l:
                dfs(l, r-1, cur + ')', ans)

            
        
        dfs(n,n,cur, ans)
        
        return ans
    
    def generateParenthesis2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        
        ans = []
        cur = []
        
        def dfs(l, r, cur, ans):

            if r == 0 and l == 0:
                ans.append(cur[:])
                return
            if l > 0:
                cur.append('(')
                dfs(l-1, r, cur, ans)
                cur.pop()
            if r > l:
                cur.append(')')
                dfs(l, r-1, cur, ans)
                cur.pop()

            
        
        dfs(n,n,cur, ans)
        
        for i in range(len(ans)):
            ans[i] = ''.join(ans[i])
            
        
        return ans
    
n = 4
print(Solution().generateParenthesis(n))
print(Solution().generateParenthesis2(n))