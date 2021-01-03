# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def clone(self, node, adder):
        if node == None:
            return None
        tree = TreeNode(node.val + adder)
        tree.left = self.clone(node.left, adder)
        tree.right = self.clone(node.right, adder)
        return tree
        
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        dp = {}
        dp[0] = [None]
        dp[1] = [TreeNode(1)]
        dp[2] = [TreeNode(1, None, TreeNode(2)), TreeNode(2, TreeNode(1), None)]
        for i in range(3, n+1):
            dp[i] = []
            for j in range(1, i+1):
                for left_node in dp[j-1]:
                    for right_node in dp[i-j]:
                        newTree = TreeNode(j)
                        newTree.left = self.clone(left_node, 0)
                        newTree.right = self.clone(right_node, j)
                        dp[i].append(newTree)
        return dp[n]