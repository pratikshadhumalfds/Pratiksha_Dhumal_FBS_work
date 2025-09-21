###Write a Python program to find the longest common prefix of all strings. Use the Python set.

words = ["flower", "flow", "flight"]

prefix = ""
for chars in zip(*words):
    if len(set(chars)) == 1:
        prefix += chars[0]
    else:
        break

print("Longest Common Prefix:", prefix)
