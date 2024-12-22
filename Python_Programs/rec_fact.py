def rec_fact(n):
    if n == 0:
        return 1
    else:
        return n * rec_fact(n-1)

n = 1

if n < 0:
    print("Enter a positive integer:")
else:
    print(rec_fact(n))