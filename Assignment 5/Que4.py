num=int(input("enter the number: "))
temp=num
count=0
while(temp>0):
    digit=temp%10
    count=count+1
    temp=temp//10
temp=num
sum=0
while(temp>0):
    digit=temp%10
    sum=sum+digit**count
    temp=temp//10
   

if(sum==num):
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")