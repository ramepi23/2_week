def is_prime(num):
    for i in range(2, num):
        if num % i  == 0:
            return False
    return True 

def primes_below(n):
    prime_lot = []
    for i in range(2,n):
        if is_prime(i):
            prime_lot.append(i)
    return prime_lot