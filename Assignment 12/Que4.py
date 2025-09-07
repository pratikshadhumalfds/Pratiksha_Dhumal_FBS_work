###python program to form a new string where the first and last character have been changed

str = 'You are my best friend'
string = str[-1] + str[1:-1] + str[0]
print('str:', str)            
print('string:', string)       #changed string.