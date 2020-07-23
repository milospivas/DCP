# This problem was asked by Microsoft.
# PROBLEM
# Given a dictionary of words and a string made up of those words (no spaces),
# return the original sentence in a list.

# If there is more than one possible reconstruction,
# return any of them.

# If there is no possible reconstruction,
# then return null.

# For example,
# given the set of words "quick", "brown", "the", "fox",
# and the string "thequickbrownfox",
# you should return ["the", "quick", "brown", "fox"].

# Given the set of words "bed", "bath", "bedbath", "and", "beyond",
# and the string "bedbathandbeyond",
# return either ["bed", "bath", "and", "beyond] or ["bedbath", "and", "beyond"].

# SOLUTION
# 1. build a Trie from the given dictionary


class TrieNode:

  def __init__(self):
    self.is_word: bool = False
    self.children: dict = {}

  def insert_word(self, word: str) -> None:
    curr = self  # This is unnecessary in Python because self is a local variable,
    # but I do believe this is good, hygienic practice, and it costs almost nothing.

    for c in word:
      if not c in curr.children:
        curr.children[c] = TrieNode()
      curr = curr.children[c]

    curr.is_word = True

  def find_word(self, word: str) -> bool:
    curr = self  # This is unnecessary in Python because self is a local variable,
    # but I do believe this is good, hygienic practice, and it costs almost nothing.

    for c in word:
      if not c in curr.children:
        return False
      curr = curr.children[c]

    if curr.is_word:
      return True
    else:
      return False

  def words(self) -> list:
    chars = list(self.children.keys())
    lst = []
    if self.is_word:
      lst += [""]

    for c in chars:
      suffixes = self.children[c].words()
      if suffixes is not None:
        lst += [c + suff for suff in suffixes]

    if lst != []:
      return lst
    else:
      return None

  # Tail recursion variant
  def words_tr(self, prefix: str = "") -> list:
    chars = list(self.children.keys())
    lst = []
    if self.is_word:
      lst += [prefix]
      # print(prefix) # or do something else since the prefix is now the full word

    for c in chars:
      prefixes = self.children[c].words_tr(prefix + c)
      if prefixes is not None:
        lst += [prefixes]

    if lst != []:
      return lst
    else:
      return None


# 2. DP through the string and the Trie somehow
# dp[j] = i means that s[i:j+1] is a word, AND that s[0:i] can be separated into words.
# We have a queue q, that is initialized with [0]
#
# We iterate through the string with a iterator j,
# starting from position q[i], going towards the end of the string: n-1 (where n = len(s)),
# and from the root of the Trie.
# We keep iterating while the current characters are following a word down the Trie.
# If we run into a word, we add j+1 into the q,
# so that we would later also check for words begining after the current found word: at s[j+1].
# We also mark the current word with dp[j] = q[i].
# We then reconstruct the sentence using dp-values,
# Starting from dp[n-1] until we reach dp[x] = 0.


def get_sentence(word_list: list, s: str) -> list:
  # Build a Trie from word list:
  trie_root = TrieNode()
  for word in word_list:
    trie_root.insert_word(word)

  # Init dp list, q and i
  n = len(s)
  dp = [None for _ in range(n)]
  q = [0]
  i = 0
  while i < len(q):
    # Init j and auxiliary trie pointer/iterator
    j = q[i]  # index in s, of a character, begining a word
    curr = trie_root

    # While we're inside the string and current character is following the Trie:
    while j < n and s[j] in curr.children:
      # Go down the Trie
      curr = curr.children[s[j]]
      # We progress the Trie pointer at the start of the loop due to the nature of the Trie.

      # If we've found a word:
      if curr.is_word:
        # If this isn't the end of the string:
        if j + 1 < n:
          # Add the position of the next character to q
          # because it's begining a next word and we need to find where it ends.
          q += [j + 1]
        # Mark the begining of the current word
        dp[j] = q[i]

      j += 1

    i += 1

  if dp[n - 1] is not None:  # If the last word in the string exists
    lst = []  # Init an empty list
    j = n - 1  # and a pointer j to the end of the last word
    while j >= 0:  # While the pointer is inside the string:
      i = dp[j]  # get the start of the current word
      lst += [s[i:j + 1]]  # add the word to the list
      j = i - 1  # set j to the end of the preceding word
    return list(reversed(lst))  # we went backwards, so return the reversed list
  else:
    return None  # if the last word doesn't exist, there is no way to reconstruct the full sentence
    # TODO we can still reconstruct the biggest possible part of the sentence that starts from the begining
    # by finding the first dp value that is not None


# word_list = ["word", "worth", "worthy", "woe"]
# root = TrieNode()
# for s in word_list:
#   root.insert_word(s)

# # words = root.words()
# words = root.words_tr()
# print(words)

word_list = ["quick", "brown", "the", "fox"]
string = "thequickbrownfox"
sentence = get_sentence(word_list, string)
print(sentence)

word_list = ["bed", "bath", "bedbath", "and", "beyond"]
string = "bedbathandbeyond"
sentence = get_sentence(word_list, string)
print(sentence)
