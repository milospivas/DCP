# write your code in Python 3.6
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    ''' Checks if S is properly nested.

    S is properly nested if:
        1) S is empty
        2) S has the form "(U)"
        3) S has the form "VW"
    where U, V and W are properly nested strings.

    Parameters
    ----------
    S : str
        String made of '(' and ')'.

    Returns
    -------
    out : int
        1 if properly nested, 0 otherwise.
    '''
    cnt = 0

    for c in S:
        cnt = (cnt + 1) if (c == '(') else (cnt - 1)

        if cnt < 0:
            return 0

    return int(cnt == 0)