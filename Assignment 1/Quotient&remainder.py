###WAP to calculate Quoitent & Remainder of two numbers...

numerator = int(input("Enter the 1st no:"))
denominator= int(input("Enter the 2nd no:"))

if denominator == 0:
    print("Error: division by zero is not allowed.")
else:
    quotient = numerator // denominator
    remainder = numerator % denominator

    print(f"quotient: {quotient}")
    print(f"remainder: {remainder}")