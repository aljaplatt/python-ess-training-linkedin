import threading
import time
from multiprocess import Process

#? 9. THREADS AND PROCESSES

#* THREADS

#* Calculates square of number after 1 second 
# def longSquare(num):
#     time.sleep(1)
#     return num**2

print([longSquare(n) for n in range(0, 5)]) #? [0, 1, 4, 9, 16]

#* Waiting for data from a remote server, threads allow to wait in parallel - not one at a time.
#? 2 threads - t1 & t2 - target is the target function, args = what we pass to that fn
#* comma in tuple indicates its a tuple, not a local variable with a single value?  
# t1 = threading.Thread(target=longSquare, args=(1,))
# t2 = threading.Thread(target=longSquare, args=(2,))

#? Start threads
# t1.start()
# t2.start()

#? Joins threads - join fn checks if the thread has completed execution, and will pause until it has
# t1.join()
# t2.join()

#? Where are the results? No way to directly access return value - but threads share memory!

#* Create results dictionary  and pass into longSq fn.
#? Instead of returning,  output is added to the dictionary 
# def longSquare(num, results):
#     time.sleep(1)
#     results[num] = num**2

# results = {}

# t1 = threading.Thread(target=longSquare, args=(1,results))
# t2 = threading.Thread(target=longSquare, args=(2,results))

#! Writing 'start / join' can be laborious, if you have many threads / values
# t1.start()
# t2.start()

# t1.join()
# t2.join()

# #* Threads share memory and can modify the same object  
# print(results) #? {2: 4, 1: 1}

#! It is a common practice to put these into a list = threads = []

# def longSquare(num, results):
#     time.sleep(1)
#     results[num] = num**2

# results = {}
# threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0, 100)]
# [t.start() for t in threads]
# [t.join() for t in threads]
# print(results)

#? OUTPUT for 100 threads! 
# [0, 1, 4, 9, 16]
# {2: 4, 1: 1}
# {2: 4, 1: 1, 0: 0, 8: 64, 9: 81, 16: 256, 17: 289, 19: 361, 30: 900, 25: 625, 28: 784, 29: 841, 3: 9, 13: 169, 15: 225, 21: 441, 22: 484, 4: 16, 14: 196, 6: 36, 20: 400, 39: 1521, 40: 1600, 5: 25, 42: 1764, 43: 1849, 44: 1936, 45: 2025, 47: 2209, 7: 49, 38: 1444, 37: 1369, 32: 1024, 41: 1681, 46: 2116, 10: 100, 11: 121, 12: 144, 18: 324, 33: 1089, 23: 529, 70: 4900, 75: 5625, 82: 6724, 85: 7225, 86: 7396, 91: 8281, 92: 8464, 94: 8836, 95: 9025, 96: 9216, 97: 9409, 98: 9604, 99: 9801, 63: 3969, 81: 6561, 26: 676, 35: 1225, 36: 1296, 49: 2401, 50: 2500, 51: 2601, 52: 2704, 53: 2809, 60: 3600, 66: 4356, 74: 5476, 77: 5929, 79: 6241, 83: 6889, 84: 7056, 87: 7569, 93: 8649, 24: 576, 27: 729, 64: 4096, 61: 3721, 65: 4225, 69: 4761, 73: 5329, 78: 6084, 90: 8100, 62: 3844, 31: 961, 34: 1156, 67: 4489, 68: 4624, 80: 6400, 88: 7744, 89: 7921, 48: 2304, 57: 3249, 71: 5041, 72: 5184, 76: 5776, 54: 2916, 56: 3136, 55: 3025, 58: 3364, 59: 3481}

#* MULTIPROCESSING - pip3 install multiprocess
#? Processes don't share memory. 


def longSquare(num, results):
    time.sleep(1)
    print(num**2)
    print('Finished computing!')

results = {}
processes = [Process(target=longSquare, args=(n,results)) for n in range(0, 10)]
[p.start() for p in processes]
[p.join() for p in processes]

#? OUTPUT 
# 01
# 4
# 9
# Finished computing!Finished computing!16
# 25Finished computing!


# 36Finished computing!

# 49Finished computing!64

# 81Finished computing!
# Finished computing!


# Finished computing!Finished computing!
# Finished computing!


# [None, None, None, None, None, None, None, None, None, None]

results = {}
threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0, 10)]
[t.start() for t in threads]
[t.join() for t in threads]
print(results)

#? WHATS HAPPENING?
#  Threading emulates parallel computing
# useful when your programs have periods of downtime 

#? OUTPUT 
# 9163625496481
# Finished computing!
# 14

# Finished computing!

# Finished computing!
# Finished computing!



# Finished computing!
# Finished computing!
# 0Finished computing!
# Finished computing!


# Finished computing!
# Finished computing!

# {}

#* 10. WORKING WITH FILES


#? 11. PACKAGING PYTHON