# write your code in Python 3.6
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    ''' Check if S is properly nested.

    S is properly nested if:
        1) S is empty
        2) S has the form "(U)", "[U]" or "{U}"
        3) S has the form "VW"
    where U, V and W are properly nested strings.

    Parameters
    ----------
    S : str
        The string to be checked for nesting.
        0 < len(S) < 2 * 10**5

    Returns
    -------
    out : int
        1 if properly nested, 0 otherwise.
    '''

    def __exception_S_None():
        if S is None:
            raise Exception('S is None.')

    def __exception_S_str():
        if type(S) is not str:
            raise Exception('S is not a string.')

    def __exception_S_len():
        if len(S) > 200000:
            raise Exception('S is too big.')

    def __exception_S_elements():
        brackets = {'(', '[', '{', '}', ']', ')'}
        for c in S:
            if c not in brackets:
                raise Exception('Element(s) of S are not brackets.')

    def __init_brackets():
        open_brackets = {'(' : 0, '[' : 0, '{' : 0}
        closed_to_open_bracket = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        return open_brackets, closed_to_open_bracket

    def __check_nesting_via_stack():
        stack = []
        for c in S:
            if c in open_brackets:
                stack += [c]
            else:
                open_of_c = closed_to_open_bracket[c]
                if (len(stack) > 0) and (open_of_c == stack[-1]):
                    stack.pop()
                else:
                    return 0

        return int(len(stack) == 0)

    __exception_S_None()
    __exception_S_str()
    __exception_S_len()

    if S == '':
        return 1

    __exception_S_elements()

    open_brackets, closed_to_open_bracket = __init_brackets()

    properly_nested = __check_nesting_via_stack()

    return properly_nested