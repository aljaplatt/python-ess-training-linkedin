import timeit

# print('Performance and Timeit module')
# # Experiment with sieve of Eratosthenes - find prime nums in range 
# print([x for x in range(1, 151) if not any([x % y == 0 for y in range(2, x)]) and not x == 1])
# # same - compare which is faster
# print([x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])])
# # same
# # Initialize a list
# primes = []
# for possiblePrime in range(2, 151):
# # Assume number is prime until shown it is not.
#    isPrime = True
#    for num in range(2, int(possiblePrime ** 0.5) + 1):
#        if possiblePrime % num == 0:
#            isPrime = False
#            break
#    if isPrime:
#        primes.append(possiblePrime)
# print(primes)


def test1():
    [x for x in range(1, 151) if not any([x % y == 0 for y in range(2, x)]) and not x == 1]
    return(1)

def test2():
    [x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])]

def test3():
    # Initialize a list
    primes = []
    for possiblePrime in range(2, 151):
    # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    #print(primes)
    return(1)

print(timeit.timeit('test1()', globals=globals(), number=10))
print(timeit.timeit('test2()', globals=globals(), number=10))
print(timeit.timeit('test3()', globals=globals(), number=10))
'''
0.00519004202215001
0.004818165994947776
#* 0.0005011670000385493 FASTEST
'''