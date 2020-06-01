//
//  238. Product of Array Except Self.cpp
//  leetcode
//
//  Created by xujian chen on 6/1/20.
//  Copyright © 2020 xujian chen. All rights reserved.
//
/*
 238. Product of Array Except Self
 Medium

 4567

 395

 Add to List

 Share
 Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

 Example:

 Input:  [1,2,3,4]
 Output: [24,12,8,6]
 Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

 Note: Please solve it without division and in O(n).

 Follow up:
 Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

 Accepted
 513,642
 Submissions
 863,943
 */

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int left[nums.size()];
        int right[nums.size()];
        vector<int> rslt;
        for(int i = 0; i< nums.size(); ++i){
            if (i==0) {
                left[i] = nums[i];
                right[nums.size()-i-1] = nums[nums.size()-i-1];
            }
            else {
                left[i] = left[i-1]*nums[i];
                right[nums.size()-i-1] = right[nums.size()-i]*nums[nums.size()-i-1];
            }
        }
        rslt.push_back(right[1]);
        
        for(int i = 1; i<nums.size()-1; ++i){
            rslt.push_back(left[i-1]*right[i+1]);
        }
        rslt.push_back(left[nums.size()-2]);
        return rslt;
    }
};
