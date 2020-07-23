# This problem was asked by Amazon.

# # PROBLEM
# Given an integer k and a string s,
# find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

# # SOLUTION
# 1. The task is asking for a substring, not a subsequence.
# Substrings must be contiguous, subsequences needn't be.
# 2. It looks like a DP problem but it isn't really (or doesn't have to be)
# The solution takes O(N) time and O(N) memory


def max_ksub(s, k):
  # edge cases
  if k == 0 or s == "":
    return ""
  if k >= len(s):
    return s

  max_start = 0  # memorized starting idx of max substring
  max_len = 0  # memorized length of max substring
  curr_start = 0  # memorized startind idx of current substring that satisfies max k-distinct condition
  curr_len = 0  # memorized current substring length

  # dictionary that has characters that appear in current substring for keys
  # the entry value is the index in current substring where it last occured
  chars = {}

  # We go through the string in one pass, adding characters to current substring until we can
  # And when we can't, we delete the first character from the substring,
  # and all the ones until the last occurence of that characer in the substring (that is memorized in the chars dict.)
  # In worst case, we go through the string twice, so time complexity is O(N)

  # For example:
  # s = "asdasdfsdfsdf"
  # k = 3
  # idx  0123456789...
  # when i = 3
  # curr_start is = 0, and curr_len = 3
  # So the current substring is "asd"
  # chars = {"a":0, "s":1, "d":2}
  # then we add the second "a"
  # and curr_len is now 4, and chars = {"a":3, "s":1, "d":2}
  # and current substring is now "asda"
  #
  # When i = 6
  # curr_start is still 0, curr_len = 6
  # So the current substring is "asdasd"
  # chars = {"a":3, "s":4, "d":5}
  # When we add f,
  # we remove "asda" from the substring, i.e. we remove all characters from range(curr_start, chars[curr_start]+1) == range(0, 4))
  # And now curr_start = chars[curr_start]+1 = 4,
  # curr_len = i - curr_start + 1 = 3
  # So the current substring is "sdf"
  # and chars = {"s":4, "d":5, "f":6}
  #
  # We update the max values in every iteration, and finally get that the max substring is "sdfsdfsdf"
  for i in range(len(s)):
    curr_len += 1
    if (s[i] not in chars and len(chars) == k):
      new_start = chars[s[curr_start]] + 1
      for j in range(curr_start, new_start):
        chars.pop(s[j], "None")
      curr_start = new_start
      curr_len = i - curr_start + 1

    chars[s[i]] = i
    if curr_len > max_len:
      max_len = curr_len
      max_start = curr_start
  return s[max_start:max_start + max_len]


s = "absba"
k = 2
print(s, k, max_ksub(s, k))
s = "asdasdfsdfsdf"
k = 3
print(s, k, max_ksub(s, k))
s = "sababsdabababab"
k = 3
print(s, k, max_ksub(s, k))
s = ""
print(s, k, max_ksub(s, k))
s = "asdfasdf"
k = 0
print(s, k, max_ksub(s, k))
