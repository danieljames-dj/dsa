# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        cur = root
        res = []
        while root != None:
            if root.left == None:
                res.append(root.val)
                root = root.right
            else:
                cur = root.left
                while cur.right != None and cur.right != root:
                    cur = cur.right
                if cur.right == root:
                    cur.right = None
                    res.append(root.val)
                    root = root.right
                else:
                    cur.right = root
                    root = root.left
        return res