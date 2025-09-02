###WAP to input two angles from user to find third angle of the triangle.

Angle1 = int(input("Enter first angle:"))
Angle2 = int(input("Enter second angle:"))

Angle3 = 180 -(Angle1 + Angle2)  ###180 = angle1 + angle2 +angle3 

print(f'Angle3 is {Angle3}')