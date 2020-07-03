''' Problem:
    Given a list of daily temperatures T, return a list such that, for each day in the input,
    tells you how many days you would have to wait until a warmer temperature.
    If there is no future day for which this is possible, put 0 instead.

    For example, given the list of temperatures
    T = [73, 74, 75, 71, 69, 72, 76, 73],
    your output should be
    sol = [1, 1, 4, 2, 1, 1, 0, 0].
'''

''' Solution(s):
    Brute-force:
        for each element, linearly search for the next greater one 
        O(n^2) time

    Better solution:
        Keep a MinHeap with value-index pairs (or just indices) to store
            all elements not yet matched with a next greater element.
        Start with only the first element in the heap.
        Then for every next element,
            while it's greater than the min in the heap,
                extract min and compute the distance
            then add it to the heap
        O(n*log(n)) time

    Optimal solution:
        We can do basically the same thing from the MinHeap solution with a stack.
        
        Pseudocode:
            For each element in the given list:
                pop all the lesser elements from the stack
                while marking their distance from the current element
                Push the current element.
        
        Note that the stack will always remain in non-ascending order.
        We will never push an element over a lesser one,
        because we poped all the lesser ones first.
        This is why we don't need to check the stack further from the
        first element greater or equal than the current one.
        => O(n) time.
    
    All solutions are O(n) space.
'''

### the stack solution:

def dailyTemperatures(T):
    ''' For a given list T, returns a list of the same length,
    where every i-th element is the distance from the i-th element in T
    to the next element in T greater than the i-th element.
    '''

    # initialize the solution list and a stack
    sol = [0 for _ in T]
    stack = [0 for _ in T]
    top = 0

    # iterate through the list
    for i, curr in enumerate(T):
        # first, pop all the elements lesser than the current one
        while top > 0 and T[stack[top-1]] < curr:
        # while the stack is not empty and
        # the top of the stack is lesser than the current element
            # 1. pop stack
            top -= 1
            prev_lesser = stack[top]
            # 2. save the distance between the current element and the top of the stack
            sol[prev_lesser] = i - prev_lesser

        # push to stack
        stack[top] = i
        top += 1
        # note that the stack keeps the element indices, not values directly.

    return sol