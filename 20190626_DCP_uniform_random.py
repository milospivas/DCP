# This problem was asked by Facebook.

# # PROBLEM
# Given a stream of elements too large to store in memory,
# pick a random element from the stream with uniform probability.

# # SOLUTION
# How is the stream given?
# If the number of elements is given, the problem seems too simple.
# If there are N elements, the uniform probability is 1/N.
# If the number of elements isn't given, what does uniform probability mean?
# Do we dynamically increase N by 1 with each new element, starting from 1?
# If so, then at the first element N == 1, probability for picking it would always be 1.
# And we would always pick the first element.
# Then at the 2nd element, we pick it with 1/2 probability and overwriting the first pick.
# Then for every N-th iteration,
# we pick the N-th element with 1/N probability.
# If we previously picked an element (with uniform 1/(N-1) probability),
# The probability that it remains picked after the current iteration doesn't pick the current element is:
# 1/(N-1) * (1 - 1/N = 1/(N-1) * (N - 1)/N = 1/N
# So we just pick every N-th element (for N >= 1) with 1/N probability, overwriting the previous picks.

import random
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import numpy as np


def pick_rnd_from_stream(array_stream=None):
  pick = None

  if array_stream is None:
    N = 1
    while True:
      x = input()
      if x == "exit()" or x == "exit":
        break
      if N * random.random() < 1:
        pick = x
      N += 1
  else:
    for i in range(len(array_stream)):
      N = i + 1
      if N * random.random() < 1:
        pick = array_stream[i]

  return pick


def testing(k, n):
  sample = [i for i in range(k)]
  count = [0 for i in range(k)]

  for _ in range(n):
    pick = pick_rnd_from_stream(sample)
    if pick is not None:
      count[pick] += 1
    else:
      print("Error. None picked!")

  # fig = plt.figure()
  fig, ax = plt.subplots(num=n)
  fig.suptitle("Distribution")

  spl_asarray = np.asarray(sample)
  cnt_asarray = np.asarray(count)
  plt.plot(spl_asarray, cnt_asarray, label="Is it uniform? n = " + str(n))
  ax.set_ylim(bottom=0)
  plt.legend()
  plt.show(block=False)


# for i in range(k):
#   print(i, count[i])

k = 42
N = 1000000
n = 1
while n <= N:
  testing(k, n)
  n *= 100
plt.show()