# This problem was asked by Google.
# # PROBLEM

# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.
# The list is very long, so making more than one pass is prohibitively expensive.
# Do this in constant space and in one pass.

# # SOLUTION
# 1. Have two pointers left and right
# 2. Init them both to the begining of the list
# 3. Iterate right k times
# 4. Iterate both of them, keeping the current value of left.val, until right is null
# 5. return the last value of left.val


class Node:

  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next


def get_kth_last(head, k):
  left = right = head

  for _ in range(k):
    right = right.next

  while right is not None:
    val = left.val
    left = left.next
    right = right.next

  return val


head = Node(1, Node(2, Node(3, Node(4))))
for k in range(4):
  sol = get_kth_last(head, k)
  print(sol)