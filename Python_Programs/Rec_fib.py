def rec_fib(n):
    if n <= 1:
        return n
    else:
        return rec_fib(n-1) + rec_fib(n-2)

n = 6

if n <= 0:
    print("enter a number greater than zero")
else:
    print("Fibonacci Series:")
    for i in range(n):
        print(rec_fib(i))

