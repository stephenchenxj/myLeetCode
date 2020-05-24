//
//  543. Diameter of Binary Tree.cpp
//  leetcode
//
//  Created by Xujian CHEN on 5/24/20.
//  Copyright © 2020 Xujian CHEN. All rights reserved.
//

/*
 
 543. Diameter of Binary Tree
 Easy

 2771

 177

 Add to List

 Share
 Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

 Example:
 Given a binary tree
           1
          / \
         2   3
        / \
       4   5
 Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

 Note: The length of path between two nodes is represented by the number of edges between them.

 Accepted
 312,989
 Submissions
 651,754
 
 */


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    
    int l_r(TreeNode* root, int& len){
        int l, r;
        if (root->left == nullptr){
            l = 0;
        }else{
            l = l_r(root->left, len)+ 1;
        }
        if (root->right == nullptr){
            r = 0;
        }else{
            r = l_r(root->right, len)+ 1;
        }
        
        if (len < l + r) len = r + l;
        
        return max(l,r) ;
    }
    
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if (root == nullptr) return 0;
        int len = 0;
        l_r(root, len);
        return len;
    }
};
