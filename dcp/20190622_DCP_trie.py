# This problem was asked by Twitter.

# # PROBLEM
# Implement an autocomplete system.
# That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
# For example,
# given the query string "de" and the set of strings ["dog", "deer", "deal"],
# return ["deer", "deal"].

# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

# # SOLUTION
# we're gonna need a Trieeeeeee


class Trie:

  def __init__(self):
    self.children = {}
    self.is_word = False  # ???

  def add(self, str):
    curr = self
    i = 0
    while i < len(str):
      if str[i] in curr.children:
        curr = curr.children[str[i]]
        i += 1
      else:
        break

    while i < len(str):
      curr.children[str[i]] = Trie()  # make a new node
      curr = curr.children[str[i]]  # go to new node
      i += 1

    curr.is_word = True
    # return

    # strings = ["dog", "deer", "deal"]
    # Trie would look like this:
    #                 d
    #               /   \
    #              o     e
    #             /     / \
    #            g     e   a
    #                 /   /
    #                r    l

  def trie2words(self, prefix):
    if self.is_word == True:
      return [prefix]
    else:
      words = []

      for chr in self.children:
        suffixes = self.children[chr].trie2words(prefix + chr)
        words += [x for x in suffixes]
      return words

  def find_by_prefix(self, str):
    curr = self
    i = 0
    while i < len(str):
      if str[i] in curr.children:
        curr = curr.children[str[i]]
        i += 1
      else:
        return None

    return curr.trie2words(str)


def autocomplete(strings, queries):
  trie = Trie()
  for s in strings:
    trie.add(s)

  sols = []
  for q in queries:
    sols += [trie.find_by_prefix(q)]
  return sols


strings = [
    "dog", "deer", "deal", "dead", "don", "deed", "dean", "dealt", "dereck"
]
queries = ["de", "dea", "do"]
sols = autocomplete(strings, queries)
for q, s in zip(queries, sols):
  print(q, ":", s)