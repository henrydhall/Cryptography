"""a4.py"""

# Problem 2.4
def brute_force_discrete_log(g,h,p):
    for i in range(0,p):
        if (g**i - h) % p == 0:
            return i
    return 'fail'

if __name__ == '__main__':
    """
    print(brute_force_discrete_log(2, 13, 23))
    print(brute_force_discrete_log(10, 22, 47))
    print(brute_force_discrete_log(627, 608, 941))
    """
    print( brute_force_discrete_log(2,1,5) )
    print( brute_force_discrete_log(2,2,5) )
    print( brute_force_discrete_log(2,3,5) )
    print( brute_force_discrete_log(2,4,5) )

    print( brute_force_discrete_log(2,9,5) )
    print( 2*brute_force_discrete_log(2,3,5) % 4 )


