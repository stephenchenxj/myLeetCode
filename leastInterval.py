# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 01:13:50 2019

@author: stephen.chen
Task Scheduler

Given a char array representing tasks CPU need to do. It contains capital 
letters A to Z where different letters represent different tasks. Tasks could 
be done without original order. Each task could be done in one interval. For 
each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same
 tasks, there must be at least n intervals that CPU are doing different tasks 
 or just be idle.

You need to return the least number of intervals the CPU will take to finish 
all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

 

Note:

    The number of tasks is in the range [1, 10000].
    The integer n is in the range [0, 100].


"""
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        total = len(tasks)
        majorTask = 0
        myMap = dict()
        for t in tasks:
            if myMap.get(t) == None:
                myMap[t] = 1
            else:
                myMap[t] += 1
                if myMap[t] > majorTask:
                    majorTask = myMap[t]
        highFrequenceTasksNo = 0
        for k in myMap.keys():
            if myMap[k] == majorTask:
                highFrequenceTasksNo += 1
            
                
        return max((majorTask-1)*(n+1) + highFrequenceTasksNo, total)
    
test = Solution()
print(test.leastInterval(["A","B","C","D","E","A","B","C","D","E"], 4))
            
        

