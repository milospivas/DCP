# This problem was asked by Airbnb.

# # PROBLEM
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.
# For example,
# [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?


# # SOLUTION
# definitely dp
# but first recursive variant as a proof of concept
def maxsum(l):
  if l == []:
    return 0
  if len(l) == 1:
    return max(0, l[0])
  if len(l) == 2:
    return max([0] + l)
  else:
    return max(maxsum(l[:-1]), l[-1] + maxsum(l[:-2]))


def dp_maxsum(l):
  dp = [None for _ in range(len(l))]
  dp[0] = max(0, l[0])
  dp[1] = max(0, l[0], l[1])

  for n in range(2, len(l)):
    dp[n] = max(dp[n - 1], dp[n - 2] + l[n])

  return dp[len(l) - 1]


def dp_maxsum_optimal(l):
  dp_2 = max(0, l[0])
  dp_1 = max(0, l[0], l[1])

  for n in range(2, len(l)):
    dp = max(dp_1, dp_2 + l[n])
    dp_2 = dp_1
    dp_1 = dp

  return dp_1


l1 = [-1, 2, 4, 6, 2, 5, -1]  # should return 13, since we pick 2, 6, and 5.
l2 = [-1, 5, 1, 1, 5, -1]  # should return 10, since we pick 5 and 5.

assert dp_maxsum_optimal(l1) == 13
assert dp_maxsum_optimal(l2) == 10
