###WAP to calculate total salary of employee based on basic, da=10% basic, ta=12% of basic, hra=15% of basic....

Amt = int(input("Enter the Amount of Salary:"))

Da = (Amt*10)/100   ##10%
Ta = (Amt*12)/100   ##12%
Hra = (Amt*15)/100   ##15%

Total_Salary = Da + Ta + Hra + Amt 

print(f'Total_Salary is {Total_Salary}')