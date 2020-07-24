'''
    Unit testing module for MaxCounters.py

    Author: Miloš Pivaš, student
'''

from MaxCounters import Solution
from MaxCounters import solution


### Testing Solution.Node #########################################################################

def test_Solution_Node_init():
    '''
    Testing Solution.Node.__init__()
    '''

    val, time = 42, 0
    n = Solution.Node(42, 0)

    init_passed = (val, time) == (n.val, n.time)
    return init_passed


### Testing Solution.Counters #####################################################################

def test_Solution_Counters_init():
    '''
    Testing Solution.Counters.__init__()
    '''

    N = 42
    C = Solution.Counters(N)

    init_passed = (N, {}, 0, 0, 0) == (C.N, C.counter, C.min_time, C.min, C.max)
    return init_passed

def test_Solution_Counters_increment_at_start():
    '''
    Testing Solution.Counters.increment() at start
    '''

    N = 3
    C = Solution.Counters(N)

    i, time = 1, 1
    C.increment(i, time)

    true_sol = (N, 1, time, 0, 0, 1)
    sol = (C.N, C.counter[i].val, C.counter[i].time, C.min_time, C.min, C.max)
    increment_passed = true_sol == sol
    return increment_passed

def test_Solution_Counters_set_min_to_max_after_increment():
    '''
    Testing Solution.Counters.set_min_to_max() after increment()
    '''

    N = 3
    C = Solution.Counters(N)

    i, time = 1, 1
    C.increment(i, time)

    time_plus_1 = time+1
    C.set_min_to_max(time_plus_1)

    set_min_to_max_passed = (time_plus_1, 1, 1) == (C.min_time, C.min, C.max)
    return set_min_to_max_passed

def test_Solution_Counters_get_all_counters():
    '''
    Testing Solution.Counters.get_all_counters()
    '''

    N = 3
    C = Solution.Counters(N)

    counters = C.get_all_counters()

    true_sol = ([0] * N)
    get_all_counters_passed = true_sol == counters

    return get_all_counters_passed

def test_Solution_Counters_get_all_counters_after_increment():
    '''
    Testing Solution.Counters.get_all_counters() after increment()
    '''

    N = 3
    C = Solution.Counters(N)

    i, time = 1, 1
    C.increment(i, time)

    counters = C.get_all_counters()

    true_sol = ([0] * N)
    true_sol[i-1] = 1
    get_all_counters_passed = true_sol == counters

    return get_all_counters_passed

def test_Solution_Counters_get_all_counters_after_increment_and_set_min_to_max():
    '''
    Testing Solution.Counters.get_all_counters()
    after increment() and set_min_to_max()
    '''

    N = 3
    C = Solution.Counters(N)

    i, time = 1, 1
    C.increment(i, time)

    time_plus_1 = time+1
    C.set_min_to_max(time_plus_1)

    counters = C.get_all_counters()

    true_sol = ([1] * N)
    get_all_counters_passed = true_sol == counters

    return get_all_counters_passed

def test_Solution_Counters_get_all_counters_after_inc_set_inc_set():
    '''
    Testing Solution.Counters.get_all_counters() after
    increment(), set_min_to_max(), increment(), set_min_to_max()
    '''

    N = 3
    C = Solution.Counters(N)

    time = 0
    for i in [1,2]:
        time += 1
        C.increment(i, time)

        time += 1
        C.set_min_to_max(time)

    counters = C.get_all_counters()

    true_sol = ([2] * N)
    get_all_counters_passed = true_sol == counters

    return get_all_counters_passed


### Testing Solution.solution #####################################################################

def test_Solution_solution_no_containers():
    '''
    Testing Solution.solution() on N = 0
    '''
    N, A = 0, [1,2,3]

    true_sol = []
    sol = Solution.solution(N, A)
    solution_passed = true_sol == sol
    return solution_passed

def test_Solution_solution_no_operations():
    '''
    Testing Solution.solution() on A = []
    '''
    N, A = 42, []

    true_sol = [0] * N
    sol = Solution.solution(N, A)
    solution_passed = true_sol == sol
    return solution_passed

