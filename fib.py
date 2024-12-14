def fib1(n):
    if n==1 or n==2: return 1
    return fib1(n-1)+fib1(n-2)

from functools import lru_cache 

@lru_cache 
def fib2(n):
    if n==1 or n==2: return 1
    return fib2(n-1)+fib2(n-2)

def fib3(n):
    if n==1 or n==2: return 1
    second_last = 1
    last = 1
    for i in range(3,n+1):
        curr = last + second_last
        second_last = last 
        last = curr
    return last 

from time import time 
N = 30

a = time()
print(fib3(N))
b=time()
print(f"Iterative Took {round(b-a,3)} seconds")

a = time()
print(fib2(N))
b=time()
print(f"Cached recursive Took {round(b-a,3)} seconds")

a = time()
print(fib1(N))
b=time()
print(f"Recursive Took {round(b-a,3)} seconds")