def sum_odd(n):
    s=0
    for i in range (1, n+1, 2):
        s+=i
    return s
n=int(input("Enter the number:"))
print('Sum of odd Numbers:',sum_odd(n))