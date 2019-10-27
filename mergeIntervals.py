# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 00:23:30 2019

@author: stephen.chen

Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <=0:
            return[]
        intervals.sort()
        
        result = [intervals[0]]
        for l_r in intervals:
            overlap = 0
            for gap in result:
                if l_r[0] >= gap[0] and l_r[0] <= gap[1]:
                    gap[0] = min(l_r[0], gap[0])
                    gap[1] = max(l_r[1], gap[1])
                    overlap = 1
                elif l_r[1] >= gap[0] and l_r[1] <= gap[1]:
                    gap[0] = min(l_r[0], gap[0])
                    gap[1] = max(l_r[1], gap[1])
                    overlap = 1
                elif l_r[1] >= gap[1] and l_r[0] <= gap[0]:
                    gap[0] = min(l_r[0], gap[0])
                    gap[1] = max(l_r[1], gap[1])
                    overlap = 1
            if not overlap:
                result.append(l_r)
        return result
    
test = Solution()
Input = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(test.merge(Input))