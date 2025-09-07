###python program to find larger string without using bulid-in functions.

def get_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

str1 = 'we are indians'
str2 = 'India is my country'

len1 = get_length(str1)
len2 = get_length(str2)

if len1 > len2:
    print("Larger string is:", str1)
elif len2 > len1:
    print("Larger string is:", str2)
else:
    print("Both strings are of equal length.")
