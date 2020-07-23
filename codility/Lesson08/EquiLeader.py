# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# write your code in Python 3.6

def solution(A):
    ''' Returns the number of ways to split the list A
    into slices A[:i] and A[i:] so that they have an equi-leader.

    A leader of an array of length N is an element that appears more than N/2 times in the array.
    An equi-leader of two arrays is an element that is a leader in both arrays.

    Parameters
    ----------
    A : list
        List of ints.

    Returns
    -------
    out : int
        The solution.
    '''
    cnt = {}

    for x in A:
        cnt[x] = (cnt[x] + 1) if (x in cnt) else 1

    N = len(A)
    leader = None
    for k, v in cnt.items():
        if v > N/2:
            leader = k
            leader_cnt = v

    if leader is None:
        return 0

    equi_leader_cnt = 0

    leader_cnt_left = 0
    for i, a in enumerate(A):
        if a == leader:
            leader_cnt_left += 1

        is_left_leader = leader_cnt_left > (i+1)/2
        is_right_leader = (leader_cnt - leader_cnt_left) > (N - i - 1) / 2
        if (is_left_leader) and (is_right_leader):
            equi_leader_cnt += 1

    return equi_leader_cnt