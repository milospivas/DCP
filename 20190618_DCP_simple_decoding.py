# This problem was asked by Facebook.

# # PROBLEM

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
# count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

# # SOLUTION

# _1     : 1
# 1_1    : 1 + 1 = 2
# 11_1   : 2 + 1


def numways(msg):
  if len(msg) == 0:
    return 1
  if len(msg) == 1:
    return 1
  else:
    temp = numways(msg[:-1])
    if len(msg) > 1 and int(msg[-2]) <= 2 and int(msg[-1]) <= 6:
      temp += numways(msg[:-2])
    return temp


def dp_numways(msg):
  dp = [0 for _ in msg + " "]
  dp[0] = 1
  dp[1] = 1

  for n in range(2, len(msg) + 1):
    i = n - 1
    dp[n] = dp[n - 1]
    if n >= 2 and int(msg[i - 2]) <= 2 and int(msg[i - 1]) <= 6:
      dp[n] += dp[n - 2]
  return dp[len(msg)]


def dp_numways_optimized(msg):
  dp2 = 1
  dp1 = 1

  for n in range(2, len(msg) + 1):
    i = n - 1
    dp = dp1
    if n >= 2 and int(msg[i - 2]) <= 2 and int(msg[i - 1]) <= 6:
      dp += dp2
    dp2 = dp1
    dp1 = dp

  return dp1


s = "1111"
print(numways(s))
print(dp_numways(s))
print(dp_numways_optimized(s))