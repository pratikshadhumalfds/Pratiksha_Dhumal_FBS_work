num=int(input("enter the number: "))
sum=0
temp=num
i=1
while(i<=num//2):
    if(num%i==0):
        sum=sum+i
    i=i+1
if(temp==sum):
    print(f"{num} is perfect number")
else:
    print(f"{num} is not perfect number")