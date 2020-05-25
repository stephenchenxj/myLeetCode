//
//  67. Add Binary.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/24/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

/*
 67. Add Binary
 Easy

 1619

 265

 Add to List

 Share
 Given two binary strings, return their sum (also a binary string).

 The input strings are both non-empty and contains only characters 1 or 0.

 Example 1:

 Input: a = "11", b = "1"
 Output: "100"
 Example 2:

 Input: a = "1010", b = "1011"
 Output: "10101"
  

 Constraints:

 Each string consists only of '0' or '1' characters.
 1 <= a.length, b.length <= 10^4
 Each string is either "0" or doesn't contain any leading zero.
 */

class Solution {
public:
    string addBinary(string a, string b) {
        string rslt;
        int carry = 0;
        stack<char> digits;
        
        int len = max(a.size(), b.size());
        for (int i = 0; i < len; ++i){
            int ca = 0;
            int cb = 0;
            if(i<a.size()){
                ca = a[a.size()-i-1] - '0';
            }
            if(i<b.size()){
                cb = (b[b.size()-i-1]- '0');
            }
            int temp = ca + cb + carry;
            carry = temp/2;
            digits.push(char(temp%2 + '0'));
            //if(temp%2 ==1) digits.push('1');
            //else digits.push('0');
        }
        if(carry == 1) digits.push('1');
        
        while(digits.size()>0){
            rslt.push_back(digits.top());
            digits.pop();
        }
        return rslt;
        
    }
};
