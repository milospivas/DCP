# https://www.youtube.com/watch?v=5o-kdjv7FD0
# Problem:
# N - number of steps
# X - set of possible number of steps you can climb instantly

# How many different ways are there to climb the stairs?


# Recursive solution:
def calc(N, X):
  # Termination condition:
  if N == 0:
    # there's one way to cross 0 steps
    return 1

  # If there are remaining steps
  if N > 0:
    sol = 0
    # for every possible step from X
    for s in X:
      if s <= N:
        sol += calc(N - s, X)  # calculate No. of paths
    return sol  # return the sum of results

  else:  # hygienic
    return 0


# DP solution:
#   We need to memoize the recursion.
#   We will build it bottom up.
#   But the problem is symetrical so it doesn't matter.


def dpcalc(N, X):
  dp = [0 for _ in range(N + 1)]
  dp[N] = 1
  for n in range(N, 0, -1):
    for s in X:
      if 0 <= n - s:
        dp[n - s] += dp[n]
    # print(n, dp, X)
  return dp[0]


print(calc(3, [1, 2]))
print(dpcalc(3, [1, 2]))
