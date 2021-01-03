# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        loc = 0
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                break
            loc += 1
        root.left = self.buildTree(preorder[1:loc+1], inorder[:loc+1])
        root.right = self.buildTree(preorder[loc+1:], inorder[loc+1:])
        return root