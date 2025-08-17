###WAP to prompt user to enter userid and password . after verifying userid and 
# password display a 4 digit random number and ask user to enter the same. if user enters the same number 
# then show him success message otherwise failed.(something like captcha)...

userid = input("Enter the User name:")
password = int(input("Enter the Password:"))

import random
captcha = random.randint(1111,9999)

print(f'Captcha: {captcha}')

user_captcha = int(input("Enter the captcha again: "))

if(("Pratiksha_Dhumal"== userid) and (8080610358 == password)):       ##print(f'incorrect userid and password')
    if(user_captcha == captcha):
        print(f'Success..!!! Access granted')
    else:
        print(f'Captcha is Wrong...')   


      