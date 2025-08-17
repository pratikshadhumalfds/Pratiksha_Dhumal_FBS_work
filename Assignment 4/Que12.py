num=int(input("enter the number: "))
for i in range(1,num+1):
    temp=i
    count=0
    while(temp>0):
        digit=temp%10
        count=count+1
        temp=temp//10
    temp=i
    res=0
    while(temp>0):
        digit=temp%10
        res=res+digit**count
        temp=temp//10
    if(res==i):
        print(i)