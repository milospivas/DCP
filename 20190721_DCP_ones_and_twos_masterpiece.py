# This is one of the most beautiful problem solutions ever.

# PROBLEM
# Given an array where each element appears 3 times except one which appears only once,
# in O(N) time and O(1) space, find that one special element.

# SOLUTION
# This is a variation to the problem where all elements appear 2 times, except for one special element.
# The solution is to XOR the whole array.
# x^y = y^x # comutative
# x^0 = x   # 0 is a neutral element
# x^x = 0   # reflexive?

# So we need a logical function FOO where:
# x^y = y^x
# x^0 = x
# x^x^x = 0


# Addition mod 3 would work for numbers smaller then 3
# So we need to calculate it bitwise.
#
# I am not yet 100% sure how exactly this works, but here's the code:
def special(lst):
  ones = 0
  twos = 0
  for x in lst:
    twos |= ones & x
    ones ^= x
    not_threes = ~(ones & twos)
    ones &= not_threes
    twos &= not_threes
  return ones
