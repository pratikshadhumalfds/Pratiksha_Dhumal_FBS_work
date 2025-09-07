###python program to count the occurances of each word in a string...

str = 'This is a apple. This is a banana.'

words = str.split()

dict = {}        #dict for storing word count.

for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

for word, count in dict.items():
    print(word, ":", count)



