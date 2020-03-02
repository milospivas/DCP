# This problem was asked by Twitter.

# # PROBLEM

# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
# •	record(order_id): adds the order_id to the log
# •	get_last(i): gets the i-th last element from the log. i is guaranteed to be smaller than or equal to N.

# You should be as efficient with time and space as possible.


# # SOLUTION
class orders:

  def __init__(self, N):
    self.n = N
    self.size = 0
    self.offset = 0
    self.buffer = [None for _ in range(N)]

  def record(self, id):
    self.buffer[self.offset] = id
    self.offset += 1
    self.offset %= self.n
    if self.size < self.n:
      self.size += 1

  def get_last(self, i):
    if i > self.size or i < 1:
      return None
    else:
      return self.buffer[(self.offset - i) % self.n]


N = 4
o = orders(N)
ords = [1, 2, 3, 4, 5, 6]

[o.record(x) for x in ords]
[print(o.get_last(i)) for i in range(1, N + 1)]
