# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        prev = None
        next = head.next
        while curr.next != None:
            curr.next = prev
            prev = curr
            curr = next
            next = curr.next
        
        curr.next = prev
        return curr



        