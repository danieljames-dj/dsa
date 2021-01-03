# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def solve(self, root, last = -100000000000000):
        if root.left != None:
            last = self.solve(root.left, last)
        if last == None or root.val <= last:
            return None
        elif root.right != None:
            return self.solve(root.right, root.val)
        else:
            return root.val
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.solve(root) != None if root != None else True