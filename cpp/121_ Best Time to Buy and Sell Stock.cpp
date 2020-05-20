//
//  121_ Best Time to Buy and Sell Stock.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/20/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxPrft = 0;
        if (prices.size() == 0) return maxPrft;
        
        int lowest = prices[0];
        for(int p :prices){
            if (lowest > p) lowest = p;
            if (maxPrft < p-lowest) maxPrft = p-lowest;
        }
        
        return maxPrft;
    
        
    }
};
