# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:17:07 2020

@author: stephen.chen

207. Course Schedule
Medium

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to 
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it 
possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is 
             possible.

Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take 
             course 0 you should
             also have finished course 1. So it is impossible.

Note:

    The input prerequisites is a graph represented by a list of edges, not 
    adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.

Accepted
302,896
Submissions
750,686

"""

import collections

class Solution(object):
    
    def canFinish1(self, numCourses, prerequisites):
        forward = {i: set() for i in range(numCourses)}
        print(forward)
        backward = collections.defaultdict(set)
        print(backward)
        for i, j in prerequisites:
            forward[i].add(j)
            backward[j].add(i)
        print(forward)
        print(backward)
        queue = collections.deque([node for node in forward if len(forward[node]) == 0])
        print(queue)
        while queue:
            node = queue.popleft()
            for neigh in backward[node]:
                forward[neigh].remove(node)
                if len(forward[neigh]) == 0:
                    queue.append(neigh)
            forward.pop(node)
        return not forward
    
    
    
    
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        inDegree = dict()
        unlock = dict()
        
        courseToTake = []
        for i in range(numCourses):
            inDegree[i] = set()
        for i in range(len(prerequisites)):
            inDegree[prerequisites[i][0]].add(prerequisites[i][1])
            if not unlock.get(prerequisites[i][1]):
                unlock[prerequisites[i][1]]=set({prerequisites[i][0]})
            else:
                unlock[prerequisites[i][1]].add(prerequisites[i][0])
                
        for i in range(numCourses):
            if len(inDegree[i])== 0:
                courseToTake.append(i)
                
        while courseToTake:
            course = courseToTake.pop(0)
            numCourses -= 1
            if unlock.get(course):
                helpedCourses = unlock[course]
                for c in helpedCourses:
                    inDegree[c].remove(course)
                    if len(inDegree[c])== 0:
                        courseToTake.append(c)
                    
        if numCourses == 0:
            return True
        else:
            return False
        
    

numCourses = 4
prerequisites = [[1,0], [3,0], [0,1]]        
test = Solution()
print(test.canFinish(numCourses, prerequisites))
        
    
        
        
            
        
            
            

