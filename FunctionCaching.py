from functools import lru_cache
import time
@lru_cache(maxsize=None)                
# def fx(n):
#     time.sleep(5)
#     return n*5
# print(fx(20))
# print("done for the 20")
# print(fx(2))
# print("done for the 2")
# print(fx(10))
# print("done for tehe 10")
# #After this the value of the result stored in the cache so the memory go in the fast way.

# print(fx(20))
# print("done for the 20")
# print(fx(2))
# print("done for the 2")
# print(fx(10))
# print("done for tehe 10")
# for the factorial
def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)
print(fib(20))
print(fib(21))
#output:6765
