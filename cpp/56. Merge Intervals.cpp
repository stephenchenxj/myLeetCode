//
//  56. Merge Intervals.cpp
//  leetcode
//
//  Created by xujian chen on 6/1/20.
//  Copyright © 2020 xujian chen. All rights reserved.
//

/*
 56. Merge Intervals
 Medium

 3882

 277

 Add to List

 Share
 Given a collection of intervals, merge all overlapping intervals.

 Example 1:

 Input: [[1,3],[2,6],[8,10],[15,18]]
 Output: [[1,6],[8,10],[15,18]]
 Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
 Example 2:

 Input: [[1,4],[4,5]]
 Output: [[1,5]]
 Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 Accepted
 569,798
 Submissions
 1,471,981
 */

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.size() == 0) return intervals;
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> merged;
        
        int i = 0;
        merged.push_back({intervals[0][0],intervals[0][1]});
        
        while(i<intervals.size()){
            while (merged.back()[1] >= intervals[i][0] ){
                merged.back()[1] = max(merged.back()[1],intervals[i][1]);
                ++i;
                if (i==intervals.size()) break;
            }
            if(i<intervals.size())
                merged.push_back({intervals[i][0],intervals[i][1]});
        }
        
        return merged;
    }
};
