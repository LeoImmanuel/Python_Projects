def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return  True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(4,num):
        if ( num % i ) == 0:
            break
    else:
        return True


n = 3

prime_list = [ num for num in range(2,n+1) if is_prime(num) ]
print(prime_list)
