# Asked by:
# PROBLEM
# Given N time intervals of lectures as (start, end)
# Return min number of classrooms needed to hold them all

# SOLUTION
# Let's assume that lectures are all happening inside one 24h day.
# I would first ask what's the time format for start and end values.
# Let's assume they are objects with .H and .M fields

# We can use a relatively small 24x60 matrix T to mark the number of lectures that need to be held at every minute.

# So, firstly we fill T with zeroes.
# Then we add 1 inside every time interval.
# We can do this in one pass.
# For every interval i, we mark the starting minute with T[i.start.H][i.start.M] += 1
# an take 5 minutes after the end of the lecture with:
# finish = add_minutes(i.end, 5)
# And mark it with: T[finish.H][finish.M] -= 1
# Then we go over the matrix linearly, starting from T[0][1], adding value of the previous element to the current one
# We can also use a linearized matrix so instead of T[i][j] we would write T[i*60 + j]

# So the solution is in O(24*60) + O(N) = O(N) time and O(24*60) = O(1) space


class time:

  def __init__(self, H, M):
    if H > 23 or M > 59:
      print("Error! Wrong time format")
      return None

    self.H = H
    self.M = M

  def print(self, end="\n"):
    if self.H < 10:
      print("0", end="")
    print(self.H, end=":")

    if self.M < 10:
      print("0", end="")
    print(self.M, end=end)


def add_minutes(t_old, mins):
  t = time(t_old.H, t_old.M)
  t.M += mins
  if t.M > 59:
    t.M %= 60
    t.H += mins // 60
    if t.H > 23:
      t.H %= 24
  return t


class time_interval:

  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print(self, end="\n"):
    self.start.print(end="")
    print(" - ", end="")
    self.end.print(end=end)


def num_classrooms(lectures):
  T = [0 for _ in range(24 * 60)]

  for i in lectures:
    start_idx = i.start.H * 60 + i.start.M

    finish = add_minutes(i.end, 5)
    finish_idx = finish.H * 60 + finish.M

    T[start_idx] += 1
    if finish_idx < 24 * 60:
      T[finish_idx] -= 1

  for i in range(1, 24 * 60):
    T[i] += T[i - 1]

  # for H in range(24):
  #   for M in range(60):
  #     print(T[H * 60 + M], end=" ")
  #   print("H =", H)
  return max(T)


# start = time(8, 30)
# end = time(10, 00)
# i = time_interval(start, end)
# finish = add_minutes(i.end, 5)
# start.print()
# end.print()
# i.print()
# finish.print()

i1 = time_interval(time(9, 00), time(12, 00))
i2 = time_interval(time(10, 00), time(13, 00))
i3 = time_interval(time(12, 30), time(14, 00))
i4 = time_interval(time(8, 30), time(14, 00))

lectures = [i1, i2, i3, i4]
num = num_classrooms(lectures)
print(num)