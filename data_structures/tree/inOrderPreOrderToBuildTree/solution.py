class Node:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None

def buildTree(preOrder, inOrder, treeSize, start, end, root, indexKeys):
	index = indexKeys[root.val]
	if index > start:
		root.left = Node(preOrder[treeSize])
		treeSize += 1
		treeSize = buildTree(preOrder, inOrder, treeSize, start, index, root.left, indexKeys)
	if index < end - 1:
		root.right = Node(preOrder[treeSize])
		treeSize += 1
		treeSize = buildTree(preOrder, inOrder, treeSize, index+1, end, root.right, indexKeys)
	return treeSize

def printTree(root):
	if root == None:
		return
	printTree(root.left)
	print(root.val, end = ' ')
	printTree(root.right)

preOrder = input().split()
inOrder = input().split()
indexKeys = {}
for i in range(len(inOrder)):
	indexKeys[inOrder[i]] = i
root = Node(preOrder[0])
buildTree(preOrder, inOrder, 1, 0, len(inOrder), root, indexKeys)
printTree(root)