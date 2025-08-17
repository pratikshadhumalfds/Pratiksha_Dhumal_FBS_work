num=int(input("enter number of passengers: "))
cost=int(input("enter per ticket cost: "))
total_amt=0
for i in range(1,num+1):
    age=int(input(f"accept age of pasenger{i}: "))
    if(age<12):
        dis=cost*0.70
    elif(age>59):
        dis=cost*0.50
    else:
        dis=cost
    total_amt=total_amt+dis
    print(f"passenger {i} ticket price={dis}")
    
print(f"total amount for all passenger: {total_amt}") 