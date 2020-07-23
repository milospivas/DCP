# This problem was asked by Stripe.

# PROBLEM
# Given an array of integers,
# find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

# SOLUTION
# The array a is given of length  N == N
# Firstly, we can say that all integers smaller than 1 can't be a solution by definition.
# Secondly, also by definition, all integers "x" greater than N + 1 can't be a solution.
# If they could, that would mean that there were N+1 distinct integers != "x" in the array of length N which is a contradiction.
# The case when N+1 is the solution is when all integeres from 1 to N are present in the array.

# So only meaningful integers are those that satisfy: 1 <= x <= N

# In O(N) time, we can match each meaningful integer x with the position x-1 in the array a.
# What is left will be array where each element a[i] is either i+1 or None.
# The first None element, at the index k corresponds with the fact that k+1 is the smallest missing integer.
# If there are no None elements, the smallest missing integer is N+1.

# Example:
# The given array
# a = [3, 4, -1, 14, 15, 1, 2, 0, 7, 12, 8, 9, 20, 3, 11, 6, 5]

#      v     -1 is going out
# a = [_, 4,  3, 14, 15, 1, 2, 0, 7, 12, 8, 9, 20, 3, 11, 6, 5]

#         v      14 is going out
# a = [_, _,  3,  4, 15, 1, 2, 0, 7, 12, 8, 9, 20, 3, 11, 6, 5]

#             v
# a = [_, _,  3,  4, 15, 1, 2, 0, 7, 12, 8, 9, 20, 3, 11, 6, 5]

#                 v
# a = [_, _,  3,  4, 15, 1, 2, 0, 7, 12, 8, 9, 20, 3, 11, 6, 5]

#                     v 15 is going out
# a = [_, _,  3,  4, __, 1, 2, 0, 7, 12, 8, 9, 20, 3, 11, 6, 5]

#                        v a[0] = 1
# a = [1, _,  3,  4, __, _, 2, 0, 7, 12, 8, 9, 20, 3, 11, 6, 5]

#                           v a[1] = 2
# a = [1, 2,  3,  4, __, _, _, 0, 7, 12, 8, 9, 20, 3, 11, 6, 5]

#                              v 0 is going out
# a = [1, 2,  3,  4, __, _, _, 0, 7, 12, 8, 9, 20, 3, 11, 6, 5]
# . . .

# values "_" will be None values in the actual program


def find_smallest_missing_int(a):
  N = len(a)
  for i in range(N):
    # remember the current index and value as the old ones
    old_i = i
    old = a[old_i]

    # while old value isn't marked as None
    # and old value is meaningful
    # and old value isn't already matched with the appropriate position in the array
    while old is not None and (old <= N and old >= 1) and a[old - 1] != old:
      a[old_i] = None  # remove the value at the old index from array

      new_i = old - 1  # get the new position

      new = a[new_i]  # swap old value and new value
      a[new_i] = old
      old = new

      old_i = new_i  # new position is now old position

    # if the old value isn't None and isn't meaningful, remove it from the array
    if old is not None and not (old <= N and old >= 1):
      a[old_i] = None

  print(a)

  for i in range(N):
    if a[i] == None:
      return i + 1
      # break
  return N + 1


# -----------------------------------------------------------------------
a = [3, 4, -1, 14, 15, 1, 2, 0, 7, 12, 8, 9, 20, 3, 11, 6, 5]
# a = [-1, -2, -3]

# print(sorted(a))
sol = find_smallest_missing_int(a)
print(sol)