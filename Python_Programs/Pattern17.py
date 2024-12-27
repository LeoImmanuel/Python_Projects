#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

n = int(input("Enter number:"))

# top triangle
for i in range(1,n+1):
# printing spaces
    for j in range(1,n+1-i):
        print(" ",end=" ")
# printing *
    for k in range((i*2)-1):
        print("*", end=" ")
    print()
# bottom triangle
for i in range(1,n):
# print spaces
    for j in range(1,i+1):
        print(" ",end=" ")
# print *
    for j in range((2 * ( n - i ) ) - 1 ):
        print("*", end=" ")
    print()