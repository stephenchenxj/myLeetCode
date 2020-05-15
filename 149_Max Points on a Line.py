"""
149. Max Points on a Line
Hard

758

1823

Add to List

Share
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

Accepted
148,186
Submissions
885,247

"""


from fractions import Fraction

class Solution(object):
    
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        #a =Fraction(6,5)
        #print(type(a))
        #print(Fraction(12,10))
        if len(points) < 3:
            return len(points)
        
        ans = 0
        lines = dict()
        for i in range(len(points)):
            x0 = points[i][0]
            y0 = points[i][1]
            dup = 0
            lines.clear()
            
            for j in range(i+1, len(points)):
                x1 = points[j][0]
                y1 = points[j][1]
                
                dy = y1 - y0
                dx = x1 - x0
                
                slope = 0
                if dx == 0 and dy == 0:
                    dup += 1
                    print(dup)
                elif dx == 0:
                    slope = float("inf")
                    lines[slope] = lines.get(slope, 1) + 1
                else:
                    slope = Fraction(dy, dx)
                    lines[slope] = lines.get(slope, 1) + 1
            
            if lines:
                cnt = max(lines.values()) + dup
            else:
                cnt = 1 + dup
                
            if ans < cnt:
                ans = cnt
        return ans