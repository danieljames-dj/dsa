# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def mistakeNode(self, root, prev, first, middle):
        if root.left != None:
            prev, first, middle = self.mistakeNode(root.left, prev, first, middle)
        if prev != None and root.val < prev.val:
            if first == None:
                first = prev
            middle = root
        if root.right != None:
            return self.mistakeNode(root.right, root, first, middle)
        else:
            return (root, first, middle)
    
    def recoverTree(self, root: TreeNode) -> None:
        _, first, middle = self.mistakeNode(root, None, None, None)
        temp = first.val
        first.val = middle.val
        middle.val = temp