def test_Solution_solution_single_increment():
    '''
    Testing Solution.solution() on N, A = 3, [1]
    '''
    N, A = 3, [1]

    true_sol = [0] * N
    true_sol[0] = 1
    sol = Solution.solution(N, A)
    solution_passed = true_sol == sol
    return solution_passed

def test_Solution_solution_increment_and_set():
    '''
    Testing Solution.solution() on N, A = 3, [1,4]
    '''
    N, A = 3, [1,4]

    true_sol = [1] * N
    sol = Solution.solution(N, A)
    solution_passed = true_sol == sol
    return solution_passed

def test_Solution_solution_increment_set_increment():
    '''
    Testing Solution.solution() on N, A = 3, [1,4,2]
    '''
    N, A = 3, [1,4,2]

    true_sol = [1] * N
    true_sol[1] = 2
    sol = Solution.solution(N, A)
    solution_passed = true_sol == sol
    return solution_passed

def test_Solution_solution_increment_set_increment_set_increment():
    '''
    Testing Solution.solution() on N, A = 3, [1,4,2,4,3]
    '''
    N, A = 3, [1,4,2,4,3]

    true_sol = [2] * N
    true_sol[2] = 3
    sol = Solution.solution(N, A)
    solution_passed = true_sol == sol
    return solution_passed


### Testing solution() ############################################################################

def test_solution_no_containers():
    '''
    Testing solution() on N = 0
    '''
    N, A = 0, [1,2,3]

    true_sol = []
    sol = solution(N, A)
    solution_passed = true_sol == sol
    return solution_passed

def test_solution_no_operations():
    '''
    Testing solution() on A = []
    '''
    N, A = 42, []

    true_sol = [0] * N
    sol = solution(N, A)
    solution_passed = true_sol == sol
    return solution_passed

def test_solution_single_increment():
    '''
    Testing solution() on N, A = 3, [1]
    '''
    N, A = 3, [1]

    true_sol = [0] * N
    true_sol[0] = 1
    sol = solution(N, A)
    solution_passed = true_sol == sol
    return solution_passed

def test_solution_increment_and_set():
    '''
    Testing solution() on N, A = 3, [1,4]
    '''
    N, A = 3, [1,4]

    true_sol = [1] * N
    sol = solution(N, A)
    solution_passed = true_sol == sol
    return solution_passed

def test_solution_increment_set_increment():
    '''
    Testing solution() on N, A = 3, [1,4,2]
    '''
    N, A = 3, [1,4,2]

    true_sol = [1] * N
    true_sol[1] = 2
    sol = solution(N, A)
    solution_passed = true_sol == sol
    return solution_passed

def test_solution_increment_set_increment_set_increment():
    '''
    Testing solution() on N, A = 3, [1,4,2,4,3]
    '''
    N, A = 3, [1,4,2,4,3]

    true_sol = [2] * N
    true_sol[2] = 3
    sol = solution(N, A)
    solution_passed = true_sol == sol
    return solution_passed


### Running tests #################################################################################

test_functions = [ 
    test_Solution_Node_init,
    test_Solution_Counters_init,
    test_Solution_Counters_increment_at_start,
    test_Solution_Counters_set_min_to_max_after_increment,
    test_Solution_Counters_get_all_counters,
    test_Solution_Counters_get_all_counters_after_increment,
    test_Solution_Counters_get_all_counters_after_increment_and_set_min_to_max,
    test_Solution_Counters_get_all_counters_after_inc_set_inc_set,
    test_Solution_solution_no_containers,
    test_Solution_solution_no_operations,
    test_Solution_solution_single_increment,
    test_Solution_solution_increment_and_set,
    test_Solution_solution_increment_set_increment,
    test_solution_increment_set_increment_set_increment,
    test_solution_no_containers,
    test_solution_no_operations,
    test_solution_single_increment,
    test_solution_increment_and_set,
    test_solution_increment_set_increment,
    test_solution_increment_set_increment_set_increment
]

for test_func in test_functions:
    print('Runing: ', test_func.__name__)
    print('Description:')
    print(test_func.__doc__)
    print()
    assert test_func() == True

print('Exiting...')