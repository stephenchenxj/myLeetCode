//
//  253. Meeting Rooms II.cpp
//  leetcode
//
//  Created by xujian chen on 6/3/20.
//  Copyright © 2020 xujian chen. All rights reserved.
//

/*
 253. Meeting Rooms II
 Medium

 2462

 41

 Add to List

 Share
 Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

 Example 1:

 Input: [[0, 30],[5, 10],[15, 20]]
 Output: 2
 Example 2:

 Input: [[7,10],[2,4]]
 Output: 1
 NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 Accepted
 276,641
 Submissions
 610,710
 */

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        
        int cnt = 0;
        vector<int> begins;
        vector<int> ends;
        
        for(auto i:intervals){
            begins.push_back(i[0]);
            ends.push_back(i[1]);
            //cout<<i[0]<<"-"<<i[1]<<endl;
        }
        
        sort(begins.begin(), begins.end());
        sort(ends.begin(), ends.end());
        
        int j = 0;
        int minRooms = 0;
        for(int i = 0; i < begins.size(); ++i){
            while(ends[j] <= begins[i]){
                j++;
                cnt--;
            }
            if (begins[i] < ends[j]) {
                cnt ++;
            }
            if (minRooms < cnt) minRooms = cnt;
        }
        
        return minRooms;
        
        
    }
};
