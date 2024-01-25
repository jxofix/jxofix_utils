import time
from datetime import timedelta

def fib(n):
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)

def fib_memo(n, memo={}):
    if memo is None:
        memo = {}
    if n in memo: return memo[n]
    if n <= 2: return 1

    memo[n] = fib_memo(n-1, memo)+fib_memo(n-2, memo)
    return memo[n]

def fib_tom(n):
    if n <= 2: return 1
    a = 1
    b = 1
    res = a + b

    for i in range(n-3):
        a = b
        b = res
        res = a + b

    return res


test_num = 20

print('-'*3, 'fib reccursive', '-'*3)
start = time.time()
print(fib(test_num))
end = time.time()
print(timedelta(seconds=end-start))

print('-'*3, 'fib memo', '-'*3)
start = time.time()
print(fib_memo(test_num))
end = time.time()
print(timedelta(seconds=end-start))

print('-'*3, 'fib tom', '-'*3)
start = time.time()
print(fib_tom(test_num))
end = time.time()
print(timedelta(seconds=end-start))