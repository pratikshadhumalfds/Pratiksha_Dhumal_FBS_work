num = int(input("Enter a three-digit number: "))


if 100 <= num <= 999:
    
    reversed_num = int(str(num)[::-1])
    print("Reversed number:", reversed_num)
else:
    print("Please enter a valid three-digit number.")