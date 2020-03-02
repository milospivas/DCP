# This problem was asked by Microsoft.
# # PROBLEM
# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
# Recall that the median of an even-numbered list is the average of the two middle numbers.
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

# # SOLUTION
# Have a max-heap and a min-heap.
# Iterate through the list.
# Keep a middle element, and smaller elements in the max-heap, and bigger elements in the min-heap,
# so that the heaps are the same sizes or at 1 difference at most.
# The running median is either the middle element, if the heaps are the same size,
# Or the average of the middle and root.val of the bigger heap.


class Heap:
  """ Generic binary heap class with static and class methods that provide basic heap ops:
  sift up/down, heapify, insert, extract, and sort.
  
  All functions, including sort are in-place medianing they cost O(1) memory.

  You can pass a reference to a custom compare funciton "cmp" for comparing composite data structures,
  or pass a boolean flag "is_max_heap" to chose between a max-heap and a min-heap.

  The cmp argument specifies the function for comparing the list elements:
    The given function needs to take 3 arguments in format: (a:list, i:int, j:int),    
    The function should return:
      -1  :   for   a[i] < a[j],
      0   :   for   a[i] == a[j],
      1   :   for   a[i] > a[j].
    This maintains a max-heap.

  If no compare function is given is_max_heap flag can be used to specify
  whether the heap is max heap or min heap.
  """

  @staticmethod
  def swap(a: list, i: int, j: int) -> None:
    """ swaps i-th and j-th element in list a """
    try:
      x = a[i]
      a[i] = a[j]
      a[j] = x
    except IndexError as e:
      print(e)

  @staticmethod
  def cmp_max(a: list, i: int, j: int):
    """ Compares i-th and j-th element in list a. 
    Return values for different scenarios are:
    -1  :   for   a[i] < a[j],
    0   :   for   a[i] == a[j],
    1   :   for   a[i] > a[j].
    This cmp method is compatible with max-heap operations.
   """
    try:
      if a[i] < a[j]:
        return -1
      if a[i] == a[j]:
        return 0
      if a[i] > a[j]:
        return 1

    except (IndexError, KeyError) as e:
      print(e)
      return None
    pass

  @staticmethod
  def cmp_min(a: list, i: int, j: int):
    """ Compares i-th and j-th element in list a. 
    Return values for different scenarios are:
    -1  :   for   a[i] < a[j],
    0   :   for   a[i] == a[j],
    1   :   for   a[i] > a[j].
    This cmp method is compatible with min-heap operations.
   """
    try:
      if a[i] < a[j]:
        return 1
      if a[i] == a[j]:
        return 0
      if a[i] > a[j]:
        return -1

    except (IndexError, KeyError) as e:
      print(e)
      return None
    pass

  @classmethod
  def sift_down(cls: "this class",
                a: list,
                n: int,
                node: int,
                cmp: callable = None,
                is_max_heap: bool = True) -> None:
    """ Sift down the heapified list a, of length n,
    starting from node as the root and going down.
    """
    if n <= 0:
      pass

    if cmp is None:
      if is_max_heap:
        cmp = cls.cmp_max
      else:
        cmp = cls.cmp_min

    while 2 * node + 1 < n:
      left = 2 * node + 1
      right = 2 * node + 2

      largest = node
      if left < n and cmp(a, left, largest) == 1:
        largest = left

      if right < n and cmp(a, right, largest) == 1:
        largest = right

      if node != largest:
        cls.swap(a, node, largest)
        node = largest
      else:
        break

  @classmethod
  def heapify(cls: "this class",
              a: list,
              n: int,
              cmp: callable = None,
              is_max_heap: bool = True) -> None:
    """ Heapify the list a, of length n.
    """

    start = n // 2
    for i in range(start, -1, -1):
      cls.sift_down(a, n, i, cmp, is_max_heap)

  @classmethod
  def sort(cls: "this class",
           a: list,
           n: int,
           cmp: callable = None,
           is_max_heap: bool = True) -> None:
    """ Sorts the list a, of length n.    
    """
    cls.heapify(a, n, cmp, is_max_heap)

    for i in range(n - 1, -1, -1):
      cls.swap(a, i, 0)
      cls.sift_down(a, i, 0, cmp, is_max_heap)

  @classmethod
  def extract(cls: "this class",
              a: list,
              n: int,
              cmp: callable = None,
              is_max_heap: bool = True) -> any:
    """ Extract the root of the heap. """
    if n <= 0:
      raise IndexError("Can't perform extract on an empty heap.")

    val = a[0]
    cls.swap(a, 0, n - 1)
    cls.sift_down(a, n - 1, 0, cmp, is_max_heap)
    del (a[n - 1])
    return val

  @classmethod
  def sift_up(cls: "this class",
              a: list,
              n: int,
              node: int,
              cmp: callable = None,
              is_max_heap: bool = True) -> None:
    """ Sift an element up the heap a, of length n. """
    if n <= 0:
      pass

    if node >= n:
      raise IndexError("Element index out of heap range")

    if cmp is None:
      if is_max_heap:
        cmp = cls.cmp_max
      else:
        cmp = cls.cmp_min

    while node // 2 >= 0:
      parent = node // 2
      if parent >= 0 and cmp(a, node, parent) == 1:
        cls.swap(a, parent, node)
        node = parent
      else:
        break
    pass

  @classmethod
  def insert(cls: "this class",
             a: list,
             n: int,
             val: any,
             cmp: callable = None,
             is_max_heap: bool = True) -> int:
    """ Insert a value into the heap a, of length n.
    """
    if n < 0:
      raise IndexError("Length of the heap is negative.")

    a += [val]
    n += 1
    Heap.sift_up(a, n, n - 1, cmp, is_max_heap)

    return n


