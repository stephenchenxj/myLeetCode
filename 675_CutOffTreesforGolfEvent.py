"""
675. Cut Off Trees for Golf Event
Hard

446

258

Add to List

Share
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
In one step you can walk in any of the four directions top, bottom, left and right also when standing in a point which is a tree you can decide whether or not to cut off the tree.

You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:

Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
 

Example 2:

Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
 

Example 3:

Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
 

Constraints:

1 <= forest.length <= 50
1 <= forest[i].length <= 50
0 <= forest[i][j] <= 10^9
Accepted
26,847
Submissions
79,580


"""


class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        tree = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    tree.append([forest[i][j], (i,j)])
        
        tree = sorted(tree)
        steps = 0
        st = (0,0)
        c = 0
        last = None
        for entry in tree:
            to = entry[1]
            c = self.bfs(st,to, forest)
            if c == -1:
                return -1
            steps += c
            st = to
        
        return steps
    
    
    def bfs(self,fr,target, forest):
        l = []
        l.append((0,fr[0],fr[1]))
        vis = set()
        vis.add(fr)
        ll = 0
        while ll < len(l):
            c, i, j = l[ll]
            ll += 1
            if (i,j) == target:
                forest[i][j] = 1
                return c
            for x,y in [(i-1,j),(i,j-1),(i,j+1),(i+1,j)]:
                if x >= 0 and x < len(forest) and y >= 0 and y < len(forest[0]) and (x,y) not in vis and forest[x][y] > 0:
                    l.append((c+1,x,y))
                    vis.add((x,y))
        
        return -1