# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:33:44 2019

@author: stephen.chen

785. Is Graph Bipartite?
Medium

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent 
subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the 
edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  
There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.

 

Note:

    graph will have length in range [1, 100].
    graph[i] will contain integers in range [0, graph.length - 1].
    graph[i] will not contain i or duplicate values.
    The graph is undirected: if any element j is in graph[i], then i will be in graph[j].

Accepted
69,477
Submissions
153,149
"""
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        groupA = 1
        #visited vertices or vertices which has been added into the q
        vertices = dict()        
        
        for i in range(len(graph)):
            #enter from item
            if not vertices.get(i):
                q = [i]    
                vertices[i] = groupA
                while q:        
                    j = q.pop(0)
                    if vertices[j] == 1:
                        groupNeighbour = 2
                    else:
                        groupNeighbour = 1
                    for n in graph[j]:
                        if vertices.get(n):# this vertix has been labled before
                            if vertices[n] != groupNeighbour:
                                return False
                        else: # this vertix has not been labled before
                            vertices[n] = groupNeighbour
                            
                            if n not in q:
                                q.append(n)    
        return True
    
    def traverseGraphBFS(self, graph):
        #visited vertices or vertices which has been added into the q
        vertices = dict()        
        #enter from the first item
        q = [0]        
        while q:        
            i = q.pop(0)
            vertices[i] = True
            #print current vertix
            print(i)        
            for n in graph[i]:
                if not vertices.get(n):
                    q.append(n)    
                    vertices[n] = True
                    
                
                
graph = [[1,3],[0,2],[1,3],[0,2]]

test = Solution()
print(test.isBipartite(graph))   
#test.traverseGraphBFS(graph)     