class GeneralHeap:
  """ General heap class that can be either min-heap or max-heap.
  The "is_max_heap" boolean flag is passed to the constructor to determine the type.
  """

  def __init__(self, is_max_heap):
    self._is_max_heap = is_max_heap
    self._array = []
    self._n = 0

  def insert(self, val: int) -> None:
    self._n = Heap.insert(
        self._array, self._n, val, is_max_heap=self._is_max_heap)
    pass

  def extract(self) -> any:
    try:
      val = Heap.extract(self._array, self._n, is_max_heap=self._is_max_heap)
      self._n -= 1
      return val
    except IndexError as e:
      print(e)
      return None

  def peek(self) -> any:
    try:
      return (self._array[0])
    except IndexError as e:
      print(e)
      return None

  def __len__(self) -> int:
    return self._n

  def __str__(self) -> str:
    return str(self._array)

  def __repr__(self) -> str:
    return str(self._array)


def running_median(stream: list) -> list:
  h_min = GeneralHeap(False)
  h_max = GeneralHeap(True)
  middle = stream[0]

  medians = [middle]

  # print(middle)

  for i in range(1, len(stream)):
    x = stream[i]
    if x <= middle:
      h_max.insert(x)
    else:
      h_min.insert(x)

    if len(h_max) - len(h_min) < -1:
      h_max.insert(middle)
      middle = h_min.extract()

    if len(h_max) - len(h_min) > 1:
      h_min.insert(middle)
      middle = h_max.extract()

    if len(h_max) - len(h_min) == 1:
      median = (h_max.peek() + middle) / 2
    elif len(h_max) - len(h_min) == 0:
      median = middle
    else:
      median = (middle + h_min.peek()) / 2

    medians += [median]
    # print("for elements:")
    # print("\t", [middle], h_max, "len =", len(h_max), end="")
    # print("    <------" if len(h_max) > len(h_min) else "")
    # print("\t", [middle], h_min, "len =", len(h_min), end="")
    # print("    <------" if len(h_max) < len(h_min) else "")
    # print("\t", "=> median: {:5s}".format(str(median)))

  return medians


# stream = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stream = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]

# medians = running_median(stream)
# print(stream)
# print(medians)

# help(Heap)


