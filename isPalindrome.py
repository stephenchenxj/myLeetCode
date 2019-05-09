# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        movingNode = head
        oldHead = head
        newHead = head
        while movingNode.next:
            newHead = movingNode.next
            movingNode.next = movingNode.next.next
            newHead.next = oldHead
            oldHead = newHead
        return newHead
    
    def findMiddle(self, head):
        fast = head
        slow = head
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        value = []
        length = 0
        while head:
            value.append(head.val)
            head = head.next
            length += 1
        palindrome = True
        while length > 1:
            bottom = value.pop()
            top = value.pop(0)
            length -= 2
            if bottom != top:
                palindrome = False
                break
        
        return palindrome
        '''
        if not head:
            return True
        mid = self.findMiddle(head)
        secondHalfHead = mid.next
        mid.next = None
        
        secondHalfReverse = self.reverseList(secondHalfHead)
        
        palindrome = True
        while secondHalfReverse:
            if head.val != secondHalfReverse.val:
                palindrome = False
                break
            head = head.next
            secondHalfReverse = secondHalfReverse.next
        
        return palindrome
        
def main():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(1)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    mySolution = Solution().findMiddle(node1)
    print(mySolution.val)
    
    mySolution = Solution().isPalindrome(node1)
    print(mySolution)
    
if __name__ == '__main__':
    main()
    