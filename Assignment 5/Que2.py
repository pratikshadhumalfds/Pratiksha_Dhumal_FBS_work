num=int(input("enter number of students: "))

# sub1=int(input("enter marks of subject1: "))
# sub2=int(input("enter marks of subject2: "))
# sub3=int(input("enter marks of subject3: "))
# sub4=int(input("enter marks of subject4: "))
# sub5=int(input("enter marks of subject5: "))


sum=0
for i in range(1,num+1):
    print(f"enter marks of student {i}: ")
    total_marks=0
    for sub in range(1,6):
        marks=int(input(f"subject {sub} marks: "))
        total_marks=total_marks+marks
    percentage=(total_marks/500)*100
    sum=sum+percentage
    print(f"percentage of students: {percentage}") 
avg=sum/num
print(f"average percentage of student: {avg}")   