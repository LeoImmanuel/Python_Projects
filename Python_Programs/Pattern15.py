#    A
#   ABC
#  ABCDE
# ABCDEFG

def print_pyramid(n):

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(1, n + 1):
        inc_part = alphabet[ : 2 * i - 1]

        print(inc_part.center( 2 * n - 1 ))


n = 5

print_pyramid(n)