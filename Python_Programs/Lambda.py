from functools import reduce

n = [ 2, 4, 6, 8, 7, 1, 10, 13, 24 ]

evens = list(filter(lambda x:  x%2 == 0 ,n))

sqt = list(map(lambda x: x*x,evens))

print(sqt )

total = reduce(lambda x,y: x+y, sqt)

print(total)

