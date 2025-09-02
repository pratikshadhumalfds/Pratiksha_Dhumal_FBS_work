####WAP to Swap to Variables Without Using Third Variable....(Advance technique)

X = int(input("Enter 1st no:"))
Y = int(input("Enter 2nd no:"))

print(f'Before Swapping Variables X={X}, Y={Y}')

X,Y = Y,X

print(f'After Swapping Variables X={X}, Y={Y}')