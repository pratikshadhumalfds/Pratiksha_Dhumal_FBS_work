num=int(input("enter the number: "))
temp=num
sum=0
while(temp>0):
    digit=temp%10
    temp=temp//10
    fact=1
    i=1
    while(i<=digit):
        fact=fact*i
        i=i+1
    sum=sum+fact
if(sum==num):
    print(f"{num} is strong number")
else:
    print(f"{num} is not strong number")