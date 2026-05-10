class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def depth(node):
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        depth(root)
        return self.res