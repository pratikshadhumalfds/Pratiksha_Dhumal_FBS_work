####WAP to check wheather

side1 = int(input("Enter the angle1:"))
side2 = int(input("Enter the angle2:"))        ####(side or angle ghetla tari chalel)
side3 = int(input("Enter the angle3:"))

if(side1==side2)and(side2==side3)and(side3==side1):
    print(f'Angle is Equilateral')
elif(side1==side2):
    print(f'Angle is Isoscales')
else:                                          ###(side1!=side2)and(side2!=side3)and(side3!=side1)
    print(f'Angle is Scalene')


