# This problem was asked by Google.

# # PROBLEM
# The area of a circle is defined as πr^2.
# Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.

# # SOLUTION
# We look at the square with the sides of length 2r.
# We take the coordinate system where the origin is matching the center of the square
# So that the square vertices are:
# A = (r, r)
# B = (-r, r)
# C = (-r, -r)
# D = (r, -r)
# We sample N different points inside the square.
# I.e. we sample N pairs (x,y) of numbers between -r and r
# Area of the inscribed circle is A = πr^2
# We estimate the area by estimating counting all the points which are inside the circle, i.e.
# All the points for which:
# x^2 + y^2 <= r^2 holds true
# Let M be the number of those points.
# Then,
# M/N = CircleArea/SquareArea = πr^2/(2r)^2 = π/4
# Now, for Monte Carlo methods,
# it can be derived that error estimation is of the form
# error_estimate = sigma(X)/sqrt(N),
# where sigma(X) is standard deviation of the random sample X
# Since sigma(X) = sigma(X, N) = sqrt(1/N * sum_squared_differences(X-mean))
# error_estimate = 1/N * sqrt(sum_squared_differences(X-mean))
# now since we need 3 decimal places precision
# error_estimate needs to be <= 0.001
# 1/N * sqrt(sum_squared_differences(X-mean)) <= 0.001
# 1000*sqrt(sum_squared_differences(X-mean)) <= N

# TODO FIX
# https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-90-computational-methods-in-aerospace-engineering-spring-2014/probabilistic-methods-and-optimization/review-of-probability-and-statistics/
import random
import math
import statistics


def get_sample(N, r):
  X = [random.random() * 2 * r - r for _ in range(N)]
  Y = [random.random() * 2 * r - r for _ in range(N)]
  P = [(x, y) for (x, y) in zip(X, Y)]

  return P


def error_estimate(P):
  N = len(P)
  r = 1
  P = get_sample(N, r)
  mean = (1 / N * (sum([x[0] for x in P])), 1 / N * (sum([y[1] for y in P])))
  differences = [(p[0] - mean[0], p[1] - mean[1]) for p in P]
  squared_differences = [x[0]**2 + x[1]**2 for x in differences]
  sum_sqd = math.sqrt(sum(squared_differences))
  return 1 / N * sum_sqd


def error_estimate2(P):
  N = len(P)
  r = 1
  P = get_sample(N, r)
  sigma = statistics.stdev(P)
  # TODO fix
  err = sigma / math.sqrt(N)
  return err


def pi_calc(precission):
  N = 16
  r = 1
  P = get_sample(N, r)
  err = error_estimate(P)
  # err = error_estimate2(P)
  N = math.ceil(N * err / precission)

  while err > precission:
    P = get_sample(N, r)
    err = error_estimate(P)
    # err = error_estimate2(P)
    N = math.ceil(N * err / precission)

  M = 0
  for p in P:
    if p[0]**2 + p[1]**2 <= r**2:
      M += 1
  pie = 4 * M / N
  return pie


precission = 0.001
print(pi_calc(precission))
