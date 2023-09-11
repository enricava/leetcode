// https://leetcode.com/problems/partition-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = firstNext = ListNode(0)
        second = secondNext = ListNode(0)
        
        while head:
            if head.val < x:
                firstNext.next = head
                firstNext = head
            else: 
                secondNext.next = head
                secondNext = head
            head = head.next
        
        firstNext.next = second.next
        secondNext.next = None
        return first.next