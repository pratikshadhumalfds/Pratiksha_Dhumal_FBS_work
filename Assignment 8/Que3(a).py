def sum_natural(n):
    s=0
    for i in range (1, n+1):
        s+=i
    return s

n=int(input("Enter n:"))
print("Sum=",sum_natural(n))    