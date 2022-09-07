import time

#! we don't want to use time.time() to measure performance as it uses the system clock. This clock can change.

def f():
    return (1,) * 100000

#! time
# t0 = time.time()

# for _ in range(10):
#     f()

# t1 = time.time()

# print(f"{t1 - t0:.5f}")


#? monotonic - more accurate
t0 = time.monotonic()

for _ in range(10):
    f()

t1 = time.monotonic()

print(f"{t1 - t0:.5f}")