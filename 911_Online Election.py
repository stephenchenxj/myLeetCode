#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 00:02:43 2020

@author: chen

911. Online Election
Medium

292

247

Add to List

Share
In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.  

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.

 

Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation: 
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.
 

Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0].
Accepted
20,069
Submissions
40,329

"""


class TopVotedCandidate(object):
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        
        self.mostVotedByTime = dict()
        self.mostVoted = dict()
        maxVotes = 0
        person = 0
        
        for i,t in enumerate(times):
            if persons[i] not in self.mostVoted.keys():
                self.mostVoted[persons[i]] = 1
            else:
                self.mostVoted[persons[i]] += 1
            if maxVotes <= self.mostVoted[persons[i]]:
                maxVotes = self.mostVoted[persons[i]]
                person = persons[i]
            self.mostVotedByTime[times[i]] = person
        
        self.keys = sorted(self.mostVotedByTime)

        #print(self.mostVotedByTime)


    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        l = 0
        r = len(self.keys)-1
        if t >= self.keys[r]:
            return self.mostVotedByTime[self.keys[r]]
        
        
        while l < r:
            
            if self.keys[int((l+r)/2)] > t:         
                r = int((l+r)/2)
            else:
                l = int((l+r)/2)+1
        return self.mostVotedByTime[self.keys[r-1]]