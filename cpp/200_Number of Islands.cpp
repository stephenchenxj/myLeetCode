/*
200. Number of Islands
Medium

4949

187

Add to List

Share
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
Accepted
669,899
Submissions
1,461,178

*/




class Solution {
private:
    void dfs(vector<vector<char>>& grid, int r, int c){

        int nr = grid.size();
        int nc = grid[0].size();

        grid[r][c] = '0';
        if (r - 1 >= 0 && grid[r-1][c] == '1') dfs(grid, r - 1, c);
        if (r + 1 < nr && grid[r+1][c] == '1') dfs(grid, r + 1, c);
        if (c - 1 >= 0 && grid[r][c-1] == '1') dfs(grid, r, c - 1);
        if (c + 1 < nc && grid[r][c+1] == '1') dfs(grid, r, c + 1);




    };

public:
    int numIslands(vector<vector<char>>& grid) {

        int nr = grid.size();
        if(!nr) return 0;
        int nc = grid[0].size();

        int num_islands = 0;

        for(int r = 0; r < nr; ++r){
            for (int c = 0; c < nc; ++c){
                if(grid[r][c]=='1'){
                    ++num_islands;
                    dfs(grid, r, c);
                }
            }
        }
        return num_islands;
    }
};
