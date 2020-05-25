//
//  88 Merge Sorted Array.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/25/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

/*
 88. Merge Sorted Array
 Easy

 2008

 3948

 Add to List

 Share
 Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

 Note:

 The number of elements initialized in nums1 and nums2 are m and n respectively.
 You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
 Example:

 Input:
 nums1 = [1,2,3,0,0,0], m = 3
 nums2 = [2,5,6],       n = 3

 Output: [1,2,2,3,5,6]
 Accepted
 556,468
 Submissions
 1,432,837
 */


class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        while(m>0 && n>0){
            if(nums1[m-1]>nums2[n-1]){
                nums1[m+n-1] = nums1[m-1];
                --m;
            }else{
                nums1[m+n-1] = nums2[n-1];
                --n;
            }
        }
        while(n>0){
            nums1[n-1] = nums2[n-1];
            --n;
        }
    }
};
