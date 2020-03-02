# This problem was asked by Google.
# # PROBLEM

# The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
# Given two strings, compute the edit distance between them.


# # SOLUTION
# DP
# naive recursion:
def dp(a, b, i, j):
  if len(a) - i == 0:
    return len(b) - j
  if len(b) - j == 0:
    return len(a) - i

  # possible moves at a[i]:
  # if a[i] == b[j]: move on,
  # else:
  #   del(a[i]) - cost 1
  #   ins(b[j]) - cost 1
  #   swap(a[i], b[j]) - cost 1

  if a[i] == b[j]:
    return dp(a, b, i + 1, j + 1)
  else:
    guess_del = 1 + dp(a, b, i + 1, j)
    guess_ins = 1 + dp(a, b, i, j + 1)
    guess_swap = 1 + dp(a, b, i + 1, j + 1)
    return min(guess_del, guess_ins, guess_swap)

  # # TODO this is hardcoded but it can easily be replaced with a set of operations,
  # # with their costs given,
  # # and their i/j changes
  # # for example,
  # class Operation:
  #   def __init__(self, cost: int, del_i: int, del_j: int):
  #     self.cost = cost
  #     self.del_i = del_i
  #     self.del_j
  # # and then for delete:
  # op_del = Operation(1, 1, 0)
  # op_ins = Operation(1, 0, 1)
  # op_rep = Operation(1, 1, 1)
  # # so then
  # curr_min = None
  # for op in operation:
  #   guess = op.cost + dp(a, b, i + op.del_i, j + op.del_j)
  #   if curr_min is None or guess < curr_min:
  #     curr_min = guess
  # return curr_min


# with memoization:
def DP(a, b):
  dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
  for i in range(len(a) - 1, -1, -1):
    dp[i][len(b)] = 1 + dp[i + 1][len(b)]

  for j in range(len(b) - 1, -1, -1):
    dp[len(a)][j] = 1 + dp[len(a)][j + 1]


  for i in range(len(a) - 1, -1, -1):
    for j in range(len(b) - 1, -1, -1):
      if a[i] == b[j]:
        dp[i][j] = dp[i + 1][j + 1]
      else:
        guess_del = 1 + dp[i + 1][j]
        guess_ins = 1 + dp[i][j + 1]
        guess_swap = 1 + dp[i + 1][j + 1]
        dp[i][j] = min(guess_del, guess_ins, guess_swap)

  # for line in dp:
  #   print(line)
  return dp[0][0]


s1 = "sicko"
s2 = "Rick"
assert dp(s1, s2, 0, 0) == DP(s1, s2) == 2
# print(dp(s1, s2, 0, 0))
# print(DP(s1, s2))
