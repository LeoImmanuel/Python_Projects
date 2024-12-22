n = 4
fact = 1
if n <=0:
    print("Input positive number ")
else:
    for i in range(1,n+1):
        fact = fact * i
    print(fact)