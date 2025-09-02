###Calculate Minimum Numbers Of Notes...
###WAP to to accept an interger amount from user and tell minimum number of notes for representing that amount...

Amt = int(input("Enter Amount:"))

temp = Amt

Two_Thousand =  temp // 2000
temp = temp % 2000

Five_Hundred = temp // 500
temp = temp % 500

Two_Hundred = temp // 200
temp = temp % 200

Hundred = temp // 100
temp = temp % 100

fifty = temp // 50
temp = temp % 50

twenty = temp // 20
temp = temp % 20

ten = temp // 10
temp = temp % 10

Total_Notes = Two_Thousand + Five_Hundred + Two_Hundred + fifty + twenty +ten
print(f'Total No. Of Notes: {Total_Notes}')
print(f'Total No. Of Notes: Two_Thousand {Two_Thousand}Notes, Five_Hundred {Five_Hundred}Notes, Two_Hundred {Two_Hundred}Notes, fifty {fifty}Notes, twenty {twenty}Notes, ten {ten}Notes')






