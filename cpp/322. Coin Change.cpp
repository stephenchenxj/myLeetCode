//
//  322. Coin Change.cpp
//  leetcode
//
//  Created by xujian chen on 6/3/20.
//  Copyright © 2020 xujian chen. All rights reserved.
//

/*
 322. Coin Change
 Medium

 3721

 132

 Add to List

 Share
 You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

 Example 1:

 Input: coins = [1, 2, 5], amount = 11
 Output: 3
 Explanation: 11 = 5 + 5 + 1
 Example 2:

 Input: coins = [2], amount = 3
 Output: -1
 Note:
 You may assume that you have an infinite number of each kind of coin.

 Accepted
 379,582
 Submissions
 1,097,347
 */

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        
        int f[coins.size()+1][amount+1] ;
        
        f[0][0] = 0;
        for(int i = 1; i <= coins.size(); ++i){
            f[i][0] = 0;
        }
        for(int j = 1; j <= amount; ++j){
            f[0][j] = INT_MAX;
        }
        
        
        for(int i = 1; i <= coins.size(); ++i){
            for(int j = 1; j <= amount; ++j){
                int temp = INT_MAX;
                if (j >= coins[i-1]) {
                    if (f[i][j-coins[i-1]]!= INT_MAX)
                        temp = f[i][j-coins[i-1]] + 1;
                }
                f[i][j] = min(f[i-1][j], temp);
            }
        }
        
        if (f[coins.size()][amount] == INT_MAX) return -1;
        return f[coins.size()][amount];
        
    }
};
