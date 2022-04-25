##################################################
# Fibonacci series
# SOL 1: Recursion (w/o caching) - T: O(2^N), S: O(N)
##################################################
# def getNthFib(n):
#     if n == 2:
#         return 1
#     elif n == 1:
#         return 0
#     else:
#         return getNthFib(n - 1) + getNthFib(n - 2)


#############################################################
# Fibonacci series
# SOL 2: Recursion (w caching i.e. caching) - T: O(N), S: O(N)
#############################################################
# def getNthFib(n, memoize = {1: 0, 2: 1}):
#     if n in memoize:
#         return memoize[n]
#     else:
#         memoize[n] = getNthFib(n-1, memoize) + getNthFib(n-2, memoize)
#         return memoize[n]


#############################################################
# Fibonacci series
# SOL 3: Iterative - T: O(N), S: O(1)
#############################################################
def getNthFib(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter+=1
    return lastTwo[1] if n > 1 else lastTwo[0]