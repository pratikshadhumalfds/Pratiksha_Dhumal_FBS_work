###WAP to calculate percentage of 5 subjects...

Marathi = int(input("Enter the marks of Marathi:"))
English = int(input("Enter the marks of English:"))
Maths = int(input("Enter the marks of Maths:"))
Science = int(input("Enter the marks of Science:"))
Geography = int(input("Enter the marks of Geography:"))

gain_marks = Marathi + English + Maths + Science + Geography

Percentage = (gain_marks / 500) * 100

print(f'Percentage of all subjects is {Percentage}%')