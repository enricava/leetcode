// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        prev = head
        head = prev.next
        nextt = head.next
        prev.next = None
        while nextt != None:
            head.next = prev
            prev = head
            head = nextt
            nextt = nextt.next
        head.next = prev
        return head