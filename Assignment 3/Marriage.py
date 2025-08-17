###WAP to check person is eligible to marry or not(male age>=21 and female age>=18)

Age = int(input("Enter the Person Age:"))

if Age>=21 and Age>=18:
    print(f'Eligible for Marriage...')
else:
    print(f'Not Eligible for Marriage...')  


###For ladies...

if Age>=18:
    print(f'Eligible for Marriage...')
else:
    print(f'Not Eligible for Marriage...')

###For Gents...

if Age>=21:
    print(f'Eligible for Marriage...')
else:
    print(f'Not Eligible for Marriage...')