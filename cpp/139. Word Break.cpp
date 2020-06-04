//
//  139. Word Break.cpp
//  leetcode
//
//  Created by xujian chen on 6/4/20.
//  Copyright © 2020 xujian chen. All rights reserved.
//

/*
 139. Word Break
 Medium

 4017

 215

 Add to List

 Share
 Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

 Note:

 The same word in the dictionary may be reused multiple times in the segmentation.
 You may assume the dictionary does not contain duplicate words.
 Example 1:

 Input: s = "leetcode", wordDict = ["leet", "code"]
 Output: true
 Explanation: Return true because "leetcode" can be segmented as "leet code".
 Example 2:

 Input: s = "applepenapple", wordDict = ["apple", "pen"]
 Output: true
 Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
              Note that you are allowed to reuse a dictionary word.
 Example 3:

 Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
 Output: false
 Accepted
 526,648
 Submissions
 1,339,915
 */

class Solution {
    unordered_map<string, bool> _mem;
    
    bool wordBreak(string& s, unordered_set<string>& dict) {
        if(_mem.count(s)) return _mem[s];
        if(dict.count(s)) {
            _mem[s] = true;
            return true;
        }
        
        for(int i = 1; i< s.length(); ++i){
            string left = s.substr(0,i);
            string right = s.substr(i);
            if (wordBreak(left, dict) && wordBreak(right, dict))
                return _mem[s] = true;
        }
        
        
        return _mem[s] = false;
    }
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        return wordBreak(s, dict);
    }
};
