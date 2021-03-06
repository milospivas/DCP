'''
    Solution for Codility Lesson04, MaxCounters problem.

    Author: Miloš Pivaš, student
'''

class Solution:

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
                self.counter[i] = Solution.Node()

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
            counters = [0 for _ in range(self.N)]

            for i in range(1, self.N+1):
                counters[i-1] = (self.counter[i].val) if ((i in self.counter) and (self.counter[i].time > self.min_time)) else self.min

            return counters


    @classmethod
    def solution(cls, N, A):

        if N == 0:
            return []
        if A == []:
            return [0] * N


        C = cls.Counters(N)
        for time, i in enumerate(A):
            if i < N+1:
                C.increment(i, time+1)
            else:
                C.set_min_to_max(time+1)

        counters = C.get_all_counters()

        return counters


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

    sol = Solution.solution(N, A)

    return sol