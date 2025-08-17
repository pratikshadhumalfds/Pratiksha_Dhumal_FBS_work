def is_prime(num):
    if num < 2:
        return False
    for i in range (2, int(num**0.5)+1):
        if num % i == 0:
            return False
        return True
def sum_primes(n):
    s=0
    for i in range(1, n+1):
        if is_prime(i):
            s+=i
    return s

n=int(input("Enter the number:"))
print('Sum of primes:', sum_primes(n)) 