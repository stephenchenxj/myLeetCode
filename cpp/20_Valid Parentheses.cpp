//
//  20_Valid Parentheses.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/20/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

class Solution {
public:
    bool isValid(string s) {
        stack<char> brackets;
        set<char> left= {'(', '[', '{'};
        unordered_map<char, char> m = {
        {'(', ')'},
        {'[', ']'},
        {'{', '}'},
    };
        for(char c : s)
            if (m.find(c) != m.cend()){
                brackets.push(c);
                
            }else{
                if (brackets.size() == 0) return false;
                char l = brackets.top();
                brackets.pop();
                if(c != m[l]) return false;
            }
        return (brackets.size() == 0);
    }
};
