//
//  53_Maximum Subarray.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/20/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0];
        int pre_max = 0;
        
        for(int n: nums){
            pre_max = max(pre_max+n, n);
            if (maxSum < pre_max) maxSum = pre_max;
        }
        
        return maxSum;
        
    }
};
