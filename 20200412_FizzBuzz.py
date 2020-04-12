''' FizzBuzz game implementation.
    The key takeaway is the separation of 'game' cases and the default case.
'''

def print_fizz_buzz(n : int) -> None:
    ''' for numbers from 1 to n, play FizzBuzz:\n
            if number is a multiple of 3: print Fizz,\n
            if number is a multiple of 5: print Buzz,\n
            if neither: print that number.\n
    
    '''

    print("FizzBuzz({}):".format(n))
    
    for i in range(1, n+1):
        print("\t", i, ": ", end="")

        default_flag = True

        # the 'game' cases:
        if i % 3 == 0:
            print("Fizz", end="")
            default_flag = False
        
        if i % 5 == 0:
            print("Buzz", end="")
            default_flag = False


        # the default case
        if default_flag:
            print(i, end="")
        
        print()


# test cases
print_fizz_buzz(42)

print_fizz_buzz(0)

print_fizz_buzz(-1)

print_fizz_buzz(1)