class QuickHeap:

  @staticmethod
  def swap(a, i, j):
    try:
      x = a[i]
      a[i] = a[j]
      a[j] = x
    except IndexError as e:
      print(e)

  @staticmethod
  def cmp_max(a, i, j):
    try:
      if a[i] < a[j]:
        return -1
      if a[i] == a[j]:
        return 0
      if a[i] > a[j]:
        return 1
    except IndexError as e:
      print(e)
      return None

  @staticmethod
  def cmp_min(a, i, j):
    try:
      if a[i] < a[j]:
        return 1
      if a[i] == a[j]:
        return 0
      if a[i] > a[j]:
        return -1
    except IndexError as e:
      print(e)
      return None

  @classmethod
  def sift_down(cls, a, idx, is_max_heap):
    """ """  # TODO write docstring
    n = len(a)
    if n <= 0:
      raise IndexError("Heap is empty")

    if is_max_heap:
      cmp = cls.cmp_max
    else:
      cmp = cls.cmp_min

    i = idx
    while 2 * i + 1 < n:
      left = 2 * i + 1
      right = left + 1

      largest = i
      if left < n and cmp(a, left, largest) == 1:
        largest = left

      if right < n and cmp(a, right, largest) == 1:
        largest = right

      if largest != i:
        cls.swap(a, largest, i)
        i = largest
      else:
        break

  # @classmethod
  # def heapify(cls, a, is_max_heap):
  #   """ """  # TODO write docstring
  #   n = len(a)
  #   if n <= 0:
  #     pass

  #   start = n//2
  #   for idx in range(start, -1, -1):
  #     cls.sift_down(a, idx, is_max_heap)

  @classmethod
  def sift_up(cls, a, idx, is_max_heap):
    """ """  # TODO write docstring
    n = len(a)
    if n <= 0:
      raise IndexError("Can't perform sift_up on an empty heap")

    if is_max_heap:
      cmp = cls.cmp_max
    else:
      cmp = cls.cmp_min

    i = idx

    if i >= n:
      raise IndexError()
    if i < 0:  # support for pythonic negative indices
      i += n
    if i < 0:
      raise IndexError()

    while i // 2 >= 0:
      p = i // 2

      if p >= 0 and cmp(a, i, p) == 1:
        cls.swap(a, i, p)
        i = p
      else:
        break

  @classmethod
  def insert(cls, a, val, is_max_heap):
    """ """  # TODO write docstring

    a += [val]

    try:
      cls.sift_up(a, -1, is_max_heap)
    except IndexError as e:
      print(e)

    pass

  @classmethod
  def extract(cls, a, is_max_heap):
    """ """  # TODO write docstring
    n = len(a)
    if n <= 0:
      raise IndexError("Can't perform extract on an empty heap.")

    val = a[0]
    cls.swap(a, 0, -1)
    del a[-1]
    cls.sift_down(a, 0, is_max_heap)
    return val


def quick_running_median(stream):
  h_max = []
  h_min = []

  middle = stream[0]
  medians = [middle]
  print(medians)
  for i in range(1, len(stream)):
    x = stream[i]
    if x <= middle:
      QuickHeap.insert(h_max, x, True)
    else:
      QuickHeap.insert(h_min, x, False)

    if len(h_max) - len(h_min) == 2:
      QuickHeap.insert(h_min, middle, False)
      middle = QuickHeap.extract(h_max, True)
    elif len(h_max) - len(h_min) == -2:
      QuickHeap.insert(h_max, middle, True)
      middle = QuickHeap.extract(h_min, False)

    if len(h_max) - len(h_min) == 1:
      median = (h_max[0] + middle) / 2
    if len(h_max) - len(h_min) == 0:
      median = middle
    if len(h_max) - len(h_min) == -1:
      median = (middle + h_min[0]) / 2

    medians += [median]
    print("for elements:")
    print("\t", [middle], h_max, "len =", len(h_max), end="")
    print("    <------" if len(h_max) > len(h_min) else "")
    print("\t", [middle], h_min, "len =", len(h_min), end="")
    print("    <------" if len(h_max) < len(h_min) else "")
    print("\t", "=> median: {:5s}".format(str(median)))

  return medians


medians = quick_running_median(stream)

# print(stream)
# print(medians)
# print(" ".join([format(x, " 3d") for x in a]))
# print(" ".join([format(x, "03d") for x in range(n)]))
