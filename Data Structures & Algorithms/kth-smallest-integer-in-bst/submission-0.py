# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #in-order-traversal with overhead for value
        self.visited = 0
        self.result = -1

        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            self.visited += 1
            if self.visited == k:
                self.result = root.val
            dfs(root.right)
            return

        dfs(root)
        return self.result


        
        