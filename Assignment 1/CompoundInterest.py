###WAP to enter P,T,R and calculate compound interest...

P=int(input("Enter the number 1:"))
R=int(input("Enter the number 2:"))
T=int(input("Enter the number 3:"))

Compound_interest = (P*(1+ (R/100)) *T)- P 

print(f'Compound interest is {Compound_interest}')