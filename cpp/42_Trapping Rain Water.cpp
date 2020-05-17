//
//  42_Trapping Rain Water.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/17/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        
        int rslt = 0;
        int len = height.size();
        
        if(len<3) return 0;
        
        int leftM = height[0];
        int rightM = height[len-1];
        
        int left = 1;
        int right = len-2;
        
        while(left <= right){
            if (leftM <= rightM){ // left bar is shorter, move left end, searching for higher bar
                if (leftM < height[left]) leftM = height[left];
                int temp = min(leftM, rightM) - height[left];
                if(temp > 0) rslt += temp;
                left += 1;
            }else{
                if (rightM < height[right]) rightM = height[right];
                int temp = min(leftM, rightM) - height[right];
                if(temp > 0) rslt += temp;
                right -= 1;
            }
        }
        return rslt;
    }
};
