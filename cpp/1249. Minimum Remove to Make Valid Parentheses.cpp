//
//  1249. Minimum Remove to Make Valid Parentheses.cpp
//  leetcode
//
//  Created by xujian chen on 6/2/20.
//  Copyright © 2020 xujian chen. All rights reserved.
//

/*
 1249. Minimum Remove to Make Valid Parentheses
 Medium

 675

 23

 Add to List

 Share
 Given a string s of '(' , ')' and lowercase English characters.

 Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

 Formally, a parentheses string is valid if and only if:

 It is the empty string, contains only lowercase characters, or
 It can be written as AB (A concatenated with B), where A and B are valid strings, or
 It can be written as (A), where A is a valid string.
  

 Example 1:

 Input: s = "lee(t(c)o)de)"
 Output: "lee(t(c)o)de"
 Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
 Example 2:

 Input: s = "a)b(c)d"
 Output: "ab(c)d"
 Example 3:

 Input: s = "))(("
 Output: ""
 Explanation: An empty string is also valid.
 Example 4:

 Input: s = "(a(b(c)d)"
 Output: "a(b(c)d)"
  

 Constraints:

 1 <= s.length <= 10^5
 s[i] is one of  '(' , ')' and lowercase English letters.
 Accepted
 56,942
 Submissions
 92,439
 */


class Solution {
public:
    string minRemoveToMakeValid(string s) {
        vector<int> index2remove; // create a vector to store index of '('. In the end, index2remove size will drop to 0 only when s is balanced.
        for(int i = 0; i < s.length(); ++i){
            if (s[i] == '(') index2remove.push_back(i);
            else if (s[i] == ')'){
                if (index2remove.size()>0) index2remove.pop_back();
                else s[i] = 'A'; //detected ')' that can't be balanced. Mark it to 'A'.
            }
        }
        
        string result;
        int j = 0;
        for(int i = 0; i < s.length(); ++i){ // traverse s
            if(j < index2remove.size()){ //
                if(i == index2remove[j] ){
                    ++j;
                    continue;
                }
            }
            if (s[i]== 'A') continue;
            result += s[i]; //cope s[i] to result only if it is not marked to 'A' or i is not in the index2remove.
        }
        return result;
    }
};
