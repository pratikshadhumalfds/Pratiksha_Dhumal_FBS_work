###WAP to check if user has entered correct userid and password...

userid = input("Enter the User name:")
password = int(input("Enter the Password:"))

login_userid = "Pratiksha_Dhumal"
login_password = 8080610358

if((login_userid == userid) and (login_password == password)):
    print(f'{userid} and {password} is entered correct userid and password')
else:
    print(f'{userid} and {password} is not correct')    