###python program to count the number of vowels in a string..

str = 'My Name is Pratiksha Dhumal'
count = 0
vowels = 'a' , 'e' , 'i' ,'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U'

for char in str:
    if char in vowels:
        count += 1
print('Total_number_of_vowels:', count)