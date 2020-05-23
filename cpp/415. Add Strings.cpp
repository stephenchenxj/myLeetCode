//
//  415. Add Strings.cpp
//  cpp_lambda
//
//  Created by Xujian CHEN on 5/22/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

/*
 415. Add Strings
 Easy

 845

 253

 Add to List

 Share
 Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

 Note:

 The length of both num1 and num2 is < 5100.
 Both num1 and num2 contains only digits 0-9.
 Both num1 and num2 does not contain any leading zero.
 You must not use any built-in BigInteger library or convert the inputs to integer directly.
 Accepted
 171,441
 Submissions
 366,450
 */

class Solution {
public:
    string addStrings(string num1, string num2) {
        int carry = 0;
        long l1 = num1.size();
        long l2 = num2.size();
        stack<char> chars;
        
        
        for(int i = 0; i < max(l1, l2); ++i){
            int digit = 0;
            digit += carry;
            if(i < l1){
                digit += (num1[l1-1-i]-'0');
            }
            if(i < l2){
                digit += (num2[l2-1-i]-'0');
            }
            carry = digit/10;
            digit %= 10;
            chars.push(digit+'0');
        }
        
        if (carry == 1){
            chars.push('1');
        }
        
        long l = chars.size();
        
        string rslt;
        for(int i = 0; i<l; ++i){
            char temp = chars.top();
            rslt += chars.top();
            chars.pop();
        }
        
        
        return rslt;
        
    }
};
