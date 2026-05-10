# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()

        if root:
            q.append([root, root.val])
        
        good_nodes = 0

        while len(q) > 0:
            curr = q.popleft()
            if curr[0].val >= curr[1]:
                good_nodes += 1
            
            new_max = max(curr[0].val, curr[1])
            if curr[0].left:
                q.append([curr[0].left, new_max])
            if curr[0].right:
                q.append([curr[0].right, new_max])
        
        return good_nodes
