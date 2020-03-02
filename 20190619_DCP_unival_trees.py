# This problem was asked by Google.

# # PROBLEM
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

# # SOLUTION
# definitely DP solution


# tree would probably be given in this format
class node:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  # ...


#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
#
#           0
#     1           2
#  3    4      5      6
# 7 8  9 10  11 12  13 14
#
#           0
#     2           2
#  1    0      1      6
# 1 1  4 5   1  1   2   2
#

# def list_add_element(l, idx, element):
#   if element is not None:
#     n = len(l)
#     if idx >= n:
#       l += [None for _ in range(n, idx + 1)]
#     l[idx] = element
#   return l

# # I want to convert it to array representation
# # Level by level search is good
# def tree_array(tree):
#   a = [tree]
#   q = [tree]
#   i = 0
#   while i < len(q):
#     if q[i] is not None:
#       q += [q[i].left]
#       q += [q[i].right]
#       a = list_add_element(a, 2 * i + 1, q[i].left)
#       a = list_add_element(a, 2 * i + 2, q[i].right)
#     i += 1
#   return a

# def get_sibling(artree, idx):
#   if idx == 0:
#     return None
#   if idx % 2 == 0:
#     return idx - 1
#   else:
#     return idx + 1

# def num_univals(tree):
#   artree = tree_array(tree)
#   unival = [False for _ in artree]
#   n = len(artree)
#   sol = 0
#   for i in range(n - 1, 0, -1):
#     if artree[i] is not None:
#       if (artree[i].left is None and artree[i].right is None):
#         sol += 1
#         unival[i] = True
#       if i % 2 == 1:
#         i_sib = get_sibling(artree, i)
#         if (unival[i] == unival[i_sib] == True) and (
#             artree[i].val == artree[i_sib].val == artree[i // 2].val):
#           sol += 1
#           unival[i // 2] = True
#   return sol

# tree = node(0, node(1), node(0, node(1, node(1), node(1)), node(0)))

# # a = tree_array(tree)
# # i = 0
# # for vert in a:
# #   if vert is not None:
# #     print(i, vert.val)
# #   else:
# #     print(i, None)
# #   i += 1

# assert num_univals(tree) == 5

# ------------------------- ------------------------- ------------------------- ------------------------- ------------------------- -------------------------
# The solution above is too complex, you don't have to make a heap like structure when putting vertices in an array
# So:


# Starting from root, going level by level, flatens the tree into a list of lists
# where each element is represented as [node, left_idx, right_idx]
def tree2list(root):
  if root is not None:
    l = [[root]]
    i = 0
    while i < len(l):
      if l[i][0].left is not None:
        l[i] += [len(l)]
        l += [[l[i][0].left]]
      if l[i][0].right is not None:
        l[i] += [len(l)]
        l += [[l[i][0].right]]
      i += 1
    return l
  else:
    return None


# Flatens the tree into a list
# Goes from last node to root and checks if the subtree of the given root is unival
# It remembers if it in the unival list
def num_univals_opt(root):
  lst = tree2list(tree)
  unival = [False for _ in lst]

  sol = 0
  for i in range(len(lst) - 1, -1, -1):
    if lst[i][0].left is None and lst[i][0].right is None:
      sol += 1
      unival[i] = True
    if lst[i][0].left is not None and lst[i][0].right is not None:
      if lst[i][0].left.val == lst[i][0].right.val == lst[i][0].val and (
          unival[lst[i][1]] and unival[lst[i][2]]):
        sol += 1
        unival[i] = True
  return sol


#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
tree = node(0, node(1), node(0, node(1, node(1), node(1)), node(0)))
assert num_univals_opt(tree) == 5

#     0
#   /  \
#  1     0
#     /    \
#    0      0
#   / \   /  \
#  1   1 0    0
tree = node(0, node(1),
            node(0, node(0, node(1), node(1)), node(0, node(0), node(0))))
assert num_univals_opt(tree) == 6
