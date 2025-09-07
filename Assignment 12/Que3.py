### python program to detect if two strings are anagrams

###Method 1st

str1 = "listen"
str2 = "finish"

dict1 = {}
for char in str1:
    if char not in dict1:
        dict1[char] = 1

dict2 = {}
for char in str2:
    if char in dict1:
        dict2[char] = 0       #adhich str1 madhe aahe mahanun 0.
    else:
        dict2[char] = -1       #naveen letter je str1 madhe nhiye pn str2 madhe aahe.

print("first string:", dict1)
print("second string:", dict2)

if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


### Method 2nd 






