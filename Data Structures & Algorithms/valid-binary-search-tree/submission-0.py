class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValidBSTHelper(root):
            if root is None:
                return [True, float('inf'), float('-inf')]
            else:
                left_valid, left_min, left_max = isValidBSTHelper(root.left)
                right_valid, right_min, right_max = isValidBSTHelper(root.right)
                
                is_valid = left_valid and right_valid and left_max < root.val < right_min
                
                return [is_valid, min(root.val, left_min), max(root.val, right_max)]
        
        return isValidBSTHelper(root)[0]