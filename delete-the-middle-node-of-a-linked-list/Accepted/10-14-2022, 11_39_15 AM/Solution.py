// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast = slow = prev = head
        
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            
        if prev == slow:
            head = None
            
        prev.next = slow.next
        
        return head