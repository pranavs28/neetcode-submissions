# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        second = self.reverseList(second)
        first = head
        while second:
            n1 = first.next
            n2 = second.next
            first.next = second
            second.next = n1
            first, second = n1, n2


        return


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

        


        