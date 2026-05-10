class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        self.res = False
        def sameTree(a, b):
            if a is None and b is None:
                return True
            elif a is None or b is None:
                return False
            else:
                if sameTree(a.left, b.left) and sameTree(a.right, b.right) and a.val==b.val:
                    return True
                else:
                    return False

        if subRoot is None:
            return True
        if root is None:
            return False

        if sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)