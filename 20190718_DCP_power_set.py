# This problem was asked by Google.

# # PROBLEM
# The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
# You may also use a list or array to represent a set.

# # SOLUTION

# import scipy.special


def power_set(s: list) -> list:
  n = len(S)
  if n == 0:
    return [[]]

  if n == 1:
    return [[], s]

  D = {}
  i = 0
  for x in s:
    D[i] = x
    i += 1

  n = len(s)
  lst = [[] for _ in range(n)]
  lst[0] = [[]]
  lst[1] = [[x] for x in range(n)]
  lst += [[list(range(n))]]

  for k in range(2, n):
    # m = len(lst[k - 1])
    for i in range(len(lst[k - 1])):
      for j in range(lst[k - 1][i][-1] + 1, n):
        lst[k] += [lst[k - 1][i] + [j]]

  # print(lst)

  for k in range(len(lst)):
    for i in range(len(lst[k])):
      for j in range(len(lst[k][i])):
        lst[k][i][j] = D[lst[k][i][j]]

  return lst


S = ["a", "b", "c", "d"]
PS = power_set(S)
print(PS)