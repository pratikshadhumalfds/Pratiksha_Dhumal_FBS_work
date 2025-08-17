###WAP to take input 5 subject marks from user and display grade(e.g. First Class, Second Class...)

Marathi = int(input("Enter the marks of Marathi:"))
English = int(input("Enter the marks of English:"))
Maths = int(input("Enter the marks of Maths:"))
Science = int(input("Enter the marks of Science:"))
Geography = int(input("Enter the marks of Geography:"))

gain_marks = Marathi + English + Maths + Science + Geography

Percentage = (gain_marks / 500) * 100

if Percentage>=80:
    print(f'Distinction...')
elif Percentage>=70 and Percentage<=80:
    print(f'First Class...')
elif Percentage>=60 and Percentage<=70:
    print(f'Second Class...')    
elif Percentage>=50 and Percentage<=60:
    print(f'Third Class...')
elif Percentage>=40 and Percentage<=50:
    print(f'Pass Class...')
else:
    print(f'fail')    

print(f'Percentage of all subjects is {Percentage}%')