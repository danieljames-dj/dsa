class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def insert(root, val):
	if val > root.val:
		if root.right == None:
			root.right = Node(val)
		else:
			insert(root.right, val)
	else:
		if root.left == None:
			root.left = Node(val)
		else:
			insert(root.left, val)

def largest(root):
	if root.right == None:
		return root.val
	else:
		return largest(root.right)

def hasChild(root):
	return True if (root.right != None or root.left != None) else False

def secondLargest(root):
	if root.right == None:
		return largest(root.left)
	elif hasChild(root.right):
		return secondLargest(root.right)
	else:
		return root.val

arr = [int(_) for _ in input().split()]
root = Node(arr[0])
for i in range(1, len(arr)):
	insert(root, arr[i])
print(secondLargest(root))