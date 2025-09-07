###python program to take in two strings and display the larger string without using built-in functions..

str1 = 'I am Dhumal Pratiksha'
str2 = 'I am Dhumal Krishna'

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

len1 = string_length(str1)
len2 = string_length(str2)

if len1 > len2:
    print("Larger string is:", str1)
elif len2 > len1:
    print("Larger string is:", str2)
else:
    print("Both strings are of equal length.")
