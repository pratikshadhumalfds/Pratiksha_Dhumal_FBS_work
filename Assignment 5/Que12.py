x=int(input("enter value of x:"))
num=int(input("enter number os terms: "))

i=1
denominator=1
sum=0
while(i<=num):
    term=(x**i)/denominator
    if(i%2==0):
        sum=sum-term
    else:
        sum=sum+term
    i=i+1
    denominator=denominator+2
print(sum)
    