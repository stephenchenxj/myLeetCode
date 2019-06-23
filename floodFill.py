#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:19:19 2019

@author: dev

Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

"""

class Solution(object):
    processed = []
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if sr >= len(image) or sc >= len(image[0]):
            return None
        self.processed = []
        self.sameColor(image, sr, sc, newColor, image[sr][sc])
        
        return image
        
    def sameColor(self, image, sr, sc, newColor, targetColor):
        image[sr][sc] = newColor
        if (sr + 1) < (len(image)):
            if image[sr+1][sc] == targetColor:
                image[sr+1][sc] = newColor
                if[sr+1, sc] not in self.processed:
                    self.processed.append([sr+1, sc] )
                    self.sameColor(image, sr+1, sc, newColor, targetColor)
        if (sr - 1) >= 0:
            if image[sr-1][sc] == targetColor:
                image[sr-1][sc] = newColor
                if[sr-1, sc] not in self.processed:
                    self.processed.append([sr-1, sc] )
                    self.sameColor(image, sr-1, sc, newColor, targetColor)
        if (sc + 1) < len(image[0]):
            if image[sr][sc+1] == targetColor:
                image[sr][sc+1] = newColor
                if[sr, sc+1] not in self.processed:
                    self.processed.append([sr, sc+1] )
                    self.sameColor(image, sr, sc+1, newColor, targetColor)
        if (sc - 1) >= 0:
            if image[sr][sc-1] == targetColor:
                image[sr][sc-1] = newColor   
                if[sr, sc-1] not in self.processed:
                    self.processed.append([sr, sc-1] )
                    self.sameColor(image, sr, sc-1, newColor, targetColor)
        
        
                
                
image = [[0,0,0],[0,1,0]] 
print(Solution().floodFill(image, 1, 1, 2))