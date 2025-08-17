def is_armstrong(n):
    digits=str(n)
    power=len(digits)
    total=0
    for d in digits:
        total+=int(d)**power
    return total == n

n=int(input("Enter the Number:"))
if is_armstrong(n):
    print("Is a Armstrong Number")
else:
    print("Is Not a Armstrong Number:")
       


       ####153,370,371,407,1634,8208,9474 are armstrong numbers...