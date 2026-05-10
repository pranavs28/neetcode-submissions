class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -math.inf

        def dfs(root):
            if root is None:
                return 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            self.res = max(self.res, left + right + root.val)
            return root.val + max(left, right)
        dfs(root)
        return self.res