# PROBLEM
# Given an array of integers,
# return a new array such that
# each element at index i of the new array
# is the product of all the numbers in the original array
# except the one at i.

# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24].

# If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?


# SOLUTION
# With division - O(N)
def products(L):
  P = 1
  for el in L:
    P *= el

  return [round(P / x) for x in L]


# Follow-up: without division - O(N^2)
def products_nodiv(L):
  p = [1 for _ in L]

  for i in range(len(L)):
    for j in range(len(L)):
      if i != j:
        p[j] *= L[i]
  return p


# It could be sped up using a binary tree - O(NlogN)
import math


# compute the next highest power of 2 of 64-bit v
def next_pow2(v):
  v -= 1
  v |= v >> 1
  v |= v >> 2
  v |= v >> 4
  v |= v >> 8
  v |= v >> 16
  v |= v >> 32
  v += 1
  return v


def logloop(n):
  while n > 0:
    yield n
    n >>= 1


def product_bintree(L):

  class ptree:
    _tree = []
    _size = 0
    _n = 0
    _maxn = 0

    def __init__(self, list):
      self._n = len(list)
      self._maxn = next_pow2(self._n)
      self._size = 2 * self._maxn - 1
      self._tree = [1 for _ in range(self._size)]
      for i in range(self._n):
        self._tree[self._maxn - 1 + i] = list[i]

      for lvl in logloop(self._maxn - 1):
        for el in range(lvl, 2 * lvl + 1, 2):
          self._tree[el >> 1] = self._tree[el] * self._tree[el + 1]

    def print_tree(self):
      print(self._tree)

    def sibling(self, node):
      if node is None:
        return None
      if node == 0:
        return None
      if node % 2 == 0:
        return node - 1
      else:
        return node + 1

    def parent(self, node):
      if node == 0:
        return None
      else:
        return (node - 1) >> 1

    def node_product(self, node):
      P = 1
      temp = self.sibling(node + self._maxn - 1)
      while temp is not None:
        P *= self._tree[temp]
        temp = self.sibling(self.parent(temp))
      return P

  p = ptree(L)
  p.print_tree()
  return [p.node_product(x) for x in range(len(L))]


# [1, 2, 3]
# [p2p3, p1p3, p1p2]

#              p1p2p3p4p5
#     p1p2p3p4             p5
#   p1p2     p3p4      p5       1
# p1   p2   p3  p4   p5   1   1   1

#       0
#   1       2
# 3   4   5   6

# L = [1, 2, 3, 4, 5]
L = [x for x in range(1, 100)]
print("Naive sol:")
print(products(L))
print("No division:")
print(product_bintree(L))
print("With binary tree:")
print(products_nodiv(L))