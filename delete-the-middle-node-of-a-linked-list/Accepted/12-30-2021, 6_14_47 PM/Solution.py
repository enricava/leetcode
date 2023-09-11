// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        prev = slow = fast = head
        count = 1
        while fast and fast.next:
            count += 1
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = slow.next
        
        if count <= 1:
            head = None
            
        return head