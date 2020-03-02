# This problem was asked by Facebook.
# # PROBLEM
# You are given an array of non-negative integers that represents
# a two-dimensional elevation map where each element is unit-width wall and the integer is the height.
# Suppose it will rain and all spots between two walls get filled up.
#
# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index,
# 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left),
# so we can trap 8 units of water.

# # SOLUTION

# In O(N) space
# Go from one side and keep current maximum height, curr_max
# hold[i] = curr_max - height[i]
# Then go from the other side to correct it, except now:
# hold[i] = min(hold[i], curr_max - height[i])

# Modification for an in-place version, so O(1) space:
# Again, go from one side and keep the current maximum height, curr_max,
# but now:
# height[i] = height[i] - curr_max
# And the same things in the other direction.
# Now the peaks and sides will be at height 0, and everything else underwater.


def water_trapped(height: list):
  if len(height) == 0:
    return 0

  curr_max = height[0]
  for i in range(len(height)):
    if height[i] > curr_max:
      curr_max = height[i]

    height[i] -= curr_max

  curr_max = height[-1]
  for i in range(len(height) - 1, -1, -1):
    if height[i] > curr_max:
      curr_max = height[i]

    height[i] -= curr_max

  return -sum(height)


height = [5, 4, 3, 2, 3, 4, 3, 2, 1]
print(water_trapped(height))
height = [5, 4, 3, 2, 3, 4, 5, 6, 1]
print(water_trapped(height))
