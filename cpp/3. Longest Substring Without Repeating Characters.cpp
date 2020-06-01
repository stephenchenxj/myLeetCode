//
//  3. Longest Substring Without Repeating Characters.cpp
//  leetcode
//
//  Created by xujian chen on 5/31/20.
//  Copyright © 2020 xujian chen. All rights reserved.
//
/*
 3. Longest Substring Without Repeating Characters
 Medium

 8944

 540

 Add to List

 Share
 Given a string, find the length of the longest substring without repeating characters.

 Example 1:

 Input: "abcabcbb"
 Output: 3
 Explanation: The answer is "abc", with the length of 3.
 Example 2:

 Input: "bbbbb"
 Output: 1
 Explanation: The answer is "b", with the length of 1.
 Example 3:

 Input: "pwwkew"
 Output: 3
 Explanation: The answer is "wke", with the length of 3.
              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 Accepted
 1,505,480
 Submissions
 5,010,191
 */

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        int ans = 0;
        for(int i = 0; i < n; ++i){
            int j = i;
            vector<int> seen(128);
            while(j<n && !seen[s[j]]){
                seen[s[j]] = 1;
                ++ j;
            }
            ans = max(ans, j - i);
        }
        return ans;
        
    }
};
