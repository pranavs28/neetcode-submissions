# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def is_balanced_helper(root):
            if not root:
                return True, 0
            height = 1
            left_balance, left_height = is_balanced_helper(root.left)

            right_balance, right_height = is_balanced_helper(root.right)
            
            if not (left_balance and right_balance) or abs(right_height - left_height) > 1:
                return False, 0
            else:
                return True, 1 + max(left_height, right_height)

        res, height = is_balanced_helper(root)
        return res
        


        
        