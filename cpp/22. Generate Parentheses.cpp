//
//  22. Generate Parentheses.cpp
//  leetcode
//
//  Created by xujian chen on 6/1/20.
//  Copyright © 2020 xujian chen. All rights reserved.
//

/*
 22. Generate Parentheses
 Medium

 4852

 257

 Add to List

 Share
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 For example, given n = 3, a solution set is:

 [
   "((()))",
   "(()())",
   "(())()",
   "()(())",
   "()()()"
 ]
 Accepted
 527,749
 Submissions
 858,613
 */

class Solution {
    void backtrack(int max, vector<string>& rslt, string current, int left, int right){
        if (current.length() == 2*max){
            rslt.push_back(current);
            return;
        }
        if(left<max){
            backtrack(max, rslt, current+"(", left+1, right);
        }
        if(right<left){
            backtrack(max, rslt, current+")", left, right+1);
        }
        
    }
public:
    vector<string> generateParenthesis(int n) {
        vector<string> rslt;
        
        backtrack(n, rslt, "", 0, 0);
        
        return rslt;
        
    }
};
