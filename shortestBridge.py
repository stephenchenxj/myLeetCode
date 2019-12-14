# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 04:04:10 2019

@author: stephen.chen

934. Shortest Bridge
Medium

In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: [[0,1],[1,0]]
Output: 1

Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

 

Note:

    1 <= A.length = A[0].length <= 100
    A[i][j] == 0 or A[i][j] == 1

 

"""

class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        q = []
        
        #label the given piece of land to 2, and label its connected lands to 2 
        # add the given piece of land to the queue
        def dfs(A, i, j, q):
            if i >=0 and i < len(A) and j >= 0 and j < len(A[0]):
                if A[i][j] == 1:
                    A[i][j] = 2
                    q.append((i,j))
                    dfs(A, i+1, j, q)
                    dfs(A, i-1, j, q)
                    dfs(A, i, j+1, q)
                    dfs(A, i, j-1, q)
        
        #find the first piece of land, and extend it. 
        #at the same time, create a queue of all pieces of land in the island for future growing
        found = False
        for i in range(len(A)):
            for j in range(len(A[0])):
                if not found and A[i][j] == 1:
                    dfs(A, i, j, q)
                    found = True
        
        def meetNewIsland(A, i, j, q):
            if i >=0 and i < len(A) and j >= 0 and j < len(A[0]):
                if A[i][j] == 1: # find the island
                    return True
                if A[i][j] == 0: # find sea, turn it to land by labelling it to 2, and add it to the queue
                    A[i][j] = 2
                    q.append((i,j))
        
        steps = 0
        q_new = []
        while q:
            (i,j) = q.pop()
            if meetNewIsland(A, i+1, j, q_new):
                return steps
            if meetNewIsland(A, i-1, j, q_new):
                return steps
            if meetNewIsland(A, i, j+1, q_new):
                return steps
            if meetNewIsland(A, i, j-1, q_new):
                return steps
            if not q:
                q = q_new[:]
                steps += 1
                q_new = []
        
        
        return steps

A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
test = Solution()
print(test.shortestBridge(A))