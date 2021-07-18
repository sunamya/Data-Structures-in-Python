class Node:
	
	# constructor to create node of
	# binary tree
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

class Height:
	def __init__(self):
		self.height = 0

def isBalanced(root):
	
	lh = Height()
	rh = Height()

	if root is None:
		return True

	l = isBalanced(root.left)
	r = isBalanced(root.right)

	if abs(lh.height - rh.height) <= 1:
		return l and r

	return False
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)

if isBalanced(root):
	print('Tree is balanced')
else:
	print('Tree is not balanced')
