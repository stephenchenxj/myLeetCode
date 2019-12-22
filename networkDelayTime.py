# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 04:21:05 2019

@author: stephen.chen

743. Network Delay Time
Medium

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), 
where u is the source node, v is the target node, and w is the time it takes 
for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all 
nodes to receive the signal? If it is impossible, return -1.

 

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

 

Note:

    N will be in the range [1, 100].
    K will be in the range [1, N].
    The length of times will be in the range [1, 6000].
    All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

Accepted
58,098
Submissions
129,500
"""

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        '''
        
        #since the total length of times will be in the range [1,6000], w < 100
        #set initial map to a max value of 6001
        delay = dict()
        for i in range(N):
            delay[i+1] = 6001
            
        q = [K]
        delay[K] = 0
        
        processedRoute = dict()
        
        while q:
            n = q.pop(0)
            for i, time in enumerate (times):
                if not processedRoute.get(i):
                    if time[0] == n:
                        q.append(time[1])
                        delay[time[1]] = min(time[2] + delay[time[0]], delay[time[1]])
                        processedRoute[i] = True
        
        result = max(delay.values())
        if result == 6001:
            return -1
        else:
            return result
        '''
        
        delay = dict()
        for i in range(N):
            delay[i+1] = 6001
        
        delay[K] = 0
        for i in range(N):
            for time in times:
                delay[time[1]] = min(delay[time[1]], time[2] + delay[time[0]])
        result = max(delay.values())
        if result == 6001:
            return -1
        else:
            return result
        
        
        

test = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4 
K = 2
times = [[4,2,76],[1,3,79],[3,1,81],[4,3,30],[2,1,47],[1,5,61],[1,4,99],[3,4,68],[3,5,46],[4,1,6],[5,4,7],[5,3,44],[4,5,19],[2,3,13],[3,2,18],[1,2,0],[5,1,25],[2,5,58],[2,4,77],[5,2,74]]
N = 5
K = 3
print(test.networkDelayTime(times, N, K))
