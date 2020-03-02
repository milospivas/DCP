# This problem was asked by Amazon.

# # PROBLEM
# There exists a staircase with N steps,
# and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase.
# The order of the steps matters.
#
# For example, if N is 4, then there are 5 unique ways:
# •	1, 1, 1, 1
# •	2, 1, 1
# •	1, 2, 1
# •	1, 1, 2
# •	2, 2
#
# What if, instead of being able to climb 1 or 2 steps at a time,
# you could climb any number from a set of positive integers X?
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

# # SOLUTION
# straight to the DP solution:


# Time complexity O(N*X)
# Space complexity O(N)
def dp_numways(N, X):
  dp = [0 for _ in range(N + 1)]
  dp[0] = 1

  for i in range(0, N):
    for x in X:
      if i + x <= N:
        dp[i + x] += dp[i]
  return dp[N]


# Time complexity O(XlogX + N*X)
# Space complexity O(X)
def dp_numways_opti(N, XmaybeNotSorted):
  from collections import deque as deq

  X = sorted(XmaybeNotSorted)  # O(XlogX)
  dp = deq([0 for _ in range(X[-1] + 1)])  # O(X)
  dp[0] = 1
  # dp is now a double-ended queue and we can use it as a circular buffer

  for i in range(0, N):  # O(N*X)
    # print(i, ":", dp)
    for x in X:
      if i + x <= N:
        dp[x] += dp[
            0]  # we replace i with 0 because we right-shift the buffer in every iteration

    # right-shift of the buffer:
    dp.popleft()
    if i + X[-1] < N:
      dp.append(0)

  # print(N, ":", dp)
  return dp[0]


N = 5
X = [1, 2, 3]
assert dp_numways(N, X) == dp_numways_opti(N, X)