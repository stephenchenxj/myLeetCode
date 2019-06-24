#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 21:51:33 2019

@author: dev
"""

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        
        visitedRoom = set()
        visitedRoom.add(0)
        availableKeys = []
        for key in rooms[0]:
            availableKeys.append(key)
        
        while availableKeys:
            key = availableKeys.pop()
            if key not in visitedRoom:
                visitedRoom.add(key)
                for newKey in rooms[key]:
                    if newKey not in availableKeys:
                        availableKeys.append(newKey)
            
                        
                
            
            
        if len(visitedRoom) == len(rooms):
            return True
        else:
            return False
        