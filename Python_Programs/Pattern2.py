#1
#12
#123
#1234
#12345

n = 5
for i in range(n):
    for j in range(i+1):
        print(j+1, end="")
    print()