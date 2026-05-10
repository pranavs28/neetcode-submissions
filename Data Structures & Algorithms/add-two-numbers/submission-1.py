# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = l1
        l2_curr = l2

        res_head = None
        res_tail = None
        carry = 0

        while l1_curr or l2_curr or carry > 0:
            if l1_curr and l2_curr:
                val = (l1_curr.val + l2_curr.val + carry) % 10
                carry = (l1_curr.val + l2_curr.val + carry) // 10
            elif l1_curr:
                val = (l1_curr.val + carry) % 10
                carry = (l1_curr.val + carry) // 10
            elif l2_curr:
                val = (l2_curr.val + carry) % 10
                carry = (l2_curr.val + carry) // 10
            else:
                val = carry
                carry = 0

            digit_node = ListNode(val)
            if not res_tail:
                res_head = digit_node
                res_tail = digit_node
            else:
                res_tail.next = digit_node
                res_tail = res_tail.next
            
            if l1_curr:
                l1_curr = l1_curr.next
            if l2_curr:
                l2_curr = l2_curr.next
        
        return res_head



        

        