###python program to multiply all the items in a dictionary... 

dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

result = 1
for value in dict.values():
    result *= value

print('Multiplcation of all items in a dict:', result)