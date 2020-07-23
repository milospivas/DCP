def subsets(S, N):
  if N < 0:
    return -1

  if S == []:
    if 0 == N:
      return [[]]
    else:
      return -1

  #if len(S) > 1:
  sol = []
  if S[0] <= N:
    sol_with = subsets(S[1:], N - S[0])
    if -1 != sol_with:
      sol_with = [[S[0]] + x for x in sol_with]
      sol += sol_with

  sol_wout = subsets(S[1:], N)
  if -1 != sol_wout:
    sol += sol_wout

  if [] == sol:
    return -1
  else:
    return sol


def dp_numsubsets(N, S):
  dp = [[0 for _ in range(len(S) + 1)] for _ in range(N + 1)]

  # dp [ n ] [ x ] == dp_numsubsets(n, S[0:x])
  dp[0][0]

  print([0] + S)
  for n in range(1, N + 1):
    for i, num in zip(range(1, len(S) + 1), S):
      # if we're not including the i-th element
      dp[n][i] += dp[n][i - 1]

      # if we are including the i-th element but it is smaller than n
      if num < n:
        dp[n][i] += dp[n - num][i - 1]

      # if the i-th element is exactly n
      if num == n:
        dp[n][i] += 1

    print(dp[n], "n =", n)

  return dp[N][len(S)]


N = 16
S = [2, 4, 6, 10]

#   S =    [2, 2, 4, 4, 6, 10]
#     0  1  1  1  1  1  1  1
#     1  _  _  _  _  _  _  _
#     2  _  1  2  2  2  2  2
#     3  _  _  _  _  _  _  _
#     4  _  _  1  2  3  3  3
#     5  _  _  _  _  _  _  _
#     6  _  _  _  2  4  5  5
#     7  _  _  _  _  _  _  _
#     8  _  _  _  1  3  5  5
#     ...
print(dp_numsubsets(N, S))
