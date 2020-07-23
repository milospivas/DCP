# write your code in Python 3.6
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    ''' Returns a list representing the final states of N counters
    after operations given by A.

    Parameters
    ----------
    N : int
        The number of counters
    A : list
        List of int. Represents operations:
            if 1 <= A[i] <= N:
                represents increment(C[A[i]])
            else:
                represents set all C[A[i]] to max(C).

    Returns
    -------
    out : list
        List of int. The list of counter N values after processing
        with operations given by A.
    '''

    class Node:

        def __init__(self, val = 0, time = 0):
            self.val = val
            self.time = time

    class Counters:

        def __init__(self, N):
            self.N = N
            self.counter = {}
            self.min = 0
            self.min_time = 0
            self.max = 0

        def increment(self, i, time):
            if not i in self.counter:
                self.counter[i] = Node()

            node = self.counter[i]

            new_val = (self.min + 1) if (node.time < self.min_time) else (node.val + 1)

            node.val = new_val
            node.time = time

            if new_val > self.max:
                self.max = new_val


        def set_min_to_max(self, time):
            self.min = self.max
            self.min_time = time

        def get_all_counters(self):
            counters = [0 for _ in range(N)]

            for i in range(1, N+1):
                counters[i-1] = (self.counter[i].val) if ((i in self.counter) and (self.counter[i].time > self.min_time)) else self.min

            return counters


    def test():
        n = Node(42, 0)
        print(n.val, n.time)

        C = Counters(N)
        print(C.N, C.counter, C.max)

        i, time = 1, 1
        C.increment(i, time)
        print(C.counter, C.counter[i].val, C.counter[i].time)
        print(C.min, C.min_time, C.max)

        C.set_min_to_max(4)
        print(C.min, C.min_time, C.max)

        i, time = 2, 5
        C.increment(i, time)
        print(C.counter, C.counter[i].val, C.counter[i].time)
        print(C.min, C.min_time, C.max)

        counters = C.get_all_counters()
        print(counters)

        i, time = 2, 6
        C.increment(i, time)
        counters = C.get_all_counters()
        print(counters)

        time = 7
        C.set_min_to_max(time)
        counters = C.get_all_counters()
        print(counters)

        C = Counters(1)
        C.increment(1, 1)
        print(C.counter[1].val, C.counter[1].time)
        counters = C.get_all_counters()
        print(counters)


    C = Counters(N)
    for time, i in enumerate(A):
        if i < N+1:
            C.increment(i, time+1)
        else:
            C.set_min_to_max(time+1)

    counters = C.get_all_counters()

    return counters