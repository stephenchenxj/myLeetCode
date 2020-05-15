/*
2. Add Two Numbers
Medium

7742

1986

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
Accepted
1,331,488
Submissions
4,005,817

*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int forward = 0;
        ListNode* pre_node = NULL;
        ListNode* head = NULL;
        while (l1 != NULL || l2 != NULL || forward != 0){
            int val = 0;
            if (l1 != NULL) val += l1->val;
            if (l2 != NULL) val += l2->val;
            if (forward != 0) val += forward;

            forward = val/10;
            val = val%10;
            ListNode* cur = new ListNode(val);
            if (head == NULL){
                head = cur;
            }
            if (pre_node == NULL){
                pre_node = cur;
            }
            else{
                pre_node->next = cur;
            }
            if (l1!= NULL)
                l1 = l1->next;
            if(l2 != NULL)
                l2 = l2->next;
            pre_node = cur;

        }
        return head;

    }
};
