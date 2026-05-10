# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_pointer = head
        hare = head
        for i in range(n):
            hare = hare.next

        if not hare:
            return head.next
        
        while hare and hare.next:
            n_pointer = n_pointer.next
            hare = hare.next
        
        if n_pointer.next:
            n_pointer.next = n_pointer.next.next
        else:
            n_pointer = None
        return head

        
        