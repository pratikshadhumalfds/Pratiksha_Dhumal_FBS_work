###WAP to input angles of a triangle and check whether triangle is valid or not...

side1 = int(input("Enter the side1:"))
side2 = int(input("Enter the side2:"))
side3 = int(input("Enter the side3:"))

if(side1+side2>side3)and(side2+side3>side1)and(side3+side1>side2): 
    print(f'Triangle is valid')
else:
    print(f'Triangle is not valid')



#### two angle addition 3rd angle peksha mothich asli pahije tar to angle valid asto.