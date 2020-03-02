# Given a list of numbers and a number k,
# return whether any two numbers from the list add up to k.

# For example,
# given [10, 15, 3, 7] and k of 17,
# return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


def does_it_add_up(L, k):
  count = set()

  for x in L:
    count.add(x)
    if (k - x) in count:
      return True

  return False


L = 3, 15, 10, 6
k = 17
print(does_it_add_up(L, k))
