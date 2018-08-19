class TreeNode:
	def __init__(self, val, n):
		self.val = val
		self.children = [None] * n

class BinaryTreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None

	def insert(self, val):
		if not self.root:
			self.root = BinaryTreeNode(val)
			return

		cursor = self.root
		while True:
			if val <= cursor.val:
				if cursor.left:
					cursor = cursor.left
				else:
					cursor.left = BinaryTreeNode(val)
					return
			else:
				if cursor.right:
					cursor = cursor.right
				else:
					cursor.right = BinaryTreeNode(val)
					return

	def search(self, val):
		cursor = self.root

		while cursor:
			if val == cursor.val:
				return True
			elif val <= cursor.val:
				cursor = cursor.left
			else:
				cursor = cursor.right

		return False

	def remove(self, val):
		self.remove_helper(self.root, val)

	def remove_helper(root, val):
		if root is None:
			return

		if val == root.val:
			if root.left is None:
				return root.right
			elif root.right is None:
				return root.left

			temp = root.right
			while temp:
				temp = temp.left
			root.val = temp.val
			self.remove_helper(root.right, temp.val)
		elif val < root.val:
			root.left = self.remove_helper(root.left, val)
		else:
			root.right = self.remove_helper(root.right, val)