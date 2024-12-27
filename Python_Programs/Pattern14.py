#    A
#   ABA
#  ABCBA
# ABCDCBA

def print_pyramid(n):

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(1, n + 1):
        inc_part = alphabet[:i]

        dec_part = inc_part[:-1][::-1]

        line = inc_part + dec_part

        print(line.center( 2 * n - 1 ))


n = 3

print_pyramid(n)


