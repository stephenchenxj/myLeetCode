//
//  7. Reverse Integer.cpp
//  cpp_lambda
//
//  Created by Xujian CHEN on 5/22/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//
/*
 7. Reverse Integer
 Easy

 3201

 5036

 Add to List

 Share
 Given a 32-bit signed integer, reverse digits of an integer.

 Example 1:

 Input: 123
 Output: 321
 Example 2:

 Input: -123
 Output: -321
 Example 3:

 Input: 120
 Output: 21
 Note:
 Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 Accepted
 1,063,083
 Submissions
 4,136,784
 */


class Solution {
public:
    int reverse(int x) {
        //int sign = x>0 ? 1: -1;
        int rslt = 0;
        //x = abs(x);
        
        while(x){
            int temp = x%10;
            if (rslt > INT_MAX/10 || (rslt == INT_MAX/10 && temp > 7)) return 0;
            if (rslt < INT_MIN/10 || (rslt == INT_MIN/10 && temp < -8)) return 0;
            rslt = 10*rslt + temp;
            x /= 10;
        }
        
        
        return rslt;
        
    }
};
