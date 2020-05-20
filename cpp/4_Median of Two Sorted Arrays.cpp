//
//  4_Median of Two Sorted Arrays.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/19/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

#include <iostream>
#include <vector>


using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size();
        int len2 = nums2.size();
        if(len1 > len2) return findMedianSortedArrays(nums2, nums1);
        
        int k = (len1 + len2 + 1)/2;
        
        int m1 = 0;
        int m2 = k - m1;
        
        int l = 0;
        int r = len1 ;
        while(l<r){
            m1 = (l + r)/2;
            m2 = k - m1;
            if (nums1[m1] < nums2[m2-1]){
                l = m1 + 1;
            }else{
                r = m1;
            }
        }
        
        m1 = l;
        m2 = k - m1;
        
        int c1 = 0;
        if (m2 == 0){
            c1 = nums1[m1-1];
        }else if(m1 == 0){
            c1 = nums2[m2-1];
        }
        else{
            c1 = max(nums1[m1-1], nums2[m2-1]);
        }
        
        if ((len1+len2)%2 == 1)
            return c1;
        
            
            
        int c2 = 0;
        if (m1 >= len1){
            c2 = nums2[m2];
        }else if(m2 >= len2){
            c2 = nums1[m1];
        }
        else{
            c2 = min(nums1[m1], nums2[m2]);
        }
        return (c1+c2)/2.0;
    }
};
