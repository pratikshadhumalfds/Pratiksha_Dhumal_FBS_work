###WAP to check angle of triangle is valid or not...

angle1 = int(input("Enter the angle1:"))
angle2 = int(input("Enter the angle2:"))
angle3 = int(input("Enter the angle3:"))

if(angle1 + angle2 + angle3 == 180):
    print(f'Triangle is valid')
else:
    print(f'Triangle is not valid')    
