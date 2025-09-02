####WAP to Swap to Variables Without Using Third Variable....

X = int(input("Enter 1st no:"))
Y = int(input("Enter 2nd no:"))

print(f'Before Swapping Variables X={X}, Y={Y}')

X = X + Y
Y = X - Y
X = X - Y

print(f'After Swapping Variables X={X}, Y={Y}')