fib0 = 0
fib1 = 1

n = 5
if n<=0 :
    print("Enter values greater than zero")
elif n == 1 :
    print(fib0)
else:
    print(fib0)
    print(fib1)
    for i in range(n-2):
        fib2= fib1 + fib0
        fib0, fib1 = fib1, fib2
        print(fib2)