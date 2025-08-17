correct_password='pratiksha@123'
correct_uid='dhumalpratiksha'
for i in range(1,4):
    password=input("enter valid passowrd: ")
    userid=input("enter valid userid: ")
    if userid==correct_uid and password==correct_password:
        print("login successful")
        break
    else:
        print("incorrect credentials")
else:
    print("program terminated")