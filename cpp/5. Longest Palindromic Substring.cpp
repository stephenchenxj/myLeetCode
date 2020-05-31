//
//  5. Longest Palindromic Substring.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/25/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

/*
 5. Longest Palindromic Substring
 Medium

 6410

 513

 Add to List

 Share
 Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

 Example 1:

 Input: "babad"
 Output: "bab"
 Note: "aba" is also a valid answer.
 Example 2:

 Input: "cbbd"
 Output: "bb"
 Accepted
 899,064
 Submissions
 3,085,923
 */

#include <iostream>
#include <string>
using namespace std;

class Solution {
    bool isPalindrome(string& s, int l, int r){
        if(l < 0) return false;
        if(r >= s.size()) return false;
        if (s[l]!= s[r]) return false;
        return true;
    }
    
public:
    string longestPalindrome(string s) {
        string rslt;
        
        int len = s.size();
        
        int l = 0;
        int r = 0;
        for(int i = 0; i<len; ++i){
            l = i;
            r = i;
            while(isPalindrome(s, l, r)){
                if (rslt.size() < r-l+1 ) rslt = s.substr(l,r-l+1);
                --l;
                ++r;
            }
            l = i;
            r = i+1;
            while(isPalindrome(s, l, r)){
                if (rslt.size() < r-l+1 ) rslt = s.substr(l,r-l+1);
                --l;
                ++r;
            }
        }
        
        return rslt;
        
    }
};
