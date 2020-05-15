#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 11:40:47 2020

@author: chen
"""

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        itineraries = []
        itinerary = []
        airport = "JFK"
#        itinerary.append(airport)
        self.dfs(tickets, itineraries, itinerary, airport)
        itineraries.sort()
        return itineraries[0]
        
    def dfs(self, tickets, itineraries,itinerary, airport):
        if not tickets: # find a valid itineray
            itinerary.append(airport)
            itineraries.append(itinerary)
            return True
        potential_tickets = []
        for t in tickets:
            if t[0] == airport:
                potential_tickets.append(t)
        print(potential_tickets)

        if not potential_tickets:
            return
        potential_tickets.sort()
                
        for t in potential_tickets:
            itinerary.append(t[0])
            airport = t[1]
            tickets.remove(t)
            if self.dfs(tickets, itineraries, itinerary, airport):
                return True
            tickets.append(t)
            itinerary.pop()
        
    

tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(Solution().findItinerary(tickets))
