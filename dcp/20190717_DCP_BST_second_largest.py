# This problem was asked by Dropbox.
# # PROBLEM

# Given the root to a binary search tree, find the second largest node in the tree.
# # SOLUTION
# BST condition:
# The left child of the node is always smaller, and the right child is always greater then or equal to the node.
# So, go right until you can. That's the largest node.
# If he has a left child, that's the second largest.
# If he doesn't, his parent is the second largest.


class BSTNode:

  def __init__(self, val=None, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def second_largest(root):
  if root is None:
    return None

  curr = root
  parent = None

  while curr.right is not None:
    parent = curr
    curr = curr.right

  if curr.left is not None:
    return curr.left
  else:
    return parent


root = BSTNode(1, BSTNode(-1, BSTNode(-3)))
assert second_largest(root).val == -1

root = BSTNode(1, None, BSTNode(3, None, BSTNode(5)))
assert second_largest(root).val == 3

root = BSTNode(1, None, BSTNode(3, None, BSTNode(5, BSTNode(4))))
assert second_largest(root).val == 4

root = BSTNode(42)
assert second_largest(root) == None

root = None
assert second_largest(root) == None

print("Unit tests passed.")