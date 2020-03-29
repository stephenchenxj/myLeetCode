#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 13:45:13 2020

@author: stephenchen

1192. Critical Connections in a Network
Hard

722

62

Add to List

Share
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
Accepted
36,419
Submissions
74,606

"""


from collections import defaultdict
class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        adj=defaultdict(set)
        for a,b in connections:
            adj[a].add(b)
            adj[b].add(a)
        
        vis=[False]*n
        time = [0]
        dfn = [0]*n
        low = [0]*n
        parent = [-1]*n
        res=[]
        
        def tarjan(u):
            vis[u]=True
            time[0]+=1
            dfn[u]=low[u]=time[0]
            
            for v in adj[u]:
                if not vis[v]:
                    parent[v] = u
                    tarjan(v)
                    low[u] = min(low[u], low[v])
                    
                    if low[v]>dfn[u]:
                        res.append([u,v])
                elif v!=parent[u]:
                    low[u] = min(low[u], dfn[v])
            
        for root in range(n):
            if not vis[root]:
                tarjan(root)
        return res