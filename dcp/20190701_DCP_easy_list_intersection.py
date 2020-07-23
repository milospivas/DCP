# # PROBLEM [Easy]
# Given two singly-linked lists that intersect at some point,
# find the intersecting node in O(M + N) time and O(1) space,
# where M and N are list lengths.

# Example:
# l1 = 3 -> 7 -> 8 -> 10
# l2 = 99 -> 1 -> 8 -> 10
# sol = 8

# # SOLUTION
# Given that the problem was marked as [Easy] and in the example, the lists intersect at the 3rd node of both lists,
# I will assume that by "intersect at some point" they mean that the intersecting point is a node with the same distance from the starting node in both lists.


class Node:

  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next


class SinglyList:

  def __init__(self, list=None):
    self.head = Node()
    aux = self.head

    for i in range(len(list)):
      aux.data = list[i]
      if i < len(list) - 1:
        aux.next = Node()
        aux = aux.next

  def print(self):
    aux = self.head
    while aux is not None:
      print(aux.data)
      aux = aux.next


def find_intersection(l1, l2):
  aux1 = l1.head
  aux2 = l2.head

  while aux1 is not None and aux2 is not None:
    if aux1.data == aux2.data:
      return aux1.data
      # print(aux1.data)
      # break
    aux1 = aux1.next
    aux2 = aux2.next

  return None


l1 = SinglyList([3, 7, 8, 10])
l2 = SinglyList([99, 1, 8, 10])

# l1.print()
# print()
# l2.print()

print(find_intersection(l1, l2))
