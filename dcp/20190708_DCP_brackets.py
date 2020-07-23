# This problem was asked by Facebook.
# # PROBLEM
# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.

# # SOLUTION
# Use a stack
# go through the characters of the string
#   if it's an open bracket -> push it on the stack
#   else pop the stack until the matching closing bracket is poped
#     if the stack is empty and the matching closing bracket isn't found:
#       return False
#   if at the end of the string the stack ISN'T empty:
#     retrun False
#   else:
#     return True


class Node:

  def __init__(self, val=None, prev=None):
    self.val = val
    self.prev = prev


class Stack:

  top = None

  def push(self, val):
    node = Node(val, self.top)
    self.top = node

  def pop(self):
    if self.top is not None:
      val = self.top.val
      self.top = self.top.prev
      return val
    else:
      print("Error. Stack is empty.")
      return None


def are_regular(s):
  # keys are closed brackets
  # items are open brackets
  brackets_map = {")": "(", "]": "[", "}": "{"}
  S = Stack()
  for b in s:
    # if b is not a closed bracket
    if b not in brackets_map:
      S.push(b)
    else:
      x = S.pop()
      while x != brackets_map[b]:
        if x is None:
          return False

        x = S.pop()

  if S.top is not None:
    return False
  else:
    return True


s = "()"
print(are_regular(s), s)
s = "[]"
print(are_regular(s), s)
s = "{}"
print(are_regular(s), s)

s = "[{]}"
print(are_regular(s), s)

s = "{{{}"
print(are_regular(s), s)

s = "([])[]({})"
print(are_regular(s), s)