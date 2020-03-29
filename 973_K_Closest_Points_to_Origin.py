#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:30:52 2020

@author: stephenchen

973. K Closest Points to Origin
Medium

1222

101

Add to List

Share
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
Accepted
199,688
Submissions
322,691

"""


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        
        counter=0
        my_dict=dict()
    	
        for i in range(len(points)):
            my_dict[i]=self.distance(points[i])
        res=sorted(my_dict.items(), key=lambda x:x[1])
        output=[]
        for i in res:
            if counter<K:
                output.append(points[i[0]])
            counter+=1
        return output
    
    
    def distance(self,x):
    	origin=[0,0]
    	return (x[0]-origin[0])**2+(x[1]-origin[1])**2
    
points = [[1,3],[-2,2],[2,-2]]
K = 2

print(Solution().kClosest(points, K))