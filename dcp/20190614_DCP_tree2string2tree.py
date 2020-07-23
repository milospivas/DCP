# PROBLEM
# Given the root to a binary tree,
# implement serialize(root),
# which serializes the tree into a string,
# and deserialize(s),
# which deserializes the string back into the tree.

# For example, given the following Node class


class Node:
  val = None
  left = None
  right = None

  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

# SOLUTION
# I'm not sure what do they mean exactly with "serializing the tree into a string"
# So I'm assuming that the point is to bijectively map the tree into a string
#
# Ok, so first idea that pops up for serialize() is:
# 1. Turn the tree into a list where
#      list[0] is root and list[2*i] is left, list[2*i+1] is right child
#      We do that with BFS traversal
# 2. Then flatten the val list into a string
#       have a special character sepparating the elements (like "\n")
#


def serialize(root):
  s = ""
  q = [root]
  current = 0
  while current < len(q):
    if q[current] is not None:
      s += q[current].val + "\n"
      q += [q[current].left]
      q += [q[current].right]
    else:
      s += "\n"

    current += 1
  return s


def deserialize(s):
  q = []
  val = ""
  for c in s:
    if c == "\n":
      q += [val]
      val = ""
    else:
      val += c

  q[0] = Node(q[0])
  for i in range(len(q) // 2):
    if q[i] != "":
      if q[2 * i + 1] != "":
        q[i].left = Node(q[2 * i + 1])
        q[2 * i + 1] = q[i].left

      if q[2 * i + 2] != "":
        q[i].right = Node(q[2 * i + 2])
        q[2 * i + 2] = q[i].right
  return q[0]


node = Node('root', Node('left', Node('left.left')), Node('right'))
# s = serialize(node)
# print(s)
# root = deserialize(s)
assert deserialize(serialize(node)).left.left.val == 'left.left'
