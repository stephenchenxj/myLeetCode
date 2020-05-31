//
//  main.cpp
//  leetcode
//
//  Created by xujian chen on 5/31/20.
//  Copyright © 2020 xujian chen. All rights reserved.
//

#include <iostream>
#include <vector>
#include <utility>
#include <queue>

using namespace std;

class Solution {
    void bfs(vector<vector<int>>& grid, queue<pair<int,int>>& rottens, queue<pair<int,int>>& newRottens, int& mins){
        if (rottens.empty() && newRottens.empty())return;
        
        if (rottens.empty()) {
            ++mins;
            std::swap(rottens, newRottens);
        }
        
        pair<int,int> loc = rottens.front();
        rottens.pop();
        int r = loc.first;
        int c = loc.second;
        
        
        
        if (r-1>=0){
            if (grid[r-1][c] == 1){
                grid[r-1][c] = 2;
                newRottens.push(make_pair(r-1,c));
            }
        }
        if (r+1<grid.size()){
            if (grid[r+1][c] == 1){
                grid[r+1][c] = 2;
                newRottens.push(make_pair(r+1,c));
            }
        }
        if (c-1>=0){
            if (grid[r][c-1] == 1){
                grid[r][c-1] = 2;
                newRottens.push(make_pair(r,c-1));
            }
        }
        if (c+1<grid[0].size()){
            if (grid[r][c+1] == 1){
                grid[r][c+1] = 2;
                newRottens.push(make_pair(r,c+1));
            }
        }
        bfs(grid, rottens, newRottens, mins);
    }
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int mins = 0;
        int rows = (grid.size());
        int cols = (grid[0].size());
        queue<pair<int,int>> rottens;
        queue<pair<int,int>> newRottens;
        for(int r = 0; r<rows; ++r){
            for(int c = 0; c<cols; ++c){
                if (grid[r][c] == 2){ // find rotten orange
                    rottens.push(make_pair(r,c));
                }
            }
        }
        
        bfs(grid, rottens, newRottens, mins);
        
        for(int r = 0; r<rows; ++r){
            for(int c = 0; c<cols; ++c){
                if (grid[r][c] == 1) //still have fresh orange
                    return -1;
            }
        }
        return mins;
    }
};

int main(){
    
    vector<vector<int>> grid = {{2,2}, {1,1}, {0,0}, {2,0}};
    Solution mySolution = Solution();
    cout << mySolution.orangesRotting(grid) << endl;
}
