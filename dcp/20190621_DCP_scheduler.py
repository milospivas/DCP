# This problem was asked by Apple.

# # PROBLEM
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

# # SOLUTION

from time import sleep


def job():
  print("I'm working here!")


def schedule_after_n(f, n):
  sleep(n / 1000)
  f()


f = job
n = 10000
schedule_after_n(job, n)
