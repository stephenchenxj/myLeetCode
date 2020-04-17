#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:57:22 2020

@author: chen

39. Combination Sum
Medium

3222

102

Add to List

Share
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
Accepted
490,314
Submissions
906,904


"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = [] # record all solutions
        cur = [] # record one solution
        
        #s: starting index. 
        def dfs(candidates, target, s, cur, ans):
            if target == 0: #if target equals 0, find one solution
                ans.append(cur[:])
                return
                
            for i in range(s, len(candidates)):
                
                #sorted list, if current val bigger than target, no need to search the rest
                if candidates[i] > target: 
                    break
                #add candidates[i] to the cur solution.
                cur.append(candidates[i])
                
                

                #else, go deeper. because item can be used multiple times, i remains the same
                dfs(candidates, target-candidates[i], i, cur, ans)
                
                #finish search of candidates[i], pop it out, and try next items in candidates.
                cur.pop()
                    
        
        candidates.sort()
        dfs(candidates, target, 0, cur, ans)
        return ans
    
candidates = [2,6,3,7]
target = 7
print(Solution().combinationSum(candidates, target))