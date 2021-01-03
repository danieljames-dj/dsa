# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def heightIfBalanced(self, root):
        if root is None:
            return 0
        else:
            leftHeight = self.heightIfBalanced(root.left)
            rightHeight = self.heightIfBalanced(root.right)
            if leftHeight != None and rightHeight != None and abs(leftHeight - rightHeight) <= 1:
                return 1 + max(leftHeight, rightHeight)
            else:
                return None
    
    def isBalanced(self, root: TreeNode) -> bool:
        return self.heightIfBalanced(root) != None