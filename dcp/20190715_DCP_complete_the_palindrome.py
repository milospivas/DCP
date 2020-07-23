# This problem was asked by Quora.
# # PROBLEM
# Given a string, find the palindrome that can be made by inserting
# the fewest number of characters as possible anywhere in the word.
# If there is more than one palindrome of minimum length that can be made,
# return the lexicographically earliest one (the first one alphabetically).

# For example, given the string "race", you should return "ecarace",
# since we can add three letters to it (which is the smallest amount
# to make a palindrome). There are seven other palindromes that can be made
# from "race" by adding three letters, but "ecarace" comes first alphabetically.

# As another example, given the string "google", you should return "elgoogle".

# # SOLUTION
# DP


# naive recursion:
def min_insertions1(s):
  if s == "":
    return 0

  if s[0] == s[-1]:
    return (min_insertions1(s[1:-1]))
  else:
    return min(min_insertions1(s[1:]), min_insertions1(s[:-1])) + 1


# optimized
def min_insertions2(s, l, r):
  if l >= r - 1:
    return 0

  if s[l] == s[r - 1]:
    return (min_insertions2(s, l + 1, r - 1))
  else:
    return min(min_insertions2(s, l + 1, r), min_insertions2(s, l, r - 1)) + 1


# now we need to add the option of returning the optimal palindrome
def nearest_palindrome1(s, l, r):
  if l > r - 1:
    return ""
  if l == r - 1:
    return s[l]

  if s[l] == s[r - 1]:
    return s[l] + nearest_palindrome1(s, l + 1, r - 1) + s[r - 1]
  else:
    s1 = s[l] + nearest_palindrome1(s, l + 1, r) + s[l]
    s2 = s[r - 1] + nearest_palindrome1(s, l, r - 1) + s[r - 1]
    if len(s1) < len(s2):
      smallest = s1
    if len(s1) > len(s2):
      smallest = s2
    if len(s1) == len(s2):
      smallest = s1 if (s1 < s2) else s2
    return smallest


# now we need to make a bottom-up, memoized version
# since we're dealing with substrings, we need a 2D array
def nearest_palindrome_dp(s):
  n = len(s)
  dp = [["" for _ in range(n)] for _ in range(n)]
  for i in range(n):
    dp[i][i] = s[i]

  for i in range(1, n):
    for j in range(i, n):
      # print("{},{}".format(j - i, j), end=" ")
      l = j - i
      r = j

      if s[l] == s[r]:
        dp[l][r] = s[l] + dp[l + 1][r - 1] + s[r]
      else:
        s1 = s[l] + dp[l + 1][r] + s[l]
        s2 = s[r] + dp[l][r - 1] + s[r]
        n1 = len(s1)
        n2 = len(s2)
        if n1 < n2:
          smallest = s1
        if n1 > n2:
          smallest = s2
        if n1 == n2:
          smallest = s1 if s1 < s2 else s2
        dp[l][r] = smallest

  return dp[0][n - 1]


s = "google"
# s = "race"
print(min_insertions1(s))
print(min_insertions2(s, 0, len(s)))
print(nearest_palindrome1(s, 0, len(s)))
print(nearest_palindrome_dp(s))