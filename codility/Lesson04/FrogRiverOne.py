# write your code in Python 3.6
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    ''' Return the eariliest time
    when the frog can jump to the other side of the river bank
    of length X, with the leaves falling described by A.

    The frog is initially at position = 0.
    The other side of the bank is at postiion = X+1.
    The frog can jump over the river, when the leaves form a path.
    (The river is very slow, so the leaves practically don't move).

    Parameters
    ----------
    X : int
        Length of the river bank.

    A : list
        List of int, representing the falling leaves.
        A[K] represents the position where one leaf falls at time K,
        measured in seconds.

    Returns
    -------
    out : int
        The earliest time when the frog can jump (in seconds).
        -1 if impossible to jump.

    Raises
    ------
    Exception
        'Input X is None.'
    Exception
        'Input A is None.'
    Exception
        'Input X of wrong type.'
    Exception
        'Input A of wrong type.'
    Exception
        'Element(s) of input A of wrong type.'
    Exception
        'X is negative,'
    Exception
        'Element(s) from A out of range'
    '''

    def __exception_handling():

        if X is None:
            raise Exception('Input X is None.')

        if A is None:
            raise Exception('Input A is None.')

        if type(X) is not int:
            raise Exception('Input X of wrong type.')

        if type(A) is not list:
            raise Exception('Input A of wrong type.')

        for pos in A:
            if type(pos) is not int:
                raise Exception('Element(s) of input A of wrong type.')

        if X < 0:
            raise Exception('X is negative,')

        for pos in A:
            if not (0 < pos < X+1):
                raise Exception('Element(s) from A out of range')


    def __mark_first_leaf_times():
        ''' Marks the first occurence of a leaf at each position.
        '''
        leaf_times = {}
        for K, pos in enumerate(A):
            if not pos in leaf_times:
                leaf_times[pos] = K
                continue

            if K < leaf_times[pos]:
                leaf_times[pos] = K
        return leaf_times

    def __check_every_position():
        ''' Checks if every position has a leaf.
        '''
        leaf_absent = False
        for pos in range(1, X+1):
            if pos not in leaf_times:
                leaf_absent = True
                break
        return leaf_absent

    def __find_last_leaf_time():
        max_time = -1
        for time in leaf_times.values():
            if time > max_time:
                max_time = time
        return max_time

    __exception_handling()

    leaf_times = __mark_first_leaf_times()

    leaf_absent = __check_every_position()

    max_time = -1 if leaf_absent else __find_last_leaf_time()

    return max_time


def test_solution():

    input_list = [  (3, [1,2,3]),
                    (0, []),
                    (1, [1]),
                    (None, []),
                    (42, None),
                    (4.2, []),
                    (4, [3.2, 3, 1]),
                    (-5, []),
                    (5, [42]),
                    (5, [-42])]

    for X, A in input_list:
        print('X, A =',X,A)
        try:
            sol = solution(X, A)
            print('solution =',sol)
        except Exception as e:
            print(e)