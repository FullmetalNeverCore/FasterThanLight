import math
from time import perf_counter
from numba import njit,prange

@njit(fastmath=True)
def isprime_num(num):
    for x in range(2,int(math.sqrt(num))+1):
        return False if num%x == 0  else True 

@njit(fastmath=True,parallel=True)
def runnner_num(x):
    for x in prange(x):isprime_num(x)

def isprime(num):
    for x in range(2,int(math.sqrt(num))+1):
        return False if num%x == 0  else True 
def runnner(x):
    for x in range(x):isprime(x)

def start():
 x = input('INPUT A NUMBER OF ITERATIONS: ')
 calculating_time(int(x))

def calculating_time(x):
    start = perf_counter()
    runnner_num(x)
    end = perf_counter()
    print('Python+Numba'),print(end - start)
    print('Pure Python incoming!!!')
    start_org = perf_counter()
    runnner(x)
    end_org = perf_counter()
    print('Python'),print(end_org - start_org)


start()