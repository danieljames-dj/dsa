# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSubtreeSymmetric(self, tree1, tree2):
        return tree1 == None and tree2 == None or tree1 != None and tree2 != None and tree1.val == tree2.val and self.isSubtreeSymmetric(tree1.left, tree2.right) and self.isSubtreeSymmetric(tree1.right, tree2.left)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return root == None or self.isSubtreeSymmetric(root.left, root.right)