//
//  953.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/24/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

/*
 953. Verifying an Alien Dictionary
 Easy

 710

 278

 Add to List

 Share
 In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

 Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

  

 Example 1:

 Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
 Output: true
 Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
 Example 2:

 Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
 Output: false
 Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
 Example 3:

 Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
 Output: false
 Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
  

 Constraints:

 1 <= words.length <= 100
 1 <= words[i].length <= 20
 order.length == 26
 All characters in words[i] and order are English lowercase letters.
 */


class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        
        unordered_map<char, char> dict;
        int i = 0;
        for(char c: order){
            dict[c] = 'a' + i;
            ++i;
        }
        vector<string> translatedWords;
        for(auto& word : words){
            //cout << word << endl;
            //string translatedWord;
            for( auto& c : word){
                //translatedWord.push_back(dict[c]);
                c = dict[c];
            }
            //translatedWords.push_back(translatedWord);
        }
        
        return is_sorted(words.begin(), words.end()); // useful!
        //string preWord = translatedWords[0];
        //for(auto word:translatedWords){
        //    if (word < preWord) return false;
        //    preWord = word;
        //}
        // return true;
    
        int mapping[26];
        for (int i = 0; i < 26; i++)
            mapping[order[i] - 'a'] = i;
        for (string &w : words)
            for (char &c : w)
                c = mapping[c - 'a'];
        return is_sorted(words.begin(), words.end());
    }
};
