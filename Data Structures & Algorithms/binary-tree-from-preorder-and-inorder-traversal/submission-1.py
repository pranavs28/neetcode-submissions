# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #first in preorder is the root
        #can use this to split inorder
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        inorder_root = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1 + inorder_root] , inorder[:inorder_root])
        root.right = self.buildTree(preorder[inorder_root + 1:], inorder[inorder_root+1:])
        return root

        
        
        