# This problem was asked by Google.

# # PROBLEM
# Suppose we represent our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2.
# subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1.
# subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

# We are interested in finding the longest (number of characters) absolute path to a file within our file system.

# For example, in the second example above,
# the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

# Given a string representing the file system in the above format,
# return the length of the longest absolute path to a file in the abstracted file system.
# If there is no file in the system, return 0.
# Note:
# The name of a file contains at least a period and an extension.
# The name of a directory or sub-directory will not contain a period.

# # SOLUTION

s = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

# s = "dir\n
# \t	subdir1\n
# \t	\t	file1.ext\n
# \t	\t	subsubdir1\n
# \t	subdir2\n
# \t	\t	subsubdir2\n
# \t	\t	\t	file2.ext"


class Node:

  def __init__(self, start=0, parent=None, level=None, path_len=0):
    self.start = start
    self.end = None
    self.path_len = path_len
    self.len = 0
    self.children = []
    self.parent = parent
    self.level = level

  # def set_end(self, end, s):
  def set_end(self, end):
    self.end = end
    self.len = self.end - self.start
    # self.string = s[self.start:self.end]


root = Node(0, None, 0)

max = 0
max_node = None
aux = root
prev_lvl = 0
curr_lvl = 0
is_file = False

for i in range(len(s)):
  if s[i] == ".":
    is_file = True

  if i == len(s) - 1 or s[i + 1] == "\n":
    # aux.set_end(i + 1, s)
    aux.set_end(i + 1)
    aux.path_len += aux.len + 1
    # aux.level = curr_lvl
    prev_lvl = curr_lvl
    curr_lvl = 0
    if is_file and aux.path_len - 1 > max:
      max = aux.path_len - 1
      max_node = aux
  elif s[i] == "\t":
    curr_lvl += 1
  elif s[i - 1] == "\t":
    for j in range(prev_lvl - curr_lvl + 1):
      aux = aux.parent
    new = Node(i, aux, curr_lvl, aux.path_len)
    aux.children += [new]
    aux = new

print(max)
aux = max_node
max_path = s[aux.start:aux.end]
aux = aux.parent
while aux is not None:
  max_path = s[aux.start:aux.end] + "/" + max_path
  aux = aux.parent

print(max_path)