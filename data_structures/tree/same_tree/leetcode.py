# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return (p == None and q == None or p != None and q != None and p.val == q.val
            and (p.left == None and q.left == None or self.isSameTree(p.left, q.left))
            and (p.right == None and q.right == None or self.isSameTree(p.right, q.right)))