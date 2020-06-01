//
//  15. 3Sum.cpp
//  leetcode
//
//  Created by xujian chen on 6/1/20.
//  Copyright © 2020 xujian chen. All rights reserved.
//

/*
 15. 3Sum
 Medium

 6543

 785

 Add to List

 Share
 Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

 Note:

 The solution set must not contain duplicate triplets.

 Example:

 Given array nums = [-1, 0, 1, 2, -1, -4],

 A solution set is:
 [
   [-1, 0, 1],
   [-1, -1, 2]
 ]
 Accepted
 878,368
 Submissions
 3,353,690
 */

class Solution {
    void twoSum(vector<int>& nums, int index, int target, vector<vector<int>>& rslt){
        int l = index;
        int r = nums.size()-1;
        while(l < r){
            if(nums[l]+nums[r]== target){
                if (!rslt.empty()){
                    if (nums[l] == rslt.back()[1] && -target == rslt.back()[0]) {
                        ++l;
                        --r;
                        continue;
                    }
                }
                rslt.push_back({-target, nums[l], nums[r]});
                ++l;
                --r;
            }
            else if (nums[l]+nums[r] < target){
                ++l;
            }
            else{
                --r;
            }
        }
    }
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> rslt;
        int previous;
        for(int i = 0; i < n-2; ++i){
            if (nums[i] > 0) break;
            if (!rslt.empty()){
                if (nums[i] == rslt.back()[0]) continue;
            }
            twoSum(nums, i+1, -nums[i], rslt);
            
        }
        return rslt;
        
    }
};
