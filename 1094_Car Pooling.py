#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:37:18 2020

@author: chen

1094. Car Pooling

Medium

415

19

Add to List

Share
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
 
 

Constraints:

trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000
Accepted
24,523
Submissions
43,215

"""

class Solution2(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        loc_on_off = dict()
        
        for trip in trips:
            loc_on_off[trip[1]] = loc_on_off.get(trip[1], 0) + trip[0]
            loc_on_off[trip[2]] = loc_on_off.get(trip[2], 0) - trip[0]
        
        stops = sorted(loc_on_off)
        cnt = 0
        for stop in stops:
            cnt += loc_on_off[stop]
            if cnt > capacity:
                return False
        return True


class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        if not trips:
            return False
        if capacity == 0:
            return False
        
        ons = dict()
        offs = dict()
        
        for trip in trips:
            if trip[1] not in ons:
                ons[trip[1]] = trip[0]
            else:
                ons[trip[1]] += trip[0]
            if trip[2] not in offs:
                offs[trip[2]] = trip[0]
            else:
                offs[trip[2]] += trip[0]
                
        
        num_onboard = 0
        max_num = 0
        starts = sorted(ons)
        ends = sorted(offs)
        
        j = 0
        for i in range(len(starts)):
            num_onboard += ons[starts[i]]
            
            while j < len(ends) and ends[j] <= starts[i]:
                num_onboard -= offs[ends[j]]
                j += 1
            if max_num < num_onboard:
                max_num = num_onboard
                
        if max_num > capacity:
            return False
        else:
            return True
        
                
        
        
        

        
trips = [[3,2,8],[4,4,6],[10,8,9]]
capacity = 11
print(Solution().carPooling(trips, capacity))