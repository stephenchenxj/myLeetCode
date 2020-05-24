//
//  283. Move Zeroes.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/24/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

/*
 283. Move Zeroes
 Easy

 3554

 118

 Add to List

 Share
 Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

 Example:

 Input: [0,1,0,3,12]
 Output: [1,3,12,0,0]
 Note:

 You must do this in-place without making a copy of the array.
 Minimize the total number of operations.
 Accepted
 794,558
 Submissions
 1,385,033
 */

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int len = nums.size();
        int cnt = 0;
        for(int i = 0; i + cnt < len; ++i){
            if (nums[i] == 0){
                nums.erase(nums.begin()+i);
                nums.push_back(0);
                i --;
                cnt++;
            }
        }
        
    }
};
