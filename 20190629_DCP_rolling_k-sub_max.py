# This problem was asked by Google.

# # PROBLEM
# Given an array of integers and a number k,
# where 1 <= k <= length of the array,
# compute the maximum values of each subarray of length k.

# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3,
# we should get: [10, 7, 8, 8], since:
# •	10 = max(10, 5, 2)
# •	7 = max(5, 2, 7)
# •	8 = max(2, 7, 8)
# •	8 = max(7, 8, 7)

# Do this in O(n) time and O(k) space.
# You can modify the input array in-place and you do not need to store the results.
# You can simply print them out as you compute them.

# # SOLUTION
# First I would say that double ended queue would be a good structure to use
# But it isn't really needed since k is given and it is static
# So we can implement some sort of a circular buffer:
# class cbuff:

#   def __init__(self, k):
#     self._k_ = k
#     self._lst_ = [None for _ in range(k)]
#     self._offset_ = 0
#     self._max_ = None

#   # 0123456789
#   # 012012012012

#   def getleft(self):
#     return self._lst_[self._offset_]

#   def insert(self, val):
#     self._lst_[self._offset_] = val
#     self._offset_ += 1
#     self._offset_ %= self._k_

#     if val > self._max_:
#       self._max_ = val

# Nope
# This is all wrong
# We need a O(k) size structure
# That keeps a max, with get_max() is O(1)
# And where push_right, pop_left take O(1) time
#

# k = 3
# a = [10, 7, 2, 5, 8, 7]
# 10 - max 10
# 10 7 - max 10
# 10 7 2 - max 10
# 7 2 5 - max 7

from collections import deque

# The solution is O(n) time
# We're using a O(k) sized double-ended queue "dq"
# It always holds indices of elements from currently viewed subarray
# If dq = [i0, i1, ... i_m],
# a[i0] is the maximum of the subarray,
# a[i1] is the maximum of the subarray a[i0 +1 : i1 +1]
# a[i2] is the maximum of the subarray a[i1 +1 : i2 +1]
# ...


def k_sub_min(a, k):
  dq = deque([])
  # go through the array a
  for i in range(len(a)):

    # if we have passed the first subarray,
    # and if the index of the first element of the previous subarray is still in the dq
    # pop that element
    if i >= k and dq[0] == i - k:
      dq.popleft()

    # if we can add more elements to the dq
    if len(dq) < k:
      # go from right side and pop all indices of elements
      # that are smaller than the current element
      while len(dq) and a[dq[-1]] < a[i]:
        dq.pop()  # this is popright()

      # append the current element's index
      dq.append(i)  # this is pushright()

    # if we have passed first k-1 elements,
    # print the max of current subarray
    if i >= k - 1:
      print(a[dq[0]])


#       0  1  2  3  4  5
# a = [10, 7, 2, 5, 8, 7]
a = [3, 2, 1, 5, 1, 4, 1, 2]
# a = [4, 3, 2, 1, 0, -1]
k = 3
# a = []
# k = 0
k_sub_min(a, k)