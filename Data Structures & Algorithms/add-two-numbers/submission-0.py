# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit_val = 1
        curr = l1
        l1_val = 0
        l2_val = 0
        while curr:
            l1_val += (curr.val * digit_val)
            digit_val *= 10
            curr = curr.next
        
        curr = l2
        digit_val = 1
        while curr:
            l2_val += (curr.val * digit_val)
            digit_val *= 10
            curr = curr.next
        
        new_val = l1_val + l2_val
        val_str = str(new_val)[::-1]
        
        head = None
        tail = None
        for char in val_str:
            char_node = ListNode(int(char))
            if not tail:
                head = char_node
                tail = char_node
            else:
                tail.next = char_node
                tail = tail.next
        
        return head

        

        