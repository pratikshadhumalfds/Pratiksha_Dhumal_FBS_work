def sum_powers(n):
    s=0
    for i in range(1, n+1):
        s+=i**i
    return s
n=int(input("Enter the number:"))    
print('Sum of powers:',sum_powers(n))