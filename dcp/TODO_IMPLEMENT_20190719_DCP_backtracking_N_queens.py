# This problem was asked by Microsoft.

# # PROBLEM
# You have an N by N board.
# Write a function that, given N,
# returns the number of possible arrangements of the board
# where N queens can be placed on the board without threatening each other,
# i.e. no two queens share the same row, column, or diagonal.

# # SOLUTION
# 1. It's going to be a backtracking solution
# 2. Attacking conditions of q(i1, j1) and q(i2, j2):
#   i1 == i2        # same row
#   j1 == j2        # same column
#   i1 - j1 == i2 - j2    # parallel to the main diagonal
#   i1 + j1 == i2 + j2    # parallel to the antidiagonal
# 3. 1