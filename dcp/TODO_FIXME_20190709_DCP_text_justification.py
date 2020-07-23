# # This problem was asked by Palantir.
# # PROBLEM
# Write an algorithm to justify text.
# Given a sequence of words and an integer line length k,
# return a list of strings which represents each line, fully justified.

# More specifically, you should have as many words as possible in each line.
# There should be at least one space between each word.
# Pad extra spaces when necessary so that each line has exactly length k.
# Spaces should be distributed as equally as possible,
# with the extra spaces, if any, distributed starting from the left.

# If you can only fit one word on a line,
# then you should pad the right-hand side with spaces.
# Each word is guaranteed not to be longer than k.

# For example, given the list of words
# ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
# and k = 16,
# you should return the following:
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

# # SOLUTION
# DP


def score(words, k, i, j):
  num_words = j - i
  val = 0
  for x in range(i, j):
    val += len(words[x])
  val += num_words - 1

  if val <= k:
    return num_words - 1
  else:
    return -1


def justify(words, k):
  n = len(words)
  dp = [[0, 0, 0] for _ in range(0, n + 1)]

  for i in range(n - 1, -1, -1):
    max = -1
    max_j = None
    max_len = 0
    len_ij = 0
    num_words = 0
    for j in range(i + 1, n + 1):
      # score_ij = score(words, k, i, j)
      num_words += 1
      len_ij += len(words[j-1])
      
      if len_ij + num_words - 1 <= k:
        score_ij = len_ij + num_words - 1
      else:
        break
      
      temp = score_ij + dp[j][0]
      if temp > max:
        max = temp
        max_j = j
        max_len = len_ij
    dp[i] = [max, max_j, max_len]

  i = 0
  lines = []
  while i < n:
    line = ""
    char_len = dp[i][2]
    num_words = dp[i][1] - i
    padding = k - char_len - (num_words-1)
    if num_words == 1:
      # print(words[i], end="")
      line += words[i]
      for _ in range(padding):
        # print(" ", end="")
        line += " "
    else:
      per_space = padding // (num_words -1 )
      remainder = padding % (num_words -1 )
      for j in range(i, dp[i][1]):
        # print(words[j], end="")
        line += words[j]
        if j != dp[i][1] - 1 :
          for _ in range(per_space+1):
            # print(" ", end="")
            line += " "
          if remainder > 0:
            # print(" ", end="")
            line += " "
            remainder -= 1
    # print() 
    lines += [line]
    i = dp[i][1]
  return lines


words = [
    "the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "1",
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"
]
# words = [
#     "the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"
# ]
k = 16
lines = justify(words, k)
for l in lines:
  print(l)
