#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:17:58 2020

@author: chen

391. Perfect Rectangle
Hard

323

68

Add to List

Share
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.
 

 

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.
 

 

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.
 

 

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
 

Accepted
23,277
Submissions
77,911

"""

import sys
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        
        
        cornersCnt = dict()
        sumarea = 0
        minx = sys.maxint
        miny = sys.maxint
        maxx = 0
        maxy = 0
        for rect in rectangles:
            cornersCnt[(rect[0],rect[1])] = cornersCnt.get( (rect[0],rect[1]), 0) + 1
            cornersCnt[(rect[2],rect[3])] = cornersCnt.get( (rect[2],rect[3]), 0) + 1
            cornersCnt[(rect[0],rect[3])] = cornersCnt.get( (rect[0],rect[3]), 0) + 1
            cornersCnt[(rect[2],rect[1])] = cornersCnt.get( (rect[2],rect[1]), 0) + 1
            if minx > rect[0]:
                minx = rect[0]
            if miny > rect[1]:
                miny = rect[1]
            if maxx < rect[2]:
                maxx = rect[2]
            if maxy < rect[3]:
                maxy = rect[3]
            sumarea += (rect[2]-rect[0]) * (rect[3]-rect[1])
        
        if sumarea != (maxx-minx)*(maxy-miny):
            return False

        fourCorners = [(minx, miny), (minx, maxy), (maxx, miny), (maxx, maxy)]
        cnt = 0
        for corner in cornersCnt.keys():
            if cornersCnt[corner] == 1:
                cnt += 1
                if corner not in fourCorners:
                    return False
            elif (cornersCnt[corner] != 2) and (cornersCnt[corner]!= 4):
                return False
        return cnt == 4
        
