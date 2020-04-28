''' 
    Magical Company [Math/Dynamic Programming]

    Task description:
        A company has N offices with n[i] workers in every i-th office.

        The HR departement has started practicing black magic,
        and now every day, the number of workers in every office magically doubles.
        Due to spacial constraints, when there are more than C workers in a single office,
        half of the workers are moved to a brand new office (the office building is also magical).
        
        How many offices will the company have on any given day from now?

        Given values are:
            C in range(1, 1001) - office pop cap
            N in range(0, 1001) - #offices at day0
            M in range(1, 51)   - #days queried 
            
            n[i] in range(1, C+1) (for i in range(N)) - #workers in each office
            d[i] in range(0, 51) (for i in range(M)) - days for which to compute the current #offices
    
    Solution author: Miloš Pivaš
    Problem adapted from: https://open.kattis.com/problems/magicalcows
'''

######################################## Maths solution ########################################

from math import log2, floor

def num_opt_n(C, N, M, n, d):
    """ Simple maths solution.

        Time complexity O(M * N)
        Space complexity O(N) + O(M)
    """
    #   For each office, calculate how many days are left until it's full:
    #       size * 2**a[i] = C
    #       2**a[i] = C/size
    #       a[i] = log2(C/size)
    a = [floor(log2(C/size)) for size in n]
    
    sol = [0 for _ in d] # init the solution list

    # Then for every queried day, and for each office
    for i, day in enumerate(d):
        for days_until_full in a:
        # simply calculate the number of offices spawned from the starting one:
            # if days_until_full is bigger than day, there's no doubling
            days_of_doubling = max(0, day - days_until_full)
            sol[i] += 2**days_of_doubling

    return sol


def num_opt_c(C, N, M, n, d):
    """ Since offices are independant,
        all offices of the same size will behave the same,
        so we will count the occurrences of each size,
        and deal with only one office per size.

        Time complexity O(M * C)
        Space complexity O(C) + O(M)
    """
    o = [0 for _ in range(C+1)]
    a = [0 for _ in range(C+1)]

    for size in n:
        o[size] += 1   # number of occurrences of each size in n
    
    for size in range(1, C+1):
        a[size] = floor( log2(C/size) )   # number of days until size will double up to C
    
    sol = [0 for _ in d] # init the solution list

    # for every queried day, and for each office size:
    for i, day in enumerate(d):
        for size in range(1, C+1):
            if o[size] > 0: # if there are offices of that size
            # simply calculate the number of offices spawned from the starting offices:
                days_until_full = a[size]
                # if days_until_full is bigger than day, there's no doubling
                days_of_doubling = max(0, day - days_until_full)
                sol[i] += o[size] * (2**days_of_doubling)

    return sol


def num(C, N, M, n, d):
    """ Chooses which algorithm to use,
        based on the values of N and C
    """

    if N <= C:
        return num_opt_n(C, N, M, n, d)
    else:
        return num_opt_c(C, N, M, n, d)



######################################## DP solution ########################################

def num_dp(C, N, M, n, d):
    """ Dynamic programming solution via memo table.
        Time complexity O(M * C)
        Space complexity O(M * C)

        * Note: this could be optimized for O(M + C) space complexity by using only 2 lists as rows,
        instead of the whole memo table.
        But since the upper bound for C is already very small (50), there's no good reason to do this,
        since it would also require overwriting lists with 0s which would slow the execution down.
    """
    # skip the calculation if no offices given
    if N == 0:
        sol = [0 for _ in d]
    else:
        last_day = max(d)

        # init a memo table
        dp = [[0 for _ in range(C+1)] for _ in range(last_day+1)]
        
        sol = [0 for _ in d] # init the solution list

        # fill the values for day0
        for size in n:
            dp[0][size] += 1

        # for each day, from day 1, up to the last queried day
        for day in range(1, last_day+1):
            for size in range(C+1):
                if size <= C/2:
                    dp[day][2*size] += dp[day-1][size]
                else:
                    dp[day][size] += 2*dp[day-1][size]

        for k, day in enumerate(d):
            sol[k] = sum(dp[day])
        
    return sol

######################################## Console input ########################################

# C, N, M = (int(x) for x in input().split(' '))
# n = [int(input()) for _ in range(N)]
# d = [int(input()) for _ in range(M)]

# # sol = num(C, N, M, n, d)
# # for x in sol:
# #     print(x)

# sol_dp = num_dp(C, N, M, n, d)
# for x in sol_dp:
#     print(x)

######################################## Test cases ########################################

C, N, M = 2, 5, 5
n = [1, 2, 1, 2, 1]
d = [0, 1, 2, 3, 4]
sol = num(C, N, M, n, d)
print(sol)
sol_dp = num_dp(C, N, M, n, d)
print(sol_dp)
assert(sol == sol_dp)


C, N, M = 1, 5, 5
n = [1, 1, 1, 1, 1]
d = [0, 1, 2, 3, 4]
sol = num(C, N, M, n, d)
print(sol)
sol_dp = num_dp(C, N, M, n, d)
print(sol_dp)
assert(sol == sol_dp)


C, N, M = 8, 4, 5
n = [1, 3, 2, 1]
d = [0, 1, 2, 3, 4]
sol = num(C, N, M, n, d)
print(sol)
sol_dp = num_dp(C, N, M, n, d)
print(sol_dp)
assert(sol == sol_dp)


C, N, M = 5, 3, 5
n = list(range(1,C+1))
d = [0, 1, 2, 3, 4]
sol = num(C, N, M, n, d)
print(sol)
sol_dp = num_dp(C, N, M, n, d)
print(sol_dp)
assert(sol == sol_dp)


C, N, M = 42, 0, 3
n = []
d = list(range(1,M+1))
sol = num(C, N, M, n, d)
print(sol)
sol_dp = num_dp(C, N, M, n, d)
print(sol_dp)
assert(sol == sol_dp)
