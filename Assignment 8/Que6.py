def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(b,end=' ')
        a, b = b, a+b

n=int(input("Enter the number of Terms:"))
print('Fibonacci series:', fibonacci(n))       