# 1
# 23
# 456
# 78910

n = int(input("Enter number:"))
count = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(count,end=" ")
        count += 1
    print()
