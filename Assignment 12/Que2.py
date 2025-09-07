##python program to remove nth index character from a Non-Empty string.

str = "we all are indians"
n = 13

string = str[:n] + str[n+1:]

print("Original string:", str)
print("After removing index", n, ":", string)
