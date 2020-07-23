# This problem was asked by Jane Street.
# # PROBLEM
# Suppose you are given a table of currency exchange rates, represented as a 2D array.
# Determine whether there is a possible arbitrage: that is, whether there is some sequence
# of trades you can make, starting with some amount A of any currency, so that you can end up
# with some amount greater than A of that currency.
# There are no transaction costs and you can trade fractional quantities.

# # SOLUTION
# kind of looks like a graph search

# Ok, this can totally be done via graph search.
# with currencies being nodes in the graph
# and exchange rates being weights of the edges
# but instead of path length being the sum of the edge weights
# the path length is the PRODUCT of the edge weights.
# And the problem we are essentially solving is:
# All Pairs Shortest Paths, or in this case, longest paths.
# And that can be done with a simple modification to Floyd's algorithm.


def floyd(w):
  n = len(w)

  d = [[x for x in line] for line in w]

  # hygienic
  try:
    for i in range(n):
      d[i][i] = 1  # since 1 is neutral element in multiplication
  except IndexError as e:
    print(e)
    print("Exchange rate matrix is not complete.")

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if d[i][j] < d[i][k] * d[k][j]:
          d[i][j] = d[i][k] * d[k][j]

  [print(line) for line in d]
  for i in range(n):
    if d[i][i] > 1:
      print(True)
      return True

  return False


w = [[1, 0.5, 0.5], [1.9, 1, 1], [2, 1, 1]]

assert floyd(w) == True