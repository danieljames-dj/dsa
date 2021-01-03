# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q, res = [], []
        if root != None:
            q.append(root)
        while len(q) > 0:
            curLevel = []
            for i in range(len(q)):
                node = q.pop(0)
                curLevel.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            res.append(curLevel)
        return res