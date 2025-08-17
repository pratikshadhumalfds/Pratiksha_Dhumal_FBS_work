def is_leap (year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
year=int(input("Enter the year:"))
if is_leap(year):
    print(year,"Is a Leap Year")
else:
    print(year,"Not a Leap Year")    
