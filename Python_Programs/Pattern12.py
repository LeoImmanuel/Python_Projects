#    *
#   ***
#  *****
# *******

n = 4

for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for k in range((i*2)+1):
        print("*",end="")
    print ()

"""
k = 2 * n - 1
for i in range(1,n+1):
    print(" " * (k // 2), end="")
    print("*" * (2 * i - 1))
    k = 2 * (n - i) - 1
    
"""