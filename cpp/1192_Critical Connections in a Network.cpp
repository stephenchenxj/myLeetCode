//
//  1192_Critical Connections in a Network.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/18/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

/*
 
 1192. Critical Connections in a Network
 Hard

 911

 72

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
 47,246
 Submissions
 96,983
 
 */
 

#include <iostream>
#include <unordered_map>
#include <map>
#include <vector>

using namespace std;


class Solution {
private:
    void dfs(int id, int parentId, vector<bool>& visited, vector<int>& ids, vector<int>& depths, vector<vector<int>>& graph, vector<vector<int>>& rslt){
        if (visited[id] == true){
            depths[parentId]= min(depths[id],depths[parentId]);
            return;
        }
        visited[id] = true;
        ids[id] = ids[parentId]+1;
        depths[id] = ids[id];
        vector<int> childrenIds = graph[id];
        
        for(int childId: childrenIds){
            if(childId == parentId){
                continue;
            }
            else{
                dfs(childId, id, visited, ids, depths, graph, rslt);
                depths[id]= min(depths[id],depths[childId]);
            }
        }
        if( depths[id] > ids[parentId]){
            rslt.push_back({parentId, id});
        }
    }
    
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        vector<vector<int>> rslt;
        vector<vector<int>> graph(n, vector<int>());
         for (const vector<int>& conn : connections) {
            graph[conn[0]].push_back(conn[1]);
            graph[conn[1]].push_back(conn[0]);
        }
        vector<int> depths(n,0);
        vector<int> ids(n,-1);
        vector<bool> visited(n, false);
        dfs(0, 0, visited, ids, depths, graph, rslt);
        return rslt;
    }
};

int main(void){
    vector<vector<int>> connections = {{0,1},{1,2},{2,0},{1,3}};
    //vector<vector<int>> connections ={{1,0},{2,0},{3,0},{4,1},{5,3},{6,1},{7,2},{8,1},{9,6},{9,3},{3,2},{4,2},{7,4},{6,2},{8,3},{4,0},{8,6},{6,5},{6,3},{7,5},{8,0},{8,5},{5,4},{2,1},{9,5},{9,7},{9,4},{4,3}};
    
    //Solution mysolution = Solution();
    Solution mysolution = Solution();
    auto rslt = mysolution.criticalConnections(4, connections);
    
    for(auto v:rslt){
        for(int n:v)
            cout<<n<<"-";
    }
    
}
