"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ll_archive = {}

        curr = head
        prev = None
        copy_list = None
        while curr:
            copy = Node(curr.val)
            ll_archive[curr] = copy
            if prev:
                ll_archive[prev].next = copy
            else:
                copy_list = copy
                
            prev = curr
            curr = curr.next

        copy_curr = copy_list
        curr = head
        print(ll_archive)
        while copy_curr:
            if curr.random is not None:
                copy_curr.random = ll_archive[curr.random]
            curr = curr.next
            copy_curr = copy_curr.next
        
        return copy_list

        



        