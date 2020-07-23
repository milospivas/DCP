# This problem was asked by Facebook.

# # PROBLEM
# A builder is looking to build a row of N houses
# that can be of K different colors.

# He has a goal of minimizing cost while ensuring that
# no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column
# represents the cost to build the nth house with kth color,
# return the minimum cost which achieves this goal.

# # SOLUTION
# Looks like DP


def find_min_rec(a, n, k):
  if n == 0:
    return a[0][k]

  K = len(a[0])

  lst = []
  for i in range(K):
    if i != k:
      lst += [a[n][k] + find_min_rec(a, n - 1, i)]

  return min(lst)


def find_min(a):
  N = len(a)
  K = len(a[0])
  sol = min([find_min_rec(a, N - 1, k) for k in range(K)])
  return sol


def find_min_dp(a):
  N = len(a)
  K = len(a[0])

  dp0 = a[0]
  for n in range(1, N):
    dp1 = dp0
    dp0 = []
    for k in range(K):
      lst = []
      for i in range(K):
        if i != k:
          lst += [[a[n][k] + dp1[i]]]
      dp0 += min(lst)
  return min(dp0)


a = [[2, 1], [0, 3], [2, 5]]
print(find_min(a))
print(find_min_dp(a))
